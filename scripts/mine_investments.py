"""Forecast mine investments from assessment inputs and compare with later responses."""
import argparse
import csv
import math
from collections import Counter, defaultdict
from io import BytesIO
from itertools import combinations
from pathlib import Path
from statistics import mean
from zipfile import ZipFile

from openpyxl import load_workbook

from data import sha256, write_json


BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / "research" / "mine-investments"
RESULTS = BASE / "scripts" / "results"
SNAPSHOT = "f7bf6464c4347f7a603bb0b4dba81845e91d15d440a4a72a78ac5e300d78f54c"
FROZEN_FORECAST = "8dede1157ab035d64dbe2785ba17bd0b6c9abef4e7f667e420e048ab9fa5f38e"
RESPONSES = {"I": "adopt", "N": "retain", "P": "unresolved", "K": "unresolved", "": "unresolved"}
SITE_FIELDS = ["ID", "FY", "STATE", "SIC", "NAICS", "PRODUCTS"]
RESOURCE_FIELDS = [part + field for part in "PSTQ"
                   for field in ("SOURCCODE", "CONSERVED", "SAVED")]
OFFER_FIELDS = ["SUPERID", "ID", "AR_NUMBER", "ARC2", "IC_CAPITAL", "IC_OTHER", *RESOURCE_FIELDS]
FORECAST_FIELDS = ["SUPERID", "ID", "sample", "reason", "annual_kwh", "annual_dollars",
                   "outlay_dollars", "npv_5y_dollars", "simple_payback_years",
                   "delta_operating_w_per_k", "five_year_offset_kwh",
                   "profit_5y", "profit_2y", "operating_mep", "district_mep"]


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    with temporary.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def columns(sheet, fields):
    rows = iter(sheet.values)
    header = next(rows)
    positions = [header.index(field) for field in fields]
    for row in rows:
        yield {field: row[i] for field, i in zip(fields, positions)}


def in_cohort(site):
    naics = str(site["NAICS"] or "")
    sic = str(site["SIC"] or "")
    return (site["FY"] is not None and int(site["FY"]) <= 2024
            and (naics.startswith("212") or (not naics and sic[:2] in {"10", "12", "14"})))


def keyed(rows, key):
    result = {}
    for row in rows:
        value = row[key]
        if not value or value in result:
            raise ValueError(f"Missing or duplicate {key}: {value}")
        result[value] = row
    return result


def open_snapshot(archive):
    if sha256(archive) != SNAPSHOT:
        raise ValueError("Workbook archive differs from the frozen snapshot; use the tracked extracts.")
    with ZipFile(archive) as outer:
        name, = [entry for entry in outer.namelist() if entry.endswith(".xlsx")]
        return load_workbook(BytesIO(outer.read(name)), read_only=True, data_only=True)


def extract_inputs(archive, folder):
    book = open_snapshot(archive)
    try:
        sites = keyed((s for s in columns(book["ASSESS"], SITE_FIELDS) if in_cohort(s)), "ID")
        offers = keyed((r for r in columns(book["RECC"], OFFER_FIELDS) if r["ID"] in sites),
                       "SUPERID")
    finally:
        book.close()
    write_csv(folder / "assessments.csv", SITE_FIELDS, [sites[k] for k in sorted(sites)])
    write_csv(folder / "recommendations.csv", OFFER_FIELDS, [offers[k] for k in sorted(offers)])
    print(f"Extracted {len(sites)} assessments and {len(offers)} offers without outcome fields.")


def number(value):
    if value is None or value == "":
        return None
    n = float(value)
    if not math.isfinite(n):
        raise ValueError(f"Nonfinite input: {value}")
    return n


def choice(value):
    if abs(value) < 1e-7:
        return "tie"
    return "adopt" if value > 0 else "retain"


def forecast_offer(offer):
    result = {"SUPERID": offer["SUPERID"], "ID": offer["ID"], "sample": "excluded",
              "district_mep": "undetermined"}
    if not str(offer["ARC2"]).startswith("2."):
        return dict(result, reason="outside energy category")
    savings = 0.0
    kwh = 0.0
    for prefix in "PSTQ":
        resource = offer[prefix + "SOURCCODE"]
        if not resource:
            continue
        if resource not in {"EC", "ED", "EF"}:
            return dict(result, reason="other resource or substitution")
        dollars = number(offer[prefix + "SAVED"])
        if dollars is None:
            return dict(result, reason="missing resource dollar estimate")
        savings += dollars
        if resource == "EC":
            energy = number(offer[prefix + "CONSERVED"])
            if energy is None:
                return dict(result, reason="missing site kWh")
            kwh += energy
    if kwh <= 0:
        return dict(result, reason="no positive site kWh saving")
    capital = number(offer["IC_CAPITAL"])
    other = number(offer["IC_OTHER"])
    if capital is None and other is None:
        return dict(result, reason="no recommendation cost components")
    given = [v for v in (capital, other) if v is not None]
    cost = sum(given)
    if min(given) < 0 or cost <= 0:
        return dict(result, reason="no positive investment or negative component")
    npv = savings * sum(1 / 1.10**year for year in range(1, 6)) - cost
    result.update(sample="primary" if len(given) == 2 else "one_component",
                  reason="", annual_kwh=kwh, annual_dollars=round(savings, 2),
                  outlay_dollars=round(cost, 2), npv_5y_dollars=round(npv, 2),
                  simple_payback_years=round(cost / savings, 5) if savings > 0 else "",
                  delta_operating_w_per_k=round(-1000 * kwh / (8760 * 293.15), 6),
                  five_year_offset_kwh=5 * kwh, profit_5y=choice(npv),
                  profit_2y=choice(2 * savings - cost), operating_mep="retain")
    return result


def forecast(folder, results):
    sites = keyed(read_csv(folder / "assessments.csv"), "ID")
    offers = keyed(read_csv(folder / "recommendations.csv"), "SUPERID")
    if set(r["ID"] for r in offers.values()) - set(sites):
        raise ValueError("Recommendation without an assessment")
    forecasts = [forecast_offer(offers[k]) for k in sorted(offers)]
    write_csv(results / "mine_investment_forecasts.csv", FORECAST_FIELDS, forecasts)
    primary = [r for r in forecasts if r["sample"] == "primary"]
    print(f"{len(primary)} primary decisions; "
          f"{sum(r['profit_5y'] == 'adopt' for r in primary)} opposing predictions.")


def extract_outcomes(archive, folder):
    offers = keyed(read_csv(folder / "recommendations.csv"), "SUPERID")
    book = open_snapshot(archive)
    try:
        fields = ["SUPERID", "IMPSTATUS"]
        responses = keyed((r for r in columns(book["RECC"], fields) if r["SUPERID"] in offers),
                          "SUPERID")
    finally:
        book.close()
    if responses.keys() != offers.keys():
        raise ValueError("Outcome extract must include every frozen recommendation, including blanks")
    write_csv(folder / "responses.csv", fields, [responses[k] for k in sorted(responses)])
    print(f"Extracted follow-up fields for {len(responses)} frozen recommendations.")


def compare(rows, rule):
    disagreements = [r for r in rows if r[rule] in ("adopt", "retain")
                     and r[rule] != r["operating_mep"]]
    scored = [r for r in disagreements if r["response"] != "unresolved"]
    by_site = defaultdict(list)
    for r in scored:
        by_site[r["ID"]].append(r[rule] == r["response"])
    profit_hits = sum(sum(hits) for hits in by_site.values())
    n = len(scored)
    total = len(disagreements)
    missing = total - n
    site_means = [mean(values) for values in by_site.values()]
    # Leave one whole assessment out, retaining recommendation weights in each remaining sample.
    leave_one_out = [(profit_hits - sum(values)) / (n - len(values))
                     for values in by_site.values() if len(values) < n]
    return {
        "available_investments": len(rows), "disagreements": total,
        "agreements": sum(r[rule] == r["operating_mep"] for r in rows),
        "financial_ties": sum(r[rule] == "tie" for r in rows),
        "scored_disagreements": n, "assessments_scored": len(by_site),
        "disagreement_statuses": dict(sorted(Counter(r["status"] or "blank" for r in disagreements).items())),
        "profit_hits": profit_hits, "operating_mep_hits": n - profit_hits,
        "always_retain_hits": sum(r["response"] == "retain" for r in scored),
        "always_adopt_hits": sum(r["response"] == "adopt" for r in scored),
        "profit_share_known": round(profit_hits / n, 6) if n else None,
        "profit_share_equal_assessments": round(mean(site_means), 6) if site_means else None,
        "profit_share_leave_one_assessment_out": (
            [round(min(leave_one_out), 6), round(max(leave_one_out), 6)] if leave_one_out else None),
        "profit_hits_bounds_including_unresolved": [profit_hits, profit_hits + missing],
        "operating_mep_hits_bounds_including_unresolved": [n - profit_hits, n - profit_hits + missing],
    }


def mill_comparisons(path):
    """Reconstruct the design comparisons from Parker tables 2–3 and Wardrop table 5.1."""
    boddington, morrison = {}, {}
    for row in read_csv(path):
        tonnes = float(row["annual_million_tonnes"])
        name = row["design"]
        if row["site"] == "Boddington":
            boddington[name] = {
                "capital_million_aud": round(tonnes * float(row["capital_per_annual_tonne"]), 4),
                "motor_output_gwh_year_at_design_tonnage": [
                    round(tonnes * float(row[field]), 4)
                    for field in ("specific_kwh_min", "specific_kwh_max")],
            }
        elif row["site"] == "Morrison":
            morrison[name] = {
                "capital_million_cad": float(row["capital_millions"]),
                "annual_operating_million_cad": tonnes * float(row["operating_cost_per_tonne"]),
                "operating_mw": float(row["operating_mw"]),
            }
        else:
            raise ValueError(f"Unexpected site: {row['site']}")
    sag = morrison["Conventional SAG"]
    rolls = morrison["Pressure rolls plus ball mill"]
    premium = rolls["capital_million_cad"] - sag["capital_million_cad"]
    saving = sag["annual_operating_million_cad"] - rolls["annual_operating_million_cad"]
    return {
        "boddington_early_designs": boddington,
        "morrison_rolls_relative_to_sag": {
            "extra_capital_million_cad": round(premium, 3),
            "annual_operating_saving_million_cad": round(saving, 4),
            "incremental_five_year_npv_million_cad": round(
                saving * sum(1 / 1.10**year for year in range(1, 6)) - premium, 4),
            "simple_payback_years": round(premium / saving, 3),
            "change_in_operating_mw": round(rolls["operating_mw"] - sag["operating_mw"], 2),
        },
    }


def compare_within_assessments(primary):
    """Exploratory comparison of the ordering of two offered investments at the same site."""
    by_site = defaultdict(list)
    for row in primary:
        by_site[row["ID"]].append(row)
    pairs = []
    for site, proposals in sorted(by_site.items()):
        for first, second in combinations(proposals, 2):
            npv_gap = float(first["npv_5y_dollars"]) - float(second["npv_5y_dollars"])
            kwh_gap = float(first["annual_kwh"]) - float(second["annual_kwh"])
            # Opposing preferences: the more profitable proposal also avoids more dissipation.
            if npv_gap * kwh_gap <= 0:
                continue
            profit, heat = (first, second) if npv_gap > 0 else (second, first)
            answers = {profit["response"], heat["response"]}
            if "unresolved" in answers:
                verdict = "unresolved"
            elif len(answers) == 1:
                verdict = "both adopted or scheduled" if "adopt" in answers else "both declined"
            elif profit["response"] == "adopt":
                verdict = "profit"
            else:
                verdict = "operating_mep"
            pairs.append({"assessment": site, "profit_prefers": profit["SUPERID"],
                          "operating_mep_prefers": heat["SUPERID"], "profit_offer_status": profit["status"],
                          "operating_mep_offer_status": heat["status"], "verdict": verdict})
    return pairs


def score(folder, results):
    forecast_file = results / "mine_investment_forecasts.csv"
    if sha256(forecast_file) != FROZEN_FORECAST:
        raise ValueError("Forecast file differs from the version committed before scoring")
    forecasts = keyed(read_csv(forecast_file), "SUPERID")
    offers = keyed(read_csv(folder / "recommendations.csv"), "SUPERID")
    responses = keyed(read_csv(folder / "responses.csv"), "SUPERID")
    sites = keyed(read_csv(folder / "assessments.csv"), "ID")
    if not forecasts.keys() == offers.keys() == responses.keys():
        raise ValueError("Forecasts, inputs and follow-up must cover the same offers")
    decisions = []
    for key, forecast_row in sorted(forecasts.items()):
        status = responses[key]["IMPSTATUS"]
        if status not in RESPONSES:
            raise ValueError(f"Unknown follow-up status at {key}: {status!r}")
        if forecast_row["sample"] == "excluded":
            continue
        site = sites[forecast_row["ID"]]
        decisions.append({**forecast_row, "fy": site["FY"], "state": site["STATE"],
                          "sic": site["SIC"], "naics": site["NAICS"], "product": site["PRODUCTS"],
                          "arc": offers[key]["ARC2"], "status": status, "response": RESPONSES[status]})
    fields = [*FORECAST_FIELDS, "fy", "state", "sic", "naics", "product", "arc", "status", "response"]
    write_csv(results / "mine_investment_decisions.csv", fields, decisions)
    primary = [r for r in decisions if r["sample"] == "primary"]
    coal = [r for r in primary if r["sic"].startswith("12") or r["naics"].startswith("2121")]
    both_codes = [r for r in primary if r["sic"][:2] in {"10", "12", "14"}
                  and r["naics"].startswith("212")]
    results_by_rule = {
        "primary_five_year": compare(primary, "profit_5y"),
        "two_year_simple_payback": compare(primary, "profit_2y"),
        "allow_one_cost_component": compare(decisions, "profit_5y"),
        "coal_only": compare(coal, "profit_5y"),
        "both_industry_codes": compare(both_codes, "profit_5y"),
        "lighting": compare([r for r in primary if r["arc"].startswith("2.71")], "profit_5y"),
        "motors_drives_or_compressed_air": compare(
            [r for r in primary if r["arc"].startswith(("2.41", "2.42"))], "profit_5y"),
    }
    per_assessment = {site: compare([r for r in primary if r["ID"] == site], "profit_5y")
                      for site in sorted({r["ID"] for r in primary})}
    pairs = compare_within_assessments(primary)
    write_csv(results / "mine_investment_pairs.csv",
              ["assessment", "profit_prefers", "operating_mep_prefers", "profit_offer_status",
               "operating_mep_offer_status", "verdict"], pairs)
    site_sizes = Counter(r["ID"] for r in primary)
    split_pairs = [p for p in pairs if p["verdict"] in {"profit", "operating_mep"}]
    summary = {
        "source_url": "https://itac.university/storage/ITAC_Database.zip",
        "source_sha256": SNAPSHOT, "forecast_sha256": FROZEN_FORECAST,
        "extract_sha256": {name: sha256(folder / name) for name in
                           ("assessments.csv", "recommendations.csv", "responses.csv", "mill-designs.csv")},
        "roster_assessments": len(sites), "roster_recommendations": len(offers),
        "forecast_samples": dict(sorted(Counter(r["sample"] for r in forecasts.values()).items())),
        "exclusions_first_reason": dict(sorted(Counter(r["reason"] for r in forecasts.values()
                                                       if r["sample"] == "excluded").items())),
        "results": results_by_rule, "primary_by_assessment": per_assessment,
        "identified_district_conflicts": sum(r["district_mep"] in ("adopt", "retain")
                                             and r["district_mep"] != r["profit_5y"] for r in decisions),
        "status_definition": "I includes implemented and definitely scheduled. N means reported no.",
        "exploratory_within_assessment": {
            "all_pairs": sum(math.comb(size, 2) for size in site_sizes.values()),
            "oppositely_ranked_pairs": len(pairs), "split_response_pairs": len(split_pairs),
            "assessments_with_split_responses": len({p["assessment"] for p in split_pairs}),
            "verdicts": dict(sorted(Counter(p["verdict"] for p in pairs).items())),
        },
        "separate_published_designs": mill_comparisons(folder / "mill-designs.csv"),
    }
    write_json(results / "mine_investments.json", summary)
    print(results_by_rule["primary_five_year"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("extract-inputs", "forecast", "extract-outcomes", "score"))
    parser.add_argument("--archive", type=Path, default=BASE / "scripts/data/ITAC_Database.zip")
    parser.add_argument("--inputs", type=Path, default=INPUT)
    parser.add_argument("--results", type=Path, default=RESULTS)
    args = parser.parse_args()
    if args.stage == "extract-inputs":
        extract_inputs(args.archive, args.inputs)
    elif args.stage == "forecast":
        forecast(args.inputs, args.results)
    elif args.stage == "extract-outcomes":
        extract_outcomes(args.archive, args.inputs)
    else:
        score(args.inputs, args.results)


if __name__ == "__main__":
    main()
