---
name: pruna-p-h3-image-comfyui
description: "Run Pruna's P-H3-Image in ComfyUI: a distilled MiniMax H3 image model with a 4B text encoder, int8 weights, a prompt upsampler, and an 8-step distilled sampling schedule (ManualSigmas + er_sde, CFG 1). Text-to-image and image edit from the official ComfyUI workflow templates, 35.31 GB total. Trigger when doing local H3-class image generation or editing on a mid-range GPU and the full H3 stack is too heavy."
---

# Pruna P-H3-Image in ComfyUI

## Purpose

This skill reconstructs the exact workflow from crystal_alpine's post, the
official ComfyUI workflow templates, and the comment thread, step by step,
so another agent can run Pruna's P-H3-Image in ComfyUI. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The core method is: distill H3 down to an int8
image model with a small text encoder, and let a prompt upsampler plus an
8-step distilled schedule do the work the big model used to do.

## Source

- Post: "Pruna P-H3-Image is now available in ComfyUI" by crystal_alpine —
  https://www.reddit.com/r/comfyui/comments/1xn9ufc/pruna_ph3image_is_now_available_in_comfyui/
  (r/comfyui, score 99, 13 comments, 12 retrieved)
- Templates (read node-by-node): `image_p_h3_image_edit.json` (24 nodes)
  and `image_p_h3_t2i.json` (subgraph) in
  Comfy-Org/workflow_templates — https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_p_h3_image_edit.json
  and https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_p_h3_t2i.json
- Models: https://huggingface.co/PrunaAI/p-h3-image-comfy
  (diffusion model from Comfy-Org/MiniMax-H3)
- Evidence: full post text, 12 comments, both templates with exact
  filenames, sizes, sigmas, and prompt format. Native clip; no video
  transcript exists, but the workflow is fully specified by the templates.

## Tools used

**Pruna P-H3-Image** (distilled image model built on MiniMax H3, 4B text
encoder); **ComfyUI** (update first — Desktop/Cloud updates follow stable
releases, so nightly-supported models may not be available there).

## Phase 1: Install the models (35.31 GB total)

**Do**
1. Update ComfyUI first (the template notes Desktop/Cloud updates follow
   stable releases, so nightly-supported models may not be available there).
2. Place the files (template's own storage map):
   - `diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors`
     (19.53 GB, from Comfy-Org/MiniMax-H3)
   - `text_encoders/p-h3-image_text_encoder_int8_convrot.safetensors`
     (4.77 GB) and
     `text_encoders/p-h3-image_prompt_upsampler_w4a8.safetensors` (6.26 GB)
   - `vae/p-h3-image_vae_int8_convrot.safetensors` (2.93 GB)
   - `loras/p-h3-image_lora_bf16.safetensors` (1.82 GB)
3. Load the official template for the job: `image_p_h3_image_edit.json`
   (image edit) or `image_p_h3_t2i.json` (text to image).

**Check**
- Total on disk: 35.31 GB. The "lighter and faster" claim is relative to
  full H3, not absolute: the diffusion model alone is 19.53 GB.

**Why**
The whole workflow is int8/w4a8-quantized except the bf16 LoRA: the size
saving is the product, and the template's file map is the install contract.

## Phase 2: Write the prompt as aspect ratio + one request

**Do**
1. Write the prompt in the template's format: `Aspect ratio: <ratio>` on
   one line, then `Request: <what to change>` (edit) or the request after
   `Request:` in the prompt box (text to image). The prompt upsampler
   expands it before sampling (TextGenerateV2, 1536 tokens).
2. Keep the request to one short sentence: "The model keeps the
   composition when the request is one short sentence" (template note).
   Example from the template: "Aspect ratio: 1:1 / Request: change the
   lighting to night time".
3. Keep the `Aspect ratio:` line in sync with the Resolution Selector:
   "otherwise the prompt asks for one shape and the latent produces
   another" (template note).

**Check**
- Sizes at 8.0 MP, multiple 32 (template table): 1:1 Square 2912x2912;
  4:3 Standard 3360x2496; 3:2 Photo 3552x2368; 16:9 Widescreen 3872x2176;
  3:4 Portrait Standard 2496x3360; 2:3 Portrait Photo 2368x3552; 9:16
  Portrait Widescreen 2176x3872. Width and height 0 give 2912x2912.
- For image edit, the source image goes into `Load Image` and the result
  matches its shape, so width/height on the conditioning follow the image
  automatically. ImageScaleToTotalPixels: lanczos, 0.95, 32.

**Why**
The upsampler does the prompt engineering; the human's job is a short,
shape-consistent request. Shape disagreement between prompt and latent is
the documented failure mode.

## Phase 3: Sample the 8-step distilled schedule

**Do**
1. Sample with the template's fixed schedule: `ManualSigmas` 9 values
   ("1.0, 0.984753, 0.967905, 0.951688, 0.925372, 0.881923, 0.810083,
   0.528718, 0.0") with sampler `er_sde`, CFG 1, MiniMaxH3SigmaShift [1, 1].
2. Load the LoRA (`p-h3-image_lora_bf16.safetensors`) at strength 1
   (LoraLoaderModelOnly).
3. Set seed control to `randomize` for new images, back to `fixed` to
   reproduce the shipped example.

**Check**
- "Sampling is an 8-step distilled schedule (`ManualSigmas` + `er_sde`,
  CFG 1) — more steps do not help" (template note). Do not raise the step
  count expecting quality gains.

**Why**
Distillation bakes the quality into 8 steps; the schedule is the model,
not a tuning knob.

## Production practice

No AAA game studio publishes a distilled-H3 image-model recipe, so this section is production inference practice, labeled as such, not a studio claim. The pattern it documents is the same stack the skill uses, applied as a measured discipline with one shipped-title precedent:

- **Compress in layers and state each layer's saving.** Pruna's own account of P-H3-Image lists the layers in order: a prompt upsampler (Qwen3.5-9B) that expands short requests; the text encoder distilled from 32B to 4B (67 GB to 9 GB, same image quality claimed); sampling distilled from 50 steps to 8 via advanced DMD; a retrained decoder because H3's video decoder returned blurry single frames; and quantization to 8-bit and 4-bit. The vendor's headline numbers are 7x smaller and 5x faster than the original H3, with the smallest ComfyUI set at 20 GB against 143 GB for H3. The discipline is to keep each layer separable and stated, so a quality regression can be blamed on one layer instead of on "the distilled model."
  Source: https://www.llms.blog/posts/p-h3-image-pruna-open-image-model
- **Quantize, then validate against the full-precision reference.** NVIDIA's production quantization guidance (TensorRT ModelOpt) names TensorRT the recommended production target for quantized ONNX models (2-4x for INT8) and states the rule plainly: always validate accuracy versus FP32 and FP16, and run an initial pilot on a representative subset before large-scale deployment. Pruna's own framework follows the same shape: compress with a SmashConfig (cachers, compilers, quantizers such as HQQ), then evaluate throughput, total time, and CLIP score against the base model; their SDXL example reports about 2x faster and smaller with CLIP score nearly unchanged.
  Sources: https://docs.nvidia.com/tao/tao-toolkit/latest/text/tao_quant/limitations.html and https://docs.pruna.ai/en/stable/docs_pruna/tutorials/image_generation.html
- **Compressed AI media is shippable when it is measured: the shipped-title precedent.** EA and Petroglyph's Command & Conquer Remastered Collection (2020) shipped AI-upscaled FMV: the original master tapes were lost, the surviving footage was 320x200, and the team used machine-learning upscaling to bring it to HD at 30 fps with reworked audio. The upscaled footage is visibly a compromise next to true HD, and it shipped anyway, because the alternative was no FMV at all. That is the bar this skill's "lighter and faster, not better" tradeoff has to clear: a measured compromise that ships beats a full model that does not fit the card.
  Sources: https://dontfeedthegamers.com/command-and-conquer-remastered-cutscenes-fmv-ai/ and https://en.wikipedia.org/wiki/Command_%26_Conquer_Remastered_Collection
- **Treat 4-bit as a separate promotion, not a free upgrade.** Pruna's own stated limits: the 4-bit version keeps the quality but can change small details and sometimes the composition. The ComfyUI template in this skill already ships int8 with a bf16 LoRA; a 4-bit variant is a different model for acceptance purposes, not the same model with a smaller number.
  Source: https://www.llms.blog/posts/p-h3-image-pruna-open-image-model

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Write a `compression-manifest.json` for every install: each file with its precision (int8 diffusion, int8/w4a8 text encoder and upsampler, int8 VAE, bf16 LoRA), its size, and the layer it belongs to (upsampler, encoder, sampler, decoder, quantizer). If any file is swapped for a 4-bit variant, the manifest records it as a new model version, not a patch.
2. Add a fixed acceptance set before committing to the model: five prompts spanning the failure modes the thread already names, one short single-sentence request (the template's sweet spot), one complex multi-clause request (the 4B encoder's stress case), one texture-heavy subject at 8 MP (the VAE pixelation case), one edit that must preserve composition, and one RefMod identity pass. Record pass/fail per prompt in the manifest.
3. Run the VAE pixelation check from the failure modes as a gate, not a note: generate the texture-heavy prompt at 8 MP, inspect at 100% zoom, and record whether pixelated texture appears. A fail means the model is disqualified for texture-heavy work, not that the prompt needs rewriting.
4. Keep the "lighter and faster, not better" verdict in the manifest: if full H3 is already runnable on the card, record that this model is a resource tradeoff, not a quality upgrade, and say so in the run log.

**Check**
- A P-H3-Image install is accepted only when its compression manifest is complete and its five-prompt acceptance set passes; an install with a missing manifest or an unrun acceptance set is an unmeasured claim, not a budget.
- A 4-bit variant is accepted only when it passes the same five-prompt set against the int8 baseline on identical prompts and seeds; a 4-bit run that changes composition on the identity or edit prompt is rejected, not tuned around.

**Why**
The skill's value is a reproducible install-and-acceptance contract for a hardware class, not one 35.31 GB download. A manifest plus a fixed acceptance set turns Pruna's vendor numbers into a measurement the agent can repeat, and the 4-bit promotion gate is what keeps the smallest file from quietly becoming the default.

## The human method, distilled

1. Quantize everything, then let the upsampler carry the prompt.
2. One short request, one shape: aspect ratio and latent must agree.
3. Eight steps is the schedule: more steps do not help.

## Failure modes

- **VAE pixelation at high megapixels.** Commenter fallengt: "VAE isn't
  built for images; the model automatically compresses picture quality.
  Even at 8 megapixels, we get pixelated texture" (with a sample image).
  The image-first VAE question is open; check texture quality at 8 MP
  before committing to the model.
- **CLIP-size cost.** Commenter TurbTastic: lighter and "significantly...
  more forgiving for low/medium GPUs", but "reducing the CLIP model size
  that much is going to come at a significant cost." The 4B text encoder
  is the tradeoff; watch prompt adherence on complex requests.
- **"What is the point if you can do the same with minimax?"**
  Commenter jd3k's challenge: the distilled model's advantage is
  lighter/faster, not better. If you already run full H3, this is a
  resource tradeoff, not a quality upgrade.
- **Consistency claim is one user, unverified.** Commenter
  Affectionate_Rub9491 (non-technical, favorite had been Qwen 2.1): "This
  one simply BLOWS it out of the water with realism and consistency... in
  90% of generations." Treat 90% as one user's report, not a measurement.
- **Works with RefMods.** Commenter edisson75: "Just in case, it works
  with refmods too" (with a sample image, +14); the apply-refmod node goes
  "between the conditioning output and the input of the guider." Identity
  workflows transfer to this model.
- **Training support exists.** Commenter imlo2: "Ostris just posted to X
  about having added P-H3-Image training support to AI-Toolkit."

**Depth status:** FULL (full post text + 12 comments + both official
workflow templates read node-by-node with exact filenames, sizes, sigmas,
and prompt format; no video transcript exists for a native clip, but the
workflow is fully specified by the templates).
