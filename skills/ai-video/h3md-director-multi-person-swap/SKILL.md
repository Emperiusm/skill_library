---
name: h3md-director-multi-person-swap
description: "Swap up to 5 people in any live-action video with MiniMax H3 in ComfyUI: SAM3.1 tracks people by identity, Qwen Image 2.1 builds a keyframe plan at every crossing, the Director renders with the Remake LoRA. Trigger when a character swap must survive crossings, overlaps, and camera cuts."
---

# H3MD 0.5–0.6: Multi-Person Character Swap in MiniMax H3

## Purpose

This skill reconstructs the exact workflow ReferenceFluffy6159 demonstrates for swapping up to five people in one video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: find the crossing and overlap moments first and give the model a keyframe for each one, and track people by identity, not by position.

## Source

Creator: ReferenceFluffy6159. Post: "Put yourself into any dance video – swap up to 5 people at once, 100% local (MiniMax H3 + ComfyUI)" https://www.reddit.com/r/comfyui/comments/1xzrra6/ (score 38, 8 comments, including the author's two detailed replies; full post text and comments read) | Workflows (free): https://civitai.com/models/3037225?modelVersionId=3478241 | Nodes: https://github.com/1113800942/comfy-h3md-director | Walkthrough (Chinese voice, English subtitles): https://youtu.be/WMQJjmHZikc | 2026-11-19 scout run, audit 3.

Update (0.6): "H3MD 0.6: upgraded keyframes let a free open-source ComfyUI tool swap every person in a messy, crowded group video (MiniMax H3)" https://www.reddit.com/r/comfyui/comments/1y38u12/h3md_06_upgraded_keyframes_let_a_free_opensource/ (r/comfyui post 1y38u12, score 50, 4 comments; full post text and comments read) | Free workflows: https://civitai.com/models/3037225 | Nodes (AGPL-3.0): https://github.com/1113800942/comfy-h3md-director | Full walkthrough (English audio, Chinese audio track and subtitles too): https://youtu.be/ye7YbiWgzsg — captions were unobtainable in the 2026-11-23 run and the media download was blocked by YouTube's bot sign-in wall, so the walkthrough's on-screen steps are not in this skill | 2026-11-23 scout run, audit 6. The 0.6 phases below supersede the 0.5 keyframe plan where they differ; the 0.5 render, face-fix, and limits phases above still stand except where the 0.6 post contradicts them, and the contradiction is noted in place.

## Tools used

MiniMax H3, ComfyUI, comfy-h3md-director nodes (H3MD 0.5, then 0.6), Qwen Image 2.1 (0.5 keyframe step only; the 0.6 post does not name the prompt-writing model — it says only "your own AI writes the keyframe prompts with the included skill"), H3 Image (paints the 0.6 keyframes), SAM3.1, Remake LoRA, VOSR2. 100% local.

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

## Phase 5 (0.6): Pre-scan and one manual identity check

**Do**
1. "Pre-scan + one manual check. Face tracking and body masks build a cast list; you drag a line from each character picture to the right person (one picture can link to several boxes when someone is half-visible)."
2. This check covers the hard cases the author names: "People cross, block each other, walk in and out of frame and wear almost the same clothes – the kind of clip where swap tools keep putting the wrong face on the wrong person."

**Check**
- The cast list must link every picture to the right person, including half-visible people (one picture to several boxes). The author states the check's purpose directly: "That one check is what stops the mix-ups."

**Why**
Identity by manual link, not by position or by automatic tracking alone: when people cross and wear almost the same clothes, position-based assignment puts the wrong face on the wrong person. One human link per character is the fix, and it is the only manual step claimed. This supersedes the 0.5 Phase 1 numbering/left-to-right plan as the identity step; the 0.5 left-to-right numbering is not repeated in the 0.6 post.

## Phase 6 (0.6): Place keyframes only where the picture needs one, and redo one at a time

**Do**
1. "Your own AI writes the keyframe prompts with the included skill; H3 Image paints them." No model name for "your own AI" is stated in the 0.6 post; do not carry the 0.5 Qwen Image 2.1 name over as a 0.6 fact.
2. "Keyframes only where the picture needs one (start, each cut, someone entering or coming back, people swapping places)." Result on the author's example: "a 38 s five-person clip went from 19 keyframes to 10."
3. "Redo rerolls a single keyframe; for big errors ask your AI for a new package (cached, only the wrong ones rerun)."
4. "The plan imports straight into the Director, which renders 2–3 minute videos."

**Check**
- Count the keyframes against the event list: start, each cut, each entry/return, each place-swap. The 19-to-10 reduction is the author's measured result on that one clip, not a general guarantee.
- A single bad keyframe is fixed by rerolling that keyframe alone. Larger errors get a new package, with caching so "only the wrong ones rerun".

**Why**
Keyframes are placed at identity-risk moments (cuts, entries, returns, swaps), not at a fixed interval. Fewer, better-placed keyframes is the 0.6 claim: "We rebuilt and improved how H3MD makes them, so multi-character swap now holds on complex scenes." Localised repair means a single-keyframe failure does not cost a full re-render.

## Phase 7 (0.6): Budget the render on an RTX 5090

**Do**
1. Author reply to "How much it takes to render video?": "at 5090 and H3MD 1 sec -> 1 min, short video like under 15 sec usually more fast, around 12 mins, over mins like 2 mins usually take around 120 mins". Read as: roughly 1 minute of render per 1 second of video; a sub-15-second video around 12 minutes; a ~2-minute video around 120 minutes. The author's English is compressed; quote it, do not smooth it into a cleaner claim.
2. Note that this replaces the 0.5 Phase 2 budget (26 seconds in 29 minutes) as the current planning figure for the 0.6 workflow; the two figures are from different clips and different versions, so do not average them.

**Check**
- Budget 1 min/sec on a 5090 as the planning figure, and watch the ~2 s mark of the 0.6 demo for the reported pop (see Failure modes). No other hardware figure is stated.

**Why**
Render time is the real cost of the workflow: the keyframe savings in Phase 6 buy identity correctness, not speed.

## Failure modes

- **Identity swap on crossings:** the model puts the wrong face on a person or the wrong clothes on a body. The fix is a keyframe at every crossing and overlap, not a better prompt.
- **Wrong person from a contradicting description line:** one line per person must agree with that person's picture (gender, ethnicity, clothes).
- **Blurry faces in wide shots:** faces at 50–100 px need the H3-in-SAM3-mask redraw plus VOSR2; even then, keep faces out of very wide shots.
- **Stacked people, big-to-small swaps, long-to-short hair:** stated limits of version 0.5; do not expect the workflow to handle them.
- **Visible pop at ~2 s (0.6 demo):** "Except the weird pop at about 2 seconds in, it looks good!" (commenter RobMilliken). The author did not reply to that comment. Watch the ~2 s mark when checking a 0.6 render; no cause or fix is stated.

## AAA studio practice

- **ILM Flux, The Irishman (2019).** The closest production analogue to swapping several people in one shot: three leads (De Niro, Pacino, Pesci) were de-aged simultaneously across four decades, in crowded scenes where the actors sat at a table leaning toward each other and talked. ILM's answer was a per-actor model built once, up front, from controlled-environment captures of each actor's full range of facial movements, plus a markerless three-camera rig (central RGB camera flanked by two infrared witness cameras) that derived the performance from light and texture on set, with no head cams, markers, or special lighting. The parallel to this skill is direct: identity is a per-person record built before the solve, and the crossing moments are handled by capture geometry, not by hoping the model keeps identities straight. Source: https://www.cgw.com/Press-Center/Web-Exclusives/2019/Face-Lift-The-Irishman.aspx ; https://www.motionpictures.org/2020/02/de-aging-the-iconic-actors-of-martin-scorseses-the-irishman-2/
- **ILM FaceSwap, Indiana Jones and the Dial of Destiny (2023).** FaceSwap is a modular suite, not a single technique: 3D facial tracking and retargeting, keyframe animation, ML-driven facial solves, the underlying plate, or full CG. The production's rule was per-shot recipes, with each shot getting its own combination of techniques, and the identity anchor was a FACS expression library plus frames matched from past performances to the current shot's orientation. That is the studio version of this skill's keyframe plan: the hard moments get their own reference material, chosen per shot. Sources: https://80.lv/articles/see-how-industrial-light-magic-made-harrison-ford-40-years-younger ; https://www.artofvfx.com/indiana-jones-and-the-dial-of-destiny-andrew-whitehurst-production-vfx-supervisor-ilm/
- **Disney Research FRAN (2022).** FRAN applies the change as a layer over the original face rather than generating a new one, which is what preserves identity while the head moves and lighting changes, and it gives artists localized control to direct and fine-tune per frame. The failure it names for other systems, "facial identity loss, poor resolution and unstable results across subsequent video frames," is the production phrasing of this skill's crossing/overlap failure mode. Source: https://studios.disneyresearch.com/2022/11/30/production-Ready-Face-Re-Aging-for-Visual-Effects/

**Agent-executable upgrades**

1. **Per-person identity record (`swap-identities.json`).** One entry per person: person number, reference-picture hash, description line, first-frame bounding box (left-to-right order), and the list of keyframe timestamps with the crossing or overlap each one covers. This is the skill-scale version of ILM's per-actor model: the identity record exists before the render starts.
2. **Description-line contradiction check.** Before rendering, compare each person's description line against that person's picture (gender, ethnicity, clothes keywords) and flag any contradiction in the manifest. The skill's own failure mode says a contradicting line overrides a right picture; this check runs before the 29-minute render, not after it.
3. **Crossing audit.** Extract one frame at every keyframe-plan timestamp with ffmpeg and log, per crossing, that every swapped person is visible with a face present. A crossing with no keyframe in the plan is a gap in the plan, flagged before rendering.
4. **Render manifest (`swap-render.json`).** Clip length, resolution, Remake LoRA version, render seconds, GPU, per-person swap status, and the resolution-lock gate: refuse to render at any resolution other than the Remake-supported sizes (1664x960 / 960x1664 / 2560x1472) instead of discovering the lock mid-render.
5. **Small-face gate.** Measure face height in pixels on every keyframe automatically. Faces at 50-100 px are routed to the Phase 3 SAM3-mask redraw plus VOSR2 pass; faces below 50 px are flagged as keep-out-of-wide-shot, per the author's own caveat.

## The human method, distilled

1. Find the hard moments first: keyframes go on the crossings and overlaps, not on the easy stretches.
2. Track identity, not position: numbering left-to-right in the first full frame is what makes crossings survivable.
3. One simple line per person, and it must agree with the picture.
4. (0.6) Spend human attention exactly once — the drag-line identity check — and let the rebuilt keyframe generation carry the rest. Keyframes only at identity-risk moments; redo one keyframe at a time.

**Depth status:** FULL (full post text + 8 comments, including the author's detailed replies on identity tracking, keyframes, and limits; the native clip is the before/after demo of the same workflow). 0.6 update: FULL (post-text only, with the walkthrough unviewed — captions unobtainable, download blocked by the bot sign-in wall). Distinct from `minimax-h3-character-swap-comfyui`, `minimax-h3-character-swap-nomask-lowvram`, and `minimax-h3-reference-video-character-swap`: H3MD is a different tool (comfy-h3md-director) with a keyframe-plan step and identity tracking for up to five people at once.
