# Video tooling scout: have-vs-need — 2026-11-05

Daily run of the video-tooling-scout (Reddit scan, last 2 days). Depth-escalation mode: `pre-approved`, max 2 media downloads (Ehsan 2026-09-27).

## Gap alerts

**No P1 gap fills today.** None of the eight audited videos fills a P1 row in
`references/p1-gaps.md` (rigging/retarget, perf budgets, import validation
gates, mesh compression, mesh refinement, AI-vendor acceptance spec, art
bible, skyline fill, Godot import gate). Two P2-adjacent signals, not fills:

- **P2 MCP-driven DCC loop — two new data points, same day.** The soda ad
  (audit 5) builds its 3D blockout with ChatGPT + Blender MCP, and the
  ComfyUI-VFX-Suite (audit 2) ships an AI Director that drives ComfyUI over
  MCP (Ollama local LLM, or Claude/ChatGPT via MCP). Both are agents driving
  a DCC-adjacent tool and iterating visually, which is the shape the P2 gap
  prescribes (spike Blender MCP behind the review stage). Neither is the full
  loop (no visual-iteration cycle is shown), so the gap stays open; the
  evidence for spiking it is now stronger.
- **P1 AI-vendor acceptance spec — adjacent evidence only.** RefMods (audit
  7) bakes character identity into a scored, reusable file (face + voice),
  and the Hiraeth design audits (audit 3) are "what good means" as runnable
  agent skills. Both are the right shape for the acceptance-spec gap, but
  neither is a per-asset-type generation/acceptance spec for the Aegis
  intake, so the gap stays open.

## Videos scanned

- **54 video posts** across 23 subreddits (unity, unrealengine, godot,
  threejs, GraphicsProgramming, blender, houdini, substance3d,
  photogrammetry, gameassets, topology, aigamedev, comfyui, vibecoding,
  technicalart, proceduralgeneration, vfx, RealTimeVFX, shaders,
  VoxelGameDev, Simulated, 3Dmodeling, gamedev), last 2 days (Nov 3-5,
  2026), min score 20.
- **Caveats:** the first scan run found 56 videos; the second run found 54
  because r/unity returned HTTP 521, so Unity posts are missing from this
  run. Comment retrieval first failed for five posts because the scout
  passed the v.redd.it media IDs to the comment API; retrying with the
  correct post IDs from the permalinks retrieved all of them (soda ad 9/9,
  forest 25/42, RefMods 11/12, Pruna 12/13, falling-sand 4/4). PullPush
  returned HTTP 521 during the first attempt but was not needed after the
  retry; old-Reddit JSON is bot-walled from this sandbox (302). Post text
  beyond the scan's 300-character snippet was recovered for all eight
  audits on a re-fetch (Arctic Shift is flaky across runs: the same query
  missed these posts an hour earlier).
- **YouTube channel scan: down for this run.** All 11 configured channels
  failed. The sandbox egress CA was missing from the video-summarizer
  venv's certifi bundle; appending the current CA from
  `/usr/local/share/ca-certificates/hatch-egress-ca.crt` fixed the SSL
  errors, but every channel then hit YouTube's "Sign in to confirm you're
  not a bot" wall. Per the skill, the YouTube source is down for this run;
  Reddit only. No login is available in this loop, so no retry.

## Videos deeply analyzed

| # | Video | Creator | URL | Duration |
|---|-------|---------|-----|----------|
| 1 | I Open Sourced the Digital Twin Plugin From My Unreal Fest Talk (BIM streaming plugin for UE5) | Third Space Interactive | https://www.youtube.com/watch?v=eQsCQ-yeNXw | 291 s (4:51) |
| 2 | From a raw video to a finished shot — entirely local, entirely inside ComfyUI, and all under 24 GB of VRAM (ComfyUI-VFX-Suite) | Turbulent-Barber582 | https://www.reddit.com/r/comfyui/comments/1xnm2tl/from_a_raw_video_to_a_finished_shot_entirely/ | native Reddit clip |
| 3 | One month building Hiraeth: a Moebius-inspired adventure game, with Opus 5.5, Astra, Tripo & Suno (expansion of the 2026-11-04 audit) | 4nf | https://www.reddit.com/r/threejs/comments/1xn2uff/one_month_building_hiraeth_a_moebiusinspired/ | native Reddit clip |
| 4 | Infinite terrain and biome generation in Godot | ErmanStudio | https://www.reddit.com/r/proceduralgeneration/comments/1xn1fbv/infinite_terrain_and_biome_generation_in_godot/ | native Reddit clip |
| 5 | I used a Blender blockout to guide an AI-generated soda ad | Time-Ad-7720 | https://www.reddit.com/r/comfyui/comments/1xn4cq4/i_used_a_blender_blockout_to_guide_an_aigenerated/ | native Reddit clip |
| 6 | Custom Engine Forest Showcase - (130 fps average on RTX 3080 1440p) | Novapierce_ (repost of Toni Macaroni) | https://www.reddit.com/r/GraphicsProgramming/comments/1xnly73/custom_engine_forest_showcase_130_fps_average_on/ | native Reddit clip |
| 7 | RefMods for MiniMax H3: consistent character + voice references, running on a 6 GB GPU (free workflow) | EzkaProductions (walkthrough by AmberNova Studio) | https://www.reddit.com/r/comfyui/comments/1xnxlvv/refmods_for_minimax_h3_consistent_character_voice/ ; walkthrough https://www.youtube.com/watch?v=GHfHmrGeISM | 312 s (5:12) |
| 8 | Pruna P-H3-Image is now available in ComfyUI | crystal_alpine | https://www.reddit.com/r/comfyui/comments/1xn9ufc/pruna_ph3image_is_now_available_in_comfyui/ | native Reddit clip |

## Audits

### 1. "I Open Sourced the Digital Twin Plugin From My Unreal Fest Talk" (Third Space Interactive)

Source: https://www.youtube.com/watch?v=eQsCQ-yeNXw | 291 s | r/unrealengine post 1xo0p5n (score 22, 1 comment)

Tools used: **FragmentsUnreal** (open source, Apache 2.0, UE 5.4+); IFC to
`.frag` converter (web viewer at fragmentsunreal.dev/viewer); docs at
fragmentsunreal.dev. Built by Arkoun Merchant with co-dev Jairo over 16
months (author comment: "my own plugin built with my co-dev over 16
months").

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: build three versions of every
building at import, stream them from a server, and swap by distance, so a
whole city loads in seconds with no Nanite and no Datasmith cleanup.

### Phase 1: Convert IFC to .frag

**Do**
1. Convert IFC models to the plugin's `.frag` format (converter at
   fragmentsunreal.dev/viewer).
2. The demo models were created from scratch: a 40-floor office tower and
   the city block around it (34 models), plus a 47-building university
   campus (Carleton CIMS models) and a nine-block piece of Midtown
   Manhattan built from public data.

**Check**
- The converted model carries its IFC metadata: the frame shows a selected
  element tooltip ("Column 900x900 fireproofed h3.4B") listing Psets
  (Pset_MemberCommon, Pset_ColumnCommon, IfcClassification, IfcQuantities,
  IfcCondition).

**Why**
The plugin's unit is the IFC element with its metadata, not a baked mesh:
selection, filtering, and queries all work per element downstream.

### Phase 2: Import with three versions per building

**Do**
1. At import, build three versions of every building: every element on its
   own, merged chunks, and a light proxy for far away.
2. File reading and mesh building happen on background workers, so the game
   keeps running while a model loads.
3. Anything that repeats is stored once as an instance: one building on the
   campus has 336 of the same chair.

**Check**
- Frame-verified: the far version is a merged shell at "About 10% of the
  triangles" of the full version.
- Load-time grid (frame): the old versions load buildings in 5:19-6:44 per
  building; the new version loads them in 0:07-0:14. The first plugin
  version ever took 24 minutes for the Manhattan scene; the Unreal Fest
  version took 6 minutes for outer shells only.

**Why**
The deleted optimization (see Phase 4) gated loading on clicks; the
replacement front-loads the cost at import so runtime is a distance swap,
not a load.

### Phase 3: Stream from a server, select exactly

**Do**
1. Stream models from a remote server at runtime: nothing is cooked into the
   packaged build, models can be continuously updated, and the application
   adapts.
2. The whole 34-model block streams in about thirty seconds (author's post
   text).
3. Clicking a building selects the exact element under the cursor from any
   distance: the plugin promotes that building up level by level until it
   finds it.

**Check**
- Frame-verified UI: a "375 Park Avenue" panel with To Focus / Show only,
  a Floor Visibility slider ("Currently showing: 13-24", and in another
  frame "1-28"), and a Category Filter (All / Structural / Shell / MEP /
  Interior). Focusing a building ghosts the rest of the city.

**Why**
A digital twin is a live view of changing models, not a packaged level:
streaming plus per-element selection is the whole product.

### Phase 4: Delete the gated loading

**Do**
1. Delete the Unreal Fest optimization: back in June every building came in
   as an empty shell and you had to click it to "activate" before its
   interior would load.
2. Replace it with ungated loading (Phases 2-3): every building gets all
   three versions at import and swaps by distance.

**Check**
- The author's reason, in the post text: "That was fine for the demo, not
  so fine when I actually started user testing haha. People want as little
  friction as possible."

**Why**
A demo optimization that adds a click per building is a tax on every user;
user testing, not the stage demo, decides what stays.

### Phase 5: Drive it from Blueprint

**Do**
1. Use the plugin's API from Blueprint: floor ranges, category filters,
   metadata queries, selection — plus an editor panel for importing.
   (Frame: the docs site shows a "Blueprint flow" with a 4-step sequence
   starting "1. start import" and "batch import Fragments".)
2. Note the scope boundary (author's post text): the panel UI shown in the
   video is the author's own UI built on top of the plugin's Blueprint
   calls; it is not in the repo.

**Check**
- The repo (github.com/fragever/FragmentsUnreal) plus docs
   (fragmentsunreal.dev) are the deliverable; the demo panel is not.

**Why**
The plugin ships the API and the importer; the showcase UI is product
surface, not plugin surface.

### The human method, distilled
1. Test the demo optimization with real users before keeping it; the stage
   version is not the shipped version.
2. Pay the cost once at import (three versions, background workers) so
   runtime is a swap, not a load.
3. Instance what repeats; stream what changes; select exactly what the
   cursor points at.

**Depth status:** PARTIAL (no captions/transcript; 12 frames reviewed from
download #1, plus full description and full post text; spoken detail such as
exact worker counts is unavailable).

---

### 2. "From a raw video to a finished shot — entirely local, entirely inside ComfyUI, and all under 24 GB of VRAM" (Turbulent-Barber582)

Source: https://www.reddit.com/r/comfyui/comments/1xnm2tl/from_a_raw_video_to_a_finished_shot_entirely/ | r/comfyui post 1xnm2tl (score 51, 18 comments, 16 retrieved) | native Reddit clip

Tools used: **ComfyUI-VFX-Suite** v0.1.0-preview
(github.com/pavlovfilmdirector/ComfyUI-VFX-Suite, #OpenSourceHiggsfield
entry); **COLMAP / GLOMAP** camera tracking; custom **LTX-2.3 IC-LoRAs**;
**LTX-2.5** + layout-to-render IC-LoRAs; **FLUX.3 Klein** keyframes;
**Qwen Image Edit** relighting; **Nuke** export nodes; **Ollama** local LLM
or MCP (Claude/ChatGPT) AI Director; mobile remote control.

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: track the real camera, block the
scene in 3D, generate with layout-aware LoRAs, and let an agent run the
chain, all locally under 24 GB of VRAM.

### Phase 1: Track the camera from raw footage

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

### Phase 2: Block the scene in 3D, design keyframes

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

### Phase 3: Relight with Qwen Image Edit

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

### Phase 4: Let the AI Director run the chain

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

### Phase 5: Finish and export to Nuke

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

### The human method, distilled
1. Track first: the camera solve gates everything downstream.
2. Layout before pixels: 3D blockout + keyframes, then generation.
3. Relight deliberately: the initial frame must satisfy before generation
   runs.
4. Let the agent operate the chain; direct in plain language.
5. Ship in two weeks and let the thread find the holes (16 GB VRAM and
   handheld-phone tracking are the open ones).

**Depth status:** FULL (full post text + 16 comments with exact tool names,
failure modes, and quoted principles; native clip has no transcript to
retrieve; no generation parameters were disclosed).

---

### 3. "One month building Hiraeth" (4nf) — expansion of the 2026-11-04 audit

Source: https://www.reddit.com/r/threejs/comments/1xn2uff/one_month_building_hiraeth_a_moebiusinspired/ | r/threejs post 1xn2uff (score 436, 72 comments; 25 retrieved this run — Arctic Shift partial coverage)

This post was fully audited 2026-11-04 (skill
`hiraeth-agentic-game-dev-loop` staged). Today's re-scan adds:

- **Serendipity-map question, unanswered:** commenter twinsBuild: "the map
  of walkable ground 50m+ from anything is such a smart idea, empty space is
  the thing you never notice until a playtester gets bored. did it end up
  changing the layout a lot, or mostly where you dropped small props?" No
  author answer in the retrieved comments. This is now a standing open
  check on the skill: does the map change layout, or only prop placement?
- **Ticket-system / Claude-vs-Codex thread:** bobmefred and
  MesquiteBarbecueChip discuss forcing Codex to use a ticketing system for
  each revision, Claude Code in the desktop app doing "a lot of the heavy
  lifting," and the indie dev clinics Discord ($5/mo) as a place for
  genuine feedback. One commenter (bobmefred, software engineer): "we write
  0 lines of code... I act more like a director than a coder."
- **Author reply:** 4nf: "hahahaha, alright let me fix that 😅" (in reply
  to a playtest note).
- The core tooling is unchanged from 2026-11-04: Opus 5.5 + Astra dev,
  Midjourney refs, Tripo/Meshy/in-engine assets, Suno music, three.js +
  Unity JS-bridge builds, design audits as agent skills, serendipity map,
  visual changelog.

**Depth status:** PARTIAL (as before; skill expanded with the new comment
evidence, counts updated to score 436 / 72 comments).

---

### 4. "Infinite terrain and biome generation in Godot" (ErmanStudio)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xn1fbv/infinite_terrain_and_biome_generation_in_godot/ | r/proceduralgeneration post 1xn1fbv (score 54, 7 comments, 6 retrieved) | native Reddit clip

Tools used: **Godot** (version undisclosed). No other tools named.

Post text (verbatim, in full): "Hi! Sharing a short clip of the procedural
world generation I've been building in Godot. The world is infinite and
generated in chunks around the player, with terrain and biomes created on
the fly. It's still a work in progress. I'd love to hear what you think, and
I'm happy to answer any questions."

Comments: the only technical question — "Are you using a chunk system? I'm
struggling myself with performance with infinite terrain…" (Tasty_Extent_8613)
— went unanswered. Other comments: a fly-cam suggestion (shoxicwaste),
"Muck" comparison (avlisb), "it looks like Minecraft" (darkkrim, -10).

No chunk size, noise/erosion method, biome rules, or performance numbers
were disclosed. There is no extractable workflow.

**Depth status:** DEPTH-LIMITED (post text + thin comments only; no
parameters, no workflow). Report only, no skill.

---

### 5. "I used a Blender blockout to guide an AI-generated soda ad" (Time-Ad-7720)

Source: https://www.reddit.com/r/comfyui/comments/1xn4cq4/i_used_a_blender_blockout_to_guide_an_aigenerated/ | r/comfyui post 1xn4cq4 (score 26, 9 comments, all 9 retrieved) | native Reddit clip

Tools used: **ChatGPT + Blender MCP** (blockout); **GPT Image in ComfyUI**
(cinematic scene references); **MiniMax H3 reference-to-video** (generation).

Workflow, from the post text (verbatim): "I wanted more control over the
composition and movement in each shot, so I created a simple 3D blockout
using ChatGPT and Blender MCP. Then I made cinematic scene references with
GPT Image in ComfyUI and paired each one with its blockout clip in MiniMax
H3's reference-to-video workflow."

The core method is: block the shot in 3D with an agent driving Blender,
paint the look as a still, then let H3's reference-to-video carry both the
composition (from the blockout clip) and the look (from the reference image)
into the final shot.

Comments add three facts: the author calls these "first pass" ("Yeah it's
not perfect by any means, these were first pass"); commenter Derefringence
caught a continuity defect ("the moment the background orange pieces turn
they become a different piece of orange"); and the technique has an Unreal
variant — Lucky_Feedback9915 is "trying the same way but in unreal engine",
and the author asks "Have you tried unreal mcp with chatgpt?" No MCP
prompts, H3 steps/resolution, or GPT Image settings were disclosed.

**Depth status:** PARTIAL (workflow named, no parameters; first-pass
quality with a known continuity defect). Report only: the Blender MCP + H3
ref-to-video pattern is partially covered by existing skills
(`blender-mcp-previs-minimax-h3`, `comfyui-motion-previs-studio`), and
without parameters it cannot pass the depth-calibration gate as a
standalone skill. Noted as P2 agentic-DCC evidence (see Gap alerts).

---

### 6. "Custom Engine Forest Showcase - (130 fps average on RTX 3080 1440p)" (Novapierce_, repost of Toni Macaroni)

Source: https://www.reddit.com/r/GraphicsProgramming/comments/1xnly73/custom_engine_forest_showcase_130_fps_average_on/ | r/GraphicsProgramming post 1xnly73 (score 732, 42 comments, 25 retrieved — Arctic Shift partial coverage) | native Reddit clip; original video https://youtu.be/uR5EvBWxN14 (Toni Macaroni)

Tools used: a **handwritten custom engine** (8 months of work, "pretty much
all of it is handwritten", per the post text). No engine name, no language,
no libraries disclosed by the author. Commenter Keyframe uses
**meshoptimizer** to generate voxels for distant geometry.

Architecture, from the post text (verbatim):
- "CLODs (virtual geometry) with voxels for far representations (no
  impostors are used here)."
- "Screenspace + Voxel hybrid GI (no raytracing)."
- "Proxies without instance data for very far away representations."

Performance, from the post text (author's claims): 130 fps average at
1440p on an RTX 3080; aerial views 200 fps; dense forest 80 fps.

What CLOD means here, from commenter thats_what_she_saidk (attributed,
third-party explanation, not the author's words): "CLOD is continuous lods,
it's a technique that can be leveraged when the meshes are preprocessed for
and rendered using a meshlet pipeline. It's basically nanite in unreal
engine. Instead of swapping whole meshes as LODs which is the traditional
way, you swap parts of the mesh, or 'clusters' of triangles. So the lodding
is incremental across a whole mesh rather than swapping (and popping) the
whole thing at certain distances or pixel error thresholds. Proxies I
imagine are simply much less geometrically detailed versions of the trees,
or even larger chunks of many trees far far in the distance. Voxels: The
trees are pre-processed to generate several levels of voxels for the
foliage so at a certain distance instead of rendering the individual
triangles of the leaves. It swaps to render p..." (comment truncated at
800 characters by the fetcher).

Frames reviewed (10, from the video file downloaded 2026-11-05 05:50 during
yesterday's study of this same video; no new download this run): dense
forest edge and meadow, dappled forest floor, a stream with reeds, foggy
meadow, dark canopy interior, a hillside with a tower and mountains beyond,
an aerial valley view, and a sunlit clearing. On-screen counters in the
sampled frames show fps plus cpu/gpu milliseconds varying by view (two
legible samples: ~46.6 fps at cpu 8.49 ms / gpu 4.82 ms in fog, ~98.9 fps
at cpu 8.33 ms / gpu 7.19 ms on the hillside); the post's 130/200/80
figures are the author's claims, not frame-verified here.

Comment-thread findings (all attributed):
- **No LOD fade control.** Keyframe: "You can also see he has no control
  over LOD fade, that is - there is none. It just rolls as an edge with the
  camera."
- **AI-authorship contested.** Multiple commenters doubt the "handwritten
  in 8 months" claim: "I wanna press X for doubt on that" and "Either Toni
  is a rare genius or claude has been more involved than he wants to
  admit" (thats_what_she_saidk, graphics programmer of 25 years); "No
  technical breakdown, no explanation as to what or how the systems are or
  have been implemented. Buzzwords at the start of the showcase and
  frequent reposting around various subreddits trying to get people to
  guess what game engine it was done in" (Xylozene). Treat the 8-month
  handwritten claim as contested, not established.
- **Resource usage unanswered.** Gibgezr asked about CPU/GPU/RAM/VRAM usage
  in the YouTube comments and assumes "he's using most of the system
  resources, so not a lot left over for any 'game' beyond this on a 3080."
- **Look notes.** am314159 suggests more within-tree foliage color
  variation (light/shade, slope aspect); i-make-robots praises the forest
  floor branches and wants seasonal changes.
- **Open question:** "It says no DLSS 5 does that mean no DLSS at all or
  just not DLSS 5?" (Bingus-Chillingus, unanswered).

Directly relevant to Valkyrie: Ehsan studied this same video on 2026-11-05
as the reference for the Valkyrie forest clearing (handoff at
`~/workspace/your_files/valkyrie-forest-clearing-handoff.md`), so this
audit adds the Reddit-thread context, the architecture list, and the fps
numbers, not new technique.

**Depth status:** PARTIAL (showcase only; architecture list + commenter
explainer + 10 frames reviewed; no build steps, code, or parameters
disclosed). Report only, no skill: no extractable build workflow.

---

### 7. "RefMods for MiniMax H3: consistent character + voice references, running on a 6 GB GPU (free workflow)" (EzkaProductions; walkthrough by AmberNova Studio)

Source: https://www.reddit.com/r/comfyui/comments/1xh5vkppnnenzh1/refmods_for_minimax_h3_consistent_character_voice/ — canonical post ID `h5vkppnnenzh1` | r/comfyui post (score 146, 12 comments, unretrievable: Arctic Shift HTTP 400, PullPush HTTP 521) | walkthrough https://www.youtube.com/watch?v=GHfHmrGeISM (312 s, AmberNova Studio, no captions)

Tools used: **RefMods** (ComfyUI custom nodes, `ComfyUI-MiniMaxH3Mod` by
Luisacaotica); **MiniMax H3**; **Qwen Image 2.1** (+ Viggle Turbo low-VRAM
variant); **ComfyUI-GGUF** (low VRAM); KJNodes, rgthree-comfy,
ComfyUI-Easy-Use, Comfyroll Custom Nodes, LayerStyle, ComfyUI-Qwen-TTS
(optional, Voice Design). Workflow free at
ambernovastudio.gumroad.com/l/qitclz.

From the author's post text (in addition to the walkthrough): "You
extract a reference **once** (a character from 8 images, or a voice from a
short audio clip), save it as a reusable \u201cmod,\u201d and load it into
any future generation. No retraining, no LoRA. Just load the mod and
generate." Setup on a 6 GB VRAM laptop: "Load H3 RefMods \u2192 Apply H3
RefMod (between the I2V node and the guider)"; "Separate strengths per
slot: visual 0.9 for the character, audio 0.9 for the voice"; "Low VRAM
stack: H3 SLA Attention + Low VRAM Attention + Chunk FeedForward + Turbo
LoRA." Honest results: "Visual identity: very consistent. Same face, hair
and outfit across different scenes" and "Voice: Consistent voices from clip
to clip." Tip for two characters: "keep each character and each voice in
**separate mod files** and describe each subject clearly in the prompt (name
+ appearance + position)." Nodes to install: `git clone
https://github.com/Luisacaotica/ComfyUI-MiniMaxH3Mod`, `git clone
https://github.com/PlagueKind/ComfyUI-PlagueKind-Nodes`, `git clone
https://github.com/kijai/ComfyUI-KJNodes`.

Comment-thread findings (11 comments retrieved, all attributed): the
6 GB claim is confirmed by the author in reply ("Yes. Try the workflow" to
"So you can actually generate consistent characters and audio with 6gb
vram?"); boobkake22 challenges the premise ("You can just do this with
regular R2V. You don't need refmods for this."); Beneficial_Fish_7509 asks
whether RefMods solve the standard ref2va failure modes ("sometimes the
character doesn't have the same voice as reference" and babbling "when
there is supposed to be silence") — unanswered; look_a_dragon asks how
long generation takes and how long the clips are — unanswered; xivurs wants
FastH3 support; seppe0815 dismisses the look ("allways the minimax a.i
slop look").

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: bake face and voice into reusable
RefMod files once (no LoRA training), then generate clips with them on a
6 GB card.

### Phase 1: Build the reference dataset from scratch (Qwen Image 2.1)

**Do**
1. If no reference images of the character exist, create the dataset with
   Qwen Image 2.1 (description text: "I also show you how to create a
   complete dataset from scratch using Qwen Image 2.1").
2. Drive the dataset prompts with a CR Prompt List node (frame-verified, 8
   prompts): close-up portrait of the face, straight-on front view, neutral
   relaxed expression, direct eye contact, face filling most of the frame,
   soft even lighting; close-up of the face turned 45 degrees toward the
   left side of the frame, three-quarter view; the same turned 45 degrees
   toward the right; waist-up shot, front view, arms relaxed at the sides,
   direct gaze; full-body shot, frontal view, relaxed A-pose with arms
   slightly away from the torso and feet shoulder-width apart, head level,
   direct eye contact, even soft lighting; full-body shot turned 45 degrees
   toward the right side, three-quarter view, natural stance; full-body rear
   three-quarter view, glancing back over the shoulder at the camera, soft
   rim light.
3. Append the identity lock to every prompt (frame-verified, truncated in
   frame): "Same person as in <image 1>: identical face, hairstyle, skin
   tone, age, outfit and body proportions, same visual style and ima..."
4. Node settings (frame-verified): start_index 0, max_rows 8.

**Check**
- The picker grid shows 8 photos of the same character ("Amb (1)" through
  "Amb (8)"); one is selected and the button reads "USE IT IN A
  GENERATION". The intro frame reads "Reference images 5/8".

**Why**
Eight angles with a locked identity sentence is the dataset: the RefMod
bakes identity from coverage, not from one hero shot.

### Phase 2: Bake the person RefMod

**Do**
1. Feed the references into the "Create / person reference" node
   (frame-verified inputs: ref_image_0, ref_video_0, refs_bundle, mask,
   av_encoder, vae, mask_list).
2. Set (frame-verified): name "Amber", mode "Full Reference", concept_type
   "identity", background_retention 0.00, ref_resolution 1024, pool_h 16,
   pool_w 16, latent_frames 16, Refinement Steps 0, merge "stack",
   motion_only "full".
3. Save with a filename prefix and subfolder; version with _v1, _v2, etc.
   (frame note: "Filename comes from... Keep name + folder... Use _v1,
   _v2, etc.").

**Check**
- The saved RefMod loads as one file in the generation workflow; there is
  no per-generation retraining step.

**Why**
Identity lives in the file: "It stores references instead of training a
LoRA, so you can go from a few photos to a finished clip in a single
session" (description text).

### Phase 3: Bake the voice RefMod

**Do**
1. Upload a clean audio sample (frame-verified: "Amber.wav", 0:09) in the
   Audio Mod upload node; the H3 Audio VAE is already selected
   (minimax_h3_audio_vae_fp32.safetensors).
2. Set in "Create / audio reference" (frame-verified): name "Amber",
   max_seconds 30.0, max_tokens 5120, budget_policy "error", concept_type
   "voice"; write a description.
3. Note the node's own caveat (frame-verified): "Use a clean audio sample,
   30sec max for voice... music, sound effects or speech references.
   Speaker identity transfer is not validated."

**Check**
- Voice is a separate RefMod from face: same name ("Amber"), different
  concept_type ("voice" vs "identity").

**Why**
Face and voice are independent references; a character that looks right
but sounds wrong fails the same way a wrong face does.

### Phase 4: Generate on 6 GB VRAM (low-VRAM section)

**Do**
1. Use the workflow's dedicated low-VRAM section with the 6 GB models:
   MiniMax H3 fused turbo int8 (MATLOWAI), Qwen Image 2.1 Viggle Turbo,
   and the hybrid ref2va model (smhfacct
   Minimax-H3-fl2va-ref2va-hybrid-models).
2. Set the attention stack (frame-verified): Model Attention Backend
   "comfy_kitchen attention" feeding MiniMax H3 Low VRAM Attention
   (head_chunks 4) and MiniMax H3 Chunk FeedForward (chunks 2,
   seq_threshold 4096); H3 SLA Attention with sparsity_ratio 0.90,
   block_size 64, min_seq_len 8192, dense_last_steps 0, protect_audio
   "protect", enabled "sparse", dense_steps 1, dense_backend
   "comfy_kitchen", disable_fp16_accum "disabled (recommended)",
   stabilize_motion "off", Protect Image/Video Reference "Off",
   tail_correction "off", use_int8_qk "on (experimental)".
3. Load the Video Generation models (frame-verified): unet
   "minimax_h3_hybrid_fl2va_ref2va_825-40-int8.safetensors", clip
   "qwen3vl_32b_minimax_fp8_e4m3fn.safetensors", vae
   "minimax_h3_video_vae_fp8.safetensors", vae_1
   "minimax_h3_audio_vae_fp32.safetensors"; Model Preview Override
   max_resolution 1024, preview_quality 80, suppress_default_preview true,
   preview_fps 12, tiny_vae "taeh3.safetensors".

**Check**
- The workflow has two dedicated video-generation sections; one is built
  specifically for low-VRAM GPUs (6 GB) "with dedicated models that fit
  properly on this kind of graphics card" (description text).

**Why**
Sparse attention + chunked feedforward + int8 weights is what fits H3 on
6 GB; the recipe is the low-VRAM section, not a smaller prompt.

### Phase 5: Apply the RefMods and sample

**Do**
1. In "Apply H3 RefMod" (frame-verified): Characters/Amber 1.00, retention
   0.85, curve_direction "constant", scramble_seed 1291797728,
   control_after_generate "randomize", curve_shape "linear", curve_value
   1.00, graph_preset "(none)", scramble_mode "shuffle", scramble_keep 1,
   max_total_tokens 0; audio/Amber 1.00.
2. Sample with sampler_name "res_multistep", scheduler "simple", steps 8.
3. Create Video at fps 24, bit_depth auto, color_space sRGB.
4. Starting guidance from the workflow's own note (frame-verified): "Start
   with strength 2.0 and version 1."

**Check**
- The generated frames keep the same face across scenes (Babylon street,
  Amalfi-coast terrace) and the same voice reference throughout.

**Why**
Retention 0.85 with a constant curve is the identity hold: the RefMod
steers every step, and the strength-2.0 starting point is the author's
calibrated default.

### The human method, distilled
1. Bake identity once (face + voice, separate files), prompt scenes forever.
2. Eight angles make the dataset; one angle does not.
3. Fit the model to the card: int8 + sparse attention + chunked feedforward
   is the 6 GB recipe, not a quality compromise to apologize for.
4. Start at strength 2.0, version 1; change one thing at a time.

**Depth status:** FULL (frame-verified parameters from 12 reviewed frames;
no transcript/captions, so spoken narration is unavailable). Variant of the
existing `minimax-h3-refmod-identity-comfyui` skill (image-only, 2026-10-16
post): this one is video + voice + 6 GB low-VRAM, a different workflow, so
it becomes variant skill `minimax-h3-refmod-voice-lowvram`.

---

### 8. "Pruna P-H3-Image is now available in ComfyUI" (crystal_alpine)

Source: https://www.reddit.com/r/comfyui/comments/1xn9ufc/pruna_ph3image_is_now_available_in_comfyui/ | r/comfyui post 1xn9ufc (score 99, 13 comments, 12 retrieved) | native Reddit clip

Tools used: **Pruna P-H3-Image** (distilled image model built on MiniMax H3,
paired with a 4B text encoder); official ComfyUI workflow templates
(`image_p_h3_image_edit.json`, `image_p_h3_t2i.json` in
Comfy-Org/workflow_templates); models at Hugging Face
PrunaAI/p-h3-image-comfy.

This audit reconstructs the exact workflow from the post, the official
workflow templates, and the comment thread, step by step, so another agent
can follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: distill H3 down to an int8 image model with a
small text encoder, and let a prompt upsampler plus an 8-step distilled
schedule do the work the big model used to do.

### Phase 1: Install the models (35.31 GB total)

**Do**
1. Update ComfyUI first (the template notes Desktop/Cloud updates follow
   stable releases, so nightly-supported models may not be available there).
2. Place the files (template's own storage map):
   - `diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors`
     (19.53 GB, from Comfy-Org/MiniMax-H3)
   - `text_encoders/p-h3-image_text_encoder_int8_convrot.safetensors`
     (4.77 GB) and
     `text_encoders/p-h3-image_prompt_upsampler_w4a8.safetensors` (6.26 GB)
   - `vae/p-h3-image_vae_int8_convrot.safetensors` (2.93 GB)
   - `loras/p-h3-image_lora_bf16.safetensors` (1.82 GB)
3. Load the official template for the job: `image_p_h3_image_edit.json`
   (image edit) or `image_p_h3_t2i.json` (text to image).

**Check**
- Total on disk: 35.31 GB. The "lighter and faster" claim is relative to
  full H3, not absolute: the diffusion model alone is 19.53 GB.

**Why**
The whole workflow is int8/w4a8-quantized except the bf16 LoRA: the size
saving is the product, and the template's file map is the install contract.

### Phase 2: Write the prompt as aspect ratio + one request

**Do**
1. Write the prompt in the template's format: `Aspect ratio: <ratio>` on
   one line, then `Request: <what to change>` (edit) or the request after
   `Request:` in the prompt box (text to image). The prompt upsampler
   expands it before sampling (TextGenerateV2, 1536 tokens).
2. Keep the request to one short sentence: "The model keeps the
   composition when the request is one short sentence" (template note).
3. Keep the `Aspect ratio:` line in sync with the Resolution Selector:
   "otherwise the prompt asks for one shape and the latent produces
   another" (template note).

**Check**
- Sizes at 8.0 MP, multiple 32 (template table): 1:1 Square 2912x2912;
  4:3 Standard 3360x2496; 3:2 Photo 3552x2368; 16:9 Widescreen 3872x2176;
  3:4 Portrait Standard 2496x3360; 2:3 Portrait Photo 2368x3552; 9:16
  Portrait Widescreen 2176x3872. Width and height 0 give 2912x2912.
- For image edit, the source image goes into `Load Image` and the result
  matches its shape, so width/height on the conditioning follow the image
  automatically.

**Why**
The upsampler does the prompt engineering; the human's job is a short,
shape-consistent request. Shape disagreement between prompt and latent is
the documented failure mode.

### Phase 3: Sample the 8-step distilled schedule

**Do**
1. Sample with the template's fixed schedule: `ManualSigmas` 9 values
   ("1.0, 0.984753, 0.967905, 0.951688, 0.925372, 0.881923, 0.810083,
   0.528718, 0.0") with sampler `er_sde`, CFG 1, MiniMaxH3SigmaShift [1, 1].
2. Load the LoRA (`p-h3-image_lora_bf16.safetensors`) at strength 1.
3. Set seed control to `randomize` for new images, back to `fixed` to
   reproduce the shipped example.

**Check**
- "Sampling is an 8-step distilled schedule (`ManualSigmas` + `er_sde`,
  CFG 1) — more steps do not help" (template note). Do not raise the step
  count expecting quality gains.

**Why**
Distillation bakes the quality into 8 steps; the schedule is the model,
not a tuning knob.

### The human method, distilled
1. Quantize everything, then let the upsampler carry the prompt.
2. One short request, one shape: aspect ratio and latent must agree.
3. Eight steps is the schedule: more steps do not help.

Comment-thread findings (all attributed):
- **Consistency claim (single user, unverified):** Affectionate_Rub9491,
  a non-technical user whose favorite had been Qwen 2.1: "This one simply
  BLOWS it out of the water with realism and consistency... When I edit an
  image of me to have different facial expressions, it doesnt give me
  horror like other models. It actually gives me an image that looks like
  a real picture of me doing that expression, in 90% of generations."
- **VAE quality caveat:** fallengt: "VAE isn't built for images; the model
  automatically compresses picture quality. Even at 8 megapixels, we get
  pixelated texture" (with a sample image). The image-first VAE question
  is open.
- **RefMod compatibility:** edisson75: "Just in case, it works with refmods
  too" (with a sample image, +14); the apply-refmod node goes "between the
  conditioning output and the input of the guider."
- **Training support:** imlo2: "Ostris just posted to X about having added
  P-H3-Image training support to AI-Toolkit."
- **CLIP-size cost concern:** TurbTastic: lighter and "significantly...
  more forgiving for low/medium GPUs", but "reducing the CLIP model size
  that much is going to come at a significant cost."
- **Open question:** jd3k: "What is the point if you can do the same with
  minimax?" — the distilled model's advantage (lighter/faster) vs the
  quality cost is the thread's unresolved debate.

**Depth status:** FULL (full post text + 12 comments + both official
workflow templates read node-by-node with exact filenames, sizes, sigmas,
and prompt format; no video transcript exists for a native clip, but the
workflow is fully specified by the templates).

---

## Tooling extracted per video (with source evidence)

| Tool / stage | Found in | Source evidence |
|---|---|---|
| FragmentsUnreal BIM streaming (IFC→.frag, 3-LOD import, background workers, instancing, remote streaming, Blueprint API) | 1 | Video description + full post text + 12 frames (far shell "About 10% of the triangles"; load grid 0:07-0:14 vs 5:19-6:44) |
| ComfyUI-VFX-Suite (COLMAP/GLOMAP tracking, LTX IC-LoRA, FLUX.3 Klein, Qwen Image Edit relight, MCP AI Director, Nuke export) | 2 | Full post text + 16 comments (author: "automatically reads the studio instructions and toolset...") |
| Hiraeth agentic loop (design-audit agent skills, serendipity map, visual changelog) | 3 | Full post text + 25 comments (twinsBuild serendipity-map question; ticket-system thread) |
| Godot infinite terrain (chunk system, biomes on the fly) | 4 | Post text + 6 comments (chunk-system question unanswered) |
| Blender MCP blockout → GPT Image refs → MiniMax H3 ref-to-video | 5 | Full post text + 9 comments (first-pass quality, orange-piece continuity defect, Unreal MCP variant) |
| Custom-engine forest (CLOD virtual geometry + voxel far field; 130/200/80 fps claims) | 6 | Full post text (architecture list) + 25 comments (CLOD explainer, no LOD fade, contested authorship) + 10 frames |
| RefMods video + voice (H3 SLA Attention, int8 6 GB recipe, Qwen Image 2.1 dataset) | 7 | Full post text (0.9/0.9 strengths, node placement, PlagueKind nodes) + 11 comments + video description + 12 frames (exact node names, parameters, model filenames) |
| Pruna P-H3-Image (distilled H3 image model, 4B text encoder) | 8 | Full post text + 12 comments + both official workflow templates read node-by-node (exact models, sizes, 8-step sigmas, prompt format) |

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| FragmentsUnreal 3-LOD-at-import + distance swap (far shell ~10% tris) | 1 | PARTIAL | Aegis HAVE LOD generation (`runtime/lods`) and UE packaging (`ue/`); no runtime streaming import, no distance-swap loader, no background-worker import | backlog — the import-time multi-LOD pattern transfers to foundry output; the BIM/IFC part does not |
| FragmentsUnreal per-element metadata query + exact-click selection | 1 | NEED | No in-engine metadata query/selection stage in the foundry inventory | backlog — pattern only; game assets are not IFC elements, but exact-click selection is review-tooling relevant |
| ComfyUI-VFX-Suite local AI-video studio (tracking + IC-LoRA + Nuke export) | 2 | NEED | No video/AI-video stage in Aegis; trailer bucket only | watchlist — revisit when Aegis needs a trailer |
| MCP AI Director (VFX Suite) + Blender MCP blockout | 2, 5 | PARTIAL | P2 MCP-driven DCC gap is open; prior art in `agentic-blender-asset-pipeline` skill; today adds two new data points | backlog — strengthens the P2 spike case (Blender MCP behind review stage) |
| RefMods identity/voice consistency (baked file, scored reuse) | 7 | PARTIAL | P1 acceptance-spec gap is open; RefMod is adjacent evidence (identity consistency as a scored file), not a spec | backlog — feed into the acceptance-spec fix design |
| Pruna P-H3-Image (lighter/faster H3 image model, fully specified: 35.31 GB, 8-step schedule) | 8 | NEED | No image-gen model choice in the intake; model-swappable by design | watchlist — a lighter H3-class image model is an intake option if image gen enters the foundry; workflow is fully specified, not a rumor |
| Custom-engine forest CLOD + voxel far field | 6 | PARTIAL | Aegis HAVE LOD generation; no CLOD/virtual-geometry or voxel far-field stage | watchlist — pattern for large scenes; the UE client (Aetheria) is a separate repo, not audited |
| Godot infinite terrain chunk system | 4 | NEED | Not applicable (UE/Rust stack; no infinite terrain need) | skip |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| RefMods 8-photo dataset recipe (CR Prompt List, 8 angles, identity-lock sentence) | 7 | NEED | 2d3d has an AI image client + install/acceptance gates, but no identity-consistency mechanism for character sprite sets | backlog — directly reusable for character sprite sets; test on one character |
| Blender MCP blockout (agent-driven 3D blockout) | 5 | PARTIAL | 2d3d has projection painting + reference reconstruction; no MCP-driven Blender step | watchlist — automation upgrade to the art pipeline |
| Pruna P-H3-Image (edit + text-to-image templates, exact models/sizes/sigmas) | 8 | NEED | Image client is model-swappable in principle; no H3-class model in use | watchlist — fully specified local image-edit path (35.31 GB); VAE pixelation caveat at 8 MP is open |
| FragmentsUnreal BIM streaming | 1 | NEED | UE-only; 2d3d is Godot | skip |
| Godot infinite terrain chunk system | 4 | NEED | 2d3d is fixed-level side-scroller; no infinite terrain need | skip — chunk-around-player pattern noted only |
| Custom-engine forest CLOD | 6 | NEED | 2d3d's look is 2D-to-3D pixel art; no dense 3D forest need | skip |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Godot infinite terrain chunk system | 4 | PARTIAL | Desktop City HAVE procedural authoring (`tools/procedural_art.py`, `city_*`, `procgen_*` probes); no infinite chunk streaming | watchlist — city is bounded, not infinite; chunk pattern is reference only |
| Custom-engine forest CLOD + voxel far field | 6 | PARTIAL | Desktop City HAVE own trees (`city_trees.py`); no CLOD/virtual-geometry far field | watchlist — perf pattern for dense vegetation at city scale |
| Blender MCP blockout | 5 | PARTIAL | Desktop City HAVE `tools/blockout.py`; no MCP-driven blockout | backlog — automation upgrade to an existing stage |
| FragmentsUnreal BIM streaming | 1 | NEED | UE-only; Desktop City is Godot | skip |
| RefMods / Pruna / VFX Suite | 7, 8, 2 | NEED | No AI-video or character-identity work in Desktop City | skip |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| FragmentsUnreal 3-LOD pattern | 1 | HAVE | Solarempire HAVE LOD0-LOD3 GLBs + HLOD proxy per asset | — (pattern already present; BIM/IFC part not applicable) |
| Blender MCP loop (agents drive Blender stages) | 5 | PARTIAL | Solarempire pipeline is Blender-stage based (audit→prepare→segment→retopo→...); no MCP-driven loop | backlog — P2-adjacent for its Blender pipeline |
| Godot infinite terrain | 4 | NEED | Space game; no terrain chunking need | skip |
| RefMods / Pruna / VFX Suite / forest CLOD | 7, 8, 2, 6 | NEED | No AI-video, character-identity, or dense-forest stage | skip |

## Watchlist trending

Genuine reappearances (from `bin/trend_watchlist.py`, corrected for
auto-match false positives; the full corrected list lives in
`references/tooling-watchlist.md`):

- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-03, 2026-10-05, 2026-10-08, 2026-10-09, 2026-10-11, 2026-10-16, 2026-10-23, 2026-10-24, 2026-10-27, 2026-10-28, 2026-10-29, 2026-11-01, 2026-11-03, 2026-11-04, 2026-11-05) **TRENDING**
- MCP servers driving Blender/Unreal (agentic DCC) (first seen 2026-09-27, status BACKLOGGED; seen again 2026-09-28, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-30, 2026-11-01, 2026-11-05) **TRENDING**
- RefMod (ComfyUI custom nodes, character identity without LoRA training) (first seen 2026-10-16, status BACKLOGGED; seen again 2026-10-21, 2026-10-29, 2026-11-03, 2026-11-05) **TRENDING**
- FLUX 3 Image Klein (5.6B, Black Forest Labs, native ComfyUI) (first seen 2026-10-16, status WATCH; seen again 2026-10-17, 2026-10-21, 2026-10-22, 2026-10-28, 2026-10-29, 2026-11-03, 2026-11-05) **TRENDING**
- Qwen Image Edit 2.1 in AI-video pipelines (first seen 2026-10-23, status WATCH; seen again 2026-10-24, 2026-10-28, 2026-10-29, 2026-11-05) **TRENDING**
- MiniMax H3 Reference-to-Video character swap + motion transfer (ComfyUI, local RTX 5070 Ti) (first seen 2026-10-24, status WATCH; seen again 2026-10-29, 2026-10-31, 2026-11-03, 2026-11-04, 2026-11-05) **TRENDING** [2026-11-05: H3 reference-to-video mode genuinely reappears (soda ad pairs blockout clips with GPT Image refs in H3 ref-to-video), but for scene/composition generation, not the character-swap workflow this row tracks]

Auto-match false positives corrected in the watchlist file (token overlap,
not genuine reappearances; each carries a bracketed note in the file):
Nano Banana-class image edit; Codex CLI driving Blender via MCP; Tripo
Smart Mesh P2.0; GPT Astra mesh-split workflow; Godot 4.5 .NET procedural
creature pipeline; Flux klein 9B/4B; SelfLift; MiniMax H3 no-masking
character-swap LoRA; Orogen + Infinite Diffusion; Pixaroma FLUX 3 Klein
pack; SyncTile; MiniMax H3 Chain Director; 2x2 storyboard-grid; Automated
AI documentary pipeline; MiniMax H3 native 3MP low-VRAM; MiniMax H3 Face
Refiner; MiniMax H3 toy-to-real; ComfyUI-ldoi; Terrain3D v1.1.0; IV Studio;
devdef ComfyUI video app; MIDI fingering; Reshoot 4D. Four of the
Hiraeth-linked ones are the same post re-scanned in the overlapping window,
already audited 2026-11-04, not new mentions.

New watchlist additions (append-only, 2026-11-05):
- FragmentsUnreal (open-source BIM/IFC streaming plugin for UE5, Apache 2.0)
- ComfyUI-VFX-Suite (local VFX studio inside ComfyUI, v0.1.0-preview)
- Pruna P-H3-Image (distilled MiniMax H3 image model + 4B text encoder)
- Custom-engine forest: CLOD virtual geometry + voxel far field (Toni Macaroni)
- meshoptimizer voxel generation for distant geometry (commenter Keyframe, forest thread: 'i use meshoptimizer to generate voxels for distant crap')

## Gap recommendations (highest-leverage NEEDs)

1. **Spike Blender MCP behind the Aegis review stage (P2).** Two
   independent data points today (soda-ad blockout via ChatGPT + Blender
   MCP; VFX Suite AI Director over MCP) show agents driving DCC-adjacent
   tools in production use. Next step: the P2 prescription stands — a
   small spike with a human-approved loop, reusing the
   `agentic-blender-asset-pipeline` skill as prior art.
2. **Test the RefMods 8-photo dataset recipe on a 2d3d character.** The CR
   Prompt List 8-angle recipe with an identity-lock sentence is the most
   directly reusable artifact today: 2d3d's sprite pipeline has no
   identity-consistency mechanism. Next step: one character, 8 prompts,
   measure identity hold across the sprite set before adopting.
3. **Adopt the import-time multi-LOD pattern for Aegis foundry output.**
   FragmentsUnreal builds all three LODs at import and swaps by distance
   (far shell ~10% tris) with background workers; Aegis already generates
   LODs but has no distance-swap loader. Next step: backlog as a
   foundry-output option; the BIM/IFC part stays out of scope.
4. **Keep the ComfyUI-VFX-Suite tracking + relight pipeline on watch for
   Aegis trailers.** COLMAP/Glomap camera tracks plus LTX IC-LoRA
   generation plus Nuke export is the first end-to-end local trailer
   pipeline seen with a stated failure mode and fix. Next step: none until
   Aegis needs a trailer; the 16 GB VRAM question is open.
5. **Forest CLOD + voxel far-field stays Valkyrie-relevant, not a repo
   gap.** The showcase corroborates the Valkyrie forest-clearing direction
   with fps numbers (130 avg / 200 aerial / 80 dense, author claims) but
   discloses no build steps. Next step: none in the scout; the existing
   Valkyrie handoff carries it.

## Explicit non-goals

- SPH black hole sim (r/Simulated, "Earth torn apart by tidal forces", 1M
  particles live on GPU, 34 comments) — ranked 9th, outside the 8-video
  cap; sim-engine pattern, no repo attach point. Not analyzed.
- Falling-sand Godot C# sync (r/godot post 1xo9f3r, 60 Hz pixel physics in
  plain C# outside Godot, host-run world sim sending compressed terrain
  updates so craters and liquids stay in sync, 4-player co-op, game Nine
  Lives Below on Steam, demo in about a week) — ranked 13th; author: C#
  handles this processing 'a lot quicker' than GDScript and 'this type of
  game just wouldn't work out on the multiplayer side' in GDScript.
  Notable for Valkyrie's Godot C# stack (plain-C# sim library is the same
  architecture Valkyrie locked on 2026-11-04), candidate for a later run.
- Realtime pathtracing 47 MP across 50 product assets (rank 11) and the
  ComfyUI ND UI Builder (rank 12) — below the cap, not analyzed.
- YouTube channel scan — source down (bot-check wall on all 11 channels);
  Reddit only this run. Unity subreddit posts missing (HTTP 521).

## Depth-escalation usage

- Mode: `pre-approved`, max 2 media downloads. Downloads attempted: 2,
  succeeded: 2, skipped: 0, approval gates hit: 0.
  - #1: BIM video (eQsCQ-yeNXw) — captions unavailable (transcript source
    "none"), so the download was used; 12 frames extracted and reviewed.
    The video-summarizer `yt_download.py` shim failed (its venv has no
    `python3` binary), so the download ran with the working venv's yt-dlp
    (`~/workspace/skills/video-summarizer/.venv/bin/yt-dlp`) using the same
    arguments (android player client, ≤720p). No approval gate involved.
  - #2: RefMods walkthrough (GHfHmrGeISM) — captions unavailable, download
    used; 12 frames extracted and reviewed.
  - Forest video: no new download; reused the 2026-11-05 05:50 download +
    10 frames from yesterday's study of the same video.
- Whisper transcription was not attempted (sandbox cannot complete the
  model download; per the skill, that is a local-machine step).

## skill_library artifacts staged

- New skill `fragmentsunreal-bim-streaming-ue5` (`skills/engine-runtime/`)
- New skill `comfyui-vfx-suite-local-studio` (`skills/ai-video/`)
- New variant skill `minimax-h3-refmod-voice-lowvram` (`skills/characters/`)
- New skill `pruna-p-h3-image-comfyui` (`skills/ai-video/`)
- Expanded skill `hiraeth-agentic-game-dev-loop` (`skills/automation/`,
  new comment evidence, counts updated)
- Report-only (no skill): Godot infinite terrain, Blender blockout soda ad,
  Custom Engine Forest Showcase (DEPTH-LIMITED/PARTIAL, no extractable
  executable workflow or no parameters)
- Full report published to `docs/scout-reports/have-vs-need-2026-11-05.md`;
  watchlist rows synced to the repo mirror
  `video-tooling-scout/references/tooling-watchlist.md`; README tables
  updated (skill count + category counts, no chronological prose).
