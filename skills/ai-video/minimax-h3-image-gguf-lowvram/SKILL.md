---
name: minimax-h3-image-gguf-lowvram
description: "Run MiniMax H3-Image locally in ComfyUI on a low-VRAM or Pascal card: Abiray GGUF models with the ComfyUI-GGUF node by city96 and a fix script, ComfyUI 0.45.0 or newer, CUDA 13/driver 580 on RTX 40-series, CUDA 12.6 plus GGUF only on GTX 10-series. Trigger when H3 Image must run locally on modest hardware, or when choosing between the official files and the GGUF path."
---

# MiniMax H3-Image, GGUF Low-VRAM Run in ComfyUI

## Purpose

This skill reconstructs the exact workflow Olivio Sarikas shows for running MiniMax H3-Image locally in ComfyUI on low-VRAM hardware: Abiray GGUF models with the ComfyUI-GGUF custom node by city96 and a fix script, matched to the GPU by ComfyUI version, PyTorch/CUDA build, and driver. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: match the model files and the ComfyUI version to your GPU first; the generation settings follow from that match.

## Source

Creator: Olivio Sarikas. Video: "MiniMax H3 Image - Normal + GGUF Guide!", https://www.youtube.com/watch?v=kXZCGml0th0 (14:39, 7,237 views, uploaded 2026-11-18). Audited in the 2026-11-20 scout run, audit 3, from the description (no captions exist for this video).

This is a different workflow from `minimax-h3-image-native-comfyui` (the official native day-0 workflow: one checkpoint, 6 steps, guidance 1, native resolutions to 6272x2688). Same model, different distribution: the GGUF path is for low-VRAM and Pascal cards, with its own node, fix script, and version gates. It is also different from the community P-H3-Image fine-tune (skill `pruna-p-h3-image-comfyui`): official weights in GGUF form, not a distilled fine-tune.

## Tools used

ComfyUI 0.45.0 or newer, MiniMax H3-Image (official Comfy-Org files: int8, w4a8, text encoders, VAE, PE), Abiray GGUF models, Abiray GGUF workflow JSON, GGUF fix script (`minimax_h3_image_gguf_fix.py`), ComfyUI-GGUF custom node by city96, PyTorch 2.13 with CUDA 13.0, NVIDIA driver 580 or newer.

## When to use this skill

- Running MiniMax H3-Image locally in ComfyUI on a low-VRAM card.
- Running H3-Image on a GTX 10-series (Pascal) card that cannot run the modern stack.
- Choosing between the official Comfy-Org files and the Abiray GGUF distribution.
- Diagnosing why ComfyUI does not recognize the "minimax" model type.

## Prerequisites

- ComfyUI 0.45.0 or newer (older versions do not know the "minimax" model type).
- For the GGUF path: the ComfyUI-GGUF custom node by city96, updated to the latest version.
- A current ComfyUI Portable build (e.g. PyTorch 2.13 with CUDA 13.0) on RTX 40-series cards; the CUDA 12.6 Portable build on GTX 10-series cards.
- NVIDIA driver 580 or newer for CUDA 13.x.

## Phase 1: Check your versions before downloading anything

**Do**
1. Check PyTorch and CUDA in a ComfyUI Portable command prompt: `python_embeded\python.exe -c "import torch; print(torch.__version__, torch.version.cuda, torch.cuda.is_available())"`. Example output: `2.13.0+cu130 13.0 True`.
2. Check the driver and max supported CUDA version with `nvidia-smi`, looking at "CUDA Version" in the top right.
3. Confirm the ComfyUI and PyTorch versions at the top of the ComfyUI startup log.

**Check**
- The three version numbers must agree with each other before any model file is chosen: PyTorch's CUDA build, the driver's supported CUDA, and ComfyUI's version.

**Why**
The model files, the GGUF path, and the driver requirement all depend on these three numbers. Checking them first prevents downloading the wrong model variant.

## Phase 2: Pick the model files for your hardware

**Do**
1. For the normal path, take the official ComfyUI files (int8, w4a8, text encoders, VAE, PE) from https://huggingface.co/Comfy-Org/MiniMax-H3-Image/tree/main.
2. For low VRAM, take the GGUF models by Abiray from https://huggingface.co/Abiray/MiniMax-H3-Image-GGUF, plus Abiray's GGUF workflow JSON (drag into ComfyUI): https://huggingface.co/Abiray/MiniMax-H3-Image-GGUF/resolve/main/image_minimax_h3_image_t2i_gguf.json

**Check**
- *Inference:* the description lists both paths but gives no file sizes, VRAM numbers, or step counts for either; those are in the video, which has no captions.

**Why**
One model, two distributions: the official files for full-precision cards, GGUF for low-VRAM cards. The hardware decides the path, not preference.

## Phase 3: Meet the version and driver gates

**Do**
1. Use ComfyUI version 0.45.0 or newer; older versions do not know the "minimax" model type.
2. For GGUF, update the ComfyUI-GGUF custom node by city96 to the latest version.
3. Place the GGUF fix script directly in `ComfyUI/custom_nodes`, then restart ComfyUI. Script: https://huggingface.co/Abiray/MiniMax-H3-Image-GGUF/blob/main/minimax_h3_image_gguf_fix.py
4. On RTX 40-series cards, use a current ComfyUI Portable build (PyTorch 2.13 with CUDA 13.0); CUDA 13.x requires driver 580 or newer.
5. On GTX 10-series (Pascal) cards, use the ComfyUI Portable build with CUDA 12.6 and GGUF models only.

**Check**
- ComfyUI must recognize the "minimax" model type (0.45.0+); the GGUF node must be current; the fix script must be in `custom_nodes` before the restart.

**Why**
Each gate is a hard failure if missed: an old ComfyUI cannot load the model at all, a stale GGUF node breaks the GGUF path, and CUDA 13 on an old driver fails at startup. The Pascal rule is the fallback for cards that cannot run the modern stack.

## What the video promises that the description does not disclose

- "Which model files to download, the right settings, and how to get the best quality out of it" are the video's stated contents, but the description carries only the files and the version gates. Step counts, sampler settings, and the quality settings are in the video, which has no captions and was not downloaded (download allowance spent on the two higher-ranked videos). The model itself renders "insanely detailed images at up to 16+ megapixels" per the description.

## The human method, distilled

1. Versions first: PyTorch, CUDA, driver, ComfyUI must agree before any download.
2. Hardware picks the distribution: official files for modern cards, GGUF for low VRAM and Pascal.
3. The fix script and the node update are part of the install, not optional extras.

## AAA studio practice

ComfyUI has crossed from community tool into AAA production platform, and quantization is how studios put big models on ordinary hardware. Ubisoft La Forge open-sourced CHORD, its PBR material estimation model, together with ComfyUI custom nodes, explicitly because ComfyUI gives them "an efficient framework to build integrated workflows doing texture image synthesis, material estimation and material upscaling"; the three-stage pipeline (texture generation, CHORD material estimation, material upscaling to 2K/4K) produces PBR texture sets that integrate directly into DCC tools and game engines for prototyping and placeholder assets. At DigiPro 2025 Ubisoft presented the next step: an end-to-end agentic pipeline where an N8N workflow-automation platform with a ComfyUI image-generation pipeline converts meeting transcripts and creative briefs into structured asset casting lists with concept previz imagery in minutes, and an agent connected to Blender via MCP populates scenes from a library of over 30,000 production-indexed USD assets. The studio lesson is that the workflow graph, not the model, is the asset: the same graph runs on a laptop and as a deployed endpoint, and each stage (generation, estimation, upscaling) operates independently so a stage can be swapped without rebuilding the pipeline.

The GGUF half of this skill is the same quantization discipline applied to local inference. On video diffusion models, GGUF quantization compresses 16-bit weights to 8/6/4-bit integers with layer-sensitive schemes: critical layers keep higher precision while less sensitive layers compress harder. The HunyuanVideo 1.5 guide measures the ladder as Q8 minimal quality loss at 12-14 GB VRAM, Q6 slight reduction at 10-12 GB, Q4 noticeable but acceptable at 8 GB, with Q4 cutting a 23 GB model to under 7 GB; quality degradation becomes noticeable at Q3 and below. Unsloth's LTX-2.5-GGUF ships Q4_K_M, Q5_K_M, Q8_0 and a BF16 baseline targeting 6-12 GB VRAM against 16 GB+ unquantized, with sensitive temporal attention heads and normalization layers preserved at higher bit-depth. *Inference:* those numbers are measured on video diffusion transformers, not on H3-Image; treat them as the shape of the ladder (Q8 near-lossless, Q4 the budget tier, Q3 the cliff), not as H3-Image measurements.

The AAA rule that transfers: version-pin the whole stack and treat the quantization tier as a budget decision, not a preference. The skill's Phase 1 version check is the local version of Ubisoft's staged pipeline contract: the graph declares its model, node, and driver requirements up front, and a mismatched stage fails before any generation starts.

Sources:
- ComfyUI blog, "Ubisoft Open-Sources the CHORD Model and ComfyUI Nodes for End-to-End PBR Material Generation" (ComfyUI as AAA production platform, three-stage pipeline, 1024 to 2K/4K upscale): https://blog.comfy.org/p/ubisoft-open-sources-the-chord-model
- DigiPro 2025, "From Brief to Scene: Agentic AI for Asset Production at Ubisoft" (N8N + ComfyUI brief-to-previz pipeline, 30k USD asset library, Blender MCP scene population): http://digiproconf.org/program/program-4/
- Apatero, "HunyuanVideo 1.5 Low VRAM Guide - GGUF & 5G Builds" (Q8/Q6/Q4 VRAM ladder, 23 GB to under 7 GB at Q4, Q3 quality cliff): https://apatero.com/blog/hunyuanvideo-15-low-vram-gguf-5g-complete-guide-2025
- ArtRealmAI, "LTX-2.5-GGUF: Lean Video Generation on Consumer GPUs" (Q4_K_M/Q5_K_M/Q8_0 tiers, 6-12 GB target, sensitive layers preserved): https://artrealmai.com/article/ltx-2-5-gguf-unsloth-image-to-video-quantized

### Agent automation upgrade (Do / Check / Why)
**Do**
- Add a version-gate script that runs before any download: it prints PyTorch version, CUDA build, driver CUDA ceiling from `nvidia-smi`, and ComfyUI version into `version-gate.json`, and exits non-zero with the exact mismatch named if any of the three disagree with the chosen model path (GGUF vs official files).
- Add a quantization-tier manifest `gguf-tier.json` recording the chosen tier (Q8, Q6, or Q4), the model file hash, the measured VRAM at load, and the acceptance image; a tier change is a manifest change, not a re-download guess.
- Add a fix-script presence check to the gate: verify `minimax_h3_image_gguf_fix.py` exists in `ComfyUI/custom_nodes` and the ComfyUI-GGUF node version is current before starting ComfyUI, so a stale node fails at setup instead of mid-generation.
**Check**
- The gate fails with the named version (e.g. "driver supports CUDA 12.6, portable build needs 13.0") instead of a load error after the model download.
**Why**
- The skill's whole failure mode is version mismatch discovered late; a gate that runs before downloads turns the manual Phase 1 check into a contract, and the tier manifest makes the Q8/Q6/Q4 tradeoff explicit and reversible instead of a one-off download choice.

**Depth status:** PARTIAL (files, links, version gates, and hardware rules are fully disclosed in the description; generation settings and quality steps are in-video only, no captions).
