---
name: minimax-h3-addguide-longform-automation
description: "Make 60 seconds of MiniMax H3 video on a 6 GB RTX 3050: six 260-frame shots at 864x480 and 25 steps, stitched with the H3 Add Guide node (MiniMaxH3AddGuide) carrying the last 22 frames and audio forward, driven by a Python script that queues the shots through the ComfyUI API, trims the overlaps, and encodes one MP4. 6 hours 35 minutes unattended plus about 10 minutes of setup. Includes the official six-section reference prompt format and the finish-the-audio-first rule. Trigger when a long H3 video is needed on a low-VRAM card, or when shots drift apart between segments."
---

# MiniMax H3 Add Guide Long-Form Automation (60 s on a 6 GB RTX 3050)

## Purpose

This skill reconstructs the 60-second MiniMax H3 workflow from the author's post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: generate short shots, stitch them with a 22-frame overlap, and let a script do the waiting.

## Source

Creator: No_Cow26. Reddit post:
https://www.reddit.com/r/comfyui/comments/1xtimco/this_took_x_hrs_35_mins_to_make_on_a_rtx_3050_6gb/
(r/comfyui post 1xtimco, score 251, 79 comments) | 2026-11-12 scout run, audit 3.

This is a distinct long-form method from the other H3 long-video skills in this library (`minimax-h3-selflift-long-video`, `minimax-h3-synctile-long-video`, `minimax-h3-chain-director`, `minimax-h3-longform-documentary`): it uses the native H3 Add Guide node for continuity and a Python API script for the queue, not SelfLift stitching, SyncTile nodes, or Chain Director. Do not merge them.

## Tools used

**ComfyUI** native H3 nodes, **MiniMax H3** reference-to-video, int8 quantized model, **Qwen3-VL** text encoder, **MiniMaxH3AddGuide** node, **Python** script driving the ComfyUI API. Commenter-mentioned: **Vibevoice**, **Chatterbox** (local TTS), **RefMod** (audio reference alternative), **drozbay crop-and-inpaint + SAM masking** (face repair at distance).

## Phase 1: Set up the shots

**Do**
1. Use the MiniMax H3 reference-to-video model in ComfyUI's native H3 nodes, with the int8 quantized model and the Qwen3-VL text encoder.
2. Reuse two character images in every shot to keep the characters consistent.
3. Write prompts in the official six-section reference prompt format: subject definitions, summary, retention analysis, detailed description, soundscape, music. Use no negative prompts, "because H3 doesn't use them".
4. Generate six shots of 260 frames (10.8 s each) at 864x480 and 25 steps, with the res_multistep sampler and the simple scheduler.

**Check**
- Total runtime was about 6 hours 35 minutes, unattended; setup was about 10 minutes ("Maybe 10 mins to setup let's say, that's it. Not more, not less."). If your setup takes longer than ~10 minutes, you are doing per-shot work the script should do.

**Why**
- Short shots fit the card; the overlap (next phase) is what makes them read as one video. The two reference images are the only consistency mechanism; there is no other character lock.

## Phase 2: Stitch with Add Guide

**Do**
1. Start each shot from the last 22 frames and audio of the previous one, using the H3 Add Guide node (MiniMaxH3AddGuide) at frame 0.
2. Do not re-supply the character images per shot: "I just provided the 2 character sheet. For each shots, the 22 frames from last generation is used for the continuity."

**Check**
- Commenter rguerraf asked why a 22-frame overlap between MP4s; the author's answer is the mechanism above. The overlap is the continuity; without it the shots drift apart.
- Known issues, stated by the author: soft detail, some flicker, and huge time to produce. "Still tuning."

**Why**
- The last 22 frames carry motion, framing, and audio forward. It is cheaper than generating a 60-second clip in one pass, which the card cannot do.

## Phase 3: Automate with a Python script

**Do**
1. Write a small Python script that sends the six shots to ComfyUI's API one after another, saves each result, trims the 22-frame overlaps, and encodes one 60-second MP4 with audio.
2. Start it and walk away; the author reports the run as unattended.

**Check**
- Commenter Support_Marmoset, who does the same work manually, confirms the shape: "I take days to get to this tbh, but I dont use Add Guide I make each shot myself". The script is the difference between 6h35m unattended and days of manual work.
- Support_Marmoset's own numbers for comparison: 15-second ref-to-video to 1 MP in 25 min, then a v2v upscaler with context windows to 3 MP in 30 min. Higher VRAM buys resolution, not less time: "you just use it trying to get to higher resolutions."

**Why**
- The queue is the job. The human's work is the setup; the machine's work is the waiting.

## Phase 4: Fix the audio before the video

**Do**
1. For dialogue, generate the voice first with any local TTS (commenter Support_Marmoset: "Vibevoice, Chatterbox, even MMH3 can do it. I have a workflow just for TTS.").
2. Use the finished audio as the audio reference (or refmod's, per preference). Better: make one audio file with all the dialogue for the length of the shot, and use the guide for prompting so the model uses it as given.
3. Expect garbled gibberish in the audio if you do not do this, "which MMH3 loves to do, especially with speedup loras."

**Check**
- If the audio contains words nobody wrote, the audio reference was not locked down. The fix is a single finished audio file, not a better prompt.

**Why**
- H3 invents audio when the audio reference is vague. A finished audio file turns the model from a writer into a lip-syncer.

## The human method, distilled

1. Six short shots plus a 22-frame overlap beat one long generation the card cannot run.
2. Two character images, reused everywhere; nothing else locks identity.
3. Automate the queue; the human's job is 10 minutes of setup.
4. Finish the audio first, then generate the video to it. (Commenter principle, adopted by the thread.)

**Depth status:** FULL (full post text with exact shot counts, resolution, steps, sampler, scheduler, node name, and runtime; 25 comments including the author's clarifications and Support_Marmoset's comparative numbers and TTS advice).
