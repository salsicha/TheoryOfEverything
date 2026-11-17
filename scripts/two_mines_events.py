"""Follow reported MSHA inundation and hoisting incidents into the next quarter.

Download the two archives listed in SOURCES from the MSHA Open Government portal,
then pass their paths with --accidents and --production. The files exceed the
general research downloader's size limit. --fetch retrieves missing annual EIA
workbooks used to establish the producing cohorts.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZipFile

import pandas as pd

from data import Context, sha256, write_json
from two_mines import METHODS, baseline_mines, load_years

BASE = "https://arlweb.msha.gov/OpenGovernmentData/DataSets/"
SOURCES = {
    "Accidents": BASE + "Accidents.zip",
    "MinesProdQuarterly": BASE + "MinesProdQuarterly.zip",
}
TYPES = {"04": "inundation", "11": "hoist_damage"}
KEY = ["mine_id", "year", "quarter"]


def read_coal(path, table, fields):
    cols = ["MINE_ID", "CAL_YR", "CAL_QTR", "COAL_METAL_IND", *fields]
    with ZipFile(path) as archive, archive.open(table + ".txt") as source:
        chunks = pd.read_csv(
            source, sep="|", encoding="latin1", chunksize=100_000, usecols=cols,
            dtype={"IMMED_NOTIFY_CD": str, "DOCUMENT_NO": str},
        )
        selected = []
        for chunk in chunks:
            keep = chunk.CAL_YR.between(2016, 2019) & chunk.COAL_METAL_IND.eq("C")
            if table == "Accidents":
                keep &= chunk.IMMED_NOTIFY_CD.isin(TYPES)
            selected.append(chunk.loc[keep])
    return pd.concat(selected, ignore_index=True).rename(
        columns={"MINE_ID": "mine_id", "CAL_YR": "year", "CAL_QTR": "quarter"}
    )


def event_panel(baseline, accidents, production):
    # Keep Q4 out: a following quarter in the next policy year changes exposure.
    incidents = accidents.loc[accidents.year.between(2017, 2019) & accidents.quarter.le(3)].copy()
    if incidents.DOCUMENT_NO.duplicated().any():
        raise ValueError("Repeated MSHA document number")
    if production.duplicated([*KEY, "SUBUNIT_CD"]).any() or production.COAL_PRODUCTION.lt(0).any():
        raise ValueError("Unexpected negative production or repeated subunit-quarter")
    # Multiple workers, documents or episodes can share one mine's quarterly output.
    incidents["inundation_reports"] = incidents.IMMED_NOTIFY_CD.eq("04").astype(int)
    incidents["hoist_damage_reports"] = incidents.IMMED_NOTIFY_CD.eq("11").astype(int)
    counts = incidents.groupby(KEY, as_index=False)[["inundation_reports", "hoist_damage_reports"]].sum()
    cohort = baseline[["year", "mine_id", "method", "state"]].copy()
    cohort["year"] += 1
    events = counts.merge(cohort, on=["year", "mine_id"], validate="many_to_one")
    output = production.groupby(KEY).COAL_PRODUCTION.sum(min_count=1).reset_index()
    output["ordinal"] = output.year * 4 + output.quarter
    series = output.set_index(["mine_id", "ordinal"]).COAL_PRODUCTION
    for label, offset in (("preceding_tons", -1), ("incident_tons", 0), ("following_tons", 1)):
        index = pd.MultiIndex.from_arrays([events.mine_id, events.year * 4 + events.quarter + offset])
        events[label] = series.reindex(index).to_numpy()
    return counts, events


def summarize(events):
    by_method = {}
    for method in METHODS:
        baseline = events.loc[events.method.eq(method)]
        eligible = baseline.loc[baseline.preceding_tons.gt(0)]
        by_method[method] = {
            "baseline_eligible_incident_quarters": len(baseline),
            "without_confirmed_positive_preceding_quarter": len(baseline) - len(eligible),
            "incident_quarters": len(eligible), "distinct_mines": int(eligible.mine_id.nunique()),
            "inundation_reports": int(eligible.inundation_reports.sum()),
            "hoist_damage_reports": int(eligible.hoist_damage_reports.sum()),
            "positive_during_quarter": int(eligible.incident_tons.gt(0).sum()),
            "explicit_zero_during_quarter": int(eligible.incident_tons.eq(0).sum()),
            "unknown_during_quarter": int(eligible.incident_tons.isna().sum()),
            "positive_following_quarter": int(eligible.following_tons.gt(0).sum()),
            "explicit_zero_following_quarter": int(eligible.following_tons.eq(0).sum()),
            "unknown_following_quarter": int(eligible.following_tons.isna().sum()),
        }
    return by_method


def run(ctx, accidents_path, production_path):
    baseline = baseline_mines(load_years(ctx))
    accidents = read_coal(accidents_path, "Accidents", ["IMMED_NOTIFY_CD", "DOCUMENT_NO"])
    production = read_coal(production_path, "MinesProdQuarterly", ["SUBUNIT_CD", "COAL_PRODUCTION"])
    national, events = event_panel(baseline, accidents, production)
    yearly = {}
    for year in (2017, 2018, 2019):
        national_cases = national.loc[national.year.eq(year)]
        annual = events.loc[events.year.eq(year)]
        groups = summarize(annual)
        eligible = annual.loc[annual.preceding_tons.gt(0)]
        overlap = eligible.groupby("state").method.nunique()
        yearly[year] = {
            "national_coal_report_counts_before_cohort_linkage": {
                k: int(national_cases[k].sum()) for k in ["inundation_reports", "hoist_damage_reports"]
            },
            "national_coal_incident_quarters_before_cohort_linkage": len(national_cases),
            "matched_appalachian_producers": groups,
            "areas_with_both_methods": sorted(overlap.index[overlap.eq(2)].tolist()),
        }
    files = [("Accidents", accidents_path), ("MinesProdQuarterly", production_path)]
    sources = [{"file": name + ".zip", "source_url": SOURCES[name], "sha256": sha256(path),
                "bytes": path.stat().st_size} for name, path in files]
    linked = events.sort_values(KEY).astype(object)
    linked = linked.where(linked.notna(), None)
    return {
        "question": "Did previously producing Appalachian mines with a reported inundation or serious hoist incident record positive output in the following quarter?",
        "event_definition": "MSHA immediate-notification field, code 04 for unplanned liquid or gas inundation, code 11 for shaft/slope hoist damage endangering a person or interfering with the equipment for over 30 minutes. Counts of reports and of unique mine-quarters are separate. Coverage includes reports by operators and contractors.",
        "law": "https://www.ecfr.gov/current/title-30/chapter-I/subchapter-H/part-50/section-50.2",
        "cohort": "Use prior-year active Appalachian producers with one positive baseline extraction method as in the main coal analysis. Then require positive total mine output in the quarter immediately before a Q1, Q2 or Q3 event. Follow-up remains in the same policy year. The year 2017 provides an earlier comparison, 2018 precedes the tax cut, and 2019 is the tax-cut year.",
        "outcome": "Coal short tons reported by mine operators, summed across subunits by MSHA ID. Missing or all-blank values remain unknown. Quarter totals cannot distinguish a short shutdown and repair from uninterrupted mine production.",
        "limits": "The event code specifies a reportable incident. It does not establish whole-mine stoppage, water specifically, a broken pump, identical severity, the source of repair finance, or whether the equipment was put back in service. Exposure and likelihood of these incident types can vary with method. Empty comparison groups supply no effect estimate.",
        "years": yearly,
        "linked_incident_quarters": linked.to_dict(orient="records"),
        "provenance": sources + ctx.provenance,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--accidents", type=Path, required=True, help="Official MSHA Accidents.zip")
    parser.add_argument("--production", type=Path, required=True, help="Official MSHA MinesProdQuarterly.zip")
    parser.add_argument("--fetch", action="store_true", help="Fetch missing baseline EIA workbooks")
    parser.add_argument("--cache", type=Path, help="Directory for baseline EIA workbooks")
    parser.add_argument("--output", type=Path, help="Directory for the result")
    args = parser.parse_args()
    ctx = Context(fetch=args.fetch, cache=args.cache, output=args.output)
    report = run(ctx, args.accidents, args.production)
    write_json(ctx.output / "two_mines_events.json", report)
    for year, entry in report["years"].items():
        print(year, {m: g["incident_quarters"] for m, g in entry["matched_appalachian_producers"].items()})


if __name__ == "__main__":
    main()
