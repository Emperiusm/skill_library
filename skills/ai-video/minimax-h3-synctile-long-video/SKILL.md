---
name: "minimax_h3_synctile_long_video"
description: "Generate long MiniMax H3 videos in ComfyUI (tested 600 frames / 25 s at 4K) with zero clip chaining: SyncTile blends overlapping spatial tiles x temporal windows at every model call so there is a single denoising trajectory. Two-stage: 0.5 MP draft, 3D latent upscale, 4K refine. Trigger when MiniMax H3 videos must run long or 4K without seams between segments."
---

# MiniMax H3 SyncTile Long Video in ComfyUI

## Purpose

This skill reconstructs the exact workflow NyckM documents for
`Bruxosdovfx-SyncTile-MiniMax-H3-v5.4` (v5.5 nodes), step by step, so another
agent can follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The workflow's core method is: never chain clips — split the video into
overlapping regions, predict all of them at every model call, and blend them
into one canvas so there is exactly one denoising trajectory.

Variant note: same tool family as `minimax-h3-character-swap-comfyui` and the
same problem class as `minimax-h3-selflift-long-video` (long H3 videos), but a
different workflow. SelfLift stitches finished segments with dual sampling and
Color Transfer at the seams; SyncTile never creates segments to stitch — the
blend happens inside every denoising step.

## Source

Creator: NyckM (Emotional_Example_12 posted the demo to r/comfyui).
Repo: https://github.com/NyckM/Bruxosdovfx-SyncTile-MiniMax-H3-v5.4
(r/comfyui post 1xbzx5n, "H3 Minimax Background Replace 4k 600 frames Plus") |
2026-10-23 scout run. Evidence: the repo README (EN section, read in full),
the shipped workflow JSON
`workflow/minimaxH3BackgroundSwap_v21a_guiaFrameAnterior.json` (218 KB, node
titles and widget values read directly), and the demo post linking the
workflow. No video narration exists; the repo is the primary source.

**Tools used:** ComfyUI (with native MiniMax H3 nodes), bruxosdovfx-SyncTile
v5.5 custom nodes, bruxosdovfx Media IO nodes (Load Video Pro / Load Image /
Save Video Pro), Comfyui_Minimax_h3_latent_Upscaler (LBH 3D), ffmpeg,
Background Replace v3 LoRA (optional).

**Depth status:** FULL (repo README + workflow JSON read firsthand; no
transcript or captions exist for the demo clip).

## When to use this skill

- A MiniMax H3 video must exceed the model's native length without visible
  seams between chained clips.
- Output must reach 4K without the VRAM cost of a full 4K latent.
- Background or character replacement must hold across a long shot.

## Prerequisites

- ComfyUI with native MiniMax H3 nodes.
- `git clone https://github.com/NyckM/Bruxosdovfx-SyncTile-MiniMax-H3-v5.4`
  into `ComfyUI/custom_nodes/` (or copy the `bruxosdovfx-SyncTile` folder).
  **Delete `ComfyUI-SyncTile-H3` if present** (old version). Restart; the
  console prints `[bruxosdovfx • SyncTile] v5.5 carregado`.
- bruxosdovfx Media IO pack: https://github.com/NyckM/Video-Util-ComfYUI
- 3D latent upscaler: https://github.com/LBH-123-AI/Comfyui_Minimax_h3_latent_Upscaler
- ffmpeg on PATH (or `pip install imageio-ffmpeg`).
- Models (exact files from the workflow README):
  - `models/diffusion_models/Minimax/minimax_h3_fused_refdelta_r1024_turbo8_mystic07_int8_convrot.safetensors`
    (21 GB; fused ref2va+fl2va, turbo 4 steps)
  - `models/text_encoders/qwen3vl_32b_minimax_h3_int8_convrot.safetensors`
    (27 GB; lower-RAM alternative: `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors`, 15.7 GB)
  - `models/vae/Minimax/minimax_h3_lynnreal_light_vae_int8_convrot.safetensors`
    (light, fast video VAE; more detail/less fake texture:
    `minimax_h3_video_vae_int8_convrot` or `_fp16`)
  - `models/vae/Minimax/minimax_h3_audio_vae_fp32.safetensors`
  - `models/latent_upscale_models/minimax_h3_latent_upscaler_3d_conv_v1_bf16.safetensors`
  - Optional LoRAs (both stacks OFF by default; the fused model already
    includes turbo): `minimax_h3_pdmd_4step_lora_avg_rank_57_bf16` at 1.0
    (only with a NON-turbo model) + Background Replace v3 at 1.0 (merge of 5
    LoRAs, BF16 1.9 GB, https://huggingface.co/NyckM/Background_Replace_Minimax_H3);
    stack 2: `minimax_h3_lms_v1.0_r64` at 0.3 (sharpness).

## Phase 1: Load inputs at the model's native cadence

**Do**
1. In Bruxos Load Video Pro, pick the source video. **Force 24 fps** — H3
   runs at 24 fps.
2. In Load Image, pick the reference photo (it doubles as frame guide 1).
3. Write the prompt to describe what changes AND what stays, phrased to hold
   "in every frame" — each temporal window reads the prompt on its own.

**Check**
- The loader's frame grid reads `H3 17n+5`; valid lengths are 124, 243, 362,
  600, ... frames. A 600-frame load is the tested 25-second case.
- Hover any SyncTile node input for the PT / EN / 中文 explanation.

**Why**
H3's temporal grid is fixed (17n+5). Feeding an off-grid length invites
truncation or padding artifacts; the window math downstream assumes it.

## Phase 2: Stage 1 — draft the whole video at ~0.5 MP in blended windows

**Do**
1. Wire SyncTile Ref2VA Conditioning (H3) with tile 4096 (= no spatial split
   at this resolution) and **124-frame windows, overlap 39**.
2. Use the SyncTile Guider (H3) as a drop-in for the Basic Guider — it blends
   the regions at every model call.
3. Run **4 turbo steps** (the fused int8 model).

**Check**
- VRAM stays at one window's cost even on a 600-frame timeline; if it does
  not, a window/overlap value mismatches between the conditioning nodes.
- Same `window_frames` / `window_overlap_frames` on both conditioning nodes.

**Why**
Every window is predicted and blended into one canvas at each step, so there
is one denoising trajectory for the whole video. Seams cannot form because
segments are never rendered independently. (Author's one-sentence version:
"the video is split into overlapping regions; at every model call all regions
are predicted and blended into one screen.")

## Phase 3: 3D latent upscale (no decode)

**Do**
1. Pass the stage-1 latent through the LBH 3D latent upscaler to ~6–8 MP
   **without decoding to pixels**.

**Check**
- Composition from stage 1 is preserved; only resolution changes.

**Why**
Decoding then re-encoding would cost a full VAE round trip and risk detail
loss; upscaling in latent space keeps the single-trajectory composition
intact for the refine pass.

## Phase 4: Stage 2 — 4K refine with spatial tiles x temporal windows

**Do**
1. Run SyncTile with **1472x896 spatial tiles x 124-frame windows**.
2. Refine with sigmas `0.878, 0.8, 0.6316, 0` — final steps only: fixes
   texture, keeps composition.
3. Set `temporal_mode = carry previous frames` on the SyncTile Guider (v5.5):
   windows run in sequence and each window's start locks to the last
   `carry_frames` (**21**) finished frames of the previous one.

**Check**
- No ghosting or double exposure at window joins; camera motion holds.
- If VRAM overflows: drop `window_frames` to 107 or 90; raise
  `window_overlap_frames` to 56 or 73 if seams or flicker appear.

**Why**
The carry-frames lock is what removes the classic long-video failure modes
(ghosting at joins, drifting camera). Overlap is the seam budget: more
overlap costs VRAM, less risks flicker. Tune overlap up only when you see the
defect, not preemptively.

## Phase 5: Frame guides (optional, for background/character hold)

**Do**
1. The Load Image photo is already guide 1 (frame 1).
2. For more guides: unmute the blue "Frames-guia extras" group, load a still
   in each Guide node (each still = that source frame with the background
   already swapped, same framing), Ctrl+M the group, and type the frames in
   `guide_frames` on the stage-1 node in the same order (e.g. 100, 220, 340,
   460). Number of images must equal number of frames.
3. Place one guide every ~4–5 seconds so every window has an anchor.

**Check**
- The background/character holds through the whole video instead of
  drifting mid-shot.

**Why**
The prompt is read per window; a visual anchor every few seconds pins the
identity that text alone lets drift.

## Phase 6: Stream-decode to file

**Do**
1. Decode with SyncTile Stream Decode (H3): block by block straight to file
   (h265 10-bit, h264, or ProRes) **without filling RAM**.
2. Optionally take its IMAGE output into Bruxos Save Video Pro (the workflow
   writes mp4/h264 with a Kodak 5207 film-transform option in the shipped
   config).

**Check**
- Output lands in `output/` (Save Video Pro) plus an h265 copy in
  `output/SyncTile/`.
- Long renders never OOM the frame buffer.

**Why**
A 600-frame 4K decode does not fit in RAM as images; streaming the decode
block-by-block is what makes the long-video claim real rather than
theoretical.

## The human method, distilled

1. **One trajectory, not many clips.** "No tile seams, no chained clips, and
   the VRAM is one region's" — the author's sentence for the whole design.
2. **Draft cheap, refine dear.** 0.5 MP establishes composition in 4 steps;
   expensive pixels only touch texture.
3. **Overlap is a budget, not a default.** 124/39 is the tested point; move
   it only against an observed defect (flicker/seams up, VRAM down).
4. **Lock the joins explicitly.** `carry_previous_frames` with 21 carry
   frames exists because windows in sequence drift without it.
5. **Anchor identity visually.** Prompts are read per window; frame guides
   every ~4–5 s hold what text lets drift.
6. **Never decode until the file.** Latent-space handoffs between stages and
   streaming decode keep the pipeline inside VRAM/RAM budgets.

## Failure modes

- **Ghosting / double exposure at window joins:** enable
  `temporal_mode = carry previous frames`; verify `carry_frames` = 21.
- **Flicker or seams:** raise `window_overlap_frames` (39 → 56 → 73),
  same value on both conditioning nodes.
- **VRAM overflow:** lower `window_frames` (124 → 107 → 90); use the nvfp4
  text encoder (15.7 GB vs 27 GB); use the light VAE.
- **Background drifts mid-video:** add frame guides; restate the hold in the
  prompt with "in every frame".
- **Old node pack conflicts:** delete `ComfyUI-SyncTile-H3` before
  installing v5.5.
