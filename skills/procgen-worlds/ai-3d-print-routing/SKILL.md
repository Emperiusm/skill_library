---
name: ai-3d-print-routing
description: "Route AI output between printable STL shells and textured, editable 3D assets: the print-versus-render decision, watertight and manifold requirements, and the asymmetry rule that one direction is cheap and the other is nearly impossible. Trigger when deciding whether an AI model should print or render."
---

# Print Routing for AI 3D Assets

## Purpose

This skill routes AI output to the right destination before work
starts, because print and render demand opposite things from the same
input. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle). The core
method is: decide the destination first, apply that destination's
acceptance criteria only, and respect the asymmetry between the two
directions.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/image-to-stl-vs-image-to-3d-model
- https://customuse.com/learn/text-to-stl-vs-text-to-3d-model

## Tools used

Tools used: image-to-3D and text-to-3D generators (including Sloyd,
named in the STL articles, for controllable low-poly forms); slicers
for print validation; DCC tools for render-side finishing.

## Phase 1: Decide print or render before generating

**Do**
1. Name the destination first: a physical object (print) or a screen
   asset (render). The input lane is either a photo or a prompt, but
   the routing decision is the same.
2. Apply only that destination's acceptance criteria:
   - Print: watertight and manifold geometry, adequate wall
     thickness, millimeter scale, clean STL.
   - Render: topology, UVs, PBR materials, rig where applicable,
     engine-ready export.
3. Do not try to satisfy both sets at once: a model optimized for
   both is optimized for neither.

**Check**
- Is the destination written down before generation?
- Are you judging the output by the destination's criteria, not the
  other destination's?

**Why**
Same input, different acceptance criteria. A beautiful textured mesh
that is not watertight is a failed print; a watertight shell with no
UVs is a failed render. The routing decision prevents paying for the
wrong kind of quality.

## Phase 2: Run the print-side solidity pass

**Do**
1. Check watertightness: no holes, no open edges, no non-manifold
   geometry.
2. Check wall thickness against the printer and material: thin walls
   that slice are thin walls that break.
3. Set millimeter scale deliberately and verify it in the slicer,
   not in a viewer.
4. Export a clean STL (or 3MF where the pipeline supports it) and
   slice-test it before calling it done.

**Check**
- Does it slice cleanly with no errors?
- Is the scale in millimeters and verified in the slicer?
- Is there a `print-validation.log` with pass/fail lines for the
  validator, the slicer analysis, the layer-preview scroll, wall
  thickness, and the dimension check?

**Why**
A slicer is the print world's engine import: the only proof that
counts. Viewers hide the holes that slicers refuse.

## Phase 3: Respect the asymmetry rule

**Do**
1. Remember the asymmetry: a model built for a screen can be exported
   to STL after a solidity pass, but an STL rarely back-fills into a
   textured, animated, game-ready asset.
2. When in doubt about the destination, generate for the screen first
   and derive the print from it, not the reverse.
3. When the destination is definitely print, skip render work
   entirely: topology, UVs, textures, and rigs are wasted effort on a
   shell.

**Check**
- If this asset later needs to render, is the screen-side source
  still available, or was only the STL kept?
- Did the team pay for render work on a print-only asset?

**Why**
The asymmetry is a one-way door. Keeping the richer source preserves
options; keeping only the STL destroys them. Routing decisions are
cheap at the start and expensive to reverse.

## Phase 4: A/B test with a single brief when unsure

**Do**
1. When the destination is genuinely uncertain, run a single-brief
   A/B test: the same photo or prompt through both lanes, then judge
   each output by its own destination's criteria.
2. Record which lane won and why, so the next asset in the set does
   not re-litigate the routing.

**Check**
- Was each output judged by its own criteria?
- Is the routing decision recorded for the set?

**Why**
A bake-off settles routing with evidence instead of debate, and the
record compounds: the second asset's routing decision is free.

## Production practice (print and manufacturing anchor)

This skill has no game-studio anchor: print acceptance is a
manufacturing question, not a games question. The practices below
come from print-production sources, and the automation is a
validation log, not a new claim about printability:

- **Two independent validators, then the slicer.** Run an automated
  manifold/watertight check, get a second opinion from the slicer's
  own analysis tool (different tools use different detection
  algorithms), manually inspect boolean junctions, dense organic
  detail, and joints in wireframe, then validate in the slicer
  itself: slice at a standard layer height, scroll the layer preview
  for missing layers or unexpected material islands, and confirm
  physical dimensions against intent (unit-scale errors print a
  100 mm part at 10 mm).
  (Source: https://www.tripo3d.ai/blog/explore/3d-printing-model-marketplace-requirements-manifold-watertight)
- **Manifold means exactly two faces per edge, normals outward.**
  A watertight mesh has no holes, no gaps, and no edge shared by
  fewer or more than two triangles; flipped patches read as voids
  in the slice. Tessellation error should sit comfortably below
  both the smallest meaningful feature and the process resolution;
  past that point extra facets only slow every downstream step.
  (Source: https://www.acsmaterial.com/blog-detail/preparing-files-for-3d-printing.html)
- **Prefer 3MF where the pipeline supports it.** The 3MF container
  enforces valid topology rules at the container level instead of
  leaving slicers to guess inside versus outside, and a 3MF project
  carries placement, supports, and filament profiles with the
  geometry, so the next print reruns a tested process rather than
  just a shape.
  (Source: https://blog.fileformat.com/cad/3mf-vs-stl-why-3mf-could-replace-stl-for-modern-3d-printing-workflows/)
- **Automation (agent-executable):** write a `print-validation.log`
  per asset with one pass/fail line each for the automated
  validator, the slicer analysis, the layer-preview scroll, wall
  thickness versus printer/material, and the dimension check
  (intended versus slicer-reported size in millimeters); keep the
  richer screen-side source file alongside the STL/3MF so the
  asymmetry rule stays enforceable. (Inference: the log format
  applies the two sources' checks to this skill's Phase 2.)

## The human method, distilled

1. Destination first, generation second.
2. Print means watertight, manifold, millimeter scale, clean STL.
3. Render means topology, UVs, PBR, rig, verified export.
4. Screen to print is a solidity pass; print to screen is nearly
   impossible. Keep the richer source.
5. Uncertain? Single-brief A/B test, judged per destination.

## Depth status

FULL (article text).
