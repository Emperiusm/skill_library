---
name: blender-mcp-camera-minimax
description: "Direct AI video camera moves in 3D first: block the move with Codex CLI plus Blender MCP, render a reference clip, assign role-based inputs in MiniMax H3 reference-to-video. Trigger when AI video needs a deliberate camera move."
---

# Blender MCP Camera Blocking for MiniMax H3 Reference-to-Video

## Purpose

This audit reconstructs the exact workflow in the author's words ("How I made it"), step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: author the camera move in a 3D package where you can see it, then give the AI model explicit per-input roles.

## Source

Creator: Time-Ad-7720

Source: https://www.reddit.com/r/comfyui/comments/1wqybjk/ (native Reddit video, r/comfyui post 1wqybjk, score 224, 17 comments) | 2026-09-28 scout run

## Tools used

Tools used: Blender (mannequin scene + camera animation); Blender MCP via Codex CLI (agentic Blender control); ComfyUI with MiniMax H3 reference-to-video workflow. Hardware reported: RTX 5070 Ti, 32 GB RAM.

## Phase 1: Block the camera move in Blender with MCP

**Do**
1. Use Codex CLI with Blender MCP to build a simple mannequin scene and animate the camera (author suggests it takes ~2 minutes to block and iterate a move).
2. Keep the body planted while the head and eyes follow the lens.
3. Refine: mostly waist-up, fast eased transitions, short holds, one extreme closeup near the end. The sequence returns to its opening composition (loops).

**Check**
- Scrub the viewport: does the move feel wrong? Fix it before any generation.

**Why**
- (from commenter Ok-Fennel6578, affirmed by author): "You can block the move in 2 minutes, see if it feels wrong, fix it, then let H3 worry about the actual image. Way less lottery-ticket directing." Prompt language cannot describe a dolly path; a viewport can.

## Phase 2: Render the reference clip

**Do**
1. Render the Blender reference at **1080 x 1080, 30 fps, five seconds**.

**Check**
- The clip is the ground truth for camera motion only; image quality is irrelevant.

**Why**
- Separates "the camera move" from "the image" as independent inputs.

## Phase 3: Assign roles in ComfyUI

**Do**
1. Load the mannequin clip + a character reference sheet + a waterfront background image into MiniMax H3's reference-to-video workflow in ComfyUI.
2. Write a prompt that assigns each input its role: character, environment, or camera motion.
3. Generation settings: 20 steps at ~53 s/iteration, 0.6 resolution setting, 1:1 aspect ratio, no turbo LoRA. ~17 min 40 s for sampling at the reported rate.

**Check**
- Verify identity drift, framing changes, background consistency, and the loop seam against the Blender reference.

**Why**
- Role-assigned inputs beat descriptive prompting for multi-constraint shots; the commenters confirm 3+ characters cause bleed/cloning, so keep reference counts low and characters distinct.

## The human method, distilled

1. Direct the camera in 3D, generate the image in AI, never the reverse.
2. Check the four failure modes on every output: identity drift, framing changes, background consistency, loop seam.

## AAA studio practice

Camera-first directing is standard AAA cinematics practice; this skill's
Blender blocking plus AI rendering is the indie form of it.

1. **Camera as an independent data stream.** Ninja Theory's SIGGRAPH 2016
   "real-time cinematography" on *Hellblade: Senua's Sacrifice*: a scene
   shot, edited, and rendered live in front of an audience in under ten
   minutes, with camera motion and focus captured as their own stream played
   back against performances in UE4 Sequencer. Camera path as an independent
   input, not baked into footage.
   - Sources: https://blog.siggraph.org/2016/10/ninja-theory-epic-games-talk-hellblade-future-real-time.html/;
     https://www.fxguide.com/fxfeatured/epic-win-previs-to-final-in-five-minutes/
2. **Lock the camera before spending money.** Naughty Dog (GDC 2017): *all*
   cinematic scenes start in previs; digital previz (crude models) plans
   camera angles, sets, and movement before any rendering, and the mocap
   stage physically recreates in-game geometry because stage time is
   expensive.
   - Source: https://gamesbeat.com/how-planning-and-technology-helped-naughty-dog-animate-uncharted-4-a-thiefs-end/
3. **The camera as a physical film camera.** Santa Monica Studio, *God of
   War* (2018): zero camera cuts mandated across gameplay and cinematics; DP
   Dori Arazi tuned the virtual mocap equipment like a documentary camera,
   and where mocap was impossible animators hand-blocked staging with
   untextured models (GDC 2019).
   - Source: https://sms.playstation.com/stories/evolving-our-tech-building-powerful-and-unique-game-talented-creatives
4. **The vendor-standard workflow.** Epic's Animation Field Guide: realtime
   pipelines begin with blocking and layout in Sequencer with low-resolution
   stand-ins, then each asset is replaced with a final version as work
   progresses.
   - Source: http://acaa.work/resources/guide.pdf
5. **Camera-first is a formal role.** Skydance's Senior Cinematics Camera
   Layout Artist (*Marvel 1943: Rise of Hydra*) operates the virtual camera
   at performance-capture shoots and edits cameras in Maya and Unreal.
   - Sources: https://up2staff.com/santa-artist-seattle-angeles-los-valley-at-skydance;
     https://www.aivanet.com/2024/03/unreal-engine-just-demoed-film-quality-visuals-running-in-real-time/
6. **Camera as a separate pass.** An 80 Level artist interview documents
   capturing the performance first, then "shooting" the cameras as a later
   pass (5-6 angles), authoring them in Maya, and syncing into Sequencer.
   - Source: https://80.lv/articles/integrating-real-time-rendering-into-film-production-pipeline/

### Agent-executable automation upgrades (from AAA practice)

- **Export the camera path as data.** Export the Blender camera animation
  (FBX or Alembic) alongside the reference clip; keep it as the ground-truth
  move for any re-render in any tool. (AAA form: Ninja Theory's camera as an
  independent stream; Epic's Sequencer layout.)
- **Automate the four failure checks.** *Inference (labeled):* these are
  standard computer-vision metrics assembled here, not cited studio
  automation. Compute per-output deltas against the reference: identity
  embedding distance (identity drift), camera-path correlation from frame
  homography (framing changes), background similarity outside the subject
  mask (background consistency), and first-frame vs last-frame match (loop
  seam). An agent runs the numbers; the human still judges intent.
- **Shoot the move twice.** Render two blocking variants (e.g. wide vs
  tight) before any generation, mirroring the 5-6-angle coverage pass; pick
  the move, then spend the generation budget. (AAA form: 80 Level's separate
  camera pass.)

## Depth status

FULL (author's full "How I made it" post text + 17 comments).

*Inference (labeled):* the ComfyUI workflow file and prompts are linked on Google Drive (not fetched); node-level details are not verified.
