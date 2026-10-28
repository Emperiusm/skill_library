---
name: ai-3d-game-prop-pipeline
description: "Take an AI-generated game prop from constrained brief to in-engine verification: candidates, retopology, PBR texturing, LODs, export, and a go/no-go gate, with the recipe saved so the next prop in the set costs a fraction of the first. Trigger when making game-ready props with AI."
---

# AI Game-Prop Pipeline: Brief to In-Engine Verification

## Purpose

This skill turns a generated first mesh into a shippable game prop through
a fixed staged chain, so cleanup debt does not arrive at import time.
Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The core method is:
constrain the brief, pick the cleanest candidate, repair it in stages,
prove it in the engine, and save the recipe.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/generate-game-ready-props-with-ai
- https://customuse.com/learn/making-game-ready-3d-models-with-ai
- https://customuse.com/learn/ai-3d-tools-for-game-assets
- https://customuse.com/learn/ai-3d-asset-pipeline
- https://customuse.com/learn/ai-3d-for-indie-game-developers

Evidence note: the articles' substantive sections were read; only minor
FAQ tails were unseen. CustomUse node and canvas steps described in the
sources are generic workflow stages, not verified product instructions:
no pricing, plan limits, or click-level CustomUse settings appear in the
sources.

## Tools used

Tools used: AI generators (Meshy, Tripo, Rodin/Hyper3D, 3D AI Studio for
first meshes; Sloyd for parametric low-poly props; Kaedim as a
human-in-the-loop cleanup service), DCC tools (Blender, Maya, Substance,
Houdini) for finishing, engines (Unity, Unreal, Fab, Roblox, UEFN) as
destinations. Generators are compared by role, not as if interchangeable.

## Phase 1: Constrain the brief and generate candidates

**Do**
1. Write the brief with the destination attached: engine, role (hero,
   background), triangle budget, texture budget, and format. A prop
   without a budget is not a brief.
2. Generate 3 to 6 candidates and pick the cleanest base: strong
   silhouette, even surface, separable parts. Do not fight the first
   result when a cleaner candidate exists.

**Check**
- Can you state the budget tier this prop was approved for before
  generating?
- Does the picked candidate have the strongest silhouette and the
  least fused geometry of the set?

**Why**
Candidate selection is the cheapest cleanup step in the pipeline. A
strong silhouette with even surface saves far more downstream time than
any repair pass recovers.

## Phase 2: Inspect the first mesh and decide repair vs regenerate

**Do**
1. Orbit the mesh and read it from every angle that matters for the
   job, including the back the generator invented.
2. Flag fused parts (a lid fused to a body, a strap fused to a shell),
   holes, flipped normals, and baked-in lighting in the texture.
3. Decide: repair when proportions are good and only edge flow needs
   work; regenerate from better reference when limbs are fused, the
   pose is locked mid-action, or intersections are everywhere.

**Check**
- Is every important part separated with a sane hierarchy?
- Does the mesh hold up from the angles that matter, not just the
  preview angle?

**Why**
The first mesh took under a minute; everything that makes it shippable
happens after it. Repairing a bad base costs more than picking a better
candidate or regenerating once.

## Phase 3: Retopologize and unwrap

**Do**
1. Auto-retopologize to a quad-dominant low-poly cage at the budget
   (worked examples: a 240K-triangle lantern to about 3K, a 90K-triangle
   crate to about 2,400), keeping the high-poly aside for baking.
2. Hand-fix the spots auto passes leave behind, such as a pinched
   handle loop.
3. Unwrap with hidden seams (down the back edge on the lantern) and
   even texel density across materials.

**Check**
- Triangle count is inside the approved budget tier, LODs included.
- Topology matches the job: deforming for anything animated,
  simplest-possible for anything static.

**Why**
Retopology is what turns triangle soup into an editable asset: a mesh
you can open, separate, and rework without it falling apart.

## Phase 4: Bake and texture with separated PBR slots

**Do**
1. Bake high-poly detail into a normal map.
2. Generate PBR maps (albedo without baked shadows, normal, roughness,
   metallic) on separated material slots: metal and glass apart, never
   one fused painted map.
3. Confirm the maps read correctly under the level's directional light,
   not just the generator's flat preview. Add small decals (a maker's
   mark) only after the base maps read clean.

**Check**
- Do materials behave under real lighting, with no baked-in shadows?
- Are metal, fabric, and glass on separate slots that bind to your
  shaders?

**Why**
A fused texture looks right in a viewer and wrong everywhere else. PBR
separation is what lets the asset respond to scene lighting instead of
wearing the generator's lighting forever.

## Phase 5: Optimize, export, and prove in the engine

**Do**
1. Generate LOD1 and LOD2, compress textures, add a collision proxy
   (a collision box on the crate), and move the pivot to the base so
   the prop sits on the floor correctly.
2. Export GLB and FBX (FBX for rigged or engine handoff, GLB for
   PBR-first delivery) at the right scale and axes: the lantern should
   be about 30 cm tall, not 30 m.
3. Import into the actual engine and confirm 1:1 scale, material slots
   intact, normals not inverted, and no warnings. Drop it into the real
   level, lit with the level's lighting, viewed at gameplay distance
   and up close.

**Check**
- Did it survive a real import, not a viewer preview?
- Did it survive a real in-context review, not just a preview?
- Is the import logged as a pass/fail record (scale, slots, normals,
  warnings) rather than a screenshot?

**Why**
Viewer previews hide scale, slot, and lighting failures. The engine
import is the acceptance test; everything before it is preparation.

## Phase 6: Gate it and save the recipe

**Do**
1. Run the final go/no-go before the asset enters source control. Every
   line is a hard yes or no, and any no sends it back:
   - Scale, materials, and skeleton survived a real import.
   - Polycount is inside the approved budget tier, LODs included.
   - Topology matches its job.
   - The recipe that produced it is saved, so the next asset in the set
     does not start from zero.
   - Per-asset cleanup time is sustainable at the quantity left to
     ship, not just for this one.
2. Save the recipe (same UV scheme, same trim sheet, same export
   preset) so the next twelve props in the set start from a working
   template, with only the silhouette changing.

**Check**
- Miss any go/no-go line and the asset is still useful for concepting
  or grayboxing, but it is not ready to commit.
- Can another team member understand and rerun the workflow?

**Why**
Steps 1 through 5 made one prop. The saved recipe is what makes props
two through thirteen cost a fraction of the first, which is where AI
stops being a demo and starts being a budget line that goes down.

## AAA studio practice

Production prop pipelines are gated by written requirements and a
blockout, not by the first good-looking mesh:

- **Requirements before modeling.** A game-ready hero prop starts
  from a requirements read (triangle budget, texture-set count,
  reference photos of the exact model) and proceeds in order:
  references, blockout, high-poly, low-poly, unwrap, bake, texture,
  final presentation. Skipping the requirements read is how a prop
  blows its budget after the texturing is done.
  (Source: https://polycount.com/discussion/comment/2799864#Comment_2799864)
- **The standard chain, with a library at the end.** The industry
  workflow runs concept, sculpt (high-poly and low-poly), UV
  mapping, baking and texturing, then lighting and editing in the
  target editor, with finished models added to the team's asset
  library for reuse.
  (Source: https://www.perforce.com/blog/p4/game-asset-creation-workflow)
- **Automation (agent-executable):** write a `prop-requirements.md`
  before generating (engine, role, triangle budget, texture-set
  count, format, deadline) and refuse to start without it; add a
  blockout approval gate (silhouette and scale approved before any
  high-poly or texture work); pack background props into shared
  texture atlases to cut draw calls, following the atlas practice
  in (Source: https://www.unboxfuture.com/2026/07/how-to-sculpt-bake-and-texture-stylized.html);
  log the final engine import (scale, slots, normals, warnings) as
  a pass/fail record, not a screenshot.

## The human method, distilled

1. Budget before generation. No budget tier, no brief.
2. Pick the cleanest candidate; never repair a bad base out of loyalty
   to the first result.
3. Separate before texturing. Fused slots cannot be fixed downstream.
4. Prove in the engine, not the viewer. Import is the acceptance test.
5. Save the recipe. A pipeline that makes one prop is a demo; a
   pipeline that makes thirteen is production.
6. Price cleanup at quantity. A sustainable single prop can still be an
   unsustainable set.

## Depth status

FULL (article text; substantive sections read, minor FAQ tails unseen).
