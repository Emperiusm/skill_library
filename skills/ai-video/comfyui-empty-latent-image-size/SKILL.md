---
name: comfyui-empty-latent-image-size
description: "Set image size in ComfyUI the way the model actually reads it: the empty latent node sets width, height, and batch; the sampler only fills the grid. Steps of 8 vs 16, why 1080 becomes 1088, why the same seed gives a new image at a new size, and when batching saves time. Trigger when an image comes out the wrong size, a seed stops reproducing, or a batch is slower than separate runs."
---

# ComfyUI image size: the empty latent sets it

## Purpose

This skill reconstructs the exact workflow pixaroma demonstrates in "ComfyUI Image Size Explained: Empty Latent Image, Aspect Ratio and Batch Size", step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: the image size is set by the empty latent, not by the sampler, so choose the size first, then hunt for a seed you like.

## Source

Creator: pixaroma

Source: https://youtu.be/J3acw3v1tGk | r/comfyui post 1xomh5m (score 25, 2 comments) | YouTube, 683 s | full auto-captions retrieved via yt-dlp (9,029 chars) + media downloaded + 12 frames extracted, 2 reviewed (VAE decode comparison, node-search menu)

Practice + Finished workflows (free, no account): https://workflows.pixaroma.com/comfyui-nodes-explained/3/

Depth: FULL — full auto-captions, exact parameters, numbers, and quoted principles throughout; two frames reviewed.

## Tools used

ComfyUI, Empty Latent Image node, Empty SD3 Latent Image node, Z-Image Turbo, KSampler, VAE Decode, Resolution Pixaroma node.

## Phase 1: Understand what a latent is (the "A Deeper Look" chapters)

**Do**
1. Know the chain: Empty Latent -> KSampler (fills the grid from the seed, step by step) -> VAE Decode (unpacks the latent into pixels).
2. Know the packing: VAE packs each 8x8 pixel square into one cell with 16 numbers. A 1024x1024 image becomes a 128x128 cell grid, about 260,000 numbers, 12 times fewer than pixels.
3. An empty latent is the same grid with all numbers zero; decoded, it is a solid gray image.

**Check**
- The video packs a panda with a real VAE (Z-Image) and shows it as 16 layers, one panda per layer, each storing a different piece of information. VAE decode unpacks it back; up close the face looks the same, and "on average, each pixel changed by less than 1%" (author).
- Frame reviewed: the "PACKED + UNPACKED vs ORIGINAL" comparison is on screen.

**Why**
- The model works on the packed form, so the size of the grid (width/8, height/8) is the size of the image. Only the empty latent's size matters.

## Phase 2: Size first, then seed

**Do**
1. Set width and height on the empty latent node (e.g. 1024x1024, then 512x512).
2. Run. The 512 image is not the same panda smaller: when the size changes, the initial noise changes, so the same seed gives a new image.

**Check**
- Compare the two outputs: different image, not a resize.

**Why**
- The author's rule, stated twice: "first choose a size, and then look for a [seed] that you like." Hunting a seed at the wrong size wastes the search.

## Phase 3: Bigger costs more than linearly (but less than the fragment math suggests)

**Do**
1. Try 2048x2048 on the same prompt: much more fine detail in fur and eyes, 4x the pixels, and "it took five times as long on my video card" (author).
2. Z-Image handled every size tried, from 512 to 2048.

**Check**
- The author's habit: try ideas at regular size and only enlarge favorites, because generating each attempt in bulk at 2048 is "much faster" avoided.

**Why**
- Fragments interact pairwise, so doubling the size to 2048 makes ~16,000 fragments and 16x the fragment pairs, but "not all work grows so quickly," so measured time was 5x, not 16x. (Author's explanation; the 5x is measured, the 16x pairs is the model.)

## Phase 4: The 1080 -> 1088 rounding (steps of 16 vs 8)

**Do**
1. Enter 1080 in the height field of the Empty SD3 Latent Image node. Press Enter: it changes to 1088. The SD3 node only accepts sizes in increments of 16, so it rounds to the nearest.
2. The older Empty Latent Image node works with a step of 8, so it stores 1080. "Eight extra pixels is not a problem. Your image will just be a little taller."

**Check**
- The rule behind 16: one latent cell spans 8x8 pixels, and Z-Image cuts the latent into 2x2-cell pieces, so each slice covers a 16x16 pixel square. At 1024 that is 64 fragments wide and 64 high, 4,096 fragments. 1088 is exactly 68 fragments. Any size must correspond to whole fragments.
- The old node's 1080 is 135 rows of cells, so the last fragment row is only half filled; ComfyUI fills it with a copy of the top row and then cuts off the excess, which is why you still get exactly 1080.

**Why**
- Steps of 16 are not a mandatory rule; "they simply allow the size to fit the parts of the model exactly." Sizes that fit the model's fragments work best.

## Phase 5: Aspect ratio (the model recomposes, it does not stretch)

**Do**
1. Enter 832 width and 1216 height for a vertical phone-screen image; run. Same pixel count as a square, so about the same time.
2. Wide format works the same way (1216x832).
3. Do not go too far: at 2048x512, "the panda no longer fits, and its body is cut off."

**Check**
- The model does not stretch the image; "she recomposes the entire scene into a new form" (author, auto-caption wording).

**Why**
- Shape is the ratio of width to height; the model re-lays-out the scene for the shape, so extreme ratios lose the subject instead of squeezing it.

## Phase 6: Batch size

**Do**
1. Enter 4 in the batch size field and run: four different pandas, all from the same seed. Save Image shows all four and saves each as a separate file.
2. Re-running with the same seed gives the same four images.

**Check**
- At the video's size, four images took "almost as long to create as four separate runs, so the [batch] saved almost no time." With smaller images (512), the batch "worked almost twice as fast because the video card had free resources."
- A larger batch also requires more video card memory, "so start with a small number" (author).

**Why**
- Batching parallelizes only when the GPU has free resources; at large sizes there is nothing free to use.

## Phase 7: Which empty latent node to use

**Do**
1. Double-click the canvas and search "empty latent." The menu lists: Empty Latent Image (original, for older models like SD 1.5 and SDXL), Empty SD3 Latent Image (for models such as Z-Image), and per-model variants (Flux 2 has its own; the reviewed frame also lists Empty Hunyuan Video 1.0 Latent, Empty LTXV Latent Video, Empty Ace Step 1.0 Latent Audio, Empty Stable Cascade Latent Image).
2. With an empty latent node and a KSampler, the choice does not matter: ComfyUI adapts the blank canvas to the model before drawing. The author compared Empty Latent Image to the SD3 version on Z-Image and "the images were identical, pixel for pixel."
3. The real difference is the size step: 8 or 16.
4. Two exceptions: video models need their own latent node because video has frames; and some samplers from other node packages do not adapt the size, so on Flux 2 the image can come out twice as large. "So, keep the one that was in your workflow and everything will be fine."

**Check**
- Frame reviewed: the node-search menu on screen matches the transcript's list.

**Why**
- The node is a blank canvas; the sampler and model decide what the canvas means. Only the step size and the two exceptions change the outcome.

## Phase 8: The easier way (Resolution Pixaroma)

**Do**
1. Use the Resolution Pixaroma node instead of entering dimensions manually: choose a shape (e.g. 16:9), select a size from the list. Every size in the list is already a multiple of 16, so nothing is rounded.
2. Its latent output goes directly to the KSampler instead of an empty latent. The batch field next to it sets how many images you get.
3. If you do not have Pixaroma nodes, the install link is in the video description.

**Check**
- Run: a wide image, ready for thumbnail or video.

**Why**
- Manual dimension entry is where the rounding mistakes happen; a list of pre-validated sizes removes the mistake class.

## Phase 9: Practice (the workflows)

**Do**
1. Open the Practice workflow from https://workflows.pixaroma.com/comfyui-nodes-explained/3/ (drag into ComfyUI). Notes on the canvas give tasks: (1) the empty latent is not connected, so drag its latent output into the KSampler's latent input and run; (2) make a vertical image; (3) try 1080; (4) make a batch of four; (5) save with Ctrl+S.
2. Compare against the Finished workflow, which shows every answer.

**Check**
- The Finished workflow is the answer key; the Practice workflow is the exercise.

**Why**
- The video is built as a lesson with an answer key, not just a demonstration.

## The human method, distilled

1. **Size first, then seed.** The same seed at a new size is a new image.
2. **Try small, enlarge favorites.** 2048 costs 5x the time for 4x the pixels.
3. **Fit the model's fragments.** Steps of 16 on the SD3 node exist so sizes land on whole 16x16 fragments; 1080 -> 1088 is rounding, not a bug.
4. **The model recomposes, never stretches.** Extreme aspect ratios cut the subject off.
5. **Batch only when the GPU has room.** At large sizes a batch of 4 saves almost no time; at 512 it nearly doubles speed.
6. **Any empty latent works with KSampler.** The step size (8 vs 16) is the real difference; keep the node that came with the workflow.

## Commenter additions (not in the video)

- Author (pixaromadesign): Z-Image handled every size tried, 512 to 2048, but older models like SD 1.5 and SDXL "do better close to the size they were trained on." Upscaling is not in this video; Ep05 covers it (simple upscaling with and without a model, SeedVR2, workflows that upscale then run a second KSampler pass over the finished image, after VAE Decode): https://workflows.pixaroma.com/ep/5/.
- Commenter Anro5753: since sizes snap to multiples of 16, "picking resolutions near the model's trained pixel budget (not just a big number) tends to matter more than raw size."

## Failure modes

- **Same seed, different size, different image.** Not a bug: the initial noise changes with size. Pick the size before hunting the seed.
- **1080 becomes 1088 on the SD3 node.** Rounding to the nearest multiple of 16. Use the old node (step 8) if you need exactly 1080, or the Resolution Pixaroma node for pre-validated sizes.
- **Batch of 4 at large size saves almost no time.** The GPU has no free resources at 2048; batch at 512 if you want the speedup, and watch VRAM.
- **Flux 2 with a foreign sampler can double the image size.** Some third-party samplers do not adapt the latent size. Keep the node that came with the workflow.
- **Extreme aspect ratios cut the subject.** 2048x512 lost the panda's body; the model recomposes instead of stretching.

**Depth status:** FULL (full auto-captions + media downloaded + 12 frames extracted, 2 reviewed; exact parameters, numbers, and quoted principles throughout).
