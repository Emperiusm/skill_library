#!/usr/bin/env python3
"""Validate the skill_library repository.

Adapted from gamedev-skills/awesome-gamedev-agent-skills
scripts/validate-skills.py (Apache License 2.0; see THIRD-PARTY-NOTICES.md),
restructured for this repository's category layout and cross-checks.

Checks, standard library only:
- Every SKILL.md (skills/<category>/<name>/ and video-tooling-scout/) has
  frontmatter with exactly the portable fields: name, description.
- name is kebab-case (lowercase letters, digits, single hyphens), at most 64
  chars, and equals the skill's folder name (the Agent Skills standard; the
  standard installers reject anything else).
- description is non-empty, at most 1024 chars, without angle brackets.
- No duplicate skill names anywhere in the library.
- Local resource links in SKILL.md files resolve.
- skills/README.md mentions every skill folder (index completeness).
- The root README's category counts and total match the actual tree.
- .claude-plugin/marketplace.json is valid, lists every skill exactly once,
  and every listed path exists.

Usage: python3 tools/validate_skills.py [--root PATH]
Exit code 0 when clean, 1 with one line per error otherwise.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
CODE_PATH_RE = re.compile(r"`((?:references|scripts|assets)/[^`\s]+)`")

MAX_NAME = 64
MAX_DESCRIPTION = 1024
ALLOWED_FRONTMATTER = frozenset({"name", "description"})


def split_frontmatter(text: str) -> tuple[dict[str, str] | None, int]:
    """Parse the flat fields and folded scalars used by this repository."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, 0
    end = next((i for i, line in enumerate(lines[1:], 1) if line.strip() == "---"), None)
    if end is None:
        return None, 0
    fields: dict[str, str] = {}
    key_re = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")
    i = 1
    while i < end:
        raw = lines[i]
        if not raw.strip() or raw.lstrip().startswith("#") or raw[:1] in (" ", "\t"):
            i += 1
            continue
        match = key_re.match(raw)
        if not match:
            i += 1
            continue
        key, inline = match.group(1), match.group(2).strip()
        if key in fields:
            fields[f"__duplicate__{key}"] = ""
        if inline in {">", "|", ">-", "|-", ">+", "|+"}:
            block: list[str] = []
            i += 1
            while i < end and (not lines[i].strip() or lines[i][:1] in (" ", "\t")):
                if lines[i].strip():
                    block.append(lines[i].strip())
                i += 1
            fields[key] = " ".join(block).strip()
            continue
        fields[key] = inline.strip("\"'")
        i += 1
    return fields, end + 1


def find_skill_files(root: Path) -> list[Path]:
    files = sorted((root / "skills").rglob("SKILL.md"))
    scout = root / "video-tooling-scout" / "SKILL.md"
    if scout.is_file():
        files.append(scout)
    return files


def local_link_target(target: str) -> str | None:
    link = target.strip().strip("<>").split("#", 1)[0].split("?", 1)[0]
    if not link or link.startswith(("http://", "https://", "mailto:", "#")):
        return None
    if "/" not in link and not link.startswith(".") and Path(link).suffix == "":
        return None
    # Patterns and placeholders are illustrations, not links.
    if "*" in link or "<" in link or ">" in link:
        return None
    return link


def validate_skill(path: Path, root: Path) -> list[str]:
    rel = path.relative_to(root).as_posix()
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    fields, _ = split_frontmatter(text)
    if fields is None:
        return [f"{rel}: missing or unclosed frontmatter"]
    dupes = [k for k in fields if k.startswith("__duplicate__")]
    if dupes:
        errors.append(f"{rel}: duplicate frontmatter key(s): {', '.join(dupes)}")
    extra = set(fields) - ALLOWED_FRONTMATTER - {k for k in fields if k.startswith("__duplicate__")}
    if extra:
        errors.append(f"{rel}: non-portable frontmatter field(s): {', '.join(sorted(extra))}")
    missing = ALLOWED_FRONTMATTER - set(fields)
    if missing:
        errors.append(f"{rel}: missing frontmatter field(s): {', '.join(sorted(missing))}")
    name = fields.get("name", "")
    if name:
        if len(name) > MAX_NAME:
            errors.append(f"{rel}: 'name' is {len(name)} chars (max {MAX_NAME})")
        if not NAME_RE.match(name):
            errors.append(f"{rel}: 'name' must use lowercase letters, digits, and single hyphens")
        if name != path.parent.name:
            errors.append(f"{rel}: 'name' = {name!r} must equal folder name {path.parent.name!r}")
    desc = fields.get("description", "")
    if not desc:
        errors.append(f"{rel}: 'description' is missing or empty")
    else:
        if len(desc) > MAX_DESCRIPTION:
            errors.append(f"{rel}: 'description' is {len(desc)} chars (max {MAX_DESCRIPTION})")
        if "<" in desc or ">" in desc:
            errors.append(f"{rel}: 'description' must not contain angle brackets")
    for target in MD_LINK_RE.findall(text):
        link = local_link_target(target)
        if link and not (path.parent / link).exists():
            errors.append(f"{rel}: local resource link does not resolve: {target!r}")
    # Code-span paths name bundled resources only when the skill actually
    # bundles that top-level folder; otherwise they are the documented
    # project's own files (an audited pipeline's assets/, not the skill's).
    bundled = {entry.name for entry in path.parent.iterdir() if entry.is_dir()}
    for target in CODE_PATH_RE.findall(text):
        link = local_link_target(target)
        if link and link.split("/", 1)[0] in bundled and not (path.parent / link).exists():
            errors.append(f"{rel}: local resource link does not resolve: {target!r}")
    return errors


def validate_unique_names(files: list[Path], root: Path) -> list[str]:
    seen: dict[str, list[str]] = {}
    for path in files:
        fields, _ = split_frontmatter(path.read_text(encoding="utf-8"))
        if fields and fields.get("name"):
            seen.setdefault(fields["name"], []).append(path.relative_to(root).as_posix())
    return [
        f"duplicate skill name {name!r}: {', '.join(paths)}"
        for name, paths in seen.items()
        if len(paths) > 1
    ]


def skill_dirs(root: Path) -> list[Path]:
    return sorted(p.parent for p in (root / "skills").rglob("SKILL.md"))


def validate_index(root: Path) -> list[str]:
    errors: list[str] = []
    index_path = root / "skills" / "README.md"
    if not index_path.is_file():
        return ["skills/README.md: missing"]
    index_text = index_path.read_text(encoding="utf-8")
    for d in skill_dirs(root):
        if d.name not in index_text:
            errors.append(f"skills/README.md: no entry for skill {d.name!r}")
    return errors


def validate_readme_counts(root: Path) -> list[str]:
    errors: list[str] = []
    readme = root / "README.md"
    if not readme.is_file():
        return ["README.md: missing"]
    text = readme.read_text(encoding="utf-8")
    actual: dict[str, int] = {}
    for d in skill_dirs(root):
        cat = d.parent.name
        actual[cat] = actual.get(cat, 0) + 1
    total = sum(actual.values())
    m = re.search(r"## The skills\s+(\d+) skills", text)
    if m and int(m.group(1)) != total:
        errors.append(f"README.md: says {m.group(1)} skills, tree has {total}")
    for cat, count in re.findall(r"\| \[`([a-z0-9-]+)`\]\(skills/[a-z0-9-]+/\) \| (\d+) \|", text):
        if actual.get(cat) != int(count):
            errors.append(
                f"README.md: category {cat!r} says {count}, tree has {actual.get(cat, 0)}"
            )
    for cat in actual:
        if cat not in text:
            errors.append(f"README.md: category {cat!r} missing from the skills table")
    return errors


def validate_marketplace(root: Path) -> list[str]:
    errors: list[str] = []
    path = root / ".claude-plugin" / "marketplace.json"
    if not path.is_file():
        return [".claude-plugin/marketplace.json: missing"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f".claude-plugin/marketplace.json: invalid JSON: {exc}"]
    listed: list[str] = []
    for plugin in data.get("plugins", []):
        listed.extend(plugin.get("skills", []))
    for entry in listed:
        if not (root / entry).is_dir():
            errors.append(f"marketplace.json: listed skill path does not exist: {entry}")
    expected = {"./" + d.relative_to(root).as_posix() for d in skill_dirs(root)}
    expected.add("./video-tooling-scout")
    listed_set = set(listed)
    # The "everything" plugin lists all skills; per-category plugins repeat
    # them. Count each skill once per plugin, and require the union to cover
    # the whole library exactly.
    if listed_set != expected:
        missing = sorted(expected - listed_set)
        extra = sorted(listed_set - expected)
        if missing:
            errors.append(f"marketplace.json: skills not listed: {', '.join(missing)}")
        if extra:
            errors.append(f"marketplace.json: listed paths not in tree: {', '.join(extra)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    root = args.root
    files = find_skill_files(root)
    errors: list[str] = []
    for path in files:
        errors.extend(validate_skill(path, root))
    errors.extend(validate_unique_names(files, root))
    errors.extend(validate_index(root))
    errors.extend(validate_readme_counts(root))
    errors.extend(validate_marketplace(root))
    if errors:
        print(f"{len(errors)} error(s):")
        for error in errors:
            print(f"  {error}")
        return 1
    print(f"OK: {len(files)} skills validated, indexes and marketplace in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
