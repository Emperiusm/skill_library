# video-tooling-scout daily report — 2026-10-03

Depth mode: `pre-approved`, max 2 media downloads per run (enabled by Ehsan 2026-09-27).
Date range: last 2 days (Oct 1–3, 2026). Subreddits: unity, unrealengine, godot,
blender, houdini, substance3d, photogrammetry, gameassets, topology, aigamedev,
comfyui, vibecoding, technicalart, proceduralgeneration, vfx, Simulated, 3Dmodeling, gamedev.

## Gap alerts

**No hard P1 gap alerts today.** No extracted tool fills a described P1/P2 gap
(a match = a tool that fills the described need, by keyword or meaning). Two
gap-relevant findings below inform open gaps without filling them:

- **P1 acceptance-spec gap (aegis intake/): informed, not filled.** mexxmillion's
  per-shot lock lists (audit #3) are the working practice the gap asks for:
  every shot ships with an explicit "NOT ALLOWED TO CHANGE" list
  (shot 24: the woman, the flags, camera angle, background, only 2 people) plus
  frame-by-frame QC rejection notes. This is "what good means" operationalized
  as a per-job record. Recommendation: adopt the practice (lock-list template
  in intake/ acceptance records), not the tools.
- **P1 rigging/skin/retarget gap (aegis trellis-pipe): weak adjacent signal, not filled.**
  HBLink's Characters feature (beta) transfers Blender rigs to KineFX/APEX and
  the author tested Mixamo clips on a Blender rig ("worked just fine") — the
  mocap-clip-onto-rig pattern the gap eventually needs. But it is a paid
  DCC-bridge plugin in beta, not a foundry stage, and does no auto-rigging or
  skinning. Gap stays open; keep Mixamo clips as the acceptance set when the
  stage is built.

## Scan summary

- **Videos scanned:** 8 (score ≥ 20, 18 subreddits, 2 days).
- **Deeply analyzed:** 3 FULL audits (#1–3), 1 DEPTH-LIMITED (#4), 1 KNOWLEDGE
  distillation (#5), 3 NO-TOOLING (#6–8, with reasons).

---

## 1. "HBLink is out: Blender ⇄ Houdini" (Itz_Keay)

Source: https://www.reddit.com/r/Houdini/comments/1wv71uh/hblink_is_out_blender_houdini/
(native Reddit video; r/Houdini post 1wv71uh, score 75, 22 comments) | Gumroad
(paid); support via Telegram https://t.me/hblinkplugin (Reddit blocks Gumroad URLs)

Tools used: **HBLink** (Blender↔Houdini bridge add-on; tested on Houdini 22 and
Blender 5.2, Windows), Houdini SOPs/Solaris/Karma, Blender, USD, Alembic, VDB,
Mixamo (beta character transfer), free test rig Rogue_Rig_v3 by Gutemberg Nascimento.

This audit reconstructs the exact workflow from the author's post text and his
answers in the 22 comments, step by step, so another agent can follow the same
process. Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The tool's core method is:
live for iteration, cache for replay, point clouds for anything with topology
churn.

### Phase 1: Set up the live link

**Do**
1. Install HBLink on both sides. Connect Blender → Houdini over a local socket
   on your own machine. Author: "Live mode sends data directly between Houdini
   and Blender over a local socket on your own machine. There's no intermediate
   file, just a small message format with the geometry data."
2. Push live geometry, UVs, attributes, and materials from Blender into Houdini
   SOPs; or push the whole scene into Solaris with Karma-ready materials,
   lights, cameras, and a matching sky.

**Check**
- Geometry lands in SOPs; materials arrive Karma-ready; lights/cameras/sky
  match between apps.

**Why**
- No intermediate file means no export/import round-trip tax while iterating.

### Phase 2: Transfer simulations with ready-made shaders

**Do**
1. In Houdini, run pyro, FLIP, RBD, cloth, particles, or hair.
2. Send live or cached into Blender; HBLink supplies ready-made shaders on the
   Blender side.
3. In Blender's sidebar panel, drive colour gradients, size ramps, hair taper,
   retiming with smooth slow motion, and instancing — "all from one sidebar panel".

**Check**
- Per the author, it is "just a setup with three nodes in Houdini and a panel
  in Blender that updates parameters based on the imported simulation you
  select within Blender. Curves will provide different parameters, as will
  VDB and particles."

**Why**
- The parameter panel re-binds to whatever sim type is selected, so one UI
  covers every sim class instead of per-type scripts.

### Phase 3: Cache mode with smart invalidation

**Do**
1. For replay, cache: "Cache mode writes standard Alembic (.abc) files, plus
   VDB for volumes, along with a small JSON file that tells Blender how to
   rebuild materials and settings." Blender → Solaris goes through USD.
2. For RBD specifically, use the point-cloud recipe instead of Alembic
   hierarchies: cache the fracture pieces once (rest frame), then write a
   tiny per-frame point file carrying transform + velocity; Blender plays it
   back as instances. Author: "live link was doing that but rbd now caches
   the pieces once plus a tiny per-frame point file (transform + velocity),
   and Blender plays them back as instances. No Alembic hierarchy, and about
   35× smaller per frame in my test."
3. Let smart caching invalidate: it "knows when a cache is outdated, resumes
   interrupted caches."

**Check**
- Interrupted cache resumes instead of restarting; RBD playback file size is
  roughly 35× smaller than the Alembic-hierarchy equivalent in the author's test.

**Why**
- Alembic point-level or hierarchy caches are the known pain point (commenter
  Randalix: "with alembic it is ugly. inefficient. either cache point level
  or have a stupid slow hierarchy cache"). Rest-frame + transform/velocity
  point cloud is the Houdini-side answer: cache rest fracture (single frame)
  plus the simulation point cloud.

### Phase 4: Share custom attributes and groups

**Do**
1. Rely on automatic sharing for the important attributes.
2. For custom attributes or groups, select them in the HBLink tab to include
   them. Author: "The important attributes will automatically share. If you
   need custom attributes, you can send those by selecting them in the tab,
   same with groups."

**Check**
- Selected attributes arrive in the other DCC; unselected ones do not bloat
  the transfer.

**Why**
- Explicit attribute selection keeps the small message format small.

### Phase 5: Transfer characters (BETA)

**Do**
1. Send a Blender rig to KineFX / APEX; apply Mixamo clips to the rig.
2. Test rig provided free: Rogue_Rig_v3 by Gutemberg Nascimento.

**Check**
- Author: "It's still a beta feature. I tested a few Mixamo clips with a
  Blender rig, which worked just fine. I'm definitely going to improve it in
  a few weeks."

**Why**
- Mocap-clip-onto-rig is the fastest way to validate a retarget path before
  building a real one. (Inference: this is the author's testing method, not
  an auto-rigging claim.)

### The human method, distilled

1. **No intermediate file while iterating; standard files for replay.**
   Socket for live, Alembic/VDB/JSON for cache.
2. **Cache the rest, stream the motion.** One rest fracture + per-frame
   transform/velocity point cloud beats any hierarchy cache (35× in test).
3. **Rebuild materials from a sidecar, not from the cache.** The JSON file
   tells Blender how to rebuild materials and settings — the cache carries
   motion, the sidecar carries intent.
4. **Panel binds to selection.** Three Houdini nodes + one Blender panel that
   re-binds parameters to whatever sim is selected.
5. **Test retarget paths with Mixamo clips before building anything.**

### Failure modes (from the comments)

- **Alembic hierarchy pain** (Randalix): solved by the point-cloud recipe above.
- **Gumroad links banned on Reddit**: distribution is via DM/Telegram
  (https://t.me/hblinkplugin); commenters kept asking "Link?".
- **Unclear comparison**: asked how HBLink holds up against Blendini, the
  author replied only "Nah Same issue" — ambiguous, do not read more into it.
- **Beta character transfer**: Mixamo clips worked on the author's test rig;
  wider rig coverage is "in a few weeks", not now.

**Depth status:** FULL (post text + 22 author/peer comments; no transcript exists
for native Reddit video; no media download needed — the technique details are
author-stated with numbers).

---

## 2. "Super Simple MiniMax Character Swap Workflow Probably the Best Local Method Out Right Now" (Pleasant-Living-3702)

Source: https://www.reddit.com/r/comfyui/comments/1wvff4i/super_simple_minimax_character_swap_workflow/
(native Reddit video; r/comfyui post 1wvff4i, score 146, 33 comments)

Tools used: **ComfyUI** + **comfyui-minimax-h3-studio** (MIT,
https://github.com/BiggerFishy/comfyui-minimax-h3-studio; simplified by the
author from https://civitai.red/models/2855941/minimax-h3-character-replacement),
**SAM3** (text-prompted segmentation), **MiniMax H3** (video generation).

This audit reconstructs the exact workflow from the author's post text and his
answers in the 33 comments, step by step, so another agent can follow the same
process. Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The workflow's core method is:
describe the finished result, mask the who, invert the mask, let the model
repaint.

### Phase 1: Install and load the workflow

**Do**
1. Install ComfyUI and the comfyui-minimax-h3-studio workflow (GitHub zip).
   The latest release adds a LoRA loader and an easier video trimmer.

**Check**
- The main controls live in the **green settings node in the middle**; the
  complicated nodes are tucked away.

**Why**
- The author's design goal was plug-and-play: "I tried to make it as plug and
  play as possible."

### Phase 2: Save the character once

**Do**
1. Store a reference image together with a detailed character description;
   reload both whenever the character returns. Author: "This is probably my
   favorite feature. Save a reference image together with a detailed character
   description, then load both again when you want to use that character in
   another video."

**Check**
- Switching back to an old character needs no retyping.

**Why**
- Descriptions are the expensive part; caching them is the whole convenience.

### Phase 3: Trim the source video in-workflow

**Do**
1. Pick the section to edit with the built-in trimmer — no external editor.

**Check**
- The trimmer is functional but plain ("The trimming UI could be fancier, but
  it works").

**Why**
- Staying in one app keeps the loop tight.

### Phase 4: Mask with SAM3

**Do**
1. Choose a masking mode: **SAM3** (describe the target, e.g. type "the man"
   or "the woman" in the sam3 prompt box), **Rectangle** (draw a box), or
   **No mask** (re-render the whole frame).
2. Note the author's history: "Originally the workflow used qwen with rules
   to describe the character and it also described the video. It worked
   sometimes and other times it sucked.. I removed it because it took too
   long to describe the video." A plug-and-play Qwen auto-fill would need a
   good rule set AND would only know the target if there is exactly one
   character.

**Check**
- SAM3 prompt box contains a plain description of the target ("the man").

**Why**
- Explicit text masks beat flaky auto-description for reliability.

### Phase 5: Invert the mask, then generate

**Do**
1. The workflow **inverts the colors inside the selected area before
   generation**. Author: "This helps MiniMax replace the subject more
   consistently."
2. Feed the source video (guides mouth movements, body movement, scene) and
   the reference image (guides the replacement's appearance).
3. Use the author's character-sheet tip: "I also found that using a character
   sheet is very useful."

**Check**
- The inverted-color region is exactly the character to replace; the rest of
  the frame is the motion/scene guide.

**Why**
- Inversion is the mask made legible to the model: an unmistakable "repaint
  here" signal. (Inference: the author treats it as a conditioning trick, not
  a documented H3 feature.)

### Phase 6: Set generation parameters

**Do**
1. Start from the example settings: Seed **Fixed** for reproducibility, then
   switch Seed behavior to **Randomize** to explore.
2. Target megapixels: **0.8 MP** (the demo setting); try **1.0 MP** for higher
   resolution; the author does not usually go above that.
3. Keep everything else at defaults for the first run.

**Check**
- Author's measured setup: **RTX 4090 (24 GB VRAM), 32 GB DDR5, 3-second
  video, 0.8 MP → about 2 minutes 30 seconds.**

**Why**
- Defaults-first is the fastest route to a first good take.

### Phase 7: Prompt for the finished result

**Do**
1. Describe the finished result, in detail. The author's working prompt:
   "A barn owl man wearing white polo shirt stands in the middle with
   feathers on his arms and neck, as women crowd around feeling him up and
   down."
2. He also tested the degenerate prompt (video prompt only, "the man" in the
   sam3 box) and "got basically the same result" — but warns simple prompts
   like "swap the man in this video with a barn owl" will "probably not
   result in a decent gen."

**Check**
- Author's principle: "in my workflow its important to describe the finished
  result." Detailed prompts produce better results; matching the seed "doesn't
  guarantee an identical result on every setup."

**Why**
- The model fills what the prompt leaves vague; finished-result description
  is the control surface.

### The human method, distilled

1. **Mask the who, invert it, repaint.** SAM3 finds the person; color
   inversion marks the repaint zone unmistakably.
2. **Describe the finished result**, not the edit.
3. **Save characters, not prompts.** Image + description cached as a unit.
4. **Resolution is a quality lever, not a speed lever.** Cropping at the same
   0.8 MP concentrates detail but makes clean re-blending hard; "using a high
   quality (resolution) video will give you back just as high as a resolution
   result already though."
5. **Expect failures; iterate.** "None of these modes are perfect. It may take
   a few attempts."

### Failure modes (from the comments)

- **Transitions/effects wash out.** On a TikTok multi-clip edit, "the edits
  transitions and effects like blurs and filters and flashes kinda went away
  but the character themselves stayed practically the same"; detailed prompts
  preserve them better.
- **OOM on long videos.** A 4070 Ti user runs a looping system (30–40 s
  before OOM, 64 GB system RAM caching); shareable prompt: "Replace only the
  original performer in <Video 1> with <Subject 1>. <Subject 1> is the person
  shown in <Picture 1> and <Picture 2>. <Picture 1> supplies face and identity
  details. <Picture 2> supplies full-body appearance."
- **Qwen auto-description was hit-or-miss and slow** — removed, not coming back
  without a solid rule set.

**Depth status:** FULL (full post text + 33 comments; author-stated numbers
throughout; no transcript exists for native Reddit video).

---

## 3. "I Put Myself in a Music Video — The Breakdown" (mexxmillion)

Source: https://mexxmillion.github.io/h3-digital-double-story/breakdown/ (full
written breakdown; the explainer video itself was made with agentic workflows,
Qwen Image 2.1, Minimax Music, Qwen TTS) | r/comfyui post 1wvf3b9 (score 76,
8 comments)

Tools used: **MiniMax H3** (video generation; shot 24: 1344×768, 8 steps,
ACC LoRA), **SAM3** (per-frame character masking), **ComfyUI** front-end
("Pocket AI": H3 video, Qwen Image, Krea 2, voice workflows in one place),
**Tensor Master** (job dispatcher: queues, GPU scheduling, Vast GPU rental
with prepared profiles), **RTX 3090** (home) + rented **RTX 5090s** on Vast,
phone UI for queue monitoring, **Genjutsu** on Higgsfield (commercial
comparison model).

This audit reconstructs the exact production method from the author's full
written breakdown and the post comments, step by step, so another agent can
follow the same process. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle). The
production's core method is: keep everything, swap the guy — 45 seconds is
30 jobs.

### Phase 1: Audition the character (character sheets)

**Do**
1. Generate candidate character sheets and reject in rounds: rock star ("TOO
   MUCH ROCK STAR", felt like a costume), studded hat ("TOO COWBOY THE HAT"),
   street cap ("CLOSER… STREET CAP"), braids ("NAH BRAIDS").
2. Land on: own loose black hair with silver streaks, sunglasses, tank top,
   tattoos, layered chains — "Something I'd actually (almost) wear."
3. Lock the final look as a character sheet (costume/hair, with and without
   glasses — "because the glasses come off in some shots") placed next to the
   author's real portrait, "so the styling can go wild while the face stays…
   actually mine."

**Check**
- The look reads as the person, not a costume.

**Why**
- Separating identity (portrait) from styling (sheet) lets styling go wild
  without face drift.

### Phase 2: Turn 45 seconds into 30 jobs

**Do**
1. Slice the video at every edit — "Drums. The floor. Close-ups. A whip pan
   that lasts eight frames. Every cut changes the rules."
2. Give each shot its own job: its own prompt, its own references, and an
   explicit **NOT ALLOWED TO CHANGE** list. Example — JOB · SHOT 24:
   minimax-h3 · 1344×768 · 8 steps · ACC LoRA; locked: the woman, the flags,
   camera angle, background, only 2 people.
3. Leave woman-only shots untouched; fix a lost face by re-rendering only
   that close-up, "without throwing away a good take somewhere else."

**Check**
- Every shot has a lock list before it renders.

**Why**
- "45 seconds is 30 shots." Directing one shot at a time contains failures to
  the shot that failed.

### Phase 3: The negative-video trick

**Do**
1. Let **SAM3** find the guy in every frame and flip the colors inside his
   outline — "That trippy negative video becomes the motion guide for
   **MiniMax H3**: it says *exactly* who to redraw, while the original motion,
   timing and camera carry straight through."
2. Add the character sheet + portrait as references; H3 paints the double
   into the gap.

**Check**
- The mask points at the right person.

**Why**
- "Think of the mask as the most literal stage direction ever written: *this*
  person. If it points at the wrong person, you get a gorgeous, completely
  wrong take. (Foreshadowing.)"

### Phase 4: Run a tiny render farm from the couch

**Do**
1. Build two apps: **Pocket AI** (ComfyUI front end: every workflow — H3
   video, Qwen Image, Krea 2, voice — in one place) and **Tensor Master**
   (dispatcher: queues jobs, schedules onto whatever GPU is free, GPU rental
   built in).
2. Rent with prepared profiles that "bring the models and environment along,
   so I'm not rebuilding a ComfyUI box by hand every time"; one- or two-click
   renting on Vast (home RTX 3090 + rented RTX 5090s).
3. Set idle cutoffs and max lifetimes on rentals "so nothing keeps billing
   after I walk away."
4. Operate from the phone: check the queue, watch a worker, look at a
   returned take, ask for a repair, add capacity.

**Check**
- The dispatcher's invariant: "the agents need the next job ready *before* a
  worker goes idle."

**Why**
- Thirty shots rendered over and over is too much for one GPU; a queue plus
  elastic rentals turns it into a scheduling problem.

### Phase 5: Run a four-agent crew

**Do**
1. Split into four roles with shared production notes, human as director:
   **Coordinator** (keeps the shot list, latest notes, selected takes);
   **Prep** (turns notes into prompts + references, queues the jobs);
   **Farm monitor** (babysits machines: pickup, progress, failures);
   **QC** (checks frames, writes very specific notes).
2. Run the loop: "my direction → prep → render → QC → take 2 ↺".
3. Let QC go "frame by frame on anything headed for the edit. Every problem
   became a note for Prep. Sometimes the fix was a sharper prompt. Sometimes
   a better reference. Sometimes the guide itself was wrong, and no amount of
   persuasive wording would save it."

**Check**
- A rejected take carries a specific note (e.g. "Face drifting back to the
  original actor?", "Bracelet turned into a sleeve?", "Glasses on the wrong
  person?") — never a vague "looks off".

**Why**
- "One agent doing everything in order was a bottleneck. A rented GPU can
  finish its work while everyone's still staring at yesterday's problem."

### Phase 6: Fix the four canonical failures

**Do**
1. **#1 The third guy:** a whip pan's mask grabbed the wrong person and the AI
   "added me as a **third** performer between the original two." Fix: a
   hand-tracked mask on the man on the left; the pan survived.
2. **#2 The ghost:** in a dark shot the mask vanished for a few frames — "I
   flickered in and out like a ghost and bits of the original costume leaked
   through." Fix: fill the nine empty masks; steady take.
3. **#3 The hidden cut:** one "shot" secretly contained a cut from duo to
   solo; "the model happily carried the woman and the drum kit into the solo
   part." Fix: split at the internal cut, generate both halves.
4. **#4 The face fight:** too much "match the original expression" and "the
   model rebuilt the original actor's face on my character." Fix: loosen that,
   lean on likeness — "kept me recognizable, with the performance still borrowed."

**Check**
- Each fix is verified against source → rejected → fixed comparison clips.

**Why**
- Most failures are mask/guide failures, not prompt failures; fix the guide
  first.

### Phase 7: Skip the rejected experiments

- **Character-swap LoRA**: "NOT DEFAULT — Tested with and without. No clear
  enough likeness boost."
- **Face-only refine**: "TOO FIDDLY — Crop the face, regenerate, merge back.
  Pose, glasses and seams fought us."
- **Slow-motion guide**: "EXPENSIVE — More room for the performance, but more
  frames, memory and waiting."
- **Original-color guide**: "SOMETIMES — Saved one take, then added me instead
  of replacing him in the pan."

### Phase 8: Compare against the commercial model

**Do**
1. Run the same source through **Genjutsu** on Higgsfield.
2. Hardest shot (2 seconds: co-star pulls the sunglasses off mid-performance)
   took **11 takes** with H3; Genjutsu "left the glasses on his face, recast
   my co-star with dark hair, and quietly swapped the whole set and its
   colors. Pretty video. Wrong scene."

**Check**
- Shot 11 (the star glasses) logged 11 completed takes; the sunglasses handoff
  in shot 3 took 11 submissions.

**Why**
- Scene fidelity (locks honored) beats prettiness. Lock lists are the metric.

### The receipts

- Jobs: **158 done, 18 cancelled, 3 failed** (recorded jobs across tests and
  earlier versions, not clips in the final cut).
- GPU time: ~6h50m on the home 3090 + 2h48m on rented 5090s (summed per-job,
  not wall clock); peak concurrency two workers.
- Rented compute: **~$6–8** (modeled from recorded rates × lifetime, not an
  invoice).
- Agent tokens: "1 week of AI agent tokens. Gone in 1 night." — "The cost
  nobody puts in the GPU math."

### The human method, distilled

1. **Keep everything. Swap the guy.** Preserve camera, dancing, energy, co-star.
2. **45 seconds is 30 shots.** Slice at every edit; each shot is a job.
3. **Lock lists before generation.** Every job names what must not change.
4. **The mask is the most literal stage direction ever written.** Wrong target
   = gorgeous, completely wrong take.
5. **QC goes frame by frame; every problem becomes a note for Prep.**
   Sometimes the fix is a sharper prompt, sometimes a better reference,
   sometimes the guide itself.
6. **One agent is a bottleneck; four agents with shared notes are a crew.**
7. **Budget the tokens, not just the GPUs.** A week's agent budget burned in
   one night.

**Depth status:** FULL (author's complete written breakdown with numbers,
job specs, failure taxonomy, and receipts; commenters corroborate the
agentic-setup reading).

---

## 4. "Real-time cloth simulation in TouchDesigner - POPtober day 1" (matigekunst)

Source: https://www.reddit.com/r/Simulated/comments/1wv76e2/realtime_cloth_simulation_in_touchdesigner/
(native Reddit video; r/Simulated post 1wv76e2, score 33, 1 comment)

Tools used: **TouchDesigner** (inference: POPs, given the author's 2026-10-02
TouchDesigner POPs GPU XPBD softbody post); technique: **XPBD cloth sim with
forces coming from real-time monocular depth** (author's full post text).

What the evidence supports: the same author posted a TouchDesigner POPs GPU
XPBD softbody ("Trampoline") yesterday with 70 shader passes at 60fps; this
POPtober day-1 piece applies the same class of solver to cloth, driven by
live monocular depth (a camera-based depth estimate feeding forces into the
cloth). The single comment ("That's really cool!") adds nothing.

**Depth status:** DEPTH-LIMITED. One-line post text, no comments with signal,
no captions on native Reddit video. A media download was attempted under this
run's pre-approved allowance (2 attempts) to enable frame review; both failed
on sandbox network flakiness (SSL CA rotation, then v.redd.it connection
resets — no approval gates hit). What a download would add: frame-level
confirmation of the depth→force visualization and cloth solver behavior.

---

## 5. "Not Color: What Every Digital Artist Should Know About Color Science" — Nathan Vegdahl, Blender Conference 2026

Source: https://youtu.be/SqJ_rtaPqg4 | 48:39 | r/vfx post 1wvdab5 (score 40,
2 comments) | captions: full ASR (1196 segments)

Tools used: **Blender** (live demo: rebuilt the chromaticity diagram with
S/M/L axes in "the Blender Cave"); knowledge: **CIE 1931 chromaticity**,
**ACES AP0/AP1**, **sRGB/Rec.709**, **Sony S-Gamut**, camera spectral
sensitivities (Sony Alpha 9). Referenced: Captain Disillusion's color video
("spot-on… at least as accurate as my presentation"), Steven Yedlin (camera
color), a next-day practical color-management talk by the speaker's friend Mark.

This is a knowledge talk, not a tooling workflow, so it is distilled as
principles rather than Do/Check/Why phases.

- **The horseshoe is not "all the colors the human eye can see."** More
  accurate: "all the ways light can stimulate the cones of the human eye
  under normal circumstances." The only unambiguously correct part of the
  folk description is "the human eye".
- **Three cones just sum stimulation.** S/M/L cones add up all stimulation;
  they cannot tell where along the spectrum it came from. Different spectra
  can produce identical stimulation (metamerism); RGB displays exploit this.
  (Demo: three spectral spikes that would be three distinct notes as sound
  collapse to one color experience as light.)
- **Color observers are mutually incompatible.** A tetrachromat ("Bob")
  distinguishes spectra normal vision cannot; humans and Bob live in "different
  kind of vision universes." Cameras too: different sensors are "mutually
  colorblind" with each other and with humans — infinitely many spectra look
  the same to a Sony Alpha 9 but different to the eye, and vice versa.
- **An RGB color space = RGB primaries + a white point.** The equal-channel
  point calibrates relative channel brightness so the same numbers give
  consistent eye stimulation across displays; the perceptual white point is
  the brain's white-balance anchor (warm-room/cool-room demo).
- **Display vs capture vs coordinate spaces.** sRGB is a display space;
  camera spaces (Sony S-Gamut) are "a best effort mapping to human color
  space" and their gamut-triangle corners are meaningless marketing ("they
  don't really care about the corners because those don't show up");
  interchange spaces (ACES AP0) just store colors, working spaces
  (ACES AP1/ACEScg) are for rendering/compositing. All RGB spaces are
  defined the same way (RGBW points); use case differs.
- **Impossible colors are real.** The pure-M-cone stimulation thought
  experiment was actually run; subjects reported "a blue-green of
  unprecedented saturation." (Wikipedia: "impossible colors".)
- Assumes linear color throughout ("for the pedants… I am completely
  assuming linear color for the entire rest of this talk").

**Depth status:** KNOWLEDGE — full captions captured; no workflow to extract.
Relevance: color-pipeline literacy for any foundry material stage; Aegis has
no PBR material import policy or validation gate (inventory NEED), 2d3d and
Desktop City likewise carry no color pipeline — file as knowledge, not a gap fill.

---

## 6–8. NO-TOOLING

- **"Why VFX still beats AI in 2026"** (Schopix Studios, https://youtu.be/F_qlwfktVMM,
  8:01, r/vfx, 57 comments): opinion essay — five reasons artists "are not
  cooked" (generative AI cannot be controlled exactly, repeats poorly, failed
  generations burn time). No tooling workflow demonstrated. NO-TOOLING.
- **"Pressure Works is Live!"** (r/Simulated, Steam game launch: pneumatic
  machine-building sandbox): product announcement, no workflow. NO-TOOLING.
- **"How could I get higher waves?"** (r/Houdini, beach-wave sim question):
  Q&A with one concrete tip from DavidTorno — the fluid swells from the speed
  and amount of fluid moving into what is in front of it; "If you are using
  POP Advect By Volume DOP to read in the vel field, you can just increase the
  Force Scale to push harder." Useful tip, no extractable workflow. NO-TOOLING.

---

## Per-repo have-vs-need

### Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| DCC bridge live-link + cache pattern (socket live, Alembic/VDB/JSON sidecar, USD to Solaris) | #1 HBLink | NEED | trellis-pipe has weld/lods/orm_pack but no DCC round-trip caching stage | **backlog** — adopt the technique, not the paid plugin: rest-cache + per-frame transform/velocity point file (~35× smaller than Alembic hierarchies) is a cheap foundry caching upgrade; JSON material-rebuild sidecar pattern for ue/ stage |
| Mixamo-clip → rig transfer (beta) | #1 HBLink | NEED | audit-verified: no rigging/skinning/retarget stage in trellis-pipe | **watchlist** — P1 gap stays open; keep Mixamo clips as the acceptance set when building runtime/rig |
| Per-shot lock lists + 4-agent QC crew | #3 mexxmillion | NEED | no AI-vendor generation/acceptance spec in intake/ | **adopt now (practice)** — lock-list template ("NOT ALLOWED TO CHANGE") in intake/ acceptance records; QC rejection-note discipline for review/ |
| Pocket AI + Tensor Master (phone-driven ComfyUI front-end + GPU dispatcher w/ Vast rentals) | #3 mexxmillion | PARTIAL | fleet/ exists for AWS GPU runs; no couch-driven rental dispatch or agent-ready-queue discipline | **watchlist** — rental profile pattern + idle-cutoff/max-lifetime billing guards worth copying when fleet grows |
| SAM3 + color-inversion character swap (MiniMax H3) | #2 comfyui-minimax-h3-studio | NEED | intake/ has concept-to-input; no video inpainting/edit stage | **watchlist** — AI-video bucket; revisit when Aegis needs a trailer (existing Minimax row trending) |
| XPBD cloth w/ realtime depth forces (TouchDesigner) | #4 | NEED | no cloth/physics stage in foundry | **watchlist** — cinematics bucket only (trending row) |
| Color-science literacy (CIE 1931, ACES AP0/AP1, display vs capture spaces) | #5 Not Color | NEED | no PBR material import policy or validation gate | **backlog (knowledge)** — file with the material-stage work, not a gap fill |

### 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| JSON sidecar material/settings rebuild | #1 HBLink | NEED | qa/asset_validate.py missing (roadmap rec 9, P1) | **adopt now (pattern)** — manifest sidecar describing materials/settings maps directly onto rec 9's provenance/manifest checks |
| SAM3 video segmentation for inpainting | #2, #3 | PARTIAL | pipeline/reference uses SAM 2 for recon | **watchlist** — extend SAM usage toward video masks when inpainting enters scope |
| Per-shot lock lists / QC rejection notes | #3 | NEED | no written art bible (roadmap rec 2, P1); no per-job acceptance records | **backlog** — lock-list template complements rec 2's art bible with per-job acceptance |
| Color pipeline literacy | #5 | NEED | no color pipeline evidence | **skip** — knowledge note only |

### Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Per-generation lock lists | #3 | PARTIAL | tools/asset_standards.py + data/asset_standards.json + SPRITES.md (stable IDs, anchors) | **backlog** — PRD 17.1 requires execution + visual review + human approval per AI asset; per-job lock lists would make "what good means" explicit per asset class |
| Shader-driven skyline fill | — | NEED (P1) | no equivalent; every building authored/generated | nothing today; gap stands |
| MiniMax H3 / TouchDesigner cloth | #2, #4 | NEED | no AI-video or cloth stage (by design: fixed-view sprites) | **skip** — outside scope |

### Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Per-asset lock lists (acceptance discipline) | #3 | PARTIAL | concept PNG is visual authority; per-class export profiles; no written acceptance spec for Meshy-class inputs | **backlog** — extend concept-PNG-as-authority with per-asset lock lists at the audit stage |
| Rig stage comparison | #1 HBLink | HAVE | stages/rig.py + assetpipe/blender/rig.py exist (unlike Aegis) | note only — DCC-side Mixamo pattern not needed |
| Godot import validation gate | — | NEED (P1) | nothing to validate into yet (ADR 0003) | nothing today; gap stands |

## Watchlist trending

## Watchlist trending
- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-03) **TRENDING**
- TouchDesigner POPs GPU XPBD softbody (Gauss-Seidel, 70 shader passes @ 60fps) (first seen 2026-10-02, status WATCH; seen again 2026-10-03)

New watchlist additions (5): HBLink (BACKLOGGED); comfyui-minimax-h3-studio (BACKLOGGED);
Pocket AI + Tensor Master (WATCH); per-shot lock lists + 4-agent QC crew (BACKLOGGED);
Genjutsu/Higgsfield (WATCH).

## Gap recommendations (highest leverage)

1. **Per-job lock lists in Aegis intake/ (adopt the practice, not the tools).**
   mexxmillion's "NOT ALLOWED TO CHANGE" lists are the P1 acceptance-spec gap
   made concrete. Next step: add a lock-list template to intake/ acceptance
   records and a QC rejection-note format to review/.
2. **Rest-cache + point-file caching recipe for the foundry.** HBLink's RBD
   recipe (rest fracture cached once + per-frame transform/velocity point
   file, ~35× smaller than Alembic hierarchies) is a cheap technique transfer
   into trellis-pipe caching, and it serves the P1 perf-budget gap's
   compression side.
3. **JSON material-rebuild sidecar for 2d3d's P1 asset-validation gate.**
   HBLink's cache-side JSON (tells Blender how to rebuild materials/settings)
   is the manifest/provenance pattern roadmap rec 9 needs.
4. **Keep Mixamo clips as the retarget acceptance set.** HBLink's beta proves
   the mocap-clip-onto-rig pattern in a shipping tool; when Aegis builds
   runtime/rig, the acceptance test is already written.
5. **Budget agent tokens like GPU hours.** mexxmillion burned a week of agent
   tokens in one night on a 30-shot video — any agentic foundry loop needs a
   token budget next to the GPU budget.

## Explicit non-goals

- VFX-vs-AI essay (opinion, no workflow); Pressure Works (product launch);
  higher-waves thread (single sim tip, no workflow); Not Color as a tool
  (knowledge talk); Genjutsu as an adoption candidate (failed the
  scene-fidelity test — pretty but wrong scene); Viggle (already on
  watchlist, nothing new).

## Depth-escalation usage

- Mode: pre-approved, max 2 downloads. Attempted: 1 video
  (TouchDesigner realtime cloth, v.redd.it/c83gmpeqewsh1), 2 attempts, 0 succeeded.
- Attempt 1 (public-mirror downloader): failed — expected `.venv/bin/yt-dlp`
  does not exist in this environment. Switched to the video-summarizer skill's
  downloader (working, complete script set).
- Attempt 2: SSL verify failure — sandbox egress proxy CA had rotated; fixed
  per AGENTS.md (refreshed from /usr/local/share/ca-certificates/hatch-egress-ca.crt,
  appended to the skill venv's certifi bundle).
- Attempt 3 (retry): v.redd.it connection resets (IncompleteRead, then remote
  end closed connection). No approval gates hit at any point. Stopped hitting
  v.redd.it per the host-flakiness rule; audit #4 marked DEPTH-LIMITED.
- Audits #1–3 reached FULL from post text, comments, and the author's full
  written breakdown — no downloads needed. YouTube videos #5–6 had full
  captions via yt_summarize; no downloads needed.

## skill_library staging (ready to publish, browser upload when Ehsan is present)

- New: `skills/hblink-blender-houdini-bridge/` (bridge workflow + RBD point-cloud recipe).
- New variant: `skills/minimax-h3-character-swap-comfyui/` (SAM3 + inversion masking workflow;
  distinct from resistance-sci-fi-short's director workflow and konte's DSL).
- New variant: `skills/agentic-multishot-ai-video-farm-crew/` (Pocket AI + Tensor Master +
  4-agent crew + lock lists; distinct from konte-multishot-ai-video's TS DSL).
- Report mirrored to `docs/scout-reports/have-vs-need-2026-10-03.md`; index updated.
- Watchlist synced to `video-tooling-scout/references/tooling-watchlist.md`; skills README
  table rows added.

---
*Report: ~/workspace/goals/video-tooling-scout-vs-game-pipelines/hidden_files/have-vs-need-2026-10-03.md*
