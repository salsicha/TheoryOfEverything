import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mine_investments import compare, compare_within_assessments, forecast_offer, in_cohort


def electric_offer(**updates):
    offer = {"ID": "A", "SUPERID": "A01", "ARC2": "2.7142", "IC_CAPITAL": "1000",
             "IC_OTHER": "0", "PSOURCCODE": "EC", "PCONSERVED": "8760", "PSAVED": "240",
             "SSOURCCODE": "ED", "SCONSERVED": "9999", "SSAVED": "100",
             "TSOURCCODE": "", "QSOURCCODE": ""}
    return {**offer, **updates}


class TestMineForecast(unittest.TestCase):
    def test_industry_takes_precedence_over_secondary_code(self):
        self.assertTrue(in_cohort({"FY": 2024, "NAICS": None, "SIC": 1221}))
        self.assertFalse(in_cohort({"FY": 2024, "NAICS": 921110, "SIC": 1011}))
        self.assertFalse(in_cohort({"FY": 2025, "NAICS": 212111, "SIC": 1221}))

    def test_forecast_uses_metered_kwh_and_ignores_realized_cost_and_decision(self):
        row = forecast_offer(electric_offer())
        self.assertEqual(row["sample"], "primary")
        self.assertEqual(row["annual_dollars"], 340)
        self.assertEqual(row["annual_kwh"], 8760)
        self.assertAlmostEqual(row["delta_operating_w_per_k"], -1000 / 293.15, places=6)
        self.assertEqual((row["profit_5y"], row["profit_2y"], row["operating_mep"]),
                         ("adopt", "retain", "retain"))
        self.assertEqual(row, forecast_offer(electric_offer(IMPSTATUS="N", IMPCOST="999999")))

    def test_missing_cost_differs_from_explicit_zero_and_fuel_switch_is_excluded(self):
        self.assertEqual(forecast_offer(electric_offer(IC_OTHER=""))["sample"], "one_component")
        self.assertEqual(forecast_offer(electric_offer(IC_OTHER="", IC_CAPITAL=""))["sample"], "excluded")
        self.assertEqual(forecast_offer(electric_offer(SSOURCCODE="E2"))["sample"], "excluded")

    def test_pending_outcomes_do_not_score_as_rejections(self):
        forecast = dict(forecast_offer(electric_offer()), response="adopt", status="I")
        pending = dict(forecast, ID="B", response="unresolved", status="P")
        result = compare([forecast, pending], "profit_5y")
        self.assertEqual(result["scored_disagreements"], 1)
        self.assertEqual(result["profit_hits_bounds_including_unresolved"], [1, 2])
        self.assertEqual(result["operating_mep_hits_bounds_including_unresolved"], [0, 1])

    def test_pair_comparison_counts_joint_decisions_and_never_pairs_across_sites(self):
        a = dict(forecast_offer(electric_offer()), response="adopt", status="I")
        b = dict(a, SUPERID="A02", npv_5y_dollars="10", annual_kwh="8000")
        c = dict(b, ID="B", SUPERID="B01")
        self.assertEqual([p["verdict"] for p in compare_within_assessments([a, b, c])],
                         ["both adopted or scheduled"])
        rejected = dict(b, response="retain", status="N")
        pair, = compare_within_assessments([rejected, a])
        self.assertEqual((pair["profit_prefers"], pair["verdict"]), ("A01", "profit"))
        self.assertEqual(compare_within_assessments([a, dict(b, annual_kwh="8760")]), [])


if __name__ == "__main__":
    unittest.main()
