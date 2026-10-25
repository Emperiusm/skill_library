---
name: substance-painter-3dspace-blur-filter
description: "Remove UV seam artifacts in Substance Painter with a custom 3D-space blur filter that samples neighbors by 3D proximity from a baked Position Map instead of UV adjacency; bake the result down on low-end machines. Reconstructs Such_Screen_3435's free filter workflow from r/Substance3D. Trigger when UV seams survive 2D blur, or when evaluating blur-across-islands techniques."
---

# Substance Painter 3D-Space Blur Filter

## Purpose

This skill reconstructs the workflow behind Such_Screen_3435's custom blur
filter for Substance Painter, step by step, so another agent can apply the
same seam-killing technique. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The workflow's core method is: change what "neighbor" means (3D proximity
via a baked Position Map) and the seam artifact class disappears.

## Source

Creator: Such_Screen_3435. Thread:
https://www.reddit.com/r/Substance3D/comments/1x35ts9/ ("Made a 3D-space
blur filter for Substance Painter to reduce UV seam artifacts", r/Substance3D
post 1x35ts9, score 219, 17 comments, 2026-10-12 scout run). Companion:
https://www.artstation.com/artwork/WdXOD2 (linked in post text). The filter
was previously a paid Gumroad addon; the author released it free: "This is my
own implementation, and I've decided to share it for free."

## Tools used

Substance Painter (custom filter), baked Position Map (mesh map).

## Phase 1: Bake the Position Map

**Do**
1. Bake a Position Map for the mesh using Painter's standard mesh-map bake.
2. Verify the bake: every pixel's RGB must encode its 3D position; holes or
   streaks in the position bake will corrupt the blur.

**Check**
- Inspect the Position Map directly: it should read as a smooth
   rainbow-gradient over the model. Hard edges where the model is smooth
   mean a bad bake; fix the bake before touching the filter.

**Why**
The Position Map is the filter's only source of 3D truth. Everything
downstream assumes it is correct, so a bad position bake poisons the blur
silently.

## Phase 2: Apply the 3D-space blur

**Do**
1. Apply the custom blur filter to the layer that shows seam artifacts.
2. The filter reads each pixel's 3D position from the Position Map and
   gathers blur samples by 3D proximity: pixels adjacent on the model but
   split across UV islands blur together.
3. Set the blur radius against the seam width (exact radius values were not
   published in the thread; start small and grow until the seam band
   disappears).

**Check**
- Before/after on the seam: the artifact band along island borders should
   shrink because the blur no longer stops at the UV edge.
- Check non-seam areas too: the blur is 3D-uniform, so detail near (but not
   on) seams gets softened as well. Mask the filter to seam neighborhoods
   if detail loss is unacceptable.

**Why**
UV-space blur cannot see across island borders, so seams survive any 2D
kernel no matter how wide. Sampling in 3D space makes the seam a non-event:
neighbors are defined by the model, not the unwrap.

## Phase 3: Manage the performance cost

**Do**
1. Expect the filter to be slow. Quote from the author: "Performance issues
   are pretty much unavoidable with this kind of effect."
2. On a low-end machine (commenter Nek0ni: the original version "always
   slows my potato to a crawl"), bake the filter result to a static layer
   and disable the live filter.

**Check**
- Editor responsiveness with the filter live: if brush strokes lag, the
   filter is costing more than the iteration speed is worth. Bake it down.

**Why**
3D neighborhood gathering is far more samples than a 2D kernel; the cost is
inherent, not a bug. The filter is a finishing move, not an interactive
one. The author's honesty about the cost is the documentation: plan for it.

## AAA studio practice

The 3D-space blur is a special case of production seam practice, and the general rules from Adobe's own support channels and production forums strengthen the skill's checks:

- Adobe's support answer on UV seam artifacts: hide seams where possible, use tri-planar projection where UV projection fails, and match UV padding to the baker's dilation setting (Substance Painter's default dilation is 32 pixels), because seams that survive in the material view (not just the normal view) are the ones that matter. Source: https://community.adobe.com/questions-59/artifacts-on-uv-seams-related-to-height-628252
- Adobe's support answer on normal seams across UV islands: a visible seam in the normal view alone is expected (tangent-space orientation differs per island) and is not a defect; judge by the material view, and check the normal format (DirectX vs OpenGL) when seams appear only in a third-party app. Source: https://community.adobe.com/questions-59/normal-issue-in-different-uv-islands-in-substance-painter-629097
- Production forum practice (Polycount) for the same artifact class: straighten UV borders and align them to the pixel grid, move seams to unobtrusive areas, and use edge padding sized to the lowest mip level. Source: https://polycount.com/discussion/comment/2782327/

**Do (agent-executable, adds to Phases 1-3)**
1. Before applying the filter, run the seam triage: check the material view, not the normal view, and record which seams are actually visible in the material; only those seams get the filter, so detail elsewhere is never softened.
2. Set UV padding/dilation to match the export resolution's lowest mip (start from the 32-pixel default and scale with texture size), and place seams on hard edges or hidden areas first; the filter is the fix for seams that survive that placement, not a substitute for it.
3. Add a before/after seam-band measurement: screenshot the seam region at fixed camera and lighting before and after the filter, and confirm the artifact band shrinks while non-seam detail at a fixed distance from the seam stays sharp; if detail loss is unacceptable, mask the filter to seam neighborhoods, per the skill's Phase 2 check.
4. Automate the performance fallback from Phase 3: bake the filter result to a static layer and disable the live filter whenever editor brush latency is observed, and keep the baked layer named so the live filter can be re-enabled for rework.

**Check**
- Only material-visible seams are filtered, padding matches dilation, and the before/after pair shows seam reduction without collateral softening.

**Why**
- Production seam work is triage first (which seams matter, where they sit, how much padding they get) and filtering second; a filter applied blindly to every seam costs detail and performance for no gain.

## The human method, distilled

1. Fix the seam at the sampling level, not with a wider 2D kernel: redefine
   "neighbor" and the artifact class disappears.
2. Ship the cost honestly: the author does not claim it is fast; the check
   is "does the machine survive it", and the fallback is baking the result.
3. Release the tool when it is useful, not when it is fast: the filter went
   from paid to free on the strength of the technique, performance caveat
   included.

**Depth status:** PARTIAL (post text + comment quotes; no exact radius
values or filter-node wiring published in the thread).
