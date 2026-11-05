---
name: reshoot-4d-comfyui
description: "Reshoot any person in 4D inside ComfyUI: capture a video as 4D (motion in 3D, background, original camera path), keyframe a new virtual camera in the node editor, re-shoot along the new path with ReDirector, then photoreal-render every frame with LTX 2.3 guided by the real footage warped to the new view. Trigger when you need the same moment from a new camera angle without re-shooting."
---

# Reshoot 4D: New Camera Angles from a 4D Capture

## Purpose

This skill reconstructs the Reshoot 4D workflow, step by step, so another agent can re-shoot a person from a new camera angle inside ComfyUI the same way. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: capture a person as 4D (motion in 3D, background, original camera path), keyframe a new camera inside ComfyUI, re-shoot the video along the new path, then photoreal-render every frame guided by the real footage warped to the new view.

## Source

- Post: "Reshoot 4D: Reshoot Anyone in 4D" by itsmetamike — https://www.reddit.com/r/comfyui/comments/1xmtqu0/reshoot_4d_reshoot_anyone_in_4d/ (r/comfyui, score 22, 5 comments)
- Browser demo (no install): https://itsmetamike.github.io/reshoot-4d/demo/
- Code (AGPL-3.0) + workflow: https://github.com/itsmetamike/reshoot-4d
- Evidence: full author writeup (2026-11-04 scout run) + 5 comments. OpenSourceHiggsfield entry.

## Tools used

ComfyUI; 4D capture (quick mode for fast previews, full 4D Gaussian splat for closer direction); ReDirector (retake along the new camera path); LTX 2.3 (photoreal pass); Cseti's CrossView-Warp IC-LoRA (warps real footage to the new view); RIFE (24 → 60 fps); Blender camera interchange (.fbx / .abc / .usd import and export). Tested on one RTX 3090 (24 GB).

## AAA studio practice

- **The exact workflow, academically.** *Hybrid Cinematography* (Nhan Tran et al., Cornell + Google, 2026): "We present Hybrid Cinematography, a workflow that bridges physical capture and generative reshooting to manage hallucination risk while filmmakers can still act on it. Using an editable 3D shot plan and a proxy of the take, our previsualization evaluates hallucination risk in real time" — "built around one editable 3D shot plan that every stage reads", evaluated with seven experienced filmmakers ([arxiv.org/html/2610.12455](https://arxiv.org/html/2610.12455)). Its reshoot definition matches this skill: "Given a recorded take, these models can render the same performance from a new camera trajectory chosen or revised after capture" (intro, citing the reshooting literature). On this skill's ~30–40° limit: "a target trajectory may require rendering things that were not visible at all, or not visible in sufficient detail, in the captured trajectory, leaving parts of the shot for the model to hallucinate. We call this unrecorded demand the shot's hallucination risk." Also: "the take is always what a later stage consumes. It is never what the plan is measured against" — Reshoot 4D's splat-vs-photoreal split is the working version of that principle.
- **Camera-controlled re-render, lab-scale.** ReCamMaster (Jianhong Bai et al., Kuaishou Technology/CUHK/HUST, ICCV 2025): "a camera-controlled generative video re-rendering framework that reproduces the dynamic scene of an input video at novel camera trajectories" — trained on "136K realistic videos... with 122K different camera trajectories" generated in Unreal Engine 5 ([arxiv.org/html/2503.11647v1](https://arxiv.org/html/2503.11647v1)). Research lab, not a film studio; the anchor is the production-shaped training pipeline.
- **Splats as the cheap directing proxy in virtual production.** Magnopus: "We frequently use splats in virtual production scenarios, where invariably there are multiple cameras rendering concurrently in a single instance of Unreal" — with the discipline that the renderer "has to decide, every frame, which part to render, go and fetch it and then draw it on-screen" ([magnopus.com, 2026](https://www.magnopus.com/blog/gaussiansplats-part-3-theres-always-a-bigger-scene)). Same tiering as Reshoot 4D's quick-mode splat vs full 4D: direct on the proxy, spend on the final.
- **Camera interchange is a standards problem.** The Academy Software Foundation's USD Camera Working Group: "the cascade of interpretive pipeline dependencies on proprietary Camera rigs would be obsolesced [by a unified USD Camera schema]. Applications that are leveraging USD will be able to pick up the Camera attributes directly" ([wiki.aswf.io](https://wiki.aswf.io/display/WGUSD/USD+Camera?focusedCommentId=13492713)). Reshoot 4D's .fbx/.abc/.usd round-trip is the indie version of that handoff.
- **ILM StageCraft: cheap interactive before expensive final.** The virtual camera is tracked in real time and the engine updates the background "accordingly... Over 50% of The Mandalorian was shot in this one, virtual location reducing location shoots and chroma key (blue and greenscreen) compositing" ([boldentrance.com](https://boldentrance.com/stagecraft-ilm-the-mandalorian/)).

## Phase 1: Capture the 4D

**Do**
1. Feed in a video of one person.
2. Build the 4D capture: "their motion in 3D, the background around them, and where the original camera was and how it moved."
3. Use quick mode for fast previews; use the full 4D Gaussian splat "if you want a closer look while you direct."

**Check**
- The capture resolves the original video's camera path (commenter u/sitefall's read of the repo; the author did not confirm this in retrieved comments — treat as inference).
- Everything runs locally.

**Why**
Directing needs the scene before the camera: motion, background, and the original camera must all be known before a new path can be keyframed.

## Phase 2: Direct the virtual camera

**Do**
1. Open the 4D camera editor inside the node ("opens right inside the node, so no separate app").
2. Keyframe the camera anywhere on the timeline; look through it or step outside to see the whole scene.
3. Navigate like a DCC: Blender-style view gizmo, J/K/L shuttle, frame stepping, multi-select to move or retime keys together.
4. Set per-key camera settings: aperture, focus (in metres or locked to the subject), vignette, grain. Do rack focus and aperture pulls between keys. Alt+click in the viewport to focus on whatever is clicked.
5. Add lens looks per shot: distortion, chromatic aberration, bloom, halation, anamorphic bokeh. Keep depth and subject matte passes if comping afterwards.
6. Agent-executable: auto-generate candidate camera moves from templates (push-in, orbit, arc, crane-up with real-world filming constraints) so the node editor becomes a selector/adjuster over generated trajectories, rather than hand-keyframing every path — ReCamMaster-style rule-driven trajectory synthesis.
7. Agent-executable: write the keyframed path to one canonical camera-path file (prefer USD Camera per the ASWF working group) that capture, the node editor, ReDirector, and Blender all read/write.

**Check**
- Keys are editable after the fact: "Change those later without re-rendering. The render gets reused, so a focus tweak takes a few minutes instead of the whole pipeline again."
- Zoom keys change the lens after the render, "which makes dolly zooms work."
- Automated round-trip check: export the camera file, import it back, diff the camera matrices, alert on drift — no silent interpretation by any stage.

**Why**
Camera direction is iteration; iteration must be cheaper than rendering. Reusing the render for focus tweaks is what makes the editor a directing tool instead of a render queue.

## Phase 3: Retake and photoreal-pass

**Do**
1. Retake: "ReDirector re-shoots the whole video along your new path."
2. Photoreal pass: "LTX 2.3 renders every final frame, guided by the real footage warped to the new view (Cseti's CrossView-Warp IC-LoRA)."
3. Agent-executable: enforce the two-tier pass — a splat-only novel-view preview (real-time, free) must be auto-approved for coverage and composition before the photoreal LTX pass runs, mirroring the Magnopus/ILM cheap-before-expensive discipline.
4. Agent-executable: run a hallucination-risk gate before the expensive render, Hybrid-Cinematography-style: render the Gaussian splat along the keyframed camera path, compute per-frame observed coverage (angular deviation from the source camera, how much of the frame was actually observed), and flag frames beyond the ~30–40° working envelope as high hallucination risk — block or warn before CrossView-Warp/LTX runs. (The ~30–40° bound is this skill's own stated limit; the paper gives no degree number.)

**Check**
- Inference (labelled): u/sitefall hypothesizes ReDirector is "an older Wan fun control model" taking the camera path from the UI as input; the author did not confirm this in retrieved comments.
- Known limits (author): "Stays good within about 30 to 40 degrees of the original camera"; "Fast spins can still smear a face for a few frames."

**Why**
The splat is the directing proxy; the retake + photoreal pass is the deliverable. The warp LoRA is what keeps the new view anchored to real footage instead of hallucinating.

## Phase 4: Finish

**Do**
1. Run the finish node: 24 to 60 fps with RIFE, real motion blur from a shutter angle, upscale up to 4K, keep the original audio.
2. Bring your own camera: import an animated camera from .fbx, .abc, or .usd ("tested with Blender exports"); it "starts on the original camera at roughly real scale, lens and focus included"; files with several cameras work; export moves back out.
3. Use the settings panel at the top of the workflow for per-run changes (quality, frame rate, upscale).

**Check**
- Roughly 30 minutes per shot on one RTX 3090 (24 GB).
- Commenter u/I_just_made: the default camera panning (normal vertical axis, inverted horizontal) is "awful"; author: "Noted. Consider the fix cooking as we speak. Also try editor mode if you're wanting a bit more refinement for camera movement."

**Why**
Finishing is a separate node from directing: frame rate, motion blur, and upscale are delivery decisions, not camera decisions.

## The human method, distilled

1. Direct inside the tool, not beside it (the editor lives in the node).
2. Make iteration cheaper than rendering (settings reuse the render; focus tweaks take minutes).
3. Test interchange with the DCC people actually use (Blender-tested .fbx/.abc/.usd, both directions).
4. Ship the no-install browser demo.
5. State the angular limit plainly (30–40 degrees from the original camera).

**Depth status:** FULL (complete author writeup: tools, parameters, hardware, timings, failure modes; 5 comments).
