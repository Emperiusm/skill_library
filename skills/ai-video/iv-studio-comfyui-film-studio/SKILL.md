---
name: iv-studio-comfyui-film-studio
description: "Direct AI short films without touching a node graph: drive your own ComfyUI over its API with IV Studio — an agent writes the MiniMax H3 prompt from references, a checker fixes what H3 punishes, hunt cheap 0.4-0.9 MP previews ranked three ways, finish the pick from the same latent, and block camera moves on a staging board that renders a grey previs clip H3 follows. Trigger when producing AI video where prompt quality, take selection, and camera control are the bottlenecks."
---

# IV Studio: Directing ComfyUI Without the Node Graph

## Purpose

This skill reconstructs the IV Studio film-studio workflow, step by step, so another agent can direct AI video through a ComfyUI API the same way. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: drive your own ComfyUI over its API so you never touch a node graph — an agent writes the H3 prompt from references, a checker fixes what H3 punishes, previews are hunted and ranked, the pick finishes from the same latent, and a staging board turns blocking into exact screen directions or a grey previs clip that H3 follows.

## Source

- Post: "I built a free, open-source film studio on top of ComfyUI + MiniMax H3: idea to finished short film, on your own PC" by itsVariance — https://www.reddit.com/r/comfyui/comments/1xmp6dh/i_built_a_free_opensource_film_studio_on_top_of/ (r/comfyui, score 202, 29 comments)
- Code (MIT): https://github.com/hollisorg/iv-studio — Download: https://github.com/hollisorg/iv-studio/releases/latest
- Evidence: full author writeup + detailed previs explanation + 29 comments (2026-11-04 scout run). Was DEPTH-LIMITED on 2026-11-03 (post body blocked, 1 comment); upgraded today.

## Tools used

IV Studio (Windows desktop app, MIT); ComfyUI (driven over its API); MiniMax H3 (video); Qwen3-VL via Ollama or an AI agent via MCP (prompt writing); OpenAI Whisper (take ranking); DLSS 5 or SeedVR2 (finish upscale); SAM 3.1 (cut-out); MiniMax Music 3 / ACE-Step (music); VoxCPM2 (local voices); Civitai LoRAs; three.js headless browser + ffmpeg (previs); RunPod / Modal (cloud GPU with idle shutoff); 142-tool MCP server. Tested on RTX 4090 + 64 GB RAM; 16 GB cards work with smaller previews; every model downloads from its host with SHA-256 verification.

## Phase 1: Let the agent write the prompt

**Do**
1. "Write it for me": a local model (Qwen3-VL via Ollama, or your AI agent through MCP) looks at reference pictures and writes the H3 prompt.
2. Run the checker: it "catches the mistakes H3 punishes (frame-grid lengths, speaker tags, unattached references) and fixes most in one click."

**Check**
- Commenter u/bumredeemer: "the frame grids is my biggest gripe about h3" — the checker is the answer to the most common H3 complaint.

**Why**
Prompt for the model's failure modes, not its strengths: the checker encodes what H3 punishes.

## Phase 2: Hunt, then finish

**Do**
1. "Hunt, then finish: quick previews with live step pictures."
2. Rank takes "by what OpenAI Whisper hears, likeness and sharpness."
3. "A review names each problem with its timestamp."
4. "The pick finishes from the same latent with DLSS 5 or SeedVR2." The author's rule: "It does individual generations at low mp (0.4 to 0.9) and then upscales them from there for better and quicker iteration and results."

**Check**
- Previews stay at 0.4–0.9 MP; only the picked take pays the upscale cost.

**Why**
Hunt cheap, finish once: ranking three ways (audio, likeness, sharpness) before committing the expensive pass.

## Phase 3: Structure the film

**Do**
1. Projects: "a six-step wizard from idea to short film (script, cast, storyboard sketches you can play as an animatic)."
2. "Every shot is filmed from its sketch, so faces and rooms stay consistent."

**Check**
- The sketch is playable as an animatic before any generation is spent.

**Why**
The sketch is the consistency contract: faces and rooms are locked before the model ever sees the shot.

## Phase 4: Block on the staging board

**Do**
1. "Staging board: place people and the camera on a top-down floor plan; it becomes exact screen directions, or a grey previs clip H3 follows for arcing moves."
2. Build the previs in-app ("The previs is built into the app, no Blender needed"): block the shot on the top-down board — up to four people, each one's facing, gaze target, and walk path; camera lens, height, and move (push, pan, track, arc).
3. Render the previs "in motion as grey mannequins on a plain floor" with three.js in a headless browser + ffmpeg: "about 3 to 5 seconds a clip."
4. Feed the clip into MiniMax H3's reference-to-video mode as `<Video 1>`, alongside the character and location pictures. "The prompt tells H3 the previs only sets camera and blocking, so it keeps the motion and framing but doesn't copy the grey look."

**Check**
- Author's honest finding: "it really pays off on arcs and orbits around characters. H3 struggl[es]..." — truncated in the retrieved comment; the struggle is named but its object is not. Treat the truncation as a known unknown.

**Why**
A grey previs the model is told not to copy is the cleanest way to direct camera motion: blocking without style contamination.

## Phase 5: Edit the footage, not the graph

**Do**
1. "An editor that makes footage: right-click to extend a shot, fill a gap, retake a line, cut someone out (SAM 3.1) or reframe to vertical."
2. "Also in there: character LoRA training, Replace (Genjutsu Level), music (MiniMax Music 3 / ACE-Step), local voices (VoxCPM2), Civitai LoRAs."
3. Direct alongside the agent: "a 142-tool MCP server so Claude Code or any agent can direct alongside you."
4. Without a strong GPU: "render on your own Runpod or Modal account and shuts the GPU off when idle" (the Runpod path is "brand new, so feedback is welcome").

**Check**
- Every model "downloads from its host and checks its SHA-256."
- Open questions from the comments: full-film re-render from the workflow (u/VeryLiteralPerson, u/fevenis — no author answer captured); Linux support (asked twice, unanswered — Windows-only per the post); Ollama on a non-localhost address for podman (author: "Should be out in an update here in the next hour"); single-video generations (author: "Yes it can! There is a timer to make it automatic").

**Why**
The app is a director's console, not a node editor: edit footage, verify downloads, and let the GPU bill stop when idle.

## The human method, distilled

1. The API is the product (drive ComfyUI; never touch the node graph unless you want to).
2. Check what the model punishes (H3-specific checker, one-click fixes for frame grids, speaker tags, unattached references).
3. Hunt cheap, finish once (0.4–0.9 MP previews ranked three ways; finish from the same latent).
4. Previs the model can follow (grey mannequins + "don't copy the grey look" prompt).
5. Verify downloads (SHA-256 on every model).
6. Report the honest finding (arcs/orbits pay off; H3 struggles — truncated).

**Depth status:** FULL (complete author writeup + detailed previs explanation + 29 comments). Inference: H3's struggle object is truncated in the retrieved comment; Linux support unanswered.
