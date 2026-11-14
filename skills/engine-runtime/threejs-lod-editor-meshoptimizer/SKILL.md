---
name: threejs-lod-editor-meshoptimizer
description: "Tune three.js LOD thresholds by eye with the three.ez LOD editor on meshoptimizer: define each level by an Error budget (shape change as a share of model size) and a Ratio (share of triangles kept), test skinned and morph-target models, and export ready-to-use TypeScript/JavaScript for InstancedMesh2 per-instance level selection. Includes the 5,000-character, 76M-to-500K-drawn benchmark and the skin-weight caveat. Trigger when a three.js scene needs measured LOD budgets instead of guessed triangle targets."
---

# three.js LOD Editor on meshoptimizer

## Purpose

This skill reconstructs the three.ez LOD editor workflow from the author's post
and comments, step by step, so another agent can follow the same process. Every
phase has three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The core method is: error is the budget,
triangle count follows.

## Source

Creator: agargaro. Reddit post:
https://www.reddit.com/r/threejs/comments/1xuhlmz/i_built_a_lod_editor_for_threejs_on_top_of_meshoptimizer/
(r/threejs post 1xuhlmz, score 45, 4 comments). Library:
https://github.com/agargaro/simplify-geometry. InstancedMesh2:
https://github.com/agargaro/instanced-mesh. Try it:
https://agargaro.github.io/simplify-geometry/. 2026-11-13 scout run, audit 5.

This is a distinct tool from the InstancedMesh2 bone-animation-textures skill
(`bone-animation-textures-gpu-instancing`): that one bakes animation clips into
textures for GPU skinned instancing; this one simplifies geometry into LOD
levels and exports the InstancedMesh2 code that picks them. They compose; do
not merge them.

## Tools used

**three.ez/simplify-geometry** (meshoptimizer wrapper),
**InstancedMesh2**, **three.js**, **meshoptimizer**.

## Phase 1: Simplify with the library

**Do**
1. Pass a three.js `BufferGeometry` to three.ez/simplify-geometry and get back
   the simplified `BufferGeometry` levels. They are plain three.js geometries,
   usable anywhere, not only with InstancedMesh2.
2. Define each level by two numbers: **Error** (how much the shape may change,
   as a share of the model size; 0.01 = 1%) and **Ratio** (the share of triangles
   to keep; 0.25 = a quarter).

**Check**
- The simplified level still reads as the same model at its intended viewing
  distance; the triangle count follows from the error limit, it is not set
  directly.

**Why**
An error budget is a quality contract; a triangle target is a guess. Setting
the error first is what makes the LOD levels comparable across different models.

## Phase 2: Tune the thresholds in the LOD Editor

**Do**
1. Open the editor, which brings simplify-geometry and InstancedMesh2 together
   (InstancedMesh2 picks the level per instance).
2. Let the editor generate the levels automatically, then tune every one.
3. Open your own glTF/GLB; the editor works with skinned and morph-target
   animated models.
4. Export ready-to-use TypeScript/JavaScript code for InstancedMesh2.

**Check**
- Test the different LODs and their transitions in the editor. The author built
  it because "to get my demos running as smoothly as possible, I needed to find
  the best LOD thresholds for each model."

**Why**
Thresholds are found by looking, not by calculating. The editor is a tuning
instrument, and the exported code is the record of the tuned decision.

## Phase 3: Measure the result

**Do**
1. Measure with the per-instance level pick: in the video, 5,000 animated
   characters, 76M triangles at full detail, about 500K actually drawn. The
   commenter calls out the mechanism: "the per-instance level pick is what
   makes 5k animated characters workable, nice."

**Check**
- Drawn triangles collapse by two orders of magnitude while the scene still
  reads as 5,000 characters.

**Why**
Per-instance selection is the win: a crowd is mostly far away, so most
instances should be cheap. A single global LOD would either waste triangles
or visibly pop.

## Phase 4: Do not break the skin (commenter caveat)

**Do**
1. For skinned models, feed the skin weights into meshoptimizer's
   `simplifyWithAttributes`, or lock verts that have mixed bone influence.
   Commenter PurchaseCommercial34: "with position only it'll happily collapse
   verts across a joint, so a level looks fine in bind pose and then bends
   wrong once an elbow or knee moves."
2. Confirm the author's model: the library's simplification is error-driven
   decimation ("Meshoptimizer removes details that have the least impact on
   the shape, within the error limit set"), so the fix is to make the error
   metric see the skin weights, not to simplify less.

**Check**
- Pose the model at each LOD level; a level that looks fine in bind pose and
  bends wrong in motion is a broken level.

**Why**
Position-only simplification does not know about bones. The check has to be
done in motion, because the failure only appears in motion.

## AAA studio practice

Error is the budget, and the simplifier that preserves shading and
silhouette wins. Lukasz Gallo benchmarked four open-source simplifiers
(meshoptimizer, CGAL, Open3D, fast-simplification) on production assets from
Bohemia Interactive's Arma Reforger: 288 benchmark operations across eight
assets, plus 150 people judging visual quality in about 2,800 pairwise
comparisons. All four implement quadric error metric variants, but
"geometric accuracy metrics like Hausdorff distance explained only about
10-15% of what drove players' visual preferences. Shading preservation,
silhouette integrity, and feature retention mattered far more."
Meshoptimizer won perceptual preference (57.6%) and was fastest (24 ms
average) because "it classifies vertices by type before collapsing,
automatically detects attribute discontinuities from the index buffer, and
preserves shading boundaries that the other tools either ignore or average
away." Source: 80 Level, "Testing 4 Free Mesh Simplification Tools",
https://80.lv/articles/testing-4-free-mesh-simplification-tools

Frostbite's in-house LOD technology (GDC 2020) was built because "popular
LOD tools triangulate meshes and ignore topology. While LODs are sometimes
thought of as throwaway, maintaining good topology benefits subsequent
hand-editing, lighting and animation. For that reason, BioWare historically
spent days per model hand-authoring their character LODs. Instead, this
work aims to procedurally generate LODs that look like artist-authored
models, most of the time, saving hundreds of thousands of dollars per
title." The bar is artist-authored quality, not just fewer triangles.
Source: GDC Vault, Ashton Mason, "Quad Mesh Simplification in Frostbite",
http://gdcvault.com/play/1026739/Quad-Mesh-Simplification-in

Compulsion Games (South of Midnight, UE4, Xbox Series S, 60 fps target)
built named "LOD Recipes": per-category simplification pipelines (organic
meshes, foliage of different sizes, architectural pieces), with a different
mesh simplification pipeline per LOD level, editable in-editor with
real-time rebuild and visual feedback. "After changing LOD pipelines in the
LOD Recipe Asset user interface, we could build LODs on individual meshes,
or all meshes in the recipe, and see the difference in the editor in real
time." For HLODs, a building went from "407 objects with 300,000 tris to 1
object with 10,000 tris"; a Sawmill set of 6,631 objects and 6,633,401
triangles became a 25,900-triangle far stand-in "ready in an afternoon."
Source: Simplygon, "Customer story: South of Midnight",
https://simplygon.com/blog/91543032-aaa3-44a1-97c7-02d25c3f8d20

For skinned characters, Simplygon's pipeline uses a different reducer per
chain step: "For close-up LODs, you can trust the quad reducer to retain a
topology that mirrors the original... For far-away LODs, you can use the
triangle reducer that is designed to maintain detail even when characters
span just a few pixels on screen. Both make sure to meticulously preserve
skinning and blend shapes." A bone reducer simplifies "the rig to use fewer
skinning influences for your LODs", and vertex-weight reduction is aimed
"toward what matters most, so faces, hands, and silhouettes keep their
detail." Source: Simplygon, "Craft superior character LODs",
https://www.simplygon.com/solutions/characters

Ubisoft Mainz replaced a 3ds Max round-trip prototype for Anno 1800
("Game engine -> 3ds Max -> Simplygon -> 3ds Max -> game engine") with a
scripted headless pipeline ("Game engine -> Simplygon -> game engine") using
Simplygon Standalone with a Python interface and a thread pool: "Optimizing
a single asset was significantly faster than before... and optimizing
multiple assets was mind-blowingly fast thanks to multi-threading. The
entire game now took only around 3 hours to optimize. This meant we could
optimize all assets in one go, look for any issues, and optimize all of them
again. In the end we ran all assets countless times through Simplygon." All
models already used 5 LODs, which were kept; aggregation with geometry
merging and reduction was the biggest draw-call win. Source: Simplygon,
"How Simplygon helped bringing Anno 1800 to PS5 and Xbox",
https://simplygon.com/blog/e51566c7-bfe2-4d97-8443-aec75cf22882

Meshoptimizer itself is the production decimation backend in NVIDIA's
updated `vk_lod_clusters` sample (Zorah scene, 1.6B triangles), whose
processing "mostly uses meshoptimizer's `clusterlod.h`": attribute-aware
simplification (`meshopt_simplifyWithAttributes`) where "each attribute has
a scalar weight, and is weighted according to its impact over the surface",
and error-driven streaming where "the error values simplifier produces
during simplification process are controlling the streaming process". In
permissive mode "it is important that attributes with discontinuities are
given to the simplifier for attribute-based weighting, and that the output
error is used during LOD selection; simply using a fixed triangle count
budget does not guarantee reasonable appearance." Source: Arseny Kapoulkine
(meshoptimizer author), "Billions of triangles redux",
https://zeux.io/2026/09/30/billions-of-triangles-redux/

For crowds, Epic's Mass Entity framework (used in Fortnite) manages visual
representation in bands: skeletal mesh (near), static mesh (mid), instanced
static mesh (far), culled (very far). Recommended distance bands from the
Mass AI walkthrough: skeletal mesh 0-25 m with a 25-30 m crossfade, static
mesh 30-75 m, instanced static mesh 80-190 m, cull at 200 m. "Skeletal mesh
agents (LOD 0) are approximately 50x more expensive per-agent than
instanced static mesh agents (LOD 2)" and "the number of near-LOD skeletal
mesh agents has more impact on performance than the total agent count."
Benchmark: 10,000 agents at 4.6 ms crowd cost on RTX 4080. Far agents use
vertex animation textures (VAT) baked from skeletal animation, replayed on
static meshes via shader. (The distance bands are the tutorial author's
recommended values, not Epic-published numbers; use them as starting
presets.) Source: StraySpark, "Building Crowds and Traffic in UE5: Mass AI
and 10,000 NPCs at 60fps",
https://www.strayspark.studio/blog/crowd-traffic-simulation-ue5-mass-ai

### Agent automation

- **LOD manifest with per-level measured error and a regression gate.** For
  each asset, generate every LOD directly from the original (never chain
  LODs from LODs), and record per level: triangle count, ratio,
  meshoptimizer-returned error, and a silhouette/feature checklist result.
  Reject any level whose measured error exceeds its budget or that fails the
  silhouette check, and re-run the whole batch after fixes, the Anno 1800
  loop ("optimize all assets in one go, look for any issues, and optimize
  all of them again"). Do not gate on Hausdorff alone; the Arma Reforger
  benchmark shows it explains only 10-15% of perceived quality.
- **Skinned-model motion test plus per-level bone/influence reduction.**
  Play each LOD through a small pose set (walk-cycle extremes, joint bends)
  and measure max vertex deviation against LOD0 in the same poses, on frames
  not used for fitting. Keep a per-level bone-reduction table (drop
  twist/finger/face bones at far levels, reassigning weights to the nearest
  kept bone), following Simplygon's bone reducer. (The in-motion measurement
  pattern is adapted from the third-party SkinLOD tool, not a AAA studio
  practice; the AAA-grounded part is Simplygon's skinning preservation and
  bone reduction.)
- **Named per-category LOD recipes and crowd distance-band presets.** Keep
  a recipe table (organic character, hard-surface prop, foliage,
  architecture) with starting Error/Ratio presets per level, following
  Compulsion's LOD Recipes, plus default InstancedMesh2 distance bands for
  crowds (skeletal 0-25 m, static 30-75 m, instanced 80-190 m, cull 200 m),
  with the 5,000-character benchmark as the regression check (drawn
  triangles and near-LOD skeletal count, not just total instance count).

## The human method, distilled

1. Set the error budget first; let the triangle count follow.
2. Tune thresholds by looking at transitions, not by guessing numbers.
3. Test skinned LODs in motion, never in bind pose alone.
4. Export the tuned decision as code, so the tuning survives the demo.

## Failure modes

- **Position-only simplification on skinned models.** Lower LODs collapse
  verts across joints and bend wrong once animated. Feed skin weights into
  `simplifyWithAttributes` or lock mixed-influence verts.
- **Judging LODs in bind pose.** The failure only appears in motion. Always
  pose-check every level.
- **Setting triangle targets directly.** A triangle target without an error
  budget is not comparable across models; the Error number is the contract.

**Depth status:** FULL (full post text, 1,643 characters, plus all 4 comments;
the author confirms the error-driven decimation in the thread).
