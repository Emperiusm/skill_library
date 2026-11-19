---
name: h3-facerefine-plus
description: "Refine faces in MiniMax H3 video with ComfyUI-H3-FaceRefine-Plus v0.2.0: one Mode dropdown picks the V1 or V2 recipe, heavy steps run on the GPU for a 2.7x speedup, default strength 0.30. Trigger when H3 faces wobble, look pasted-on, or drift in colour."
---

# FaceRefine Plus v0.2.0 for MiniMax H3

## Purpose

This skill reconstructs the exact workflow AnniCodex demonstrates for refining faces in MiniMax H3 video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: one Mode dropdown picks the whole recipe, and the heavy steps run on the GPU.

## Source

Creator: AnniCodex. Post: "FaceRefine Plus v0.2.0 for MiniMax H3: 2.7x faster, one-dropdown V1/V2 modes, stronger default" https://www.reddit.com/r/comfyui/comments/1xzvw7k/ (score 25, 5 comments; full post text and comments read) | Repo: https://github.com/AnniCodex/ComfyUI-H3-FaceRefine-Plus | Side-by-side tests: https://annicodex.github.io/FaceRefine-Plus-Tests/ | 2026-11-19 scout run, audit 4.

## Tools used

ComfyUI-H3-FaceRefine-Plus v0.2.0 (add-on pack for Carasibana's ComfyUI-H3-FaceRefine), MiniMax H3, SAM3, VOSR2.

## Phase 1: Install it the way that works today

**Do**
1. Install with git: `cd ComfyUI/custom_nodes` then `git clone https://github.com/AnniCodex/ComfyUI-H3-FaceRefine-Plus`. Version 0.2.0 is on the Comfy Registry, but the ComfyUI Manager list can take a few days to catch up and may still offer v0.1.0.
2. Already on v0.1.0 from git? Run `git pull` inside the folder and restart ComfyUI.
3. Install the dependencies: it needs the official ComfyUI-H3-FaceRefine. V2 also needs SAM3 nodes, and the `+ VOSR2` modes need ComfyUI-VOSR2.
4. Load the example workflow `examples/face_refine_plus_modes_workflow.json`.

**Check**
- Old workflows with the v0.1 labels still load.

**Why**
A Manager list that lags the release is a real install failure mode; git is the recommended path until the list catches up.

## Phase 2: Take the speed win

**Do**
1. Run the refine. The heavy steps now run on the GPU, with the same output within 1/255 of the old CPU nodes.

**Check**
- On the `mara` example (107 frames, RTX 5090, model loaders cached), a full refine went from 244 seconds to 90 seconds: 2.7x faster, +170% speed.
- A commenter asked whether the speedup holds for longer clips too; unanswered in the thread, so do not assume it without measuring.

**Why**
Moving the heavy steps to the GPU is a pure engineering win: identical output, less than half the time, no recipe change.

## Phase 3: Pick V1 or V2 from one dropdown

**Do**
1. Use the `H3 FaceRefine Plus Mode` node. It picks the whole recipe, and lazy switches run only the branch you pick.
2. **V1 (default):** the face crop is re-drawn with a prompt plus 3 reference pictures, then Stitch Plus, Flow Lock, and Tone Match. Best identity and the least wobble.
3. **V2:** a SAM3 mask on the face (or face + hair), only that part is re-drawn, character sheet only. About 1.4x faster than V1, more wobble. Optional VOSR2 pass for extra sharpness.

**Check**
- The add-on fixes three named defects in the base refiner: the refined face wobbling on the head, the pasted-on look, and colour drift.
- A commenter asked whether the V1 face crop includes the hairline, or whether V2 with the face + hair mask is the better choice when a character's bangs are a big part of her look; unanswered in the thread, so test both on a bangs-heavy clip before choosing.

**Why**
One dropdown instead of a hand-wired node graph means the recipe is a choice, not a build: V1 when identity matters most, V2 when speed matters and some wobble is acceptable.

## Phase 4: Use the stronger default

**Do**
1. Use the new default strength of 0.30 (was 0.15, which changed too little on small faces).

**Check**
- The side-by-side test page carries the before/after evidence for the strength change.

**Why**
A default that changes too little is a default that does nothing on the faces that need refining most; 0.30 is the author's calibrated answer.

## Failure modes

- **Manager still offers v0.1.0:** the ComfyUI Manager list lags the release by days. Install with git instead of waiting.
- **Wobble on V2:** V2 is faster but wobbles more. If identity stability matters, use V1.
- **Strength too weak on small faces:** that was the v0.1.0 default (0.15). v0.2.0 defaults to 0.30 for exactly this reason.
- **Bangs and hairline:** unresolved in the thread; test V1 against V2 face + hair mask on the actual clip.

## The human method, distilled

1. Prove it side by side first: the test page comes before the feature list.
2. One dropdown, one recipe: a mode switch beats a node graph nobody can reproduce.
3. Same output, faster: the GPU move is only a win because the output stays within 1/255.

**Depth status:** FULL (full post text + 5 comments, including the speed measurement, the V1/V2 recipes, and the two unanswered questions, which are recorded as open). Distinct from the cgpixel23 `minimax-h3-face-refine` workflow in the watchlist: FaceRefine Plus is AnniCodex's add-on pack for Carasibana's ComfyUI-H3-FaceRefine, not cgpixel23's 6GB VRAM workflow.
