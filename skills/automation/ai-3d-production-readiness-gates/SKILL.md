---
name: ai-3d-production-readiness-gates
description: "Decide whether an AI asset can be handed to the next person without repair: a five-level quality ladder, an inspection list, a decision matrix by asset type, and pass, revise, and reject gates that apply to every destination. Trigger when gating an AI asset for handoff."
---

# Production-Readiness Gates for AI 3D Assets

## Purpose

This skill is a gate framework, not a build procedure: it decides
whether an asset passes, needs revision, or gets rejected, for any
destination (games, VFX, product, print), not just game props. Every
phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The core method is:
grade the level, inspect against the list, apply the gate, and let
cleanup cost decide the close calls.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/production-ready-ai-3d-assets
- https://customuse.com/learn/production-ready-ai-3d-asset-checklist
- https://customuse.com/learn/ai-3d-model-generator-after-first-mesh
- https://customuse.com/learn/ai-3d-asset-generator

Evidence note: the asset-generator article was read firsthand by the
parent agent in full; one member article's tail was additional-details
only. All substantive sections were read.

## Tools used

Tools used: DCC tools and engines as inspection and import endpoints.
No gate tool is prescribed; the ladder, list, and gate rules are the
deliverable.

## Phase 1: Grade the asset on the quality ladder

**Do**
1. Grade the asset honestly on five levels, and buy against the level
   actually needed, not the prettiest possible output:
   - Level 1, preview: looks good in a thumbnail, but the mesh may be
     messy, hollow, or impossible to edit cleanly.
   - Level 2, concept asset: communicates a direction and can be
     shown in reviews. Allowed to be imperfect because its job is to
     settle a decision.
   - Level 3, editable asset: can be opened, inspected, separated
     into parts, retextured, or cleaned without falling apart.
   - Level 4, workflow asset: moves through retopology, PBR texturing,
     rigging, optimization, export, and review as a repeatable
     process rather than a one-off rescue job.
   - Level 5, production-ready for a specific context: meets the exact
     requirements of the target engine, renderer, shot, marketplace,
     or product workflow.
2. Name the target level before gating. An asset can be production-
   ready for a thumbnail and not for an engine; "production-ready"
   without a context is meaningless.

**Check**
- Is the target level written down, with the context attached?
- Most tools reliably produce Level 1 or 2. Is this asset being
  graded as if it were Level 5 without the work that earns it?

**Why**
The level framing prevents the central category error in AI 3D: paying
Level 5 prices for Level 2 output, or rejecting Level 2 output for not
being Level 5 when Level 2 was the job. The real competition, and the
real cost, lives in Levels 3 through 5.

## Phase 2: Inspect against the list

**Do**
1. Run the inspection list before trusting any output:
   - Geometry: solid, or hollow and full of holes?
   - Topology: quad-based with clean edge flow, or dense triangle
     soup?
   - Scale: real-world size, or 0.01x?
   - Texture quality: sharp at the resolution the context needs?
   - Material separation: metal, fabric, and glass on separate slots,
     or fused into one painted map?
   - UVs: usable layout, or overlapping and unworkable?
   - Polycount: within the target platform's budget?
   - Rigging or deformation needs: will the edge flow allow animation?
   - Export format: the file the pipeline expects?
   - Import behavior: opens cleanly in Blender, Unity, or Unreal
     without errors?
   - Cleanup time: how long until it is actually usable?
2. For professional teams, treat cleanup time as the hidden cost: the
   fastest generator is not always the fastest pipeline.

**Check**
- Every list item answered, not just the photogenic ones?
- Is cleanup time estimated, or is it the number nobody measured?

**Why**
The list exists because previews hide exactly these failures. An asset
that passes the list is an asset the next person can use without
repair, which is the definition of handoff-ready.

## Phase 3: Apply the gate and let cleanup cost decide

**Do**
1. Apply the eight-check gate: any single failure rejects the asset
   for handoff (it may still serve concepting or grayboxing). Run the
   six destination gates alongside it: the asset must satisfy the
   requirements of its specific destination, not gates in general.
2. Decide refine versus regenerate: refine when the mesh has good
   proportions and only needs better edge flow, materials, or export;
   regenerate when the base is fused, locked, or broken beyond repair.
3. Run the 20-minute usability test: can this asset be made usable
   within about 20 minutes of work? If not, it is not a refinement
   candidate; it is a regeneration candidate.
4. Let cleanup cost decide the close calls: a tool that gives a
   stunning Level 2 preview but a Level 3 mesh that takes a day to
   clean is not faster; it just moves the bottleneck downstream.

**Check**
- Pass, revise, or reject: is the verdict recorded with the failing
  checks named?
- Was the 20-minute test actually run, or was the verdict guessed?

**Why**
Gates work only when they are binary and recorded. A gate that
everyone negotiates per asset is not a gate; it is a conversation that
repeats on every handoff.

## Phase 4: Use the decision matrix for buying

**Do**
1. Map the asset's job to how much finishing work stands between a
   raw output and a usable asset, graded Often, Sometimes, or Rarely
   for "generator output ships as-is":
   - Concept or mood: Often. Deciding factor is strong directions per
     minute.
   - Game prop: Rarely. Deciding factor is retopology, texturing, and
     FBX or GLB export beyond the mesh.
   - Character: Rarely. Generation gives a base; rigging and topology
     cleanup decide if it animates.
   - Environment: Rarely. Assembly, scale alignment, and optimization
     across many parts.
   - Product visual: Rarely. The model as a controlled source of truth
     so variations do not drift.
   - 3D print: Sometimes. Whether the mesh is solid enough to slice.
2. The moment a row reads Rarely, stop asking which generator makes
   the best preview and start asking which environment lets the team
   finish the asset.

**Check**
- Is the row for this asset's job Rarely? If yes, is the team staffed
  and tooled for finishing, or still shopping for previews?
- Does the tool choice match the asset's next step? Show a concept
  means speed matters; ship in a game means topology, materials,
  rigging, and export matter; hold a shot means scene control
  matters; launch product imagery means consistency matters.

**Why**
The pattern is consistent: a generator can start any asset, but only a
workflow turns the start into a deliverable. The buying rule follows
from it: the best generator is the one that makes the next step
easier, not the one that creates the prettiest isolated preview.

## The worked example, in miniature

A small studio needs a stylized lantern for a mobile game, budgeted at
roughly 3,000 triangles with separate metal and glass materials, ready
as a GLB. Concept (minutes): four variations from a prompt, one
picked, refined with a reference image for the metalwork; Level 2.
High-poly generation (minutes): image-to-3D produces a roughly
30,000-triangle triangulated mesh with one baked texture; Level 1.
Retopology: down to a clean about 3,000-triangle low-poly cage with
usable edge flow; Level 3. Texturing: PBR maps baked from the
high-poly onto the low-poly (albedo, normal, roughness, metallic),
metal and glass on separate slots, carried as a repeatable rerunnable
chain; Level 4. Export and import check: GLB at the right scale, opens
cleanly in the engine, renders correctly under the game's lighting;
Level 5 for this context. Review: team sign-off, same graph reused for
the next twelve lanterns. The generator did the first two steps in
minutes; steps three through six are where production lives.

## The human method, distilled

1. Grade the level, name the context. Level without context is noise.
2. Inspect against the list, including cleanup time.
3. Any single gate failure rejects for handoff. Record the verdict.
4. 20-minute test decides refine versus regenerate.
5. Cleanup cost decides close calls. A preview that costs a day of
   cleanup is not fast.
6. Buy by the asset's next step, never by preview beauty.

## AAA studio practice

- **QA is two script hooks, not a human checklist.** A published
  automated-QA workflow for 3D assets (Tripo blog) runs
  post-generation scripts immediately after an asset is created
  and pre-export scripts before it leaves the DCC tool. The checks
  are scripted: albedo tagged sRGB while roughness, metallic, and
  normal maps are linear; UV seam-bleed sampled along texture
  borders; mipmaps validated; roughness and metallic maps at the
  same resolution as albedo; normal maps in the correct tangent
  space; material files referencing textures that actually exist.
  Source: https://www.tripo3d.ai/blog/explore/automated-qa-checks-for-meshes-and-textures
- **Whole-library validation runs as a node network, not one
  asset at a time.** A Game Developer piece on procedural
  pipelines uses Houdini's Procedural Dependency Graph to check
  an entire asset library for required attributes (UV, UV2 for
  lightmaps and blending, vertex colors including alpha, vertex
  normals), driven by a parameter any team member can change, and
  distributable to a compute farm instead of waiting for someone
  to complain after release.
  Source: https://www.gamedeveloper.com/programming/streamline-your-pipeline-with-procedural-workflows-automation

**Automation upgrade (agent-executable, derived from the above)**
1. Convert the Phase 2 inspection list into two scripts:
   `qa-post-generation` (runs on every raw output) and
   `qa-pre-export` (runs before handoff). Each writes a
   `qa-report.json` with one pass/fail entry per check, naming the
   failing check; the gate verdict in Phase 3 reads this report,
   not a human's impression.
2. Add the scripted checks the sources name explicitly: color
   space per map type, UV seam-bleed sampling, mipmap presence,
   PBR map resolution parity, normal tangent space, and material
   file path existence.
3. Run the library-level check as a batch: the same check set over
   every asset in the folder, with a summary report (asset, failed
   checks) so one bad export cannot hide among good ones.
4. Record the 20-minute usability test result in the gate log
   (minutes spent, usable or not) instead of estimating it.

## Depth status

FULL (article text).
