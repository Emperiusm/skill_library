# Video tooling scout — have-vs-need, 2026-11-01

Depth mode: `pre-approved` (max 2 media downloads per run, Ehsan 2026-09-27).
Depth-escalation usage this run: **0 downloads attempted, 0 succeeded, 0 skipped.**
No video in the top 8 needed the deepened pipeline: every audited post had full
post text plus author comments, and no YouTube video entered the deep-analysis
set. The download allowance was untouched.

**YouTube source: DOWN for this run.** The scan's CA bundle
(`~/workspace/skills/video-summarizer/.venv/.../certifi/cacert.pem`) had again
lost its Hatch Sandbox Egress CA (rotated; the on-disk copy was stale). Per
AGENTS.md I refreshed it from `/usr/local/share/ca-certificates/hatch-egress-ca.crt`
(system store is kept current) and verified `youtube.com` returns 200 through
the bundle. Listing then worked (each channel's newest video IDs resolved), but
**all 11 channels failed full extraction** with YouTube's "Sign in to confirm
you're not a bot" wall (`--cookies-from-browser`/`--cookies` suggested). Per the
skill, the run continued with Reddit only; a dead source never blocks a run.
If the bot wall persists, the YouTube source stays down until a cookie-based
route is approved.

## Gap alerts

**No new P1/P2 gap matches this run.** Every extracted tool was checked against
`references/p1-gaps.md` by keyword and by meaning.

Two P2 strengthenings (not new; existing row "MCP-driven DCC loop (agents drive
Blender/UE, iterate visually)", BACKLOGGED):

1. **Claude drives ComfyUI through the Video Builder's MCP/API** (Cheap_Credit_3957,
   audit 3): the most complete public MCP-driven DCC loop seen yet. The agent
   wrote every scene prompt, ran 80 renders (~12 GPU hours, mostly overnight),
   reviewed every take itself, re-shot failures (cloned guests, bad camera moves),
   spliced fixes frame-exactly, and checked lip-sync per scene. Exact sampler
   settings disclosed (MiniMax H3 Singularity ref2va v2 int8; pass 1: 25 steps;
   pass 2: 8-step 768p ref2v LoRA v1.1, 4 steps, 0.35 denoise). This is the P2
   gap's exact shape in production, with cost data (12 hours, ~8% of a $20
   Claude Pro plan).
2. **ChatGPT + Blender MCP for previs** (Time-Ad-7720, audit 2): agentic Blender
   scene building (low-poly biplane + landscape: meadows, forests, mountains,
   lakes, clouds) feeding a MiniMax H3 reference-to-video pipeline. Same author
   as the existing `blender-mcp-camera-minimax` skill, new variant.

## Videos scanned and deeply analyzed

Reddit scan: **41 video posts across 23 subreddits**, last 2 days
(2026-10-30 to 2026-11-01), min score 20. YouTube scan: **0 videos** (source
down, bot wall on all 11 channels; see above).

Deep analysis (8 cap):

| # | Video (title) | Creator | Source | Sub | Depth |
|---|---------------|---------|--------|-----|-------|
| 1 | I built a free, open-source alternative to Substance Painter (Windows + Linux) | Admirable-Struggle78 (alla2001/material-painter) | v.redd.it/c6dzzd2gswyh1; r/3Dmodeling post 1xkrhq4 (score 190, 36 comments) | r/3Dmodeling | FULL (author comments carry the tooling detail) |
| 2 | Blender previsualization with MiniMax H3 | Time-Ad-7720 | v.redd.it/akqdv3440wyh1; r/comfyui post 1xkoos6 (score 95, 5 comments) | r/comfyui | FULL (author post text + writeup link) |
| 3 | Happy Halloween! MiniMax H3 did it again! Music video using my video builder inside ComfyUI | Cheap_Credit_3957 | v.redd.it/op532mi4duyh1; r/comfyui post 1xkhkea (score 84, 12 comments) | r/comfyui | FULL (exact human/agent division + exact settings) |
| 4 | Four generated worlds on a cube-sphere: plates, then climate, then water, then history on top | chronicleofgods | v.redd.it/y8wec4fb3myh1; r/proceduralgeneration post 1xkggn9 (score 72, 12 comments) | r/proceduralgeneration | FULL (6-stage pipeline + tuning story) |
| 5 | Real-scale planet terrain from plate tectonics and climate, seamless from orbit to the ground | Fresh-Daikon-9408 (exolunehq/exolune) | v.redd.it/l7nfmxr3ouyh1; r/proceduralgeneration post 1xkibsb (score 84, 12 comments) | r/proceduralgeneration | FULL (repo + emergent benchmarks) |
| 6 | Progress on my MetaHuman Character | skillerdose | v.redd.it/hhodb4m09nyh1; r/3Dmodeling post 1xjmkgy (score 88, 4 comments) | r/3Dmodeling | PARTIAL (mocap tool unnamed, no parameters) |
| 7 | LayerShop update: now with Regions | HonestTicket6013 | v.redd.it/g62bzjf6vtyh1; r/comfyui post 1xkef1v (score 57, 12 comments) | r/comfyui | PARTIAL (tool announcement; no executable workflow) |
| 8 | Not enough AI gamedevs building AI-gamedev tools, so I made one! This is an Infinite Language Generator | talamakina | v.redd.it/ndchef2mmyyh1; r/aigamedev post 1xkxs3d (score 81, 36 comments) | r/aigamedev | FULL (design-level; tool is WIP) |

## 1. "I built a free, open-source alternative to Substance Painter" (Admirable-Struggle78)

Source: https://www.reddit.com/r/3Dmodeling/comments/1xkrhq4/i_built_a_free_opensource_alternative_to/ | r/3Dmodeling post 1xkrhq4 (score 190, 36 comments) | Repo: https://github.com/alla2001/material-painter

Tools used: **material-painter** (alla2001/material-painter). Builds for
Windows + Linux + Mac (one app for Apple Silicon and Intel; not notarized, so
first launch needs right-click > Open). Author wrote it with Claude's
assistance: "Claude is not a person, so yeah it's only me, and I did contribute
by debugging and testing so I did help in the creation process."

This audit reconstructs the tool from the author's comments, step by step, so
another agent can evaluate it. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle). The
tool's core method is: author materials in a built-in node graph, write custom
shader nodes in WGSL, bake on the GPU with caching, export to engine presets.

### Phase 1: Design the material in the node graph

**Do**
1. Build the material in material-painter's built-in node graph (no external
   graph tool needed).
2. For custom behavior, write shader nodes directly in **WGSL**.

**Check**
- The graph evaluates live; iterate until the material reads correctly in the
  viewport.

**Why**
- The node graph is the differentiator the author names against ArmorPaint
  ("more mature and battle-tested"): material design happens inside the tool,
  not in an external DCC, and WGSL nodes keep the custom code portable to
  WebGPU-class targets.

### Phase 2: Bake on the GPU with caching

**Do**
1. Bake textures with the GPU baker; caching makes rebakes incremental.

**Check**
- Re-bake after edits: cached results should return near-instantly for
  unchanged regions.

**Why**
- GPU baking with caching is the second named differentiator; the bottleneck
  in texture painting is the bake-test loop, so the loop must be cheap.

### Phase 3: Export to engine presets

**Do**
1. Export with the built-in presets for **Unreal, Unity, Godot, Blender**.
2. If the source is a Substance file: stop. `.sbsar`/`.spp` are proprietary
   and cannot be loaded; import textures instead.

**Check**
- Verify the exported maps against the target engine's material inputs
  (albedo/normal/roughness/metalness/AO per the preset).

**Why**
- The author's copyright position is explicit: they considered importing
  Substance materials but decided it was against copyright rules, so the
  strategy is "the community make[s] and share[s] the materials." The export
  presets are the interoperability story instead of format conversion.

### The human method, distilled
1. Ship the tool, then grow the asset commons: the value of a painting tool is
   the materials library, so make the community the library (Discord for bug
   reports; releases on GitHub).
2. Don't fight proprietary formats; route around them with export presets.
3. An AI-assisted solo dev can ship a DCC tool: prompt, debug, test, ship.

**Depth status:** FULL (author's comments carry the feature set, the WGSL/GPU-bake
differentiators, the ArmorPaint comparison, the copyright position, and the
Mac build notes).

## 2. "Blender previsualization with MiniMax H3" (Time-Ad-7720)

Source: https://www.reddit.com/r/comfyui/comments/1xkoos6/blender_previsualization_with_minimax_h3/ | r/comfyui post 1xkoos6 (score 95, 5 comments) | Writeup: https://www.kaziahmed.net/kazitorials/biplane-adventures

Tools used: **Blender** (low-poly scene), **ChatGPT + Blender MCP** (agentic
scene building), **MiniMax H3 reference-to-video in ComfyUI**, **Suno**
(AI-assisted vocals for the author's original song "Believe in the Magic of
You").

This audit reconstructs the exact workflow shown in the post, step by step, so
another agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: block the whole shot list cheaply in a
lightweight 3D scene, then let the AI model spend the expensive generation
budget only on shots whose direction is already locked.

### Phase 1: Build the previs scene with an agent

**Do**
1. Prompt ChatGPT through Blender MCP to build a low-poly biplane and a
   landscape (meadows, forests, mountains, lakes, clouds).
2. Animate multiple camera angles into a **15-second loop**.
3. Keep geometry and textures deliberately crude: at the previs stage only
   camera angles, movement, composition, and timing matter.

**Check**
- Scrub the timeline: does the camera direction read without any textures?
  If not, fix the move before any generation.

**Why**
- (author's stated interest): test camera movements and shot compositions in
  a relatively lightweight 3D environment before committing to more
  resource-intensive AI video generations.

### Phase 2: Assemble reference inputs

**Do**
1. Render the Blender shots as visual references.
2. Prepare a **custom biplane reference sheet** for design consistency and a
   **pilot character reference**.
3. Write structured prompts guiding animation and visual style toward the
   target look: a **1990s hand-drawn anime aesthetic**.

**Check**
- The biplane reads as the same machine in every reference; the pilot's
  design is locked.

**Why**
- Reference sheets carry design consistency across shots; the Blender shots
  carry camera direction; the prompt carries style. Each input has one job.

### Phase 3: Generate with MiniMax H3 reference-to-video

**Do**
1. Feed the Blender shots + biplane sheet + pilot reference into MiniMax H3
   reference-to-video in ComfyUI with the structured prompts.

**Check**
- Verify each shot retains the original scene direction while hitting the
  1990s anime look.

**Why**
- The 3D scene is the cheap place to iterate; the generation budget is spent
  only after direction is settled.

### The human method, distilled
1. Direct the camera in 3D, generate the image in AI, never the reverse.
2. Reference discipline: one input per concern (direction, design, style).
3. (commenter Portable_Solar_ZA, affirmed by the thread): the same pattern
   works for background references — Blender virtual sets rendered out in
   MiniMax H3 as 360 videos. It is hit and miss: a simple square room came out
   perfectly; a small rectangular bathroom lost camera coverage inside it.
4. (commenter thesolewalker): the SolarRenderer LoRA
   (huggingface.co/Enderfga/SolarRenderer) is worth trying on this pipeline.

**Depth status:** FULL (author's full post text + writeup link + 5 comments).

## 3. "Happy Halloween! MiniMax H3 did it again!" (Cheap_Credit_3957)

Source: https://www.reddit.com/r/comfyui/comments/1xkhkea/happy_halloween_minimax_h3_did_it_again_music/ | r/comfyui post 1xkhkea (score 84, 12 comments) | YouTube mirror: https://youtu.be/c6fHIx32Z-s | Builder: https://github.com/vrgamegirl19/comfyui-vrgamedevgirl

Tools used: **VRGDG Video Builder in ComfyUI** (custom node + MCP/API);
**Claude** (agent); **MiniMax H3 Singularity ref2va v2 (int8)** with the
**8-step 768p ref2v LoRA v1.1**; **Krea 2** (three-panel character sheets);
**Nano Banana** (locations); **Suno 6** (song + stems); **ElevenLabs Scribe**
(lyric timing); **Topaz AI** (final enhance pass).

This audit reconstructs the exact human/agent division of labor the author
published, step by step, so another agent can follow the same process. Every
phase has three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The video's core method is: the human owns
the brief, the casting, and the verdicts; the agent owns the words, the
planning, and the overnight render farm; the sampler settings are fixed and
shared.

### Phase 1: The human briefs and casts

**Do**
1. Give Claude the story idea: a fun pop-punk style female rock song, a
   Halloween house party in a Victorian mansion, the band playing on a stage,
   the singer working the room between choruses.
2. Give Claude the character descriptions (the singer's costume is the one
   the author will wear that night; the bass player is what her sister plans
   to wear — Krea 2 rendered them "almost spot on").
3. Take Claude's lyrics and make the song in **Suno**, keeping the **stems**.
4. Take Claude's location prompts and make the mansion locations in
   **Nano Banana**.
5. Pick the characters from the ones Claude generated with the Krea 2
   three-panel reference-sheet workflow.
6. Set staging rules: instruments only on the stage; guests partying naturally
   (no crowd posing behind her); lots of close-ups when she's off stage; fun
   camera moves.

**Check**
- The cast sheets look like the intended people before any video is rendered;
  the song stems separate cleanly (the agent needs them for timing).

**Why**
- Everything the human cares about being right (cast likeness, staging rules,
  song) is decided by the human. The agent never re-decides casting.

### Phase 2: The agent plans and renders

**Do**
1. Let Claude: write the location prompts; build the band and guest characters
   from the descriptions with Krea 2 three-panel reference sheets.
2. Let Claude time every sung word with **ElevenLabs Scribe** and work out
   from the stems who plays when.
3. Let Claude plan the video (**19 scenes, 2:29**) and write every MiniMax H3
   prompt, with lyric timing for each shot and the facial acting.
4. Let Claude run the whole render queue through the Builder's Agent API:
   **80 renders, about 12 GPU hours**, much of it overnight.
5. Let Claude review every take itself and re-shoot failures (cloned guests,
   the camera pulling back wide on a held note).
6. Let Claude splice the fixed scenes into the final video frame-exactly and
   check the lip-sync in every scene.

**Check**
- Every scene passes the agent's own take review; the human reviews drafts
  and the finished video and orders re-shoots of anything disliked (the stage
  scenes were all close-ups at first, so the human asked for wide shots with
  moving cameras; the human also asked for a new opening — guests arriving at
  the house — and the agent redid the prompts and re-ran the scenes).

**Why**
- The agent is its own critic with a re-shoot budget; the human is the final
  verdict. The re-shoot loop is the quality contract.

### Phase 3: Lock the sampler settings

**Do**
1. Use the exact settings the author published:
   - Model: **MiniMax H3 Singularity ref2va v2 (int8)**
   - Pass 1: **25 steps**
   - Pass 2: the **8-step 768p ref2v LoRA v1.1, 4 steps, 0.35 denoise**
   - Characters: Krea 2 three-panel sheets; Locations: Nano Banana; Song: Suno 6
2. Run everything through the VRGDG Video Builder in ComfyUI. A 2-pass
   workflow with the same settings ships in the repo's `Workflows/MiniMax-H3-Two-Stage-Sampling-v2/`
   folder for single scenes; the full video needs the builder. (Note: the main
   model is now the V2, so swap the LoRA accordingly.)
3. Optional finishing: a final enhance pass in **Topaz AI** to fix far-away
   blurry faces from wide shots ("You don't need to do this. It looks fine
   both ways.").

**Check**
- The 2-pass shareable workflow reproduces one scene with the same settings.

**Why**
- Fixed settings + one builder = reproducible pipeline; the enhance pass is
   a polish option, not a crutch.

### The human method, distilled
1. **Brief once, verdict often**: the agent owns words, planning, and the
   render farm; the human owns casting, staging rules, and re-shoot orders.
2. **Timing is data**: lyric timing from ElevenLabs Scribe + song stems turns
   "a music video" into per-shot per-word direction.
3. **Cost it**: this video took ~12 hours including the overnight render and
   next-day re-rolls, and used about **8% of Claude usage on the $20 pro
   plan**. (Commenter note: the same stack runs locally with LM Studio or
   Gemma4/Qwen .gguf models instead of Claude.)

**Depth status:** FULL (the author's own verbatim human/agent division,
exact sampler settings, render counts, GPU hours, and cost).

## 4. "Four generated worlds on a cube-sphere" (chronicleofgods)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xkggn9/four_generated_worlds_on_a_cubesphere_plates_then/ | r/proceduralgeneration post 1xkggn9 (score 72, 12 comments) | Game: Chronicle of Gods, https://store.steampowered.com/app/5221390/

Tools used: the author's custom generator (god game *Chronicle of Gods*).

This audit reconstructs the exact pipeline the author published, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The generator's core method is: one seed, six fixed stages run
once per world, on a cube-sphere whose tiles are grouped into biome regions —
and the history simulation then runs on regions, not tiles.

### Phase 1: Crust — where the continents sit

**Do**
1. From the seed, place the continents.

**Check**
- The landmass layout reads at a glance on the parchment-atlas render.

**Why**
- Everything downstream (plates, climate, realms) inherits from this one
  placement; get the continents right first.

### Phase 2: Plates — Voronoi tectonics

**Do**
1. Run Voronoi tectonics over the crust.
2. Where plates push together, raise **mountain ranges**; where they pull
   apart, cut **rifts**; at sea, place **trenches**.

**Check**
- Mountain chains sit on convergence boundaries; rifts on divergence.

**Why**
- Terrain features inherit from plate boundaries, so the map tells a
  geological story instead of being noise with excuses.

### Phase 3: Elevation, then solve for sea level

**Do**
1. Compute elevation from the plate features.
2. Solve for the sea level that partitions land from ocean.

**Check**
- Continent/ocean balance looks plausible before climate runs.

**Why**
- Sea level is a solved value, not a tuned constant; the elevation field
  decides it.

### Phase 4: Climate — temperature, moisture, rain shadows

**Do**
1. Temperature from **latitude and height**.
2. Moisture from **rain bands**, with **rain shadows behind the mountains**.

**Check**
- Wet windward, dry leeward; deserts and jungles land where the rules say.

**Why**
- Two drivers (latitude/height, rain bands) produce the whole climate;
  mountains are climate machines, not decoration.

### Phase 5: Hydrology — flood, judge, and carve

**Do**
1. **Flood** the basins, **judge** them, then **carve**: basins fill, small
   ones get culled, dry ones drain instead of staying lakes, and rivers carve
   their way out to the sea.

**Check**
- Lakes span sizes from small to inland seas (the author's hard-won tuning:
  the first settings culled every lake under a size, so every survivor was a
  huge inland sea. Lowering the floor and letting dry basins drain fixed it —
  and as a side effect added rivers, "because a drained basin has to empty
  somewhere").

**Why**
- The lake-culling floor is the tuning knob that decides whether the world
  has rivers at all; hydrology is a judgment loop, not a one-shot fill.

### Phase 6: Fertility and biomes — moisture spreads, lookup decides

**Do**
1. Spread river and lake moisture into the surrounding land.
2. Assign each tile's biome by lookup on **temperature band x moisture band**.
3. Group tiles into **regions that follow the biomes**; the surface is a
   **cube-sphere: six square faces with 5 km tiles**.

**Check**
- Region boundaries follow biome boundaries; the simulation works on
   regions, not single tiles.

**Why**
- Regions are the simulation's unit of work (the mortal realms grow on top
   of the terrain as colored patches); single tiles are too fine to simulate
   history on. The parchment-atlas render shows four worlds, each from a
   seed, with only two map layers on in the clip (realms and their wars, fog
   lifted; in play only part of the world is visible).

### The human method, distilled
1. Fixed pipeline, run once: crust -> plates -> elevation/sea level ->
   climate -> hydrology -> biomes. Order is load-bearing.
2. Tune the judgment loops, not the noise: the lake floor setting decided
   the world's rivers.
3. Ask the open question in the open: the author asks readers who did rivers
   on a sphere whether they carved from the heightmap like this or routed
   first and cut the terrain to fit (commenter MrNotmark: route then carve —
   "much easier").
4. Disclosure as method: the author states the marketing text is mostly
   AI-generated (reread and reiterated many times; the Steam page took many
   hours), and that playtests start on Discord in a week or two.

**Depth status:** FULL (author's six-stage pipeline verbatim + the lake-tuning
story + the region-over-tile simulation design).

## 5. "Real-scale planet terrain from plate tectonics and climate" (Fresh-Daikon-9408)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xkibsb/realscale_planet_terrain_from_plate_tectonics_and/ | r/proceduralgeneration post 1xkibsb (score 84, 12 comments) | Repo: https://github.com/exolunehq/exolune

Tools used: **Exolune** (github.com/exolunehq/exolune, open repo with docs on
the making).

This audit reconstructs the exact technique the author published, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The engine's core method is: simulate plates once at startup in
under a second, then evaluate everything per point on the GPU every frame —
so a 1:1-scale planet needs no streaming.

### Phase 1: Simulate plates at startup (< 1 s per planet)

**Do**
1. Simulate plates at startup; budget **under one second per planet**.
2. Type every boundary: **collisions, subduction trenches, rifts, ridges,
   transforms, active and passive margins**.

**Check**
- All boundary types present and typed; startup stays under the second.

**Why**
- One fast sim replaces baked heightmaps; plates are data, not assets.

### Phase 2: Derive terrain from boundary distance

**Do**
1. Compute the large forms as **profiles on the distance to the boundaries**.
2. Drive the noise detail by the **local geology**.

**Check**
- The author's emergent benchmarks on the default Earth-sized planet
   (6,378 km radius): highest peak **8,541 m** (a stratovolcano on a mountain
   range); deepest point **10,539 m below sea level** (bottom of a subduction
   trench); ~19 km total relief, in the range of Everest (8,849 m) and the
   Challenger Deep (~10,935 m). The plate boundary profiles are calibrated on
   Earth's — "but nobody placed these two spots: they come out of the plate
   simulation."

**Why**
- Emergent extremes are the acceptance test: if the sim is right, Everest
   and the trench appear on their own.

### Phase 3: Climate from winds and relief

**Do**
1. Climate from **prevailing winds and relief**: wet windward slopes, rain
   shadows, deserts under the subtropical highs.
2. Let **vegetation, snow, and clouds** follow the climate.
3. Add **volcanism**: arcs, hotspot chains, atolls. (Erosion — river valleys,
   glaciers, coastal cliffs — is the stated next step.)

**Check**
- Deserts sit under the subtropical highs; vegetation tracks moisture.

**Why**
- Climate is derived, not painted; it follows the same terrain the plates
   made.

### Phase 4: Render per point on the GPU, no streaming

**Do**
1. Evaluate everything **per point on the GPU each frame**, in **double
   precision near the ground**.
2. Stream nothing: fly **from orbit down to a pebble in one shot**.

**Check**
- One continuous flight, no loading, no streaming hitches; precision holds
   at ground level.

**Why**
- (author): "One of the advantage of this rendering engine is that there is
   no loading nor streaming, so no flight speed limitation." Per-point GPU
   evaluation is what makes 1:1 scale tractable.

### The human method, distilled
1. Calibrate on Earth, trust emergence: boundary profiles from Earth's, then
   let the peaks and trenches surprise you.
2. Fast startup is a feature: plates in under a second means planets are
   disposable — generate, fly, discard.
3. Open the repo and the docs early; the author explicitly welcomes feedback
   and contributors.

**Depth status:** FULL (startup budget, boundary type list, 1:1 scale number,
GPU eval design, and the emergent peak/trench benchmarks, all from the author).

## 6. "Progress on my MetaHuman Character" (skillerdose)

Source: https://www.reddit.com/r/3Dmodeling/comments/1xjmkgy/progress_on_my_metahuman_character/ | r/3Dmodeling post 1xjmkgy (score 88, 4 comments)

Tools used: video-to-motion-capture conversion (**tool unnamed**), **MetaHuman**
character in **Unreal Engine**, **Niagara Simulation** (hair),
**Chaos Cloth Simulation** (clothes).

The workflow, as stated by the author: convert a video to motion capture data
and use it on the MetaHuman character for **facial animation** in Unreal
Engine — and "everything was in real time." Hair runs on Niagara Simulation;
clothes on Chaos Cloth Simulation. Commenter feedback on the bake: the jacket
edges look off — bevel the edges before baking the high poly (bevel to the
power of 4 of the subdiv level for a smooth edge); the author confirms the
cloth model is high-poly baked into low-poly.

**Depth status:** PARTIAL (the video-to-mocap tool is unnamed and no parameters
are given; the real-time claim and the Niagara/Chaos stack are the substance).

## 7. "LayerShop update: now with Regions" (HonestTicket6013)

Source: https://www.reddit.com/r/comfyui/comments/1xkef1v/layershop_update_now_with_regions/ | r/comfyui post 1xkef1v (score 57, 12 comments) | Download: https://layershop.aardvarkstudios.net/

Tools used: **LayerShop v0.17** (ComfyUI image-editing front-end).

The announcement: v0.17 supports creation with **regions** for four local
models — **MOSS Image**, **Flux 3 Klein**, **Ideogram 4**, **FIBO 2 Dev**.
The author's ranking: MOSS Image support is "best in class"; FIBO 2 is worst,
"sometime this model treats the bounding boxes as suggestions of approximate
placement, but still better then nothing." Linux support is on the todo list.

Comment thread notes: Krea 2 does not natively support bounding-box/region
creation; workarounds exist (Krea2-BBOX-Prompter on GitHub,
krea2-turbo-bbox on HuggingFace, "will take lot more work of course"). The
open test the community wants: two neighboring regions with different colors
(a red mug in one box, a blue mug in the other) — keeping attributes from
swapping across touching boxes is the hard part.

**Depth status:** PARTIAL (tool announcement with model list and author
ranking; no executable workflow to extract).

## 8. "Infinite Language Generator" (talamakina)

Source: https://www.reddit.com/r/aigamedev/comments/1xkxs3d/not_enough_ai_gamedevs_building_aigamedev_tools/ | r/aigamedev post 1xkxs3d (score 81, 36 comments)

Tools used: the author's **Infinite Language Generator** (WIP); a local audio
voice tool tailored to scramble English; MCP integration.

This audit reconstructs the tool's design from the author's posts and
comments, step by step, so another agent can follow the same process. Every
phase has three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The tool's core method is: generate the
whole language once from a seed, deterministically — then voice it and glyph
it.

### Phase 1: Generate the language from a seed call

**Do**
1. Make one seed call that produces the **whole language + rules**.
2. Keep it **deterministic**: "so far, yes, all deterministic" — one exact
   sentence sounds the same even hours apart. ("Technically, someone could
   spin up entire races with this tool.")

**Check**
- Re-request the same sentence later: identical output. Extend the language
   without regenerating already-recorded dialogue (the community's explicit
   feature ask: "If you add new vocabulary later, can the existing
   word-to-sound mappings stay fixed?").

**Why**
- Consistency is the product: hand-making a consistent language "isn't
   something worth burning tokens into," so the seed call buys it once and
   the determinism keeps it.

### Phase 2: Voice it and glyph it

**Do**
1. Run the author's **local audio voice tool**, "specifically tailored to
   scramble English into other 'fictional' languages" (ships character
   consistency), instead of a vendor API (ElevenLabs "ships a lot of
   features" but the local tool is purpose-built).
2. Generate **animated glyphs** for the language.
3. Ship the **whole dictionary and a subtitle tool** with it.

**Check**
- Voiced lines stay character-consistent; the subtitle tool covers the
   generated dialogue.

**Why**
- A fake language needs three artifacts to be usable in a game: the words
   (dictionary), the voice (audio), and the writing (glyphs).

### Phase 3: Tool it up

**Do**
1. Expose the tool so it "can tool up with an MCP."
2. Solve the open UX problem the author names: making **"Editing a Language
   Construct"** visually appealing to the user.

**Check**
- Another agent can call the generator through MCP; a human can edit a
   construct without regenerating the world.

**Why**
- (author's thesis): "we aren't building tools that actually help AI-enabled
   workflows... Most of you are relying on Claude/Codex to actually build the
   tools you want, as you go along. This, I feel, is a mistake." The choice is
   "token usage + time dedicated"; "simply 'cloning' this feature isn't worth
   the effort."

### The human method, distilled
1. Deterministic first: seed once, keep mappings fixed, extend without
   regenerating.
2. Build the tool, don't rent the workflow: purpose-built local voice
   scrambling beats a general vendor API for fictional languages.
3. Ship the boring parts too: dictionary + subtitle tool are what make the
   language shippable.

**Depth status:** FULL at design level (the tool is WIP; the determinism
contract, the three artifacts, and the MCP direction are all author-stated).

---

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| material-painter (open-source Substance alternative: node graph, WGSL nodes, GPU baking) | audit 1 | NEED | Inventory: "No PBR texture/material import policy or material validation gate"; foundry has ORM packing + OptiX baking but no hand-authoring tool | watchlist (added 2026-11-01): manual texturing fallback for foundry outputs; test export presets against ORM packing |
| Blender MCP previs → MiniMax H3 ref-to-video | audit 2 | NEED | No AI-video/trailer pipeline in inventory; P2 MCP-driven DCC loop is BACKLOGGED | watchlist: trailer bucket; strengthens P2 |
| Claude-driven ComfyUI via Video Builder MCP/API (exact settings, self-review loop) | audit 3 | NEED (P2 shape) | P2 "MCP-driven DCC loop" row: prior art was `agentic-blender-asset-pipeline` skill; this is a richer production instance | backlog: keep as the P2 spike reference; skill expanded this run |
| Cube-sphere planet pipeline (6 fixed stages, region-based history sim) | audit 4 | NEED | No planet/terrain generation in inventory | skip for Aegis (asset foundry scope); technique noted |
| Exolune 1:1-scale GPU planet engine | audit 5 | NEED | No planet/terrain generation in inventory | watchlist: technique reference if runtime terrain ever enters scope |
| Video-to-mocap → MetaHuman (real-time, Niagara hair, Chaos Cloth) | audit 6 | NEED | Inventory: "No rigging / skinning / animation-retarget stage in the foundry" (P1) | backlog: thin but real-time video→facial-mocap evidence; mocap tool name still open |
| LayerShop v0.17 (region-based local image gen) | audit 7 | NEED | No image-edit stage with regions | skip for Aegis |
| Infinite Language Generator (seed-deterministic conlang + voice + glyphs) | audit 8 | NEED | `tools/ts/lore-compiler` exists but compiles lore; no language generation | watchlist: NPC-language generation adjacent to lore tooling |

### 2d3d

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| material-painter | audit 1 | PARTIAL | `pipeline/proc/make_textures.py` (procedural, seeded) exists; no hand-painting tool | watchlist |
| Blender MCP previs → MiniMax H3 | audit 2 | NEED | 2D pixel-art pipeline; no previs stage | skip |
| Video Builder agent stack | audit 3 | NEED | No trailer pipeline | skip (trailer bucket only) |
| Chronicle of Gods planet pipeline | audit 4 | NEED | 2D side-scroller; planet-gen out of scope | skip |
| Exolune | audit 5 | NEED | Out of scope | skip |
| MetaHuman video-to-mocap | audit 6 | NEED | 2D pixel-art characters | skip |
| LayerShop | audit 7 | NEED | No image-edit stage | skip |
| Infinite Language Generator | audit 8 | NEED | `pipeline/proc/make_audio.py` (procedural); no language-gen | watchlist: NPC barks |

### desktop-city

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| material-painter | audit 1 | NEED | Procedural assets; no hand-authoring tool | skip |
| Blender MCP previs → MiniMax H3 | audit 2 | NEED | No previs stage | skip |
| Video Builder agent stack | audit 3 | NEED | No trailer pipeline | watchlist (trailer bucket) |
| Chronicle of Gods region-based sim (tiles → biome regions; sim runs on regions) | audit 4 | NEED | No region-tick sim pattern evidenced | watchlist: region-over-tile pattern relevant to city-sim ticking |
| Exolune | audit 5 | NEED | No planet/terrain engine | skip |
| MetaHuman video-to-mocap | audit 6 | NEED | No characters | skip |
| LayerShop | audit 7 | NEED | No image-edit stage | skip |
| Infinite Language Generator | audit 8 | NEED | No dialogue system evidenced | skip |

### solarempire

| Tool / stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| material-painter | audit 1 | NEED | AI-generated assets; no hand-authoring | skip |
| Blender MCP previs → MiniMax H3 | audit 2 | NEED | No previs stage | skip |
| Video Builder agent stack | audit 3 | NEED | No trailer pipeline | watchlist (trailer bucket) |
| Chronicle of Gods planet pipeline | audit 4 | NEED | Space game; no planet-surface generation evidenced | watchlist: planet-surface prior art |
| Exolune 1:1-scale planet engine | audit 5 | NEED | No planet-surface generation evidenced | watchlist: strongest planet-gen prior art seen; emergent-benchmark pattern |
| MetaHuman video-to-mocap | audit 6 | NEED | No character pipeline | skip |
| LayerShop | audit 7 | NEED | No image-edit stage | skip |
| Infinite Language Generator | audit 8 | NEED | No language system | skip |

## Watchlist trending

Genuine reappearances (6), verified against today's evidence. Note:
`bin/trend_watchlist.py` initially auto-matched 65 rows by token overlap
("MiniMax H3", "ComfyUI", "Blender", "Niagara", "MetaHuman" etc.); 59 of those
were false positives and were removed from the watchlist before this report
was written, per the watchlist's standing convention
("[DATE auto-match was token overlap on ...; not a genuine reappearance]").
The 59 removed include: GPT Astra, SelfLift/SyncTile/Chain Director/storyboard
grid/long-video rows, Scumble, ComfyUI Asset System, comfyui-minimax-h3-studio,
Pocket AI, OmniChar, Flux Klein node pack, YEDP, RefMod, FLUX 3 Image Klein,
Pixaroma pack, MAINodes, Freefield, FrameForge, agentY, ComfyUI Motion Previs
Studio, Open-H3-Regenerate-2K, Opsis, ComfyUI-ldoi, ComfyUI custom-nodes row,
Squishy Volumes, ribbon cables, Light Wrangler, HBLink, Raup, Blender+AE+Resolve,
fake-sim rigging, Pebblecrete, galaxy generator, Nomad, GeoNodes flower, WETA
bubbles, Arborea, billboard, inverted hull, voxel-remesh, three-point lighting,
square-to-round, Decimate, hidden-geometry, Mass Battle, KeenFace.

## Watchlist trending
- MCP servers driving Blender/Unreal (agentic DCC) (first seen 2026-09-27, status BACKLOGGED; seen again 2026-09-28, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-30, 2026-11-01) **TRENDING**
- Codex CLI driving Blender via MCP (mannequin-guided camera motion) (first seen 2026-09-28, status WATCH; seen again 2026-09-28, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-30, 2026-11-01) **TRENDING**
- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-03, 2026-10-05, 2026-10-08, 2026-10-09, 2026-10-11, 2026-10-16, 2026-10-21, 2026-10-24, 2026-10-27, 2026-10-28, 2026-10-29, 2026-11-01) **TRENDING**
- Nano Banana-class image edit in intake/ (first seen 2026-09-27, status BACKLOGGED; seen again 2026-09-28, 2026-11-01) **TRENDING**
- Krea 2 image-to-video in AI music-video stack (first seen 2026-10-23, status WATCH; seen again 2026-10-24, 2026-10-27, 2026-11-01) **TRENDING**
- MOSS-Image (OpenMOSS, 5B DiT + Qwen3.5-9B text encoder + FLUX.2 VAE, Apache 2.0) (first seen 2026-10-21, status WATCH; seen again 2026-10-28, 2026-11-01) **TRENDING**

New watchlist additions this run: **material-painter** (open-source Substance
Painter alternative), **Exolune** (1:1-scale GPU planet engine),
**Infinite Language Generator** (deterministic conlang tool),
**LayerShop** (ComfyUI image editor, v0.17 regions).

## Gap recommendations

1. **Video Builder agent stack (audit 3) — the P2 MCP-driven DCC loop's best
   production evidence.** Exact sampler settings, verbatim human/agent labor
   division, an agent self-review + re-shoot loop, and cost data (12 hours,
   ~8% of a $20 Claude Pro plan). Next step: use the expanded
   `comfyui-video-builder-agent-music-video` skill as the P2 spike reference
   when the Aegis foundry loop is designed.
2. **material-painter (audit 1) — first credible open-source Substance Painter
   alternative in the wild.** Node graph + WGSL custom nodes + GPU baking with
   caching; none of the four repos has a hand-authoring texturing tool.
   Next step: try its export presets against Aegis's ORM packing
   (`runtime/orm_pack`) and note where the preset maps disagree.
3. **Exolune (audit 5) — strongest planet-gen technique seen.** 1:1 scale,
   per-point GPU evaluation, no streaming, and the emergent-benchmark pattern
   (Earth-calibrated profiles; peaks/trenches appear on their own). Next
   step: keep as watchlist prior art for Solarempire planet surfaces and any
   Desktop City scale ambitions.
4. **MetaHuman video-to-mocap (audit 6) — thin but adjacent to the P1 rig gap.**
   Real-time video→facial-mocap onto MetaHuman with Niagara hair + Chaos Cloth
   is the only real-time facial pipeline evidence seen. Next step: the mocap
   tool name is still open (author didn't name it); a read-only check of the
   thread later could close it.

## Explicit non-goals

- "This took 12 hours to make and nobody cares..." (r/comfyui 1xjv2d9,
  Grinderius, score 493, 188 comments): 25 top comments fetched; the thread is
  debate about open-source AI video realism, not a workflow. No extractable
  tooling — NO-TOOLING.
- "Excavated pipe area: original video vs. Gaussian splat" (r/photogrammetry
  1xjwcwc, AECPLATFORM): vendor demo, 2 comments, no workflow detail —
  NO-TOOLING.
- "Claude Code made a unique trailer for my game" (r/vibecoding 1xkpw07,
  TheGrowthYardGaming): YouTube video, 0 Reddit comments, YouTube metadata
  degraded and source down — DEPTH-LIMITED, skipped (no download attempted).
- Rim2812 UE5 vehicle-damage plugin, navarisun ComfyUI Motion Previs Studio,
  sanchezrobertodev Opsis, uisato Generative Lexicon Press: all audited
  2026-10-31; not re-audited.
- The remaining scanned posts are game/mechanic showcases with no extractable
  tooling (astronomy app, leg grabbers, three.js prototype, RTS car steering,
  Incredibles fan game, "What I see vs what you see" memes, falling-sand and
  crab sims, exploding-animals sprite tool [6 comments, two-click tool for
  laypeople — interesting but no workflow detail], Procedural Planet for RTS
  [15 comments, ask-for-feedback post, no pipeline detail]).
