# Have-vs-need: 2026-10-07

Daily video-tooling-scout run. Scan window: last 2 days (2026-10-05 to 2026-10-07).
Depth mode: `pre-approved` (max 2 media downloads, Ehsan 2026-09-27).

## Gap alerts

**None.** Extracted tools (Blender constraint rigging, Substance Painter,
ZBrush, Arnold/Maya, toon aiStandard shading) match no P1/P2 gap in
`references/p1-gaps.md` by keyword or meaning. The one rigging-adjacent
finding (audit #1, constraint-driven "fake simulation" rigging) is manual
rigging work, and the P1 rigging gap explicitly needs automation
(auto-rig / skinning / animation retarget); per the standing precedent set
with the Rigify row (2026-09-30, "does NOT fill the P1 rigging-stage gap,
no automation"), manual rigging is adjacent prior art, not a gap fill.
Nothing else extracted fills or addresses any gap.

## Scan summary

- Subreddits queried: unity, unrealengine, godot, blender, houdini, substance3d,
  photogrammetry, gameassets, topology, aigamedev, comfyui, vibecoding,
  technicalart, proceduralgeneration, vfx, Simulated, 3Dmodeling, gamedev.
- Coverage gaps: `comfyui`, `technicalart`, `vfx`, `Simulated`, `gamedev`
  returned HTTP 422 from Arctic Shift this run; their video posts were not
  scanned.
- Video posts returned: 4 (r/3Dmodeling x2, r/Substance3D x1, r/proceduralgeneration x1).
- Deep analysis cap: 8. Deeply analyzed: 3 (the 4th, "Rotating Dotted Sphere",
  had zero tooling signal and was excluded from the diff).

| # | Title | Creator | Source | Depth |
|---|-------|---------|--------|-------|
| 1 | Blender 3d Rigging performed without simulation or body blend shapes | Broad-Requirement-83 | https://v.redd.it/dpngmfgx9oth1 (r/3Dmodeling post 1wyclry, score 800, 42 comments) | PARTIAL |
| 2 | Silco Hand Painted (Substance Painter // Zbrush // Arnold Maya) + cross-post (Toon // aiStandard and Substance Painter) | ImpressiveAct5779 | https://v.redd.it/cp1lq262woth1 (r/Substance3D post 1wyfrab, score 298, 3 comments) + https://v.redd.it/o4kyz4v0soth1 (r/3Dmodeling post 1wyf5cn, score 187, 4 comments) | DEPTH-LIMITED |
| 3 | Rotating Dotted Sphere | DigitCell | https://v.redd.it/4lgj94okyoth1 (r/proceduralgeneration post 1wyg4or, score 55, 1 comment) | NO-TOOLING |

## 1. "Blender 3d Rigging performed without simulation or body blend shapes" (Broad-Requirement-83)

Source: https://v.redd.it/dpngmfgx9oth1 | r/3Dmodeling post 1wyclry (score 800) | native clip

Tools used: Blender (bone constraints: Transform modifiers, Stretch To, Track To,
Stretch). No named plugins, versions, or add-ons in the evidence.

This audit reconstructs the exact workflow described by the author in the post
text and their own comments, step by step, so another agent can follow the
same process. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle). The video's core
method is: fake the simulation with constraints instead of running one.

The author's stated use case: "intended for animation and game-development
workflows, including NSFW projects" (post selftext); the demo rig produces
clothing/body motion without cloth simulation and without blend shapes.

### Phase 1: Lay out base bones

**Do**
1. Build the standard base bone chain for the character (the bones that will
   actually drive the mesh).
2. Plan the chain the author describes: **Base bone -> modifier -> constraints
   -> guide bone -> modifier (transform, location, etc.) -> constraints**
   (author's own description of the system).

**Check**
- The chain order matches the author's quoted architecture exactly:
  each base bone feeds through a modifier into constraints on a guide bone,
  which in turn feeds through its own modifier into final constraints.

**Why**
The whole system is constraints-driven: "if this bone transforms in this
way, then this should do that" (author). Organizing the logic per bone is
where the author reports spending most of the time.

### Phase 2: Build guide bones with Track To + Stretch

**Do**
1. Add guide bones (the bones that will track targets and stretch).
2. Give the guide bones a **Track To** constraint (they aim at their targets)
   **and also the Stretch modifier** (author: bones "had Track To and also
   had the Stretch modifier").

**Check**
- [inference] A guide bone points at its target and elongates; verify by
  moving the target and watching the bone track and stretch.

**Why**
Track To gives direction, Stretch gives distance response: the pair turns a
target's motion into a direction-plus-stretch signal the deform bones can
consume.

### Phase 3: Add Stretch To with low values on the deform bones

**Do**
1. On the bones that deform the mesh, add **Stretch To** constraints pointed
   at the guide bones from Phase 2.
2. Keep the Stretch To values **low** (author: "I used Stretch To with low
   values"). The author gives no numeric values, so start small and tune by
   eye.

**Check**
- [inference] The deform bone stretches subtly toward its guide bone; if it
  overshoots, the value is too high. "Low values" is the author's only
  guidance.

**Why**
Low-value Stretch To produces jiggle/second-motion fakery: enough to read
as soft-body response, not enough to break the silhouette. This is the
"fake simulation" the title promises.

### Phase 4: Drive behavior with Transform modifiers

**Do**
1. Add **Transform modifiers** (bone constraints) so that one bone's transform
   drives another's: "Everything uses Transform modifiers" (author).
2. Author more conditional logic: "if this bone transforms in this way, then
   this should do that" (author), i.e. map specific base-bone motions to
   specific deform-bone responses.

**Check**
- [inference] Pose the base bones through the character's range and confirm
  each dependent bone responds with the authored motion; adjust the mappings
  per bone.

**Why**
Transform modifiers are the control layer: they turn raw bone motion into
authored, repeatable secondary motion without any simulation solve or
blend-shape set.

### The human method, distilled

1. **Fake it with constraints, don't simulate.** Stretch To + Track To on
   guide bones gives soft-body read at zero sim cost.
2. **The system is simple on purpose:** "quite simple, so with a few small
   adjustments, you can adapt them to pretty much anything" (author).
3. **Spend the time on the logic graph,** not on more bones: organizing the
   if-this-transforms-then-that mappings is the real work.
4. **Low values on Stretch To** are the tuning rule of thumb; no numbers were
   published.

**Depth status:** PARTIAL. Evidence is the author's post selftext plus the
author's own explanatory comment (the exact modifier stack and the
base-bone-to-guide-bone architecture, all quoted). 42 comments were claimed
but only 3 were retrievable (Arctic Shift index gap; PullPush and old-Reddit
fallbacks returned nothing; reddit.com is blocked for direct fetch in this
loop), so the community's parameter guesses and the author's replies to
follow-ups are missing. No Stretch To values, no Blender version, no export
path to engine. The native clip itself (a demo, not a tutorial) was not
downloaded: the deepened pipeline targets YouTube/Vimeo and there is no
download script for v.redd.it, and a download of a demo reel would not have
yielded parameters beyond what the author's comment already states.

## 2. "Silco Hand Painted" (ImpressiveAct5779) - two posts, one artwork

Source: https://v.redd.it/cp1lq262woth1 (r/Substance3D post 1wyfrab, score 298,
3 comments) and https://v.redd.it/o4kyz4v0soth1 (r/3Dmodeling post 1wyf5cn,
score 187, 4 comments) | native clips. Same author, same character (Silco,
Arcane); the two posts are cross-posts of one artwork with two shading
variants: the r/Substance3D post's title names **Substance Painter // Zbrush
// Arnold Maya**, the r/3Dmodeling post's title names a toon variant
(**"Toon // Aistantard and Substance Painter"**, "Aistantard" read as
Arnold's aiStandardSurface shader).

Tools named: Substance 3D Painter, ZBrush, Arnold for Maya, aiStandardSurface
toon shading (all from titles only; the "Aistantard" reading is an inference
from the Arnold naming convention).

What the evidence supports: a hand-painted stylized character (Silco from
Arcane) sculpted in ZBrush, textured by hand painting in Substance Painter,
rendered in Arnold for Maya in two variants: a standard PBR look and a
toon-shaded look via aiStandardSurface.

Comments (r/3Dmodeling post only; the r/Substance3D post's 3 comments could
not be retrieved, Arctic Shift 422): a viewer saying "I'd kill for a course
on how to do exactly this", another viewer who "saw this on Instagram a few
days ago", and an AutoModerator process note. No author process breakdown,
no brush names, no shader parameter values, no render settings.

**Depth status:** DEPTH-LIMITED. Titles name the full tool stack and one
technique (hand painting; toon variant via aiStandard), but no workflow
detail exists in the retrievable evidence. A media download would only show
the finished render; it could not recover the painting process or shader
parameters. Stays in this report only per the standing rule (no thin
evidence into skills/).

## 3. "Rotating Dotted Sphere" (DigitCell)

Source: https://v.redd.it/4lgj94okyoth1 | r/proceduralgeneration post 1wyg4or
(score 55, 1 comment) | native clip

The only comment says "Dyson swarm". No tool, language, or technique is
named anywhere in the post or comments. Likely a shader/canvas demo (dot
pattern rotating on a sphere), but that is speculation, not evidence.

**Depth status:** NO-TOOLING. Zero tooling signal; excluded from the diff and
the watchlist.

---

## Per-repo have-vs-need

Repo evidence below is by keyword search of each inventory this run
(`substance|painter|zbrush|arnold|maya|hand-paint` absent in all four
inventories; `rig` present in aegis and 2d3d as noted below).

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Constraint-driven fake-simulation rigging (Stretch To + Track To, no sim/blend shapes) | #1 | NEED | `aegis-pipeline-inventory.md`: "No rigging / skinning / animation-retarget stage in the foundry" | Watchlist: new BACKLOGGED row this run; adjacent prior art for the P1 rig gap (fills it only if paired with automation), useful jiggle pattern at zero sim cost |
| Hand-painted stylized texturing (Substance Painter + ZBrush + Arnold Maya, toon aiStandard variant) | #2 | NEED | None of substance/painter/zbrush/arnold/maya appear in inventory | Watchlist: new WATCH row this run; stylized-character texturing reference (aigamedev/character bucket), pairs with existing `substance-painter-characters` skill |
| Rotating Dotted Sphere | #3 | - | Out of scope | Skip: no tooling |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Constraint-driven fake-simulation rigging | #1 | NEED | Inventory mentions "procedural rigs" only for generated 2D sprite art, nothing on constraint-driven 3D secondary motion | Skip: 2d3d is a 2D pixel-art pipeline; jiggle-by-constraint has no 3D rig to apply to |
| Hand-painted stylized texturing (Painter/ZBrush/Arnold) | #2 | NEED | No Painter/ZBrush/Arnold stage in inventory | Watchlist: hand-painted stylization reference for 2d3d's toon look; technique-transfer only, not a stage adoption |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Constraint-driven fake-simulation rigging | #1 | NEED | No rigging stage in inventory | Skip: cozy city-builder has no characters to jiggle |
| Hand-painted stylized texturing (Painter/ZBrush/Arnold) | #2 | NEED | No Painter/ZBrush/Arnold stage in inventory | Watchlist: toon-shading reference for the cozy aesthetic; stylization guidance only |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Constraint-driven fake-simulation rigging | #1 | NEED | No rigging stage in inventory | Watchlist: cheap secondary-motion pattern for space units/cinematics without sim overhead |
| Hand-painted stylized texturing (Painter/ZBrush/Arnold) | #2 | NEED | No Painter/ZBrush/Arnold stage in inventory | Watchlist: stylized ship/station texturing reference |

## Gap recommendations (highest-leverage NEEDs)

None this run that clear the bar. The two extracted pipeline patterns are
watchlist-grade, not gap-fillers:

1. Constraint-driven fake-simulation rigging (audit #1) is adjacent to the
   P1 rigging/retarget gap (aegis) but fills only the "secondary motion
   cheaply" slice; the gap's automation core (auto-rig, skinning, retarget)
   remains untouched. Next step if wanted: spike the Stretch To/Track To
   guide-bone pattern on one Aegis character asset and measure rig-time vs
   the current manual approach.
2. Hand-painted toon texturing (audit #2) is a style reference for Desktop
   City and 2d3d, not a pipeline stage adoption.
3. The standing highest-leverage items remain the 2026-10-05 set (OmniChar
   acceptance-spec template for Aegis P1; Marigold V2 eval for 2d3d; Flux
   klein on watchlist; YEDP notes for the rig gap; Hillaire LUT atmosphere).

## Watchlist trending

## Watchlist trending
- MCP servers driving Blender/Unreal (agentic DCC) (first seen 2026-09-27, status BACKLOGGED; seen again 2026-09-28, 2026-10-05, 2026-10-06, 2026-10-07) **TRENDING**
- Squishy Volumes (free Blender MPM soft-body, fracture upcoming) (first seen 2026-09-27, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07) **TRENDING**
- Procedural ribbon cables (Blender GeoNodes) (first seen 2026-09-27, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07) **TRENDING**
- Light Wrangler Blender add-on (gobo lighting rigs) (first seen 2026-09-27, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07) **TRENDING**
- Codex CLI driving Blender via MCP (mannequin-guided camera motion) (first seen 2026-09-28, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07) **TRENDING**
- GPT Astra (mesh split, UV fix, CC0 texture replacement; Blender MCP looping) (first seen 2026-09-28, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07) **TRENDING**
- HBLink (Blender<->Houdini live-link + cache bridge, Gumroad, by Itz_Keay) (first seen 2026-09-28, status BACKLOGGED; seen again 2026-10-05, 2026-10-06, 2026-10-07) **TRENDING**
- Raup shell morphospace (flare/verm/spire parametric 3D generation; snug-fit rule verm=1/flare; Blender geo nodes + TouchDesigner; Blender/TouchDesigner files on Patreon) (first seen 2026-09-27, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07) **TRENDING**
- Blender + After Effects + DaVinci Resolve VFX finishing pipeline (first seen 2026-10-06, status WATCH; seen again 2026-10-07)
- Tripo Smart Mesh P2.0 (multi-view to 3D + Tripo rigging) (first seen 2026-09-28, status BACKLOGGED; seen again 2026-10-05, 2026-10-06, 2026-10-07) **TRENDING**
- GrandpaCAD (T-pose character generation + rigging) (first seen 2026-09-28, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07)
- Rigify manual character rigging (extra controllers, FK arms) (first seen 2026-09-30, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07)

Analyst note: the rows above Blender + After Effects + DaVinci Resolve
matched on the generic "Blender" token only (audit #1 names Blender; audit
#2 names no generic Blender token but "ZBrush"/"Arnold"/"Maya" tokens did not
hit those rows) and are weak signals for this run, not genuine
reappearances. Genuine token matches this run are **Tripo Smart Mesh P2.0**,
**GrandpaCAD**, and **Rigify manual character rigging**, all matched on the
"rigging" keyword against audit #1 (the Blender fake-simulation rigging
post). Tripo Smart Mesh P2.0 is the one genuinely relevant reappearance:
its auto-rigging is the closest existing answer to the P1 rig gap, and its
second sighting reinforces its BACKLOGGED standing.

## New watchlist additions (2026-10-07)

Appended to `references/tooling-watchlist.md` (append-only) and synced to the
public mirror:

| Date seen | Tool / stage | Seen in | Status | Note |
|-----------|--------------|---------|--------|------|
| 2026-10-07 | Constraint-driven "fake simulation" rigging (Blender Stretch To + Track To, no sim or blend shapes) | r/3Dmodeling "Blender 3d Rigging performed without simulation or body blend shapes" (Broad-Requirement-83) | BACKLOGGED | Chain: base bone -> modifier -> constraints -> guide bone -> modifier (transform, location, etc.) -> constraints; Stretch To at low values anchored to Track To+Stretch guide bones; adaptable fake-cloth/jiggle at zero sim cost; manual-only, does NOT fill the P1 rig/retarget gap (no automation) |
| 2026-10-07 | Hand-painted stylized character texturing (Substance Painter + ZBrush + Arnold Maya, toon aiStandardSurface variant) | r/Substance3D + r/3Dmodeling "Silco Hand Painted" cross-posts (ImpressiveAct5779) | WATCH | Tool stack named in titles only; no workflow detail retrievable; stylized/Arcane-look reference; pairs with existing substance-painter-characters skill |

## Depth-escalation usage

- Mode: `pre-approved`, allowance 2 media downloads.
- Downloads attempted: 0. Downloads succeeded: 0. Skipped on approval gate: 0.
- All 4 videos are native Reddit clips (v.redd.it). The deepened pipeline
  (download + frames, captions as text fallback) targets YouTube/Vimeo; no
  download script exists for v.redd.it in the skill path, so the allowance
  went unused. Audit #1's audit is PARTIAL from the author's own comment
  (the exact constraint architecture); a clip download would show the demo
  reel only and would not yield parameters the author's comment did not
  already state. Audits #2/#3 would gain nothing from a download (finished
  render / dot-pattern demo).

## Non-goals (found but correctly skipped)

- Audit #2's finished-render content: titles only; no recoverable workflow.
- r/comfyui, r/technicalart, r/vfx, r/Simulated, r/gamedev: Arctic Shift
  returned HTTP 422 this run; their video posts went unscanned.
- PullPush + old-Reddit fallbacks for r/3Dmodeling post 1wyclry: returned
  empty; reddit.com direct fetch is blocked in this loop, so the post's 39
  unretrieved comments stay unexamined.

## Publishing

Staged in `~/workspace/video-tooling-scout-public/` as ready-to-publish
(browser upload when Ehsan is present; never unattended):
- 1 new skill: `skills/blender-fake-sim-rigging/` (from audit #1, PARTIAL
  with extractable constraint workflow; inferences labeled). Audits #2
  (DEPTH-LIMITED) and #3 (NO-TOOLING) stay in this report only per the
  standing rule.
- Full report: `docs/scout-reports/have-vs-need-2026-10-07.md` (+ README index
  row; skill count 43 -> 44).
- Watchlist mirror synced: `video-tooling-scout/references/tooling-watchlist.md`.
