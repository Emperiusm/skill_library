---
name: ultratex-comfyui-ai-texturing
description: "Texture any untextured 3D mesh locally in ComfyUI with UltraTex: one reference image in, 2K PBR textures out, free, on 6 to 16 GB GPUs. Trigger when texturing a mesh without a paid service or a large GPU."
---

# Texture a Mesh Locally with UltraTex for ComfyUI

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: one reference image defines the
look, the mesh defines the shape, and the workflow matches the GPU you
actually have instead of the GPU the demo used.

## Source

Creator: PixelArtistry

Source: "FINALLY Good AI Texturing Locally on 6GB VRAM (Free)"
https://www.youtube.com/watch?v=4QAgeKYfBnU (about 19 minutes, audited
2026-10-25)

Evidence note, stated honestly: no captions and no transcript exist for
this video. YouTube's innertube endpoint returned a bot check, so captions
were unobtainable, and local transcription was unavailable in the sandbox
because the Whisper model download is blocked by the approval-gate rule and
was not retried. What was inspected firsthand: the downloaded video's 12
high-resolution frames, including the UltraTex README on screen and the
actual ComfyUI graphs. Every parameter below is visible in those frames;
anything not legible there is marked as such, not invented.

## Tools used

Tools used: UltraTex for ComfyUI (PixelArtistry/UltraTex on GitHub, free,
code and custom nodes MIT), ComfyUI (ComfyUI-Easy-Install recommended on
Windows, with a one-click UltraTex installer), FLUX.2 Klein base model
(must be the BASE variant), Qwen3 CLIP (GGUF workflow), FLUX.2 VAE,
BiRefNet background removal, trimesh mesh loading. The demo mesh is a
stylized character; the workflow is mesh-agnostic.

## Phase 1: Install UltraTex into ComfyUI

**Do**
1. Get ComfyUI first. The README's recommended route is ComfyUI-Easy-Install;
   its installation guide walks through every step.
2. On the UltraTex repo page, use Code, then Download ZIP.
3. Unzip it into the ComfyUI-Easy-Install folder. Two folders appear:
   `UltraTex-installer` and `UltraTex-workflows`.
4. Follow the README's copy step to put the installer and workflow folders
   in place, then double-click `install-ultratex.bat`.
5. On any other portable ComfyUI install, put the unzipped folder next to
   `python_embedded` and run `install-ultratex.bat` there instead.
6. Let the installer finish. It installs the nodes in tested, pinned
   versions, runs a real test plus the agent-attention kernel UltraTex uses
   on your GPU once, scans your ComfyUI model folders including
   `extra_model_paths.yaml` (so linked model folders are found), and copies
   the workflows into the ComfyUI workflow sidebar. The low-VRAM workflow
   is copied only if you answer yes to the low-VRAM version.

**Check**
- The installer completes its GPU test run without error.
- The UltraTex workflows appear in the ComfyUI workflow sidebar.

**Why**
Pinned node versions plus a real GPU test run are what make a one-click
install trustworthy: version drift in ComfyUI custom nodes is the usual
reason a downloaded workflow fails on first run.

## Phase 2: Pick the workflow for your VRAM

**Do**
1. Open the workflow sidebar and choose by GPU memory:
   - Workflow 1, Standard: 6 views plus PBR. 16 GB. Start here.
   - Workflow 2, Advanced: 10 views plus PBR.
   - Workflow 3, Low VRAM (GGUF): 6 to 8 GB.
2. Do not run the full model on a 6 to 8 GB card. The full model alone is
   about 9 GB and was tested on 16 GB cards; the GGUF workflow exists for
   the smaller cards.

**Check**
- The workflow you picked matches the VRAM band in the table above.

**Why**
View count and model precision are the VRAM levers. More views give more
coverage; quantization gives a runnable model. Picking the wrong band
first wastes a full run before failing.

## Phase 3: Load the mesh and the reference image

**Do**
1. Set the mesh path to your untextured mesh. Accepted formats shown in
   the graph: GLB, OBJ, PLY. The loader uses trimesh with
   `only_vertices_and_faces` enabled.
2. Load one reference image. This single image is what the textures are
   generated from: the demo's readable chest text ("VOLT") and arm patch
   ("07") come from the reference, not from a prompt.
3. Group the mesh path with the reference image, as the README instructs,
   before running.

**Check**
- The mesh preview shows your model untextured but correctly shaped.
- The reference image is the look you actually want, including any text or
  logos that must survive onto the mesh.

**Why**
UltraTex is reference-driven, not prompt-driven. A weak or wrong reference
cannot be fixed downstream; the texture will faithfully follow the wrong
image.

## Phase 4: Set the resolution and UV settings

**Do**
1. Albedo sampler resolution: 1024 for tests, 2048 for finals.
2. UV unwrap: in Prep, `uv_mode`. Keep the existing UVs for your own
   models instead of re-unwrapping.
3. Bake texture size: `texture_size` 2048.
4. Keep the Albedo LoRA strength at 1.00 (the graph's default for the
   UltraTex Albedo LoRA).

**Check**
- Test runs at 1024 read correctly before any 2048 final is queued.
- Your own UVs are preserved, not replaced by an automatic unwrap.

**Why**
1024 tests cost a fraction of a 2048 final and catch reference, mesh, and
workflow mistakes early. Re-unwrapping a finished model risks seams and
wasted UV space for no gain.

## Phase 5: Load the correct models (the failure mode that matters)

**Do**
1. Standard workflow: load the FLUX.2 Klein model, the UltraTex Albedo
   LoRA (`ultratex_flux2` family), the UltraTex Foreground VAE Decoder
   with the FLUX VAE, and the BiRefNet background-removal model
   (`birefnet.safetensors`).
2. Low-VRAM GGUF workflow: load the quantized models exactly as shown in
   the graph: UNet `flux-2-klein-base_9b-Q4_0.gguf`, CLIP
   `Qwen3-8B-Q4_K_M.gguf` with type `flux2`, and VAE
   `flux2-vae.safetensors`.
3. Verify the Klein variant before running: it must be Klein BASE. The
   normal (distilled) Klein model does not work with UltraTex.

**Check**
- Every model name matches the list above for your workflow.
- The Klein checkpoint is the BASE variant, not the distilled one.

**Why**
This is the workflow's known hard failure: the distilled Klein variant
silently does not work with UltraTex, so a run with the wrong checkpoint
wastes the whole generation instead of failing fast at load time.

## Phase 6: Run and export

**Do**
1. Press Run.
2. Open the resulting GLB in Preview 3D, or grab the files from the output
   folder.
3. Collect the outputs: the textured mesh plus the separate Albedo and MR
   (metallic/roughness) setups, with `base_color`, `roughness`, and
   `metallic` channels, plus the `unseen_before_fill` and
   `projection_confidence` passes. Preview renders are 2048 by 2048.

**Check**
- In Preview 3D, inspect the mesh from several angles, not just the front:
  the demo character reads cleanly from the front and the three-quarter
  view, with text and patches intact.
- Check the MR setup separately from the albedo: metallic and roughness
  must be their own maps, not baked into the color.
- Confirm text and logos survived: if the reference had readable text,
  the texture should carry it.

**Why**
Multi-view generation can still hide a bad angle. The separate MR maps
are what make the output usable as PBR in an engine instead of just a
pretty preview render.

## Phase 7: License check before production use

**Do**
1. Note the split: UltraTex code and custom nodes are MIT.
2. Read the model license in the README before client or production work.
   The README flags a restriction around training competing models, and
   states the model claims no ownership of your outputs.

**Check**
- You have read the model license yourself for your use case; do not rely
  on this skill's summary for a legal decision.

**Why**
Free and local does not mean restriction-free. The code license and the
model license are different documents, and the model license is the one
that governs production use.

## The human method, distilled

1. Match the workflow to the GPU first, then run. VRAM band is a Phase 2
   decision, not something to discover mid-run.
2. One good reference beats a long prompt. Choose the image for the text,
   logos, and material look it must carry.
3. Test at 1024, finalize at 2048. Cheap tests catch expensive mistakes.
4. Keep your own UVs. Automatic re-unwrapping is a last resort, not a
   default.
5. Verify the model variant by name before running. Distilled Klein is the
   known silent failure.
6. Judge the result in 3D from multiple angles, and judge the MR maps
   separately from the color. A good preview can hide a broken PBR set.

## Non-goals

- The video's closing promo for a separate Trellis2 Workflow Pack
  (GGUF low-VRAM workflow, full-precision workflow, PDF guide, RunPod
  template, prompt library) is a different product from UltraTex. It is
  not covered by this skill and its claims were not verified here.
- The "USE ELEVEN CREATIVE" sponsor card mid-video is unrelated to the
  workflow and is ignored.

## Depth status

PARTIAL (12 high-resolution frames from the downloaded video inspected
firsthand, including the README and the ComfyUI graphs; no captions or
transcript available, so spoken narration, exact install copy destinations
beyond what the frames show, and any settings only mentioned aloud are
not captured here. The README in the repo is the authority for install
details this skill could not read at full resolution.)
