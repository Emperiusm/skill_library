---
name: iv-studio-comfyui-film-studio
description: "Direct AI short films without touching a node graph: drive your own ComfyUI over its API with IV Studio — an agent writes the MiniMax H3 prompt from references, a checker fixes what H3 punishes, hunt cheap 0.4-0.9 MP previews ranked three ways, finish the pick from the same latent, and block camera moves on a staging board that renders a grey previs clip H3 follows. Trigger when producing AI video where prompt quality, take selection, and camera control are the bottlenecks."
---

# IV Studio: Directing ComfyUI Without the Node Graph

## Purpose

This skill reconstructs the IV Studio film-studio workflow, step by step, so another agent can direct AI video through a ComfyUI API the same way. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: drive your own ComfyUI over its API so you never touch a node graph — an agent writes the H3 prompt from references, a checker fixes what H3 punishes, previews are hunted and ranked, the pick finishes from the same latent, and a staging board turns blocking into exact screen directions or a grey previs clip that H3 follows.

## Source

- Post: "I built a free, open-source film studio on top of ComfyUI + MiniMax H3: idea to finished short film, on your own PC" by itsVariance — https://www.reddit.com/r/comfyui/comments/1xmp6dh/i_built_a_free_opensource_film_studio_on_top_of/ (r/comfyui, score 202, 29 comments)
- 1.0 update post: "IV Studio 1.0: I rebuilt my free, open-source film studio for ComfyUI + MiniMax H3 from your comments (now on Linux and Mac)" by itsVariance — https://www.reddit.com/r/comfyui/comments/1xqfux1/iv_studio_10_i_rebuilt_my_free_opensource_film/ (r/comfyui, score 60, 9 comments, 8 retrieved) | 2026-11-08 scout run
- Code (MIT): https://github.com/hollisorg/iv-studio — Download: https://github.com/hollisorg/iv-studio/releases/latest
- Evidence: full author writeup + detailed previs explanation + 29 comments (2026-11-04 scout run). Was DEPTH-LIMITED on 2026-11-03 (post body blocked, 1 comment); upgraded today.

## Tools used

IV Studio (Windows desktop app, MIT); ComfyUI (driven over its API); MiniMax H3 (video); Qwen3-VL via Ollama or an AI agent via MCP (prompt writing); OpenAI Whisper (take ranking); DLSS 5 or SeedVR2 (finish upscale); SAM 3.1 (cut-out); MiniMax Music 3 / ACE-Step (music); VoxCPM2 (local voices); Civitai LoRAs; three.js headless browser + ffmpeg (previs); RunPod / Modal (cloud GPU with idle shutoff); 142-tool MCP server. Tested on RTX 4090 + 64 GB RAM; 16 GB cards work with smaller previews; every model downloads from its host with SHA-256 verification.

**1.0 additions (2026-11-08):** Linux (self-updating AppImage) and Mac (Apple Silicon and Intel) builds; **Check my PC** first-launch hardware fit; **Fizgig** local character-LoRA training (16 GB+ NVIDIA card) with InsightFace likeness scoring; **RefMod** characters from 1-6 photos in ~30 s; **KJNodes** live preview override; per-shot sampler and scheduler; LoRA and RefMod trays; SDXL fine-tunes in Create > Image; **Comfy Cloud** as a third cloud option; **154 MCP tools** (up from 142). **Krea 2** (Disney Renaissance-style LoRA) made the frames for the trailer's fairy-tale opening; H3 animated them. The Linux build passes its checks on GitHub, but the author has not run GPU work on a real Linux desktop yet. Builds are unsigned: Windows shows SmartScreen, Macs need "Open Anyway" the first time.

## AAA studio practice

- **Previs is the spend gate, not the decoration.** Halon Entertainment's standard pipeline on *The Call of the Wild*: the first previs pass went in "Maya grayscale, which was sent to editorial and edited in along with surrounding shots to make sure it matched the pacing that was requested"; only at the approval phase "would we then be given the go-ahead to take it to engine" ([beforesandafters.com, 2020](http://beforesandafters.com/2020/03/04/what-actually-happens-when-a-director-asks-you-to-previs-a-scene/)). ILM's Rob Bredow on *The Mandalorian* StageCraft: "It really is an end-to-end solution; everything from the early stages of previz... What you see on that LED wall is actually what goes straight into the show"; Taika Waititi: "It's a great throwback to a time when people would make decisions before post" ([ilm.com, 2021](https://www.ilm.com/filmmakers-discuss-bringing-virtual-worlds-to-life-for-the-mandalorian-s2/)).
- **Camera handoffs are numbers, not vibes.** On *The Call of the Wild*, Halon "had given all of our camera data, lens, distant to subject, etc. over to production for shooting in illustration and QuickTime format, so it was easy to replicate on set with numbers to back everything up" ([beforesandafters.com, 2020](http://beforesandafters.com/2020/03/04/what-actually-happens-when-a-director-asks-you-to-previs-a-scene/)). On *War for the Planet of the Apes*, previs supervisor AJ Briones "sat with Matt Reeves and interactively placed all of the cameras with him... so we could take advantage of our builds by generating multiple cameras with them, which in turn helped with continuity" ([unrealengine.com](https://www.unrealengine.com/developer-interviews/halon-evolves-previs-with-unreal-engine?lang=en-US)).
- **Cheap takes before expensive frames.** Halon (2011, *John Carter of Mars* era): "In the hour it takes a keyframe artist to accomplish one take you could have done 50 takes with a virtual camera" — and the deliverable to the director was "QuickTimes with minimal edits, sound and music" ([Post Magazine, 2011](https://digital.copcomm.com/i/33429-may-2011/18)). IV Studio's grey three.js previs is the same idea aimed at a generative downstream instead of a shoot.
- **Agent coordination precedent (indie AI-film pipeline, labeled not AAA).** David Comfort's BLACKWOOD AI short (Threshold Cinema) runs "a conversational agent [that] generates references, tracks locked or blocked cards, rewrites prompts after safety-filter rejections, and proposes parallel next steps", with "character, location, and prop reference sheets... locked against a narrative bible. Only locked references attach to story beats" ([ai-primer.com, 2026-10-31](https://www.ai-primer.com/creative/stories/blackwood-solo-production-workflow)). No AAA studio publishes an equivalent agent-driven generative-video previs pipeline (inference: this is the closest published anchor for agent-assisted prompt writing).

## Phase 1: Let the agent write the prompt

**Do**
1. "Write it for me": a local model (Qwen3-VL via Ollama, or your AI agent through MCP) looks at reference pictures and writes the H3 prompt.
2. Run the checker: it "catches the mistakes H3 punishes (frame-grid lengths, speaker tags, unattached references) and fixes most in one click."
3. Agent-executable: have the agent emit a per-shot camera spec as JSON (lens mm, distance to subject, move type, start/end pose) derived from the staging board, alongside the prompt. The checker verifies every H3 prompt contains an explicit camera spec before any preview is queued — mirroring Halon's "numbers to back everything up" camera-data handoff.

**Check**
- Commenter u/bumredeemer: "the frame grids is my biggest gripe about h3" — the checker is the answer to the most common H3 complaint.
- The camera spec JSON for each shot parses and contains all four fields; the checker logs a rejection for any prompt missing one, and no rejected prompt enters the hunt queue.

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
3. Agent-executable: hash-lock (SHA-256) the character and location reference images per shot and store the hashes in the shot record, BLACKWOOD-style — only locked references may attach to a shot. The prompt checker verifies each prompt references only locked hashes and rejects prompts that introduce unapproved references. Track per-shot stage status (locked/blocked) on the board.

**Check**
- The sketch is playable as an animatic before any generation is spent.
- Every prompt in the queue resolves to locked hashes only; the checker log shows zero unapproved-reference attachments.

**Why**
The sketch is the consistency contract: faces and rooms are locked before the model ever sees the shot.

## Phase 4: Block on the staging board

**Do**
1. "Staging board: place people and the camera on a top-down floor plan; it becomes exact screen directions, or a grey previs clip H3 follows for arcing moves."
2. Build the previs in-app ("The previs is built into the app, no Blender needed"): block the shot on the top-down board — up to four people, each one's facing, gaze target, and walk path; camera lens, height, and move (push, pan, track, arc).
3. Render the previs "in motion as grey mannequins on a plain floor" with three.js in a headless browser + ffmpeg: "about 3 to 5 seconds a clip."
4. Feed the clip into MiniMax H3's reference-to-video mode as `<Video 1>`, alongside the character and location pictures. "The prompt tells H3 the previs only sets camera and blocking, so it keeps the motion and framing but doesn't copy the grey look."
5. Agent-executable: formalize the grey previs as the spend gate before the full-res finish — a scripted check on the previs clip must pass before the H3 finish is released: shot length matches the sketch animatic, the camera move follows the staging board, and character blocking is present. Derive all shot cameras from the one shared top-down staging scene file and run an automated continuity check across shots before queuing: consistent lens per character and the 180-degree axis rule — mirroring Halon's multiple-cameras-from-one-build continuity practice.

**Check**
- Author's honest finding: "it really pays off on arcs and orbits around characters. H3 struggl[es]..." — truncated in the retrieved comment; the struggle is named but its object is not. Treat the truncation as a known unknown.
- The previs gate log shows pass/fail per shot; no full-res finish runs without a passed previs; the continuity check passes (lens consistent, axis respected) or the shot returns to blocking.

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

## 1.0 update: install on any platform, fit the PC, train actors (2026-11-08)

The 1.0 changelog is the community's complaints from the last post, fixed.
Each phase below has Do / Check / Why, same as the core workflow.

### Phase 6: Install on any platform, with setup that fixes itself

**Do**
1. Linux: self-updating AppImage. Mac: Apple Silicon and Intel builds
   (rendering on your own cloud account). Windows: as before.
2. Settings > Setup installs every pack IV Studio needs, at pinned versions,
   in one click (answers the "missing custom nodes" complaint).
3. Your own H3 files (ComfyUI's template names, NVFP4, other turbo LoRAs)
   are recognised and used (answers "Setup says 7 to fix but H3 is
   installed").
4. Ollama on another address: set it in Settings (for ComfyUI and Ollama in
   separate containers).

**Check**
- Setup reports zero to fix when your own H3 files are present; pinned
  versions install in one click.

**Why**
- Install friction was the adoption blocker: the 1.0 changelog is mostly the
  community's install complaints, fixed. (Inference, labeled.)

### Phase 7: Let the app fit itself to the PC

**Do**
1. "Check my PC": on first launch it reads GPU, RAM, and drives and sets
   previews, finish size, the prompt writer, and downloads to suit.
2. If the card is too small, a guided setup connects RunPod, Modal, or Comfy
   Cloud.

**Check**
- A too-small card routes to cloud instead of failing locally; a commenter
  confirms it runs on an RTX 3060 12 GB ("Slow but works").

**Why**
- Fit the workload to the hardware before spending generation: previews and
  finish size follow the machine, not the other way round. (Inference,
  labeled.)

### Phase 8: Train actors locally, or make a RefMod in 30 seconds

**Do**
1. Train a character LoRA locally on your own 16 GB+ NVIDIA card through
   Fizgig (or on RunPod/Modal), with presets, a spending cap, "Train more,"
   and InsightFace likeness scoring to pick the checkpoint.
2. Or make a RefMod character from 1 to 6 photos in about 30 seconds.

**Check**
- InsightFace scores pick the checkpoint; the RefMod path needs only photos,
  no training run.

**Why**
- Likeness scoring turns checkpoint-picking from taste into measurement;
  RefMod is the zero-training shortcut. (Inference, labeled.)

### Phase 9: Direct with live preview and per-shot control

**Do**
1. KJNodes' preview override streams every step into a floating panel on any
   page, including renders an agent starts over MCP.
2. Sampler and scheduler per shot; LoRA and RefMod trays in Create.
3. SDXL fine-tunes in Create > Image; Comfy Cloud as a third cloud option
   beside RunPod and Modal.
4. The app now has 154 MCP tools (up from 142), a tour that lights up the
   real controls one at a time, and a two-minute tour of the whole app.

**Check**
- Every step of a render is visible in the floating preview; per-shot
  sampler/scheduler settings stick to that shot.

**Why**
- Live preview plus per-shot control is the directing surface: see every
  step, tune each shot independently. (Inference, labeled.)

## The human method, distilled

1. The API is the product (drive ComfyUI; never touch the node graph unless you want to).
2. Check what the model punishes (H3-specific checker, one-click fixes for frame grids, speaker tags, unattached references).
3. Hunt cheap, finish once (0.4–0.9 MP previews ranked three ways; finish from the same latent).
4. Previs the model can follow (grey mannequins + "don't copy the grey look" prompt).
5. Verify downloads (SHA-256 on every model).
6. Report the honest finding (arcs/orbits pay off; H3 struggles — truncated).
7. **Ship the community's changelog (1.0).** Linux, Mac, one-click node setup, own-H3 recognition, Ollama address.
8. **Fit the app to the machine (1.0).** Check my PC sets previews and finish size from the actual GPU.
9. **Score likeness, don't eyeball it (1.0).** InsightFace picks the LoRA checkpoint.
10. **A 30-second RefMod beats a training run (1.0)** when the character only needs to exist, not to be perfect.

**Depth status:** FULL (complete author writeup + detailed previs explanation + 29 comments; 1.0 update: complete author writeup + 8 comments). Inference: H3's struggle object is truncated in the retrieved comment; Linux support unanswered in the original post (answered by 1.0: Linux and Mac builds exist, GPU work on a real Linux desktop untested by the author).
