---
name: "moss_image_comfyui_recipe"
description: "Run OpenMOSS MOSS-Image (5B DiT, Apache 2.0) in ComfyUI: starter settings, VRAM/quant options, layout-JSON text rendering, and the community LoRA/tooling wave. Trigger when generating text-bearing images, posters, or concept art with open weights."
---

# MOSS-Image in ComfyUI | Open-Weights Text-Rendering Recipe

## Purpose

This skill reconstructs the recipe from the release post and its comment thread, step by step, so another agent can run the same model. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: run the official Comfy-Org workflow with conservative settings, quantize if VRAM-bound, and ride the community's LoRA/tooling wave rather than re-deriving it.

## Source

- Post: "OpenMOSS released MOSS-Image, and it's now supported in ComfyUI." by crystal_alpine — https://www.reddit.com/r/comfyui/comments/1xa6wmo/ (score 130, 28 comments, 25 top-level retrieved)
- Official workflow: https://huggingface.co/Comfy-Org/MOSS-Image
- Evidence: full post selftext + 25 top-level comments, 2026-10-21 scout run

## Tools used

MOSS-Image by OpenMOSS (5B DiT, Qwen3.5-9B text encoder, FLUX.2 VAE, Apache 2.0; Base and SFT checkpoints), ComfyUI with the official Comfy-Org workflow. Community artifacts reported in the thread: 4- and 8-step Turbo LoRAs, 2+ full finetunes, depth ControlNet (LoRA), inpainting workflow, experimental image-editing plugin.

## Phase 1: Know what the model is

**Do**
1. Architecture: 5B DiT using a Qwen3.5-9B text encoder and the FLUX.2 VAE.
2. Pick a checkpoint: **Base**, or **SFT** (fine-tuned on curated data).
3. License: Apache 2.0 — commercial use is fine.

**Check**
- Files come from the official Comfy-Org HuggingFace repo (huggingface.co/Comfy-Org/MOSS-Image).

**Why**
Apache 2.0 keeps the model usable in production/intake pipelines without license friction; the FLUX.2 VAE and 9B text encoder explain the VRAM footprint in Phase 3.

## Phase 2: Run it with the starter settings

**Do**
1. Resolution 1024×1024, 50 steps, CFG 3, shift 5 (author's recommended starting point).
2. Expect it to be slow: "Neither model is step-distilled, so it's not fast."

**Check**
- Prompted text renders legibly in English and Chinese — the headline capability: "Legible text in English and Chinese, which most open models still struggle with."

**Why**
Text rendering is the differentiator. **Layout prompts** are the second one: pass structured JSON with bounding boxes to control where text and objects go — "useful for posters, ads, and anything with a real layout." The author also notes the outputs "look good out of the box without much prompt wrangling."

## Phase 3: Fit it in VRAM

**Do**
1. Full BF16 weights: ~10 GB for the DiT plus ~17 GB for the text encoder (author-stated).
2. Use the community INT8 and INT4 quants; commenters report the model running on 8 GB cards.

**Check**
- The quantized run completes without OOM on the target card.

**Why**
The 9B text encoder dominates the VRAM budget; quantization is the practical route for single-GPU workstations.

## Phase 4: Ride the community wave (do not re-derive it)

**Do**
1. Four days after release (2026-10-17 → 2026-10-21) the community had already produced: multiple 4- and 8-step **Turbo LoRAs**, at least two **full finetunes**, a **depth ControlNet (LoRA)**, an **inpainting workflow**, LoRA support in popular trainers, an **experimental image-editing plugin**, and ComfyUI performance improvements (commenter infearia, score 19: "Every time I get back to my computer there is something new dropping for MOSS-Image. When am I supposed to test all that stuff?").
2. Re-check the ecosystem before committing to an artifact: verify each community LoRA/tool exists and is maintained — at this velocity, half-lives are short.

**Check**
- The artifact you depend on (quant, LoRA, ControlNet) is pinned to a working revision.

**Why**
For intake-style pipelines the base model is the commodity; the surrounding workflow/quant/LoRA ecosystem is the real integration cost. Track it weekly, not daily, and pin working artifacts.

## Caveats from the thread (relevant to automation)

- ComfyUI 0.36's **native loops are recursion-based** and suffer long startup delays plus max-recursion crashes past a few dozen iterations (~70 reported ceiling; PR Comfy-Org/ComfyUI#16227 replaces recursion with iteration, unmerged; fix PR #16556 linked). If you automate ComfyUI with native loops, pin the workaround or avoid native loops.
- Agentic signal worth knowing: one commenter (BazzTheBazz, score 6) reported using "Claude with the comfy mcp" to autonomously test workflows, fine-tune them to spec, download models, and place them in the right folders — "The whole thing." First-hand evidence for agent-driven ComfyUI automation; treat as prior art, not as a verified recipe.

## The human method, distilled

1. Start at the author's settings (1024×1024, 50 steps, CFG 3, shift 5) and accept slowness until a distilled variant exists.
2. Quantize the text encoder first — it is the VRAM hog.
3. Check the ecosystem weekly, not daily; pin working artifacts.

## Depth status

PARTIAL — full post selftext and 25 top-level comments; the native demo clip was not content-analyzed. No parameters were invented; VRAM and settings figures are author/community-stated.
