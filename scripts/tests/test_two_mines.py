"""Regression checks for the mine comparisons' reporting and cohort boundaries."""
import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from two_mines import baseline_mines, compare, recorded_outcomes
from two_mines_restart import restart_window


class MineRecords(unittest.TestCase):
    def test_support_units_and_mixed_method(self):
        raw = pd.DataFrame([
            (1, "Underground", 80), (1, "Surface", 0), (2, "Underground", 20),
            (2, "Surface", 30), (3, "Surface", 0),
        ], columns=["mine_id", "method", "tons"])
        raw = raw.assign(year=2017, status="Active", region="Appalachia Central", state="Virginia", county="Wise")
        cohort = baseline_mines(raw)
        self.assertEqual(cohort.mine_id.tolist(), [1])
        self.assertEqual(cohort.method.tolist(), ["Underground"])
        self.assertEqual(recorded_outcomes(raw).reported_tons.tolist(), [80, 50, 0])

    def test_absent_middle_year_is_not_a_verified_restart(self):
        baseline = pd.DataFrame({"mine_id": [1, 2], "year": 2017, "method": "Surface", "state": "Virginia"})
        output = pd.DataFrame([(1, 2018, 0), (1, 2019, 10), (2, 2019, 20)],
                              columns=["mine_id", "year", "reported_tons"])
        group = restart_window(baseline, output, 2017)["groups"]["Surface"]
        self.assertEqual(group["after_recorded_zero"]["positive"], 1)
        self.assertEqual(group["after_unobserved_intervening_year"]["positive"], 1)

    def test_reporting_contrast_can_exceed_actual_continuation_lower_bound(self):
        rows = []
        for year in range(2015, 2019):
            for method in ("Underground", "Surface"):
                missing = method == "Surface" and year == 2018
                rows.append((year, method, not missing, False, missing))
        panel = pd.DataFrame(rows, columns=["year", "method", "continued", "explicit_zero", "missing_report"])
        panel = panel.assign(state="Virginia", county="Wise", mine_id=1)
        report = compare(panel, ["state", "county"])
        self.assertEqual(report["change_in_gap_pp"]["2019_vs_2018_followup"], 100)
        self.assertEqual(report["2019_change_in_gap_missing_outcome_bounds_pp"], [0, 100])


if __name__ == "__main__":
    unittest.main()
