# Video tooling scout: have-vs-need — 2026-11-08

**Run:** daily scout, window last 2 days (2026-11-06 to 2026-11-08), depth mode `pre-approved` (max 2 media downloads).
**Scanned:** 39 Reddit video posts across 23 subreddits (4 subs down: unity, substance3d, proceduralgeneration, shaders — Arctic Shift HTTP 526). YouTube channel scan down for this run (see below).
**Deeply analyzed:** 8 videos (7 audits + 1 no-tooling screen). 2 re-scanned duplicates from 2026-11-07 (FrameExtractor, meshlet forest) noted, not re-audited.
**Depth escalation:** 1 download attempted, 1 succeeded (MiniMax H3 tutorial, 25.7 MB mid quality, no approval gate). 0 skipped on gates. Second download not attempted: no other candidate needed frames (Air Strider trailer is gameplay footage; its workflow is in the post text).

## Gap alerts

**ALERT 1 — P1 rigging gap (Aegis) and P1 production-conversion gap (2d3d): runtime procedural rig + skin in GDScript.** Primordium (audit 1) builds the skeleton and a single skin mesh from the creature design at runtime in Godot 4, with IK foot planting and body lean, no pre-made skeletal meshes. Aegis has no rigging/skinning/retarget stage in the foundry (P1 gap, fix artifact prepared with the Tripo P2.0 route); Primordium is a second, runtime route to the same need and is directly relevant evidence. 2d3d's P1 production-conversion stage covers rigging for generated meshes, and its generated hawk/boar art currently uses procedural rigs as stand-ins; Primordium shows what a runtime-generated rig looks like in production-shaped code. New skill: `characters/godot-runtime-procedural-creatures`.

**ALERT 2 — P1 AI-vendor acceptance-spec gap (Aegis intake), partial evidence: IV Studio 1.0's checker + scoring pattern.** IV Studio 1.0 (audit 8) adds a prompt checker that catches what H3 punishes, per-shot sampler/scheduler control, and InsightFace likeness scoring to pick LoRA checkpoints; the H3 agent skill (audit 4) adds a per-segment check report after every batch run. That is a scoring/acceptance pattern for AI-generated video: check before spend, score takes, keep the report. It does not fill the gap (the gap is a written "what good means" spec per asset type for intake), but it is the closest working acceptance machinery seen in the wild and the fix artifact for the gap should borrow its shape. IV Studio skill expanded.

**Near-hit — P2 MCP-driven DCC loop (Aegis): agent-driven iteration with automated checks.** Air Strider (audit 7) was built in two weeks with Codex driving iteration, Playwright browser checks catching regressions, and tuning values in config files. That is agent-driven iteration with automated verification, but it is not DCC (no Blender/UE agent loop), so it is a near-hit for the P2 gap, not a match. IV Studio 1.0's 154-tool MCP server (agents direct the film studio alongside the human) is adjacent evidence in the same direction.

## Videos scanned

39 video posts, ranked by tooling relevance x engagement. Top 8 by relevance were candidates; the full ranked list is in the scan output (`/tmp/scan-2026-11-08-clean.json`).

| # | Title | Creator | Source | Score/comments |
|---|-------|---------|--------|----------------|
| 1 | Working on a Spore-inspired evolution and tribe game in Godot 4 with procedural creatures | Ouvolk (Primordium) | https://www.reddit.com/r/godot/comments/1xqph5m/working_on_a_sporeinspired_evolution_and_tribe/ | native Reddit clip |
| 2 | thushima inspired grass in godot | alexvice02 | https://www.reddit.com/r/godot/comments/1xqhpjh/thushima_inspired_grass_in_godot/ | native Reddit clip |
| 3 | Godot is GREAT for VFX | Ordinary-Cicada5991 | https://www.reddit.com/r/godot/comments/1xqh2q9/godot_is_great_for_vfx/ | native Reddit clip |
| 4 | Minimax H3 Best Remix Tool | Friendly Ultra-Fast Character Replacement | Create 1080p Ultra-Long Videos | wjc_5 | https://www.reddit.com/r/comfyui/comments/1xqqhxh/minimax_h3_best_remix_tool_friendly_ultrafast/ | native Reddit clip + YouTube tutorial https://youtu.be/4u1gw8Swt1s |
| 5 | My free, open-source keyframe extractor for COLMAP and Gaussian Splatting just got easier to install | WearyFortune7055 (FrameExtractor) | https://www.reddit.com/r/photogrammetry/comments/1xpeqtc/my_free_opensource_keyframe_extractor_for_colmap/ | DUPLICATE of 2026-11-07 audit, not re-audited |
| 6 | This poor guy took every VFX pack I made | gennai777 | https://www.reddit.com/r/godot/comments/1xqvpc1/this_poor_guy_took_every_vfx_pack_i_made/ | native Reddit clip |
| 7 | My latest scientific visualisation | nanoseb | https://www.reddit.com/r/blender/comments/1xqmova/my_latest_scientific_visualisation/ | native Reddit clip |
| 8 | Some shots | Realistic_Blueberry3 | https://www.reddit.com/r/blender/comments/1xqrxvi/some_shots/ | NO-TOOLING |
| 9 | I implemented the meshlet pipeline from Three.js r187 in my Forest environment | PerceptionCharming | https://www.reddit.com/r/threejs/comments/1xpdv8e/i_implemented_the_meshlet_pipeline_from_threejs/ | DUPLICATE of 2026-11-07 audit, not re-audited |
| 10 | Two weeks building my dream mech game with AI: the workflow behind Air Strider | Chilkus | https://www.reddit.com/r/aigamedev/comments/1xquyde/two_weeks_building_my_dream_mech_game_with_ai_the/ + YouTube https://www.youtube.com/watch?v=kwUxv7RbT1g | YouTube trailer, 85 s, no captions |
| 11 | IV Studio 1.0: I rebuilt my free, open-source film studio for ComfyUI + MiniMax H3 from your comments (now on Linux and Mac) | itsVariance | https://www.reddit.com/r/comfyui/comments/1xqfux1/iv_studio_10_i_rebuilt_my_free_opensource_film/ | native Reddit clip |

## Audits

### 1. "Working on a Spore-inspired evolution and tribe game in Godot 4 with procedural creatures" (Ouvolk, Primordium)

Source: https://www.reddit.com/r/godot/comments/1xqph5m/working_on_a_sporeinspired_evolution_and_tribe/ | r/godot post 1xqph5m (score 32, 16 comments) | native Reddit clip

Tools used: **Godot 4**, **GDScript** (runtime generation). Demo on itch.io: https://akinjigames.itch.io/primordium. Kickstarter pre-launch page linked in the post.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: generate the creature from its design at runtime, rig and skin it from the same design, then let the ecosystem and tribe systems drive the animation.

### Phase 1: Generate the creature design

**Do**
1. Define the creature as a design (body plan + part list), not as a mesh. Parts named by the author: curved Bezier horns, tapered ears, bi-lobed tail clubs, wings you can glide with, shader eyes with blinking eyelids.

**Check**
- The design, not a sculpt, is the input: "All the creatures are generated in GDScript at runtime, with no pre-made skeletal meshes."

**Why**
- A design-driven creature can evolve: the game is Spore-inspired evolution, so the creature must change shape as it evolves. Pre-made meshes cannot do that.

### Phase 2: Build the rig and skin at runtime

**Do**
1. In GDScript, build the skeleton from the creature's design.
2. Build a single skin mesh from the same design, over that skeleton.

**Check**
- One skin mesh per creature, generated, not imported. The author states the skeleton and "a single skin mesh are built from the creature's design."

**Why**
- Rig and skin from one design cannot disagree about proportions: the same numbers drive both. (Inference, labeled: the author does not state this principle; it is the reason the architecture works.)

### Phase 3: Animate with IK and lean

**Do**
1. Foot planting via IK: feet stay planted while the body moves.
2. Lean the body into turns.

**Check**
- Feet do not slide or float during walks and turns in the clip; the body banks into the turn.

**Why**
- IK planting plus lean is what makes a generated skeleton read as alive instead of procedural: the feet obey the ground and the body obeys momentum. (Inference, labeled.)

### Phase 4: Drive behaviour with a daily schedule

**Do**
1. Give herds a daily schedule: sleeping in nests at night, stretching at dawn, resting at midday.
2. In the tribe stage, let tribe members gather, hunt, defend, and play instruments.

**Check**
- The same creatures behave differently by time of day in the clip (nest sleeping at night, stretching at dawn).

**Why**
- Schedule-driven behaviour makes the ecosystem visible without scripting every creature: time of day is the director.

### The human method, distilled
1. **Design is the asset.** The creature design generates rig, skin, and parts; nothing is pre-made.
2. **One design, one rig, one skin.** A single source of truth for proportions.
3. **Ground the feet, lean the body.** IK planting and turn lean carry the believability.
4. **Schedule, don't script.** Daily routines produce living-ecosystem behaviour from a clock.

**Depth status:** PARTIAL (full author post text + 16 comments with exact technique inventory; no code, no numeric parameters, no performance figures disclosed; author offered to answer questions about mesh generation, IK walking, and AI). Comments are mostly an AI-use debate, not workflow detail; the workflow evidence is the author's post text.
**Skill:** new `characters/godot-runtime-procedural-creatures`.

### 2. "thushima inspired grass in godot" (alexvice02)

Source: https://www.reddit.com/r/godot/comments/1xqhpjh/thushima_inspired_grass_in_godot/ | r/godot post 1xqhpjh (score 61, 2 comments) | native Reddit clip

Tools used: **Godot**, **SimpleGrassTextured** (base, reworked), Godot shaders. No shader code disclosed.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: start from a known grass base, split it into performance-tiered shader variants, and scatter procedurally.

### Phase 1: Rework the base into three shader variants

**Do**
1. Start from SimpleGrassTextured.
2. Rework it into three shader variants, one per performance tier: "three shader variants depending on how much performance you want to spend."

**Check**
- The clip is "one of the base variants." (Author's words.)

**Why**
- (Inference, labeled: the author does not state a principle.) Perf-tiered variants let the same grass scale from low-end to high-end instead of one shader serving all budgets.

### Phase 2: Scatter procedurally, mix dry grass

**Do**
1. Procedurally generate clumps and bushes.
2. Mix in some dry grass.

**Check**
- Clumps and bushes read as placed variation, not uniform tiling; dry grass breaks up the green.

**Why**
- Procedural clumps plus a dry-grass mix give variation without hand-placing every blade. (Inference, labeled.)

### Phase 3: Verify on the Steam Deck

**Do**
1. Run medium settings on the Steam Deck and compare against the showcase.

**Check**
- Author's measured result: "Medium settings look pretty close to this and made no difference to performance on the Steam Deck, which I honestly didn't expect."

**Why**
- The Deck is the honest low-end check: if medium looks this good and costs nothing there, the variants are correctly tiered. (Inference, labeled.)

### The human method, distilled
1. **Rework a known base, don't write from scratch.** SimpleGrassTextured is the starting point.
2. **Tier by performance.** Three variants, one per budget.
3. **Verify on the weakest target.** The Steam Deck result is the proof, not the editor viewport.

**Depth status:** DEPTH-LIMITED (post text only, 2 comments; three shader variants named but no shader code, no parameters, no node names; author offered to go into the implementation if anyone is interested). No skill: not executable without the shader code.
**Skill:** none (report only).

### 3. "Godot is GREAT for VFX" (Ordinary-Cicada5991)

Source: https://www.reddit.com/r/godot/comments/1xqh2q9/godot_is_great_for_vfx/ | r/godot post 1xqh2q9 (score 894, 51 comments) | native Reddit clip

Tools used: **Godot** (VFX: particles, shaders, trails). The author worked on the reel "last week with a friend to convince him to switch from Unreal to Godot." One workflow artifact: the author links **Riot's VFX style guide** (League of Legends, archived 2018 PDF) in the comments.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: a showcase reel proving Godot VFX capability, not a tutorial.

### Phase 1: Study the reference style guide

**Do**
1. Read Riot's VFX style guide (the author links it as the reference for the reel's look).

**Check**
- The reel's effects read as League-style: readable shapes, strong silhouettes, restrained palettes.

**Why**
- (Inference, labeled.) A style guide is the workflow here: the effects follow a documented look, not improvisation.

### Phase 2: Build the reel in Godot

**Do**
1. Build particle, shader, and trail effects in Godot over a week with a collaborator.

**Check**
- Commenters ask "how did you made the trail effects" (unanswered) and note Godot "didn't have native support for trails or free 3 axis tumbling till like, 2 months ago" (commenter huttyblue, score 16), which dates the trail work to a recent engine feature.
- A second commenter (huttyblue) warns to "show it running smoothly from a cleared shader cache," i.e. the reel may benefit from a warm cache; that check was not shown.

**Why**
- The reel's point is capability proof ("convince him to switch"), not a teachable pipeline. (Author's stated purpose.)

### The human method, distilled
1. **Prove capability with a reel, teach with a guide.** The video shows what Godot can do; the Riot style guide is where the method lives.
2. **Trails are the new capability.** Native trail support arrived ~2 months before the post; the reel leans on it.

**Depth status:** DEPTH-LIMITED (showcase clip; no workflow detail in post text; the trail-effects question went unanswered; the only workflow artifact is the linked Riot style guide). No skill.
**Skill:** none (report only).

### 4. "Minimax H3 Best Remix Tool | Friendly Ultra-Fast Character Replacement | Create 1080p Ultra-Long Videos" (wjc_5)

Source: https://www.reddit.com/r/comfyui/comments/1xqqhxh/minimax_h3_best_remix_tool_friendly_ultrafast/ | r/comfyui post 1xqqhxh (score 97, 5 comments) | native Reddit clip + YouTube tutorial https://youtu.be/4u1gw8Swt1s (782 s, uploader jingchen573, no captions; media downloaded this run, 12 frames reviewed)

Tools used: **ComfyUI**, **MiniMax H3**, **Spark-H3** (sparse attention, zechengtang/Spark-H3), **Spectrum** forecast caching (xmarre/ComfyUI-Spectrum-MiniMax-H3), **TemporalWindow / SpatialTiles** (mo-akkakk/ComfyUI-MiniMaxH3-TemporalWindow-SpatialTiles), **split SelfLift** (wjc573/ComfyUI-SelfLift-Split), **lightx2v Ref2VA turbo v0.1** LoRA at 1.0 + **600-step EMA turbo LoRA** at 0.5, **akatz-ai Character Swap LoRA**, **h3-motion-transfer agent skill** (github.com/wjc573/h3-motion-transfer; RunningHub workflow https://www.runninghub.ai/post/2117441641207402497). Frame-verified node names from the downloaded tutorial: "MiniMax H3 Spark Attention (Auto / Pinned)", "MiniMax H3 Temporal Window & Spatial Tiles", "MiniMax H3 Low VRAM...", "MiniMax H3 CharacterSwap", "MiniMax H3 Memory Efficient Attention", "MiniMax H3 Reference to Video", "Load LoRA", "Load Diffusion Model", "Load CLIP". Frame-verified subtitle: "at 0.5 strength, and the softness goes away." Frame-verified editor shot: segment stitching in a video editor with the subtitle "When you want a seamless join within one shot,".

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: split long clips into short segments, keep the character reference alive across segments with overlapping windows and context frames, and stack cheap accelerators because character swap is a narrow task.

### Phase 1: Pad and frame-align the clip

**Do**
1. H3 needs a 17n+5 frame length, so pad the source clip with its last frame, then trim the padding (and any context guide frames) before saving.
2. Output is 24 fps and exactly as long as the input clip.

**Check**
- Output length equals input length at 24 fps; no drift from the padding.

**Why**
- The model has a fixed frame-length arithmetic; padding absorbs it so the editor never sees a length change. (Author's rule, stated in the post.)

### Phase 2: Cut long clips into segments

**Do**
1. 720p (target 0.9-1.0 MP): up to about 15 s in one pass with TemporalWindow. Leave the window length at 6.5 s; it is per window, not the total length.
2. 1080p (2.0 MP): cut long videos into 4-6 s segments. Cut at natural shot changes and run those independently with the same character references.
3. If one shot has to be split, turn on the context switch and load the previous segment's output: its last 22 frames guide the start of the new segment, so the seam lines up.

**Check**
- The Trouble Maker stage clip in the video is 64 s, cut into 15 segments of about 4-6 s each. At 2.0 MP each segment took about 6-10 minutes.
- Clips cut at natural shot changes need no context; same-shot splits do.

**Why**
- Two problems motivated the split: "video references are slow, and on long clips the model loses the reference in the later part." Short segments keep the reference fresh; context frames keep the seam invisible. (Author's stated problems.)

### Phase 3: Stack the accelerators

**Do**
1. Enable Spark-H3 sparse attention (recent versions optimize video references, which fits character swap well).
2. Enable Spectrum forecast caching.
3. For speed LoRAs: lightx2v Ref2VA turbo v0.1 at 1.0 plus the 600-step EMA turbo LoRA at 0.5. v0.1 alone looks less greasy than v1.1 but a bit soft; adding the EMA LoRA fixes the softness and holds up better in motion.
4. Add akatz-ai's Character Swap LoRA to the chain.
5. Spark-H3 needs an NVIDIA RTX 30/40/50 card. If the GPU doesn't support Spark, Sage, or Spectrum, replace or bypass them.

**Check**
- Frame-verified: the tutorial's ComfyUI graph shows "MiniMax H3 Spark Attention (Auto / Pinned)" and Load LoRA nodes; subtitle confirms "at 0.5 strength, and the softness goes away."
- The author would not stack this many accelerators for normal generation: "character swap is a narrow, well-defined task, so sparse attention and forecast caching don't cost much quality here."

**Why**
- Narrow task, cheap acceleration: the quality risk of stacking accelerators is bounded because the job (replace this person, keep everything else) is tightly defined. (Author's stated principle.)

### Phase 4: Sample in overlapping windows with split SelfLift

**Do**
1. TemporalWindow samples the clip in overlapping windows, which cuts down on the reference dropping off late in the clip.
2. Use the split version of SelfLift, so the low-res pass and the high-res refine are separate nodes that work with TemporalWindow.
3. Leave spatial tiles off in TemporalWindow; the split SelfLift nodes don't support it.

**Check**
- Frame-verified: the graph shows "MiniMax H3 Temporal Window & Spatial Tiles" as a node.
- The reference holds through the later part of long clips instead of dropping off (the second of the author's two motivating problems).

**Why**
- Overlapping windows re-anchor the reference repeatedly; split SelfLift keeps the low-res/high-res passes compatible with the windowing. (Author's stated mechanism.)

### Phase 5: Write prompts per segment with the agent skill

**Do**
1. For simple single-shot clips, a web LLM that can watch video is enough: give Gemini the prompt template, the character sheets, and the clip, tell it who replaces whom, and paste the output into the prompt box. Load the images in the workflow in the same order they were uploaded.
2. For clips with lots of cuts, use the h3-motion-transfer skill: name clips 1, 2, 3 to run independently, or 2-1, 2-2, 2-3 so that 2-2 continues from 2-1's output. Point it at the folder and say who becomes which character. It detects hard cuts locally, writes a prompt per segment, shows the first one, runs everything in order (resumable if interrupted), then stitches the result with a side-by-side comparison and a per-segment check report.
3. It runs on RunningHub (CN or international site) or local ComfyUI; on RunningHub it uses 2.0 MP, so keep segments around 4-6 s. Built for Hermes; other agents (Claude Code, Codex) can use it by reading SKILL.md in the repo.

**Check**
- The skill shows the first prompt before running; the run is resumable; the final output includes the side-by-side comparison and per-segment check report.

**Why**
- Prompt-per-segment is the only way to keep a multi-cut clip coherent: one prompt for the whole clip cannot track who is where after every cut. (Inference, labeled: the author describes the mechanism, not this principle.)

### The human method, distilled
1. **Cut long videos sensibly.** Segments of 4-6 s at 1080p, 15 s max at 720p; cut at shot changes, use context only for forced splits.
2. **Re-anchor the reference.** Overlapping windows plus 22 context frames stop late-clip reference loss.
3. **Stack accelerators only for narrow tasks.** Spark-H3 + Spectrum + turbo LoRAs are justified because character swap is tightly defined.
4. **Let the agent write prompts per segment.** One prompt per segment, first one shown, resumable runs, check report at the end.
5. **Watch the full tutorial before starting.** The author's own warning: follow the video along with the workflow "to avoid common mistakes."

### Failure modes
- **Reference drops off late in long clips** if run in one pass without TemporalWindow; fixed by overlapping windows (Phase 4).
- **Softness from v0.1 alone**; fixed by adding the 600-step EMA turbo LoRA at 0.5.
- **Spark/Sage/Spectrum unsupported on non-RTX-30/40/50 GPUs**; replace or bypass them (required on non-NVIDIA GPUs).
- **Spatial tiles break split SelfLift**; leave them off.

**Depth status:** FULL (full author post text + 5 comments + tutorial video description + 12 frames from a downloaded copy with verified node names and subtitles; no captions exist, and local transcription is unavailable in the sandbox by design).
**Skill:** new variant `ai-video/minimax-h3-temporalwindow-character-swap` (same tool, different workflow from the existing SAM3 color-inversion `minimax-h3-character-swap-comfyui`).

### 5. "This poor guy took every VFX pack I made" (gennai777)

Source: https://www.reddit.com/r/godot/comments/1xqvpc1/this_poor_guy_took_every_vfx_pack_i_made/ | r/godot post 1xqvpc1 (score 72, 10 comments; comment fetch failed: Arctic Shift HTTP 422, old-reddit JSON blocked in sandbox) | native Reddit clip

Tools used: **Godot 4** VFX addons (author's own 13-pack bundle, $29.99: https://gennai.itch.io/godot-4-vfx-complete-collection). Packs named: frost, fire, lightning, sword, curse, blood and wounds, death and dissolve, sci-fi shields (plus 5 unnamed from the original 10).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: one mannequin, one take, every addon stacked — and the stacking only works because each shell sits at its own distance.

### Phase 1: Name and file every addon the same way

**Do**
1. Start every class with its pack's prefix.
2. Give every addon its own folder.

**Check**
- 13 packs coexist in one project without name collisions.

**Why**
- "Names were easy." Prefix + own folder is the whole convention, and it is what makes the single-project walkthrough possible. (Author's words.)

### Phase 2: Stack the shells at different distances

**Do**
1. A few packs draw on a thin copy of the mesh pushed out a few millimetres, like the ice crust and the fire. These are shell effects: a duplicate mesh offset from the surface.
2. Give each shell its own distance from the surface.

**Check**
- Before the fix: "If two sit at the same distance on one character they z-fight."
- After: "I gave each one its own distance from the surface, and now they stack fine!"

**Why**
- Two shells at the same offset fight over the same depth values; distinct offsets give the depth buffer an unambiguous order. (Author's stated failure mode and fix; the depth-buffer mechanism is labeled inference.)

### Phase 3: Walk one mannequin through everything, one take

**Do**
1. Put every addon in one project and walk one mannequin through them: frost, fire, lightning, a sword, a curse, and he ends up as ash. One take.

**Check**
- All 13 packs render on the same character in one continuous shot; the author admits "I went in a bit scared of the single project part lol."

**Why**
- One take on one character is the proof the stacking works: any z-fighting or naming collision would show immediately. (Inference, labeled.)

### The human method, distilled
1. **Prefix + folder per addon.** Naming discipline is what lets 13 packs share a project.
2. **Shells stack by distance, not by luck.** Each shell gets its own offset from the surface; equal offsets z-fight.
3. **Prove it in one take.** A single mannequin through every effect is the integration test.

**Depth status:** PARTIAL (full author post text with exact naming convention, shell technique, failure mode, and price; no shader code for the shells; comment fetch failed on both fallbacks, so commenter detail is missing).
**Skill:** new `simulation-vfx/godot-vfx-pack-shell-stacking`.

### 6. "My latest scientific visualisation" (nanoseb)

Source: https://www.reddit.com/r/blender/comments/1xqmova/my_latest_scientific_visualisation/ | r/blender post 1xqmova (score 57, 3 comments) | native Reddit clip

Tools used: **Blender** (assembly, procedural textures), a **specialist scientific fluid-dynamics software** (unnamed) for the core simulation, **Sketchfab** ship model (https://sketchfab.com/3d-models/container-ship-aaa41cca946b4a08bc08cf692b7757be, procedural textures added by the author).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: simulate the science in specialist software, assemble and texture the scene in Blender.

### Phase 1: Simulate the flow in specialist software

**Do**
1. Run the fluid-dynamics simulation (flow past two wing sails, wind-assisted propulsion) in the specialist scientific software.

**Check**
- The flow reads as physically plausible around the sails; commenters call it art ("'scientific' visualization my ass! that's an art piece right there!").

**Why**
- The simulation is the truth source; Blender is the presentation layer. (Inference, labeled.)

### Phase 2: Assemble in Blender

**Do**
1. Import the Sketchfab container-ship model.
2. Add procedural textures "to give it some more realism."
3. Bring the simulation output into the Blender scene.

**Check**
- The ship reads as a real vessel, not a bare import; commenters ask "What was the simulation software?" (unanswered in the retrieved comments).

**Why**
- Procedural textures are the cheap realism pass on a stock model. (Inference, labeled.)

### The human method, distilled
1. **Simulate where the science lives, present where the art lives.** Specialist solver for the flow, Blender for the scene.
2. **Procedural textures rescue stock models.** A Sketchfab import plus procedural texture work reads as authored.

**Depth status:** DEPTH-LIMITED (post text + 3 comments; simulation software unnamed, no parameters, no node setup; author: "I am far from being an expert"). No skill.
**Skill:** none (report only).

### 7. "Two weeks building my dream mech game with AI: the workflow behind Air Strider" (Chilkus)

Source: https://www.reddit.com/r/aigamedev/comments/1xquyde/two_weeks_building_my_dream_mech_game_with_ai_the/ + YouTube trailer https://www.youtube.com/watch?v=kwUxv7RbT1g (85 s, uploader Andres Chilkowski, no captions; metadata only, trailer has no narration) | r/aigamedev post 1xquyde (score 23, 4 comments) | play at https://chilkus.itch.io/air-strider

Tools used: **Codex** (coding and iteration), **JavaScript + Three.js** (browser game), **Vite** (development and builds), **Playwright** (browser checks and captures), **Supabase** (online rankings).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: feel first, then systems — iterate by playing, and protect what already works.

### Phase 1: Establish the feel before systems

**Do**
1. Establish movement, aiming, camera behaviour, and transformations first. Fighter, Strider, and Mech must feel distinct before adding more systems around them.

**Check**
- Play the build: each form feels different in the hand, not just different on paper.

**Why**
- "Start with the feel." If the three forms don't feel distinct, no amount of systems will save the game. (Author's stated order.)

### Phase 2: Give each form a purpose

**Do**
1. Separate combat into ground and aerial layers, then build ways for those layers to interact.
2. Make transforming change the player's options in a fight, not just the model.

**Check**
- Commenter note: "I want to see more purpose to turning into a mech …. That feels lacking vs the flight combat." The author has not answered; the mech's purpose is the known weak spot.

**Why**
- A transformation that changes options is a mechanic; one that changes only the model is a skin. (Inference, labeled.)

### Phase 3: Iterate through play

**Do**
1. Play a build, identify a specific problem, describe the desired behaviour, implement it, and play again.
2. Turn vague complaints into concrete discussions: "The turn feels wrong" becomes a concrete discussion about momentum, steering, banking, or camera response.

**Check**
- Each loop names one specific problem and one desired behaviour; the next play session tests exactly that.

**Why**
- "The interesting part wasn't getting AI to produce a first working prototype. It was using the shorter iteration cycle to keep pushing the details — the things that make a game feel like the one you imagined." (Author's stated principle.)

### Phase 4: Keep tuning accessible

**Do**
1. Put movement, weapons, camera, timing, and balance values into configuration files so adjustments don't require rebuilding the underlying systems.

**Check**
- A balance tweak is a config edit, not a code change.

**Why**
- Tuning is the most frequent change in a feel-first loop; config files keep it cheap. (Inference, labeled; the same content-as-data pattern as the watchlist's engine-decoupled rules row.)

### Phase 5: Protect what already works

**Do**
1. Preserve tuned movement and transformation timing while changing art or adding features.
2. Use focused tests and browser checks (Playwright) to catch regressions.
3. Judge the actual feel by playing; tests catch regressions, play judges feel.

**Check**
- A change that breaks tuned movement is caught by the tests before it ships; feel is verified by playing, not by the test suite.

**Why**
- In a fast iteration loop, the biggest risk is a good change quietly breaking tuned feel. Tests guard the tuning; play guards the feel. (Author's stated split.)

### Phase 6: Build presentation alongside combat

**Do**
1. Refine the transforming model, missile trails, explosions, destruction, sound, and HUD while building combat, so the action is readable and satisfying.

**Check**
- The action reads: the player can tell what is happening in a missile barrage.

**Why**
- Presentation is not polish applied at the end; readability is part of combat design. (Inference, labeled.)

### Phase 7: Add character, then turn the sandbox into a game

**Do**
1. Build a shared communications system for banter and dialogue, then connect choices and relationships to multiple endings.
2. Add a tutorial and story demo, then Survival Mode, scoring, balance, and online rankings (Supabase).

**Check**
- The story demo plays with banter, choices, and multiple endings; Survival Mode posts scores to online rankings.

**Why**
- The mech shooter "became a cockpit soap opera" — character is the differentiator once combat works. (Author's words.)

### The human method, distilled
1. **Feel first, systems second.** Distinct-feeling forms before systems around them.
2. **Vague complaint to concrete discussion.** "The turn feels wrong" becomes momentum, steering, banking, camera.
3. **Tune in config, not code.** Movement, weapons, camera, timing, balance live in files.
4. **Protect tuned feel.** Focused tests + browser checks catch regressions; play judges feel.
5. **Presentation is combat design.** Readability is built alongside the fighting, not after.

**Depth status:** FULL (complete author workflow post + 4 comments + trailer metadata; the trailer has no captions and no narration, and a media download would add gameplay frames only, not pipeline detail).
**Skill:** new `automation/ai-game-feel-iteration-loop`.

### 8. "IV Studio 1.0: I rebuilt my free, open-source film studio for ComfyUI + MiniMax H3 from your comments (now on Linux and Mac)" (itsVariance)

Source: https://www.reddit.com/r/comfyui/comments/1xqfux1/iv_studio_10_i_rebuilt_my_free_opensource_film/ | r/comfyui post 1xqfux1 (score 60, 9 comments, 8 retrieved) | native Reddit clip

Tools used: **IV Studio 1.0** (free desktop app, MIT, https://github.com/hollisorg/iv-studio, releases at https://github.com/hollisorg/iv-studio/releases/latest), **ComfyUI** (driven over its API), **MiniMax H3**, **Ollama** (separate address supported), **Fizgig** (local character-LoRA training), **RefMod** (characters from 1-6 photos), **InsightFace** (likeness scoring), **KJNodes** (live preview override), **Krea 2** (frames for the trailer's fairy-tale opening, Disney Renaissance-style LoRA), **SDXL** (Create > Image), **Comfy Cloud / RunPod / Modal** (cloud GPU), **154 MCP tools** (up from 142). Tested on a 4090 with 64 GB RAM. The Linux build passes its checks on GitHub, but the author has not run GPU work on a real Linux desktop yet. Builds are unsigned: Windows shows SmartScreen, Macs need "Open Anyway" the first time.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: the community's complaints became 1.0 — install friction, platform gaps, and missing training are the changelog.

### Phase 1: Install on any platform, with setup that fixes itself

**Do**
1. Linux: self-updating AppImage. Mac: Apple Silicon and Intel builds (rendering on your own cloud account). Windows: as before.
2. Settings > Setup installs every pack IV Studio needs, at pinned versions, in one click (answers the "missing custom nodes" complaint).
3. Your own H3 files (ComfyUI's template names, NVFP4, other turbo LoRAs) are recognised and used (answers "Setup says 7 to fix but H3 is installed").
4. Ollama on another address: set it in Settings (for ComfyUI and Ollama in separate containers).

**Check**
- Setup reports zero to fix when your own H3 files are present; pinned versions install in one click.

**Why**
- Install friction was the adoption blocker: the 1.0 changelog is mostly the community's install complaints, fixed. (Inference, labeled.)

### Phase 2: Let the app fit itself to the PC

**Do**
1. "Check my PC": on first launch it reads GPU, RAM, and drives and sets previews, finish size, the prompt writer, and downloads to suit.
2. If the card is too small, a guided setup connects RunPod, Modal, or Comfy Cloud.

**Check**
- A too-small card routes to cloud instead of failing locally; a commenter confirms it runs on an RTX 3060 12 GB ("Slow but works").

**Why**
- Fit the workload to the hardware before spending generation: previews and finish size follow the machine, not the other way round. (Inference, labeled.)

### Phase 3: Train actors locally, or make a RefMod in 30 seconds

**Do**
1. Train a character LoRA locally on your own 16 GB+ NVIDIA card through Fizgig (or on RunPod/Modal), with presets, a spending cap, "Train more," and InsightFace likeness scoring to pick the checkpoint.
2. Or make a RefMod character from 1 to 6 photos in about 30 seconds.

**Check**
- InsightFace scores pick the checkpoint; the RefMod path needs only photos, no training run.

**Why**
- Likeness scoring turns checkpoint-picking from taste into measurement; RefMod is the zero-training shortcut. (Inference, labeled.)

### Phase 4: Direct with live preview and per-shot control

**Do**
1. KJNodes' preview override streams every step into a floating panel on any page, including renders an agent starts over MCP.
2. Sampler and scheduler per shot; LoRA and RefMod trays in Create.
3. SDXL fine-tunes in Create > Image; Comfy Cloud as a third cloud option beside RunPod and Modal.
4. The app now has 154 MCP tools (up from 142), a tour that lights up the real controls one at a time, and a two-minute tour of the whole app.

**Check**
- Every step of a render is visible in the floating preview; per-shot sampler/scheduler settings stick to that shot.

**Why**
- Live preview plus per-shot control is the directing surface: see every step, tune each shot independently. (Inference, labeled.)

### The human method, distilled
1. **Ship the community's changelog.** 1.0 is the comments from the last post, fixed: Linux, Mac, one-click node setup, own-H3 recognition, Ollama address.
2. **Fit the app to the machine.** Check my PC sets previews and finish size from the actual GPU.
3. **Score likeness, don't eyeball it.** InsightFace picks the LoRA checkpoint.
4. **A 30-second RefMod beats a training run** when the character only needs to exist, not to be perfect.

**Depth status:** FULL (complete author writeup + 8 comments; Linux GPU work untested by the author is the known unknown).
**Skill:** expanded `ai-video/iv-studio-comfyui-film-studio` (1.0 update section).

### Screened out: "Some shots" (Realistic_Blueberry3)

Source: https://www.reddit.com/r/blender/comments/1xqrxvi/some_shots/ | r/blender post 1xqrxvi (score 46, 2 comments) | native Reddit clip

Selftext is one line: "a combination of modeling work in blender and shader work in unity." Comments are one-word replies. No workflow, no parameters, no technique. **Depth status:** NO-TOOLING.

## Have-vs-need tables

### Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Runtime procedural rig + skin (GDScript, Godot 4) | 1 (Primordium) | NEED | No rigging/skinning/retarget stage in the foundry (2026-09-26 audit); P1 gap, fix artifact prepared (Tripo P2.0 route) | Backlog (Primordium is a runtime route, not a foundry stage; use as reference implementation evidence for the P1 fix) |
| AI-video acceptance/checker pattern (prompt checker, take ranking, likeness scoring, per-segment check report) | 4 (H3 agent skill), 8 (IV Studio 1.0) | PARTIAL | No AI-vendor acceptance spec (P1 gap); per-shot lock lists + QC crew watchlist row is prior art | Backlog (borrow the checker + scoring shape for the P1 acceptance-spec fix artifact) |
| MiniMax H3 long-clip character swap (TemporalWindow, Spark-H3, Spectrum, split SelfLift, agent skill) | 4 | NEED | No AI-video stage in the foundry; trailer work is a future bucket | Watchlist (new variant skill staged; adopt when Aegis needs a trailer) |
| Godot VFX shell-stacking (per-shell surface offsets) | 5 (VFX packs) | NEED | No VFX stage in the foundry; PopcornFX stylized-laser row is the prior VFX watchlist entry | Watchlist (technique skill staged; cheap pattern if a VFX stage appears) |
| Godot grass shader variants (perf-tiered) | 2 | NEED | No vegetation/grass stage; ue-grass-cards-lod skill is UE-side | Watchlist (no code disclosed; revisit if a Godot grass breakdown appears) |
| Agent-driven iteration loop (Codex + Playwright checks + config tuning) | 7 (Air Strider) | PARTIAL | MCP-driven DCC loop is P2 (no fix artifact; agentic-blender-asset-pipeline skill is prior art) | Watchlist (pattern skill staged; the loop shape transfers to foundry iteration even though the DCC target differs) |
| FrameExtractor (COLMAP/3DGS keyframes, Homebrew install) | 5 (duplicate) | NEED | Intake has no video-frame front door; watchlist row BACKLOGGED | Backlog (already audited 2026-11-07; no change) |
| Meshlet pipeline (three.js r187 forest) | 9 (duplicate) | NEED | No GPU cluster culling in the foundry | Watchlist (already audited 2026-11-07; no change) |

### 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Runtime procedural rig + skin (GDScript) | 1 (Primordium) | PARTIAL | Generated hawk/boar art uses procedural rigs as stand-ins (beads 9le.25, p06.10, 9le.9); P1 production-conversion stage covers rigging | Watchlist (Primordium is a runtime alternative to baking rigs; the production-conversion fix artifact should note it) |
| Godot grass shader variants (perf-tiered) | 2 | NEED | No grass/vegetation shader stage in the Godot 4.7.2 pipeline | Watchlist (SimpleGrassTextured base is a concrete starting point; no code disclosed) |
| Godot VFX shell-stacking | 5 | NEED | No VFX stage; animated subjects rig only what exported clips use | Watchlist |
| Agent-driven iteration loop (Codex + Playwright + config tuning) | 7 | PARTIAL | 286 gdUnit4 cases + 198 QA gates + golden-path bot already guard regressions; config-file tuning is not yet a pattern | Adopt now (cheap: move tuning values into config files; Playwright-style browser checks already exist as the golden-path bot pattern) |
| FrameExtractor adaptive keyframes | 5 (duplicate) | PARTIAL | Own video frame extraction exists (`pipeline/reference/recon_pipeline.py`, fox frame extraction) | Watchlist (alternative front door; own extractor already exists) |
| Meshlet pipeline (three.js r187) | 9 (duplicate) | NEED | No GPU cluster culling; production-conversion P1 covers LODs, not meshlets | Watchlist (pattern only; no three.js engine in 2d3d) |
| MiniMax H3 long-clip character swap | 4 | NEED | No AI-video stage | Skip (trailer tooling; no attach point in a 2D/3D pixel-art pipeline) |

### Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Godot grass shader variants | 2 | PARTIAL | Own trees exist (`tools/city_trees.py`); no grass shader stage | Watchlist (perf-tiered shader pattern transfers to city greenery) |
| Agent-driven iteration loop (Codex + Playwright + config tuning) | 7 | PARTIAL | ~100 gdUnit-style tests + QA gates; no config-file tuning pattern | Adopt now (cheap: tuning values into config files fits the standalone pipeline) |
| Runtime procedural rig + skin | 1 | NEED | No rigging imposed on static buildings by design (PRD 17.1); animated subjects rig only what clips use | Skip (no attach point; buildings are sprites) |
| IV Studio 1.0 / H3 character swap | 4, 8 | NEED | No AI-video stage | Skip (no trailer pipeline in Desktop City) |
| FrameExtractor / meshlets | 5, 9 (duplicates) | NEED | No photogrammetry intake; no GPU cluster culling | Skip |

### Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Runtime procedural rig + skin (GDScript) | 1 | PARTIAL | Rigging stage present (`stages/rig.py`, `assetpipe/blender/rig.py`) — unlike Aegis, Solarempire rigs | Watchlist (runtime-rig pattern is an alternative to the baked rig stage for generated creatures; not a replacement) |
| Godot VFX shell-stacking | 5 | NEED | No VFX stage in the asset pipeline | Watchlist |
| Agent-driven iteration loop | 7 | PARTIAL | Per-asset audit + optimization reports with measured figures; no config-file tuning pattern | Adopt now (cheap: tuning values into config files) |
| Godot grass shader variants | 2 | NEED | No vegetation stage | Skip (space game; no grass) |
| IV Studio 1.0 / H3 character swap | 4, 8 | NEED | No AI-video stage | Skip |

## Watchlist trending

Curated genuine reappearances this run (the trend script's raw output over-matched on broad tokens like "Godot 4", "ComfyUI", "MiniMax H3", "Three.js", "Blender", "Houdini": it stamped 109 rows, of which 101 were token overlap, not genuine reappearances; those stamps were reverted and only the genuine ones below were kept):

- **Genuine:** AI video generation (MiniMax H3); SelfLift dual sampling + Color Transfer stitching (split SelfLift in today's H3 chain); MiniMax H3 no-masking character-swap LoRA recipe (akatz-ai Character Swap LoRA in today's chain); MiniMax H3 Reference-to-Video character swap + motion transfer (today's H3 post is that workflow); IV Studio (1.0 post); RefMod (IV Studio 1.0: RefMod characters from 1-6 photos in ~30 s); Gaussian Splatting preview in review flywheel (new r/Houdini R&D Gaussian Splats in Houdini 22 post); Engine-decoupled rules library + JSON content (Air Strider's config-file tuning is the same content-as-data pattern).
- **Not genuine (token overlap, stamps reverted):** Godot 4.5 .NET procedural creature pipeline (Primordium is GDScript runtime rig, a different project); Godot compute-shader creature brain; Cel Studio; Retrocrunch; Godot noise sky shader; Godot 1M-agent crowd; SyncTile; Chain Director; 2x2 storyboard-grid prompting; native 3MP low-VRAM recipe; Face Refiner; toy-to-real transition; Pruna P-H3-Image; all other ComfyUI/H3/Three.js/Blender/Houdini token matches; Codex CLI driving Blender via MCP (Air Strider uses Codex for coding, not Blender MCP); MCP servers driving Blender/Unreal (IV Studio's MCP drives ComfyUI film production, not Blender/Unreal); MeshletDrawingPipeline and Intelligent frame extraction (same posts re-scanned in the overlapping window, already audited 2026-11-07, no new evidence).

**New watchlist additions (10):** Spark-H3 sparse attention; Spectrum forecast caching for MiniMax H3; TemporalWindow / SpatialTiles for MiniMax H3; lightx2v Ref2VA turbo LoRAs; h3-motion-transfer agent skill; runtime procedural rig + skin generation in GDScript (Primordium); SimpleGrassTextured Godot grass base; gennai777 Godot VFX packs; Krea 2 image model; Fizgig local character-LoRA training.

## Gap recommendations

1. **Runtime procedural rig as P1 rig-gap reference implementation (Aegis).** Primordium generates rig + skin at runtime in GDScript. The prepared P1 fix takes the Tripo P2.0 baked route; note Primordium as the runtime alternative in the fix artifact. Next step: link the Primordium skill from the gap-fix notes.
2. **Borrow IV Studio's checker + scoring shape for the P1 acceptance spec (Aegis intake).** Prompt checker that catches what the model punishes, per-shot ranking three ways, InsightFace likeness scoring for checkpoints, per-segment check reports. Next step: add a "checker + score + report" section to the acceptance-spec fix artifact.
3. **Adopt config-file tuning + regression checks in 2d3d, Desktop City, Solarempire (cheap, no new tool).** Air Strider's loop — tuning values in config files, Playwright/focused tests guarding tuned feel — maps directly onto the existing QA gates in all three Godot repos. Next step: move one tuning surface (movement/camera) into a config file in 2d3d and note the pattern.
4. **Backlog the H3 TemporalWindow long-clip recipe for Aegis trailer work.** 720p to 15 s in one pass, 1080p in 4-6 s segments with 22-frame context, Spark-H3 + Spectrum + turbo LoRAs. Next step: none until Aegis needs a trailer; the variant skill holds the recipe.
5. **Watchlist the Godot VFX shell-stacking technique.** Per-shell surface offsets fixing z-fighting is a two-line fix with a clear failure mode; if any repo grows a VFX stage, this is the first pattern to lift. Next step: none; skill staged.

## Explicit non-goals

- **Houdini R&D Gaussian Splats (1xpcx44):** not analyzed; empty selftext, 0 comments, video-only. Would need a media download to audit; no slot used (H3 tutorial took the one download). Left as a scanned-but-unanalyzed note.
- **Sculpting a 3D stylized character for 3D printing (1xq4rzj):** sculpting showcase, no pipeline detail beyond tablet setup in comments. Skipped.
- **Nightscape three.js endless flight (1xqi3c8):** no tooling signal in the post text. Skipped.
- **"Would you pay $5 for a game like this?" (r/godot, 1xqbhib):** pricing question, no workflow. Skipped.
- **Vein Clot / hyperlapse / starling murmuration / water WIP posts:** showcase clips with zero tooling hits. Skipped.

## Sources and run notes

- Reddit scan: Arctic Shift API, 23 subreddits, 2-day window; 4 subs failed (unity, substance3d, proceduralgeneration, shaders — HTTP 526). Comments via fetch_comments.py (Arctic Shift); 3 posts hit Arctic Shift HTTP 422 on comments (1xqvpc1, 1xpdv8e, 1xpcx44); old-reddit JSON fallback is blocked in the sandbox (empty responses); PullPush returns HTTP 526. Full post text pulled via Arctic Shift posts search with the scan's own parameters.
- YouTube scan: all 11 channels failed after the CA fix — the sandbox egress CA in the video-summarizer venv's certifi bundle was stale (0 Hatch entries); refreshed from /usr/local/share/ca-certificates/hatch-egress-ca.crt, after which yt-dlp fetched listings, but full video extraction now hits YouTube's "Sign in to confirm you're not a bot" wall on every channel's newest video. YouTube source reported down for this run; Reddit only, per the skill. Note: single-video metadata extraction still works (both YouTube videos in this run returned metadata + descriptions). The CA refresh is a durable fix for the venv bundle.
- Depth escalation: 1 of 2 downloads used (H3 tutorial 4u1gw8Swt1s, mid quality, 25.7 MB, 12 frames reviewed). No approval gate encountered. Whisper transcription remains unavailable in the sandbox (model download blocked by design); no model download attempted.
- Skills staged this run: new `characters/godot-runtime-procedural-creatures`, new variant `ai-video/minimax-h3-temporalwindow-character-swap`, new `simulation-vfx/godot-vfx-pack-shell-stacking`, new `automation/ai-game-feel-iteration-loop`; expanded `ai-video/iv-studio-comfyui-film-studio` (1.0 update). Skill count 196 -> 200.
