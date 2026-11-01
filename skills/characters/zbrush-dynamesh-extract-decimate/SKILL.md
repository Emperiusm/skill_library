---
name: zbrush-dynamesh-extract-decimate
description: "Sculpt a character with zero booleans: one Dynamesh for the whole body, extract pieces out of it, harden edges with remesh/extrude/subdivide, alphas for micro-detail, Decimation Master from 250M to 10M polys, Marmoset Toolbag renders. Trigger when a ZBrush character needs clean extracted pieces without boolean seams."
---

# ZBrush Character Workflow: Dynamesh, Extract, Decimate

## Purpose

This skill follows Clear-Counter-640's character workflow for the
ZBrush 2027 beta testing program: **one Dynamesh for the whole
character, extract the pieces, remesh/extrude/subdivide for sharp
edges, alphas for micro-detail, no booleans anywhere.** Sculpt at
absurd density, decimate with Decimation Master, render in Marmoset
Toolbag. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle).

## Source

r/3Dmodeling, Clear-Counter-640, "3D Character I did for Zbrush 2027
beta testing program" (score 196, 34 comments, 2026-10-30):

- https://www.reddit.com/r/3Dmodeling/comments/1xjls24/
- Native Reddit video: v.redd.it/0ykme5q3vmyh1

Evidence note: all facts below are the author's claims from the post
text plus the author's workflow comments. The 2027-beta tool
specifics are under NDA (stated, not hidden); the geometry workflow
itself is fully described. No third-party verification in this audit.

## Tools used

- ZBrush (2027 beta; the author worked with Maxon directly testing new
  tools, under NDA for the specifics)
- Dynamesh (the whole character starts as one)
- Extract, remesh, extrude, subdivide
- Alphas (for the small details)
- Decimation Master
- Marmoset Toolbag (final renders)

## Phase 1: Block the whole character as one Dynamesh

**Do**
1. Start the entire character as a single Dynamesh.
2. Extract the pieces out of that Dynamesh. The author is explicit:
   "Not a single Boolean actually, it started as a dynamesh for the
   whole character, then making pieces by extracting out of that
   dynamesh."

**Check**
- Pieces separate cleanly with no boolean seams to clean up.

**Why**
Extraction from one Dynamesh keeps every piece in the same sculptural
language; booleans would introduce hard-surface seams into an organic
character.

## Phase 2: Harden edges with remesh/extrude/subdivide

**Do**
1. Remesh, extrude, and subdivide the extracted pieces to get sharp
   edges.
2. Use alphas for the small details.
3. Budget brute-force subdivision instead of optimizing early. The
   author's machine is a 5950X with 64 GB DDR4: "I just needed mesh
   resolution to use some alphas and the only way was to subdivide
   it." Optimization would have taken "10 times more" than the
   brute-force subdivide, and he works 2-3 pieces per day on personal
   time.

**Check**
- Edges read sharp at render distance; micro-detail comes from
  alphas, not geometry.
- Watch the clock: if an optimization pass takes longer than a day of
  brute-force subdividing, subdivide.

**Why**
Topology operations (remesh/extrude/subdivide) carry the form; alphas
carry the detail. On personal time, brute force beats cleverness when
the hardware can take it (5950X + 64 GB DDR4 handled 250M polys).

## Phase 3: Decimate and render

**Do**
1. Decimate the 250M-polygon character with Decimation Master down to
   10M.
2. Export to Marmoset Toolbag for the final renders.

**Check**
- 250M → 10M (25x reduction) with silhouette and alphas intact.

**Why**
Sculpt at absurd density, render at sane density; Decimation Master is
the bridge, Marmoset is the presentation.

## AAA studio practice

The core gesture of this skill, **extracting pieces from a masked body
instead of using booleans**, is standard practice among production
character artists, not a personal quirk.

1. **Extraction from masks is the standard way garments and parts are
   derived from the body.** Yuriy Barchuk (80 Level, Oct 2026): "The
   clothing was originally blocked out by extracting meshes from masks on
   the main body and using different tools to move them into place."
   Eric Liu (80 Level, Oct 2026; 10+ years in game art, including
   outsourcing work on *Marvel Rivals* and *Path of Exile*): "for the
   gum, I masked that area of the mouth and extracted it. The clothing
   was created with a similar method." In studios this is how armor,
   clothing, and gum/teeth pieces start life.
   - https://80.lv/articles/sculpting-scales-simulating-clothes-for-creature-chef-in-zbrush-marvelous-designer
   - https://80.lv/articles/sculpting-texturing-a-semi-realistic-lobo-bust-with-zbrush-substance-3d
2. **ZRemesh after blockout/extract for clean topology before detail
   sculpting.** Barchuk ZRemeshed the Dynameshed body "to ensure I had
   relatively clean topology to sculpt on" before layering detail and
   before clothing simulation; Liu ZRemeshed "several times and reduced
   the polycount to make it easier to fix and tidy the edge flow for
   later use in the pipeline." Inference: this skill's brute-force
   subdivide-only approach skips that step. On a studio timeline the
   ZRemesh step buys cheaper detail passes and topology that downstream
   steps can use, where the author's personal-time brute force
   ("optimization would have taken 10 times more") only wins when one
   person owns every step.
   - https://80.lv/articles/sculpting-scales-simulating-clothes-for-creature-chef-in-zbrush-marvelous-designer
   - https://80.lv/articles/sculpting-texturing-a-semi-realistic-lobo-bust-with-zbrush-substance-3d
3. **Decimation is a bake bridge, not just an export step.** Liu baked
   curvature, cavity, convexity, AO, position, normal, and world normal
   maps in Marmoset Toolbag from the high poly before texturing in
   Substance 3D Painter. Jueon Kim (80 Level, Oct 2026) enables Keep UVs
   in ZBrush's Decimation Master to preserve UVs during optimization,
   pairing it with ProOptimizer in 3ds Max for final counts. Inference:
   if the decimated 10M mesh is headed to a bake or texturing stage,
   preserve UVs at decimation time; otherwise that work is rebuilt later.
   - https://80.lv/articles/sculpting-texturing-a-semi-realistic-lobo-bust-with-zbrush-substance-3d
   - https://80.lv/articles/breakdown-giant-robot-in-cathedral-ruins-made-in-3d
4. **Presentation setup starts early, not after texturing.** Liu put the
   model into Marmoset Toolbag "once I was halfway through texturing" to
   begin the lighting setup (spotlight key, directional fill, rim lights
   for silhouette), rather than treating the render as a final pass.
   Inference: save the Marmoset scene as a reusable template and
   re-render per pass instead of re-lighting per render.
   - https://80.lv/articles/sculpting-texturing-a-semi-realistic-lobo-bust-with-zbrush-substance-3d

## Agent automation

**Do**
1. Write `proportions.md` before sculpting: the chosen proportion system
   (the skill's 8-head ideal vs 7.5-head realistic), the head-unit
   landmarks for the character, and a per-piece checklist: piece name,
   source body region, target silhouette landmark. No piece gets
   extracted without a checklist line.
2. Record the extract, remesh, extrude, and subdivide sequence as a
   ZBrush macro (.txt) once per piece family and replay it for the rest.
   Inference: ZBrush macro recording replays UI actions; verify the
   recording captures the parameter panel entries for your ZBrush
   version before depending on it.
3. Density budget log: per SubTool, log the subdivision level and poly
   count before decimation, then the decimated count. Gate: 25x
   reduction (250M to 10M per the skill) or your own target. If a piece
   loses silhouette after decimation, it fails the gate and goes back to
   Phase 2.
4. Silhouette check: render a turntable of the decimated mesh and compare
   frames against the 250M sculpt; log the comparison in the run log.
   Acceptance is the author's own check: edges read sharp at render
   distance, micro-detail from alphas intact.
5. If the decimated mesh heads to texturing: enable Keep UVs at
   decimation and record the bake manifest (curvature, cavity, AO,
   normal) with cage/skew notes, per the Liu/Kim practice above.
6. Save one Marmoset Toolbag scene as the lighting template (key, fill,
   rim, tone mapping) and reuse it for every render pass.

**Check**
- File manifest exists: `proportions.md`, density budget log, macro
  .txt, decimation report (before/after counts), turntable frames,
  Marmoset template scene.
- Every piece on the checklist is extract-derived with no boolean
  seams; no piece ships past the density gate without a logged check.

**Why**
The author's workflow lives in memory (5950X, personal time, a
tutorial pack that ships later). A proportion sheet, a recorded macro,
a density log, and a lighting template make the same workflow
reproducible by another agent with no access to the author.

## The human method, distilled

1. **"Not a single Boolean"**, extraction over booleans for organic
   hard pieces.
2. **Pick the proportion system before sculpting**: the 8-head ideal
   figure ("that's the ideal proportions most artists use, specially
   for women, that longer legs add more feminine") vs 7.5 heads for a
   realistic street human.
3. The author is shipping a project-based beginner tutorial pack
   (sphere, orange, keyboard, gun, Fortnite-style full character),
   watch his Instagram for the release.

**Depth status:** FULL (author post text + author comments; the actual
2027-beta tool specifics are under NDA, which is stated, not hidden).
