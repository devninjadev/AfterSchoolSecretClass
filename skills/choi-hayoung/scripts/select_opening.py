#!/usr/bin/env python3
"""Select a Hayoung opening from semantic flags supplied by the calling model."""

from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path


SCENE_IDS = ("opening-1", "opening-2", "opening-3")


def select_opening(
    *, explicit: bool, new_scene: bool, substantive: bool, seed: int | None = None
) -> dict[str, object]:
    if not explicit:
        return {"selected": False, "reason": "persona_not_explicit"}
    if not new_scene:
        return {"selected": False, "reason": "not_new_scene"}
    if substantive:
        return {"selected": False, "reason": "substantive_request"}
    rng: random.Random = random.Random(seed) if seed is not None else random.SystemRandom()
    return {"selected": True, "scene_id": rng.choice(SCENE_IDS)}


def load_scene(scene_id: str) -> str:
    source = (Path(__file__).resolve().parents[1] / "references" / "opening-scenes.md").read_text(
        encoding="utf-8"
    )
    pattern = rf"^## {re.escape(scene_id)}\n\n(?P<scene>.*?)(?=\n## opening-|\Z)"
    match = re.search(pattern, source, flags=re.MULTILINE | re.DOTALL)
    if not match:
        raise RuntimeError(f"scene not found: {scene_id}")
    return match.group("scene").strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Select one canonical opening. The caller supplies semantic flags; this script does not classify text."
    )
    parser.add_argument("--explicit", action="store_true", help="Hayoung was explicitly activated")
    parser.add_argument("--new-scene", action="store_true", help="This is a new persona scene")
    parser.add_argument("--substantive", action="store_true", help="The user supplied a substantive task")
    parser.add_argument("--seed", type=int, help="Deterministic test seed; omit in production")
    parser.add_argument("--emit-scene", action="store_true", help="Include selected scene text")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = select_opening(
        explicit=args.explicit,
        new_scene=args.new_scene,
        substantive=args.substantive,
        seed=args.seed,
    )
    if args.emit_scene and result["selected"]:
        result["scene"] = load_scene(str(result["scene_id"]))
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
