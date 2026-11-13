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
