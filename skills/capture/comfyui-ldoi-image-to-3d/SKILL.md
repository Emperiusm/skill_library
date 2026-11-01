---
name: comfyui-ldoi-image-to-3d
description: "Turn a single image into a 3D splat locally on low VRAM: ComfyUI-ldoi nodes with five fp16 weights (about 3.78GB), DINOv3 plus FLUX.2 VAE conditioning, BiRefNet fallback, then MeshLab Screened Poisson mesh and Blender voxel remesh. Trigger when an image needs a local, low-VRAM image-to-3D conversion without cloud services."
---

# ComfyUI-ldoi: Local Image-to-3D for Low VRAM

## Purpose

This skill runs the ComfyUI-ldoi pipeline from Olivio Sarikas' video:
**single image → TripoSG-based fp16 splat in ComfyUI → Screened
Poisson mesh in MeshLab → voxel remesh in Blender, all local, about
3.8 GB of fp16 weights.** Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the
principle).

## Source

Olivio Sarikas, "FREE + LOCAL: Image to 3D for LOW Vram" (YouTube,
2026-10-30), found by the YouTube channel scan:

- https://www.youtube.com/watch?v=0eIjJinYgmk
- Nodes: https://github.com/nynxz/ldoi (nynxz/ldoi)

Evidence note: the video has no captions and no transcript exists. It
was deepened via media download plus 12 reviewed frames, all read
directly. Every value below is from on-screen text in the frames; no
transcript lines were available or invented.

## Tools used

- ComfyUI-ldoi custom nodes (nynxz/ldoi on GitHub); requires **ComfyUI
  0.22+ with TripoSG support**
- Standard TripoSG graph + two ldoi nodes
- DINOv3 ViT-H/14 and FLUX.2 VAE as denoiser conditioning
- BiRefNet for background removal (fallback path)
- MeshLab (Screened Poisson surface reconstruction)
- Blender 4.5.4 (voxel remesh)

## Phase 1: Install the nodes and weights

**Do**
1. Clone into `ComfyUI/custom_nodes` and restart ComfyUI. The video
   frame shows the folder `ComfyUI-ldoi` freshly added on 30.10.2026
   in a portable `ComfyUI_windows_portable` install.
2. Download the five fp16 weights into ComfyUI's standard folders:

| File | Folder | Size | Source |
|------|--------|------|--------|
| ldoi_fp16.safetensors | models/diffusion_models | 0.74 GB | nynxz/ldoi |
| ldoi_decoder_fp16.safetensors | models/vae | 0.58 GB | nynxz/ldoi |
| dino_v3_vit_h.safetensors | models/clip_vision | 1.68 GB | VAST-AI/TripoSplat |
| flux2-vae.safetensors | models/vae | 0.34 GB | VAST-AI/TripoSplat |
| birefnet.safetensors | models/background_removal | 0.44 GB | Comfy-Org/BiRefNet |

**Check**
- Five files, about 3.78 GB total, in the folders above; ComfyUI 0.22+
  with TripoSG support.

**Why**
"The first two are ldoi's own weights (the denoiser and the coarse or
gaussian decoder) in ComfyUI's file layout... The other three are the
same encoders ldoi uses: DINOv3 ViT-H/14 and the FLUX.2 VAE condition
the denoiser." If you already run TripoSplat in ComfyUI, you have the
three encoders. fp16 throughout is the low-VRAM story.

## Phase 2: Run the image-to-splat graph

**Do**
1. Drag `workflow/ldoi_image_to_splat.png` into ComfyUI, or open it
   from Templates → Custom Nodes → ComfyUI-ldoi. It is the standard
   TripoSG graph with the ldoi files and the two ldoi nodes.
2. Load Image: the object photo. "a transparent PNG's own alpha can be
   used", otherwise BiRefNet cuts the object out.
3. The two ldoi nodes run the denoiser/decoder. Save Splat writes the
   result (the node shows model_3d, model_info, camera_info inputs;
   the 3D viewer shows the splat on a grid, the video frame shows a
   fox).
4. Create Video: 24 frames, 24fps, 360° turntable, MP4 output; Save
   Video.

**Check**
- The splat in the 3D viewer matches the input object from multiple
  angles; the turntable video shows no view-collapse.

**Why**
Transparent-PNG alpha is the cheap segmentation path; BiRefNet is the
fallback. The turntable video is the acceptance check before meshing.

## Phase 3: Convert the splat to a mesh

**Do**
1. Export the point cloud/mesh from the splat; open MeshLab.
2. Run Screened Poisson surface reconstruction on the exported layer.
   The video frame shows layers `ldoi_00002` point cloud → `Poisson
   mesh`, with the reconstruction dialog open on the fox model.

**Check**
- The Poisson mesh is watertight where the splat had coverage.

**Why**
MeshLab is the open-source mesh surgery step: "the open source system
for processing and editing 3D triangular meshes... editing, cleaning,
healing, inspecting, rendering, texturing and converting meshes."

## Phase 4: Remesh in Blender

**Do**
1. Import into Blender 4.5.4. Add a Remesh modifier with these exact
   settings: Voxel mode, Voxel Size **0.1 m**, Adaptivity **0.0**,
   Smooth Shading (the video frame shows these exact settings on a
   stylized head mesh).

**Check**
- Even voxel topology at 0.1 m, ready for sculpt/detail passes.

**Why**
Voxel remesh erases the Poisson mesh's uneven triangulation and gives
a uniform base for further work.

## AAA studio practice

AAA studios use image-to-3D capture as a fast **retouch baseline**, never as
shipped geometry, and the capture discipline is where the real lesson is.

1. **Multi-view capture is non-negotiable; overlap is the single most
   important factor.** DICE (Keneth Brown and Andrew Hamilton, GDC 2016,
   *Star Wars Battlefront* photogrammetry talk): the team shot hundreds of
   overlapping photos per asset, planned each shoot with an asset
   breakdown, and learned that overlap plus shooting from all possible
   angles is what prevents hours of retouching. Single-image inference,
   which this skill's ldoi denoiser performs, is the opposite of that
   discipline: every view the network invents is unmeasured. Inference:
   treat the splat as a rough capture, not as a measured asset.
   - https://www.3dmag.com/inspiration/3d-scanning-star-wars-battlefront/
2. **Capture replaced the "High Topo" sculpt phase with a retouching phase,
   inside the same asset phases as traditional modeling.** DICE still ran
   the standard asset pipeline (high topo, low poly, UVs, textures), just
   faster; scanned props were added to traditionally modeled characters.
   Inference: this skill's MeshLab Poisson mesh plus the 0.1 m voxel
   remesh is that pipeline's retouch/base pass, never the final in-game
   mesh; a bake to hand-built topology is still ahead of it.
   - https://www.3dmag.com/inspiration/3d-scanning-star-wars-battlefront/
3. **Control the capture, and cleanup work disappears.** Rebellion's
   photogrammetry team for *Sniper Elite 5* (Ludovico Antonicelli, 80
   Level, 2022): cross-polarized flash lighting removes delighting at the
   capture stage instead of painting it out later; 61 MP sensors future-
   proof the raw reconstructions; scale bars give ground control so assets
   arrive at real-world scale; RealityCapture's API provides "extensive
   automation, which is crucial in big productions." Inference: this
   skill's equivalent of that discipline is clean input segmentation
   (spend the effort on the alpha/BiRefNet cutout, not on fixing the
   Poisson mesh later) and recording the actual voxel size the remesh ran
   at, since the pipeline has no scale-bar step and 0.1 m is only as real
   as the export.
   - https://80.lv/articles/rebellion-deep-dive-into-photogrammetry-project/?amp=1
4. **Decimation is automated per asset with human oversight on the hard
   cases.** Rebellion generates the lowest LODs by automatic decimation
   from the one above, but glossy or hard-surface props get manual
   attention because decimated topology plus automatic UVs and bakes
   produce smoothing artifacts; they also keep hand-crafted low polys and
   consistent texel density for consoles. Inference: run the Poisson and
   remesh steps uniformly, but hand-check hard-surface or glossy inputs
   instead of trusting the automated pass.
   - https://80.lv/articles/rebellion-deep-dive-into-photogrammetry-project/?amp=1

## Agent automation

**Do**
1. Write `manifest.md` before running: the five weight files with their
   expected sizes (0.74 / 0.58 / 1.68 / 0.34 / 0.44 GB), target folders,
   the expected ComfyUI version (0.22+ with TripoSG support), and the
   input image filename. Verify all five before touching the graph.
2. Segmentation gate (Phase 2): after the BiRefNet/alpha extraction,
   compute the foreground pixel coverage of the input and log the
   percentage in `run-log.md`. The video names no cutoff, so do not
   invent one: log the number and reject the input only if background
   visibly bleeds into the object.
3. Splat acceptance: render the 24-frame turntable, pull 4 frames
   (front, left, back, right), and compare each silhouette against the
   input image. If any view collapses, re-center the input and re-run;
   do not mesh a collapsed splat.
4. MeshLab replay: after one successful manual run, save the Poisson
   filter sequence as a MeshLab filter script (.mlx) alongside the exact
   filter parameter values, so the next run replays the identical
   reconstruction. Inference: MeshLab supports saving and re-running
   filter scripts; confirm the exact batch invocation for your MeshLab
   version before relying on it.
5. Blender remesh headless (exact Phase 4 settings):

   ```
   blender --background in.ply --python remesh_01.py
   ```

   with `remesh_01.py` applying the Remesh modifier (VOXELS, voxel_size
   0.1, adaptivity 0.0), `shade_smooth()`, and writing `out.blend`.
   Log the voxel_size and adaptivity actually read back from the modifier,
   not assumed from this file.
6. Keep a `run-log.md` per asset: input image hash, weight manifest
   checksum result, foreground coverage %, turntable check pass/fail,
   triangle counts after Poisson and after voxel remesh, final file
   paths. The exported splat and turntable are the review artifacts.

**Check**
- Every artifact exists: `manifest.md`, `run-log.md`, turntable MP4,
  4 keyframe stills, the saved MeshLab filter script or the exact
  parameter values it replaces, the final remeshed mesh.
- The Poisson mesh is watertight where the splat had coverage; the
  voxel remesh reads even at 0.1 m.

**Why**
The video demonstrates a one-off run. Manifests, gate checks, logs,
and a saved filter script turn a 12-frames-read demo into a pipeline
another agent can replay from the file alone.

## The human method, distilled

1. **Keep everything fp16 and local**, the whole pipeline fits modest
   VRAM because no single weight exceeds 1.68 GB and the total is
   about 3.8 GB.
2. **Reuse the TripoSG ecosystem** (encoders, folder layout) instead of
   shipping a parallel stack.
3. **Splat → Poisson → voxel remesh**: three open tools, each doing
   the one conversion it's best at.

**Depth status:** FULL (deepened pipeline: media download + 12 frames
read directly; no captions or transcript exist; every value above is
from on-screen text in the frames).
