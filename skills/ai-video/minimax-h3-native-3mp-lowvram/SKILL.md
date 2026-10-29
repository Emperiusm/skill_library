---
name: minimax-h3-native-3mp-lowvram
description: "Generate MiniMax H3 video natively at 2336x1312 (3.06 MP) on an RTX 3060 12 GB: INT8 Ref2VA V2 + DMAD 4-step LoRA, res_multistep/simple, INT8 sparse attention at video_budget 0.10, 4096-row chunks, 243 frames in 33 minutes. Trigger when a 12 GB card must generate high-resolution video natively instead of upscaling."
---

# MiniMax H3 Native 3MP on a 12 GB Card

## Purpose

This skill reconstructs the native-resolution low-VRAM workflow, step by step, so another agent can run the same recipe. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: generate natively at 3 MP on a 12 GB card by stacking every low-VRAM trick at once, and never upscale as a substitute for native resolution.

## Source

- Post: "RTX 3060 12GB + MiniMax H3: Native 2336×1312 Snow Leopard Video | 243 Frames, 4 Steps, 33 Minutes" — https://www.reddit.com/r/comfyui/comments/1xgu6b8/ (score 24, 12 comments)
- Evidence: full post text + comments, 2026-10-28 scout run. No workflow JSON was inspected, so node wiring beyond the named settings is not claimed.

## Tools used

MiniMax H3 Singularity Ref2VA V2 (INT8), DMAD 4-step LoRA (weight 1.0), Comfy Kitchen INT8 Sparse attention (`video_budget = 0.10`), ComfyUI (host), Starlight Precise 2.6 (commenter enhancement pass only, not the author's pipeline). Hardware: RTX 3060 12 GB, 32 GB system RAM.

## Phase 1: Set the native-resolution target and refuse the upscale shortcut

**Do**
1. Target native 2336×1312 (3.06 MP), no upscaling, 243 frames at 24 FPS (~10 seconds).
2. Start from the author's own history: "I started experimenting with local AI video generation at around 0.3MP, relying on upscaling for higher-resolution output", then moved to native generation "after a lot of workflow optimization and testing".

**Check**
- The output resolution must be the generation resolution (2336×1312 in the sampler), not a post-hoc upscale of a smaller generation.

**Why**
Upscaling invents detail; native generation (in the author's experience) preserves it. The author reports "the difference in fine detail between upscaled low-resolution video and native high-resolution generation is huge" — a reported observation from experience, not a controlled benchmark in the post.

## Phase 2: Stack the low-VRAM recipe exactly

**Do**
1. Model: MiniMax H3 Singularity Ref2VA V2 (INT8).
2. LoRA: DMAD 4-step, weight 1.0.
3. Inputs: 1 starting frame + 2 snow leopard reference images.
4. Sampler: `res_multistep`. Scheduler: `simple`.
5. Sparse attention: Comfy Kitchen INT8 Sparse, `video_budget = 0.10`.
6. Memory optimization: 4096-row chunks.
7. Accept the cost: sampling speed 426.86 s/it, total generation time 1989.93 seconds (33m 09.93s) for 243 frames.

**Check**
- If any one element is dropped (INT8 model, 4-step LoRA, sparse attention at 0.10, chunked memory), the 12 GB claim is no longer the author's claim; the recipe is a stack, not a menu.

**Why**
No single trick fits 3 MP on 12 GB. INT8 halves weights, the 4-step LoRA cuts sampling passes, sparse attention at a 0.10 budget cuts the attention matrix, and chunking caps peak memory. Each trick buys a different slice of the budget.

## Phase 3: Calibrate against other 12 GB results in the thread

**Do**
1. Record the commenter corroboration, labeled as commenter results, not the author's: JinnTsui reports 25-second videos on an RTX 3060 12 GB with 32 GB RAM, including 1280×768, 600 frames in 1,347 seconds (22m 27s) with H3 + DMAD 4-step.
2. Record the mechanism commenters propose for why 12 GB cards survive at all (froschquark): "the 'magic' is simply the memory optimizations which does not let you go OOM but just shuffles the data into RAM and later also into system pagefile". Labeled as a commenter hypothesis, not a measured fact.
3. Note the open question (Danny_Stock): if 3 MP for 10 seconds takes 33 minutes, the same workflow should in theory give 1 MP for well over 10 seconds; unanswered in the retrieved comments.
4. Note the enhancement fork, not part of the recipe: ThoughtCounter ran the video through Starlight Precise 2.6 at 1:1 (no upscale).

**Check**
- Corroboration counts only when the card class matches (12 GB + 32 GB RAM); results on larger cards do not validate this recipe.

**Why**
A single 33-minute run is a proof, not a budget table. The thread's other 12 GB runs are what turn one result into a usable expectation for the same hardware class.

## AAA studio practice

No named AAA studio publishes a MiniMax H3 low-VRAM recipe, so this section is production inference practice, labeled as such, not a studio claim. The pattern it documents is the same stack the skill uses, applied as a measured discipline rather than a one-off run:

- **Quantize as the production default, and measure the saving.** CogVideoX's production optimization docs describe INT8 weight-only quantization (about 20-30% memory reduction, minimal quality impact) and FP8 dynamic quantization (about 40-50%, H100 or higher) via TorchAO, alongside VAE slicing and tiling that cut decode memory by roughly 50-80% combined. The discipline is to pick one quantization scheme, state it, and keep it fixed across a run, exactly as this skill pins INT8.
  Source: https://deepwiki.com/zai-org/CogVideo/7-performance-optimization
- **Treat INT8 as a safe production starting point, not a free lunch.** Production quantization guidance puts INT8 at roughly 2x memory reduction versus FP16 with minimal accuracy loss, and warns that the quality cost curve steepens below INT8 (INT4 costs a further 1-3% on most evals). That is why this skill's stack stops at INT8 plus sparse attention and chunking instead of pushing to INT4 to chase a bigger number.
  Source: https://developers.redhat.com/articles/2026/09/07/understanding-w8a8-int8-llm-quantization
- **Leave dense where sparsity visibly hurts, especially at seams.** An independent video-inference profiling writeup reports block-sparse attention in 41 of 48 layers, with the 7 layers where sparsity visibly hurt left dense, along with the frames that make loops seamless, because sparse attention changes what the model can see and seam frames are exactly where it hurts. Applied here: a sparse-attention budget is not uniform by default; the first and last frames of a clip, and any join frame, are the places to verify dense before accepting a sparse budget.
  Source: https://phosphene.cc/blog/ai-video-inference-profiling-silent-fallback

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Write a `run-manifest.json` for every native-resolution run: model and precision, LoRA and weight, sampler and scheduler, sparse-attention budget, chunk rows, frame count and resolution, seconds per iteration, total seconds, and peak VRAM (or the system-RAM/pagefile spill note, labeled as the commenter hypothesis it is).
2. Treat the manifest as a contract: if any one stack element changes, the previous run's time and VRAM figures are void and the run is re-measured, not carried over.
3. Add a seam check to every run: render and inspect the first frame, the last frame, and one mid-clip join frame at full resolution before accepting the sparse-attention budget; if a seam frame shows attention artifacts, re-run that segment dense and record the cost delta in the manifest.

**Check**
- A run is shippable only when its manifest is complete and its seam frames pass; a run with a missing peak-VRAM figure or an unchecked seam frame is an unmeasured claim, not a budget.
- Two runs on the same hardware class are comparable only when their manifests match on every stack element except the one being varied.

**Why**
The skill's value is a reproducible budget table for a hardware class, not one 33-minute anecdote. A manifest plus a seam check turns each run into a comparable data point, and the dense-at-seams rule is what keeps the sparse budget honest.

## The human method, distilled

1. Generate at the target resolution natively; do not let upscaling stand in for resolution.
2. Stack low-VRAM tricks (INT8, few-step LoRA, sparse attention with a stated budget, chunked memory) and publish every setting, so the recipe is reproducible rather than inspirational.
3. State the limit honestly: the author calls this "my highest successfully completed native-resolution H3 test so far, not a claim about the GPU's absolute limit".

## Depth status

FULL — full post text with every sampler, LoRA, attention, chunk, and timing number, plus commenter corroboration on the same hardware class.
