---
name: moss-image-comfyui-recipe
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

## AAA studio practice

AAA studios do not treat AI image generation as a final-art machine; they treat it as a supervised, directional stage with human review before anything ships. That maps directly onto this recipe:

- **AI output is directional, not final.** A studio writeup from Retrostyle Games reports environment mood boarding as the clearest production win: 30 lighting and color-grading variations of a dungeon in about 20 minutes with a tool like Midjourney or Firefly, versus two days for a junior artist to paint the same exploration by hand, with the AI variants explicitly "directional, not final" and used to lock a visual direction early. Prop concepting at volume is the second win: a first pass over 80 distinct medieval weapons in a day, then a human artist reviews for style-guide consistency and redraws violators, for a reported roughly 30-40% reduction in concept hours in that supervised workflow. Source: https://retrostyle-games1.artstation.com/blog/PQMXE/ai-in-game-art-what-studios-actually-ship-in-2026
- **Production use is broad but shallow.** A 2026 VAIA interview study of 101 senior games-industry leaders (Vivrato) found 94% reporting current production use of AI in at least one pipeline stage, with concept and pre-production at 79% and art, assets and animation at 60%, but a median self-rated integration depth of only 3/10. The reading for this skill: studios keep generative tools at the edges of the pipeline, under human supervision, rather than letting them drive final art. Source: https://www.invenglobal.com/articles/27509/vaia-study-finds-94-of-game-studios-using-ai-in-production
- **Layout control is now a first-class production feature, not a trick.** Black Forest Labs' FLUX 3 Image adds layout-controlled generation: each important element sits in a bounding box on a normalized canvas with its own description, aimed at advertising layouts, editorial graphics, and product variations where a consistent frame matters. The same writeup warns that a published example is not proof every requested word, product shape, or brand element survives a revision, and that outputs still require visual inspection, especially for rights-sensitive likenesses, logos, and exact copy. MOSS-Image's layout JSON is the open-weights version of that same discipline: the box is the art direction, the prompt fills it. Source: https://www.therundown.ai/tools/flux-3-image
- **Reuse one layout across shots of one location.** A third-party MOSS-Image writeup notes the layout JSON places each item (label, caption, optional text, bounding box) and that using the same layout for several shots of one location keeps a sign in the same place, so shots cut together cleanly. This is the poster equivalent of a locked set: decide where the sign goes before deciding what it says. Source (third-party writeup, not a studio claim): https://studio.aifilms.ai/blog/moss-image-open-source-layout-control-text-rendering

## Agent automation

Convert the manual recipe above into an agent-runnable job. These steps are automation of the recipe, not new studio claims:

**Do**
1. Write a job manifest JSON before generating anything: one entry per deliverable with `id`, `layout_json_path`, `checkpoint` (Base or SFT), `resolution`, `steps`, `cfg`, `shift`, `seed`, and `expected_text` (the exact strings that must render legibly). The manifest is the review surface: a human approves the manifest, not a pile of loose generations.
2. Submit the official workflow through ComfyUI's API instead of clicking the GUI: export the workflow once in API format, then POST it to the ComfyUI server's `/prompt` endpoint (default port 8188), varying only the manifest fields per job, and poll until each job completes. The GUI stays for building and testing the workflow; the API is for batch runs, headless servers, and CI-style pipelines. Source for the API pattern: https://dev.to/jovan_chan_9500711396d4e6/comfyui-api-tutorial-2026-automate-image-generation-3j2j
3. Gate every output on text legibility before it counts as done: run OCR over each rendered text region (or, at minimum, visually inspect each text box at 100% zoom) and compare against `expected_text`. Any mismatch is a failed job, not a near miss: regenerate with the same layout JSON and a new seed, and log the failure against the manifest entry. [Inference: no cited studio runs an OCR gate on MOSS-Image; this gate is the agent-executable version of the "outputs still require visual inspection" warning above.]
4. Pin the ecosystem artifacts in the manifest: checkpoint revision, quant revision, and every LoRA/ControlNet revision used. Re-check the ecosystem weekly per Phase 4, but never let a floating "latest" revision change a pinned job mid-batch.

**Check**
- Every manifest entry has a saved output image plus a pass/fail text check, and every failure names the seed and layout used so it is reproducible.
- The same layout JSON reused across shots of one location produces the sign/text in the same place in each shot; drift is a layout failure, not a style variation.

**Why**
Studios keep AI generation supervised and shallow in the pipeline; the manifest plus the text gate plus pinned revisions is what supervision looks like when an agent runs the batch. Without them, a fast batch is just fast drift.

## Caveats from the thread (relevant to automation)

- ComfyUI 0.36's **native loops are recursion-based** and suffer long startup delays plus max-recursion crashes past a few dozen iterations (~70 reported ceiling; PR Comfy-Org/ComfyUI#16227 replaces recursion with iteration, unmerged; fix PR #16556 linked). If you automate ComfyUI with native loops, pin the workaround or avoid native loops.
- Agentic signal worth knowing: one commenter (BazzTheBazz, score 6) reported using "Claude with the comfy mcp" to autonomously test workflows, fine-tune them to spec, download models, and place them in the right folders — "The whole thing." First-hand evidence for agent-driven ComfyUI automation; treat as prior art, not as a verified recipe.

## The human method, distilled

1. Start at the author's settings (1024×1024, 50 steps, CFG 3, shift 5) and accept slowness until a distilled variant exists.
2. Quantize the text encoder first — it is the VRAM hog.
3. Check the ecosystem weekly, not daily; pin working artifacts.

## Depth status

PARTIAL — full post selftext and 25 top-level comments; the native demo clip was not content-analyzed. No parameters were invented; VRAM and settings figures are author/community-stated.
