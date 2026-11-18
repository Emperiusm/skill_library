---
name: fibo-2-comfyui-json-prompts
description: "Run FIBO 2 (Bria AI, JSON-prompt trained, ~1 MP) in ComfyUI with Pixaroma nodes: a helper model writes readable structured JSON from a short idea, Turbo 4-step vs Dev 50-step, single-change edits, and box/brush inpainting via Inpaint Crop/Stitch. Trigger when an image edit needs an auditable prompt, or when choosing between FIBO 2 and MiniMax H3 Image."
---

# FIBO 2 in ComfyUI: JSON Prompts You Can Read

## Purpose

This skill reconstructs the exact workflow pixaromadesign demonstrates for FIBO 2 in Episode 43, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: never write the JSON yourself; let a helper model write it from a short idea, read what it wrote, and fix the words before you run.

## Source

Creator: pixaromadesign. Video: "MiniMax H3 Image and FIBO 2 in ComfyUI | 14 Free Workflows (Ep43)" https://youtu.be/ep5TQQGtHcI (21:47, uploaded 2026-11-17, 15,723 views; full auto-captions, 663 cues, read in full; 12 frames from the downloaded media reviewed) | r/comfyui post 1xyogw8 (score 85, 7 comments) | 2026-11-18 scout run, audit 6. The FIBO 2 half of the episode; the H3 Image half is covered by skill `minimax-h3-image-native-comfyui` (Expansion 2026-11-18). Workflows free from the video description.

## Tools used

ComfyUI 0.45+ (Pixaroma nodes, latest), FIBO 2 by Bria AI (trained on long structured JSON prompts), Pixaroma AI Prompt nodes, Sketch Pixaroma, Inpaint Crop, Inpaint Stitch. Comparison models from older episodes: Krea 2 (Ep24), MOSS (Ep40), P-H3 LoRA (Ep42), FLUX 3 Klein (Ep39), Qwen Image 2.1 (Ep36).

## Phase 1: Install the four files

**Do**
1. You need four files for FIBO 2 (the Download Models note has a button for each). The model goes into a new folder called `fibo2` inside diffusion models.
2. Then the text encoders: the first for the model itself, the other is the JSON helper.
3. The VAE is the same file as in the FLUX 2 workflows, so you may have it already.
4. Download the workflows from the description: two model folders plus a Media Inputs folder with the images used in the video. Copy those images into the ComfyUI input folder so every workflow opens with its image in place. The blue nodes with a number are the ones you change; leave the rest.

**Check**
- The `fibo2` folder exists inside diffusion models with the model in it; the JSON helper encoder is present, not just the model encoder.

**Why**
The helper is a separate file from the model: without it, there is no JSON writing, and FIBO 2's whole control surface is the JSON. The folder name matters because the workflows point at it.

## Phase 2: Generate with Turbo, finish with Dev

**Do**
1. Write one line in AI Prompt Pixaroma: who it is, what they do, where they are, what the light is like. The author's example idea: a close-up portrait of a smiling woman who pours maple syrup on a stack of pancakes, with a white mug that says Pixa beside the plate. The word for the mug goes in double quotes.
2. The helper writes the JSON first (a list with every object, the light, the camera, and the words in the image, following Bria's published open toolkit), and you can read it in the box under your idea. The helper takes 15-20 seconds; when you change only the seed, it does not write again.
3. Size: five buttons, all about 1 megapixel; what you choose is the aspect ratio (the author uses 3:4 vertical). Seed: F repeats the same image, R gives a new image with every run.
4. Turbo model: the image itself is ready in about 2 seconds. Dev model (one more file in the same folder): 50 steps instead of 4, over 20 seconds per image, genuinely different images per run (new pose, new kitchen), finer small details. Use Turbo to try ideas, Dev when an idea works.

**Check**
- Read the helper's JSON when a detail matters. A tester on Discord got a bottle with its cork still in while the syrup poured right through it. When the author added just the words "open bottle", the helper wrote "a cork stopper, partially open", and the cork stayed in all four images. The fix was longer words ("an uncapped open glass bottle with the lid removed"), and the cork was gone in all four.
- Turbo changes very little with a new seed; for a different image, change a few words in the idea.
- Busy scenes are harder: a wide flower shop gave a vase floating in the air and legs too short for the body. Keep the subject close and the room calm.

**Why**
The JSON is the control surface: a readable, editable prompt the helper writes and you audit. Short helper inputs leave the helper guessing, and the helper guesses wrong in visible ways (corks, floating vases). Longer, more specific words in the idea are cheaper than re-running.

## Phase 3: Change one thing at a time

**Do**
1. Generate the image first, like before. Then a second AI Prompt node looks at that image and at your change, and writes an edit JSON, so the model changes only that part.
2. Leave the seed on F so the first image stays the same while you try changes. Make a single change at a time ("change the pancakes to waffles"), so you can see what it did. Do not add words like "keep everything else the same", because then the model can generate the whole frame again.
3. A new change takes over 25 seconds, because the first image is not generated again. The same edit mode works on your own image: the author asks for a white t-shirt with small orange "Pixa" letters on a woman in a mustard t-shirt; the changed image is ready about 4 seconds after the helper finishes, and her face, hair, and the wall behind her stay the same. The word "small" is there for a reason: on the first try the letters were so big the image edge cut them.
4. Removal rule: on the terrace image, "remove the window and its shutters" alone gave a dark hole in one result and deleted the blue door next to it in another. With the full sentence ("so the plain white wall continues in their place"), the wall was clean in all four images and the door stayed. Say what is there instead.

**Check**
- Drag across Image Compare: only the pancakes are different. If more changed, a "keep everything else" phrase or a re-rolled seed is the cause.

**Why**
One change with a fixed seed is attributable: you know what the edit did because nothing else moved. "Keep everything else the same" is a request for the model to regenerate the frame, which is the opposite of an edit.

## Phase 4: Combine images, and mind the back view

**Do**
1. Load two images on purpose: the person in the first loader, the jacket in the second. Write a short sentence that names both images with the tags "image 1" and "image 2" (a different tag from H3 Image's "Picture 1"). The helper looks at both images before writing the JSON.
2. Run it: the author tried the red dress with a leather jacket; she wore the jacket the right way, both arms inside the sleeves. The result is about 1 MP, much smaller than H3 Image.
3. Rear-view trap: a Discord tester found a man seen from behind got the front of the jacket on his back, with the zipper and pockets, in all four images. Fix (the tester's words, adopted by the author): describe the back in the sentence ("the jacket is shown strictly from the back view, with a solid leather back panel and no zipper or front pockets visible"). With her words, FIBO 2 gave the back of the jacket in all four, though a seam runs down the middle on each and grey hoods cover the collar in three.

**Check**
- When the person is seen from behind, describe the back of the garment in the sentence. If the front appears on the back, the sentence did not say "back" clearly enough.

**Why**
The helper writes what the sentence says, and a sentence that does not say "back" leaves the model to guess the side. The tester's fix is a sentence fix, not a model fix: name the view explicitly.

## Phase 5: Inpaint a box or a brush stroke, and name only what is inside

**Do**
1. The model has no mask input, so the workflow does the masking around it. Draw a box on Sketch Pixaroma; the box becomes a mask. Inpaint Crop cuts out that area with some of the image around it and makes it bigger; the model changes only that piece; Inpaint Stitch pastes it back with a soft edge.
2. Name only what is inside the box. A prompt that named the armchair and the plant outside the box made the model paint a second armchair and a plant on the wall, inside the box.
3. Brush method: Inpaint Crop "Open mask editor", paint over the thing (window, both shutters, ledge above it), save. Paint a little more than the thing itself, because only the painted part goes back into the image. A painted mask is saved on the computer, not inside the workflow file, so always paint the mask first.
4. Without a mask, the whole image goes through the model and comes back changed.

**Check**
- Away from the box, the image did not change at all, and it kept its own size: this is how you edit an image bigger than 1 MP.
- Frames reviewed: frame 8 shows the FIBO 2 box-inpaint graph with the red Sketch Pixaroma box around the armchair and the Inpaint Crop/Stitch chain.

**Why**
The mask is the edit boundary: what you name outside it still gets painted inside it, because the model only sees the cropped piece. Painting a little extra is the seam budget: the painted part is what returns, so an exact outline leaves a hard edge.

## Phase 6: Compare honestly, then pick by the job

**Do**
1. Same three scenes on five models, each in its own episode's workflow, four images each, best of four shown: Krea 2 (Ep24), MOSS (Ep40), P-H3 LoRA (Ep42), H3 Image, FIBO 2. Every model wrote "Pixa" and "Bakery" on the apron and "Fresh Bread" on the board; FIBO 2 framed the baker wider and she holds the hot tray with bare hands where the others gave her cloths; all got the hat, backpack, and map on the jungle bunny; all spelled the perfume ad right (Krea 2 put the title on two lines; FIBO 2 cut the bottle like a gem).
2. Editing comparison, five models: H3 Image, FIBO 2, P-H3 LoRA (Ep42), FLUX 3 Klein (Ep39), Qwen Image 2.1 (Ep36). Red dress to a snowy street: every model kept her pose and the red dress; H3 Image and FIBO 2 added big snowflakes. Bunny explorer to a sunny jungle: P-H3 LoRA turned the bunny to face front and made it smaller; the others kept it turned a little to the side. Balloon letters "love" to "Pixa": every model spelled it right.
3. Know the limits. FIBO 2 stays at about 1 MP, so small far-away figures come out soft; busy scenes float things; a jacket can end up the wrong way around; the helpers make things up. H3 Image makes bigger images (4K) and has the better license for the author.

**Check**
- Read what the helper wrote, generate a few images, and look at them at full size: "you can easily miss small mistakes in a preview."

**Why**
A comparison in each model's own workflow with the same prompts is the only honest ranking. The author's verdict: "For me, FIBO 2 was easier to work with, but because of the license I probably cannot use it much, so I will stick with other edit models." License, not quality, is the reason to pass.

## License

FIBO 2 is free for personal and non-commercial use only. Commercial use needs a license from Bria (pricing link in the video description). H3 Image has a better license for the author, though some countries (including ones in Europe) need a separate MiniMax license first.

## The human method, distilled

1. Read the JSON the helper wrote before running: invented details are visible there.
2. One change at a time, seed on F, so each change is attributable.
3. Say what goes in the removed thing's place; deletions fail, replacements work.
4. Name only what is inside the box; describe the back explicitly for rear views.
5. Judge at full size; previews hide the small mistakes.

**Depth status:** FULL (full auto-captions, 663 cues, read in full; 12 frames from the downloaded media reviewed; full post text + 7 comments). The model itself was not run, and no generation beyond the quoted settings is claimed.
