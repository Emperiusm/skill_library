---
name: comfyui-vfx-suite-local-studio
description: "Take a raw video to a finished shot entirely locally inside ComfyUI with ComfyUI-VFX-Suite: COLMAP/GLOMAP camera tracking, 3D blockout with FLUX.3 Klein keyframes, LTX IC-LoRA generation, Qwen Image Edit relighting, an MCP AI Director, and Nuke export, all under 24 GB of VRAM with zero cloud APIs. Trigger when building a local AI VFX pipeline where the camera move has to survive generation."
---

# ComfyUI-VFX-Suite: Local VFX Studio in ComfyUI

## Purpose

This skill reconstructs the exact workflow from Turbulent-Barber582's post
and comment thread, step by step, so another agent can run a raw video to a
finished shot entirely locally inside ComfyUI. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: track the real camera, block the scene in
3D, generate with layout-aware LoRAs, and let an agent run the chain, all
locally under 24 GB of VRAM.

## Source

- Post: "From a raw video to a finished shot — entirely local, entirely
  inside ComfyUI, and all under 24 GB of VRAM" by Turbulent-Barber582 —
  https://www.reddit.com/r/comfyui/comments/1xnm2tl/from_a_raw_video_to_a_finished_shot_entirely/
  (r/comfyui, score 51, 18 comments, 16 retrieved)
- Repo: https://github.com/pavlovfilmdirector/ComfyUI-VFX-Suite
  (v0.1.0-preview, #OpenSourceHiggsfield entry)
- Evidence: full post text + 16 comments with exact tool names, failure
  modes, and quoted principles. Native clip; no transcript to retrieve. No
  generation parameters were disclosed.

## Tools used

**ComfyUI-VFX-Suite** v0.1.0-preview; **COLMAP / GLOMAP** camera tracking;
custom **LTX-2.3 IC-LoRAs**; **LTX-2.5** + layout-to-render IC-LoRAs;
**FLUX.3 Klein** keyframes; **Qwen Image Edit** relighting; **Nuke** export
nodes; **Ollama** local LLM or MCP (Claude/ChatGPT) AI Director; mobile
remote control.

## Phase 1: Track the camera from raw footage

**Do**
1. Drop source footage into the studio; the Smart Pipeline automatically
   extracts masks, depth, pose, and accurate camera tracks.
2. Tracking lineage (author's post text): "moving from early COLMAP/GLOMAP
   experiments to custom LTX-2.3 IC-LoRAs."

**Check**
- Author's failure mode, in his own words (comment): "Colmap and Glomap,
  much like other tracking tools, require high-quality source material for
  processing. If you provide a blurry image, the software will attempt to
  generate an intermediate, mathematically calculated frame between the
  clear ones. However, the system may occasionally fail, causing the
  camera's tracked path to veer off course."
- Fix order per the author: re-run the tracking process, or manually
  correct the data. A smoothing function exists; the author doesn't use it:
  "I personally don't use it, as I work with raw production footage, but it
  could prove useful if you are building a shot from video — for instance,
  when replacing both the environment and the characters — where you don't
  need a precise match to the original, but rather just the camera
  trajectory."

**Why**
The camera track is the control signal everything else hangs on; a bad
solve corrupts every generated frame, so track quality gates the pipeline.

## Phase 2: Block the scene in 3D, design keyframes

**Do**
1. Block scenes in 3D and design keyframes with FLUX.3 Klein.
2. Generate backgrounds and characters using LTX-2.5 + layout-to-render
   IC-LoRAs.
3. The author has his own editor for this, "simply drew inspiration from
   whatever I found convenient in Blender and Unreal" (author comment).

**Check**
- Keyframes are designed (FLUX.3 Klein) before generation, not prompted
  blind: layout-to-render IC-LoRAs take the layout as input.

**Why**
Layout first, pixels second: the 3D blockout is what makes the generated
shot match the intended composition and camera move.

## Phase 3: Relight with Qwen Image Edit

**Do**
1. Once satisfied with the initial frame, run the generation (author
   comment: "Once I'm satisfied with the initial frame, I proceed to run
   the generation").
2. Relight with the author's Qwen Image Edit workflow, which "performs
   relighting using specific, intuitive parameters" (author comment).
3. IC-LoRA operates on a video plus an initial frame (author comment).

**Check**
- Commenter Snoo20140's open question, unanswered: "How did u solve the
  relighting issue? It has been my biggest holdup." The author's answer
  points at Blender/Unreal-informed relighting plus the Qwen Image Edit
  workflow; no parameter values were posted.

**Why**
Relighting is the step that makes a generated frame sit in the real plate;
it is also the step other builders in the thread report as their hardest.

## Phase 4: Let the AI Director run the chain

**Do**
1. Chain multiple steps into a single pipeline that runs with one click;
   add custom API workflows as needed.
2. Or chat with the built-in AI agent: "You can connect a local LLM via
   Ollama to act as your studio assistant. Alternatively, if you use
   Claude, ChatGPT, or another agent service, you can hook it up via MCP."
   (author comment, verbatim). "Upon connecting, it automatically reads
   the studio instructions and toolset, taking care of the technical heavy
   lifting — from cleaning control passes and running generations to
   assembling the final composite."

**Check**
- Zero cloud APIs; every open-weights model runs locally, optimized for
  24 GB VRAM. Open question in the thread (wacomlover, unanswered):
  "Would this work with 16GB of VRAM?"

**Why**
The agent is the operator: the human directs in plain language, the agent
runs the node chain. That is the P2 agentic-DCC shape, inside ComfyUI
rather than Blender.

## Phase 5: Finish and export to Nuke

**Do**
1. Composite, relight, refine, dub, and export straight to Nuke via
   dedicated nodes.
2. Control the studio remotely from a mobile phone (already implemented).

**Check**
- Built in just 2 weeks for the challenge ("It's raw and needs more
  testing, but the core pipeline works and solves real problems for
  creators").
- Roadmap (author comment): TTS, LoRA training, video editing, generative
  animation; image, video, and 3D-object generation from images or
  descriptions plus a 3D scene environment for camera tracking and layout
  assembly are already implemented.

**Why**
Finishing in Nuke is the industry handoff: the local studio is a front
end, not a walled garden.

## The human method, distilled

1. Track first: the camera solve gates everything downstream.
2. Layout before pixels: 3D blockout + keyframes, then generation.
3. Relight deliberately: the initial frame must satisfy before generation
   runs.
4. Let the agent operate the chain; direct in plain language.
5. Ship in two weeks and let the thread find the holes (16 GB VRAM and
   handheld-phone tracking are the open ones).

## Failure modes

- **Blurry input breaks the camera solve.** COLMAP/Glomap interpolate
  between clear frames and the tracked path veers off course. Fix: re-run
  tracking, or correct the data manually. Smoothing helps only when an
  exact match to the original is not needed (replacing environment and
  characters, keeping only the camera trajectory).
- **Relighting is the hard step.** The thread's most upvoted technical
  question is how relighting was solved; the author's answer is a workflow
  plus Blender/Unreal-informed judgment, not a parameter set. Expect to
  iterate here.
- **Handheld phone footage is untested.** Commenter purelawan's question —
  rolling shutter plus motion blur, and whether IC-LoRA still follows the
  move if the track is noisy — went unanswered.
- **16 GB VRAM is unanswered.** The studio is optimized for 24 GB; no
  16 GB run was reported in the thread.
- **Not the only suite in its class.** Commenter DeepHomage lists three
  other #OpenSourceHiggsfield video suites (ComfyUI Motion Previs Studio,
  VLO, Chain Motion AI Video Editor) and is still sorting between them;
  this skill is one approach, not the settled winner.

**Depth status:** FULL (full post text + 16 comments with exact tool names,
failure modes, and quoted principles; native clip has no transcript to
retrieve; no generation parameters were disclosed).
