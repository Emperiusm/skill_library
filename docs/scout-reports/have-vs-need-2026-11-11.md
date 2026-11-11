# Video tooling scout: have-vs-need — 2026-11-11

Daily run. Depth mode: `pre-approved` (max 2 media downloads, Ehsan 2026-09-27).
Window: last 2 days of posts. Deep-analysis cap: 8 videos.

## Gap alerts

**GAP ALERT — Aegis P1 rigging / skinning / animation-retarget gap, meaning-match.**
"Fable 5.1 + GEM-X markerless mocap -> animation on any Blender skeleton"
(Sacred_B, r/aigamedev, post 1xt9uhh, score 70, 23 comments) demonstrates
exactly the stage the Aegis foundry lacks: video of real boxers/UFC fighters
is turned into animations the author says attach "to any skeleton in
Blender", using NVlabs GEM-X running locally (author claims a 3060 Ti is
enough) plus a Blender plugin to tweak and finalize. The build path is
agentic, not a product: Fable 5.1 wrote a design doc, then high-effort
Opus 5.5 subagents built the tool from that doc in 2 days (~3.5-5M tokens).
Caveats, stated plainly: the code is NOT public (the author declined to
share the plugin; Claude flagged commercial-use limits on the model, and
much of the workflow is CLI, so the plugin alone may not help), the initial
prompt was not saved, and the design doc sits behind a LimeWire link that
was not retrieved this run. So this is a lead with a demonstrated
capability, not a drop-in: the retarget-to-any-skeleton claim is shown in
the clip and stated by the author, but no code or doc was verified. The
prepared fix artifact for this gap (`aegis-pipeline/rigging-stage-design.md`)
recommends the Tripo P2.0 route; GEM-X is now a second, video-driven route
worth the same treatment. Next step: retrieve the design doc and reproduce
the pipeline from the author's description on one test clip before treating
it as a candidate stage.

No other extracted tool matches a P1/P2 gap row this run. The H3 Director
Studio V2 continuity work is adjacent to the P1 AI-vendor acceptance-spec
gap only in the loosest sense (it manages continuity, it does not specify
"what good means"), so it is not flagged as a fill. The Claybound look is
look-dev evidence for 2d3d's P1 art-bible gap, not a written bible.

## Videos scanned

**Reddit scan (`bin/scan_videos.py 2`), run twice because Arctic Shift
HTTP 526s vary per run.** First run: 29 video posts; re-run: 37 video
posts. The 526'd subreddit sets differed between the two runs (first run:
GraphicsProgramming, blender, houdini, substance3d, vibecoding,
proceduralgeneration, 3Dmodeling, gamedev; re-run: unity, threejs,
substance3d, comfyui, vfx), so the two runs covered different subs and the
candidate list below is the union of what was visible. 23 subreddits,
min score 20. Coverage is partial: any video in a 526'd sub is invisible
to that run, and the union still misses subs that 526'd in both runs
(substance3d 526'd in both).

**YouTube scan (`bin/scan_youtube.py 2`): 0 videos, all 11 channels failed.
YouTube source is DOWN for this run; Reddit only, per the skill.** The
SSL fix from yesterday (appended the current Hatch egress CA to the
video-summarizer venv certifi bundle; the bundle had rotated to "CA1")
restored channel listings, but every per-video extraction hits YouTube's
"Sign in to confirm you're not a bot" wall. No cookies exist for the
sandbox; do not retry with a signed-in session from here.

Top-ranked by relevance (union): patch.gg 50k assets (41.4), H3 Director
Studio V2 (40.8), MiniMax H3 Image (32.0), RelayVSR (30.4), lowpoly
character (30.4, no tooling), Molec sea-aliens (22.1), Claybound (20.8),
AI pixel art editor (20.7), GLSL editor (20.5, audited yesterday),
10-days game (20.4, no tooling), Milo's Day Shift (13.9), HézFX muscle
sim (2.0 relevance but score 511). Zero-tooling-signal posts were
downweighted and screened out (whale, worm, ocean, surfing game, rolling
chair, giftbow, wave vs wave, krill model, motion poster, stylization gif,
"rough job" gif).

## Audits

### 1. "50,000 open-source assets and three.js game systems [Link Included]" (Important-Respect-12)

Source: https://www.reddit.com/r/threejs/comments/1xt5zvm/50000_opensource_assets_and_threejs_game_systems/ | native Reddit video | r/threejs post 1xt5zvm (score 68, 5 comments)

Tools used: patch.gg asset toolbox (CLI + MCP search over aggregated open
asset stores); three.js systems (procedural dungeons, destruction physics,
fluids and cloth, crowd navigation, realistic car, procedural terrain,
forests, tree generators); 22 CC0 games.

This audit reconstructs the resource the post announces, so another agent
can judge whether it is worth using as an intake source. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it),
and **Why** (the principle). The post's core method is: one searchable
index over 50,000 open assets plus reusable three.js building-block
systems, instead of hunting store by store.

### Phase 1: Search everything at once

**Do**
1. Go to https://patch.gg/create/toolbox/assets (viewing needs no sign-in
   or download, per the author).
2. Search across the whole index at once via the CLI or MCP, rather than
   per-store: the index covers 3D models, textures, 2D assets, splats,
   sounds, and music. More than 5,000 of the 50,000 assets are made by
   the authors; the rest is aggregated from different open-source asset
   stores.
3. Downloading an asset requires signing in (free, per the author, to
   prevent bot attacks).

**Check**
- The asset you need is in the index and its license is open (the
  authors say everything is open-source and usable in your game).
- The download actually works after the free sign-in.

**Why**
- Aggregation is the product: 50,000 assets in one searchable place
  beats 50,000 assets spread across stores nobody checks.

### Phase 2: Take a building-block system and reshape it

**Do**
1. Pick one of the open-sourced three.js systems as a starting block:
   procedural dungeons, destruction physics, fluids and cloth, crowd
   navigation, a realistic car, procedural terrain, forests, tree
   generators.
2. Edit the block to look completely different from the system itself;
   the authors state that is the intent ("these blocks can then be
   edited in any way").

**Check**
- The system runs as a block in your game before you reshape it; the
  authors' motive is bigger reusable blocks, not finished games.

**Why**
- A working system you can reshape is worth more than a finished demo
  you cannot change.

### Phase 3: Take CC0 game aspects wholesale

**Do**
1. Use any aspect of the 22 open-source CC0 games in your own game; CC0
   means no attribution or permission step is claimed by the authors.

**Check**
- Verify the CC0 claim on the game you take from before shipping; the
  authors assert it, this run did not verify any single game's license.

**Why**
- CC0 is the only license class that needs no further clearance work.

### The human method, distilled
1. Aggregate first, then search once (CLI/MCP over everything).
2. Ship building blocks, not finished demos.
3. Make the free tier sign-in-only, not paywalled.

**Depth status:** PARTIAL (full post text + all 5 comments; comments are
praise only; this is a vendor self-promo resource announcement, no workflow
detail, no asset verified, no license verified).

---

### 2. "A very special workplace... [H3 Director Studio V2] Motion Context Dual" (Far_Patience4517)

Source: https://www.reddit.com/r/comfyui/comments/1xs4d9u/a_very_special_workplace_h3_director_studio_v2/ | native Reddit video | r/comfyui post 1xs4d9u (score 39, 14 comments)

Tools used: ComfyUI, MiniMax H3, H3 Director Studio V2
(github.com/M1cr0Bytes/MiniMax-H3-Director-Studio_V2, Civitai 2984987),
ComfyUI-H3-Motion-Context, Spectrum acceleration (BASE branch only),
Comfy Kitchen (mentioned by the author as the accelerator exception).
Commenter-mentioned: ck-attention + sparse attention + giggle turbo LoRA;
geiru_context_suite (end-frame anchoring, suggested, not yet adopted).

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: generate a BASE pass,
review it, keep the accepted BASE, and upscale that exact result with
Latent 3D; Chain carries two separate latents between segments so motion,
audio, sharpness, and detail survive the joins.

### Phase 1: Review the BASE before spending upscale

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

### Phase 2: Run Chain with dual-motion-context

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

### Phase 3: Apply Spectrum acceleration only where it belongs

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

### Phase 4: Watch the two known V2 failure modes

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
3. Note the commenter suggestion the author accepted: geiru_context_suite
   end-frame anchoring
   (github.com/roycho87/geiru_context_suite) for sharpness and color
   drift mitigation in long-video continuation clips. The author replied
   he had not considered it necessary "because I believe version 2 is
   better" but would add it; V1 now lives in the repo's legacy folder
   (legacy/H3_Director_Studio_V1).
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

### The human method, distilled
1. Review the cheap pass before paying for the expensive one.
2. Carry two latents, not one: BASE context for the next BASE, FINAL
   context for the next upscale.
3. Accelerators only on the BASE branch, only non-Turbo, only ~25 steps.
4. Test continuity with motion; static scenes forgive everything.

**Depth status:** FULL (full post text + all 14 comments; the Civitai
workflow file was not downloaded or executed, and no generation settings
beyond the ones quoted above are claimed).

---

### 3. "MiniMax H3 Image is natively supported in ComfyUI on day-0" (Lexius2129)

Source: https://www.reddit.com/r/comfyui/comments/1xsrnze/minimax_h3_image_is_natively_supported_in_comfyui/ | native Reddit video | r/comfyui post 1xsrnze (score 101, 8 comments)

Tools used: ComfyUI (latest version), MiniMax H3 Image checkpoint
(Hugging Face Comfy-Org/MiniMax-H3-Image: diffusion model + VAE +
Qwen3-VL text encoder), MiniMax H3 Image Conditioning node, Comfy-Org
workflow templates (image_minimax_h3_image_t2i.json,
image_minimax_h3_image_edit.json), Comfy Cloud (no-download option),
Prompt Enhancer. Commenter-mentioned: P-H3-Image (community fine-tune),
Z-Image Turbo, MOSS, KREA2, RefMod, MiniMax H3 LoRAs.

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: one checkpoint does
both text-to-image and reference-image editing, natively, in 6 steps.

### Phase 1: Get the weights

**Do**
1. Update ComfyUI to the latest version.
2. Download the diffusion model, VAE, and Qwen3-VL text encoder from
   Hugging Face (Comfy-Org/MiniMax-H3-Image).
3. If you already run MiniMax H3 video, you already have the text
   encoder: H3 Image uses the same Qwen3-VL text encoder as the H3
   video model.
4. Or skip downloads entirely and use Comfy Cloud with the H3 Image
   template.

**Check**
- The text encoder file is the Qwen3-VL one; no second encoder download
  is needed if H3 video is already installed.

**Why**
- Shared encoder is the install win: one heavy file serves both the
  image and the video model.

### Phase 2: Text-to-image

**Do**
1. Load the MiniMax H3 Image template from the Templates panel, or the
   t2i workflow JSON from Comfy-Org/workflow_templates.
2. Leave width and height at 0 for automatic sizing: 2048x2048 for
   text-to-image.
3. Write a long, detailed prompt (up to 4096 tokens); the author says
   detailed descriptions work best, and to use the Prompt Enhancer.
4. The model is CFG-distilled and samples in 6 steps at guidance 1. No
   negative prompt.

**Check**
- Output is generated at its native size, not upscaled: 4096x4096 at
  1:1, 4736x3552 at 4:3, 5024x3360 at 3:2, 5472x3072 at 16:9, 6272x2688
  at 21:9.

**Why**
- Six steps with nothing to tune is the whole point of a distilled
  checkpoint: the workflow is load-template, write prompt, run.

### Phase 3: Reference-image editing

**Do**
1. Load the image-edit workflow JSON.
2. Connect images: `image_1` is the picture being edited; the other
   slots are references.
3. Refer to references in the prompt as `<Picture 1>`, `<Picture 2>`,
   etc.; numbering follows input order.
4. Connect the VAE when you edit, so reference images are anchored as
   latents and not only read by the text encoder.
5. Leave width and height at 0 and the output takes the size of
   `image_1`.

**Check**
- The edit keeps the identity/structure of `image_1`; the references
  change only what the prompt names.

**Why**
- Anchoring references as latents (via the VAE) is what makes the edit
  stick to the source image instead of drifting into a fresh generation.

### Phase 4: Know what the commenters say it does badly

**Do**
1. Expect the official model to be weakest where the community fine-tune
   is strongest: commenters report P-H3-Image is smaller, works at 4M
   pixels (official H3 Image has an 8M minimum, "anything below that is
   pure pixelated slop"), is uncensored, does not change identity when
   used as an edit, and has a LoRA version that "works with every
   Minimax H3 checkpoint I've tried" plus refmods and H3 LoRAs, while
   "Minimax image does none of that. Loras don't register at all."
2. Expect the official model's advantages to be upper resolution limit
   and generation speed: about 30% faster than P-H3 at 8K in one
   commenter's test.
3. Expect failure reports: one commenter gets "completely garbled"
   results at 4-20MP that "look good in preview, but not when zooming
   in to the correct resolution"; another finds results "worse than with
   Z-Image Turbo" and worse than MOSS/KREA2 at 2MP on animated character
   sheets and style consistency.

**Check**
- Judge at full zoom, not in preview; the garbled-at-full-resolution
  report is exactly the failure preview hides.
- Judge identity on edit against P-H3-Image if identity matters more
  than resolution.

**Why**
- A day-0 native integration is a distribution win, not a quality win:
  the community fine-tune is currently the better edit model by the
  commenters' own tests, and the official model's edge is speed and
  maximum size.

### The human method, distilled
1. One checkpoint, two modes: no images means text-to-image, images
   means edit.
2. Six steps, guidance 1, no negative prompt: nothing to tune.
3. Generate at native size; never upscale to reach it.
4. Judge at full zoom, and judge identity against P-H3-Image.

**Depth status:** FULL (full post text + all 8 comments; the model
itself was not run, and no generation beyond the quoted settings is
claimed).

---

### 4. "ComfyUI Tutorial: Fixing MiniMax H3 Video Upscaling Details loss with RelayVSR & DLSS5 Nodes with only 6GB of Vram" (cgpixel23)

Source: https://www.reddit.com/r/comfyui/comments/1xsmep4/comfyui_tutorial_fixing_minimax_h3_video/ | native Reddit video | r/comfyui post 1xsmep4 (score 21, 3 comments; comments unretrievable this run, Arctic Shift 422)

Tools used: ComfyUI, MiniMax H3, RelayVSR
(project page kopperx.github.io/RelayVSR, code github.com/kopperx/RelayVSR,
models Hugging Face Comfy-Org/RelayVSR), NVIDIA DLSS5 nodes, Pika H3
6-step LoRA, attention optimization nodes. Workflow file on Google Drive
(not retrieved); video tutorial https://youtu.be/LJ-jddmGXfk (not
retrieved); Civitai article 38541 (login-walled, description only).

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: do not upscale the
whole video with the large model; let the large model make reference
latents for sparse keyframes and let a lightweight transformer rebuild
every frame from those references.

### Phase 1: Generate small, with the cheap LoRA

**Do**
1. Generate the video at 0.7 MP using MiniMax H3 with the Pika H3 6-step
   LoRA and attention optimization nodes.
2. Author timing: generation at 0.7 MP takes approximately 35 minutes.

**Check**
- The 0.7 MP base is the finished content (framing, motion, identity);
  upscale must not change it, only add detail.

**Why**
- Generating at the target resolution is the slow path; generating small
  and upscaling with references is the fast one, and the LoRA keeps the
  base cheap.

### Phase 2: Upscale with RelayVSR, not with latent upscale

**Do**
1. Run RelayVSR: a large generative model creates high-quality reference
   latents for selected (sparse) keyframes, while a lightweight
   Dual-Memory Video Transformer uses those references to reconstruct the
   remaining frames, preserving the original video structure and details.
2. The transformer reuses keyframe information across frames and updates
   recent video context; it supports first-keyframe conditioning and
   dual-endpoint conditioning with bounded lookahead.
3. The references themselves are optimized by Video-Aware Reference
   Optimization (VARO), which uses reinforcement learning with two reward
   levels: a system-level reward on videos produced by the fixed
   lightweight network, and a reference-level reward on decoded keyframe
   quality. (Inference: the paper's mechanism; the author's post states
   the large-model/small-model split, the project page states VARO.)
4. Combine with NVIDIA DLSS5 nodes in the same ComfyUI chain.
5. Author timing: upscaling to 2K with RelayVSR + DLSS5 takes
   approximately 7 minutes, on 6 GB of VRAM. For comparison, MiniMax
   latent upscaling takes approximately 45 minutes on the same job.

**Check**
- Compare the upscaled frames against the original: conventional
  upscaling "can sometimes modify the original video, introduce unwanted
  details, or change the appearance of characters and scenes" (author);
  RelayVSR's claim is that it preserves structure and details instead.
- Paper benchmark (A100 80 GB, 1080p, dual-endpoint, 15-frame keyframe
  interval): 29.29 FPS, 13.82 GB peak GPU memory, 0.327 s first-frame
  latency, vs FlashVSR-Tiny at 7.80 FPS, 24.447 GB, 2.83 s.

**Why**
- A large model on every frame is the cost; a large model on sparse
  keyframes plus a light model everywhere else is the same detail at a
  fraction of the compute. The 7-vs-45-minute comparison is the author's
  proof.

### The human method, distilled
1. Generate small and cheap (0.7 MP, 6-step LoRA).
2. Upscale by reference, not by re-generation: sparse keyframes carry
   the detail, the light transformer carries the frames.
3. Measure against the slow path (45 min latent upscale) or the speedup
   is just a claim.

**Depth status:** PARTIAL (full post text + RelayVSR project-page
abstract/method; comments unretrievable this run; Civitai article
login-walled; Drive workflow file and YouTube tutorial not retrieved.
The tutorial download was attempted under the pre-approved allowance and
failed: egress-proxy TLS, self-signed certificate in chain on
youtubei.googleapis.com via the Android player client; no approval gate
was hit and it was not retried. No ComfyUI node-level settings are
claimed.)

---

### 5. "I'm getting a little weirded out by how functional my purely vibed tool ended up being." (Sacred_B)

Source: https://www.reddit.com/r/aigamedev/comments/1xt9uhh/im_getting_a_little_weirded_out_by_how_functional/ | native Reddit video | r/aigamedev post 1xt9uhh (score 70, 23 comments)

Tools used: Fable 5.1, Claude Opus 5.5 subagents (high effort), GEM-X
(NVlabs, Apache 2.0, runs locally), Blender + author-built Blender
plugin (tweak/finalize, not public), design doc (LimeWire link, not
retrieved). Goal stated by the author: "animations that follow from real
life boxers/UFC fighters" and "animations I can attach to any skeleton in
Blender", for a 2D project with a DKC-style 3D-sprite look.

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: write a design doc
first, then let high-effort subagents build a local markerless-mocap tool
from that doc.

### Phase 1: Write the design doc before any code

**Do**
1. Decide the end goal in one sentence: animations from real fighter
   footage, attachable to any skeleton in Blender.
2. Prompt Fable 5.1 to produce a full design doc for that goal.
3. Save the design doc (the author did NOT save the initial prompt, and
   says so plainly; the doc itself is shared via LimeWire).

**Check**
- The doc exists before the build starts; it is the alignment artifact
  the subagents follow.

**Why**
- "Using a structured design doc to keep everything aligned before
  letting the subagents tackle the heavy lifting" is the approach a
  commenter calls genius, and the author confirms it: the doc, not the
  prompts, is what kept a 2-day vibe build coherent.

### Phase 2: Build with subagents in a fresh context

**Do**
1. Open a fresh context, hand it the design doc, and tell it to follow
   the doc.
2. Tell it to spin up high-effort Opus 5.5 subagents to tackle the work.
3. Two days later the author had a working tool. Total production cost
   stated: between 3.5 and 5 million tokens ("I didn't track too close").

**Check**
- The tool runs locally and produces animations from fight footage;
  the author did not expect it to work ("I really didn't think anything
  of it").

**Why**
- Fresh context plus a fixed doc is the repeatability trick: the
  subagents cannot drift from a spec they can re-read.

### Phase 3: Run GEM-X locally on fight footage

**Do**
1. Feed real boxer/UFC-fighter video to the tool; GEM-X does the heavy
   lifting (markerless motion capture from video).
2. Run it locally: the author says the design doc puts the requirement
   at a 3060 Ti. (Author claim; not verified this run.)
3. The output is animation data attachable to any skeleton in Blender.

**Check**
- The extracted motion follows the real fighter's movement; the author
  built it because he does not know how to animate and wanted
  real-life-derived motion.

**Why**
- Markerless video mocap removes the two things the author lacked: a
  mocap rig and animation skill. The model is the animator.

### Phase 4: Tweak and finalize in Blender

**Do**
1. Attach the animation to the target skeleton in Blender.
2. Use the author-built Blender plugin's tweak tool to finalize it
   (the author says the plugin includes a tweak tool he has not yet
   poked at much).
3. The author's end use is a 2D project: the animations drive a
   DKC-style 3D-sprite look.

**Check**
- The animation reads as the fighter's motion on the target skeleton;
  commenters note the trick is "making it look right with a model."

**Why**
- Extracted motion is never clean on first pass; the Blender step is
  where it becomes usable, which is why the author kept a tweak tool in
  the plugin.

### The human method, distilled
1. Doc first, code second; the doc is the spec the subagents cannot
   lose.
2. Fresh context per build; the old context's drift does not carry over.
3. Local model, local run: no cloud mocap service in the loop.
4. The plugin is only part of it; much of the workflow is CLI, and the
   author is explicit that the plugin alone may not help.

**Depth status:** PARTIAL (full post text + all 23 comments; the design
doc was not retrieved, the code is not public, the initial prompt was not
saved by the author, and no per-step parameters are claimed. The
"attaches to any skeleton" capability is demonstrated in the clip and
stated by the author, not independently verified.) **GAP ALERT** (see top
of report).

---

### 6. "Update on the 2.5D Platformer built in three.js where the whole world is clay" (dermosef)

Source: https://www.reddit.com/r/threejs/comments/1xsolnm/update_on_the_25d_platformer_built_in_threejs/ | native Reddit video | r/threejs post 1xsolnm (score 39, 7 comments; comments unretrievable this run, Arctic Shift 422)

Tools used: three.js; sculpted meshes; clay beads; normal maps;
deformable mesh (shapeable clay). Demo: playclaybound.com. Steam wishlist
page exists (Claybound, app 5547840). No engine detail beyond three.js is
claimed.

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: everything is clay
by construction (rounded boxes, noise displacement, normal-map
imperfection), and fire is a particle boil, not a shader.

### Phase 1: Make clay fire from sculpted meshes and beads

**Do**
1. Build flames from sculpted meshes in a boil of clay beads.
2. Beads rise, cool, and drop off as soot.
3. Use one light per fire, not per flame: "Takes away some of the
   vividness, but helps performance."
4. Animate only fires on screen.
5. On weak GPUs, drop the glow core and halve the beads.

**Check**
- The fire still reads as fire with one light and half the beads; the
  fallbacks are the weak-GPU test, not an afterthought.

**Why**
- Per-flame lights and always-on animation are the perf cost; the
  author's rules cap both where the player cannot see the difference.

### Phase 2: Build the clay look from rounded boxes

**Do**
1. Start every block as a rounded box with a corner radius.
2. Displace it with low-frequency noise for the wobbly silhouette.
3. Put surface imperfections in a normal map, scaled by object size.

**Check**
- The silhouette wobbles (low-frequency noise) while the surface reads
  as handmade clay (normal map); if either is missing, it reads as a
  plain box.

**Why**
- The look is three cheap decisions stacked: round the corners, wobble
  the silhouette, dirty the surface. No single step carries it.

### Phase 3: Make clay shapeable

**Do**
1. Add a separate deformable mesh driven by the player's drag, so the
   player can shape the clay directly.

**Check**
- Dragging deforms the mesh in play; the deformable mesh is separate
  from the static blocks, so shaping never breaks the level geometry.

**Why**
- Interactivity is a separate mesh because the static world and the
  shaped clay have different jobs; merging them would make one of them
  worse.

### The human method, distilled
1. One light per fire, not per flame; animate only what is on screen.
2. The look is three decisions: rounded box, noise wobble, normal-map
   imperfection scaled by size.
3. Weak-GPU fallbacks are designed in (drop the glow core, halve the
   beads), not patched on.

**Depth status:** PARTIAL (full post text; comments unretrievable this
run; no code, parameters, or render settings disclosed).

---

### 7. "My idle RPG is a pop-up diorama in a transparent, click-through window that turns as you drag it" (limericksforyoursoul)

Source: https://www.reddit.com/r/godot/comments/1xsrs7r/my_idle_rpg_is_a_popup_diorama_in_a_transparent/ | native Reddit video | r/godot post 1xsrs7r (score 193, 18 comments)

Tools used: Godot; flat pixel-art cutouts (character sprites by beowulf
on itch.io; other art from assorted itch asset packs); tutorial video
linked by the author (https://www.youtube.com/watch?v=tNL8bKycdjk, not
retrieved, YouTube bot wall). Steam page: Milo's Day Shift (app 5443940).
Windows and Mac planned end of month; Linux untested.

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: a 3D scene of flat
cutouts on a slab, shown in a borderless transparent window whose
click-through shape and camera angle both follow the window itself.

### Phase 1: Build the diorama scene

**Do**
1. Build a 3D scene of flat pixel-art cutouts on a little slab, Paper
   Mario style.
2. Render 2D character sprites inside the 3D scene and add shadows and
   lighting effects for depth; the author describes the target look as
   HD-2D (Octopath Traveler-like depth of field is the reference he has
   not tried personally).

**Check**
- The scene reads as a little living diorama, not a flat picture: the
  cutouts, slab, shadows, and lighting have to sell the depth.

**Why**
- Flat sprites in a 3D scene get depth for free from the renderer;
  drawing depth by hand would cost far more than staging it.

### Phase 2: Make the window transparent and click-through

**Do**
1. Render into a borderless, transparent window.
2. Make only the diorama itself take clicks: the window's mouse
   passthrough follows the diorama's outline, so everything around it
   goes to the apps behind.

**Check**
- Clicks outside the diorama outline land in the app behind the window;
  clicks on the diorama land in the game.

**Why**
- A desktop companion that blocks clicks is a nuisance, not a companion;
  the outline-shaped passthrough is what makes it livable on a work
  desktop.

### Phase 3: Turn the diorama as the window moves

**Do**
1. Make the camera angle follow where the window sits on the screen, so
   when the user drags the window around, the diorama turns to face
   them.

**Check**
- Drag the window to a different screen position and the diorama has
  turned; the view is a function of window position, not a fixed shot.

**Why**
- The trick is the whole concept: the window is not a frame around a
  fixed scene, it is a viewport the user moves through the scene.

### Phase 4: Split logic from visuals so offline time is just simulation

**Do**
1. Keep the game logic separate from the visuals.
2. The time the game spends working while closed is just the same
   simulation run forward.

**Check**
- Closing and reopening the game advances state by exactly the elapsed
  time, with no separate offline-progress code path.

**Why**
- One simulation with two front-ends (live and fast-forward) cannot
  drift apart the way a live sim plus a separate offline calculator can.

### The human method, distilled
1. The window is the viewport: position drives the camera.
2. Click-through follows the diorama outline, not the window rectangle.
3. One simulation, run live or run forward; never two systems.

**Depth status:** PARTIAL (full post text + all 18 comments; no code
disclosed; the author's linked tutorial video was not retrieved).

---

### 8. "Procedurally-animated mechanical sea-aliens in our Spore/Besiege/LEGO game" (foolofaperegrin)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xt17qv/procedurallyanimated_mechanical_seaaliens_in_our/ | GIF (i.redd.it) | r/proceduralgeneration post 1xt17qv (score 104, 7 comments)

Tools used: Molec (molecgame.com), the author's creature-building game;
no engine disclosed. Playtest signup via Google Form.

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: every creature part
has its own motion behaviour driven by an oscillator signal, and the
player drives the oscillators.

### Phase 1: Build creatures from parts

**Do**
1. Build creatures from parts, Spore-first-level meets Meccano/Besiege,
   inside Metroidvania levels.

**Check**
- The creature reads as a built thing, not a single mesh: parts are
  visible and separable.

**Why**
- Parts are the animation unit: if motion attaches per part, the
  creature must be built from parts first.

### Phase 2: Drive each part with an oscillator

**Do**
1. Give every part a custom motion behaviour.
2. Feed each part a signal value from an oscillator, driven by player
   input.
3. Apply the movement to each part with a function; use different
   oscillators and styles, like phase-offsets, across parts.

**Check**
- Parts move with distinct rhythms (phase-offsets visible between
  parts), not in lockstep; the motion follows player input.

**Why**
- One oscillator per part with different phases is the cheapest way to
  get organic-looking multi-part motion without keyframing anything.

### Phase 3: Add triggerable actions

**Do**
1. Give some parts actions and abilities the player can trigger.
2. Iterate on those actions toward combat and other systems.

**Check**
- Triggering an action produces a visible, distinct part behaviour, not
  just a faster oscillation.

**Why**
- Oscillation is the idle state; triggered actions are the gameplay,
  and they have to be a separate layer or every input looks the same.

### The human method, distilled
1. Parts first, motion second: the build system is the animation system.
2. Oscillators, not keyframes, for idle motion; phase-offsets for
   variety.
3. Triggered actions sit on top of oscillation, never inside it.

**Depth status:** PARTIAL (full post text + all 7 comments; GIF only,
no code, parameters, or engine disclosed).

## Re-scan, not re-audited

**Karma Rendering of VQField volumes (ZephirFX, r/Houdini post 1xs84zr,
score 50, 8 comments; also r/GraphicsProgramming post 1xs8aer, score 33,
5 comments, same video).** Already audited 2026-11-10 (audit 3, PARTIAL;
no skill, technology note only). Today's
re-scan shows the same 8 comments retrieved, with no new evidence: the
compression-time comment (200 ms/frame for high-quality VDB, 100
microsecond one-time decompression per VDB spot, cache configurable, 1 GB
VDB rendering in 1 min becomes a 10 MB VQField rendering in 1 min 30 at
half-VDB cache size), the JPEG-analogy blocky-artifact note, and the
NanoVDB comparison are all identical to yesterday's audit. No re-audit,
no skill change. (The GraphicsProgramming cross-post's 5 comments were
not fetched separately; its selftext snippet is the same VQField text.)

**Block based GLSL editor, very WIP! (Nix3220, r/GraphicsProgramming post
1xru0ic, score 25, 3 comments).** Already audited 2026-11-10 (audit 6).
Comments unretrievable this run (Arctic Shift 422 on the post, fallbacks
failed), so no new evidence could be verified. No re-audit.

**Cargo Van (Game Asset) Blender - Version 1.2 (OzgurSRL, r/3Dmodeling
post 1xs0j0v, score 82, 10 comments).** Screened out 2026-11-10 as
NO-TOOLING (empty selftext, praise comments). Re-scan: 10 comments
retrieved, all praise/thanks ("Clean asf", "model and topology is super
clean"). No workflow evidence. No audit.

**Procedurally generated, de_dust-style map (CompetitiveSide9360,
r/proceduralgeneration post 1xryysh, score 53, 3 comments).** Screened out
2026-11-10 as NO-TOOLING. Re-scan: same 2 retrieved comments ("Neat",
"The Dust Backrooms"). No audit.

## Brief notes, not deep-analyzed (cap reached)

**HézFX muscle simulation tool (shirzadbahrami, r/Simulated post 1xsb9bw,
score 511, 29 comments, 25 retrieved).** A muscle simulation tool
release, 5-year personal project, site hezfx.shirzadbahrami.com; breakdowns
on the author's LinkedIn. Post selftext unretrievable this run (Arctic
Shift 422 on r/Simulated, PullPush 526). Comments are critique, not
method: skin attaches too strongly to muscle (needs a softer lower-skin
slide layer so muscle moves independently under skin; "your model really
doesn't look all too different from normal mesh transformations without a
musculature, other than it may retain shape better"), pecs should bulge
arms-down and flatten arms-up. **Depth status:** DEPTH-LIMITED (tool
named, no engine, parameters, or workflow disclosed). Watchlisted as a new
tool. Not deep-analyzed: the 8-video cap was already spent on higher
relevance posts.

**Vector field simulation with my own math library and Vulkan!
(Terrible_Shoulder667, r/GraphicsProgramming post 1xson0r, score 120,
7 comments, 6 retrieved).** Complete little recipe, not deep-analyzed
only because the cap was reached: C# with Vulkan through Silk.NET; formula
typed as text (e.g. F(x, y) = [x, sin(y)]), parsed and compiled at runtime
into one fast delegate; 1,200 to 6,000 particles depending on window size,
integrated with RK4 on the CPU, each with a 24-point trail; everything
drawn colored with one tiny shader and 4x MSAA. All math from Epsilon, the
author's symbolic math library for .NET. Field can depend on time t; the
author suggests feeding audio features (loudness, bass energy) via FFT
for an audio visualizer. Repos: github.com/XBambinoX/VectorField and
/Epsilon. AI-assisted code disclosed. Watchlisted as a new tool. Candidate
for a skill on the next run if re-scanned.

**Improving the procedural world generation for my game (Edudelm,
r/proceduralgeneration post 1xsk5h1, score 87, 9 comments, all
retrieved).** Technique, thin: perlin noise; ridged multifractal noise for
mountains; simulated rain determines rivers and lakes; voronoi places
cities and other locations; map presets default/small/big, default is
400x400 squares shown as pixels in the preview. Turn-based RPG, sandbox
with a main quest. **Depth status:** PARTIAL (named techniques, no
parameters or code). Not deep-analyzed: cap reached. No new skill; the
technique overlaps existing procgen terrain skills.

**AI Native Pixel Art Editor (314t, r/aigamedev post 1xtam9d, score 37,
12 comments, all retrieved).** Claude built "the first ai native pixel
art editor, to allow agents to write pixel art in javascript", six months
ago, before Claude/Codex got good at pixel art; built with old Opus
4.8/5.0. Author: pointing the agent at existing examples helps a lot;
"pretty good at isometric pixel art"; CPU rendering is slow, WebGPU
acceleration is wanted; dark theme exists (top toolbar was cut off in the
clip). Code NOT shared yet ("I'll upload it to GitHub as soon as my adhd
procrastination wears off"). **Depth status:** DEPTH-LIMITED (tool
exists, no code, no workflow detail, comments are requests for the link).
No skill: nothing executable to stage. Watchlist: not added (no
distributable tool yet).

## Screened out (not audited)

- "Walk Action - Rigged Triathlon Girl - Blender" (r/blender, score 22,
  0 comments): empty selftext, no comments. Showcase only.
  **Depth status:** NO-TOOLING.
- "My 10 days progress. You play a dad trying to keep his daughter alive
  after the world ended in a single day. Tools: Opus 5.5, Gemini,
  Blender, Mixamo" (Fluffy-Discussion166, r/aigamedev, score 21,
  4 comments): empty selftext; tools named in the title only; comments
  discuss game design (water scarcity), not workflow. Mixamo is named
  but no retarget detail exists. **Depth status:** NO-TOOLING.
- "Fog, cliffs, water, boat - vibe coded with threejs, blender opus 5.5,
  gpt 6 Astra" (Efficient_Ad8214, r/vibecoding, score 106, 14 comments,
  12 retrieved): empty selftext; tools in the title only; comments are
  praise and unanswered questions (which LLM did which task, tutorial
  please). Commenters note the author posts the same scene every few
  days. **Depth status:** NO-TOOLING.
- "Pixel art shader simulating reflections on lowpoly car glass"
  (zerrot93, r/godot, score 172, 6 comments, all retrieved): selftext is
  only a Twitter link; the single technique sentence from the author is
  "Is a shader, paint pixels and move it with the camera position." No
  shader code, no parameters. **Depth status:** NO-TOOLING (one
  sentence, not a workflow).
- "I created a lowpoly game character in Blender" (r/3Dmodeling post
  1xt9m82, score 20, 2 comments): selftext unretrievable (Arctic 422,
  PullPush 526); scan snippet is "I did everthing in Blender, except
  texturing which was done in Substance painter." One comment disputes
  the "low poly" claim. **Depth status:** NO-TOOLING.
- "Moats for Game Developers" (r/gamedev, score 108, 87 comments,
  YouTube https://www.youtube.com/watch?v=0hQzOgSjIlc): business-strategy
  video (five moats against copied/slop/stolen games: trust, servers...),
  not pipeline tooling. Not audited; comments not fetched.
- "We're excited to announce the winners of the Open Source Higgsfield
  Challenge." (crystal_alpine, r/comfyui post 1xsv43t, score 283,
  23 comments, all retrieved): announcement, not a workflow. Winners'
  repos are the content (Best Overall: ComfyUI Panorama Stickers by
  nomadoor; a 90-apps list is linked in the comments). Freefield, the
  Higgsfield-on-ComfyUI clone, is already watchlisted (2026-10-28).
  Not audited.
- "Blender car animation" (r/blender post 1xtcqho, score 207, 18
  comments), "Edmund Fitzgerald (The Tunnel) Made in Blender"
  (r/blender post 1xt4tal, score 158, 10 comments), "PowerCorp - a love
  letter to hard sci-fi and space written with Godot" (r/godot post
  1xteirn, score 46, 4 comments), "Update on my game: Every spell tier
  in my magic RPG, from 1st to 10th" (r/godot post 1xt800u, score 25, 10
  comments): comments unretrievable this run (Arctic Shift 422,
  fallbacks failed). Flagged as unretrievable, not as absent; no audit.
- Zero-tooling-signal posts downweighted by the scan: "Ever see a whale
  fly?" (godot, score 570), "Yeahhh, some have a really rough job..."
  (3Dmodeling gif), "Krill model" (3Dmodeling), "Experiments with
  stylization" (blender gif), "So... I made a motion poster :D"
  (blender), "Worm" (Houdini), "My attempt at an ocean" (godot),
  "I added an enemy that regenerates skin, muscle and bone" (Simulated),
  "Verse for Blueprint Developers" (unrealengine, YouTube tutorial,
  40 comments, not fetched), "Giftbow looking for its gift" (Houdini),
  "wave vs wave" (Simulated), "Resurrecting the Tortured and the
  Torturers" (3Dmodeling), "A surfing game" (godot), "I've added a
  really needed feature: rolling chair" (godot). None name a pipeline
  tool or stage.

## Have-vs-need: Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Markerless mocap + animation retarget to any skeleton (GEM-X) | Fable/GEM-X boxing tool (audit 5) | NEED | P1 gap: no rigging/skinning/retarget stage in trellis-pipe (aegis-pipeline-inventory.md); fix artifact `aegis-pipeline/rigging-stage-design.md` exists, recommends Tripo P2.0 | **Gap alert, adopt as second route**: retrieve the design doc, reproduce on one test clip; GEM-X (Apache 2.0, local, 3060 Ti claim) is a video-driven alternative to Tripo P2.0 |
| Multi-segment AI-video continuity (H3 Director Studio V2, dual BASE+FINAL latents, BASE review gate) | H3 Director Studio V2 (audit 2) | PARTIAL | No trailer/cinematic stage in the foundry; agentic cinematic row is BACKLOGGED (watchlist 2026-09-27); konte skill exists for multishot AI video | Backlog: adopt the BASE-review gate + dual latents in the next Aegis trailer run; skill expanded, not new |
| Native image model with multi-ref edit (MiniMax H3 Image, 6 steps) | H3 Image native ComfyUI (audit 3) | PARTIAL | intake/ has an image stage; Nano Banana row says define intake's image stage as model-swappable | Watchlist: H3 Image is a new model option for intake; compare on one concept edit; note P-H3-Image is better at small sizes/identity per commenters |
| Reference-latent video upscaling (RelayVSR + DLSS5, 2K in ~7 min) | RelayVSR tutorial (audit 4) | NEED | No video-upscale stage in any repo pipeline | Watchlist: pull the Drive workflow, test on one H3 clip at 6 GB VRAM; 7 min vs 45 min latent upscale is the number to verify |
| Open-asset sourcing via CLI+MCP (patch.gg, 50k assets) | 50k assets (audit 1) | PARTIAL | intake/ exists as the concept-to-input stage; no aggregated-asset search | Watchlist: try one CLI search for a needed asset class; check license/provenance handling against intake's manifest requirements before depending on it |
| Defined look-dev (Claybound clay look) | Claybound (audit 6) | NEED | No art bible / style-family enforcement beyond the protocol registry (inventory NEED) | Watchlist: the clay look is look-dev evidence, not a written bible; useful as a worked example of a three-decision look, not a fill |
| Muscle simulation (HézFX) | HézFX (brief note) | NEED | No character/muscle stage anywhere in the foundry | Watchlist only: no attach point until characters exist |
| Oscillator-driven procedural creature motion | Molec (audit 8) | NEED | No procedural-animation stage in the foundry | Watchlist pattern only; game-specific, no code |

## Have-vs-need: 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Markerless mocap + retarget to any skeleton (GEM-X) | Fable/GEM-X (audit 5) | NEED | P1 production-conversion stage (roadmap rec 20) includes rigging; generated hawk/boar art is still procedural stand-ins | Backlog: GEM-X is a candidate input to the production-conversion stage once a real clip is reproduced |
| Defined look-dev (Claybound clay look: rounded box + noise + normal map) | Claybound (audit 6) | PARTIAL | P1 written art bible gap (roadmap rec 2); 2d3d has projection painting + reference fidelity measurement | Watchlist: use the clay look's three-decision structure as a worked example when writing the art bible; the technique itself is a different aesthetic, not the 2d3d look |
| Transparent click-through diorama window (Godot) | Milo's Day Shift (audit 7) | PARTIAL | 2d3d is Godot 4.7.2; no transparent-window/companion pattern in the repo | Watchlist: transferable Godot pattern for a desktop companion or a 2D/3D presentation trick; skill staged |
| Native image model, multi-ref edit (H3 Image) | H3 Image (audit 3) | PARTIAL | AI image client with fail-closed spend gate (`pipeline/image_client.py`); model-swappable by design | Watchlist: H3 Image is a new model option for the image client; test one concept edit |
| Open-asset sourcing via CLI+MCP (patch.gg) | 50k assets (audit 1) | PARTIAL | Asset installer with manifest + provenance (`pipeline/install_asset.py`) | Watchlist: patch.gg assets would still have to pass the installer/provenance gate; try one search and check the license metadata it returns |
| Oscillator-driven procedural creature motion | Molec (audit 8) | PARTIAL | Procedural rigs are stand-ins for generated hawk/boar art; no oscillator-driven motion stage | Watchlist pattern: cheap organic multi-part motion without keyframes; candidate for the procedural-rig stand-ins |
| Vector-field visualizer (runtime formula compile, RK4, one shader) | Vector field (brief note) | NEED | No sim-visualization stage in 2d3d | Skip for now: no attach point; note kept for a future skill if re-scanned |
| RelayVSR video upscaling | RelayVSR (audit 4) | NEED | No video stage in the 2d3d pipeline (video is an asset source, not an output) | Skip: trailer/upscale bucket, not a 2d3d pipeline stage |

## Have-vs-need: Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Open-asset sourcing via CLI+MCP (patch.gg) | 50k assets (audit 1) | PARTIAL | Standalone asset pipeline (`tools/`, Blender sprite render + procedural authoring); AI inputs optional (`tools/tripo_key.py` etc.) | Watchlist: CC0 assets are a sourcing option, but the Blender path is the proportion-faithful one (TRELLIS route retired); any patch.gg asset still has to pass the sprite contract |
| Procedural world gen (perlin + ridged multifractal mountains + simulated rain rivers + voronoi cities) | Procgen world (brief note) | PARTIAL | Procedural authoring (`tools/procedural_art.py`, `tools/city_*`, `tools/procgen_*`) | Watchlist: mountain/river techniques are transferable to Desktop City terrain; the 400x400 map + presets pattern matches the city generator's approach |
| Multi-segment AI-video continuity (H3 Director V2) | H3 Director V2 (audit 2) | NEED | No trailer stage in Desktop City | Watchlist only: trailer bucket |
| Transparent click-through window (Godot) | Milo (audit 7) | NEED | Desktop City is Godot 4.7.2; no transparent-window pattern | Watchlist: the pattern could serve a desktop-companion city view, but that is not in the PRD; no action |
| Clay look / GEM-X / Molec / HézFX / RelayVSR | audits 4-6, 8 | NEED (n/a) | No attach point: Desktop City is fixed-view isometric sprites; no characters, no video output | Skip: aesthetics and rigs do not transfer to the sprite pipeline |

## Have-vs-need: Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Markerless mocap + retarget (GEM-X) | Fable/GEM-X (audit 5) | HAVE (alternative) | Rigging stage present (`stages/rig.py`, `assetpipe/blender/rig.py`); Solarempire already rigs, unlike Aegis | Watchlist: GEM-X is an alternative mocap input to the existing rig stage, not a gap fill; no action unless the current rig input proves insufficient |
| Native image model, multi-ref edit (H3 Image) | H3 Image (audit 3) | PARTIAL | Concept PNG is visual authority; Meshy GLB is the bake source | Watchlist: H3 Image multi-ref edit is a concept-iteration option before the audit stage; test one concept edit |
| Open-asset sourcing via CLI+MCP (patch.gg) | 50k assets (audit 1) | PARTIAL | Pipeline ingests Meshy GLB + concept PNG; glTF/GLB is source of truth | Watchlist: open assets are an alternative input, but they must still pass audit/prepare/segment/retopo; try one search |
| RelayVSR / H3 Director V2 / Claybound / Milo / Molec / HézFX | audits 2, 4, 6-8 | NEED (n/a) | No video/trailer stage, no character stage beyond the rig, no clay aesthetic | Skip: no attach point in the asset pipeline |

## Watchlist trending

- MiniMax H3 Chain Director V1.0 (ComfyUI Director node, Single + Chain modes) (first seen 2026-10-25, status BACKLOGGED; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-11 [2026-11-11: H3 Director Studio V2 by the same author (Far_Patience4517), dual-motion-context BASE+FINAL latents; skill expanded with V2])
- Pruna P-H3-Image (distilled MiniMax H3 image model + 4B text encoder, ComfyUI) (first seen 2026-11-05, status WATCH; seen again 2026-11-11 [2026-11-11: commenters in the official H3 Image thread compare P-H3-Image favorably (smaller, uncensored, keeps identity on edit, LoRA version works with H3 checkpoints); discussion only, not a workflow use])

False auto-matches corrected this run (token overlap on "MiniMax H3",
not genuine reappearances; bracketed notes added in place, per file
convention): comfyui-minimax-h3-studio (SAM3 character-swap), 2x2
storyboard-grid reference prompting, Automated AI documentary pipeline,
IV Studio. The trend script over-matches on the shared "MiniMax H3"
tokens; every match it reported was verified by hand against today's
videos before being kept.

New watchlist rows appended (8): RelayVSR (large-small collaboration
video super-resolution); MiniMax H3 Image (official, native ComfyUI);
GEM-X markerless motion capture -> any Blender skeleton; patch.gg asset
toolbox (50k open assets, CLI + MCP); HézFX muscle simulation; Epsilon
symbolic math library + VectorField visualizer; Claybound clay look;
Godot transparent click-through diorama window.

## Gap recommendations (highest leverage)

1. **GEM-X as the second route into the Aegis P1 rig/retarget gap.**
   What it replaces/unblocks: the foundry has no rigging, skinning, or
   retarget stage at all; the prepared fix recommends Tripo P2.0, which
   needs clean 4-view turnaround input. GEM-X takes real video instead,
   runs locally (Apache 2.0), and outputs animations for any Blender
   skeleton. Concrete next step: retrieve the author's design doc
   (LimeWire link in post 1xt9uhh) and reproduce the pipeline on one
   boxing clip; if the retarget holds, it becomes the video-driven leg
   of the rigging stage alongside Tripo.
2. **H3 Director Studio V2 dual-motion-context as the Aegis trailer
   continuity pattern.** What it unblocks: multi-segment AI trailers
   that currently drift at the joins (sharpness/detail steps, audio
   breaks). The BASE-review gate plus separate BASE/FINAL latents is a
   concrete, adoptable discipline, and the failure modes (blur after
   segment 4-5 in continuous takes, background jumps at cuts in
   high-motion scenes) are the acceptance test. Next step: use V2's
   BASE-review gate on the next Aegis trailer run; the skill is expanded.
3. **RelayVSR as the H3 upscale path (verify the 7-vs-45-minute claim).**
   What it replaces: MiniMax latent upscaling, which the author times at
   ~45 minutes against RelayVSR + DLSS5 at ~7 minutes to 2K on 6 GB
   VRAM. Next step: pull the Drive workflow and run it on one H3 clip;
   if the detail-retention claim holds, it becomes the standard upscale
   stage for every H3 video in the library.
4. **MiniMax H3 Image as an intake image-model option.** What it
   unblocks: intake's image stage is defined as model-swappable; H3
   Image adds native 6-step generation and multi-reference editing with
   a shared encoder (no new text-encoder download for H3 video users).
   Next step: run one concept edit through it and compare identity
   retention against P-H3-Image, which commenters currently rate better
   at small sizes.
5. **patch.gg CLI+MCP search as an intake sourcing option.** What it
   unblocks: intake currently has no aggregated-asset search; 50,000
   open assets plus 22 CC0 games in one searchable index is a sourcing
   step the pipeline lacks. Next step: try one CLI search for a needed
   asset class and check what license/provenance metadata comes back,
   since intake's manifest requirements are the gate it must pass.

## Explicit non-goals

- "Moats for Game Developers": business strategy, not pipeline tooling.
- Higgsfield Challenge winners announcement: a list of repos, not a
  workflow; Freefield already covers the Higgsfield-on-ComfyUI pattern.
- HézFX as an adoptable tool: a 5-year personal project with no disclosed
  engine, parameters, or workflow; watchlisted, not adoptable from this
  evidence.
- AI Native Pixel Art Editor: real tool, code unshared; nothing to adopt
  until the author publishes it.
- Claybound clay look as the 2d3d look: a worked three-decision aesthetic
  for a different game, not the 2d3d art bible.
- Milo's transparent window as a Desktop City feature: the pattern is
  transferable, but a desktop-companion city view is not in the PRD.
- The 50k-asset index as a verified source: no asset or license was
  verified this run; it is a sourcing lead, not a vetted library.

## Depth-escalation usage and run notes

- Downloads attempted: 1 of 2 allowed. Downloads succeeded: 0.
  Downloads skipped: 0 after the attempt (none other attempted). No
  approval gate was hit anywhere in this run.
- The one attempt was the RelayVSR tutorial (YouTube, youtu.be/LJ-jddmGXfk),
  low quality, via `yt_download.py`. It failed fast with SSL
  CERTIFICATE_VERIFY_FAILED (self-signed certificate in chain) on
  youtubei.googleapis.com via the Android player client. Per the skill,
  it was not retried. A direct run of the venv yt-dlp with the Android
  client fails the same way, while the same binary's channel-tab listing
  works (youtube.com validates after the CA fix). Diagnosis: the proxy
  presents a genuine Google cert to openssl s_client for
  youtubei.googleapis.com, so the MITM leaf yt-dlp sees could not be
  compared directly; the practical result is that YouTube video fetches
  (metadata and media) are blocked from this sandbox while channel
  listings work. The second download allowance was not used: the only
  other YouTube-linked item (Milo's tutorial, youtu.be/tNL8bKycdjk)
  would hit the same wall, and the eight audited videos are otherwise
  native Reddit clips whose tooling signal is in post text and comments.
- Cert fix applied (again): appended the current Hatch egress CA
  (/usr/local/share/ca-certificates/hatch-egress-ca.crt) to the
  video-summarizer venv certifi bundle
  (~/workspace/skills/video-summarizer/.venv/lib/python3.12/site-packages/certifi/cacert.pem).
  The venv bundle had no Hatch CA in it (the system CA has rotated; its
  subject is now "Hatch Sandbox Egress CA1"). This restored yt-dlp
  channel listings; the YouTube bot wall at per-video extraction and
  the youtubei TLS failure are separate, unrelated blocks. Also note:
  `yt_download.py` resolves yt-dlp via `shutil.which` first, so it
  picks the system binary, not the venv one; the venv binary fails the
  same way on the video API host, so this is not the cause.
- Scan warnings: the Reddit scan ran twice; the 526'd sub sets differed
  per run (see Videos scanned). Arctic Shift comments search returned
  422 for 8 posts (1xsmep4, 1xsolnm, 1xru0ic, 1xtcqho, 1xt4tal, 1xteirn,
  1xt800u, plus 1xsb9bw selftext); the fetch_comments.py fallbacks (old
  Reddit JSON, PullPush) did not recover them (PullPush 526s on the
  egress proxy; old Reddit returns the bot-wall interstitial). Full
  selftext was retrieved for 14 of 18 target posts via Arctic Shift
  per-subreddit queries; the 4 failures (1xsb9bw Simulated, 1xt9m82
  3Dmodeling, 1xs84zr Houdini, 1xru0ic blender) fell back to PullPush,
  which 526'd. A service restart mid-run cleared /tmp (the selftext
  fetcher was re-run with incremental saves and recovered).
- Comment fetching: post IDs from permalinks throughout (yesterday's
  lesson: never the v.redd.it ID). 25 of 29 HézFX comments, all 23
  Fable/GEM-X comments, all 18 Milo comments, all 14 H3 Director V2
  comments, all 8 H3 Image comments, all 12 pixel-editor comments,
  all 7 Molec comments, all 9 procgen-world comments, all 6 vector-field
  comments, all 5 patch.gg comments retrieved via Arctic Shift.
- Watchlist repair: see the Watchlist trending section. The trend
  script's token-overlap matching over-matches on shared tokens
  ("MiniMax H3"); future runs should pass specific multi-word tool
  names (done this run) and verify every reported match by hand
  against the day's videos (done this run; 4 false matches corrected
  in place).
- Dedup: VQField, GLSL editor, Cargo Van, and de_dust map are re-scans
  of 2026-11-10 items, not re-audits. H3 Director Studio V2 expands
  the existing `minimax-h3-chain-director` skill (same author, same
  workflow, V2 evolution); it is not a new skill. MiniMax H3 Image is a
  new skill (official model, distinct from the community P-H3-Image
  skill `pruna-p-h3-image-comfyui`).

## skill_library artifacts staged

- EXPANDED: `skills/ai-video/minimax-h3-chain-director/SKILL.md` — V2
  section (dual-motion-context BASE+FINAL latents, BASE review gate,
  direct BASE+Upscale mode, Spectrum rules, V2 failure modes: blur after
  segment 4-5, background jumps at cuts, geiru_context_suite
  end-frame-anchoring suggestion accepted by the author).
- NEW: `skills/ai-video/minimax-h3-image-native-comfyui/SKILL.md` —
  official H3 Image, 6 steps, native resolutions, multi-ref `<Picture N>`
  editing, VAE anchoring, P-H3-Image comparison from comments.
- NEW: `skills/materials-shaders/clay-look-threejs-claybound/SKILL.md` —
  clay fire, clay look, shapeable clay, weak-GPU fallbacks.
- NEW: `skills/engine-runtime/godot-transparent-clickthrough-diorama-window/SKILL.md` —
  transparent click-through window, outline passthrough, camera
  follows window position, logic/visuals split.
- Report copy: `docs/scout-reports/have-vs-need-2026-11-11.md`.
- Watchlist rows synced to the repo mirror
  (`video-tooling-scout/references/tooling-watchlist.md`).
- README tables updated (skills/README.md grouped table; root README
  skill count and category counts only).
