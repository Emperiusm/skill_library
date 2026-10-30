---
name: houdini-single-image-gsplat-sharp-moge2
description: "Turn a single photo into a Gaussian splat in Houdini 22 two ways: the built-in MoGe-2 node (depth/normal/position to faux splat) or Apple's SHARP model via ONNX in Copernicus (sharp fp16.onnx, 1536x1536, OCIO to sRGB, disparity-factor detail attribute, ONNX Inference on CUDA, volumes to points via volumeindex(), Karma shadow-skip detail attribute, aspect fix, wrap as HDA). Trigger when a single image must become a splat without multi-view capture."
---

# Single-Image Gaussian Splats in Houdini 22 (MoGe-2 and SHARP)

## Purpose

This skill turns one photo into a Gaussian splat inside Houdini 22, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The core method is: pick the model that matches the scene
(SHARP for nature, MoGe-2 for geometry), then make Houdini speak the model's
I/O contract exactly.

## Source

YouTube, Entagma (417 caption segments, 2026-10-29):

- https://www.youtube.com/watch?v=VDIsRIsVgsw - "Free Houdini: GSplats from
  a single image (MoGe-2 & SHARP)" (16:18, 2026-10-26)
- Scene file: https://entagma.com/

Evidence note: captions only, no frames inspected. Inference labels: the
captions transcribe "Onyx" (the node is the ONNX Inference node; the file
downloaded is `sharp fp16.onnx`), "Apple Sharp/Shard" (SHARP), "MoGE2"
(MoGe-2). Node names reconstructed from context. The author's test image is
an infrared photo from a botanical garden (also in the scene-file download).

## Tools used

Houdini 22 (built-in MoGe-2 node; Copernicus/COPs; SOPs); SHARP (Apple's
single-image-to-GSPlat model) via an ONNX conversion from Hugging Face
(`sharp fp16.onnx`); OCIO Transform; ONNX Inference node; point wrangle
with `volumeindex()`; Karma.

## Phase 1: Choose the model for the scene

**Do**
1. Option A (ships with Houdini 22): the built-in node using MoGe-2, which
   computes depth, normal, and position passes from one image; then
   SideFX's COPs/SOPs work turns them into a faux Gaussian splat.
2. Option B (build it yourself): SHARP, Apple's model, which turns an image
   directly into a Gaussian splat with no SOPs magic after it.
3. Rule of thumb (author): nature scenes look better with SHARP; geometric,
   rectangular scenes work better with the MoGe-2 neural-layer-to-depth
   path.

**Check**
- Compare both on your scene; neural models are scene-dependent.

**Why**
"It's good to have choices." No single model wins everywhere; the video's
thesis is model-per-scene, not model-of-the-year.

## Phase 2: Use the built-in node correctly (the fast path)

**Do**
1. Resample big images down first: "otherwise this node will take forever."
2. Decide whether to apply a sky mask.
3. Tune the splat-point scale (author example: 2x).

**Check**
- The node works by default; the failure mode is oversized input, not
  wrong parameters.

**Why**
The built-in path is the baseline: cheap, default, and good enough to
compare the SHARP build against.

## Phase 3: Fetch the SHARP ONNX model and read its contract

**Do**
1. On Hugging Face, find the project that converted the SHARP model to
   ONNX (ONNX is "one of those machine learning formats that Houdini is
   able to read").
2. Download `sharp fp16.onnx` from Files and versions.
3. Read the contract: input = 3-channel RGB float32 image, values 0-1,
   shape [1, 3, H, W]; second input = disparity factor (focal length /
   sensor width; 1.0 if unsure; controls how far splats extend back).
   Outputs = 3D positions, 3D scales, quaternion rotations, linear
   colors, opacity - "exactly the same data representation that also
   Houdini uses for its Gaussian splats."

**Check**
- The output attributes must match Houdini's GSplat representation
  exactly; that is what makes the integration near-instant.

**Why**
Representation agreement is the whole trick: when the model's output
schema matches Houdini's splat attributes, there is no translation layer
to build.

## Phase 4: Prep the image in COPs to the model's contract

**Do**
1. In an empty scene: geo node -> dive in -> COP network -> dive in ->
   File COP with the image.
2. Set the channel type to RGB (the model expects RGB).
3. Resample to the model's stated resolution: 1536x1536 (set base size to
   parameter).
4. OCIO Transform: from scene_linear (Houdini's working space) to sRGB
   display ("our colors will look very wrong, but again, the right colors
   for our model to use").
5. Clamp pixel values 0-1.
6. Layer-to-Geometry node: convert the pixel data to a 2D volume.

**Check**
- Every step exists to satisfy the Phase 3 contract: RGB, 1536, sRGB,
  0-1. Nothing here is aesthetic.

**Why**
Models fail on contract violations, not on bad art. The prep chain is a
contract adapter.

## Phase 5: Build the inference sub-network

**Do**
1. Drop a sub-invoke node to hold the inference sub-network.
2. Inside: a detail wrangle storing the disparity factor (DF) as a detail
   attribute with a slider (author: 18 mm focal length, 23.5 mm APS-C
   sensor width).
3. Drop the ONNX Inference node; switch it to manual update while
   configuring.
4. Load the model; click "Setup shapes from model" (populates most
   parameters).
5. Set Execution Provider Automatic -> CUDA ("runs much, much faster":
   ~1 s GPU vs ~1 min CPU in the author's case). If CUDA is not found,
   paste the warnings into an LLM for the install steps.
6. Inputs: the single image, RGB values, width/height; input type =
   volume, volume order XYZ, collate channels separately, volume name C
   (as shown on the info flag); DF = float32 single value from the detail
   attribute.
7. Outputs: volume, XYZ, collate channels separately: `pos` (3 values),
   `scale` (3), `orient` (4, quaternion), `CD` (3, color; note: the node's
   default channel count for color was wrong - set 1 and paste the point
   count), `alpha` (1).

**Check**
- Cook once on CPU if CUDA fails; stash the result so it stays in memory
  ("you can leave that step out if this is working on your GPU").
- The cooked outputs must include pos, scale, orient, CD, alpha as thin
  volumes (1 voxel x N x 3).

**Why**
Manual update plus stash is the iteration discipline: inference cooks are
expensive, so configure cheaply and cook rarely.

## Phase 6: Write the volumes onto points with a wrangle

**Do**
1. Point Generate node: create the same number of points as the ONNX node
   reports.
2. Point wrangle, volumes wired to the second input, using
   `volumeindex()`: `v@P.x = volumeindex(1, 0, set(0, i@ptnum, 0))`;
   repeat for P.y (2nd value on the 3rd axis) and P.z (3rd value on the
   3rd axis).
3. Same for scale (2nd volume), orient quaternion (3rd volume, 4 values),
   and color; alpha uses `i@ptnum` at the 3rd coordinate.
4. Once the attributes (P, scale, orient, Cd, alpha) exist, "we should see
   our scene turn immediately into a Gaussian splat because Houdini looks
   for those exact attributes."

**Check**
- Points appear as a line first (X pass), then fill into 3D as y/z land.

**Why**
Houdini's splat rendering is attribute-driven: get the attribute names
right and the renderer cooperates for free.

## Phase 7: Finish for render (shadows, orientation, color, aspect)

**Do**
1. Karma efficiency: Attribute Create a detail string attribute named
   `-shadow` (use "encode invalid attribute names") so Karma skips
   shadows - "something that the big G split node does as well." Optional.
2. Fix orientation: Transform 180 degrees around Y, -90 around Z; look
   into -Z from world origin to see the image.
3. Color back: point wrangle + OCIO Transform on Cd, from linear Rec.709
   sRGB (the model's output space) to scene_linear.
4. Aspect: Transform 3D, scale X by the input image's aspect ratio
   (author's: 0.66666; the resampled square otherwise renders 1:1).
5. Wrap all the nodes into an HDA.

**Check**
- The final image matches the input photo; the aspect is not
  square-stretched.

**Why**
The last mile is representation hygiene: orientation, color space, and
aspect are all places a technically correct splat can look wrong. The HDA
is the deliverable, not the one-off network.

## AAA studio practice

- **Studios ship splats as streamed LODs, not raw PLY files.** Magnopus
  built a production splat renderer for Unreal (first Niagara-based, then
  rebuilt on instanced rendering with GPU-side per-frame sorting for its
  OKO spatial-computing platform, scaling past 30-million-splat assets)
  and adopted PlayCanvas's Streamed SOG format for delivery: scenes are
  carved into a spatial tree of region leaves with decimated LOD levels,
  selected per frame by screen-space error, requested coarsest-first, and
  streamed over HTTP with a fixed-memory working set and most-distant-
  first eviction. Applied here (labeled: Magnopus is a commercial
  spatial-computing studio, not a AAA game studio): the skill's HDA is the
  capture step; production step two is a post-process converting the splat
  to streamed LOD chunks, so the single-image splat renders at distance
  without blowing VRAM. The automation upgrade below adds the first half
  of this (cleanup plus standard PLY export) as the HDA's exit contract.
  Source: https://www.magnopus.com/blog/gaussiansplats-part-3-theres-always-a-bigger-scene
- **The production route for AI imagery is orbit-then-reconstruct, not
  single-view.** Marzena Milowska's "Through the Depths of Time" (MFA
  thesis film and VR experience, SVA 2025-2026) started every scene as an
  AI-generated image, generated a 360-degree camera orbit with Higgsfield,
  reconstructed the synthetic multi-view footage in both Postshot and Luma
  AI (keeping whichever was cleaner per scene), cleaned every splat in
  SuperSplat, and built the film in Unreal Engine 5.3 with the Luma AI
  plugin (Niagara-based splat rendering), layering RealityScan
  photogrammetry meshes underneath for two scenes. She states the key limit
  directly: single-image 3D models such as Apple's SHARP "must infer
  information that is not visible in the source" and produce Gaussians
  "designed primarily for rendering nearby viewpoints," which is why she
  synthesized views first. Applied here (labeled: an independent
  production film, not a AAA studio): the SHARP path in this skill inherits
  exactly that limit (nearby viewpoints only; do not fly the camera far).
  The HDA's disparity-factor control is the manual stand-in for what orbit
  synthesis does automatically, and the automation upgrade below records
  which model wins per scene class, turning the author's nature-vs-geometry
  rule of thumb into data.
  Source: https://radiancefields.com/stepping-inside-an-ai-generated-film-with-gaussian-splats

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Add a cleanup pass at the end of the HDA before output: cull splats
   below a tunable alpha threshold and log the percentage removed, mirroring
   the SuperSplat cleanup step in the production pipeline above; verify with
   a frame diff that the visible render did not change.
2. Add a model-selection bake: run both the MoGe-2 and SHARP paths on a
   small set of scene classes (nature, geometric, portrait) once per
   project, record which won per class, and store the mapping in the HDA;
   this automates the author's nature-vs-geometry rule of thumb into
   measured data instead of memory.
3. Add a standard PLY export step at the end of the HDA with orientation
   and color already corrected, so the output feeds downstream renderers
   (e.g. Unreal's Luma AI plugin, which expects standard 3DGS PLY) without
   a manual conversion; the HDA's exit contract matches the ecosystem's
   input contract.

**Check**
- The cleanup pass removes stray splats and the frame diff passes (visible
  pixels unchanged); the model mapping exists and is backed by per-class
  renders, not the author's memory; the exported PLY opens in a second
  renderer.

**Why**
Production splat pipelines are judged by their exit contract: clean,
portable data with known limits. The cleanup pass buys the SuperSplat
step, the model mapping buys the "which model for this scene" decision,
and the PLY export buys compatibility with the Unreal-side tooling the
industry actually renders with.

## The human method, distilled

1. Contract-first integration: read the model's I/O contract off Hugging
   Face, then build the Houdini side to match it exactly.
2. Iterate cheaply: manual update, stash cooks, configure before cooking.
3. Ship the reusable artifact: the HDA is the deliverable.

**Depth status:** FULL (417 caption segments; no frames inspected).
