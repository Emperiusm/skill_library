---
name: "substance_painter_3dspace_blur_filter"
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
