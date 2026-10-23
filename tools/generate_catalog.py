#!/usr/bin/env python3
"""Generate the browsable catalog site from the skills tree.

Emits a single self-contained site/index.html (inline CSS/JS, no build
step, no external assets): every skill as a card under its category, with
a client-side search filter, the one-line install commands up top, and
links to each SKILL.md on GitHub. Regenerate after the library changes:

    python3 tools/generate_catalog.py

Deploy the site/ folder with any static host (we use Vercel).
"""

from __future__ import annotations

import html
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_skills import split_frontmatter

ROOT = Path(__file__).resolve().parent.parent
GITHUB = "https://github.com/Emperiusm/skill_library/blob/main"

CATEGORY_TITLES = {
    "capture": "Capture and reconstruction",
    "characters": "Characters and rigging",
    "procgen-worlds": "Procedural generation and worlds",
    "ai-video": "AI video",
    "simulation-vfx": "Simulation and VFX",
    "materials-shaders": "Materials and shaders",
    "engine-runtime": "Engine and runtime",
    "automation": "Automation and pipelines",
    "no-tooling": "No tooling (negative examples)",
}


def first_sentence(desc: str, limit: int = 220) -> str:
    desc = re.sub(r"\s+", " ", desc).strip()
    if len(desc) <= limit:
        return desc
    cut = desc[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(".,;:") + "..."


def main() -> None:
    skills_root = ROOT / "skills"
    categories: dict[str, list[tuple[str, str, str]]] = {}
    for skill_md in sorted(skills_root.rglob("SKILL.md")):
        d = skill_md.parent
        fields, _ = split_frontmatter(skill_md.read_text(encoding="utf-8"))
        desc = first_sentence(fields.get("description", "")) if fields else ""
        rel = d.relative_to(ROOT).as_posix()
        categories.setdefault(d.parent.name, []).append((d.name, desc, rel))
    total = sum(len(v) for v in categories.values())

    sections = []
    for cat in sorted(categories, key=lambda c: (-len(categories[c]), c)):
        title = CATEGORY_TITLES.get(cat, cat)
        cards = "\n".join(
            f'''<article class="card" data-search="{html.escape((name + " " + desc).lower())}">
  <h3><a href="{GITHUB}/{rel}/SKILL.md">{html.escape(name)}</a></h3>
  <p>{html.escape(desc)}</p>
</article>'''
            for name, desc, rel in categories[cat]
        )
        sections.append(
            f'<section><h2>{html.escape(title)} <span class="count">{len(categories[cat])}</span></h2>\n'
            f'<div class="grid">\n{cards}\n</div></section>'
        )

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>skill_library: game tooling skills for AI agents</title>
<meta name="description" content="{total} executable game-tooling skills learned from real workflow videos, updated daily. Installs into Claude Code, Codex, Cursor, and any Agent Skills reader.">
<style>
  :root {{ color-scheme: dark; --bg:#0d1117; --panel:#161b22; --line:#30363d; --text:#e6edf3; --dim:#8b949e; --accent:#58a6ff; }}
  * {{ box-sizing: border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--text); font:16px/1.55 -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
  main {{ max-width:1060px; margin:0 auto; padding:40px 20px 64px; }}
  h1 {{ font-size:32px; margin:0 0 6px; }}
  .sub {{ color:var(--dim); margin:0 0 22px; }}
  .install {{ background:var(--panel); border:1px solid var(--line); border-radius:10px; padding:16px 18px; margin:0 0 18px; }}
  .install code {{ display:block; font:13.5px/1.7 ui-monospace, SFMono-Regular, Menlo, monospace; color:var(--accent); white-space:pre-wrap; }}
  #search {{ width:100%; padding:11px 14px; border-radius:8px; border:1px solid var(--line); background:var(--panel); color:var(--text); font-size:15px; margin:6px 0 10px; }}
  section {{ margin-top:34px; }}
  h2 {{ font-size:21px; border-bottom:1px solid var(--line); padding-bottom:8px; }}
  .count {{ color:var(--dim); font-size:14px; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(300px, 1fr)); gap:14px; }}
  .card {{ background:var(--panel); border:1px solid var(--line); border-radius:10px; padding:14px 16px; }}
  .card h3 {{ margin:0 0 6px; font-size:15.5px; }}
  .card a {{ color:var(--accent); text-decoration:none; word-break:break-word; }}
  .card a:hover {{ text-decoration:underline; }}
  .card p {{ margin:0; color:var(--dim); font-size:14px; }}
  footer {{ margin-top:48px; color:var(--dim); font-size:13.5px; }}
  footer a {{ color:var(--accent); }}
</style>
</head>
<body>
<main>
  <h1>skill_library</h1>
  <p class="sub">{total} executable game-tooling skills, learned from real workflow videos by a daily scout, plus imported engine skills. Every skill is a plain SKILL.md an agent can execute end to end.</p>
  <div class="install">
    <code>npx skills add Emperiusm/skill_library
claude plugin marketplace add Emperiusm/skill_library
claude plugin install skill-library@skill-library</code>
  </div>
  <input id="search" type="search" placeholder="Search {total} skills (try: godot, keying, crowd, publish)" aria-label="Search skills">
{chr(10).join(sections)}
  <footer>Generated {date.today().isoformat()} from the <a href="https://github.com/Emperiusm/skill_library">skill_library repository</a>. New skills land with every daily scout run. Imported skills are credited in THIRD-PARTY-NOTICES.md in the repo.</footer>
</main>
<script>
  const box = document.getElementById('search');
  box.addEventListener('input', () => {{
    const q = box.value.trim().toLowerCase();
    document.querySelectorAll('.card').forEach(card => {{
      card.style.display = !q || card.dataset.search.includes(q) ? '' : 'none';
    }});
    document.querySelectorAll('section').forEach(section => {{
      const visible = [...section.querySelectorAll('.card')].some(c => c.style.display !== 'none');
      section.style.display = visible ? '' : 'none';
    }});
  }});
</script>
</body>
</html>
"""
    out = ROOT / "site" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}: {total} skills in {len(categories)} categories")


if __name__ == "__main__":
    main()
