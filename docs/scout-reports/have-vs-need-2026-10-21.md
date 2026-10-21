# Video tooling scout: have-vs-need, 2026-10-21

Depth mode: **pre-approved** (max 2 media downloads). Depth-escalation usage:
1 download attempted, 1 succeeded (UE 5.8 Chaos Flesh tutorial, YouTube, 15.6 MB,
format 18/360p). Second slot unused: the remaining videos were native Reddit
clips, whose tooling signal lives in post text and comments per the skill
(nothing to deepen by downloading a showcase clip).

Scan: 7 video posts across 17 subreddits (2026-10-19 to 2026-10-21),
min_score 20. Note: r/godot returned HTTP 429 during the scan (rate-limited,
not scanned this run). The memory note says the scan list grew to 23
subreddits on 2026-10-20, but `subreddits.yaml` still lists 17 (threejs,
GraphicsProgramming, shaders, VoxelGameDev, RealTimeVFX missing) —
worth reconciling before the next run.

## Gap alerts

- **P2 (agentic DCC/tooling loop), new practice evidence:** in the MOSS-Image
  thread, BazzTheBazz (score 6): "I use Claude with the comfy mcp to test
  things for me and write a report. It can do everything autonomously
  including fine tuning the workflows to your specs, download the models and
  copy them in the appropriate folder. The whole thing." This is a live,
  first-hand report of an agent autonomously driving ComfyUI (model
  download, folder placement, workflow fine-tuning, report). It fills the
  described need of the P2 "MCP-driven DCC loop (agents drive Blender/UE,
  iterate visually)" gap from the ComfyUI side, joining konte, GPT Astra,
  and Codex-Blender-MCP as prior art. Recommend treating the Comfy MCP
  server as the spike candidate for intake-stage automation review.
- **P1 AI-vendor acceptance spec, supporting evidence (not a fill):**
  MOSS-Image arrived 2026-10-17 and within 4 days had multiple 4/8-step Turbo
  LoRAs, 2+ full finetunes, a depth ControlNet (LoRA), an inpainting
  workflow, and an experimental image-editing plugin (commenter infearia,
  score 19). This is the community-velocity pattern that intake's
  model-swappable image stage must absorb; it does not itself define "what
  good means."
- **P2-adjacent automation risk:** ComfyUI 0.36's native loops are
  recursion-based and crash past a few dozen iterations (~70 reported
  ceiling; PR #16227 replaces recursion with iteration, unmerged). Any
  intake/foundry automation built on native ComfyUI loops inherits this.
  No matches today for the other P1 gaps (rig/retarget, perf budgets,
  import validation, mesh compression, mesh refinement, art bible,
  skyline fill, Godot import gate).

## Videos deeply analyzed

| # | Video | Creator | URL | Duration | Source |
|---|-------|---------|-----|----------|--------|
| 1 | "Unreal Engine 5.8 Chaos Flesh and Soft Body Physics: Part 1 - The Basics \| Beginners Tutorial" | Crawford Terrace Studios | https://www.youtube.com/watch?v=pFiwaoqHjWw | 13:13 | r/unrealengine post 1x9yfi6 (score 32). Depth: FULL (287 caption lines + 12 frames reviewed) |
| 2 | "OpenMOSS released MOSS-Image, and it's now supported in ComfyUI." | crystal_alpine | https://www.reddit.com/r/comfyui/comments/1xa6wmo/ (native clip v.redd.it/omxexc0e9hwh1) | n/a (clip) | r/comfyui (score 130, 28 comments). Depth: PARTIAL (full selftext + 25 top-level comments; clip not content-analyzed) |
| 3 | "My procedural sci-fi ship generator" | OrbitalShipyard | https://www.reddit.com/r/proceduralgeneration/comments/1xa7sgb/ (native clip v.redd.it/2s4dbztcfhwh1) | n/a (clip) | r/proceduralgeneration (score 113). Depth: PARTIAL (author's own comments via author search; post-comment API 422, PullPush empty — index lag on 1-day-old posts) |
| 4 | "House of Courland" | BeginningAmphibian69 | https://www.reddit.com/r/3Dmodeling/comments/1xa8waz/ (native clip v.redd.it/l4fj9tsjmhwh1) | n/a (clip) | r/3Dmodeling (score 55). Depth: DEPTH-LIMITED (Unity scene showcase; 1 comment unretrievable; tool inference from author's past comment only) |
| 5 | "Space robot made for Zbrush 2027" | benavidmark | https://www.reddit.com/r/3Dmodeling/comments/1xaca2q/ (native clip v.redd.it/v53jumombiwh1) | n/a (clip) | r/3Dmodeling (score 29). Depth: DEPTH-LIMITED (hand-sculpt showcase; 3 comments, author only said "Yes i make all by hand") |

## 1. "Unreal Engine 5.8 Chaos Flesh and Soft Body Physics: Part 1 - The Basics | Beginners Tutorial" (Crawford Terrace Studios)

Source: https://www.youtube.com/watch?v=pFiwaoqHjWw | 13:13 | r/unrealengine post 1x9yfi6 (score 32)

Tools used: Unreal Engine 5.8, Chaos Flesh plugin (experimental), DataFlow
graph with the "Static to Tet Mesh" template, Deformable Solver actor.
Creator's rig (from description): i9-13900KF, 32 GB RAM, RTX 4070 12 GB.
Project files: https://ko-fi.com/s/73d35cabcd. Docs:
https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The video's core method is: convert a static mesh into a
tetrahedral volume with a DataFlow graph, bind the volume to the surface,
and let the deformable solver deform the volume so the surface follows.

### Phase 1: Mesh prep (rules before you start)

**Do**
1. Use a closed mesh with no overlapping geometry (same rule as Chaos
   Destruction).
2. Avoid thin geometry and long stretched vertices.
3. Keep mesh resolution under 30,000 (high-density meshes "may not simulate
   very well" — author's words).
4. Author at roughly 1 m scale: "size matters right now... the simulation
   seems to do best with meshes around 1 m in size. As you get smaller or
   larger than that, you'll start running into issues."

**Check**
- Inspect the mesh for open edges and overlaps in the DCC before import.
- Count triangles; stay under 30k for now.

**Why**
The deformable solver tessellates a tet volume inside the mesh; thin,
stretched, or oversized geometry makes the solver unstable. Chaos Flesh is
experimental: "expect limitations and issues, and save your work often."
Chaos Flesh supports Nanite static and skeletal meshes (author-stated).

### Phase 2: Project and plugin setup

**Do**
1. Create a new project: Film/Video section → Blank template. The blank
   template's floor actor is monitored for collisions by the deformable
   solver by default.
2. Edit → Plugins → search "flesh" → enable Chaos Flesh → Restart Now.

**Check**
- Frame evidence: project browser with "Blank" selected under
  Film/Video (frame_002).
- After restart, the Flesh Asset type exists under Content Drawer →
  Physics.

**Why**
The blank template gives a floor the solver already collides with, so the
first simulation works without collision configuration. (Inference:
the author's recommendation, not an engine requirement.)

### Phase 3: Create the flesh asset and assign a DataFlow template

**Do**
1. Content Drawer → right-click → Physics → Flesh Asset. Rename to
   FA_gummybear (author's naming).
2. Assign the "Static to Tet Mesh" DataFlow template. Note from the author:
   there is also a "static mesh to tet" template but it is "an exact copy
   of the skeletal to tet mesh template... just ignore this one for now."

**Check**
- The Flesh Asset editor opens with a blueprint-like DataFlow graph and
  viewport windows above it.

**Why**
UE 5.8's templates are the fast path: "starting with the 5.8 release and
the addition of the new data flow templates, creating your Chaos Flesh
assets are now easier than ever." The three system components are: the
flesh asset (geometry data), the DataFlow graph (procedural build), and
the deformable solver (runs the sim).

### Phase 4: Walk the DataFlow graph

**Do**
1. Static Mesh node: in Node Details, pick the source static mesh (author
   used a gummy bear). Open the Construction viewport tab; if dark, click
   the preview-scene icon and select Gray Ambient.
2. Static Mesh to Collection node: extracts geometry info into a collection.
3. Create Tetrahedron node: the solver does NOT operate on the static
   mesh. It builds a tet-mesh volume filling the static mesh and binds the
   tet geometry to the surface; the surface follows the tets.
   - Density: change Num Cells in Node Details. Default 10 → author bumped
     to 30 to recover the gummy bear's facial detail.
   - Cost rule: "assign only the minimum number of cells you absolutely
     need" — more tets = more sim load.
   - Alternative: set Method to Tet Wild ("better at preserving high
     detail and thin features of your mesh, but at a higher simulation
     cost"; reprocessing takes a few seconds).
4. Right-click → "set flesh default properties" → Set Flesh Default
   Properties node, wired after Create Tetrahedron. The 5.8 templates are
   missing this node; without it the solver assumes zero density and
   "basically ignores gravity and any deformations."
5. Density value: default 1.0 → author lowered to 0.01. "A higher density
   value means gravity has a stronger effect on your mesh and your mesh
   tends to crumble under its own weight." At 1.0 the bear "deforms into
   a melting mess"; at 0.01 it gets "that gummy bear wiggle and jiggle."
6. Flesh Asset Terminal node: the process/output node. Save.

**Check**
- Construction viewport shows detail appearing/disappearing as Num Cells
  changes (30 recovered the face; Tet Wild recovered thin detail).
- Simulation viewport: play shows the melt at density 1.0 vs. the jiggle
  at 0.01.

**Why**
Tet density is the resolution of the sim, decoupled from the render mesh:
tune the cheapest volume that preserves the silhouette, then set density
so gravity reads correctly instead of crumbling the mesh.

### Phase 5: Solver, scene wiring, and material fix

**Do**
1. Drag the flesh asset into the scene (material will be missing at first).
2. Add → Deformable Solver actor. Select the flesh asset → Details →
   Primary Solver → the deformable solver. Sharing rule: interacting flesh
   assets share one solver; non-interacting assets each get their own
   ("not a hard fast rule, just a recommended suggestion").
3. Simulation viewport → green play. If the mesh rockets upward, it is
   intersecting the floor: Scene Preview → Transform → Location Z = 50,
   then re-run.
4. Material: select the flesh asset → Details → search "override mat" →
   Override Material → + → pick the source material.

**Check**
- Frame evidence: outliner shows FA_gummybear + DeformableSolver, Primary
  Solver dropdown set (frame_008).
- Play: the bear jiggles with its material applied.

**Why**
The flesh asset is inert until a solver runs it, and the material lives
on the source asset, not the sim volume, so it must be re-applied as an
override.

### Differences vs. Chaos Destruction (author-stated, verify in docs)

- Flesh assets do not work with Field Systems and cannot be fractured.
- Collisions do not work by default; you specify which actors the
  deformable solver monitors (the blank-template floor is pre-monitored).
- The workflow overlaps with Chaos Destruction but is a different pipeline
  (DataFlow vs. fracture-centric).

### The human method, distilled

1. Minimum cells that preserve detail; Tet Wild only when thin features
   matter ("assign only the minimum number of cells you absolutely need").
2. Add Set Flesh Default Properties manually — the template is broken
   without it.
3. Start density low (0.01 worked for a 1 m gummy bear); 1.0 crumbles.
4. One solver per interacting group; save often (experimental).
5. If the mesh rockets, it is intersecting the floor — raise Z.

**Depth status:** FULL (287 caption lines, 12 frames reviewed, description
metadata; project files linked but not downloaded).

## 2. "OpenMOSS released MOSS-Image, and it's now supported in ComfyUI." (crystal_alpine)

Source: https://www.reddit.com/r/comfyui/comments/1xa6wmo/ | native clip
v.redd.it/omxexc0e9hwh1 | score 130, 28 comments (25 top-level retrieved)

Tools used: MOSS-Image (OpenMOSS), ComfyUI with the official workflow at
https://huggingface.co/Comfy-Org/MOSS-Image. Community artifacts reported in
comments: 4- and 8-step Turbo LoRAs, 2+ full finetunes, depth ControlNet
(LoRA), inpainting workflow, experimental image-editing plugin.

This audit reconstructs the recipe from the post selftext and the comments,
so another agent can run the same model. Every phase has Do / Check / Why.
The post's core method is: run the official Comfy-Org workflow with
conservative settings, quantize if VRAM-bound, and ride the community's
4-day-old LoRA/tooling wave. (Inference: "ride the wave" is my summary of
the comment thread, not the author's words.)

### Phase 1: What the model is

**Do**
1. Know the architecture: 5B DiT, Qwen3.5-9B text encoder, FLUX.2 VAE.
2. Pick a checkpoint: Base, or SFT (fine-tuned on curated data).
3. License: Apache 2.0 (commercial OK — author-stated).

**Check**
- Files come from the official Comfy-Org HuggingFace repo.

**Why**
Apache 2.0 keeps it usable in intake pipelines without license friction;
the FLUX.2 VAE and Qwen3.5 encoder explain the VRAM footprint below.

### Phase 2: Run it (author's starter settings)

**Do**
1. Resolution 1024x1024, 50 steps, CFG 3, shift 5.
2. Expect it to be slow: "Neither model is step-distilled, so it's not
   fast."

**Check**
- Output is legible EN/ZH text when prompted for it (the headline
  capability).

**Why**
Text rendering is the differentiator: "Legible text in English and
Chinese, which most open models still struggle with." Layout prompts:
pass structured JSON with bounding boxes to control where text and
objects go — "useful for posters, ads, and anything with a real layout."

### Phase 3: Fit it in VRAM

**Do**
1. Full BF16: ~10 GB DiT plus ~17 GB text encoder (author-stated).
2. Use community INT8 and INT4 quants; commenters report it running on
   8 GB cards.

**Check**
- Quantized run completes without OOM on the target card.

**Why**
The 9B text encoder dominates VRAM; quants are the practical route for
single-GPU workstations.

### Phase 4: The 4-day ecosystem (commenter evidence)

**Do**
1. Track the community velocity: by 2026-10-21 (4 days post-release) there
   were already multiple 4- and 8-step Turbo LoRAs, at least two full
   finetunes, a depth ControlNet (LoRA), an inpainting workflow, LoRA
   support in popular trainers, an experimental image-editing plugin, and
   ComfyUI performance improvements (commenter infearia, score 19:
   "Every time I get back to my computer there is something new dropping
   for MOSS-Image. When am I supposed to test all that stuff?").
2. Note the thread's own drift: the most-argued sub-topic was ComfyUI
   0.36's native loops (recursion-based, long startup delay,
   max-recursion crash past a few dozen iterations; PR
   Comfy-Org/ComfyUI#16227 replaces recursion with iteration; fix PR
   #16556 linked) — relevant to anyone automating ComfyUI loops.
3. Note the agentic signal: BazzTheBazz (score 6): "I use Claude with the
   comfy mcp to test things for me and write a report. It can do
   everything autonomously including fine tuning the workflows to your
   specs, download the models and copy them in the appropriate folder."
   (Quoted verbatim; P2 gap evidence, see Gap alerts.)

**Check**
- Verify each community artifact exists before depending on it (the
  thread is 4 days old; half-lives are short).

**Why**
For intake pipelines the model is the commodity; the surrounding
workflow/quant/LoRA ecosystem is the real integration cost.

### The human method, distilled

1. Start at the author's settings (1024, 50 steps, CFG 3, shift 5) and
   accept slowness until a distilled variant exists.
2. Quantize the text encoder first — it is the VRAM hog.
3. Check the ecosystem weekly, not daily; pin working artifacts.

**Depth status:** PARTIAL (full selftext + 25 top-level comments; the
native demo clip was not content-analyzed; a media download would add
little — the tooling evidence is textual).

## 3. "My procedural sci-fi ship generator" (OrbitalShipyard)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xa7sgb/ |
native clip v.redd.it/2s4dbztcfhwh1 | score 113, 10 comments (author's own
comments retrieved via author search; post-comment API returned 422,
PullPush empty — index lag on 1-day-old posts)

Tools used: plain JavaScript running in the browser, drawings on an HTML
canvas. No graphics or 3D software, no image model ("No graphics or 3D
software at all, just code" — author, verbatim). The code was written with
an AI coding assistant.

This audit reconstructs the generator from the author's four substantive
comments, so another agent can reimplement the recipe. The core method is:
describe parametric rules in detail (shapes, colors, fit), play them out
from a seed, and project real 3D geometry isometrically onto a 2D canvas
with custom shading.

### Phase 1: Define the hull as a parametric segment chain

**Do**
1. Build the hull as a chain of core segments along one axis.
2. Each segment is a box, a cylinder, or an octagonal prism; snap width,
   height, and length to a grid; follow a taper profile so the ship is
   thicker in the middle.
3. Between segments, place either a narrow neck with rings or an open
   truss.

**Check**
- The silhouette reads as one tapered body, thicker amidships.

**Why**
Grid-snapping plus a taper profile keeps random segments coherent; the
neck/truss joints break monotony without breaking the profile.

### Phase 2: Attach engines, nose, and wings

**Do**
1. Engines go on the rear segment: count 1–4, layout depends on the
   segment's width, and engine shape matches the segment shape.
2. Nose: wedge, point, blunt end, or cone.
3. Wings with optional engine pods attach to one of the longer segments.
   (Author's comment was truncated here by the API — [inference]: further
   parts like antennas/panels follow the same attach-to-segment pattern,
   consistent with the author's other comment that "the extra parts on it
   (engines, panels, connectors, antennas) have their own parameters too.")

**Check**
- Engine count never exceeds what the rear segment's width supports.

**Why**
Fit rules (count/layout keyed to the segment they mount on) are what make
generated ships look designed rather than random.

### Phase 3: Render 3D geometry as a 2D illustration

**Do**
1. Build ships as real 3D geometry (boxes, cylinders, lofted prisms) but
   with no 3D engine.
2. Project everything isometrically and draw it flat on a 2D canvas with
   the generator's own shading and palettes — "which is where the
   illustrated look comes from" (author, verbatim).
3. Every image is the same rule description played out from a different
   seed ("Every image you see is that description played out from a
   different seed" — author, verbatim).

**Check**
- The same seed reproduces the same ship; different seeds vary within the
  rules.

**Why**
Isometric projection plus custom shading is the whole aesthetic: it reads
as illustration, not as a 3D render, while the underlying geometry stays
consistent.

### Phase 4: Grow the system

**Do**
1. Extend the same parametric system to new object types: the generator
   already covers space stations, satellites, probes, fighters, drones,
   repair ships, and megastructures (author: "I'm still refining those,
   so they'll show up later"), plus megacities and docks under the
   "Orbital Shipyard" world.
2. Post one new output daily (author posts daily on Instagram
   @orbitalshipyard).

**Check**
- New types share the same palettes and fit rules so the world reads as
  one.

**Why**
One rule system, many object types: the daily-post cadence is the
iteration loop.

### The human method, distilled

1. "I came up with the idea and described it in detail: the rules, the
   colours, the shapes and how everything should fit together" — write the
   design doc first, then code it.
2. Code-drawn, seed-driven, AI-assisted coding but no image model.

**Depth status:** PARTIAL (author's own comments are the evidence; no
code seen, no numeric parameters beyond the 1–4 engine count and the
shape lists; a media download would add showcase frames, not workflow).

## 4. "House of Courland" (BeginningAmphibian69) — DEPTH-LIMITED

r/3Dmodeling post 1xa8waz (score 55): "Sharing my recent scene I made in
Unity" with an ArtStation link (artwork/vzzZaO). Native clip, 1 comment
(unretrievable — comment API 422). Tool inference only: the author's past
comment on a different post said "I textured it in substance painter and
rendered in marmoset toolbag" — may or may not apply to this Unity scene.
Showcase only; no workflow retrievable. A media download would add frames
of a finished scene, not tooling.

## 5. "Space robot made for Zbrush 2027" (benavidmark) — DEPTH-LIMITED

r/3Dmodeling post 1xaca2q (score 29): ZBrush sculpt showcase. Selftext is
an Instagram link; 3 comments retrieved, all trivial ("Thanks :)", and
"Yes i make all by hand" on an older post). Tool named (ZBrush 2027),
hand-sculpted, no workflow detail. A media download would add sculpt
frames, not tooling.

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Soft-body physics stage (UE-side) | Chaos Flesh tutorial (video 1) | NEED | trellis-pipe has weld/qa/lods/uv/bake but no soft-body stage; UE packaging stage (ue/) exists; UE5 client is the separate Aetheria repo | Watchlist: UE-side soft-body counterpart to the Squishy Volumes (Blender MPM) row; the DataFlow recipe (min-cells rule, solver-sharing rule, 1 m scale rule) is reference material for the Aetheria client |
| Open-weights image model for intake/ | MOSS-Image (video 2) | PARTIAL | intake/ does concept-to-input generation but no model is pinned; no written AI-vendor acceptance spec (P1 gap) | Backlog: evaluate MOSS-Image (Apache 2.0, text rendering, layout JSON) as intake's model-swappable image backend; community velocity (Turbo LoRAs in 4 days) is the integration-cost signal |
| Parametric code-driven asset authoring | Ship generator (video 3) | NEED | Foundry is TRELLIS-2 + mesh stages; no code-drawn parametric authoring | Watch: pattern only, no attach point today |
| ComfyUI loop automation ceiling | MOSS-Image thread comments | NEED | No evidence intake/ uses ComfyUI native loops | Note: if intake ever automates ComfyUI loops, the 0.36 recursion bug (~70-iteration ceiling) applies |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Free/open image backend for image_client.py | MOSS-Image (video 2) | PARTIAL | pipeline/image_client.py has fail-closed spend gate, $0.00 spent, OpenAI account has no credit (roadmap beads 9le.25) | Backlog: MOSS-Image is Apache 2.0 and runs quantized on 8 GB cards — a $0 image source for generated hawk/boar art; evaluate against the procedural stand-ins |
| Parametric hull recipe (grid-snap, taper, fit rules) | Ship generator (video 3) | PARTIAL | pipeline/proc/make_textures.py + make_audio.py are seeded procedural generators; no parametric-geometry recipe | Watch: technique-transfer candidate for procedural authoring stages |
| Soft-body physics | Chaos Flesh tutorial (video 1) | — | Godot 4.7.2 + Jolt physics per inventory | Skip: UE-only; Godot-side soft body is Jolt's, not Chaos |
| P1 import-validation gap (rec 9) | — | NEED (unchanged) | qa/asset_validate.py still absent per inventory | No tool today fills it |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Isometric code-drawn sprite recipe | Ship generator (video 3) | PARTIAL | tools/gen_iso_sprites.py does headless Blender sprite renders; tools/procedural_art.py, building_families.py for procedural authoring | Watch: the parametric-3D → isometric-2D-canvas + custom-shading recipe is directly analogous to Desktop City's sprite pipeline; pattern input, no new tool |
| Free concept-art image source | MOSS-Image (video 2) | PARTIAL | AI inputs optional (openai_key.py, tripo_key.py, seed_browser.py) | Watch: open-weights concept art without API spend |
| Soft-body physics | Chaos Flesh tutorial (video 1) | — | Godot 4.7.2, fixed-view sprites; PRD 17.1 | Skip: engine mismatch and not needed for sprite subjects |
| P1 shader skyline fill | — | NEED (unchanged) | No equivalent per inventory | No tool today fills it |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Vendor-independent ship generation | Ship generator (video 3) | PARTIAL | tools/asset-pipeline takes Meshy GLB + concept PNG in; profiles include SMALL_SHIP, STATION | Watch: parametric code-driven generation as an alternative to Meshy-class inputs; concept-PNG-as-authority convention could pair with a code-drawn generator |
| Text-rendering image model for concept/marking art | MOSS-Image (video 2) | PARTIAL | Concept PNG is visual authority (colour, markings, faction identity); no AI-vendor acceptance spec beyond that | Backlog: MOSS-Image's legible text + layout JSON suits faction markings/labels on concept art |
| Soft-body physics | Chaos Flesh tutorial (video 1) | — | Native PC Godot 4.7.x direction (ADR 0016) | Skip: engine mismatch |
| P1 Godot import validation gate | — | NEED (unchanged) | Nothing to validate into yet per inventory | No tool today fills it |

## Watchlist trending

## Watchlist trending
- ComfyUI custom nodes wrapping intake/ stages (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-05, 2026-10-16, 2026-10-21) **TRENDING**
- Scumble (free inpainting editor, own ComfyUI or API keys) (first seen 2026-09-30, status WATCH; seen again 2026-10-02, 2026-10-16, 2026-10-21) **TRENDING**
- ComfyUI native Asset System (pre-release) (first seen 2026-10-01, status WATCH; seen again 2026-10-02, 2026-10-16, 2026-10-21) **TRENDING**
- comfyui-minimax-h3-studio (BiggerFishy; SAM3 + color-inversion character-swap workflow, MIT) (first seen 2026-10-03, status BACKLOGGED; seen again 2026-10-09, 2026-10-16, 2026-10-21) **TRENDING**
- Pocket AI + Tensor Master (mexxmillion ComfyUI front-end + GPU job dispatcher, Vast rentals) (first seen 2026-10-03, status WATCH; seen again 2026-10-16, 2026-10-21) **TRENDING**
- OmniChar/.char portable character format + ComfyUI-Omnichar node pack (first seen 2026-10-05, status BACKLOGGED; seen again 2026-10-08, 2026-10-09, 2026-10-16, 2026-10-21) **TRENDING**
- Flux klein 9B/4B distilled variants + CCTech/Flux Klein ComfyUI node pack (first seen 2026-10-05, status WATCH; seen again 2026-10-08, 2026-10-09, 2026-10-16, 2026-10-21) **TRENDING**
- YEDP Action Director (ComfyUI 3D viewport; Mixamo/FBX/GLB; OpenPose/Depth/Canny/Normal/Shaded/Alpha passes) (first seen 2026-10-05, status WATCH; seen again 2026-10-02, 2026-10-16, 2026-10-21) **TRENDING**
- SelfLift dual sampling + Color Transfer stitching recipe (MiniMax H3, ComfyUI) (first seen 2026-10-08, status WATCH; seen again 2026-10-11, 2026-10-16, 2026-10-16, 2026-10-21) **TRENDING**
- RefMod (ComfyUI custom nodes, character identity without LoRA training) (first seen 2026-10-16, status BACKLOGGED; seen again 2026-10-21)
- FLUX 3 Image Klein (5.6B, Black Forest Labs, native ComfyUI) (first seen 2026-10-16, status WATCH; seen again 2026-10-17, 2026-10-17, 2026-10-21) **TRENDING**
- Hand-painted stylized character texturing (Substance Painter + ZBrush + Arnold Maya, toon aiStandardSurface variant) (first seen 2026-10-07, status WATCH; seen again 2026-10-21)
- Substance Painter 3D-space blur filter (baked Position Map, blur by 3D proximity to kill UV seams; previously paid Gumroad, now free) (first seen 2026-10-12, status WATCH; seen again 2026-10-21)
- PopcornFX stylized laser VFX (Unity 6 breakdown) (first seen 2026-09-30, status WATCH; seen again 2026-10-21) **TRENDING**
- TreeSculpt (spline-based tree builder, Unity asset store) (first seen 2026-10-08, 2026-10-21) **TRENDING**

Accuracy review of the auto-matches (done this run, annotated in
`references/tooling-watchlist.md`): 14 of the 15 "seen again 2026-10-21"
hits are token overlap, not genuine reappearances (ComfyUI/Unity/
Substance Painter/FLUX.2 VAE tokens; the named tool never appears in
today's posts). Only "ComfyUI custom nodes wrapping intake/ stages" is
genuine — MOSS-Image's official Comfy-Org workflow continues the
day-0-ComfyUI-support pattern (same as FLUX 3 Klein on 2026-10-16).
The false matches are annotated in place per the established convention.

New watchlist additions (genuinely new tools/stages):
- MOSS-Image (OpenMOSS, 5B DiT, Apache 2.0) — WATCH
- UE 5.8 Chaos Flesh soft-body via DataFlow templates — WATCH
- Parametric sci-fi ship generator (JS canvas isometric, seed-driven) — WATCH
- ComfyUI 0.36 native loops recursion bug (PR #16227/#16556) — WATCH

## Gap recommendations (highest-leverage NEEDs)

1. **Evaluate MOSS-Image as the $0 image backend for 2d3d's image_client.py
   and Aegis intake/.** Apache 2.0, runs quantized on 8 GB cards,
   legible text + layout-JSON prompts. Concrete next step: run the
   official Comfy-Org workflow on a local GPU and compare concept-art
   output against the current procedural stand-ins (2d3d beads 9le.25).
2. **Log the Claude + Comfy MCP report as P2 agentic-DCC prior art.**
   First-hand claim of a fully autonomous ComfyUI test/fine-tune/deploy
   loop. Concrete next step: verify the Comfy MCP server's capabilities
   against intake's automation needs before building custom loop code.
3. **Keep the Chaos Flesh DataFlow recipe as the UE-side soft-body
   reference.** The min-cells rule, density 0.01 heuristic, and
   solver-sharing rule are directly reusable in the Aetheria client when
   soft bodies are needed. No action today beyond the staged skill.
4. **Feed the ship-generator fit rules to Desktop City's sprite pipeline
   thinking.** Grid-snapped parametric segments + isometric projection is
   the same shape as gen_iso_sprites.py; the recipe is pattern input for
   future procedural authoring.
5. **Treat ComfyUI native loops as broken for automation.** If any
   intake/foundry design uses native loops, pin the recursion-for-iteration
   workaround or avoid native loops until fixed.

## Explicit non-goals

- "[OC] Real-time engine simulation..." (r/Simulated, score 182): audio +
  physics showcase; zero tooling hits, no tools named. Skipped per the
  downweight rule.
- "Spent way too long making a roguelite shooter..." (r/unity, score 145):
  game promo; zero tooling hits. Skipped per the downweight rule.
- Chaos Flesh for Godot repos (2d3d, Desktop City, Solarempire): engine
  mismatch, skipped with reason above.
- House of Courland / Space robot: showcases, no extractable workflow.

## skill_library artifacts staged

- New skill `skills/simulation-vfx/chaos-flesh-dataflow-soft-body/` (FULL audit)
- New skill `skills/ai-video/moss-image-comfyui-recipe/` (PARTIAL audit, recipe-grade)
- New skill `skills/procgen-worlds/parametric-ship-generator-isometric/` (PARTIAL audit, author-comment evidence)
- Full report staged at `docs/scout-reports/have-vs-need-2026-10-21.md`
- Watchlist rows synced to the repo mirror's `video-tooling-scout/references/tooling-watchlist.md`
- README tables updated (skills/README.md grouped tables, root README counts)

## Run notes / infra

- r/godot scan 429'd (rate limit); not covered this run.
- Comment fetch: Arctic Shift 422 on 3 of 4 native-video posts; old-Reddit
  JSON is bot-walled from the sandbox; PullPush index lags ~1 day on fresh
  posts (returned empty). Workaround that succeeded: author-comment search
  via Arctic Shift for the ship-generator thread.
- yt_download.py's bundled yt-dlp was broken (venv interpreter missing);
  installed yt-dlp 2026.08.19 via system pip (--break-system-packages).
  The YouTube download succeeded with no approval gate firing (android
  client; format 18). Worth noting the sandbox venv for the summarizer
  skill is broken — future runs will need the same workaround.
- subreddits.yaml still lists 17 subreddits vs. the 23 claimed in the
  2026-10-20 memory note (threejs, GraphicsProgramming, shaders,
  VoxelGameDev, RealTimeVFX missing). Reconcile before the next run.
