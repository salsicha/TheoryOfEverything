"""Synthetic estimator fixtures only; never used as historical observations."""
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.sandbox.regression.gmm import IV2SLS

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from methods import group_time_att, iv2sls, synthetic_control, two_period
from cases import spring_transition


class DifferenceTests(unittest.TestCase):
    def fixture(self):
        return pd.DataFrame({"unit": ["a", "b", "c", "d"] * 2, "period": [0] * 4 + [1] * 4,
            "outcome": [10., 20., 12., 22., 17., 22., 19., 24.],
            "exposure": [1, 0, 1, 0] * 2, "cluster": ["NJ", "PA", "NJ", "PA"] * 2})

    def test_known_difference_and_policy_cluster_guard(self):
        fit = two_period(self.fixture())
        self.assertAlmostEqual(fit["coefficients"]["exposure"], 5.)
        self.assertFalse(fit["inference_reported"])
        self.assertNotIn("ci95", fit)

    def test_unbalanced_is_error(self):
        with self.assertRaisesRegex(ValueError, "both periods"):
            two_period(self.fixture().iloc[:-1])

    def test_duplicate_is_error(self):
        f = self.fixture()
        with self.assertRaisesRegex(ValueError, "duplicate"):
            two_period(pd.concat([f, f.iloc[:1]]))

    def test_post_selected_exposure_rejected(self):
        f = self.fixture()
        f.loc[4, "exposure"] = 0
        with self.assertRaisesRegex(ValueError, "fixed"):
            two_period(f)


class IVTests(unittest.TestCase):
    def setUp(self):
        rng = np.random.default_rng(71)
        n = 1000
        self.c = np.column_stack([np.ones(n), rng.normal(size=n)])
        self.z = rng.normal(size=n)
        latent = rng.normal(size=n)
        self.d = 2 * self.z + self.c[:, 1] + latent
        self.y = 3 * self.d + self.c @ np.array([1., -2.]) + latent + rng.normal(size=n)
        self.cluster = np.repeat(np.arange(100), 10)

    def test_matches_independent_statsmodels_estimator(self):
        fit = iv2sls(self.y, self.d, self.c, self.z, self.cluster)
        reference = IV2SLS(self.y, np.column_stack([self.d, self.c]), np.column_stack([self.z, self.c])).fit()
        self.assertAlmostEqual(fit["effect_per_unit_treatment"], reference.params[0], places=10)
        self.assertTrue(fit["inference_reported"])

    def test_weighted_ols_limit_and_cluster_covariance(self):
        weights = np.linspace(.2, 1., len(self.y))
        fit = iv2sls(self.y, self.d, self.c, self.d, self.cluster, weights)
        reference = sm.WLS(self.y, np.column_stack([self.d, self.c]), weights=weights).fit(
            cov_type="cluster", cov_kwds={"groups": self.cluster, "use_correction": True})
        self.assertAlmostEqual(fit["effect_per_unit_treatment"], reference.params[0], places=10)
        self.assertAlmostEqual(fit["standard_error"], reference.bse[0], places=10)

    def test_rank_failure(self):
        with self.assertRaisesRegex(ValueError, "Rank-deficient"):
            iv2sls(self.y, self.d, self.c, np.ones(len(self.y)), self.cluster)

    def test_nonfinite_failure(self):
        self.y[0] = np.nan
        with self.assertRaisesRegex(ValueError, "nonfinite"):
            iv2sls(self.y, self.d, self.c, self.z, self.cluster)

    def test_few_clusters_suppresses_wald_interval(self):
        fit = iv2sls(self.y, self.d, self.c, self.z, np.repeat(np.arange(10), 100))
        self.assertNotIn("ci95", fit)
        self.assertFalse(fit["inference_reported"])


class SyntheticTests(unittest.TestCase):
    def fixture(self, shock):
        a = np.array([1, 2, 1, 3, 2, 4, 3, 5, 4, 6.])
        b = np.array([5, 3, 4, 2, 4, 1, 4, 2, 3, 1.])
        y = .3 * a + .7 * b
        y[8:] += shock
        return pd.DataFrame({"T": y, "A": a, "B": b})

    def test_recovers_known_mixture_and_effect(self):
        fit, series = synthetic_control(self.fixture(4), "T", ["A", "B"], range(8), [8, 9], [6, 7])
        self.assertAlmostEqual(fit["weights"]["A"], .3, places=5)
        self.assertAlmostEqual(fit["post_mean_gap"], 4., places=5)
        self.assertLess(fit["heldout_pre_rmspe"], 1e-5)
        self.assertFalse(fit["inference_reported"])

    def test_post_outcome_does_not_leak_into_weights(self):
        first, _ = synthetic_control(self.fixture(0), "T", ["A", "B"], range(8), [8, 9])
        second, _ = synthetic_control(self.fixture(100), "T", ["A", "B"], range(8), [8, 9])
        self.assertEqual(first["weights"], second["weights"])

    def test_missing_donor_rejected(self):
        panel = self.fixture(4)
        panel.loc[2, "A"] = np.nan
        with self.assertRaisesRegex(ValueError, "nonfinite"):
            synthetic_control(panel, "T", ["A", "B"], range(8), [8, 9])

    def test_overlap_rejected(self):
        with self.assertRaisesRegex(ValueError, "overlap"):
            synthetic_control(self.fixture(4), "T", ["A", "B"], range(9), [8, 9])


class CohortTests(unittest.TestCase):
    def test_never_and_not_yet_treated_only(self):
        rows = []
        for unit, adoption in [("early", 3), ("late", 5), ("never", 0)]:
            for period in range(1, 8):
                effect = 7 if adoption and period >= adoption else 0
                rows.append({"unit": unit, "period": period, "adoption": adoption, "outcome": period + effect})
        fit = group_time_att(pd.DataFrame(rows), horizon=2)
        for entry in fit["group_time"]:
            self.assertAlmostEqual(entry["att"], 0 if entry["event"] == -1 else 7)
        last = [r for r in fit["group_time"] if r["cohort"] == 3 and r["event"] == 2][0]
        self.assertEqual(last["control_units"], 1)

    def test_dst_rule_change(self):
        self.assertEqual(str(spring_transition(2006).date()), "2006-04-02")
        self.assertEqual(str(spring_transition(2007).date()), "2007-03-11")


if __name__ == "__main__":
    unittest.main()
