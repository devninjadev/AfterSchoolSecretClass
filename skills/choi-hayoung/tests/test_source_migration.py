from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


class SourceMigrationTests(unittest.TestCase):
    def test_migration_map_covers_every_canonical_source_domain(self) -> None:
        migration = json.loads((SKILL_ROOT / "references" / "source-migration.json").read_text(encoding="utf-8"))
        required = {
            "persona",
            "opening-1",
            "opening-2",
            "opening-3",
            "won-myunghee",
            "cfa-ethics",
            "cfa-quant",
            "cfa-economics",
            "cfa-financial-statements",
            "cfa-corporate-finance",
            "cfa-equity",
            "cfa-fixed-income",
            "cfa-derivatives",
            "cfa-alternatives",
            "cfa-portfolio",
            "research-templates",
            "behavioral-finance",
            "investor-perspectives",
            "icon",
            "character-sheet",
        }
        entries = {entry["id"]: entry for entry in migration["entries"]}
        self.assertEqual(set(entries), required)
        for identifier, entry in entries.items():
            with self.subTest(identifier=identifier):
                self.assertIn(entry["status"], {"preserved", "adapted"})
                self.assertTrue(entry["destination"])
                if entry["status"] == "adapted":
                    self.assertTrue(entry["reason"])

    def test_asset_hashes_match_migration_receipt(self) -> None:
        migration = json.loads((SKILL_ROOT / "references" / "source-migration.json").read_text(encoding="utf-8"))
        entries = {entry["id"]: entry for entry in migration["entries"]}
        for identifier, relative in {
            "icon": "assets/icon.png",
            "character-sheet": "assets/character-sheet.png",
        }.items():
            with self.subTest(identifier=identifier):
                self.assertEqual(sha256(SKILL_ROOT / relative), entries[identifier]["sha256"])


if __name__ == "__main__":
    unittest.main()
