---
name: "blender_mcp_camera_minimax"
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

## Depth status

FULL (author's full "How I made it" post text + 17 comments).

*Inference (labeled):* the ComfyUI workflow file and prompts are linked on Google Drive (not fetched); node-level details are not verified.
