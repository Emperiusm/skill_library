# Have-vs-need: 2026-10-05

Daily video-tooling-scout run. Scan window: last 2 days (2026-10-03 to 2026-10-05).
Depth mode: `pre-approved` (max 2 media downloads, Ehsan 2026-09-27).

## Gap alerts

**P1 ALERT — AI-vendor generation/acceptance spec (aegis `intake/`): practice evidence found.**
The OmniChar `.char` format (audit #1) is a concrete, machine-checkable character-identity
acceptance spec: a locked description plus a reference set whose cropped face is scored by
sface and DINOv2, optionally carrying a trained LoRA. That is "what good means" for a
generated character, expressed as data plus a similarity score, not prose. This is a
meaning-match for the P1 gap "AI-vendor generation/acceptance spec (what good means per
asset type)". Recommended next step: draft the intake acceptance-spec schema with a
per-asset-type machine-checkable score field, using the .char structure
(description + reference set + embedding score + optional adapter) as the template.
Also relevant to 2d3d's P1 "written art bible" gap (rec 2) and Solarempire's
"no AI-vendor generation/acceptance spec for Meshy-class inputs" gap.

No other extracted tool matched a P1/P2 gap by keyword or meaning. YEDP Action
Director's smart bone-name normalization (audit #6) is retargeting-adjacent but does
NOT fill the P1 rig/skin/retarget gap: it normalizes Mixamo bone names to bake
ControlNet passes, it does not rig generated meshes.

## Scan summary

- Subreddits queried: unity, unrealengine, godot, blender, houdini, substance3d,
  photogrammetry, gameassets, topology, aigamedev, comfyui, vibecoding,
  technicalart, proceduralgeneration, vfx, Simulated, 3Dmodeling, gamedev.
- Coverage gap: `gameassets` returned HTTP 422 from Arctic Shift this run (same as
  the 2026-10-04 run); its video posts were not scanned.
- Video posts returned: 6 (r/comfyui x3, r/proceduralgeneration x3).
- Deep analysis cap: 8. Deeply analyzed: 6.

| # | Title | Creator | Source | Depth |
|---|-------|---------|--------|-------|
| 1 | "One .char model, Consistent face, body & cloths, now works in Comfy(Custom node & workflows) MinimaxH3 & Flux2" | ashishsanu | https://v.redd.it/w19nx5ws09th1 (r/comfyui post 1wwmstf, score 127) | FULL |
| 2 | "Introducing Vathography: Artistic application of the Marigold V2 model for photographers" | karijoart (Karim Joseph) | https://www.youtube.com/watch?v=EjohqO3GP90 (2:37, captions) + tutorial https://www.youtube.com/watch?v=ZALSOni2XQk (3:08, captions) | FULL |
| 3 | "I made a game where everything is procedural, even the cows. Here's the trailer for PROJECT: ABSOLUTELY NORMAL" | Inevitable-Cash8506 | https://v.redd.it/72mj84s289th1 (r/proceduralgeneration post 1wwnkkl) | FULL (comments-sourced) |
| 4 | "From Space to the Surface of a Procedural Planet Shaped by Plate Tectonics" | HabitableZone_ (TropoPlate) | https://v.redd.it/wjmclj5u99th1 (r/proceduralgeneration post 1wwnogh) | PARTIAL |
| 5 | "Ink Fauna: procedural creatures painted live in sumi-e ink" | (r/proceduralgeneration post 1wwu92a) | https://v.redd.it/dhxjilt3oath1 | DEPTH-LIMITED |
| 6 | "Flux klein+YEDP" | (r/comfyui post 1wws7z7) | Google Drive workflow link | DEPTH-LIMITED |

## 1. "One .char model, Consistent face, body & cloths, now works in Comfy" (ashishsanu)

Source: https://v.redd.it/w19nx5ws09th1 | r/comfyui post 1wwmstf (score 127, 26 comments) | native clip (demo)
Repo: https://github.com/omnichar/ComfyUI-Omnichar (public, GPL-3.0; created 2026-10-02; 36 stars, 22 commits at audit time)

Tools used: ComfyUI custom node pack "ComfyUI-Omnichar"; the `.char` portable
character format; Omnichar Studio / Omnichar Cloud (character builder);
omnichar-sdk (Apache-2.0, dependency-free `.char` reader); generation backends
Minimax H3, Krea2, Flux2 dev, klein 9B and 4B; face scoring with sface and
DINOv2 (author's comment).

This audit reconstructs the exact workflow from the repo README and the author's
comments, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The video's core method is: build the character once as a
portable file, then let every model consume the same resolved references.

### Phase 1: Install the node pack

**Do**
1. Clone into the ComfyUI custom nodes directory and install the reader:
   `git clone https://github.com/omnichar/ComfyUI-Omnichar` inside
   `ComfyUI/custom_nodes`, then `pip install -r requirements.txt`. Restart ComfyUI.
2. Requirements: ComfyUI, Python 3.10+, the `omnichar-sdk` package (comes from
   `requirements.txt`).

**Check**
- If the nodes still show as missing after an install-by-URL, the author
  advises following the README's installation steps and, failing that, the
  direct git URL. (Failure mode seen in the comments: "installed with url
  still showing same"; author: "try direct git url".)

**Why**
The nodes are thin: the `.char` format is read by the standalone SDK, so the
ComfyUI pack is mostly wiring.

### Phase 2: Encode the character (build the .char)

**Do**
1. Gather reference images: face, body, and wardrobe, three slots each.
2. Feed them to the **Encode Character** node (`name`, `description`,
   `resolution`, plus the face/body/cloths slots). It sorts references by role
   so face comes first and the prompt numbers follow that order.
3. **Save Character** writes `<name>.char` into `ComfyUI/models/characters/`.
   To share one folder with Omnichar Studio, set `INLINE_CHARACTERS_DIR` to
   the Studio characters directory.

**Check**
- A `.char` holds the reference images, the locked description, and often a
  trained LoRA. The author states the same method "encodes character prompts
  [and a] cropped face which is scored by sface & dinov2", and that one
  character format is trained to work across multiple models.

**Why**
The format separates identity from the generator: one file feeds FLUX.2,
MiniMax H3, and anything else that takes references.

### Phase 3: Decode into a target model

**Do**
1. **Load Character** reads the `.char` (`char`, `char_path` in).
2. **Decode Character** (`char`, `style`, `clip`, `prompt`, `arch`,
   `max_references`, `size_from`, `fit`) emits `conditioning`, `references`,
   `refs`, `sheet`, and `prompt`.
3. Route by model type, keeping reference order (a prompt addresses images by
   number):
   - Single-batch models read `references`.
   - Numbered-slot models (MiniMax H3) take `refs` into **Character References
     Split** (fans out to `image_0`..`image_4` plus `count`) or one
     **Character Reference** node per slot (`refs`, `index` -> `image`,
     `role`, `count`).
   - Edit models that read references as latents (FLUX.2) take `refs` into
     **Character Reference Latent** on both positive and negative conditioning.
4. If the character carries a LoRA, **Apply Character LoRA** puts it on MODEL
   and CLIP (`strength`, `arch`, `min_key_coverage`).

**Check**
- Positions are kept: "Reference order is preserved, because a prompt
  addresses images by number." Verify slot N in the prompt matches image N.

**Why**
Each model family wants references differently (batch, slots, latents); the
decode step adapts one resolved set to all of them instead of rebuilding
per-model reference packs.

### Phase 4: Generate (author's tested routes)

**Do**
1. MiniMax H3: use the default MiniMax ComfyUI workflow with the split
   references in numbered slots; adjust params and resolution. The author
   notes "Character part doesn't require any heavy specs" beyond what
   MiniMax itself needs.
2. FLUX.2 Klein 9B: references-as-latents workflow to an image (shipped in
   the repo's `workflows/`).

**Check**
- Commenter benchmark (16 GB VRAM, 32 GB RAM): reference-image prompting
  OOM'd above 0.8 MP; the same reference images packed into a `.char`
  completed at 1 MP, and the commenter judged it better than reference
  images. The `.char` path is cheaper than raw reference images at the
  same resolution.

**Why**
Pre-encoding and scoring the identity once beats re-resolving raw reference
images on every run: less VRAM, consistent identity.

### The human method, distilled

1. "Build a character once, use it across image and video models" (repo
   tagline): identity is data, not a prompt you retype.
2. Encode once, decode per model: keep one resolved reference set and adapt
   it at the last step (batch vs slots vs latents).
3. Score the identity, don't eyeball it: the cropped face is scored by sface
   and DINOv2 at encode time.
4. Roadmap (author): consistent character voice and multi-character support
   are next; multi-char in one video is not yet supported.

**Depth status:** FULL (repo README with exact node I/O + author comments with
benchmarks and method detail).

## 2. "Introducing Vathography" (Karim Joseph / karijoart)

Source: https://www.youtube.com/watch?v=EjohqO3GP90 | 2:37 | captions (en/manual)
Companion tutorial: https://www.youtube.com/watch?v=ZALSOni2XQk ("Blender short
tutorial", 3:08, captions en/asr, 21 views)
Practice page: https://vathography.com | r/comfyui post 1wwrb7l (10 comments)

Tools used: Marigold V2 (single-image depth estimation; Apache 2.0, free even
for commercial use; team: Igor Pavlovic, Thiemo Wandel, Anton Obukhov, Luca
Bartolomei, Andrey Davydov, Fabio Tosi, Matteo Poggi, Sabine Süsstrunk,
Dengxin Dai); ComfyUI native Marigold V2 implementation
(https://docs.comfy.org/tutorials/utility/marigold-v2); Hugging Face demo
(https://huggingface.co/spaces/toshas/Marigold-V2); Blender compositor for the
depth remap. Author: Karim Joseph Nassar, multidisciplinary digital artist,
canton of Bern, Switzerland; practice published 1 October 2026.

This audit reconstructs the exact workflow from both videos' captions and the
video description, so another agent can follow the same process. The core
method is: a depth map is a technical pass made to be hidden; Marigold V2 made
it detailed enough to be the artwork.

### Phase 1: Estimate the depth map

**Do**
1. Take any photograph, including ones already in the archive: "Depth
   estimation is a post process. We can apply it to any photograph we already
   have."
2. Run Marigold V2 on it. Routes: the ComfyUI native implementation (no
   third-party custom nodes needed; the author warns some community nodes
   have carried malicious code), or the official Hugging Face demo for a few
   free photos a day (note: uploads are processed on HF servers, so avoid
   private images).
3. Export the depth as EXR for Blender.

**Check**
- The V2 release is the enabler: finer detail in the depth map from a single
  photograph, which the author judged sufficient to carry an artwork on its own.

**Why**
The depth map used to be an intermediate pass (Photoshop uses it for lens
blur). V2's detail crosses the threshold where the volume rendition itself is
worth showing.

### Phase 2: Remap the depth in Blender (from the tutorial captions)

**Do**
1. Render tab > Color Management: set View to **Standard** (no view transform
   applied to the images).
2. Compositing tab > New. Delete the Render Layers node and the Group Output
   node (X to delete); only the Viewer node is needed. Disable the backdrop.
3. Drag-drop the depth EXR into the compositor; connect its image output to
   the Viewer input. In the Image Editor, select the Viewer node to preview.
4. Add a **Color Ramp** node (Shift+A, search) dropped onto the connection.
5. Shape the look with the stops:
   - Mist-pass look: background white, foreground black; soften the
     transition by changing interpolation to **B-spline**.
   - Isolate a depth range: bring stops closer together ("isolating this range
     of the depth").
   - Colorize freely: stops can be any color (tutorial demos a blue).
6. Image > Save As to export.

**Check**
- Read the scene by depth and volume, not light and color; the focus becomes
  "the area we choose to highlight", and several subjects at different depths
  can be highlighted at once.

**Why**
Remapping turns a technical grayscale pass into a composed artwork: the
photographer chooses what the volume emphasizes instead of accepting the
raw depth output.

### The human method, distilled

1. New tool capability, new practice: when a hidden pass gets good enough,
   make it the artwork instead of hiding it.
2. Shoot with purpose: "the most interesting vathographs will come from
   photographs taken with purpose", reading scenes by depth and volume at
   capture time.
3. Keep the toolchain boring: stock ComfyUI + stock Blender compositor, no
   exotic nodes, so the practice is reproducible.

**Depth status:** FULL (manual captions for the intro + 80-segment ASR
captions for the tutorial with exact Blender steps).

## 3. "PROJECT: ABSOLUTELY NORMAL" (Inevitable-Cash8506)

Source: https://v.redd.it/72mj84s289th1 | r/proceduralgeneration post 1wwnkkl
(14 comments) | native clip (game trailer)
Game: https://absolutelynormal.silberie.com/download

Tools used: no named engine, DCC, or audio tool. Everything is code-built at
startup from primitives; sound and music are synthesized from sine waves and
basic waveforms. The author's comments are the entire technical record.

This audit reconstructs the author's stated method from their comments, so
another agent can follow the same discipline. The core method is: no asset
files; one seed builds the whole island, including the cows.

### Phase 1: Set the one-seed architecture

**Do**
1. Load no asset files at startup. Generate terrain, roads, towns, people,
   sky, sound effects, and radio music from one seed, so every island is
   different.
2. Build every prop from code at startup: the author's example, a bathtub, is
   "a rounded box, a few spheres for the foam, four little cones for the claw
   feet and a rubber duck made of two spheres and a cone".

**Check**
- "No assets" means: nothing made in Blender, no recorded sounds. Everything
  is built in code when the game starts.

**Why**
One seed plus code-built primitives makes every island its own with zero
asset pipeline to maintain.

### Phase 2: Keep the primitive kit small

**Do**
1. Use simple shapes, boxes and spheres, rather than pure-math surfaces: the
   author notes their approach is "a bit less hardcore" than a pure sine-wave
   game, since they use boxes and spheres for geometry.
2. Synthesize all audio the same way: "the sounds in mine actually are made
   with sine waves and other basic waveforms", including the radio music.

**Check**
- The one thing the author did not make: the font. Everything else,
  geometry and audio, is generated.

**Why**
A tiny primitive kit plus waveform audio keeps the whole game reproducible
from the seed with no external dependencies.

### The human method, distilled

1. The seed is the asset pipeline: world, props, and audio all derive from
   one value at startup.
2. Boxes, spheres, cones, sine waves: pick primitives simple enough to
   reason about, then compose them.
3. Disclose the trick plainly: the author's comments explain the method in
   the open (including the joke that "officially they're cows" and nobody
   asked where the herd keeps coming from).

**Depth status:** FULL (author's own comments; no video download needed since
the tooling signal is entirely in the text).

## 4. "From Space to the Surface of a Procedural Planet Shaped by Plate Tectonics" (HabitableZone_)

Source: https://v.redd.it/wjmclj5u99th1 | r/proceduralgeneration post 1wwnogh
(score 57, 3 comments) | native clip (space-to-surface transition)
Project: TropoPlate. Follow: https://discord.gg/Cx3uEYXu2P

Tools used: atmosphere renderer "mainly based on Hillaire's LUT-based method
(EGSR 2020), with some artistic adjustments" (author's comment); procedural
plate-tectonics terrain simulation (details in a linked prior post).

**Do** (as stated by the author)
1. Simulate the planet with plate tectonics for the terrain (method detailed
   in the author's prior post, not pulled this run).
2. Render the atmosphere with Hillaire's LUT-based method (EGSR 2020),
   adjusted artistically.
3. The clip shows the continuous transition from space down through the
   atmosphere to the surface.

**Check**
- A commenter asked about adding glacial erosion alongside simple water
  erosion, which the author did not answer in the visible comments.

**Why**
A LUT-based atmosphere gives a cheap, art-directable sky; the tectonic sim
gives the terrain large-scale geological structure for free.

**Depth status:** PARTIAL. The atmosphere method is named precisely
(Hillaire, EGSR 2020); the tectonic simulation detail lives in the author's
linked prior post, which could not be pulled (reddit.com is blocked for page
fetch in this environment and the no-live-browser rule forbids the fallback).
A media download would not add workflow detail for this clip.

## 5. "Ink Fauna: procedural creatures painted live in sumi-e ink" (r/proceduralgeneration post 1wwu92a)

Source: https://v.redd.it/dhxjilt3oath1 | 0 comments | native clip (demo)

Tools used: TypeScript and Canvas 2D; no engine, no bitmap images (author's
post text).

What the post states: type a prompt like "red koi fish" or "crane" and get a
procedural creature painted in Japanese sumi-e ink, redrawn live every frame;
the strokes swell when the creature moves fast, thin out on tight turns, and
never sit still.

**Depth status:** DEPTH-LIMITED. Stack and behavior are named, but there is no
workflow detail: no stroke-generation algorithm, no prompt-to-creature mapping,
no performance figures, and zero comments to mine. A media download would add
little: the clip is a demo, not a breakdown. The missing piece is the author
describing the stroke system.

## 6. "Flux klein+YEDP" (r/comfyui post 1wws7z7)

Source: Google Drive workflow file
(https://drive.google.com/file/d/16Zbw4-yQSrOXwJcoyADcQgCFTtVb9_2K/view?usp=sharing)
| 4 comments | scanner relevance 0.1 (downweighted: no tooling signal in post text)

Tools named (resolved via search, not from the post itself): Flux klein
(distilled small Flux variants; the Omnichar README lists klein 9B and 4B as
supported backends; the CCTech/Flux Klein node pack in
ChrisColeTech/ComfyUI-GGUF-Loader includes a Flux2KleinDepthMap preprocessor
using Depth Anything V2, checkpoints vits/vitb/vitg, default resolution 512);
YEDP Action Director (ComfyUI custom node: interactive Three.js 3D viewport,
loads FBX/GLB animations, Mixamo-compatible smart bone-name retargeting,
bakes OpenPose / Depth / Canny / Normal / Shaded / Alpha passes for
ControlNet). Comment notes: an AIO preprocessor can pull depth and color maps;
metallic, roughness, and ambient occlusion support was questioned but not
answered.

**Depth status:** DEPTH-LIMITED. The workflow file itself (a Google Drive
binary) was not opened and the post text names nothing; the tool identities
above come from resolving the title terms, not from the author's workflow.
What would reach FULL: the Drive workflow JSON showing exactly which klein
checkpoint and which YEDP passes feed the generation.

---

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Scored character-identity acceptance spec (OmniChar: locked description + reference set + sface/DINOv2 face score + optional LoRA) | #1 | NEED | intake/ has concept-to-input generation but no AI-vendor acceptance spec (verified absent 2026-09-26) | **Backlog: use the .char structure as the template for the P1 acceptance-spec gap** (gap alert above) |
| Depth-from-single-photo estimation (Marigold V2, Apache 2.0) | #2 | NEED | No depth-reconstruction stage in trellis-pipe | Watchlist: no current foundry need for depth-from-photo |
| Distilled small image models (Flux klein 9B/4B) | #1, #6 | NEED | No klein-class backend in intake/ | Watchlist: cheaper identity-consistent generation on 16 GB VRAM |
| Bone-name normalization / retargeting (YEDP smart retargeting) | #6 | NEED | No rigging/retarget stage at all (P1 gap) | Watchlist: prior art for the rig gap's research notes; does NOT fill the gap |
| LUT-based atmosphere rendering (Hillaire, EGSR 2020) | #4 | NEED | No atmosphere recipe in the cinematics bucket | Watchlist |
| One-seed asset-less game construction | #3 | NEED | Foundry is file-based by design | Watchlist: design philosophy, not adoptable as a stage |
| Speed-reactive procedural ink creatures (TypeScript/Canvas 2D) | #5 | NEED | Nothing comparable | Skip: 2D web demo, no foundry fit |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Scored character-identity acceptance spec (OmniChar) | #1 | NEED | No vendor acceptance spec; P1 "written art bible" gap (roadmap rec 2) | Backlog: identity-spec pattern feeds the art-bible/acceptance-spec work |
| Depth estimation model upgrade (Marigold V2) | #2 | PARTIAL | pipeline/reference/recon_pipeline.py already does Depth Anything 3 + SAM 2 reconstruction | Watchlist: Marigold V2 as a model-swap eval candidate (Apache 2.0, commercial OK) |
| Distilled small image models (Flux klein 9B/4B) | #1, #6 | NEED | pipeline/image_client.py has a $20 slice budget, $0.00 spent; no klein backend | Watchlist |
| Bone-name normalization (YEDP) | #6 | NEED | No retargeting stage | Watchlist |
| LUT-based atmosphere (Hillaire) | #4 | NEED | No atmosphere recipe listed | Watchlist |
| One-seed asset-less construction | #3 | PARTIAL | pipeline/proc/make_textures.py + make_audio.py are seeded generators, but the repo still ships asset files | Watchlist: the strict no-asset discipline is the new part |
| Ink creatures (TS/Canvas 2D) | #5 | NEED | Nothing comparable | Skip |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Scored character-identity spec (OmniChar) | #1 | NEED | No character pipeline (city sim) | Skip: no fit |
| Depth-from-photo (Marigold V2) | #2 | NEED | tools/extract_reference_world.py exists but no depth-estimation stage | Watchlist: could feed reference extraction |
| Flux klein 9B/4B | #1, #6 | NEED | AI inputs optional (tripo_key.py etc.), no klein | Skip: building sprites come from the Blender path by owner decision |
| YEDP Action Director | #6 | NEED | No character animation | Skip |
| LUT-based atmosphere (Hillaire) | #4 | NEED | No atmosphere recipe | Watchlist: cheap sky for the cozy city view |
| One-seed asset-less construction | #3 | PARTIAL | tools/procedural_art.py, building_families.py, city_* families: extensive procedural authoring, but assets still ship as files | Watchlist |
| Ink creatures | #5 | NEED | Nothing comparable | Skip |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Scored character-identity acceptance spec (OmniChar) | #1 | NEED | "No AI-vendor generation/acceptance spec for Meshy-class inputs beyond the concept-PNG-as-authority convention" | Backlog: .char pattern is a template for a Meshy-input acceptance spec |
| Depth-from-photo (Marigold V2) | #2 | NEED | Pipeline is concept PNG + Meshy GLB; no depth stage | Watchlist |
| Flux klein 9B/4B | #1, #6 | NEED | AI input is Meshy GLB by design | Skip |
| Bone-name normalization (YEDP) | #6 | NEED | stages/rig.py EXISTS (unlike Aegis), but YEDP is a ControlNet pass baker, not a production rigger | Watchlist: retargeting-adjacent prior art only |
| LUT-based atmosphere (Hillaire) | #4 | NEED | Space game; no atmosphere recipe listed | Watchlist: planet atmospheres |
| One-seed asset-less construction | #3 | NEED | Pipeline is file-based by design (concept PNG in, GLBs out) | Skip |
| Ink creatures | #5 | NEED | Nothing comparable | Skip |

## Gap recommendations (highest-leverage NEEDs)

1. **Adopt the scored-identity acceptance-spec pattern (Aegis P1).** OmniChar
   shows the shape: locked description + reference set + embedding similarity
   score (sface/DINOv2) + optional adapter (LoRA). Next step: draft the
   intake/ acceptance-spec schema with a machine-checkable score field per
   asset type, and mirror it into 2d3d's art-bible work and Solarempire's
   Meshy-input spec.
2. **Evaluate Marigold V2 for 2d3d's recon pipeline.** It is Apache 2.0 and
   commercial-OK, with a native ComfyUI implementation. Next step: a
   side-by-side depth-quality test against the current Depth Anything 3 stage
   on one reference plate.
3. **Keep Flux klein 9B/4B on the watchlist for budget generation.** The
   thread's benchmark (1 MP .char run succeeding on 16 GB VRAM where raw
   references OOM'd past 0.8 MP) is the first hard VRAM data point for
   identity-consistent generation on modest GPUs.
4. **File YEDP's smart bone-name normalization in the P1 rig-gap research
   notes (Aegis).** It does not fill the gap, but Mixamo-compatible
   auto-normalization of bone names is a reusable trick for whatever
   retarget stage eventually lands in trellis-pipe.
5. **Hillaire LUT atmosphere to the cinematics bucket.** Cheap,
   art-directable sky for Aegis cinematics and Solarempire planet
   atmospheres; EGSR 2020 paper is the reference implementation.

## Watchlist trending

## Watchlist trending
- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-03, 2026-10-05) **TRENDING**
- MCP servers driving Blender/Unreal (agentic DCC) (first seen 2026-09-27, status BACKLOGGED; seen again 2026-09-28, 2026-10-05) **TRENDING**
- Squishy Volumes (free Blender MPM soft-body, fracture upcoming) (first seen 2026-09-27, status WATCH; seen again 2026-10-05)
- Procedural ribbon cables (Blender GeoNodes) (first seen 2026-09-27, status WATCH; seen again 2026-10-05)
- Light Wrangler Blender add-on (gobo lighting rigs) (first seen 2026-09-27, status WATCH; seen again 2026-10-05)
- Codex CLI driving Blender via MCP (mannequin-guided camera motion) (first seen 2026-09-28, status WATCH; seen again 2026-09-28, 2026-10-05) **TRENDING**
- GPT Astra (mesh split, UV fix, CC0 texture replacement; Blender MCP looping) (first seen 2026-09-28, status WATCH; seen again 2026-10-04, 2026-10-05) **TRENDING**
- HBLink (Blender<->Houdini live-link + cache bridge, Gumroad, by Itz_Keay) (first seen 2026-10-03, status BACKLOGGED; seen again 2026-10-05)
- Raup shell morphospace (flare/verm/spire parametric 3D generation; snug-fit rule verm=1/flare; Blender geo nodes + TouchDesigner; Blender/TouchDesigner files on Patreon) (first seen 2026-10-04, status WATCH; seen again 2026-10-05)
- ComfyUI custom nodes wrapping intake/ stages (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-05) **TRENDING**

Analyst note: several rows above matched on the generic "Blender" token only
(Squishy Volumes, ribbon cables, Light Wrangler, HBLink, Raup shell, GPT Astra,
Codex CLI/MCP rows) and are weak signals for this run, not genuine
reappearances. The two strong reappearances are **AI video generation via
Minimax H3** (OmniChar's tested backend) and **ComfyUI custom nodes wrapping
generation stages** (the OmniChar node pack itself).

## New watchlist additions (2026-10-05)

Appended to `references/tooling-watchlist.md` (append-only):

| Date seen | Tool / stage | Seen in | Status | Note |
|-----------|--------------|---------|--------|------|
| 2026-10-05 | OmniChar/.char portable character format + ComfyUI-Omnichar node pack | r/comfyui ".char model" (ashishsanu) | BACKLOGGED | Scored-identity acceptance-spec pattern (sface + DINOv2 face score, locked description, optional LoRA); template for the P1 AI-vendor acceptance-spec gap; GPL-3.0 |
| 2026-10-05 | Marigold V2 single-photo depth estimation (Apache 2.0, commercial OK) | r/comfyui "Vathography" (karijoart) | WATCH | Native ComfyUI implementation; Blender Color Ramp remap recipe for depth-as-artwork |
| 2026-10-05 | Flux klein 9B/4B distilled variants + CCTech/Flux Klein ComfyUI node pack | r/comfyui "Flux klein+YEDP" + Omnichar README | WATCH | 1 MP identity-consistent run on 16 GB VRAM where raw refs OOM'd past 0.8 MP |
| 2026-10-05 | YEDP Action Director (ComfyUI 3D viewport; Mixamo/FBX/GLB; OpenPose/Depth/Canny/Normal/Shaded/Alpha passes) | r/comfyui "Flux klein+YEDP" | WATCH | Smart bone-name normalization is retargeting-adjacent prior art; does NOT fill the P1 rig gap |
| 2026-10-05 | Hillaire LUT-based atmosphere rendering (EGSR 2020) + TropoPlate plate-tectonics planet sim | r/proceduralgeneration TropoPlate (HabitableZone_) | WATCH | Cheap art-directable atmosphere; tectonic sim detail in author's prior post |
| 2026-10-05 | One-seed asset-less procedural game construction | r/proceduralgeneration PROJECT: ABSOLUTELY NORMAL (Inevitable-Cash8506) | WATCH | Boxes/spheres/cones code-built at startup; sine-wave audio synthesis; font the only external asset |
| 2026-10-05 | Ink Fauna sumi-e procedural creature system (TypeScript + Canvas 2D) | r/proceduralgeneration "Ink Fauna" | WATCH | Speed-reactive brush strokes; DEPTH-LIMITED audit (no workflow detail) |

## Depth-escalation usage

- Mode: `pre-approved`, allowance 2 media downloads.
- Downloads attempted: 0. Downloads succeeded: 0. Skipped on approval gate: 0.
- Both YouTube videos carried full captions (17 manual segments for the intro,
  80 ASR segments for the Blender tutorial), so no download was needed to reach
  FULL depth. The four native Reddit clips carry their tooling signal in post
  text and comments per the skill; a media download would not have added
  workflow detail to any of them.

## Non-goals (found but correctly skipped)

- Vathography as an art practice: the artwork is photography, not a game
  pipeline. Only the Marigold-V2-plus-Blender-remap recipe transfers.
- Ink Fauna beyond the stack note: 2D web demo with no repo fit and no
  workflow detail.
- The Google Drive workflow binary in the Flux klein+YEDP post: not opened
  (binary workflow JSON, no tooling signal in the post text).
- TropoPlate's Discord invite: community link, not tooling.
- r/gameassets coverage: Arctic Shift returned HTTP 422 for the subreddit this
  run; its video posts went unscanned (same failure as 2026-10-04).

## Publishing

Staged in `~/workspace/video-tooling-scout-public/` as ready-to-publish (browser
upload when Ehsan is present; never unattended):
- 3 new skills: `skills/omnichar-portable-characters/`,
  `skills/vathography-depth-remap/`, `skills/one-seed-procedural-game/`
  (audits #4-#6 stay in this report only: PARTIAL/DEPTH-LIMITED with no
  extractable workflow).
- Full report: `docs/scout-reports/have-vs-need-2026-10-05.md` (+ README index row).
- Watchlist mirror synced: `video-tooling-scout/references/tooling-watchlist.md`.
- `skills/README.md` table rows added.
