---
name: minimax-h3-chain-director
description: "Run multi-segment MiniMax H3 video in ComfyUI from one Director panel: Single or Chain modes, general plus per-segment prompts, H3 Motion Context carrying audiovisual continuity with automatic transition-frame trimming, independent BASE and UPSCALE stages, 3D latent upscaling, KJNodes live preview, and final export with audio. V2 (2026-11-11) adds dual-motion-context BASE+FINAL latents, a BASE review gate with direct BASE+Upscale mode, and Spectrum acceleration rules. Includes the known V1.0 failure modes (prop drift, xmarre upscaler keep_proportion bug, Motion-Context node conflict) and the V2 failure modes (blur after segment 4-5 in continuous takes, background jumps at cuts in high-motion scenes). Trigger when a MiniMax H3 project needs more than one segment held together."
---

# MiniMax H3 Chain Director V1.0 (ComfyUI Director Node)

## Purpose

This skill reconstructs the Chain Director workflow from the author's
post and comments, step by step, so another agent can follow the same
process. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle). The video's
core method is: run a whole multi-segment MiniMax H3 project from one
Director panel, with Motion Context carrying continuity between
segments.

## Source

Creator: Far_Patience4517. Reddit post:
https://www.reddit.com/r/comfyui/comments/1xdovs4/minimax_h3_dual_segment_has_evolved_into_minimax/
(r/comfyui post 1xdovs4, score 44, 22 comments) | 2026-10-25 scout run,
audit 4. This is the evolution of the author's previous MiniMax H3 Dual
Segment workflow into a Director node; it is a different workflow from
the existing SelfLift, SyncTile, SAM3, no-mask LoRA, and Reference-to-
Video MiniMax H3 skills.

V2 update (2026-11-11 scout run, audit 2): the same author released H3
Director Studio V2
(https://www.reddit.com/r/comfyui/comments/1xs4d9u/a_very_special_workplace_h3_director_studio_v2/,
r/comfyui post 1xs4d9u, score 39, 14 comments; repo
https://github.com/M1cr0Bytes/MiniMax-H3-Director-Studio_V2, Civitai
https://civitai.red/models/2984987/minimax-h3-director-studio-v2).
V2 is an evolution of the same workflow, not a different one, so this
skill is expanded here rather than split. The V2 material is in the
"V2: dual-motion-context" section below; V1.0 stays in the repo's legacy
folder (legacy/H3_Director_Studio_V1).

## Tools used

**ComfyUI**, **MiniMax H3** (H3DirectorStudioV1 node),
**ComfyUI-H3-Motion-Context** (0.5.0 or newer required),
**KJNodes** (live preview), **LBH-123-AI Latent Upscaler** (original)
vs **xmarre Latent Upscaler-Plus** variant (compatibility issue, see
Phase 4), **Civitai** workflow download (models/LoRAs not included).
Related node mentioned by a commenter, author-unexamined:
**ComfyUI_MiniMax_H3_Extender** (github.com/tritant/ComfyUI_MiniMax_H3_Extender).

## Phase 1: Install the Director and its dependency correctly

**Do**
1. Install the Director manually inside `custom_nodes` (it is not
   listed in ComfyUI Manager, per the author).
2. Update ComfyUI-H3-Motion-Context to 0.5.0 or newer (`git pull`
   inside its folder if installed with Git).
3. Do not run two Motion-Context nodes at once: a commenter reports
   NikoDemon80/ComfyUI-H3-Motion-Context conflicts with
   seitanism/ComfyUI-H3-Motion-Context-MultiRef ("If you have both,
   then it cant generate the first clip, because in MultiRef means 0 =
   load the first clip from disc"); removing the MultiRef node fixed it
   for that commenter.
4. Configure duration, aspect ratio, resolution, seed, sampler,
   scheduler, steps, and render mode from the Director panel.

**Check**
- The Director executes as the H3DirectorStudioV1 node; if ComfyUI
  cannot execute it, the Director itself is not installed correctly
  (author's diagnostic).

**Why**
- One panel replaces a fixed two-segment graph: the previous Dual
  Segment workflow is now a mode, not the whole tool.

## Phase 2: Direct Single or Chain segments

**Do**
1. Choose Single (one standalone segment) or Chain (a longer
   multi-segment sequence).
2. Define general prompts shared across the project and independent
   prompts per segment.
3. Let MiniMax H3 Motion Context carry audiovisual context between
   segments to maintain consistent motion, scenes, and transitions.
4. Let automatic context trimming remove repeated transition frames
   before the next segment begins.
5. Enable or disable reference images by number: with 10 images loaded,
   selecting only 3 uses only those 3 (author's explanation of the
   numbered image toggles, answering a commenter's confusion).

**Check**
- Continuity is the thing to verify segment by segment: motion, scene,
  and transitions must carry, not restart.

**Why**
- The Director's value is continuity management (shared prompts plus
  carried context plus trimmed seams), not just launching generations.

## Phase 3: Split BASE and UPSCALE, and preview live

**Do**
1. Run BASE and UPSCALE as independent stages with different models,
   LoRAs, samplers, schedulers, and step counts.
2. Use integrated 3D latent upscaling: a configurable upscale
   multiplier followed by a second sampling pass.
3. Monitor progress and animated previews inside the Director through
   KJNodes.
4. Keep image, video, and audio references connectable, and keep the
   workflow modifiable with other ComfyUI nodes.
5. Export the final video with audio.

**Check**
- The public workflow is sanitized: it contains no private prompts,
  personal references, or model files. Models and LoRAs come from the
  Civitai page's instructions, not the download.

**Why**
- BASE/UPSCALE independence is the quality lever: a cheap base pass
  plus a tuned upscale pass beats one monolithic setting.

## Phase 4: Watch for the three known failure modes

**Do**
1. Check every segment for identity/prop drift: a commenter reports
   "the earring changing shape, sizes, and colours mid scene, the
   mousepad logo swapping like in a kaleidoscope, vases on the right
   shelf changing shapes and sizes." These are the acceptance checks
   for any Chain Director take until the author reports otherwise.
2. Expect the UPSCALE bug if you use the xmarre Latent Upscaler-Plus
   variant: its `MinimaxH3LatentUpscaler3D` node requires an additional
   `keep_proportion` parameter the Director did not pass (it called the
   LBH-123-AI parameter set). The author confirmed it as a
   compatibility issue in V1.0, prepared a patch the same thread, and
   told Git installers to `git pull` in
   `ComfyUI/custom_nodes/ComfyUI-H3-Director-Studio-V1`, restart
   ComfyUI fully, and retry UPSCALE; ZIP installers must replace the
   Director folder and keep only one active copy.
3. Treat H3 voice-audio complaints as a model limitation, not a
   Director bug: commenters call the voice "a pain to ears" and say H3
   voice audio "sucks"; one suggests generating audio first and
   cutting to it.

**Check**
- Drift is visible in small props first (earring, mousepad logo,
  vases), not in the hero subject. Check props, not just faces.

**Why**
- A director that cannot hold props across segments has not solved
  continuity; it has only automated the generation loop. The drift
  list is the acceptance test.

## V2: dual-motion-context (H3 Director Studio V2, 2026-11-11)

V2 turns the MiniMax H3 workflow into a cleaner, more controllable
segment-based pipeline. The core method is: generate a BASE pass, review
it, keep the accepted BASE, and upscale that exact result with Latent 3D;
Chain carries two separate latents between segments so motion, audio,
sharpness, and detail survive the joins.

### Phase V2-1: Review the BASE before spending upscale

**Do**
1. Generate the BASE pass for a clip.
2. Review it and keep the chosen BASE; only the accepted BASE goes to
   upscale.
3. Or switch to direct BASE + Upscale mode when you do not need to stop
   between passes.
4. Use the active clip selector: Chain starts on the selected clip if it
   has no saved latent, otherwise it continues from the next one.
5. Clear temporary latents to restart a project from clip 1.

**Check**
- The BASE you keep is the one you reviewed; the upscale pass works on
  that exact accepted result, not a re-generation.

**Why**
- Upscale is the expensive pass; reviewing the cheap BASE first means
  you never pay to upscale a take you would have rejected.

### Phase V2-2: Carry two latents between segments

**Do**
1. For multi-segment videos, run Chain: the Director saves two separate
   audiovisual latents for each completed segment.
2. BASE latent: carries the motion and audio from the previous segment
   into the next BASE generation.
3. FINAL latent: carries the previous segment's upscaled result into the
   next upscale pass, at the final resolution.
4. Example from the author: segment 2 uses BASE 1 to generate its BASE,
   then FINAL 1 during the upscale pass.

**Check**
- Watch the joins: visible changes in sharpness and detail at segment
  boundaries, and whether the soundtrack continues across the cuts.

**Why**
- One carried latent cannot serve both passes: the BASE pass needs
  motion/audio context at base resolution, the upscale pass needs the
  finished look at final resolution. Two latents is the fix for the
  sharpness/detail step visible at joins in V1.

### Phase V2-3: Apply Spectrum acceleration only where it belongs

**Do**
1. Enable Spectrum acceleration on the BASE branch only.
2. Recommended for non-Turbo generations around 25 steps.
3. Do NOT use it with Turbo LoRAs or in the Latent 3D Upscale pass.
4. Author's rule, quoted: "Except for Comfy Kitchen, most accelerators
   tend to reduce video quality. I only use Spectrum when I'm not using
   Turbo; it also depends a lot on the type of video you're creating. If
   it's a simple video with little movement, you can use more
   accelerators, but for more complex videos, I avoid using them."

**Check**
- If the video is simple with little movement, more accelerators are
  tolerated; if it is complex, drop them.

**Why**
- Accelerators trade quality for speed, and the trade is worst exactly
  where the video is hardest (complex motion). The BASE branch is the
  only place the trade is acceptable.

### Phase V2-4: Watch the two known V2 failure modes

**Do**
1. After the fourth or fifth segment of a continuous take, check for
   blur: the author confirms "after the fourth or fifth segment, the
   image becomes blurry. It happened to me during a continuous take, it
   happens less often when there are changes in shot or camera angle."
2. At each cut, check the background: a commenter spotted sudden
   background changes at :10 and :20, "presumably because the upscaling
   is disconnected between rendered clips." The author confirms those
   are the cuts and says he deliberately chose "a challenging,
   high-motion video of the city to test how the motion context is
   preserved during the second pass. If you use a scene with less
   movement, I can guarantee that the cut won't be noticeable."
3. Note the commenter suggestion the author accepted:
   geiru_context_suite end-frame anchoring
   (github.com/roycho87/geiru_context_suite) for sharpness and color
   drift mitigation in long-video continuation clips. The author replied
   he had not considered it necessary "because I believe version 2 is
   better" but would add it; V1 now lives in the repo's legacy folder.
4. Keep the separation the author draws: manual clip work vs automated
   sequence rendering are distinct modes in V2, and the Director stays
   independent of any built-in preview system (optional BASE preview
   support exists, but the Director does not depend on it).

**Check**
- Blur shows up after segment 4-5 in continuous takes; background jumps
  show up at cuts in high-motion scenes; both are hidden in static
  scenes, so test with motion, not with a still.

**Why**
- A continuity system is only proven by the scene that breaks it. The
  author stress-tested with a high-motion city clip for exactly that
  reason, and the failure modes he reports are the acceptance test for
  anyone adopting V2.

### V2 human method, distilled (additions)

4. **Review the cheap pass before paying for the expensive one.**
5. **Carry two latents, not one**: BASE context for the next BASE, FINAL
   context for the next upscale.
6. **Accelerators only on the BASE branch**, only non-Turbo, only ~25
   steps.
7. **Test continuity with motion**; static scenes forgive everything.

## AAA studio practice

No AAA studio is documented as shipping on MiniMax H3 itself, so this section does not claim one. What is documented is the production-grade principle the Director implements: continuity across segments is managed as a system, not hoped for per clip. Filmatix, an AI-cinema production outfit, describes its multi-shot workflow as shot-by-shot generation with "full continuity control": character identity locked, state preserved across cuts, lighting matched between scenes, with a serialized AI drama (The Mia Show) as its internal R&D environment for exactly this problem. StoryMem, a multi-shot storytelling system from ByteDance and Nanyang Technological University researchers, makes the same point architecturally: it keeps a memory bank of keyframes from previously generated shots and conditions each new shot on it, reporting a 28.7% improvement in cross-shot consistency over methods without that memory. The Director's Motion Context plus trimmed seams is the ComfyUI version of that memory bank: carried context, not independent generations. The same production logic appears in practitioner workflows for long AI video: plan in the unit the tool renders (scene math), build one reference pack before generating anything, and run a continuity check that flags any scene where clothing, lighting, or props could drift from the previous one, before spending generation budget.

- Source: https://www.filmatix.ai/Cinema.html (Filmatix AI-cinema production process: shot-by-shot generation, identity locked, state preserved across cuts)
- Source: https://studio.aifilms.ai/blog/storymem-multi-shot-video-storytelling-with-visual-memory (StoryMem: keyframe memory bank conditioning subsequent shots, 28.7% cross-shot consistency improvement)
- Source: https://dipenvaja.medium.com/the-10-minute-ai-video-headline-is-really-about-stitching-short-scenes-9d80c5bd77c9 (long-AI-video workflow: scene math, one reference pack, continuity check before spend)

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Write a segment manifest before any render: one JSON file listing every segment, its general plus per-segment prompts, the reference-image indices it uses, and the transition frames to be trimmed. The Director panel settings (mode, duration, aspect, seed, sampler, scheduler, steps) are copied into the manifest, not left only in the UI.
2. Automate the prop-drift acceptance pass from Phase 4: after each segment renders, extract its first and last frames plus one mid-segment frame, and check the named props (earring, mousepad logo, shelf vases, or the project's own equivalents) across all three. Log pass/fail per prop per segment in a JSONL take log.
3. Automate the Phase 4 upscaler-compatibility gate: before the UPSCALE stage, read the upscaler node's expected parameter set from the installed node and compare it against the parameter set the Director passes. A missing parameter (the V1.0 `keep_proportion` failure mode) fails the run before any upscale compute is spent.
4. Log every segment take (seed, sampler, steps, BASE/UPSCALE split, trim frames) to the same JSONL file, so a drifted segment can be re-rendered alone instead of re-running the whole chain.

**Check**
- The manifest exists and matches the Director panel before generation starts.
- Every segment has first/mid/last frames checked against the prop list; a prop failure regenerates that segment only.
- The upscaler parameter sets match before UPSCALE runs; a mismatch is a hard stop, not a render-then-debug.
- The take log covers every rendered segment with no gaps.

**Why**
- In multi-shot production, the expensive defect is a continuity failure discovered at the final cut. The manifest, the prop check, and the parameter gate all move that discovery to before the spend: the manifest prevents a wrong reference index, the prop check catches drift while the segment is still cheap to redo, and the parameter gate catches the known V1.0 bug class before compute is burned.

## The human method, distilled

1. **One panel, two modes**: Single or Chain, same Director.
2. **Continuity is carried, not hoped for**: Motion Context plus
   trimmed seams.
3. **Props are the drift detector**: check the earring before the face.

**Depth status:** PARTIAL (V1: full post text + all 22 comments; V2: full
post text + all 14 comments; the Civitai workflow files were not
downloaded or executed, and no generation settings beyond the ones quoted
above are claimed).
