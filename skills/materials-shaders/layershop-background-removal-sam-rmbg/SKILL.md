---
name: layershop-background-removal-sam-rmbg
description: "Remove backgrounds in LayerShop, the free open-source Photoshop-style ComfyUI editor: pick what stays by subject, selection, words, or click, let SAM 3.1 find it, route the edge to BiRefNet, RMBG 3.0, or Lucida by content type, and keep the result as a paintable mask or new layer, all local on the bundled ComfyUI. Trigger when cutting out a subject in a Photoshop-style editor backed by ComfyUI. DEPTH-LIMITED: post text plus author comments, no on-screen timings or model filenames."
---

# Background Removal in LayerShop with SAM 3.1 and RMBG 3.0

## Purpose

This skill cuts out a subject in editor language, with the edge model chosen for the edge type. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: pick what stays in editor language, let SAM find it, route the edge to the model built for that edge type, and keep the result editable.

**Depth status: DEPTH-LIMITED, upper end.** Built from the author's full post text plus all 14 retrieved comments, including author answers on performance, GPU requirements, cloud models, and the upstream version pin. No on-screen step timings, model file names, or VRAM measurements beyond one user's report were disclosed, and no frame review was done. Phases below are reconstructed from the author's text; no parameters are invented.

## Source

- Post: "Background removal with SAM 3.1 + RMBG 3.0 in a Photoshop-style editor" by HonestTicket6013 (Slav) — https://www.reddit.com/r/comfyui/comments/1y4cg81/ (score 68, 14 comments, all retrieved).
- Download: https://layershop.aardvarkstudios.net/download/?ref=reddit-comfyui-removebg ; source: https://github.com/SlavomirDurej/layershop
- Scout audit 2026-11-25.

## Tools used

LayerShop (free, open-source Photoshop-style editor by Slavomir Durej, runs ComfyUI in the background); SAM 3.1 (object finding); edge models BiRefNet (quick photo cut-outs), RMBG 3.0 (hair and fur), Lucida (logos, text, and glass). Cloud models named in comments for users without a suitable GPU: GPT Image 2.5 Sunburst, GPT Image 2.5 Flare, Nano Banana Pro, Nano Banana 2, FLUX 3, Grok Imagine 2.0, Muse Image (all via API keys). Still Windows only, and a preview.

## Phase 1: Pick what stays

**Do**
1. Choose one of four inputs: the main subject, a rough selection, a few words, or a click.
2. SAM 3.1 finds the object from that input.

**Check**
- The selection is the object, however it was specified; the user never draws a precise mask by hand.

**Why**
Editor-language selection (subject, words, click) is the interface contract: the AI does the boundary, the human does the intent.

## Phase 2: Cut the edge with the right model

**Do**
1. Route the edge by content: BiRefNet for quick photo cut-outs, RMBG 3.0 for hair and fur, Lucida for logos, text, and glass.
2. Take the result as a mask you can still paint on, or as a new layer.

**Check**
- Hair/fur, glass, and text edges are the discriminating cases; each has its own model rather than one general cut-out. A commenter reports using the Rembg option to separate a man from a background, running a restoration prompt on the man, and putting him back over the background to get a restored colour subject over the original black-and-white background, with the layers visible side by side.

**Why**
No single edge model is best for hair, glass, and logos at once. Routing by edge type is the quality mechanism; keeping the mask paintable is the correction mechanism.

## Phase 3: Run it locally, on the bundled ComfyUI

**Do**
1. Run on your own PC; "nothing gets uploaded" for local models.
2. Use the ComfyUI version bundled with LayerShop. The author states in comments that some workflows are not compatible with external ComfyUI versions, especially if not up to date, and that the bundled version allows choosing speed-up LoRAs in model settings.
3. Note the upstream pin: the author states LayerShop stays on the stable 0.23.1 upstream release while upstream rewrites its UI framework and splits its engine, and will merge "once things settle (likely the next upstream release)", to port once instead of chasing daily changes.
4. For users without a suitable GPU, cloud models are available via pasted API keys (list above). LayerShop has the same requirements as ComfyUI and works best with an Nvidia GPU; a commenter on 16 GB VRAM + 32 GB RAM reports generation "incredibly slower" in LayerShop than a regular ComfyUI install (15 seconds per Krea generation normally, 4 minutes and 18% on a MOSS generation in LayerShop), and the author replies with the bundled-version and speed-LoRA checks in step 2. A user with an 8 GB VRAM card asks about SDXL; the author replies LayerShop has the same requirements as ComfyUI.

**Check**
- Local runs upload nothing. Slow runs are diagnosed first by bundled-version and speed-LoRA selection, not by hardware assumption.

**Why**
Bundling the ComfyUI version is a compatibility decision: the editor's AI tools sit inside that code, so tracking upstream daily would import regressions. The performance report is recorded as one user's experience, not a benchmark.

## Phase 4: Know the limits

**Do**
1. Still Windows only, and a preview: the author asks for reports on the trickiest pictures.
2. No video background removal: it is a photo editor, but short animated GIFs can be created (linked YouTube example in comments, not retrieved here).

**Check**
- Windows-only and photo-only are stated limits, not inferred ones.

**Why**
A preview release's contract is feedback on hard cases, not production coverage. The author explicitly solicits the trickiest pictures.

## AAA studio practice

- **Production VFX segmentation is a fully automatic first pass plus human supervision, scheduled at ingest, not a one-click finish.** Image Engine's automated video segmentation pipeline, presented at DigiPro 2025 and deployed on *Dune: Prophecy*, runs without user interaction when plates are ingested: text-prompted object detection, refined per-frame segmentation, and robust video tracking for temporal stability, stored in a custom ObjectId format, with a default behaviour of one mask per person. The authors report it was quickly adopted by artists, significantly reduced manual effort, and sped up preliminary composites, while manual rotoscopy or bluescreen cleanup is described as notoriously time-consuming. The transferable rule is LayerShop's Phase 1 plus Phase 2 in reverse order: run the automatic pass first and early, keep the human correction (here, the paintable mask) as the formal second stage, and never ship the automatic matte unreviewed. Source: https://arxiv.org/html/2507.07242v1
- **Foundation segmentation models reduce annotation effort but do not remove human supervision for production edges and temporal consistency.** A systematic review of deep-learning rotoscoping finds that SAM and SAM 2 dramatically reduce annotation effort yet still require human supervision for production-grade temporal consistency and fine boundary precision, and that hybrid human-in-the-loop architectures combining memory-based propagation, optical flow, and promptable segmentation outperform fully automatic methods in professional VFX workflows. That is the production justification for this skill's routing rule (Phase 2) and paintable-mask rule: the edge model and the human correction are both load-bearing. Source: https://www.extrica.com/article/26653
- **The newest matting models trade size for understanding, and the older segmentation model stays the high-volume choice.** Bria's RMBG 3.0 is built on its Fibo 2.0 generative image model, fine-tuned for alpha matting and distilled to a four-step matte, outputting a true 8-bit alpha channel; on Bria's own benchmark it ranked first on average (1.51, against 2.16 for RMBG 2.0), was preferred on 60.9 percent of images, and won the hair and fur category, while Bria states it is about 40 times bigger than its predecessor and points high-volume, low-latency work back to RMBG 2.0, a BiRefNet-based segmentation model of around 0.2B parameters. Treat the benchmark as Bria's own, not independent, and apply its routing lesson literally: RMBG 3.0 for quality-first hair and fur, BiRefNet-based RMBG 2.0 for volume, Lucida for glass and text, exactly as Phase 2 routes by edge type. Source: https://www.eachlabs.ai/blog/bria-rmbg-3-0

**Agent automation**

Write `cutout-manifest.json` beside every cut-out, with: input type (subject, selection, words, or click), segmentation model and version, edge model routed and the edge type that chose it, result form (paintable mask or new layer), local or cloud run, LayerShop version and bundled ComfyUI version, and, for cloud runs, the model name and that an API key was used (never the key itself). Fail the cut-out record if the edge-model field is empty or the bundled-version fields are empty, because Phase 3's diagnosis depends on them. Run these gates before delivery: (1) edge-suite gate, keep one probe image each for hair or fur, glass, and logo or text, run each through its routed model, and record pass or fail per probe in the manifest, so a model swap is caught by the suite rather than by a client image; (2) paintable-mask gate, assert the saved result is a mask or layer that can still be painted on, not a flattened image, by recording its layer type in the manifest; (3) slow-run diagnosis gate, on any run slower than the operator's recorded baseline for the same model, record bundled-version and speed-LoRA checks first, before any hardware conclusion, mirroring the author's comment replies in Phase 3; (4) upload gate, for local runs record "nothing uploaded" only after confirming the run used local models, and for cloud runs record which model received the image.

## The human method, distilled

1. Select by intent (subject, words, click); let the model find the boundary.
2. Route the edge by content type; never use one cut-out model for hair, glass, and logos.
3. Keep the mask paintable; the result is a layer, not a flattened cut.
4. Pin the bundled engine version; port once when upstream settles.

**Depth status:** DEPTH-LIMITED, upper end (see the note at the top).
