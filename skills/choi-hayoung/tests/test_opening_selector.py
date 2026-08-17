from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_ROOT / "scripts" / "select_opening.py"


def run_selector(*args: str) -> dict[str, object]:
    completed = subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


class OpeningSelectorTests(unittest.TestCase):
    def test_substantive_request_suppresses_opening(self) -> None:
        result = run_selector("--explicit", "--new-scene", "--substantive", "--seed", "7")
        self.assertEqual(result, {"selected": False, "reason": "substantive_request"})

    def test_persona_must_be_explicit_for_opening(self) -> None:
        result = run_selector("--new-scene", "--seed", "7")
        self.assertEqual(result, {"selected": False, "reason": "persona_not_explicit"})

    def test_seeded_selection_is_reproducible_and_every_scene_is_reachable(self) -> None:
        first = run_selector("--explicit", "--new-scene", "--seed", "5")
        second = run_selector("--explicit", "--new-scene", "--seed", "5")
        self.assertEqual(first, second)

        scenes = {
            run_selector("--explicit", "--new-scene", "--seed", str(seed))["scene_id"]
            for seed in range(30)
        }
        self.assertEqual(scenes, {"opening-1", "opening-2", "opening-3"})

    def test_emitted_scene_omits_legacy_image_marker(self) -> None:
        result = run_selector("--explicit", "--new-scene", "--seed", "5", "--emit-scene")
        self.assertTrue(result["selected"])
        self.assertIn("scene", result)
        self.assertNotIn("이미지 생성:", str(result["scene"]))


if __name__ == "__main__":
    unittest.main()
