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

**Check**
- Keys are editable after the fact: "Change those later without re-rendering. The render gets reused, so a focus tweak takes a few minutes instead of the whole pipeline again."
- Zoom keys change the lens after the render, "which makes dolly zooms work."

**Why**
Camera direction is iteration; iteration must be cheaper than rendering. Reusing the render for focus tweaks is what makes the editor a directing tool instead of a render queue.

## Phase 3: Retake and photoreal-pass

**Do**
1. Retake: "ReDirector re-shoots the whole video along your new path."
2. Photoreal pass: "LTX 2.3 renders every final frame, guided by the real footage warped to the new view (Cseti's CrossView-Warp IC-LoRA)."

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
