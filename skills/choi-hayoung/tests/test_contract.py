from __future__ import annotations

import re
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(?P<body>.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise AssertionError("SKILL.md must start with YAML frontmatter")
    values: dict[str, str] = {}
    for line in match.group("body").splitlines():
        key, separator, value = line.partition(":")
        if separator:
            values[key.strip()] = value.strip().strip('"')
    return values


class PackageContractTests(unittest.TestCase):
    def test_quote_policy_is_contextual_instead_of_blanket_verification(self) -> None:
        skill = read_text(SKILL_ROOT / "SKILL.md")
        persona = read_text(SKILL_ROOT / "references" / "persona-canon.md")

        self.assertIn("casual character dialogue", skill)
        self.assertIn("precise attribution", skill)
        self.assertIn("source-registry.md", skill)
        self.assertIn("정본 어록집", persona)
        self.assertIn("정확한 연도·행사·문서", persona)
        registry = read_text(SKILL_ROOT / "references" / "source-registry.md")
        self.assertIn("georgesoros.com", registry)
        self.assertIn("uscmarshallweb.s3-us-west-2.amazonaws.com", registry)
        self.assertIn("대표 인용 정본은 스탠리 드러켄밀러와 조지 소로스", registry)
        self.assertNotIn("berkshirehathaway.com/letters/letters.html", registry)
        self.assertNotIn("principles.com", registry)
        self.assertNotIn(
            "출처가 확인될 때만 직접 인용한다",
            persona,
        )

    def test_skill_and_chatgpt_metadata_expose_hayoung_identity(self) -> None:
        metadata = frontmatter(read_text(SKILL_ROOT / "SKILL.md"))
        agent = read_text(SKILL_ROOT / "agents" / "openai.yaml")

        self.assertEqual(metadata["name"], "choi-hayoung")
        self.assertTrue(metadata["description"].startswith("Use when"))
        self.assertIn('display_name: "하영"', agent)
        self.assertIn('default_prompt: "Use $choi-hayoung', agent)
        self.assertIn("allow_implicit_invocation: true", agent)
        self.assertIn('icon_small: "./assets/icon.png"', agent)

    def test_required_package_files_exist_and_are_nonempty(self) -> None:
        required = (
            "references/persona-canon.md",
            "references/opening-scenes.md",
            "references/investment-core.md",
            "references/asset-analysis.md",
            "references/portfolio-analysis.md",
            "references/research-templates.md",
            "references/won-myunghee.md",
            "references/investor-perspectives.md",
            "references/source-registry.md",
            "references/integrations.md",
            "references/world-memory-read-bridge.md",
            "references/routing-contract.json",
            "references/source-migration.json",
            "scripts/select_opening.py",
            "scripts/validate_route.py",
            "assets/icon.png",
            "assets/character-sheet.png",
        )
        for relative in required:
            with self.subTest(relative=relative):
                path = SKILL_ROOT / relative
                self.assertTrue(path.is_file(), f"missing {relative}")
                self.assertGreater(path.stat().st_size, 0, f"empty {relative}")

    def test_shipped_text_has_no_forbidden_paths_feeds_or_secret_values(self) -> None:
        forbidden_literals = (
            "/mnt" + "/data",
            "https://rss.app/feeds/" + "_8HzGbLlZYpznFQ9I.csv",
            "https://rss.app/feeds/" + "_hc8HiU0HyBWHfWoM.csv",
            "/Users/jundochang/" + "Desktop/",
        )
        secret_value = re.compile(
            r"(?i)(oauth[_ -]?token|access[_ -]?token|cookie|client[_ -]?secret)\s*[:=]\s*[\"']?[^\s\"']+"
        )
        for path in sorted(SKILL_ROOT.rglob("*")):
            if not path.is_file() or path.suffix not in {".md", ".json", ".py", ".yaml"}:
                continue
            text = read_text(path)
            with self.subTest(path=path.relative_to(SKILL_ROOT)):
                for literal in forbidden_literals:
                    self.assertNotIn(literal, text)
                self.assertIsNone(secret_value.search(text))


if __name__ == "__main__":
    unittest.main()
