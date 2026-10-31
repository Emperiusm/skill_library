---
name: open-h3-regenerate-2k-refine
description: "Refine 24fps AI video with NVIDIA's Open-H3-Regenerate-2K in ComfyUI: merged refiner plus LightX2V FL2VA Turbo plus LMS Sharp adapter, noise 0.5 to 0.7 or upscale-only mode, independent windows for long clips. Trigger when H3 or 24fps generated footage needs detail refinement and 2K upscale."
---

# Open-H3-Regenerate-2K for ComfyUI: Refine and Upscale 24fps Video

## Purpose

This skill wraps NVIDIA's Open-H3-Regenerate-2K in ComfyUI custom
nodes (imlo2): take an existing 24fps generation (or native
MiniMax-H3 latents) and run NVIDIA's merged refiner/upscaler over it
with adjustable noise, in independent windows for long clips. Every
phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The core method is: **feed
24fps footage, pick a noise level from the comparison ladder, fit the
windows in VRAM.**

## Source

r/comfyui, imlo2, "Open-H3-Regenerate-2K for ComfyUI: refinement
nodes, noise controls and comparison examples" (score 24, 18 comments,
2026-10-30):

- https://www.reddit.com/r/comfyui/comments/1xjbwoe/
- Native Reddit video: v.redd.it/li33sky01lyh1
- Nodes: https://github.com/o-l-l-i/ComfyUI-Olm-Open-H3-Regenerate-2K
- Model card: https://nvlabs.github.io/Sana/Open-H3-Regenerate-2K/
- Model source:
  https://github.com/NVlabs/Sana/tree/sol-engine/models/Open-H3-Regenerate-2K
- Weights: https://huggingface.co/Efficient-Large-Model/Open-H3-Regenerate-2K

Evidence note: all facts below are the author's claims from the post
text plus the author's comment replies (exact parameters, VRAM
numbers, and failure modes). The 18 comments include parameter
discussion and a tested no-stacking rule. No third-party verification
in this audit.

## Tools used

- ComfyUI custom nodes wrapping NVIDIA's Open-H3-Regenerate-2K
  (published merged adapters, Sharp curve branches, learned latent
  upscaler)
- The merged single LoRA is: **refiner + LightX2V's FL2VA Turbo + LMS
  Sharp adapter**, "For these few steps the refiner is merged with
  LightX2V's FL2VA Turbo and the LMS Sharp adapter into a single LoRA"
- Refines existing 24fps video or native MiniMax-H3 latents
- Adjustable noise; upscale-only mode; memory controls
- Example workflows, test clip, and detailed comparison images in the
  repo
- Competing option: Kijai's LoRA (the author thinks it contains the
  refiner only, not the merged turbo/sharp stack)

## Phase 1: Feed it 24fps video or H3 latents

**Do**
1. Load a 24fps video. The node historically raised
   `ValueError("H3 refinement expects 24 fps; resample in your video
   loader first")` on anything else; the author has since added a
   feature so the node can digest different-fps inputs itself.
2. Or feed native MiniMax-H3 latents directly.

**Check**
- The reference example: 1344x768 source refined to 2560x1440, two
  steps from noise 0.5.

**Why**
The refiner is trained on 24fps H3 output; off-rate inputs break its
temporal assumptions. The author fixed the footgun in the node rather
than documenting around it.

## Phase 2: Set noise and mode

**Do**
1. Choose upscale-only mode (adds texture/definition, minimal change)
   or noise mode. The README compares upscale-only vs noise 0.5 / 0.6
   / 0.7, pick your level from the comparison images, not from
   description.
2. For longer clips, process in independent windows (window boundaries
   may show).
3. Do NOT stack another turbo LoRA on top of the merged one. A
   commenter tested Kjai's LoRA + light2x turbo + lms lora manually
   stacked and it looked worse than the merged one: "They already have
   turbo lora unlike Kjai's one so dont stack more turbo."

**Check**
- Faces, jewelry, lettering, and small patterns WILL change under
  noise. Commenters report talking and emotional scenes "get
  butchered"; low-res sources look better after refinement.

**Why**
The merge is the product: refiner + turbo + sharp adapter in one LoRA.
Stacking more turbo on top degrades the result. Noise is a change
budget, and human faces are where the budget gets spent first.

## Phase 3: Fit it in VRAM

**Do**
1. The author tested on Windows, RTX 5090 (32 GB VRAM), 128 GB RAM:
   "probably runs at least on an RTX 4090, and you can dial down a few
   settings to try to make it fit." Smaller cards are unvalidated.
2. Expect high RAM and VRAM consumption; dial the memory controls down
   if VRAM is tight.

**Check**
- Watch VRAM during the first window; reduce window size or settings
  before committing to the full run.

**Why**
The learned latent upscaler plus merged adapters is heavy by design;
the author is explicit that this is a 4090-class tool.

## The human method, distilled

1. **"IMHO it's a bit like SoL-Refiner when it comes to output"**,
   calibrate expectations against a known refiner before adopting.
2. **When users hit the 24fps wall, fix the node** (fps digestion),
   don't write a FAQ.
3. **Ship comparison images** (upscale-only vs 0.5/0.6/0.7) so users
   pick noise from evidence, not vibes.

**Depth status:** FULL (author post text + author comments with exact
parameters, VRAM numbers, and failure modes).
