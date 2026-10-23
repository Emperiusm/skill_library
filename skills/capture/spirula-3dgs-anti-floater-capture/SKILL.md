---
name: spirula-3dgs-anti-floater-capture
description: "Produce clean 3D Gaussian splats with Spirula: plan phone capture around the actual camera moves (4K60), enable normal and depth estimation at SfM time, and use Mild training-time floater suppression. Reconstructs SnipperAndClipper's quoted workflow from r/vfx. Trigger when generating splats that must survive close camera moves without indistinct clouds or floaters."
---

# Spirula 3DGS Anti-Floater Capture

## Purpose

This skill reconstructs the exact workflow SnipperAndClipper describes in
the r/vfx "Spirula + Blender 5.3" thread, step by step, so another agent can
produce splats without the classic failure mode (indistinct clouds hanging
around, detail loss on zoom). Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The workflow's core method is: constrain the capture to the shots you will
use, then attack floaters at their cause (under-constrained depth), not
their symptom.

## Source

Creator: SnipperAndClipper (commenter workflow, quoted verbatim below).
Thread: https://www.reddit.com/r/vfx/comments/1x2r17t/ ("Spirula + Blender
5.3 pretentious arty test I made", r/vfx post 1x2r17t, 6 comments,
2026-10-12 scout run). The workflow answers Yeoldeone's question: "what's
your workflow for generating splats? Mine always has those indistinct clouds
hanging around and loses detail if you zoom in on it."

## Tools used

Spirula (3D Gaussian splatting tool), Blender 5.3 (composite/test stage),
phone video camera at 4K 60fps (capture device).

## Phase 1: Plan the camera moves first

**Do**
1. Decide the exact camera moves the splat must survive BEFORE shooting.
2. Quote: "I am capturing with the eventual camera moves in mind, not to
   create an environment viewable from many povs."

**Check**
- Write the shot list down: if a viewpoint is not on the list, it does not
  need coverage.

**Why**
A splat only needs to survive the moves it will actually perform. Shooting
the move instead of the world shrinks the problem dramatically: fewer
viewpoints to constrain, denser coverage where it matters.

## Phase 2: Capture at 4K 60fps on a phone

**Do**
1. Shoot the planned moves with the phone's video camera at 4K, 60fps.
2. Keep the motion smooth and the subject framed the way the final move
   frames it.

**Check**
- Play the footage back at full speed: motion blur or rolling-shutter wobble
  in the source becomes floater food downstream. Re-shoot shaky passes.

**Why**
60fps gives the SfM stage dense temporal correspondences; 4K gives it pixels
to match. Phone capture is sufficient when the moves are planned (the
author's entire test is phone-shot).

## Phase 3: SfM with normal and depth estimation

**Do**
1. In Spirula's SfM (structure-from-motion) stage, enable normal estimation
   and depth estimation.
2. Quote: "Spirula has a couple of settings that seem to help a lot with
   minimising floaters: normal & depth estimation when calculating sfm".

**Check**
- Inspect the sparse reconstruction before training: if the point cloud has
   large empty regions where the move goes, add capture there rather than
   hoping training fills it.

**Why**
Floaters come from under-constrained depth: Gaussians placed where no real
surface exists because the geometry was ambiguous. Normal and depth
estimation at SfM time constrain the geometry BEFORE the splats are
optimized, attacking the cause.

## Phase 4: Train with Mild floater suppression

**Do**
1. During training, enable floater suppression. Two levels are available;
   use "Mild".
2. Quote: "then two levels of floater suppression during training. 'Mild'
   suppression seems to help a lot."

**Check**
- Orbit and zoom into the trained splat: Yeoldeone's failure mode is
   "indistinct clouds hanging around" and detail loss on zoom. After Mild
   suppression both should be gone or minimal.
- If detail collapses on push-in anyway, the cause is missing capture
   coverage at that viewpoint (go back to Phase 2), not insufficient
   suppression. Do not crank suppression to compensate for missing views.

**Why**
Suppression at training time removes the Gaussians that do not earn their
keep photometrically. "Mild" is the author's tested setting: enough to kill
floaters, not so much that it eats real detail. Stronger is not better.

## Phase 5: Composite in Blender 5.3

**Do**
1. Bring the trained splat into Blender 5.3 for the composite/test.
2. Cut to the planned moves; the splat only promised to survive those.

**Check**
- Know which artifacts are defects and which are texture. The author notes:
   "I especially like the part on the train station bridge where as the pov
   moves forward, the image degrades" - splat breakup on push-in can be an
   aesthetic choice, but only when it is chosen, not when it is a surprise.

**Why**
The composite is where the capture plan pays off: every shot was pre-solved
in Phase 1, so there are no "we never shot that angle" emergencies.

## The human method, distilled

1. "Capture for the move, not the environment" (author's principle, quoted):
   constrain the problem to the shots you will use.
2. Fix floaters with the two settings that target them (SfM normal/depth
   estimation + Mild training suppression) before reaching for more
   capture.
3. Distinguish defect from texture: floaters are always defects; splat
   breakup on push-in is a defect unless you choose it as a look.

## Failure modes (from the thread)

- Indistinct clouds hanging around the subject + detail loss on zoom
  (Yeoldeone's report): under-constrained depth. Fix: Phases 3-4, in that
  order. If it persists, the viewpoint was never captured: re-shoot.
- Over-suppression eating real detail: back off to Mild; suppression is not
  a substitute for coverage.

**Depth status:** PARTIAL (author's full settings quoted from comments;
exact Spirula version and training iteration counts not published; Blender
5.3's compositing role not detailed).
