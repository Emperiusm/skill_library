---
name: minimax-h3-v2v-masterclass-comfyui
description: "Edit video with MiniMax H3 video-to-video in ComfyUI: 56-frame temporal windows with carry overlap, sync spatial tiles, SAM 3 masked-latent inpainting with MVE cropping, latent save/load crash recovery, two-batch splits for over-long videos, and the prompt rule that the original video drives animation. Trigger when an H3 video edit must hold motion and look across the whole clip."
---

# MiniMax H3 V2V Masterclass

## Purpose

This skill reconstructs the exact workflow mo_akkakk demonstrates in the MiniMax H3 V2V Masterclass, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: never generate a whole video at once; split it into temporal windows and spatial tiles, keep the original video as the animation driver, and only denoise what actually changes.

## Source

Creator: mo_akkakk (No-Property3068). Post: "MiniMax-H3 V2V Masterclass is finally here!" https://www.reddit.com/r/comfyui/comments/1xxtvn6/ (score 79, 4 comments) | Tutorial: "MiniMax H3 V2V Masterclass" https://youtu.be/_lVzzLr9aC4 (45:42, uploaded 2026-11-16, 1,100 views; full auto-captions, 1,001 cues, read in full) | Workflows: https://www.patreon.com/mo_akkakk/posts/minimax-h3-v2v-175444714 (Patreon) | 2026-11-18 scout run, audit 7. Distinct from skill `minimax-h3-synctile-long-video` (single-trajectory blend) and from the H3 image skills: this is windowed video-to-video generation, not image work.

## Tools used

MiniMax H3 (first-to-last video/audio model, 8-step LoRA), ComfyUI native MiniMax H3 nodes, the author's temporal-window + spatial-tiles custom node, SAM 3 (native ComfyUI), MVE custom crop nodes, FLUX 3 (reference-frame edits), MiniMax H3 latent upscaler, NVIDIA Regenerate LoRA + sharpening LoRA, Ripple edit + Add Guide nodes, Ultimate Upscale custom nodes.

## Phase 1: Set up the base V2V workflow

**Do**
1. Load the clip into the first-to-last video/audio model. Add the low-VRAM subgroup: low VRAM attention node, Config Kitchen attention node, sparse attention, and a node that reserves 2 GB of VRAM so the workflow does not crash during decoding or while getting the final result.
2. Make the reference frame by editing the first frame in FLUX 3 (author's example: sunny environment replaced with snowy).
3. Extend frames: round the frame count up to a number MiniMax accepts (author's example: 353 frames becomes 362; the 9 extra frames are the last frame held 9 times). Resize the reference image and the video to the generation resolution (author generates at 1 MP; 2 MP for HD, 0.5 MP to test quicker). Width and height must be multiples of 64.
4. Feed the reference node: the prompt, the video/audio, the reference image as reference image and as first-frame guide (frame index 0; bypass it if the reference is not the first frame). Feed the resized video as reference video 0, scaled by half so the calculation is faster: the reference node does not accept video references above 1 MP, and halving still keeps most details.
5. Sample with the 8-step LoRA, sampler Euler SDE, scheduler linear quadratic, 8 steps.
6. Add a clean-VRAM node after generation so decoding does not crash. Save the video and audio latents to the output `latent` folder (video 001, audio 001, and so on) so a decode crash does not cost a re-run: copy the saved latents from the output folder into the input folder, press R to refresh, and load them with Load Latent / Load Audio nodes.

**Check**
- Compare the first frame of the video with the reference frame after resizing: nothing should shift.
- Build a difference map (merge with difference, subtract the result from the original video): it shows inconsistencies. The author's result: "very very minimal shifts", "very loyal to the original video", hair and necklace movement intact.
- The save-latent trick has a catch the author states plainly: latents saved by the node will not appear in the Load Latent dropdown until copied from the output folder to the input folder and refreshed.

**Why**
Frame-count rounding and 64-multiples are the model's grid: off-grid inputs get truncated or padded. The reference video at half resolution is the speed trade: the node caps references at 1 MP anyway, so full resolution in is wasted compute. Saved latents are crash insurance: a decode crash after a long generation is the most expensive failure, and the recovery is a file copy.

## Phase 2: Split long videos into temporal windows (and spatial tiles when needed)

**Do**
1. Use the author's node to split generation into windows and tiles. Windows: generate 56 frames at a time, then the next 56, until the final length. Overlap frames: how many frames the node takes from the previous window and overlaps with the new one. Carry overlap: how many frames (author uses 5) are taken as a guide for the next window.
2. Turn on short final window when window frames are high (author's example: 107-frame windows with minimum final window 56): if only 5 frames are left, the node generates a minimum window that fits the model numbers instead of re-generating 107 frames.
3. Spatial tiles: split the frame into tiles horizontally and vertically with a chosen tile size and tile overlap. The author did not use tiles at 1 MP ("it didn't feel like I need to separate anything"); use them at Full HD or above. Tile mode: the node started with blended, then the author's own tile mode, then sync. Leave it at sync: "sync gives the best result" (documentation on GitHub for the rest).
4. Colour match tries to match colours between tiles to eliminate visible seams. Bleed scale relates to the blade/VE inputs below.
5. Feed the blade (detail) and VE (video) inputs when tiling: the reference node caps video at 1 MP and scales larger video down, so feeding the tiled original video per tile lets the generation see the full detail of the original. Bleed scale default 1 is full resolution per tile (heavy); scale down to 0.5 or 0.25 and it still keeps more detail than without blade/VE. Crop image per tile: leave on when the reference image is the first frame of the generation (each tile sees only its part); switch off for a character sheet or style sheet, where every tile must see the full reference.
6. Drift limits, measured by the author: generation starts to shift after 192 frames at 0.5 MP and after about 147 frames at 1 MP; at 56 and 73 frames in Full HD there were no shifts. Keep window frames low (56) and overlap 5, "even in fast-moving videos", and generate in high resolution from the first stage rather than upscaling later.

**Check**
- If generation is slow and animation drifts from the original, the video was generated in too few, too long windows: split smaller.
- If seams appear between tiles, colour match and bleed scale are the controls; if VRAM overflows, tiles are the cost.

**Why**
A whole video at once is slow and drifts; windows bound the drift to one window, and the carry-overlap frames are the stitch. Tiles bound the resolution: each tile is a small generation, so Full HD fits in VRAM. Sync mode is best because tiles generate in step, not one after another, so they agree with each other.

## Phase 3: Inpaint a character (or remove one) with a masked latent

**Do**
1. Create the mask for the person with SAM 3 (native ComfyUI) or any other software. Grow it a little with Grow Mask with Blur: the replacement character may have fluffier hair and need more space around the head; blurring the mask edges helps blending (a harsh edge shows after stitching).
2. Crop with the MVE custom nodes: crop the mask, the video, and the reference image with the same settings. Crop scale default 1 crops exactly around the mask; the author uses 1.25 for context around the mask. Divide-by makes sure cropped sizes accept multiplication by 64. Upscale megapixel default 0 keeps the cropped resolution; use a positive number to upscale a small crop to 1 or 2 MP, or a negative number to shrink a too-big crop.
3. Preview the cropped mask + cropped image together to confirm they match, then build the masked latent: combine the cropped video with the cropped mask (mask pre-processed by the mask-latent node) so only the masked area is denoised. Feed the masked latent to the sampler instead of the reference node's latent.
4. Stitch the generated area back with feathering between generated and original video.
5. Trim the padding back: Get Image From Batch removes the extra 9 held frames (keeps the original frame count); a resize node crops the extra pixels added for the 64-multiple rounding back to the original width and height.
6. For removal instead of replacement: feed the reference node the cropped mask-on-video (the white area) instead of the cropped video, and write the prompt to say what is behind the white area (for example, a field). If the reference video still contains the person being removed, the model gets confused.

**Check**
- The replacement keeps the original's micro-expressions and necklace movement; the author says inpainting is "even more consistent than the previous workflow because when you are only generating part of the video, it is always a better approach. It can maintain your original details even more."
- The same masking workflow works without cropping if the mask was made outside ComfyUI (Photoshop, Premiere, Nuke): use the plain inpainting workflow instead of the cropping one.

**Why**
Only denoising the masked area is the strongest consistency guarantee in the video: everything unmasked is the original pixels, not a regeneration. The crop exists to make the masked area big enough to generate well (1 MP) without generating the whole frame. The blur on the mask is the seam budget: soft edges stitch invisibly, hard edges do not.

## Phase 4: Upscale, split long videos, and know when not to

**Do**
1. Latent upscaler workflow (author's verdict: disliked): downscale the generated video to 0.5 MP, multiply resolution by 2 (author tested 4.5x), feed the original video as the reference to retrieve details from (not the generated video, which would match its own flaws), add the NVIDIA Regenerate LoRA and a sharpening LoRA, and run the temporal-window + spatial-tiles node again. The author reports "micro boiling" in the results even with the NVIDIA LoRA, and prefers generating in higher resolution from the first stage. Ultimate Upscale custom nodes do the same temporal/spatial split and can replace the author's node entirely; use a dual-video compare node to check before/after.
2. Two-batch workflow for videos longer than MiniMax's maximum frames in a single run: split the length into two batches, generate batch 1, take overlap frames (the rounding remainder, minimum 5) into batch 2, generate, then stitch with the author's node and combine audio from both batches.
3. Two-stage workflows (same three workflows with a second upscaling stage) are provided for those who prefer them.
4. Ripple edit workflow: a trained Ripple LoRA plus Ripple custom nodes; load the video with size/length matching inside the node, create first/last frame references inside the node, feed the Ripple output to the output node, and write the prompt (part of it is fixed by the LoRA's training and cannot be changed). The author's own rebuild uses Add Guide nodes instead: guide 0 is the full video, guide 1 is the reference frame (both frame index 0), the Ripple LoRA is added before the 8-step LoRA, and an empty MiniMax latent feeds the Add Guide node. Add Guide is not constrained to 1 MP like the reference node, but it makes generation heavier. Results were mixed: sometimes nice, sometimes the author's own workflow was preferred.
5. Image edit workflows (FLUX 3 x2, FIBO 2 x2, MiniMax Image x2): one general edit on the whole image, one masked-area edit stitched back onto the original.

**Check**
- The upscaler check is micro-boiling: if the upscaled video boils, the upscaler added it; generate at target resolution instead.
- The two-batch check is the stitch: the overlap frames (minimum 5) are what join the batches without a jump.

**Why**
Upscaling a generation re-generates its flaws at higher resolution; generating at resolution avoids the second pass entirely. The two-batch split is the same windows idea at the video level: overlap is the seam budget at every scale.

## Phase 5: Write the prompt so the original video drives the animation

**Do**
1. The author's prompt for the snowy result: "video one stays the same but with snowy weather, cloudy sky and ambient lighting that matches picture one. Video one is also a control net and the main strong reference driving camera animation and character animation. This is the most important line. Without this line, it might not stick to your animation."
2. "Picture one is the final and constant look throughout the whole video so that it prevents the model from shifting back to its original lighting. As an example, lighting and atmosphere doesn't change or shift away from picture one."
3. Describe what happens through the video ("a woman jumping and cheering across a snowy field while the weather is snowy and cloudy where the snow is covering everything similar to picture one. Match micro expressions hair and body movement of video one. Video one is the main drive for micro expressions hair and body movement.")

**Check**
- If the lighting drifts back to the original, the "picture one is the final and constant look" line is missing. If the animation slips, the "video one drives camera and character animation" line is missing.

**Why**
The model needs to be told what drives what: the video drives motion, the picture drives look. Without those two sentences, the model re-decides both on every window, and the video drifts.

## The human method, distilled

1. Split before you generate: windows of 56, overlap 5, sync tiles; drift is a window-size problem.
2. Only denoise what changes: masked latent for inpainting, crop for resolution, stitch with feathering.
3. Save latents before decoding: a decode crash must cost a file copy, never a re-run.
4. The prompt names the drivers: video one drives motion, picture one drives look.
5. Generate at target resolution; distrust the upscaler (micro-boiling) until it proves itself.

**Depth status:** FULL (full auto-captions, 1,001 cues, read in full; the Patreon workflows themselves were not downloaded, and no parameter beyond the captions is claimed).
