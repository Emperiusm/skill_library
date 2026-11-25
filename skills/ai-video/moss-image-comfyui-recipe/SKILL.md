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
- Expansion 2026-11-21: "MOSS Image ROCKS! Fast, Uncensored & Under 6 GB – EASY Install Guide" by Olivio Sarikas — https://www.youtube.com/watch?v=amjhvE-h2kM (10:32, 10,996 views, uploaded 2026-11-20, full ASR captions, 252 segments, + description); 2026-11-21 scout run, audit 5. A distinct low-VRAM variant on the same model: int8 quantized generation-optimized workflow at 1-2 MP plus Ultimate SD Upscale, not the 50-step starter recipe and not the tuned fusion. Model file names were ASR-garbled in the captions; the exact names and sampler/upscale numbers are now frame-verified in Phase G5 (2026-11-22 expansion).
- Expansion 2026-11-25: "MOSS TURBO - 4 Steps ONLY! Fast & Uncensored - EASY Install Guide" by Olivio Sarikas — https://www.youtube.com/watch?v=4gmEzsXOO6Q (17:13, 4,931 views, uploaded 2026-11-24, full captions, 400 segments, + description); 2026-11-25 scout run, audit 2. Turbo LoRA install/wiring/settings/defect evidence (MOSS_Image_SFT_4_steps_v2, LoRA Manager, 4-8 steps, CFG 1, Euler) in Phase H.

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

## Expansion 2026-11-18: wjc_5 tuned fusion (layer-specific Base/SFT blend + Guanlan LoRA)

Source: "MOSS Image: All-Purpose Text-to-Image | Stunning Aesthetics, Blazing Speed, Top-Tier Quality | Tuned Fusion Parameters | Beat Closed-Source Models" by wjc_5, r/comfyui post 1xxs8k1 (score 35, 17 comments; full post text read) | Video walkthrough: https://youtu.be/oOwUkO7qLps | Workflow: https://www.runninghub.ai/ai-detail/2120396101965631490 (free download, no login; also runnable online) | 2026-11-18 scout run, audit 2. This is a distinct recipe from the Ep40 Pixaroma workflows above: same model, a tuned fusion instead of the stock SFT checkpoint.

### Phase F1: Blend Base and SFT per layer, not per model

**Do**
1. Start with the individual Base and SFT models, then test uniform blends from 90% Base / 10% SFT to the reverse.
2. Move to different ratios for different parts of the model and refine through image tests. The workflow stores those layer-specific settings; it is not a single global blend percentage.
3. Judge by the failure each extreme has alone: SFT alone looks overly polished; Base alone lacks visual appeal. The blend keeps appeal without the polish.

**Check**
- Compare the same prompt across the blend sweep; the preferred blend is the one where the polished look recedes but appeal stays.

**Why**
A global blend percentage averages the two models' behaviour everywhere; per-layer ratios let the blend keep SFT's finish where it helps and Base's character where SFT would flatten it. The author is explicit that the preference is specific to this blend, not a general claim.

### Phase F2: Add the Guanlan LoRA at low strength

**Do**
1. Apply KOOK's Guanlan SFT LoRA after the blend, at strength 0.2.
2. Keep the separate switch that skips Guanlan while keeping the Base/SFT blend intact.

**Check**
- Higher weights smooth away more character texture than the author wants in this setup; 0.2 is the point where character texture survives.

**Why**
The LoRA is a seasoning, not the dish: at 0.2 it adds the SFT character the blend wants; higher, it erases the texture the blend was built to preserve.

### Phase F3: Pick a sampling route by what matters, speed or texture

**Do**
1. Everyday generation: Base 8-step DMD acceleration LoRA on, 8 steps, CFG 1, Euler with sgm_uniform.
2. More texture, longer wait: acceleration off, 50 steps, CFG 3, Euler with sgm_uniform.
3. The author tested two SFT acceleration variants and two Base variants before settling on this Base option.

**Check**
- The 50-step route retains more texture but takes roughly 4-5 times as long in the author's tests.
- The accelerated workflow, including upscaling, took about 90 seconds locally (7900XT) and 60 seconds on the online RTX 4090 setup.

**Why**
Steps buy texture, not just quality: 8 steps with the DMD LoRA is the daily driver, 50 steps is the texture route. The author warns the acceleration preference is specific to that LoRA and this blend, "rather than a claim that any acceleration LoRA will work equally well".

### Phase F4: Prompt through a multimodal chat model, then upscale with colour matching

**Do**
1. Give the prompt template to a capable multimodal chat model, send the request or reference image in that conversation, and paste the resulting prompt into ComfyUI.
2. The template handles short text requests, image-to-prompt reconstruction, and requests to change selected attributes. Instead of adding more adjectives, it asks for concrete composition, lighting, material, and typography decisions where relevant.
3. Keep internal PE (prompt enhancement) off when using an already-finished prompt. The built-in options are more convenient, but the author found the stronger external chat models more consistent.
4. Remember the limitation: on this route the chat model sees the reference image, but MOSS only receives the resulting text. It can regenerate a described scene; it does not directly edit the source pixels or guarantee the same face. To request a change, describe the complete target image, not just "change the clothes and keep everything else."
5. Optionally run native SeedVR2 upscaling targeting 8 megapixels (roughly 4K-class output, dimensions depending on aspect ratio). Keep LAB colour matching enabled; disabling colour matching introduced a yellow shift in the author's tests.

**Check**
- Commenter pushback, taken seriously by the author: Treeshark12 says "Prompt enhancing is pretty much always garbage" and the example images have "poor anatomical proportions" and "strange" limb proportions; the author replies by asking "What anomalies do you see in the image I've shown?" and repeats "Don't forget to enhance the prompts." The disagreement is unresolved in the thread: the author stands by prompt enhancement, a commenter calls it garbage and the anatomy poor.
- Another commenter (Riddy_93) reports downloading and using MOSS the day before: "the aesthetic looks better and realistic than Qwen 2.1".

**Why**
The prompt is doing the work the model cannot: MOSS receives text only, so the quality of the text is the quality ceiling. The anatomy criticism is the honest counterweight: no prompt template fixes a model's limb proportions. Upscaling without colour matching changes the image while enlarging it; LAB matching is the check that the bigger image is the same image.

### Tuned-fusion human method, distilled

1. Blend per layer, not globally; the setting lives in the workflow, not in one number.
2. LoRA at 0.2: enough to add character, low enough to keep texture.
3. Two sampling routes, chosen by the job: 8 steps/CFG 1 for everyday, 50 steps/CFG 3 for texture.
4. Prompt outside the tool: a multimodal chat model writes the prompt, ComfyUI runs it; MOSS only ever sees text.
5. Never ask for a partial edit in words; describe the complete target image.

## Expansion 2026-11-21: Olivio int8 + Ultimate SD Upscale (low-VRAM variant)

Source: "MOSS Image ROCKS! Fast, Uncensored & Under 6 GB – EASY Install Guide" by Olivio Sarikas, https://www.youtube.com/watch?v=amjhvE-h2kM (10:32, 10,996 views, uploaded 2026-11-20). Evidence: full ASR captions (252 segments) plus the description. This is a distinct workflow from the starter recipe and the tuned fusion: same model, a quantized generation-optimized workflow at 1-2 MP, then upscaling instead of generating big. Expansion 2026-11-22 (frame review, Phase G5 below): 12 frames from the downloaded video, read directly, supply the exact model filenames and sampler/upscale numbers the captions garbled or omitted; the caveat in the previous version of this section no longer applies.

### Phase G1: Pick the optimized workflow, not the base workflow

**Do**
1. Go to the official Comfy-Org MOSS-Image page: "the structure where everything goes with different workflows" (diffusion model, text encoder, VAE under Files and versions).
2. Download the workflow and drag it into ComfyUI; ComfyUI names the missing models and the folders they belong in (red frame, Details, Issues). "Click on download and point it to that folder inside of the ComfyUI folder inside of the models folder."
3. Use the generation-optimized workflow, not the base text-to-image workflow: "the base uses a base model that has not been optimized and is better for image training. The other one up here uses the model that is better optimized for your purposes for image generation."
4. Download the quantized model the workflow names into the folders the workflow points to. The exact filenames, read from the workflow's Missing Models dialog on screen (frame review, 2026-11-22; the ASR captions rendered the first name as "the int eight con rot" and are not quoted here): `moss_image_base_int8_convrot.safetensors` (diffusion model, "Download all (5.04 GB)"), `qwen3.5_9b_w4a8_gptq.safetensors` (CLIP/text encoder), `flux2-vae_small.safetensors` (VAE). The full HuggingFace MOSS-Image repo is 68.8 GB; the int8 workflow needs only the 5.04 GB diffusion-models set named here, not the whole repo.
5. "Always update ComfyUI and of course update your graphics driver" before starting.

**Check**
- The workflow opens naming its own missing files. If ComfyUI does not complain about a missing model, the files are in the right folders.

**Why**
The workflow is the install instructions: dragging it in surfaces exactly what is missing and where it goes, so there is nothing to guess about folders. The base-vs-optimized choice matters because the base checkpoint is for training, not for generation.

### Phase G2: Generate at 1-2 megapixels, with the prompt enhancer

**Do**
1. Write the prompt in the workflow, then click the prompt enhancer: "this will optimize the prompt for the use with Moss image. However, this will take some extra time."
2. Keep the resolution in the model's optimized band: "this model has been optimized for one to two megapixels. So unlike when 2.1 or MiniMax H3, this is not for 16 megapixels."
3. Use the recommended megapixel resolutions listed on the model page for the workflow you chose.

**Check**
- Judge the generated image at its native 1-2 MP size first, before upscaling: the author's portrait review praises the skin detail, round retinas, and soft lighting "already very good with the original image that is created without upscaling".

**Why**
Generating at the resolution the model was optimized for, then upscaling, is cheaper and safer than asking a 1-2 MP model for 16 MP directly. The prompt enhancer costs extra time per generation, so it is a choice, not a default the author forces.

### Phase G3: Adapt the workflow for Ultimate SD Upscale

**Do**
1. Install the Ultimate SD Upscale node: ComfyUI Manager, Extensions, search "ultimate", install "ComfyUI ultimate SD upscale".
2. Double-click the canvas background, search for the Ultimate SD Upscale node, place it where it is needed. It needs several inputs, "including an upscale model", so add a Load Upscale Model node too. Use the author's list of favorite upscale models "for the different purposes, might that be design or a photo with skin details".
3. Wire the subgraph: click the subgraph icon, and on the right side "there is a gray dot for the outs". Connect the model, the VAE, the positive prompt, and the negative prompt to the subgraph outputs, rename them positive/negative carefully ("make sure that you write the right one here so that the right one is connected"), click the return button, and connect the outputs to the matching inputs outside.
4. Drive the upscale size from the image itself: "use the get image size node, which is a base node that comes with ComfyUI and just connect the image and then connect this over here to the width and the height so that you automatically always get the same height as the original image."
5. Run at 2x upscale. Note the arithmetic the author states: "we are doing a two times upscale, this means it's creating four additional images, but if you have another ratio, it needs more images than that."

**Check**
- The adapted workflow produces the generated image and its upscale in one run, at the original image's height, with no manual resolution entry per image. The Get Image Size wiring is what makes that automatic.

**Why**
An upscaler subgraph with unwired outputs does nothing: the model, VAE, and both prompts must be passed through, or the upscale has no generation to refine. Deriving the size from the image removes the one number that would otherwise drift between the generate step and the upscale step.

### Phase G4: Review honestly, including the defects

**Do**
1. Review the test images: group portrait (face detail "more than actually from the MiniMax model"), mature-lady portrait, perfume advertisement ("very intense with the colors", reflection and foreground depth of field praised), chess/music poster (text "in the right positions and with a beautiful font" and "spelled correctly, exactly as I defined it"), character sheet (emotional expressions good; small faces "often not so great", rendered multiple times).
2. For small faces, "use a face fixer before you do the upscaling so that you get a way better quality with that and also, of course, correct face details."
3. Run the prompt-adherence test: red square on a shiny ball, seven apples side by side, a triangle behind a glass of water. "Most of that, to be honest, is correct... The only mistake it made is to place a triangle shape behind the glass of water, and you can see that this is a pyramid that's kind of floating in the air."
4. Note the hand defect plainly: "on one of the hands we actually have six fingers. Now because the model is so lightweight and renders pretty fast you actually could render it just another time."
5. Note the uncensored claim as the author's claim only: the model is "also uncensored, so I tried different prompts of the spicy variety, and yes, it actually got the anatomy right, also down to the details". No such image is shown or verified in the retrieved text.

**Check**
- Upscaled quality is judged against the two named rivals: "this rival[s] Qwen 2.1 or MiniMax H3 image model from the amazing details of a close-up portrait" (ASR rendering; the comparison is the author's judgment, not a measured benchmark).

**Why**
A fast, lightweight model changes the defect economics: a six-finger hand is a re-render, not a rescue job, because generation is cheap. That only holds if the defects are checked per image, which is why the review phase exists at all.

### Phase G5: Use the exact int8 sampler and upscale settings (frame-verified, 2026-11-22)

Source for this phase only: 12 frames extracted from the downloaded video (632 s, 21.8 MB) and read directly in the 2026-11-22 scout run (re-scan of the same video; no transcript was obtained in that run, and the 2026-11-21 ASR evidence is cited, not re-derived). Filename and value panels were enlarged and re-read before quoting. These settings belong to the int8 variant; do not borrow the starter recipe's 50 steps / CFG 3 / shift 5 for this variant, and do not borrow these settings for the starter recipe.

**Do**
1. Sampler settings on the load/sampler node: sampler `er_sde`, scheduler `simple`.
2. Resolution Selector: aspect ratio 1:1 (Square), 1.00 megapixels.
3. Ultimate SD Upscale node: upscale model `4x-UltraSharp.pth` via Load Upscale Model; `upscale_by` 2.00; steps 25; CFG 2.5; sampler `er_sde`; scheduler `simple`; denoise 0.20; mode type Linear; `mask_blur` 8; tile padding 32. The seed shown on screen (804984349185531) is the author's shown seed with "control after generate" set to randomize; it is recorded for completeness and is not a required value.
4. Frame evidence for outputs/defects in this run: group dinner portrait, violin-maker hands close-up, "VIENNA JAZZ NIGHTS" poster with legible text, prompt-adherence test (red cube on blue sphere, seven green apples, yellow pyramid behind a glass of water), and a distorted pink furry figure (garbled anatomy failure example). The six-finger hand defect reported 2026-11-21 was not isolated in this run's 12 frames and is not re-verified here.

**Check**
- The three filenames in Phase G1 step 4 match the workflow's Missing Models dialog exactly. If ComfyUI names different files, the workflow version differs and these filenames do not apply. The upscale settings are read from the on-screen node values; if the node shows different values, the on-screen values govern.

**Why**
Exact filenames remove the one guessing step the 2026-11-21 audit left open. Sampler/upscale numbers remove the second: the int8 variant now has stated settings of its own. ASR garbles filenames; the Missing Models dialog and node values are the source of truth for file and parameter names.

### Int8-upscale human method, distilled

1. The workflow names its own missing files; download exactly those.
2. Generate at the model's optimized resolution (1-2 MP); upscale after, do not generate big.
3. Wire the upscaler subgraph completely (model, VAE, both prompts) and derive its size from the image.
4. Re-render defects instead of rescuing them; fix small faces before upscaling, not after.
5. Review against named rivals and name the failures (six fingers, floating pyramid) in the same breath as the wins.

## Expansion 2026-11-25: Olivio MOSS Turbo LoRA (4-step SFT v2 + LoRA Manager)

Source: "MOSS TURBO - 4 Steps ONLY! Fast & Uncensored - EASY Install Guide" by Olivio Sarikas, https://www.youtube.com/watch?v=4gmEzsXOO6Q (17:13, 4,931 views at extraction, uploaded 2026-11-24). Evidence: full captions, 400 segments, plus the description. This expansion supplies the install, wiring, sampler settings, and defect profile for the 4/8-step Turbo LoRA that Phase 4 anticipated and Phase E3 used at draft level. It does not replace the int8 workflow above: the Turbo LoRA sits on top of the official MOSS workflow from the prerequisite video (https://www.youtube.com/watch?v=amjhvE-h2kM), and the author starts where that video left off.

### Phase H1: Install the LoRA Manager node pack

**Do**
1. In ComfyUI, open Extensions, search for LoRA Manager, and install the first one, "from Will Meow". If the Extensions window is absent, install the Node Manager first.
2. Restart ComfyUI so the new nodes load. An "L" icon appears; clicking it opens LoRA Manager in an extra tab showing the LoRAs already in your folders (use Refresh if it does not).

**Check**
- The L icon is present after restart and the manager lists existing LoRAs.

**Why**
The LoRA Manager pack supplies both the download UI and the LoRA Loader node used later. Without it, the official workflow has no place to attach a LoRA.

### Phase H2: Give LoRA Manager read-only API keys

**Do**
1. Open the manager's settings icon. Enter a Civitai API key and a Hugging Face access token.
2. Civitai: account icon, Account Settings, Security and Apps, API Key, permission preset Read Only, name it, Save, copy the key. Hugging Face: user icon, Access Tokens, Create New Token, Read Only, name it, Create Token, copy it over.

**Check**
- Both keys are read-only. The download step in Phase H3 is the functional check; the author states no separate verification step.

**Why**
Read-only keys can fetch models but cannot act on the account.

### Phase H3: Download the Turbo LoRA

**Do**
1. In LoRA Manager, click Download, paste the Civitai page address (https://civitai.red/models/3006599/moss-image-turbo-loras?modelVersionId=3414934), click Next, select the LoRA from the list shown, click Next to download. The chosen LoRA is MOSS_Image_SFT_4_steps_v2.
2. In the manager, click a LoRA and scroll down: example images show all settings used, including seed, prompt, and negative prompt, which can be sent to the workflow; the model description mirrors the Civitai page.

**Check**
- Example images carry their settings on mouse-over, so a working configuration can be copied rather than guessed.

**Why**
The example images are the settings documentation. Reading them replaces trial-and-error on steps, CFG, and prompts.

### Phase H4: Add a LoRA Loader node to the subgraph workflow

**Do**
1. Double-click the canvas background, search for LoRA Loader, and use the one labelled "LoRA Manager" in brackets. Place it inside the workflow. The official MOSS workflow is presented as a subgraph block; the captions describe it as simplified so the "noodle mess" is hidden.
2. The loader initially has no in/out because it sits in a subgraph. Click the subgraph icon to see the full workflow.
3. Expose outputs: drag from the model output's grey dot to create a Model output, and from the CLIP output to create a CLIP output. Then create inputs the same way: drag from the grey dots to the KSampler's model input, and to the CLIP inputs of the positive and negative prompt nodes, so the untouched model and CLIP go out, through the LoRA, and back into the subgraph.
4. Optional trigger words: double-click the background, add a Concatenate Text node OUTSIDE the subgraph box, put the existing prompt string into input A, and drag the LoRA's trigger-word output into string B, then send the result into the positive prompt. Placing it outside matters: if the prompt-enhancer box is disabled, a node inside it would be disabled too, but the trigger words must survive.
5. Return via the return icon to the original workflow view. Connect model to model, CLIP to CLIP, and the trigger-word string to string B on the lower part of the subgraph node.
6. Back in LoRA Manager, click the paper-plane icon to add the LoRA to the active workflow. The blue button toggles it on/off; set strength to taste (the author usually leaves it at 1, and notes LoRAs can be mixed for different styles/enhancements).

**Check**
- The loader appears in the workflow after the paper-plane click, with the model and CLIP routed through it and the trigger-word string connected.

**Why**
The subgraph hides wiring, so inputs and outputs must be created explicitly before anything can pass through the LoRA. Keeping the trigger-word concatenation outside the enhancer box preserves trigger words when the enhancer is bypassed.

### Phase H5: Set the turbo sampler settings

**Do**
1. Steps: 4 to 8. The author sets 8, "because I think usually it gives you better results". Rule of thumb stated: 4 steps should be enough at 1 megapixel; use 8 steps at 2 megapixels.
2. CFG: 1.
3. Sampler: Euler (captions render the name as "Uler"; read as the Euler sampler). The rest stays the same as the original workflow.
4. Model precision: the author uses the INT8 model, under 6 GB. The original LoRA suggests the BF16 model, almost 10 GB, which may not fit. The author reports no quality difference seen from INT8 in his tests.

**Check**
- At 1 MP, 4 steps; at 2 MP, 8 steps. If the image is a close-up with wrinkly skin, see Phase H6 before accepting the result.

**Why**
A step-distilled LoRA changes the sampler contract: the 25-to-50-step settings of the base workflow no longer apply. CFG 1 and few steps are part of the LoRA's design, not a speed shortcut applied on top of it.

### Phase H6: Judge the LoRA by its defects

**Do**
1. Expect plasticky skin on close-ups with wrinkly skin, in both BF16 and INT8. For close-ups, run without the speed LoRA at 25 steps for the better quality, remembering to set CFG and sampler back.
2. Expect extra fingers or extra limbs sometimes; render multiple times until a clean result appears.
3. Expect a checkerboard pattern in backgrounds (the example: holes in a tree behind a grey-haired man). Expect the model to stay strong on 3D/comic/artistic styles, character sheets, emotional expressions, text rendering, and prompt adherence (7 green apples in a row; a matte red square on a shiny blue ball, though the ball was not completely round), and weaker on photorealism.
4. Use the prompt wording "an amateur smartphone photo", and optionally a little blur with the blur location defined, to make photoreal results more realistic. Use the extensive negative prompt visible on the LoRA's sample images in LoRA Manager as a learning source.
5. Note the prompt enhancer trade-off: on, it optimises the prompt through an LLM model and can help results but slows the process; off, it is bypassed at the back, while trigger words still apply because of the Phase H4 placement.

**Check**
- Close-up skin, hands/fingers, and background trees are the three defect checks. A clean result is confirmed by re-rendering, not by adjusting settings after the fact.

**Why**
The LoRA's speed is real, but its defect profile is fixed: wrinkly skin, extra limbs, and checkerboard backgrounds do not improve with more steps inside the turbo settings. The author's stated rule is to switch the LoRA off for close-ups rather than fight the defect.

### Turbo LoRA human method, distilled

1. Install the node pack that owns the workflow change (LoRA Manager), before touching the workflow.
2. Copy settings from example images; do not guess steps or CFG for a distilled LoRA.
3. Wire trigger words outside any box that can be disabled.
4. Set steps by megapixels (4 at 1 MP, 8 at 2 MP), CFG 1, Euler.
5. Judge a speed LoRA by its defects (plasticky skin, extra limbs, checkerboard), and fall back to the 25-step base run for close-ups.

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
