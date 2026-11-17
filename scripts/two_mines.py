"""Compare continued recorded coal production across the 2019 US excise-tax change."""

import argparse

import numpy as np
import pandas as pd
import xlrd

from data import Context, NeedsData, sha256, write_json

URL = "https://www.eia.gov/coal/data/public/xls/coalpublic{}.xls"
HASHES = {
    2015: "48dce35a2e20ba024a80d1dce4dddacf4593f37cc2a728fad5305d55be40a84a",
    2016: "fa40f0a99cc0e17541d6f62bda56687e6b5120288c9ee6bf405df5e19804277c",
    2017: "cea3e879db15efa6525df6cb8744e2baf635c55bba140b7d3c228e61a89dcc0b",
    2018: "28b02163a18c595d7ec77a80c2f7bedbecf5fee9122906340c3a60fad5918211",
    2019: "c0d98010a1abe683f50df5d722b5a080cb0a6700b55566a2da3632857c0b52ac",
}
COLUMNS = {"Year": "year", "MSHA ID": "mine_id", "Mine State": "state", "Mine County": "county",
           "Mine Status": "status", "Mine Type": "method", "Coal Supply Region": "region",
           "Production (short tons)": "tons"}
METHODS = ["Underground", "Surface"]
REGIONS = ["Appalachia Central", "Appalachia Northern", "Appalachia Southern"]


def load_years(ctx):
    frames = []
    for year, digest in HASHES.items():
        path = ctx.public(f"EIA_coalpublic{year}.xls", URL.format(year), "xls")
        if sha256(path) != digest:
            raise ValueError(f"The {year} workbook differs from the recorded edition")
        sheet = xlrd.open_workbook(str(path)).sheet_by_name("Hist_Coal_Prod")
        header = sheet.row_values(3)
        rows = [sheet.row_values(i) for i in range(4, sheet.nrows)]
        frame = pd.DataFrame(rows, columns=header)[list(COLUMNS)].rename(columns=COLUMNS)
        if not frame.year.eq(year).all() or frame.tons.min() < 0 or frame.duplicated(["mine_id", "method"]).any():
            raise ValueError(f"Unexpected year, tonnage or repeated mine-method in {year}")
        if not (frame.mine_id.gt(0) & frame.mine_id.mod(1).eq(0)).all():
            raise ValueError(f"Invalid MSHA identifier in {year}")
        frames.append(frame.astype({"year": int, "mine_id": int}))
    return pd.concat(frames, ignore_index=True)


def baseline_mines(raw, *, require_active=True):
    positive = raw.loc[raw.method.isin(METHODS) & raw.tons.gt(0)]
    # Some IDs have both extraction methods, or a zero-ton surface support unit.
    single = positive.loc[~positive.duplicated(["year", "mine_id"], keep=False)]
    eligible = single.region.isin(REGIONS) & single.state.ne("Pennsylvania (Anthracite)")
    if require_active:
        eligible &= single.status.eq("Active")
    return single.loc[eligible, ["year", "mine_id", "state", "county", "method", "tons"]].copy()


def recorded_outcomes(raw):
    # Every reporting ID gets a row. A zero and an absent report remain distinguishable.
    all_ids = raw.assign(reported_tons=raw.tons.where(raw.method.isin(METHODS), 0))
    return all_ids.groupby(["year", "mine_id"], as_index=False).reported_tons.sum()


def follow_cohorts(raw, *, require_active=True):
    followup = recorded_outcomes(raw)
    followup["year"] -= 1
    base = baseline_mines(raw, require_active=require_active)
    base = base.loc[base.year.lt(max(HASHES))]
    panel = base.merge(followup, how="left", on=["mine_id", "year"], validate="one_to_one")
    panel["continued"] = panel.reported_tons.gt(0)
    panel["explicit_zero"] = panel.reported_tons.eq(0)
    panel["missing_report"] = panel.reported_tons.isna()
    panel["size_band"] = np.where(panel.tons.lt(100_000), "below_100k", "at_least_100k")
    return panel


def compare(panel, strata):
    """Hold the same local comparisons and their weights fixed over all four transitions."""
    group = strata + ["year", "method"]
    cells = panel.groupby(group).agg(mines=("mine_id", "size"), positive=("continued", "sum"),
                                     zero=("explicit_zero", "sum"), missing=("missing_report", "sum"))
    coverage = cells.groupby(strata).size()
    common = coverage.index[coverage.eq((len(HASHES) - 1) * len(METHODS))]
    cells = cells.reset_index().merge(common.to_frame(index=False), on=strata, validate="many_to_one")
    if cells.empty:
        return {"common_strata": 0, "status": "no_common_support"}
    cells["rate"] = 100 * cells.positive / cells.mines
    rates = cells.groupby(["year", "method"]).rate.mean().unstack("method")
    gaps = rates.Underground - rates.Surface
    # Bound actual continuation without assuming that a missing mine closed.
    cells["upper"] = 100 * (cells.positive + cells.missing) / cells.mines
    upper = cells.groupby(["year", "method"]).upper.mean().unstack("method")
    gap_low = rates.Underground - upper.Surface
    gap_high = upper.Underground - rates.Surface
    county_gaps = cells.pivot(index=strata, columns=["year", "method"], values="rate")
    area_changes = ((county_gaps[2018].Underground - county_gaps[2018].Surface)
                    - (county_gaps[2017].Underground - county_gaps[2017].Surface))
    yearly = []
    for year, rate in rates.iterrows():
        entry = {"baseline": int(year), "followup": int(year + 1),
                 "underground_minus_surface_pp": round(gaps[year], 5)}
        for method in METHODS:
            counts = cells.loc[cells.year.eq(year) & cells.method.eq(method), ["mines", "positive", "zero", "missing"]].sum()
            entry[method.lower()] = {"equal_stratum_continuation_pct": round(rate[method], 5),
                                     **{k: int(v) for k, v in counts.items()}}
        yearly.append(entry)
    report = {"common_strata": len(common), "rates": yearly,
              "2019_change_in_gap_missing_outcome_bounds_pp": [
                  round(gap_low[2018] - gap_high[2017], 5), round(gap_high[2018] - gap_low[2017], 5)],
              "change_in_gap_pp": {f"{y}_vs_{y-1}_followup": round(gaps[y-1] - gaps[y-2], 5)
                                   for y in range(2017, 2020)}}
    if len(common) > 1:
        leave_one_out = (area_changes.sum() - area_changes) / (len(common) - 1)
        report["leave_one_stratum_out_2019_contrast_range_pp"] = [round(leave_one_out.min(), 5), round(leave_one_out.max(), 5)]
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true", help="download missing verified source workbooks")
    args = parser.parse_args()
    ctx = Context(fetch=args.fetch)
    try:
        raw = load_years(ctx)
    except NeedsData as exc:
        parser.exit(1, f"{exc}\n")
    panel = follow_cohorts(raw)
    result = {
        "status": "differential_policy_exposure_comparison",
        "cohort": "Prior-year active, positive, single-method extraction in bituminous Appalachian areas; excludes Pennsylvania anthracite. Unit is MSHA mine ID.",
        "outcome": "Any positive reported underground or surface production under the same ID in the following calendar year. Missing and reported zero are separately counted.",
        "exposure": "2019 federal excise relief on taxable domestic sales; underground and surface both receive relief. Group denotes prior-year extraction method, not tax paid or retained cash.",
        "primary_weighting": "Within county each mine counts once; equal weight across state/county labels containing both methods in all four baseline cohorts.",
        "source_files": [{"year": year, "url": URL.format(year), "sha256": digest} for year, digest in HASHES.items()],
        "primary": compare(panel, ["state", "county"]),
        "size_sensitivity": compare(panel, ["state", "county", "size_band"]),
        "all_producing_statuses_sensitivity": compare(follow_cohorts(raw, require_active=False), ["state", "county"]),
        "size_weighting": "Equal county-size-cell weight, requiring both methods in all four cohorts; two bands split at 100,000 baseline short tons.",
        "coverage_before_common_support": panel.groupby("year").size().to_dict(),
        "identification": "National policy, nonrandom methods, uncertain incidence and taxability, changing export and power demand. Two earlier gap changes and leave-one-area-out range are diagnostics. No policy-level standard error.",
    }
    write_json(ctx.output / "two_mines.json", result)
    print("2019 change in continuation gap (percentage points):", result["primary"]["change_in_gap_pp"]["2019_vs_2018_followup"])


if __name__ == "__main__":
    main()
