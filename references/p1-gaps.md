# P1 pipeline gaps (TEMPLATE for video-tooling-scout)
Fill this in with your own known pipeline gaps. Every run checks extracted
tools against this file: a match goes at the very top of the report and the
operator's summary as a gap alert, so keep it short and honest.

Matching is by keyword AND by meaning: a found tool that fills the described
need counts even if the wording differs. `Inventory` is where the gap lives
(which `*-pipeline-inventory.md`); `Priority` is P1 (do now) or P2 (next).

Delete the example rows and write your own, or leave this file empty (the
scout then simply emits no gap alerts).

<!--
EXAMPLE ROWS (delete before real use):

| Gap | Inventory | Priority | Source | Match keywords |
|-----|-----------|----------|--------|----------------|
| Rigging / skinning / animation-retarget stage | example (asset pipeline) | P1 | audit 2026-01-15, verified absent | rig, retarget, skinning, auto-rig, animation |
| Per-asset performance budgets (tri counts, texel density, draw calls) | example | P1 | audit 2026-01-15 | perf budget, performance budget, tri count, texel density, draw call |
| Automated engine import validation gate | example (Godot) | P1 | audit 2026-01-15 | import validation, import gate, engine validation |

FORMAT NOTES:
- One row per gap. Keep Gap to one line.
- Match keywords: lowercase, comma-separated; the scout matches by keyword
  AND by meaning, so include the plain-language synonyms people actually use
  in video titles/descriptions.
- Source: where the gap was verified (audit date, repo-tree check). A gap is
  only listed here if it is VERIFIED absent, never "probably missing".
-->

| Gap | Inventory | Priority | Source | Match keywords |
|-----|-----------|----------|--------|----------------|

## How to maintain
- When a gap is resolved or deprioritized, annotate the row
  (RESOLVED / DEPRIORITIZED + date) rather than deleting it.
- New gaps go through the same bar as the watchlist: verified absent in the
  pipeline (audit or repo-tree check), never "probably missing".
