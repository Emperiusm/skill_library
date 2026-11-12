---
name: minimax-h3-singularity-v2-6gb
description: "Run MiniMax H3 Singularity V2 on a 6 GB VRAM card in ComfyUI: one workflow with Text2Video, Img2Video, MultiRef + Audio, Ref2Video, and 4K upscale + frame interpolation, using pruned int8/w4a8/GGUF builds, H3 SLA Attention, Low VRAM Attention, and Chunk FeedForward, with the TaoMate 3-step LoRA and R34L1SM realism LoRA. Includes per-mode timings on 6 GB and the missing-node fix (H3SLAAttention is ComfyUI-PlagueKind-Nodes; Low VRAM Attention and Chunk FeedForward are ComfyUI-KJNodes). Trigger when setting up H3 video on a 6 GB card, or when choosing between low-VRAM H3 recipes."
---

# MiniMax H3 Singularity V2 on a 6 GB GPU

## Purpose

This skill reconstructs the MiniMax H3 Singularity V2 6 GB workflow from the author's post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: one workflow file that fits a 6 GB card by quantising everything and offloading the attention work to the right custom nodes.

## Source

Creator: EzkaProductions. Reddit post:
https://www.reddit.com/r/comfyui/comments/1xtj5xr/minimax_h3_singularity_v2_on_a_6_gb_gpu_text2video/
(r/comfyui post 1xtj5xr, score 55, 15 comments) | 2026-11-12 scout run, audit 2.
Workflow file (free) in the linked YouTube video's description:
https://www.youtube.com/watch?v=opoqT6fB_Nk

This is a distinct recipe from the other low-VRAM H3 skills in this library (`minimax-h3-native-3mp-lowvram`, the RefMod workflow, the no-mask character-swap LoRA recipe): different model build (Singularity V2 fine-tune, pruned int8/w4a8/GGUF), different attention stack, and the only one with per-mode timings on 6 GB. Do not merge them.

## Tools used

**ComfyUI**, **MiniMax H3 Singularity V2** (fine-tune; pruned int8 / w4a8 / GGUF builds), **Qwen3-VL** text encoder, **H3 SLA Attention**, **Low VRAM Attention**, **Chunk FeedForward**, **TaoMate 3-step LoRA**, realism LoRA (trigger `R34L1SM`), **ComfyUI-PlagueKind-Nodes** (owns H3SLAAttention), **ComfyUI-KJNodes** (owns Low VRAM Attention and Chunk FeedForward).

## Phase 1: Pick the mode and the references

**Do**
1. Choose one of five modes in the single workflow: Text2Video (structured H3 prompt: style, subject, setting, camera, action, dialogue, soundscape), Img2Video (animate any image with native audio), MultiRef + Audio2Video (character + environment images plus your own voice clip, "with solid lip sync"), Ref2Video (up to 4 reference images, each with its own role, "great for product ads"), or 4K upscale + frame interpolation (720p to 4K, 24 to 48 fps).
2. Get the workflow file from the linked YouTube video's description (free).

**Check**
- MultiRef + Audio2Video is the mode commenters asked about most (voice-clip length for stable lip sync, face consistency across separate clips); the author answered with a tutorial link, not a number, so clip length for stable lip sync is unverified. Do not quote a number for it.

**Why**
- One workflow with five modes means the 6 GB setup cost is paid once. The mode choice is a prompt-and-reference choice, not a reinstall.

## Phase 2: Make it fit in 6 GB

**Do**
1. Use pruned int8 / w4a8 / GGUF builds of Singularity V2.
2. Turn on H3 SLA Attention + Low VRAM Attention + Chunk FeedForward.
3. Add the TaoMate 3-step LoRA for speed, plus a realism LoRA (trigger: `R34L1SM`).

**Check**
- The author's measured times on 6 GB VRAM: Text2Video 0.6 MP in ~18 min; Img2Video 8 s at 0.6 MP in ~25 min; MultiRef + Audio 10 s at 0.6 MP in ~35 min; Ref2Video 8 s at 0.8 MP in ~45 min. If a run is much slower than these, the quantised build or the attention nodes are not active.

**Why**
- Quantisation buys the fit; the attention nodes buy the speed. Either one alone still OOMs or crawls on 6 GB.

## Phase 3: Fix the red nodes

**Do**
1. If some nodes show red and the Manager says nothing is missing, the source is mislabeled, not missing.
2. H3SLAAttention comes from **ComfyUI-PlagueKind-Nodes**; Low VRAM Attention and Chunk FeedForward come from **ComfyUI-KJNodes**. Install both and restart.

**Check**
- After restart, the red nodes resolve. If they do not, the wrong pack was installed; the node names above are the author's exact attribution.

**Why**
- A mislabeled source sends you to the Manager for a pack that is already installed. The fix is knowing which pack actually owns the node.

## The human method, distilled

1. Quantise the model, then fix the attention path; do not try to run full precision on 6 GB.
2. One workflow, five modes; the mode is a reference choice.
3. When the Manager says nothing is missing but nodes are red, the source label is wrong. Check the pack, not the install.

**Depth status:** FULL (full post text with timings, node attributions, and LoRA triggers; 14 comments; the linked YouTube tutorial was not retrieved, so the workflow file itself is unverified).
