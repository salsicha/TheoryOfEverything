"""Compare Chinook observations on the same Elwha River reaches before and after dam removal."""
import argparse
from pathlib import Path

import pandas as pd

from data import Context, sha256


URL = (
    "https://www.sciencebase.gov/catalog/file/get/615c9c83d34e7b019242b88f"
    "?f=__disk__cc%2Fff%2Fe9%2Fccffe978aaaea7f20c2f9eb59d6f5786e8780c4d"
)
SHA256 = "15687c2ebd83e0c720868bcd238eecef7e4bb7f9c62558281af4e11911346232"
YEARS = (2007, 2008, 2018, 2019)
SECTIONS = ("Lower Elwha", "Middle Elwha", "Upper Elwha")


def summarize(path):
    if sha256(path) != SHA256:
        raise ValueError("The survey file differs from the USGS release used for this analysis.")
    surveys = pd.read_csv(path)
    if surveys.duplicated(["Reach_ID", "Year"]).any() or set(surveys.Year) != set(YEARS):
        raise ValueError("Expected one row per surveyed reach and year across four survey years.")
    survey_count = surveys.groupby("Reach_ID").Year.transform("size")
    matched = surveys.loc[survey_count == len(YEARS)]
    rows = []
    for year in YEARS:
        for section in SECTIONS:
            sample = matched.loc[(matched.Year == year) & (matched.Section == section)]
            adults = sample.Count_Onts
            distance = sample.Reach_Length_km.sum()
            juveniles = sample.JONTS.dropna()
            rows.append({
                "year": year,
                "section": section,
                "surveyed_reaches": len(sample),
                "surveyed_km": round(distance, 4),
                "adult_chinook": int(adults.sum()),
                "reaches_with_adults": int((adults > 0).sum()),
                "adults_per_surveyed_km": round(adults.sum() / distance, 3),
                "reaches_assessed_for_juveniles": len(juveniles),
                "reaches_with_juveniles": int((juveniles > 0).sum()) if len(juveniles) else None,
            })
    result = pd.DataFrame(rows).astype({"reaches_with_juveniles": "Int64"})
    return result.set_index(["year", "section"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--fetch", action="store_true", help="Download the original USGS survey if absent.")
    source.add_argument("--input", type=Path, help="Use a previously downloaded copy of the USGS CSV.")
    args = parser.parse_args()
    context = Context(fetch=args.fetch)
    path = args.input or context.public("Elwha_Riverscape_reach_data.csv", URL, "csv")
    context.csv("elwha.csv", summarize(path))
