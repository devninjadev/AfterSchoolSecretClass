from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_ROOT / "scripts" / "validate_route.py"

VALID_ROUTE = {
    "persona_requested": True,
    "conversation_mode": "analysis",
    "request_class": "portfolio_analysis",
    "needs_current_data": True,
    "needs_world_memory": True,
    "needs_market_news": True,
    "needs_portfolio_advisor": True,
    "needs_myunghee_context": False,
    "needs_image": False,
    "write_intent": "none",
}


def validate(payload: object, *, safe_default: bool = False) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(SCRIPT)]
    if safe_default:
        command.append("--safe-default")
    return subprocess.run(
        command,
        input=json.dumps(payload, ensure_ascii=False),
        capture_output=True,
        text=True,
    )


class RoutingContractTests(unittest.TestCase):
    def test_valid_closed_route_round_trips(self) -> None:
        completed = validate(VALID_ROUTE)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(json.loads(completed.stdout), VALID_ROUTE)

    def test_extra_key_and_unknown_enum_are_rejected(self) -> None:
        extra = {**VALID_ROUTE, "reasoning": "hidden"}
        completed = validate(extra)
        self.assertEqual(completed.returncode, 2)
        self.assertIn("extra keys", completed.stderr)

        unknown = {**VALID_ROUTE, "conversation_mode": "urgent_alpha"}
        completed = validate(unknown)
        self.assertEqual(completed.returncode, 2)
        self.assertIn("conversation_mode", completed.stderr)

    def test_safe_default_disables_optional_integrations_and_writes(self) -> None:
        completed = validate({"broken": True}, safe_default=True)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        result = json.loads(completed.stdout)
        self.assertFalse(result["needs_world_memory"])
        self.assertFalse(result["needs_market_news"])
        self.assertFalse(result["needs_portfolio_advisor"])
        self.assertFalse(result["needs_image"])
        self.assertEqual(result["write_intent"], "none")

    def test_nonexplicit_memory_phrase_fixture_has_no_write_intent(self) -> None:
        remember_only = {**VALID_ROUTE, "needs_world_memory": False, "write_intent": "none"}
        completed = validate(remember_only)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(json.loads(completed.stdout)["write_intent"], "none")


if __name__ == "__main__":
    unittest.main()
