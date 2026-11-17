"""Reanalyse output around US wind plants' tenth birthdays in Hamilton et al. (2020).

The public panel links are from Berkeley Lab's publication page. Run with the
project's research environment. A verified cached copy allows an offline rerun.
"""

import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

HERE = Path(__file__).resolve().parent
PANEL = HERE / "data" / "two_mines_wind_hamilton.csv"
OUTPUT = HERE / "results" / "two_mines_wind.json"
FOLDER = "https://drive.google.com/drive/folders/1MwKfsrPkeaf4I43ydZIK936vQW5Pbf4U"
URL = "https://drive.usercontent.google.com/download?id=1cndvsROebHxS9sppA9WQd5M0RXl4ZAT5&export=download&confirm=t"
HASH = "ee8493d80070d687a30d6219f684a13e4ae49fe0b41e15aea5c0cdea7b2a3717"


def open_panel(path):
    if path.is_file():
        content = path.read_bytes()
    else:
        with urllib.request.urlopen(URL, timeout=90) as response:
            content = response.read()
    if hashlib.sha256(content).hexdigest() != HASH:
        raise ValueError("Unexpected panel checksum. Check the source and input before use.")
    if not path.is_file():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    data = pd.read_csv(path)
    if data.duplicated(["EIA_ID", "age_months"]).any():
        raise ValueError("Duplicate plant-month in source.")
    return data


def fit(data, outcome, cutoff, calendar_effects):
    frame = data.copy()
    frame["post"] = (frame["age_months"] >= 12 * cutoff).astype(int)
    formula = f"{outcome} ~ post + ICF + C(EIA_ID)"
    if calendar_effects:
        formula += " + C(calendar)"
    model = smf.ols(formula, data=frame).fit(
        cov_type="cluster", cov_kwds={"groups": frame["EIA_ID"]}, use_t=True
    )
    if model.model.rank != model.model.exog.shape[1]:
        raise ValueError("Calendar effects leave the birthday contrast unidentified in this sample.")
    interval = model.conf_int().loc["post"] * 100
    return {
        "plants": int(frame["EIA_ID"].nunique()),
        "plant_months": len(frame),
        "pre_mean_capacity_factor_pct": round(100 * frame.loc[frame.post == 0, outcome].mean(), 5),
        "post_mean_capacity_factor_pct": round(100 * frame.loc[frame.post == 1, outcome].mean(), 5),
        "post_minus_pre_adjusted_pp": round(100 * model.params["post"], 5),
        "plant_cluster_95pct_interval_pp": [round(float(x), 5) for x in interval],
    }


def analyse(panel):
    data = panel.copy()
    date = pd.to_datetime(dict(year=data.Year, month=data.Month, day=1))
    data["calendar"] = data.Year * 100 + data.Month
    data["net_capacity_factor"] = data.Netgen / (data.Capacity * date.dt.days_in_month * 24)
    # Age starts at the first reported generation. The 2001 start of the panel
    # left-censors older facilities. Require all four years for the same units
    # so comparisons at nine, ten and eleven cannot change plant composition.
    candidates = data.loc[(data.y0 > 2001) & data.age_months.between(96, 143)].copy()
    measures = ["net_capacity_factor", "ICF", "CF"]
    candidates = candidates.loc[np.isfinite(candidates[measures]).all(axis=1)]
    count = candidates.groupby("EIA_ID")["age_months"].transform("size")
    balanced = candidates.loc[count == 48]
    if balanced.empty:
        raise ValueError("No plant with complete primary and placebo windows.")

    primary = {}
    for birthday in [9, 10, 11]:
        window = balanced.loc[balanced.age_months.between(12 * (birthday - 1), 12 * (birthday + 1) - 1)]
        primary[str(birthday)] = fit(window, "net_capacity_factor", birthday, calendar_effects=True)
    ten = balanced.loc[balanced.age_months.between(108, 131)]
    ids = data.loc[data.age_years >= 12, "EIA_ID"]
    published = data.loc[data.EIA_ID.isin(ids) & data.age_years.between(7, 12)]
    return {
        "study": "Output from operating US wind plants around the ten-year production-tax-credit horizon",
        "source": {
            "authors": "Hamilton, Millstein, Bolinger, Wiser and Jeong (2020)",
            "article": "https://doi.org/10.1016/j.joule.2020.04.005",
            "landing_page": "https://eta.lbl.gov/publications/how-does-wind-project-performance",
            "archive": FOLDER, "panel_url": URL, "panel_sha256": HASH,
            "rows": len(data), "plants": int(data.EIA_ID.nunique()),
            "calendar_years": [int(data.Year.min()), int(data.Year.max())],
        },
        "primary_specification": "First production recorded after 2001. Same plants with complete observed ages 96-143 months. For each birthday, use 12 months before and 12 after. Regress metered monthly net MWh divided by installed MW times calendar hours on a post-birthday indicator, modeled wind resource (ICF), plant fixed effects and calendar year-month fixed effects. Unit is capacity-factor percentage points. Every plant-month has equal weight.",
        "primary_birthdays": primary,
        "balanced_sample_first_generation_years": sorted(map(int, balanced.y0.unique())),
        "without_calendar_effects_age_10": fit(ten, "net_capacity_factor", 10, calendar_effects=False),
        "curtailment_adjusted_age_10": fit(ten, "CF", 10, calendar_effects=True),
        "authors_age_10_specification": fit(published, "CF", 10, calendar_effects=False),
        "authors_specification_details": "Point-estimate replication of the published notebook: all plants observed at age >=12 years; age 7 through exactly 12 inclusive; regression of curtailment-adjusted CF on post-ten, ICF and plant fixed effects. Our intervals cluster by plant. Coefficient is expressed in capacity-factor percentage points, distinct from a loss as a percent of baseline output.",
        "identification": [
            "US production tax credits ran for ten years. The public panel records first production and physical output, without recipient status or each project's tax eligibility date. The estimated exposure is a birthday proxy.",
            "The timing comparison requires other influences on generation to change smoothly at age ten. Contracts, warranties, market dispatch and repowering can also change; the mechanism is not identified.",
            "Age-nine and age-eleven comparisons assess other age-related changes on the same plants. Plant-cluster intervals describe sampling variability under independence across plants; regional or common vintage-specific shocks can widen uncertainty.",
            "Requiring uninterrupted reporting selects plants that remained observable and can include reported zero generation. Repair expenditure, allocation of own proceeds, stoppage and restart are not observed.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=PANEL)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    result = analyse(open_panel(args.data))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result["primary_birthdays"], indent=2))


if __name__ == "__main__":
    main()
