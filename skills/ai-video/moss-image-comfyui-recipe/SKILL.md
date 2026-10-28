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
- Expansion 2026-10-28: "MOSS Image in ComfyUI | Text to Image, Words & Layout (Ep40)" by pixaromadesign — https://youtu.be/l4R96NemQS8 (19 min, 13,752 views, full captions, 466 segments, + description); Reddit post https://www.reddit.com/r/comfyui/comments/1xgwtyb/ (score 39). ASR garbles brand names in places ("PixArt-Alpha" for Pixaroma nodes, "Laura" for LoRA); settings below are taken from the description and from caption passages where the meaning is unambiguous.

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

## Expansion 2026-10-28: Pixaroma Ep40, nine free workflows

The 2026-10-21 recipe covers the model; Ep40 covers how to actually use it for text-bearing images. The core method is: MOSS Image is not an edit model, it is a text-rendering model, so every workflow gives it exact words (quoted, boxed, or same-seed swapped) and never asks it to change a picture in place.

### Phase E1: Install to the version gate, with the SFT checkpoint

**Do**
1. Check versions first: double-click the canvas, add a version check. MOSS Image needs ComfyUI 0.42 or newer and Pixaroma 1.4.219 or newer.
2. Download models first (three files): the model goes in diffusion models in a MOSS folder (create it if missing); take the model with SFT in its name ("That's the finished model. The base files are made for training LoRAs"); the text encoder goes in text encoders; the VAE goes in the VAE folder (small FLUX 2 VAE, "a different file from the normal one").
3. Restart ComfyUI or press R to refresh the lists.
4. Learn the node colour convention, shared by all nine workflows: orange nodes load the models; blue nodes are the only ones you change, numbered in order; green nodes do the work; the red node saves. Outputs go to ComfyUI's output folder, each workflow in its own folder.
5. Expect the first run to take longer: ComfyUI loads about 13 GB of models from disk; after that they stay loaded.

**Check**
- Version check shows ComfyUI 0.42+ and Pixaroma 1.4.219+ before any workflow runs; the SFT (not base) checkpoint is loaded.

**Why**
Most "MOSS doesn't work" failures are version or checkpoint failures, not model failures. The colour convention is what makes nine workflows learnable as one pattern.

### Phase E2: Write text-to-image prompts the MOSS way

**Do**
1. Workflow 1, text to image: describe in order: kind of image, then the person and what each hand does, the place, the light, and the camera.
2. Put words that must appear in the image in double quotes, e.g. "pizza cafe on the wall". Skip "masterpiece" / "best quality"; describe what to see instead.
3. Seed control: F keeps the same image, R makes a new one every run. After the first run, about 9 seconds per image on the creator's card (card model not stated in captions; do not assume one).
4. Workflow 2, prompt helper: type a short idea (creator's example: a poster for a summer jazz night on a rooftop); the helper (the same text encoder that reads the prompt) writes the long prompt in about 2 seconds. Toggle between the AI-written prompt and the prompt as typed. Read the shown text and put the words you want in the idea in double quotes, because the helper invents details: in the creator's run it invented a date ("I never asked for that date. The helper made it up"). Two seeds: the AI-prompt seed rerolls the written prompt; the image seed makes a new image from the same prompt without re-running the helper.
5. RTX 30-series failure mode (creator): the run can stop with a CUDA error; restart ComfyUI, open the gear on the AI-prompt node, and turn off faster writing.

**Check**
- The sign on the wall is spelled right. For posters, every line reads right, not just the title.

**Why**
MOSS's differentiator is legible words, and words are only legible when specified: quoted, complete, and checked. Vague prompts produce made-up small text, which is the model's predictable failure, not bad luck.

### Phase E3: Go fast with the 4-step speed LoRA, for drafts only

**Do**
1. Workflow 3: add the speed LoRA (the one new file in download models, in a LoRA folder under MOSS). Prompt and size work the same as workflow 1.
2. On the K sampler, keep 4 steps and CFG 1: "The LoRA was made for exactly that."
3. Expect about 1 second per run on the creator's card, a new version every run.

**Check**
- Speed is about 8x the full workflow; if a fast run is used as a final, its small-text errors are the user's fault, not the model's surprise: big words stay right, small lines can gain or lose a word, skin comes out a little smoother. "When every word counts, use workflow one for the final image. The same prompt and seed there give you a similar image, not the same one."

**Why**
Draft speed and final accuracy are different jobs. The LoRA buys the first and must never be mistaken for the second.

### Phase E4: Put words in pictures, then lay them out in boxes

**Do**
1. Workflow 4, words in pictures: every word goes in double quotes; give each line its own quotes on its own line, and MOSS keeps the line breaks. Describe the letters (e.g. big, bold chalk letters) and what they are on (e.g. the chalkboard). Creator's checks: a chalkboard menu (title, today's menu, five lines each with a price) came out right on four seeds out of four. A book cover works only when the title is described as part of the painting ("hand-painted and lit by the lighthouse"), not pasted on.
2. Rule: the smaller the letters, the more room for a mistake, so for a lot of words pick a bigger size. Things that usually carry words (books in the background) get made-up letters unless you give the words.
3. Workflow 5, layout with boxes (Pixaroma layout-boxes node): a small canvas shaped like the image; each box is one thing (object or text). Click to select, drag a corner to resize, drag inside to move, undo steps back. Step 1 is size (box canvas takes the same shape); step 2 boxes for the creator's skincare ad: headline at top, bottle in middle, small line at bottom. A text box has its exact words plus a short description of the letters; an object box has one full description. Colours go in the words; box colour only helps you see them. Step 3 prompt describes the whole image (kind, background, colours, light); do not name the boxes there.
4. Boxes are guides, not cutouts: "The bottle fills its box roughly with its own shape and shadow." For a person/character, type its box number in the character boxes on the MOSS node.
5. Workflow 6, same picture, new words: same prompt, same seed (keep seed on F), changing words in square brackets split by a vertical bar (creator's example: Anna, Mark, Sophia, Leo). One run makes one image per name, about 9 seconds each, shown together in an image grid. Two bracket groups make every combination (two colours x two names = four images). Caveat: "It's not always exactly the same image though. Sometimes a small thing changes. The steam moves or an extra candle shows up."

**Check**
- Menu: every word and every price right, across seeds. Ad: headline, bottle, and small line all spelled right and each sitting in its box. Name swap: same cup, same light, new name on each.

**Why**
Quoted words control spelling; boxes control placement; same-seed brackets control variation. Each mechanism answers a different question (what words, where, which variant).

### Phase E5: Know the three honest failures, then work with your own pictures

**Do**
1. Failure 1, words you did not give: a sign or poster in the background can come out with made-up letters. Fix: give the words in double quotes, or let the workflow-2 helper write them.
2. Failure 2, editing: MOSS is not an edit model. "It does not change an image you give it." In the creator's edit/restyle tests it did not keep the image (hair and face changed). No edit workflow is in this episode; the creator points to FLUX 3 Klein (Ep39) or FLUX 2 for edits today.
3. Failure 3, big sizes: asking for a big size directly gives a different image (same prompt and seed, 2048 gave a different person). Fix: find the image at normal size, then enlarge with workflow 8.
4. Workflow 7, image to prompt to image: load an image; the text encoder writes a detailed prompt in about 2 seconds; pick 1536 when the image has small words so the AI sees them bigger. Result is a new image, not a copy. Add a change at the end of the idea in the AI prompt (e.g. "but at night with warm light in the window").
5. Workflow 8, upscale 2x keeping the picture: make the image in workflow 1, paste the same prompt, same size, same seed; step 4 denoise for the second pass, 0.35 is a good start. About 50 seconds on the creator's card; the example goes to 2048x2560 with real detail in hair, beard, and latte art, sign staying right.
6. Workflow 9, upscale any picture: load any image, pick the size before it doubles (1024 becomes 2048), denoise 0.25 is a good start (0.15-0.20 for small faces in a group photo). Needs one new file, an upscale model in upscale models. About 30 seconds. Caveats: it repaints lightly, so small details can change; it does not repair (scratches on an old photo stay); on photos skin and hair can come out too smooth; illustrations and 3D images benefit most.

**Check**
- Upscale check: same barista, same sign, more detail, not a different person. Edit check: if the face changed, you asked an edit question of a generation model; use the FLUX route instead.

**Why**
Every failure here has a named workaround that respects what the model is: generate at normal size then upscale, quote the words you want, and never ask MOSS to edit.

### Ep40 human method, distilled

1. Quote every word that must be spelled right; never let the model guess small text.
2. Use boxes for placement, same-seed brackets for variants, and the full workflow (not the speed LoRA) for finals.
3. Read the helper's shown text before running: invented dates and details are visible there, before they are baked into an image.
4. Generate small, then upscale; never generate big directly, and never ask a generation model to edit.

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
