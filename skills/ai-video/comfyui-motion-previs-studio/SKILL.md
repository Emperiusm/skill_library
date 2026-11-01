---
name: comfyui-motion-previs-studio
description: "Block shots in 3D before generating: dual-viewport local previs studio with camera moves, procedural character animation, a 24fps keyframe timeline, and control-pass export (OpenPose, depth, alpha, camera matrices) into ComfyUI's MiniMax H3 Ref2VA. Trigger when AI video needs precise camera and blocking control instead of prompt retries."
---

# ComfyUI Motion Previs Studio: 3D Camera Blocking Into AI Video

## Purpose

This skill runs navarisun's open-source, local-first interactive 3D
previsualization studio alongside ComfyUI: direct the scene in 3D first
(camera + blocking + keyframes), then send deterministic control
passes into generation. Never prompt blind. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: **block the scene
in 3D, keyframe on a 24fps timeline, export control passes, and only
then generate through ComfyUI.**

## Source

r/comfyui, navarisun, "ComfyUI Motion Previs Studio, 3D Camera
Blocking, Character Animation, Open" (score 39, 2 comments, 2026-10-30):

- https://www.reddit.com/r/comfyui/comments/1xjr2ia/
- Native Reddit video: v.redd.it/u1jw4i5q2oyh1

Evidence note: all facts below are the author's claims from the full
post text (3,881 chars). The two comments add only a use-case
endorsement (music videos). No third-party verification in this audit.

## Tools used

- Open-source, local-first interactive 3D previsualization studio
  (designed to work alongside ComfyUI)
- Dual 3D viewports: free-orbit scene editor + live cinematic camera
  viewfinder
- Camera control: dolly, orbit, tracking, crane, handheld, whip pan,
  customizable trajectories
- Character animation: procedural walking, running, jumping, combat
  actions, gestures; interactive FK/IK bone posing
- Scene building: 3D environments, props, lighting rigs,
  reference-image-based scene configuration
- Cinematic framing: adjustable focal lengths, depth of field, aspect
  ratios, shot composition
- 24fps timeline with camera and character keyframes
- Control passes: MP4 previsualization, OpenPose skeletons, depth maps,
  alpha masks, camera transformation matrices
- AI integration: local Ollama/LM Studio models or cloud models for
  natural-language scene direction and reference analysis
- ComfyUI API bridge for a MiniMax H3 Ref2VA workflow
- Target video models with reference inputs: LTX-2.5, MiniMax H3,
  Seedance

## Phase 1: Build the scene in 3D

**Do**
1. Assemble the environment, props, and lighting rigs in the
   free-orbit scene editor. Use reference-image-based scene
   configuration to match a target look.
2. Block character positions with procedural animation presets (walk,
   run, jump, combat, gestures) or pose bones directly with FK/IK.
3. Set focal length, depth of field, and aspect ratio per shot. Watch
   the live cinematic camera viewfinder alongside the editor.

**Check**
- The viewfinder shows the exact framing the video model will be asked
  to match.

**Why**
"We have increasingly powerful video generation models, but precise
control over camera movement, character blocking, spatial composition,
and action choreography is still challenging." 3D blocking is the
control mechanism prompts cannot provide.

## Phase 2: Keyframe on the 24fps timeline

**Do**
1. Keyframe camera moves (dolly, orbit, tracking, crane, handheld, whip
   pan, custom trajectories) and character animation on the 24fps
   timeline.
2. Plan every shot before any generation happens.

**Check**
- Scrub the timeline; camera and character motion read correctly in
  the viewfinder at 24fps.

**Why**
Previs is shot planning, not generation. The timeline is the contract
the later generations must honor.

## Phase 3: Export control passes

**Do**
1. Export the MP4 previsualization, OpenPose skeletons, depth maps,
   alpha masks, and camera transformation matrices.
2. Optionally use Ollama/LM Studio or cloud models for
   natural-language scene direction and reference analysis.

**Check**
- Each control pass (depth, pose, mask, camera matrix) matches the
  timeline frames 1:1.

**Why**
Control passes are the deterministic bridge between the 3D block and
the stochastic video model. The studio's output is structured data,
not just a video.

## Phase 4: Generate through ComfyUI

**Do**
1. Submit the previs video and reference images to ComfyUI through the
   direct local API bridge (implemented for the MiniMax H3 Ref2VA
   workflow).
2. View the generated result back in the studio.
3. Follow the studio's target pipeline: 3D Scene → Camera & Character
   Animation → Control Passes → ComfyUI → AI Video.

**Check**
- The generated shot matches the previs camera move and blocking.
  Where it drifts, adjust the 3D scene, not the prompt.

**Why**
"The whole goal is to escape that prompt spiral of endless retries and
bad takes, and instead block out the scene first, direct the camera
properly, and then send a much clearer setup into generation." The
author adds, replying to a music-video use case: "Music videos are a
perfect fit for this, especially when camera motion and shot planning
really matter."

## AAA studio practice

- ILM runs a dedicated Previz department (alongside techvis and
  postvis) whose stated mission is a "technically and aesthetically
  sound roadmap to production ... resulting in a clear creative directive
  and fewer iterations in post". Previs data is the upstream contract,
  exactly as this skill treats the 24fps timeline as the contract
  generation must honor.
  https://www.ilm.com/visual-development/
- Previs houses routinely convert previs data into physical shoot
  control: previs is used for "programming practical camera and stunt
  rigs," with techvis documenting "detailed camera and shooting details
  through diagrams or QuickTime movies" (previs supervisors at Halon
  Entertainment, Proof, MPC, Stargate Studios, and The Third Floor,
  speaking to CGW). The skill's camera-matrix export is the low-cost
  version of the same pipeline: machine-readable camera data, not just a
  video.
  https://www.cgw.com/Publications/CGW/2017/Volume-40-Issue-3-May-Jun-2017-/Planning-Process.aspx
- Gearbox Software (Borderlands) treats mocap as a previz instrument:
  "It's perfect for previz. Animators can hop in, capture a performance,
  and we can visualise how it fits into a cinematic or gameplay moment
  within the same day." Markerless capture collapsed a 30-40 minute
  marker-setup/calibration session into a full capture session in the
  same window, with data delivered to animators in under two hours
  (Vicon fireside chat with Gearbox's motion capture lead, GDC 2025).
  This is the professional precedent for the skill's procedural/FK/IK
  blocking presets: cheap, fast blocking motion used to decide camera
  and timing, never the final performance.
  https://www.vicon.com/resources/blog/vicon-markerless-helps-gearbox-studios-create-better-games-gdc-2025/
- ILM's virtual-production toolset gives filmmakers "intuitive virtual
  cameras" operated like on-set gear: handheld, dolly, crane, Steadicam,
  traditional wheels. The skill's camera vocabulary (dolly, orbit,
  tracking, crane, handheld, whip pan) mirrors the move set a working DP
  reaches for. Inference: build trajectories from that vocabulary rather
  than freeform curves when the goal is production camera language.
  https://www.ilm.com/visual-development/

## Agent automation

- Export manifest: after Phase 3, write `previs-manifest.json` listing
  every exported pass (MP4 preview, OpenPose, depth, alpha, camera
  matrices) with per-frame file naming. An agent generates this
  manifest mechanically and must refuse to start Phase 4 while any
  listed pass is missing.
- Alignment gate: programmatically verify frame counts match across all
  passes and equal the timeline length at 24fps (frames = seconds x 24),
  and that camera matrices parse as one 4x4 float matrix per frame.
  Fix failures in the 3D scene; never hand-edit pass files.
- Drift log: after each Phase 4 generation, append one line to
  `drift-log.md`: shot id, what drifted (camera / blocking / timing),
  and whether the fix was a scene change or a workflow tweak.
  Inference: cap regeneration retries (three attempts is a reasonable
  ceiling) before returning to re-blocking, so the loop cannot become
  the prompt spiral the tool exists to escape.

## The human method, distilled

1. **Block in 3D before generating a single frame.**
2. **Export deterministic control passes** (pose/depth/mask/camera
   matrices) as the interface to the video model.
3. **Iterate on the scene, not the prompt.**

**Depth status:** FULL (detailed author post text; the two comments add
only a use-case endorsement).
