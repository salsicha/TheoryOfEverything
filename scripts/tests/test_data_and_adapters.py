"""Input safety and executable missing-data adapters, using synthetic fixtures.

Nothing produced here is written to the book's empirical results directory.
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cases import run_case, spring_transition
from data import Context, NeedsData, ROOT, sha256, write_json


CASES = {c["chapter"]: c for c in json.loads((ROOT / "experiments.json").read_text())["cases"]}


class OfflineContext(Context):
    def public(self, *args, **kwargs):
        raise NeedsData("Network intentionally unavailable in synthetic tests")


class AdapterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.ctx = OfflineContext(inputs=self.root, cache=self.root / "cache", output=self.root / "output")

    def tearDown(self):
        self.temp.cleanup()

    def supply(self, chapter, frame):
        path = self.root / CASES[chapter]["input"]
        frame.to_csv(path, index=False)
        write_json(path.with_suffix(".metadata.json"), {
            "sources": ["SYNTHETIC TEST FIXTURE, NOT HISTORICAL EVIDENCE"],
            "construction": "Known-effect artificial observations",
            "coverage": "Fixture only", "assignment": "Constructed for a software test"})

    def test_missing_or_empty_provenance_is_not_data(self):
        with self.assertRaises(NeedsData):
            self.ctx.local(CASES[1])
        path = self.root / CASES[1]["input"]
        path.write_text(",".join(CASES[1]["columns"]) + "\n")
        write_json(path.with_suffix(".metadata.json"), {"sources": []})
        with self.assertRaisesRegex(ValueError, "Metadata"):
            self.ctx.local(CASES[1])

    def test_matched_network_changes_and_primary_infrastructure_fallback(self):
        rows = []
        for match in range(25):
            for exposed in [0, 1]:
                unit = f"{match}_{exposed}"
                for period in [0, 1]:
                    rows.append({"unit": unit, "period": period, "outcome": 50 + match + period * (match / 10 + 7 * exposed),
                                 "exposure": exposed, "cluster": unit, "stratum": str(match)})
        frame = pd.DataFrame(rows)
        self.supply(4, frame)
        result = run_case(CASES[4], self.ctx)
        self.assertAlmostEqual(result["analysis"]["coefficients"]["exposure"], 7)
        self.supply(12, frame)
        result = run_case(CASES[12], self.ctx)
        self.assertEqual(result["primary_status"], "comparison_available")
        self.assertIn("secondary_status", result)

    def test_electrification_adapter_with_known_effect(self):
        rng = np.random.default_rng(123)
        n = 100
        d = rng.normal(size=n)
        baseline = rng.normal(size=n)
        population = rng.uniform(10, 100, size=n)
        self.supply(5, pd.DataFrame({"unit": np.arange(n), "employment_change": 4 * d + 2 * baseline + population / 10,
            "electrification_change": d, "slope": d + rng.normal(size=n) / 10,
            "baseline_employment": baseline, "baseline_population": population, "district": np.arange(n)}))
        result = run_case(CASES[5], self.ctx)
        self.assertAlmostEqual(result["iv"]["effect_per_unit_treatment"], 4, places=8)

    def test_oklo_has_no_fabricated_models_and_checks_supplied_predictions(self):
        result = run_case(CASES[6], self.ctx)
        self.assertEqual(result["models_checked"], [])
        self.assertFalse(result["origin_of_constants_identified"])
        self.supply(6, pd.DataFrame({"model": ["synthetic_small", "synthetic_large"], "fractional_alpha_change": [1e-9, -2e-8]}))
        result = run_case(CASES[6], self.ctx)
        self.assertEqual([m["within_published_bound"] for m in result["models_checked"]], [True, False])

    def test_primary_ai_panel_runs_without_secondary_network(self):
        rng = np.random.default_rng(8)
        days = pd.date_range("2023-01-01", "2023-04-27")
        x = rng.uniform(1, 10, (len(days), 5))
        treated = x @ np.array([.1, .2, .3, .1, .3]) + (days >= "2023-03-31") * 5
        wide = pd.DataFrame(x, index=days, columns=["fr", "de", "es", "gb", "se"])
        wide["it"] = treated
        panel = wide.rename_axis("date").reset_index().melt(id_vars="date", var_name="country", value_name="outcome")
        self.supply(11, panel)
        result = run_case(CASES[11], self.ctx)
        self.assertEqual(result["primary_status"], "comparison_available")
        self.assertAlmostEqual(result["primary_coding"]["post_mean_gap"], 5, places=4)

    def test_dst_windows_and_missing_days(self):
        rows = []
        transition = spring_transition(2007)
        for state, dst in [("A", 1), ("B", 1), ("C", 0), ("D", 0)]:
            for day in range(-42, 15):
                rows.append({"state": state, "date": (transition + pd.Timedelta(days=day)).date().isoformat(),
                             "crashes": 20 + (3 if dst and day > 0 else 0), "observes_dst": dst})
        frame = pd.DataFrame(rows)
        self.supply(10, frame)
        result = run_case(CASES[10], self.ctx)
        contrasts = result["yearly_contrasts"]
        self.assertAlmostEqual(contrasts["2007_event"]["coefficients"]["exposure"], 3)
        self.assertAlmostEqual(contrasts["2007_placebo"]["coefficients"]["exposure"], 0)
        self.assertFalse(contrasts["2007_event"]["inference_reported"])
        self.supply(10, frame.iloc[:-1])
        with self.assertRaisesRegex(ValueError, "Missing daily"):
            run_case(CASES[10], self.ctx)

    def test_cache_tampering_is_rejected(self):
        self.ctx.cache.mkdir()
        path = self.ctx.cache / "example.csv"
        path.write_text("value\n1\n")
        write_json(self.ctx.cache / "example.csv.json", {"source_url": "https://example.org/data", "sha256": sha256(path)})
        ctx = Context(cache=self.ctx.cache)
        ctx.public("example.csv", "https://example.org/data", "csv")
        path.write_text("value\n2\n")
        with self.assertRaisesRegex(ValueError, "checksum"):
            ctx.public("example.csv", "https://example.org/data", "csv")


if __name__ == "__main__":
    unittest.main()
