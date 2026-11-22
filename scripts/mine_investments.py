"""Forecast mine investments from assessment inputs and compare with later responses."""
import argparse
import csv
import math
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

from openpyxl import load_workbook

from data import sha256


BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / "research" / "mine-investments"
RESULTS = BASE / "scripts" / "results"
SNAPSHOT = "f7bf6464c4347f7a603bb0b4dba81845e91d15d440a4a72a78ac5e300d78f54c"
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("extract-inputs", "forecast"))
    parser.add_argument("--archive", type=Path, default=BASE / "scripts/data/ITAC_Database.zip")
    parser.add_argument("--inputs", type=Path, default=INPUT)
    parser.add_argument("--results", type=Path, default=RESULTS)
    args = parser.parse_args()
    if args.stage == "extract-inputs":
        extract_inputs(args.archive, args.inputs)
    else:
        forecast(args.inputs, args.results)


if __name__ == "__main__":
    main()
