from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = SKILL_ROOT / "tests" / "pressure-scenarios.json"
VALIDATOR = SKILL_ROOT / "scripts" / "validate_route.py"


class PressureScenarioContractTests(unittest.TestCase):
    def test_expected_routes_are_closed_and_authorization_safe(self) -> None:
        scenarios = json.loads(SCENARIOS.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(scenarios), 8)
        for scenario in scenarios:
            with self.subTest(identifier=scenario["id"]):
                completed = subprocess.run(
                    [sys.executable, str(VALIDATOR)],
                    input=json.dumps(scenario["expected_route"], ensure_ascii=False),
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
                route = json.loads(completed.stdout)
                if not scenario["explicit_write_authorized"]:
                    self.assertEqual(route["write_intent"], "none")

    def test_generic_finance_does_not_request_persona(self) -> None:
        scenarios = {item["id"]: item for item in json.loads(SCENARIOS.read_text(encoding="utf-8"))}
        route = scenarios["generic-finance-control"]["expected_route"]
        self.assertFalse(route["persona_requested"])

    def test_substantive_hayoung_request_skips_opening(self) -> None:
        scenarios = {item["id"]: item for item in json.loads(SCENARIOS.read_text(encoding="utf-8"))}
        route = scenarios["substantive-hayoung-analysis"]["expected_route"]
        self.assertTrue(route["persona_requested"])
        self.assertNotEqual(route["conversation_mode"], "opening")


if __name__ == "__main__":
    unittest.main()
