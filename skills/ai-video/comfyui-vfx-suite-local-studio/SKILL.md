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

## AAA studio practice

- **The tracked camera is the whole trick, and the frustum is its safety margin.** ILM's StageCraft (The Mandalorian, Obi-Wan Kenobi, The Batman) works because witness cameras track the real camera's six degrees of freedom plus lens metadata (focal length, focus distance, iris, distortion profile) dozens of times per second, and Unreal renders only the frustum, the cone of the LED wall the lens actually sees, from the tracked position. The frustum is drawn slightly larger than the field of view as a safety margin that absorbs tracking latency, so a fast whip-pan never reveals the seam; engineers fight latency with predictive filtering and low-latency video paths. The same discipline applies here at indie scale: the COLMAP/GLOMAP solve is the frustum source, and a solve that veers off course corrupts every generated frame downstream, exactly as the author's failure mode describes.
  Sources: https://boldentrance.com/stagecraft-ilm-the-mandalorian/ and https://soc.org/project/obi-wan-kenobi-7/
- **Layout in 3D before pixels, and shoot the final pixel on set.** StageCraft's philosophy is "final pixel in camera": the world is fully built in 3D first, the director sees something close to the final shot in the viewfinder, and the LED wall lights the actors interactively instead of leaving lighting to post. That is the AAA version of this skill's Phase 2 (3D blockout + FLUX.3 Klein keyframes before generation) and Phase 3 (relight before running the generation): the initial frame must satisfy before the generation runs, because relighting after the fact is the expensive fix.
  Source: https://boldentrance.com/stagecraft-ilm-the-mandalorian/
- **The Nuke handoff is a contract, not a dump.** Foundry's Nuke Stage links pre-production through final pixels in one pipeline: node-graph compositing, OpenUSD scene interchange, multi-channel OpenEXR, and OpenColorIO color management shared from set to post, so content refined on the LED wall transitions seamlessly to the final composite. The ASWF's OpenEXR/OCIO guidance for Nuke and Katana makes the mechanism explicit: multiple render passes (direct/indirect diffuse and specular, depth, beauty) ride in one EXR file as layers, and compositors isolate them with Shuffle nodes for fine-grained control, all under ACES via OCIO. The studio slapcomp discipline is the same contract at shot level: a script saved under the shot directory as `[project]_[sequence]_[shot]_lighting_slapcomp_v001.nk`, importing the scan, the CG beauty and all passes, and the shot's lens-distortion node.
  Sources: https://www.foundry.com/news-and-awards/foundry-announces-nuke-stage, https://www.aswf.io/blog/openexr_opencolorio_nuke_katana/, and https://www.keheka.com/how-to-make-a-slapcomp-in-nuke/

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Write a `track-report.json` for every shot: frame count, solve reprojection error per frame, and any frame where the tracked path deviates from the smoothed path by more than the shot's tolerance. Frames that fail the tolerance go in a re-track queue (re-run tracking, then manual correction, in the author's fix order); a shot ships only when the queue is empty or every remaining entry is marked smoothing-acceptable (environment and characters replaced, camera trajectory only).
2. Add a camera-path continuity check before generation: render the tracked path as a top-down plot with the frustum overlaid at the first, middle, and last keyframes, and verify no jump between consecutive frames exceeds the largest inter-frame move in the clean section of the track.
3. Define a Nuke export contract and enforce it at export time: EXR with named AOV channels (beauty plus the passes the relight needs), one pinned OCIO config (record whether the shot is sRGB or ACES), and a generated Nuke script named `[project]_[sequence]_[shot]_vfx_v001.nk` in the shot directory. The relight pass logs a before/after frame pair against a fixed reference object in the frame, so the relight is a measured change, not a feeling.
4. Keep the 16 GB VRAM question as an open gate, not a guess: run the track-report and keyframe steps on 16 GB first (they are the cheap steps) and record which step first exceeds memory, so the open question gets an answer per step instead of per studio.

**Check**
- A shot is generation-ready only when its track-report has no unqueued failures, its path-continuity plot shows no jumps, and its initial frame is approved; a shot that fails any of the three goes back to Phase 1, not forward to generation.
- A Nuke export is shippable only when the EXR carries the named AOV channels, the OCIO config is pinned in the contract, and the relight before/after pair exists; an export missing any of the three is an unmeasured handoff.

**Why**
StageCraft's lesson is that the camera solve and the frustum are the product, and everything else is decoration on top of them. A track-report plus a continuity plot makes the author's "re-run or correct manually" fix order executable instead of aspirational, and the Nuke contract turns "export straight to Nuke" from a feature bullet into a verifiable handoff.

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
