#!/usr/bin/env python3
"""Tests for tools/validate_skills.py.

Run: python3 -m unittest discover -s tests
Covers: the real tree validates clean, and the failure modes that bit this
library in practice (snake_case names, name/folder mismatch, stale README
counts, a skill missing from the index) are all caught.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = ROOT / "tools" / "validate_skills.py"


def run_validator(root: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), "--root", str(root)],
        capture_output=True,
        text=True,
    )


def minimal_tree(tmp: Path) -> Path:
    skill = tmp / "skills" / "engine-runtime" / "demo-skill"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text(
        "---\nname: demo-skill\ndescription: \"Demo workflow.\"\n---\n\n# Demo\n",
        encoding="utf-8",
    )
    (tmp / "skills" / "README.md").write_text("# Skills\n\ndemo-skill\n", encoding="utf-8")
    (tmp / "README.md").write_text(
        "## The skills\n\n1 skills in 1 category.\n\n"
        "| [`engine-runtime`](skills/engine-runtime/) | 1 | Demo |\n",
        encoding="utf-8",
    )
    plugin_dir = tmp / ".claude-plugin"
    plugin_dir.mkdir()
    (plugin_dir / "marketplace.json").write_text(
        '{"name": "t", "plugins": [{"name": "all", "skills": '
        '["./skills/engine-runtime/demo-skill"]}]}',
        encoding="utf-8",
    )
    return tmp


class RealTreeTest(unittest.TestCase):
    def test_repository_validates_clean(self):
        result = run_validator(ROOT)
        self.assertEqual(result.returncode, 0, result.stdout)


class FailureModeTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        minimal_tree(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def expect_failure(self, needle: str):
        result = run_validator(self.tmp)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn(needle, result.stdout)

    def test_snake_case_name_rejected(self):
        skill = self.tmp / "skills" / "engine-runtime" / "demo-skill" / "SKILL.md"
        skill.write_text(skill.read_text().replace("demo-skill", "demo_skill", 1))
        self.expect_failure("single hyphens")

    def test_name_folder_mismatch_rejected(self):
        skill = self.tmp / "skills" / "engine-runtime" / "demo-skill" / "SKILL.md"
        skill.write_text(skill.read_text().replace("name: demo-skill", "name: other-skill"))
        self.expect_failure("must equal folder name")

    def test_stale_readme_count_rejected(self):
        readme = self.tmp / "README.md"
        readme.write_text(readme.read_text().replace("| 1 |", "| 2 |"))
        self.expect_failure("README.md: category")

    def test_unindexed_skill_rejected(self):
        index = self.tmp / "skills" / "README.md"
        index.write_text("# Skills\n")
        self.expect_failure("no entry for skill")


if __name__ == "__main__":
    unittest.main()
