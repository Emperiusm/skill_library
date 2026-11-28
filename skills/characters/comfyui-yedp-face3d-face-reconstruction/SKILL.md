---
name: comfyui-yedp-face3d-face-reconstruction
description: "Reconstruct one editable 3D face from one image with the Yedp-Face3D ComfyUI node, edit facial shape, expressions, eyes, and mouth, track and animate it with video motion capture including blendshape animation and GLB export plus OpenPose and Depth/Normal passes, and reuse a snapshotted expression across shots and characters via OpenPose plus ControlNet so identity stops drifting between angles. Trigger when one reconstructed face must serve as the controllable reference for generation, animation, and compositing in ComfyUI."
---

# Yedp-Face3D: 3D Face Reconstruction and Tracking in ComfyUI

## Purpose

This skill reconstructs the exact workflow shamomylle shows for Yedp-Face3D, a ComfyUI node that creates an editable 3D face from one image and uses it for tracking, animation, and control passes. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: reconstruct one editable 3D face from one image, then reuse that face as the controllable reference for generation, animation, and compositing instead of re-rolling identity per shot.

## Source

Creator: shamomylle. Post: "Yedp-Face3D — a 3D face reconstruction / tracking node for ComfyUI" — https://www.reddit.com/r/comfyui/comments/1y6re6q/yedpface3d_a_3d_face_reconstruction_tracking_node/ (score 141, 13 comments, 12 retrieved). Video: https://v.redd.it/wmi44m7l854i1. Repository: https://github.com/yedp123/ComfyUI-Yedp-Face3D (linked in the post; not opened in this run). Scout audit 2026-11-28, audit 7, PARTIAL.

## Tools used

ComfyUI, Yedp-Face3D node, RefControl Depth LoRA for FLUX.2 Klein 4B Base (workflow included in the node repository, per the author). No ComfyUI version, node parameters, model files, or hardware is stated. The author states the node is "still rough around the edges and more of a technical demo than a production ready tool" (post text, verbatim). FLUX.2 Klein 4B Base is a different model generation from the Flux Klein 9B/4B and FLUX 3 Klein rows already on the watchlist; do not confuse them. Same author (yedp123) as YEDP Action Director, different node.

## Phase 1: Reconstruct an editable 3D face from one image

**Do**
1. Feed one image to Face3D. "Face3D creates an editable 3D representation of a face from an image, with controls for things like facial shape, expressions, eyes and mouth." (post text, verbatim).
2. Edit shape, expression, eyes, and mouth with the node's controls. No control names or value ranges are stated.

**Check**
- The reconstructed face is editable in the stated dimensions (shape, expression, eyes, mouth) before it is used downstream. No edit is demonstrated in the retrieved text beyond the author's description.

**Why**
One editable reconstruction is the identity anchor: every downstream use derives from the same face, instead of each generated shot re-inventing the face. Inference, labeled: the "identity anchor" reading is the auditor's summary of the author's stated uses, not a phrase the author uses.

## Phase 2: Track, animate, and export passes

**Do**
1. Use the node "for tracking, animation, rendering and generating different passes from the reconstructed face" (post text, verbatim).
2. Video-based motion capture is supported, "including blendshape animation, GLB export, OpenPose and Depth/Normal passes" (shamomylle, comment, verbatim). No capture settings are stated.

**Check**
- The tracked face drives animation as blendshapes; the passes (OpenPose, Depth, Normal) are the control inputs for downstream generation. No pass image is shown in the retrieved text.

**Why**
Passes are the bridge: a depth or normal render of the same reconstructed head at a new angle is a control signal a generator can follow, which is how identity survives an angle change.

## Phase 3: Reuse an expression across shots and characters

**Do**
1. Snapshot an expression and reuse the output. The author: "you can do snapshot of an expression and reuse the output mostly if you use openpose and controlnet you can easily have the same expression and camera angle on different characters" (comment, verbatim, spelling as written).
2. For the multi-shot consistency use proposed by a commenter (reconstruct once from the hero image, render a depth or normal pass at each shot's angle, feed it as the control so "the jawline and nose shape stop drifting between a 3/4 shot and a profile"), the author answers that OpenPose output can be used "if you only need facial motion capture" (comment, verbatim).
3. On whether expression setups can be saved and applied to another face for consistency across separate generated shots (rather than motion from footage), the author answers in terms of the OpenPose/ControlNet snapshot reuse in step 1. No dedicated expression-save file or parameter export is confirmed in the retrieved comments; the author separately asks whether the commenter means "a separate raw per-frame expression-data export", which is left open.

**Check**
- The same expression and camera angle reproduce on a different character via the OpenPose/ControlNet route. No side-by-side evidence is given in the retrieved text.

**Why**
Expression reuse is the consistency mechanism: the expression is captured once and re-applied, instead of being re-prompted per shot and drifting. The open question (raw per-frame expression-data export) is recorded as open, not assumed answered.

## Phase 4: Try the FLUX.2 Klein workflow included in the repository

**Do**
1. "I've been experimenting with RefControl Depth LoRA for FLUX.2 Klein 4B Base workflow (It's included in the node GitHub)" (post text, verbatim). No workflow steps, settings, or results are stated.

**Check**
- No result is reported in the retrieved text. The workflow's existence in the repository is the only stated fact.

**Why**
The author's stated purpose for the post is discovery, not a tutorial: "I wanted to show a few things it can do and see what other people might come up with" and "I'm particularly curious about uses I haven't thought of yet" (post text, verbatim). The node is presented as an open-ended bridge, including "as a bridge between tracking and other ComfyUI workflows" (post text, verbatim).

## Failure modes

- Treating the node as production-ready. The author states it is a technical demo, rough around the edges.
- Re-prompting identity per shot instead of reusing one reconstructed face as the control reference.
- Assuming a raw per-frame expression-data export exists. The author left that question open.
- Confusing FLUX.2 Klein 4B Base with Flux Klein 9B/4B or FLUX 3 Klein, or Yedp-Face3D with YEDP Action Director.

## The human method, distilled

1. Ship the technical demo and ask what others would use it for, instead of inventing one intended use.
2. "The interesting part for me isn't really one specific 'intended' use though, i'm still figuring that out myself" (post text, verbatim).
3. Answer consistency questions with the concrete reuse route (snapshot plus OpenPose/ControlNet), and ask when the question needs a different export than the one the node has.

**Depth status:** PARTIAL. Capabilities, passes, export format, the reuse pattern, and the experimental status are stated by the author. No install steps, node parameters, model files, or worked example with settings are given, and the repository was not opened. What would reach FULL: a firsthand read of the repository README and a worked workflow with node settings.
