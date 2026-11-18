---
name: qwen-image-21-comfyui-local
description: "Use Qwen-Image-2.1 locally in ComfyUI as an everyday image model: 7B parameters, Turbo 8-step generation at 16 seconds per image on an RTX 4080, text-to-image, multi-image edit with up to 10 references, character sheets for consistency, and background removal to transparent PNG. Trigger when a local image model is needed for concept art, character sheets, or image edits without a cloud service."
---

# Qwen-Image-2.1 in ComfyUI (Local, Turbo 8-Step)

## Purpose

This audit reconstructs the exact workflow from Olivio Sarikas's tutorial, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: one small local model does text-to-image, image edit, and background removal, fast enough to use every day.

## Source

Creator: Olivio Sarikas. Video: "Super Fast & Easy Local Model — I use this everyday!", https://www.youtube.com/watch?v=jQZZOWY7Arg (10 min 37 s, 11,845 views, uploaded 2026-11-16). Models + workflows: https://huggingface.co/Comfy-Org/Qwen-Image-2.1. Evidence: full ASR captions (241 segments) mined firsthand; description and model-card link corroborate the 7B / 8-step Turbo / 10-reference claims. No media download was used; captions + description carry the full workflow. 2026-11-17 scout run.

## Tools used

Tools used: **Qwen-Image-2.1** (7B parameters, open-source weights; **Turbo 8-step** version), **ComfyUI**, Hugging Face workflows (text-to-image, Turbo image edit, background remove).

## Phase 1: Pick the model and the workflow

**Do**
1. Go to the Hugging Face model card (Comfy-Org/Qwen-Image-2.1): the files are laid out by category, and the workflows section lists one workflow per application (image edit with multi-image input, text-to-image, Turbo image edit, text-to-image Turbo, background remove).
2. Download the workflow for the application you want and drop it into ComfyUI; the workflow tells you which models to download and where they go.
3. Choose the Turbo version for daily use: 8 steps ("fast 8-step Turbo version", description).

**Check**
- The workflow opens in ComfyUI naming the exact model files it needs; a missing file is named by the workflow, not guessed.

**Why**
The model card does the curation: one repo holds the model variants and the matching workflows, so setup is file selection, not research.

## Phase 2: Generate with reference images

**Do**
1. Text-to-image: prompt normally; the model "renders text in images well" (description) and handles object relations (author's example: a cat looking at a fish with its paw ready).
2. Use up to 10 reference images (description) for image-to-image and multi-image edit: e.g. an image on the left plus an image of a jeans shirt, "replace that shirt with the jeans shirt and boom it does that."
3. Build character sheets as a first-class output: front, side, and back views plus detail views of different assets (ring, glasses), because "these higher resolution assets... can be used in the image to give you higher resolution results if you for example have a closeup of that back or the ring or the glasses to keep the consistency of these assets."
4. Speed, measured by the author: 16 seconds per image on an RTX 4080 after the model is loaded ("after the model has been loaded, it only takes me 16 seconds per image on my 4080").

**Check**
- Text in the image reads correctly (the author shows an infographic with designed steps as the text-rendering proof); character-sheet detail views stay consistent with the sheet's main views.

**Why**
Reference images are the consistency mechanism: the model keeps a character's assets straight because the sheet gives it the same asset from several angles at higher resolution.

## Phase 3: Remove backgrounds to transparent PNG

**Do**
1. Generate with a transparent alpha channel directly, or run the background-remove workflow on an already-created image: "the background is already removed when you render the image and you can see it here moving on a space background."
2. Animate the transparent result yourself afterwards; the alpha channel is the handoff to the animation step.

**Check**
- The rendered image moves cleanly over a different background with no halo: that is the proof the alpha is real, not a white background.

**Why**
Transparent output removes the keying step entirely: the image is already an asset, not a picture that needs cutting out.

## Caveats, stated by the author
- "This model is not open for commercial use" (video ~2:39). Do not use it for commercial game assets without checking the license.
- "This is an uncensored model, so it can also do the spicy stuff." (video ~3:09.) No content filter is built in.

## The human method, distilled
1. "Fast rendering, easy to use, has a lot of application and good prompt understanding." (video 0-1 min, quoted: the four reasons it is the author's everyday model.)
2. "After the model has been loaded, it only takes me 16 seconds per image on my 4080." (video 0:38, quoted: the speed claim, with hardware named.)
3. Character sheets first, close-ups second: the sheet is what keeps the assets consistent. (video 2:18-2:44, paraphrased.)

## Failure modes
- Inconsistent assets across generations: the fix is the character sheet (front/side/back + detail views), not more prompting.
- Commercial-use restriction: the model is not open for commercial use. Fix: check the license before any commercial asset use; use it for non-commercial work otherwise.
- No content filter: the model is uncensored. Fix: do not assume any safety filtering; keep generations in a reviewed pipeline.

## AAA studio practice
Character model sheets (front/side/back + detail views) are the standard consistency mechanism in animation and film production: every character that must survive multiple shots gets one. The video's contribution is that a local 7B model can now consume the sheet directly as reference images, so the sheet stops being a human-only document and becomes a model input. The same sheet-as-input pattern is what the MiniMax H3 character-swap workflows use for video. AAA studios now run local ComfyUI pipelines in exactly this shape. Ubisoft La Forge open-sourced CHORD, its PBR material estimation model, with ComfyUI nodes for an end-to-end material workflow: a three-stage pipeline (texture image generation from prompts or reference inputs, CHORD image-to-material estimation into Base Color/Normal/Height/Roughness/Metalness, then industrial-grade upscaling from CHORD's 1024 resolution to 2K and 4K production assets), described as "a significant step toward integrating ComfyUI into AAA-scale video game production workflows." Ubisoft's DigiPro 2025 agentic asset pipeline runs a ComfyUI image-generation pipeline that converts briefs into asset casting lists with concept previz imagery, retrieves from a library of over 30,000 production-indexed USD assets, and populates Blender scenes via MCP. The reference discipline shows up in consumer tools too: Leonardo AI's trainer locks a style from 10-20 references, after which a whole asset pack becomes a few clicks rather than a few hundred generations.

The production rule that transfers: reference-driven, multi-stage, with an explicit upscaling ladder and a license logged per model. CHORD itself ships under a Research-Only license, and Qwen-Image-2.1 is not open for commercial use; the manifest must carry the license, not just the model name.

Sources:
- ComfyUI blog, "Ubisoft Open-Sources the CHORD Model and ComfyUI Nodes" (3-stage pipeline, 1024 to 2K/4K upscale, ComfyUI in AAA production): https://blog.comfy.org/p/ubisoft-open-sources-the-chord-model
- DigiPro 2025, "From Brief to Scene: Agentic AI for Asset Production at Ubisoft" (ComfyUI image pipeline, 30k USD asset library, Blender MCP): http://digiproconf.org/program/program-4/
- Leonardo AI review (reference/seed consistency controls, 10-20 reference trainer locks style; tool review, labeled): https://getaitoolnav.com/leonardo-ai/

### Agent automation upgrade (Do / Check / Why)
**Do**
- Automate the sheet-to-close-up loop: generate the character sheet first, then feed its detail views back as reference images for every close-up generation, and log which sheet version each output used.
- Add a model-license field to the run manifest: record the license and the commercial-use flag for every model version used, and fail the run if a commercial-use asset is generated with a model flagged non-commercial (Qwen-Image-2.1 is not open for commercial use; CHORD is Research-Only).
- Add a reference-count gate: assert no generation uses more than 10 reference images, the model's stated limit, and fail with the count attached if it does.
- Add an upscaling ladder: generate at Turbo 8-step low resolution first, promote only the accepted images to full resolution, mirroring CHORD's 1024-to-2K/4K stage split.
**Check**
- Every close-up names its sheet version in its metadata, so a drifted asset can be traced to the sheet that produced it.
**Why**
- The author's consistency mechanism only works if the sheet is actually reused; logging the reuse makes it auditable instead of habitual, and the license field keeps the commercial-use restriction from being discovered after the asset ships.

**Depth status:** FULL (10-min ASR captions, 241 segments, mined firsthand; description and model card link corroborate the 7B / 8-step Turbo / 10-reference claims; no media download was used, none was needed: captions + description carry the full workflow).
