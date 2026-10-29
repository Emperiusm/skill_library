---
name: freefield-comfyui-higgsfield-clone
description: "Rebuild a closed AI product as ComfyUI apps: one folder per app (app.json + API workflow), UI/downloads/VRAM map/tests generated from those files, and a fixed-seed lab that publishes one example per app with real time and peak VRAM. Trigger when productizing a ComfyUI workflow bundle or cloning a vendor toolset with open weights."
---

# Freefield: Higgsfield Rebuilt on ComfyUI (117 Apps, Open Weights Only)

## Purpose

This skill reconstructs the Freefield workflow, step by step, so another agent can build a product-sized ComfyUI bundle the same way. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: one file format generates everything downstream, and a fixed-seed lab proves every app before it ships.

## Source

- Post: "Freefield: Higgsfield rebuilt on ComfyUI, 117 apps, open weights only (MIT)" by neuregex — https://www.reddit.com/r/comfyui/comments/1xh73t4/ (score 239, 19 comments, 20 retrieved)
- Code: https://github.com/neuregex/freefield
- Demo: https://youtu.be/N7mv2v3Txeo
- Evidence: full post text + author comments, 2026-10-28 scout run. Per-app workflow JSON was not inspected; per-app node settings are not claimed here.

## Tools used

ComfyUI + Comfy SDK (host), FLUX 3 Klein (Create Image), MiniMax H3 (Create Video, Extend Video), LTX-2.5, Wan 2.1 and 2.2, Qwen-Image-Edit, Z-Image, SeedVR2, Stable Audio 3, MiniMax Music 3 (open-weights roster, no API nodes). Hosting: Modal (L40S or H100) or any ComfyUI instance. License: MIT. The demo video's soundtrack was made in Freefield with MiniMax Music 3.

## Phase 1: Cover the product surface app by app

**Do**
1. Enumerate the target product's tools and apps. Higgsfield shows 129; Freefield covers 95 of them with 117 apps (image, video, VFX, audio).
2. Include the headline apps: Create Image with FLUX 3 Klein; Cinema Studio (a still, or a shot from that still with Higgsfield's 33 camera moves); Create Video and Extend Video with MiniMax H3; Re-shoot (a new camera angle on a clip already shot); Relight; Effects (24 LoRAs); Morph; Mixed Media; Dub; Face Swap; Depth Map; Video Background Remover; Inpaint with a brush; Photodump; Moodboard; and 72 template apps such as an AI Influencer builder, Packshot, Bullet Time, or Victory Card.
3. Use open weights only, no API nodes.

**Check**
- Count apps against the target's list: 117 apps, 95 of 129 covered. Coverage is partial by the author's own count, not total.

**Why**
A product is a bundle of small tools, not one mega-workflow. App-by-app coverage keeps each piece shippable and testable on its own, and makes the missing 34 apps a visible backlog instead of a vague gap.

## Phase 2: Make every app one folder, generated from one format

**Do**
1. Each app is one folder: an `app.json` plus a ComfyUI workflow in API format.
2. Generate the web UI, the model downloads, the VRAM map, and the tests from those files, not by hand.
3. Convert any other ComfyUI workflow into a draft app with one command: `tools/import_workflow.py`.
4. Chain apps with "Use in...": send a result to another app (author's example: an AI Influencer portrait to Image to Video).

**Check**
- A new workflow becomes a draft app with one command; the UI, download list, VRAM map, and tests all regenerate from the app files.

**Why**
The format is the product. When UI, downloads, VRAM guidance, and tests all derive from `app.json` + workflow, adding app 118 costs one folder, not a rewrite, and four copies of the same facts can never drift apart.

## Phase 3: Prove each app in the lab with fixed seeds

**Do**
1. Run every app on a GPU with fixed seeds; publish one example per app with its real time and peak VRAM.
2. Record the lab totals: 48 runs, 710 of 733 cases ok.
3. Let the lab pick the image model, not taste: six prompts on five open models with the same seed; FLUX 3 Klein followed them best.
4. Fix failures in batches: "I built a flagging system that every example that came out wrong got flagged, then I collected the flags and fixed them in batches, and kept repeating that until they all gave good results." (neuregex, comment)
5. Install note from a commenter (KeyTumbleweed5903): "it downloads everything u need - u may need to get a hugging face token"; the same commenter reports it installed without issues and worked on first tries.

**Check**
- Every app has a published example, a real time, and a peak VRAM figure; the lab pass rate is a number (710/733), not an impression.

**Why**
Fixed seeds turn "it worked once" into a repeatable claim, and batch flag-fixing turns QA from a chore into a loop that converges. This is the acceptance-spec pattern: what good means, measured, per app.

## Phase 4: Ship on rented GPU or any ComfyUI, with a VRAM map

**Do**
1. Run on Modal (L40S or H100) or point Freefield at any ComfyUI.
2. Read the docs' VRAM map for what fits on a 24 GB card before running.

**Check**
- The docs answer "does this app fit my card?" before the run starts; the installer pulls its own models (plus a Hugging Face token where gated).

**Why**
A 117-app bundle that only runs on one machine is a demo. A VRAM map plus a Modal-or-local choice makes it a tool other people can actually run.

## AAA studio practice

- **Test with every check-in, and tier the suite by speed.** Rare's Sea of Thieves practice, presented at GDC 2019, required testing with every check-in, ran a core set of tests before every check-in and longer-running tests periodically, and ran the full suite multiple times across platforms and configurations (shipping and debug). The studio reported about 10,000 tests run remotely via TeamCity. Applied here: Freefield's 117-app lab is the analogue of that full suite, and it needs a fast core tier (a subset of apps on every change) plus the full lab periodically, not an all-or-nothing lab that only runs when someone remembers.
  Source: https://docslib.org/download/1319348/automated-testing-for-multiplayer-game-ai-in-sea-of-thieves
- **One asset definition is the product, not the pile of outputs.** SideFX's Houdini Digital Assets practice wraps a larger network into a single digital asset node with an artist-friendly interface, so a team reuses one controlled definition instead of hand-maintaining copies. Freefield's `app.json` + workflow plays the same role for a ComfyUI bundle: the definition is the source, and the UI, downloads, VRAM map, and tests are generated from it, never edited by hand.
  Source: https://www.sidefx.com/tutorials/houdini-digital-assets/
- **Ship the workflow as versioned, API-submittable JSON.** ComfyUI's API pattern is that the web UI POSTs a workflow JSON to `/prompt` with a client id, and the caller polls `/history/{prompt_id}` until outputs appear. That makes a workflow a submittable artifact an agent or CI job can run headlessly, which is the precondition for Freefield's lab to be automated rather than clicked through.
  Source: https://www.runflow.io/blog/comfyui-workflow-tutorial

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Add a `check_app.py` gate that runs on every change to an app folder and fails the change if any of these drift: the app folder lacks `app.json` or an API-format workflow; the generated UI, model-download list, VRAM map, or test file does not regenerate byte-identically from those two files; or the app has no published fixed-seed example with real time and peak VRAM.
2. Tier the lab Rare-style: a core set (one app per category: image, video, VFX, audio, plus any app changed in the commit) runs on every change; the full 117-app lab runs on a schedule and before any release, and its pass rate (like the author's 710/733) is recorded per run, not per impression.
3. Record a `lab-run.json` per lab run: date, app count, pass count, failed app names, and the fixed seeds used, so a regression names the app and the seed that broke.

**Check**
- A new app is shippable only when `check_app.py` passes and its fixed-seed example exists with time and VRAM; an app with a hand-edited UI file fails the gate even if it renders.
- A lab run is reportable only with its pass count and failed-app list; "the lab is green" without numbers is not a report.

**Why**
Freefield's claim is product-sized coverage (117 apps), and coverage claims rot the moment generated files drift from their definitions. A regeneration gate plus a tiered lab keeps the bundle's 117-app number honest at the same scale Rare keeps a live game's build honest.

## The human method, distilled

1. Take a vendor's "open source" claim literally and rebuild the whole surface, not one app.
2. One file format generates everything downstream; never hand-maintain four copies of the same facts.
3. Flag every bad example, fix in batches, repeat until the lab is green; publish the pass rate.
4. Pick models by same-seed shootout, not by announcement hype.

## Depth status

FULL — full post text, 20 comments including the author's QA method, model roster, lab numbers, and install reports. The demo video itself was not transcribed, and no per-app workflow JSON was inspected, so per-app node settings are not claimed.
