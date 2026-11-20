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

**Depth status:** PARTIAL (files, links, version gates, and hardware rules are fully disclosed in the description; generation settings and quality steps are in-video only, no captions).
