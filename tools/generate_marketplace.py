#!/usr/bin/env python3
"""Regenerate .claude-plugin/marketplace.json from the skills tree.

One "everything" plugin (the scout plus all skills) and one plugin per
category, so users can install the whole library or a single category:

    claude plugin marketplace add Emperiusm/skill_library
    claude plugin install skill-library@skill-library
    claude plugin install engine-runtime@skill-library

Run after adding or moving skills; tools/validate_skills.py fails while
the manifest and the tree disagree.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    skills_root = ROOT / "skills"
    categories: dict[str, list[str]] = {}
    for skill_md in sorted(skills_root.rglob("SKILL.md")):
        d = skill_md.parent
        categories.setdefault(d.parent.name, []).append("./" + d.relative_to(ROOT).as_posix())
    all_skills = ["./video-tooling-scout"] + [
        path for paths in categories.values() for path in paths
    ]
    plugins = [
        {
            "name": "skill-library",
            "source": "./",
            "description": "Everything: the video-tooling-scout plus every skill in the library.",
            "strict": False,
            "skills": all_skills,
        }
    ]
    for category in sorted(categories):
        plugins.append(
            {
                "name": category,
                "source": "./",
                "description": f"The {category} skills.",
                "strict": False,
                "skills": categories[category],
            }
        )
    manifest = {
        "name": "skill-library",
        "owner": {"name": "Emperiusm"},
        "metadata": {
            "description": "Game-tooling skills learned from real workflow videos, "
            "updated daily by the video-tooling-scout, plus imported engine skills."
        },
        "plugins": plugins,
    }
    out = ROOT / ".claude-plugin" / "marketplace.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}: {len(plugins)} plugins, {len(all_skills)} skills")


if __name__ == "__main__":
    main()
