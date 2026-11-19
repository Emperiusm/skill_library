---
name: h3md-director-multi-person-swap
description: "Swap up to 5 people in any live-action video with MiniMax H3 in ComfyUI: SAM3.1 tracks people by identity, Qwen Image 2.1 builds a keyframe plan at every crossing, the Director renders with the Remake LoRA. Trigger when a character swap must survive crossings, overlaps, and camera cuts."
---

# H3MD 0.5: Multi-Person Character Swap in MiniMax H3

## Purpose

This skill reconstructs the exact workflow ReferenceFluffy6159 demonstrates for swapping up to five people in one video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: find the crossing and overlap moments first and give the model a keyframe for each one, and track people by identity, not by position.

## Source

Creator: ReferenceFluffy6159. Post: "Put yourself into any dance video – swap up to 5 people at once, 100% local (MiniMax H3 + ComfyUI)" https://www.reddit.com/r/comfyui/comments/1xzrra6/ (score 38, 8 comments, including the author's two detailed replies; full post text and comments read) | Workflows (free): https://civitai.com/models/3037225?modelVersionId=3478241 | Nodes: https://github.com/1113800942/comfy-h3md-director | Walkthrough (Chinese voice, English subtitles): https://youtu.be/WMQJjmHZikc | 2026-11-19 scout run, audit 3.

## Tools used

MiniMax H3, ComfyUI, comfy-h3md-director nodes (H3MD 0.5), Qwen Image 2.1, SAM3.1, Remake LoRA, VOSR2. 100% local.

## Phase 1: Build the keyframe plan

**Do**
1. Drag in the source video. Add one picture per character.
2. Write "picture 1 → left 2" and one description line per person.
3. Let the workflow track the people with SAM3.1, pick the moments where they cross or overlap, redraw just those people, and pack everything into a plan. The keyframe step uses Qwen Image 2.1 edit, 2 steps. About 2.5 minutes for a 26-second clip.

**Check**
- People are numbered left to right in the first frame where everyone is visible.
- Every swapped person needs at least one large, clear keyframe (medium shot, face visible), with one keyframe per camera shot.

**Why**
H3 gets confused when people cross or overlap: it puts the new face on the wrong person, or one person ends up in another's clothes. The fix is to find those moments first and give the model a keyframe for each one, instead of hoping the model keeps identities straight on its own.

## Phase 2: Render the swap

**Do**
1. Let the Director render the swap with the Remake LoRA, with the source's own sound locked.
2. Budget the render: a 26-second clip took 29 minutes on an RTX 5090.
3. Observe the resolution lock: Remake only works at 1664×960 / 960×1664 (or 2560×1472). Version 0.5.5 switches to it automatically.

**Check**
- In the demo, three of five dancers were swapped for the author's own characters and the other two were left untouched.
- In the author's test, two people crossed twice and every identity stayed correct. Crossing paths, swapping places, leaving and re-entering frame, and camera cuts are all fine (author's claim).

**Why**
Identity tracking, not position tracking, is what survives a crossing: a person who leaves the frame and comes back on the other side is still the same person, and the render must not reassign them.

## Phase 3: Fix small faces in wide shots

**Do**
1. For small faces (50–100 px), redraw them with H3 inside a SAM3 head mask, then run VOSR2.
2. Keep faces out of very wide shots if you can.

**Check**
- The result is much clearer, but not perfectly sharp (author's own caveat).

**Why**
A face that is 50 pixels in the source has no identity to preserve; redrawing it inside a head mask is the only way to give the refiner something to work with.

## Phase 4: Respect the limits

**Do**
1. Do not use it where people stack too close together, where a big person is swapped for a much smaller one, or where long pony hair is swapped for short hair. Those are the author's stated limits.
2. Write the description line carefully: without a prompt enhancer, the edit model follows your text. One simple line per person is enough, but if the line contradicts the picture (wrong gender, ethnicity, or clothes), you get the wrong person.
3. Remember it is not limited to dance videos: "Remake swap works on any live-action clip" (author's reply).

**Check**
- If the swap produces the wrong person, check the description line against the picture first: a contradiction there is the most likely cause.

**Why**
The failure mode is a contradiction between the picture and the text: the model follows the text, so a wrong line overrides a right picture.

## Failure modes

- **Identity swap on crossings:** the model puts the wrong face on a person or the wrong clothes on a body. The fix is a keyframe at every crossing and overlap, not a better prompt.
- **Wrong person from a contradicting description line:** one line per person must agree with that person's picture (gender, ethnicity, clothes).
- **Blurry faces in wide shots:** faces at 50–100 px need the H3-in-SAM3-mask redraw plus VOSR2; even then, keep faces out of very wide shots.
- **Stacked people, big-to-small swaps, long-to-short hair:** stated limits of version 0.5; do not expect the workflow to handle them.

## The human method, distilled

1. Find the hard moments first: keyframes go on the crossings and overlaps, not on the easy stretches.
2. Track identity, not position: numbering left-to-right in the first full frame is what makes crossings survivable.
3. One simple line per person, and it must agree with the picture.

**Depth status:** FULL (full post text + 8 comments, including the author's detailed replies on identity tracking, keyframes, and limits; the native clip is the before/after demo of the same workflow). Distinct from `minimax-h3-character-swap-comfyui`, `minimax-h3-character-swap-nomask-lowvram`, and `minimax-h3-reference-video-character-swap`: H3MD is a different tool (comfy-h3md-director) with a keyframe-plan step and identity tracking for up to five people at once.
