"""Trace previously producing mines through a reported zero year and into the next year."""
from __future__ import annotations

import argparse
from pathlib import Path

from data import Context, write_json
from two_mines import METHODS, baseline_mines, load_years, recorded_outcomes


def outcomes(frame, column):
    """Separate a positive return, an explicit zero, and unknown follow-up."""
    positive = int(frame[column].gt(0).sum())
    zero = int(frame[column].eq(0).sum())
    unknown = int(frame[column].isna().sum())
    count = len(frame)
    return {
        "mines": count,
        "positive": positive,
        "zero": zero,
        "unknown": unknown,
        "without_positive_record": count - positive,
        "positive_fraction_bounds": (
            [positive / count, (positive + unknown) / count] if count else None
        ),
    }


def restart_window(baseline, conventional, year):
    cohort = baseline.loc[baseline.year.eq(year), ["mine_id", "method", "state"]].copy()
    for offset, name in ((1, "intervening_tons"), (2, "followup_tons")):
        observations = conventional.loc[conventional.year.eq(year + offset)]
        cohort[name] = cohort.mine_id.map(observations.set_index("mine_id").reported_tons)
    eligible = cohort.loc[cohort.intervening_tons.eq(0)]
    groups = {}
    for method in METHODS:
        at_start = cohort.loc[cohort.method.eq(method)]
        interrupted = eligible.loc[eligible.method.eq(method)]
        unobserved = at_start.loc[at_start.intervening_tons.isna()]
        groups[method] = {
            "positive_baseline": len(at_start),
            "recorded_positive_in_intervening_year": int(at_start.intervening_tons.gt(0).sum()),
            "after_recorded_zero": outcomes(interrupted, "followup_tons"),
            "after_unobserved_intervening_year": outcomes(unobserved, "followup_tons"),
        }
    geography = {}
    for state, area in eligible.groupby("state", sort=True):
        geography[state] = {method: int(area.method.eq(method).sum()) for method in METHODS}
    return {
        "baseline_year": year,
        "zero_year": year + 1,
        "outcome_year": year + 2,
        "groups": groups,
        "zero_year_cohort_by_baseline_area": geography,
        "areas_with_both_methods_after_zero": [
            area for area, counts in geography.items() if all(counts.values())
        ],
    }


def run(ctx):
    raw = load_years(ctx)
    baseline = baseline_mines(raw)
    # A refuse-only record provides no explicit conventional-production observation.
    # Keep only years with at least one underground or surface row for this identifier.
    conventional = recorded_outcomes(raw).merge(
        raw.loc[raw.method.isin(METHODS), ["year", "mine_id"]].drop_duplicates(),
        on=["year", "mine_id"], validate="one_to_one",
    )
    windows = [restart_window(baseline, conventional, year) for year in (2015, 2016, 2017)]
    return {
        "question": "After an explicit full year of zero production, did previously producing mines resume coal extraction in the following year?",
        "2019_geographic_comparison_status": (
            "descriptive_common_support" if windows[-1]["areas_with_both_methods_after_zero"]
            else "no_common_support"
        ),
        "design": "Use the main comparison's producing Appalachian mine cohort in each initial year. Fix method and area at that initial observation. Require an explicit zero-ton underground or surface record in the middle year. Count positive underground or surface production under the same MSHA identifier in the third year.",
        "interpretation": "Endpoints in 2017 and 2018 precede the tax cut. The endpoint in 2019 coincides with the cut. Each window starts with a distinct baseline cohort. A full zero year is a production interruption of unknown cause. Annual records do not identify equipment failure, timing of a repair, or shifts worked.",
        "missingness": "A missing conventional-production observation leaves output unknown. Follow-up bounds assign unknown mines first no positive output and then positive output. A null interval means the cohort is empty. The separate reporting-gap counts include mines with unknown interruption status and cannot furnish verified restarts.",
        "windows": windows,
        "provenance": ctx.provenance,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true", help="Download missing EIA workbooks")
    parser.add_argument("--cache", type=Path, help="Directory for source workbooks")
    parser.add_argument("--output", type=Path, help="Directory for the result")
    args = parser.parse_args()
    ctx = Context(fetch=args.fetch, cache=args.cache, output=args.output)
    report = run(ctx)
    write_json(ctx.output / "two_mines_restart.json", report)
    for window in report["windows"]:
        print(window["outcome_year"], {
            method: window["groups"][method]["after_recorded_zero"] for method in METHODS
        })


if __name__ == "__main__":
    main()
