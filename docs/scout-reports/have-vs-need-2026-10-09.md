# Video tooling scout: have-vs-need 2026-10-09

Run: daily cron `daily-video-tooling-scout`, Fri 2026-10-09 08:18 EDT.
Depth mode: `pre-approved` (max 2 media downloads/run, enabled by Ehsan 2026-09-27).
Depth escalation used: **0 attempted / 0 succeeded / 0 skipped** (all 8 scanned
videos were native Reddit video; per the skill's native-video path the tooling
signal lives in post text + comments, so no download was warranted; the 2
DEPTH-LIMITED audits below note that a media download would add only render
frames, not the node graph, so the allowance was deliberately not consumed).
Scan: `/usr/bin/python3 bin/scan_videos.py 2` over 18 subreddits, Oct 7-9 2026.
Note: r/photogrammetry returned HTTP 422 from Arctic Shift (index-side error,
not a read failure); all other subs scanned. Comments via `bin/fetch_comments.py`
(Arctic Shift; no fallback needed). Videos scanned: 8. Videos deeply analyzed: 6.
Report: `hidden_files/have-vs-need-2026-10-09.md` (goal workspace; the body's
`~/workspace/your_files/video-tooling-scout/` path is stale per goal rules).

## Gap alerts

No extracted tool today directly FILLS a P1/P2 gap. Four near-hits / supporting
evidence items, all worth routing into the gap work:

1. **2d3d P1 import-validation gate (roadmap rec 9), supporting prior art.** mflux
   (ex-Spore procgen dev) plans a *documented schema of custom glb properties* so
   third parties can write their own importers for his Godot procgen output
   (audit #5). Second independent prior art for the same gap after the Godot 4.5
   creature pipeline's JSON frame-manifest (watchlist 2026-10-04, seen again
   today). The pattern converging: schema-first interchange, documented custom
   properties, not just code.
2. **Desktop City P1 shader-driven skyline fill, design template.** Petrundiy2's
   procedural galaxy pipeline (audit #4) is built on a far/near crossfade:
   volumetric glow at distance (billions of stars can't be stored), resolved
   stars on approach, glow energy preserved through the transition. That is the
   exact LOD philosophy the skyline-fill gap needs: unmodeled far field as
   shader/volume output, resolved geometry near.
3. **Aegis P1 per-asset performance budgets, human-verified datapoint.**
   tramdrey's rowan tree: one texture, 1300 faces, masked-opacity material
   (audit #6). A concrete artist-set budget for a background foliage asset.
4. **Aegis P1 AI-vendor acceptance spec, more failure-mode evidence.** The
   MiniMax H3 character-swap thread documents identity failure modes in the
   wild: extreme seed dependence, poor facial likeness, "first gen works then
   it ignores the swap entirely" (audits #2). OmniChar's scored-identity
   pattern (watchlist, seen again today) remains the template.

## Videos scanned

8 video posts, Oct 7-9 2026, ranked by tooling relevance x engagement:

| # | r/sub | Title | Author | Score/comments | Relevance |
|---|-------|-------|--------|---------------|-----------|
| 1 | Houdini | Building a procedural multi row pave solver in Houdini - Grid and Hex patterns | Plane-Good-6147 | 37 / 2 | 30.7 |
| 2 | comfyui | ComfyUI Tutorial: Character Swap with MiniMax H3 using LORA LOWVRAM Workflow (6GB) | cgpixel23 | 366 / 27 | 27.3 |
| 3 | proceduralgeneration | Apparently this is called Pebblecrete, so I made it as a fully customizable shader in Blender! | Nompen_art | 93 / 7 | 21.9 |
| 4 | vfx | I've been creating a lot of procedural deep space VFX in recent years. Here's some galaxies showreel! | Petrundiy2 | 137 / 17 | 12.7 |
| 5 | proceduralgeneration | How I'm generating a container port in my game | mflux | 148 / 10 | 0.6 |
| 6 | 3Dmodeling | I made a rowan tree for my game | tramdrey | 84 / 17 | 0.3 |
| 7 | Houdini | I know it's a bit early for this kind of stuff but I am allready in the mood | Maxwellbundy | 148 / 10 | 0.6 |
| 8 | proceduralgeneration | Amoeboid cell | DigitCell | 24 / 3 | 0.1 |

#7 (holiday render, no tooling signal) and #8 (clip, no tooling signal) were not
audited: zero-tooling-signal posts are downweighted regardless of engagement.
#5 and #6 scored low on title hits but their comment threads carried real
pipeline detail, so they were audited.

## Audits

---

## 1. "Building a procedural multi row pave solver in Houdini - Grid and Hex patterns" (Plane-Good-6147)

Source: https://www.reddit.com/r/Houdini/comments/1x078ni/building_a_procedural_multi_row_pave_solver_in/ |
native Reddit video (v.redd.it clip) | r/Houdini post 1x078ni (score 37)

Tools used: **Houdini** (version unstated). No plugins named.

This audit reconstructs the workflow from the author's single descriptive
sentence plus the clip, because the two comments ("Thanks!", "nice! nice!")
carry no technique. Every phase below is inference except where quoted; the
node graph is not visible.

Author's full statement: "The flexibility of Houdini's attribute workflow makes
it straightforward to build multi-pattern distributions with real-time topology
updates."

### Phase 1: Scatter distribution points (inference)

**Do**
1. Generate a point cloud over the paving area (inference: grid scatter or a
   subdivided plane's points as the distribution source).
2. Store a pattern selector as a point attribute (inference: e.g. an integer
   `pattern` attribute, 0 = grid row, 1 = hex row).

**Check**
- Spreadsheet: every point carries the pattern attribute before any geometry
  is instanced.

**Why**
The author names the attribute workflow as the enabler; pattern selection must
live on points, not on geometry, so the layout stays editable.

### Phase 2: Multi-row pattern solver (inference)

**Do**
1. For grid rows: offset alternate rows by half a unit in X (running-bond
   logic). For hex rows: stagger rows by half a cell and compress row spacing
   to the hex pitch (inference: `sqrt(3)/2 * cellsize`).
2. Copy paver geometry to points, reading the pattern attribute to pick the
   variant per row.

**Check**
- Viewport: switching the pattern attribute updates the whole layout live
  (the author's "real-time topology updates").

**Why**
Row-based patterns are 1D offsets applied per row; expressing the offset as a
function of the row index (an attribute) is what makes grid and hex the same
solver with different constants.

### Phase 3: Paver instancing (inference)

**Do**
1. Instance (not copy) the paver geometry onto the solved points so topology
   updates stay cheap.

**Check**
- Point count vs drawn geometry: instancing keeps the scene responsive while
  the solver re-runs.

**Why**
Real-time updates only survive if the per-frame work is transform updates,
not geometry rebuilds.

### The human method, distilled
1. Put the design decision in attributes, keep geometry dumb (author's words:
   "the flexibility of Houdini's attribute workflow").

**Depth status:** DEPTH-LIMITED (author gave one sentence; both comments
vacuous; clip shows the render, not the network). A media download would add
render frames only, not the node graph; FULL depth needs the .hip file or a
network screenshot from the author. The pre-approved download allowance was
not consumed here for that reason.

---

## 2. "ComfyUI Tutorial: Character Swap with MiniMax H3 using LORA LOWVRAM Workflow (6GB)" (cgpixel23)

Source: https://www.reddit.com/r/comfyui/comments/1wzy0w2/comfyui_tutorial_character_swap_with_minimax_h3/ |
native Reddit video (tutorial) | r/comfyui post 1wzy0w2 (score 366, 27 comments)

Tools used: **ComfyUI**, **MiniMax H3** (video model), **Character Swap LoRA**,
**Qwen3VL-32B-minimax Q2.gguf** (CLIP, named in comments as a dependency ask).
Comment-thread alternatives: **wan2gp**, **LTX 2.5**, **Qwen Image 2.1**,
**RefMods** (named as the current meta).

This audit reconstructs the exact workflow from the author's post text and the
27-comment thread. The tutorial video's node graph itself was not visible, so
node-level wiring is inference; every parameter and quoted principle below is
sourced.

Author's recipe, quoted: "new ComfyUI workflow for video character swapping
using MiniMax H3 + Character Swap LoRA, and the main advantage is that it works
**without masking**, which can significantly reduce VRAM usage and simplify the
process. The workflow generates at **0.4 MP in just 8 steps**."

### Phase 1: Assemble the low-VRAM stack

**Do**
1. Load the MiniMax H3 video model in ComfyUI with the Character Swap LoRA.
2. Load the Qwen3VL-32B-minimax Q2.gguf CLIP (commenter Otherwise-Bar-1930
   asked "where do I get the Qwen3VL-32B-minimax -Q2.gguf??? (Clip)": it is a
   named dependency of this workflow class).
3. Skip any masking/segmentation stage entirely. No SAM, no rotoscope.

**Check**
- VRAM: the whole workflow must fit in 6GB (commenter TurbTastic assumes
   "OP has a laptop 3060 which I think has 6GB VRAM"; Netrezen: "Just
   surprised you can even run H3 on less than 8GB VRAM tbh").

**Why**
Masking is the VRAM hog (segmentation model + masked latent bookkeeping).
The LoRA carries the identity signal instead of a mask, so the pipeline sheds
an entire model.

### Phase 2: Identity carrier, character sheet vs LoRA

**Do**
1. Choose the identity carrier: either train a Character Swap LoRA, or use a
   character sheet. Commenter ImpressiveStorm8914's breakdown, quoted:
   "they are a collection of images, stored in a single .safetensor file and
   you load that into Comfy instead of 1 or more reference images or a lora.
   The advantages are, you only load one file per character, creating one
   takes less than a minute (unlike loras), they can offer greater variety
   (emotions, looks etc) over 1 or 2 reference images and character bleeding
   is cut down to a minimum."
2. If using a sheet, include multiple angles; commenter nstern2 warns "OPs
   character sheets are pretty useless since you only see the front of the
   characters."

**Check**
- Sheet contents: front + angles + expressions; a front-only sheet is a known
   weak carrier.

**Why**
One file per character, sub-minute creation, beats per-character LoRA
training; but a sheet is only as good as its coverage. This is the current
community tradeoff, with RefMods named by Netrezen as "what it's all about
now."

### Phase 3: Generate at the low-VRAM operating point

**Do**
1. Render at **0.4 megapixels, 8 steps** (author's numbers).
2. Cap clips at ~5 seconds: commenter Reckless_Venom1507, quoted: "On less
   than 6gb vram u can't go beyond 5 seconds and 0.4 MP."

**Check**
- Output: does the swap hold for the full 5 seconds? Known failure modes
   from the thread: "Poor facial likeness in my tests" (frogsty264371);
   "the first gen works and then it just ignores the swap entirely"
   (stonebloomers); "kept turning the woman into a guy wearing an orange
   shirt and hat" with no prompt reference to a man/shirt/hat (blimey4).

**Why**
At 6GB the operating envelope is 5s / 0.4MP / 8 steps. Pushing past any one
of those is where identity breaks down.

### Phase 4: Fight seed dependence and drift

**Do**
1. Expect to hunt seeds. Commenter fsocietyARG, quoted: "Seems its VERY seed
   dependant, i Once tried this same lora and after several (i mean SEVERAL)
   attempts i found only a working seed."
2. Anti-drift trick (commenter TurbTastic, quoted): "Have you tried injecting
   the reference video latent into the latent that's going to the sampler?
   That way it starts sampling with the reference video latent instead of an
   empty latent, and that can help to avoid drift like when they go out of
   sync with their motions."

**Check**
- Identity across the clip: faces must not morph or swap back mid-shot.

**Why**
Empty-latent starts let the model drift off the reference motion; seeding the
sampler with the reference latent anchors both motion and identity.

### Phase 5: Know the low-VRAM alternatives

**Do**
1. If ComfyUI OOMs, try **wan2gp**: commenter nstern2, quoted: "I find that
   wan2gp works better for video stuff than comfyui ever does, especially
   for low vram cards."
2. nstern2's start-frame trick, quoted: "start with a good starting image.
   Use something like qwen image 2.1 and image to image generate your
   character in the same pose as the original character but keeping the
   background."
3. **LTX 2.5** tier: Reckless_Venom1507, quoted: "If I had 12 gb vram I
   wouldn't be using LTX 2.5, for now I am. It is fast definitely faster
   than 2.3 but loses the faces within a second if it has some movements,
   for talking videos it's good."

**Check**
- Pick the tool by VRAM: 6GB = H3 no-mask recipe or LTX 2.5 (talking heads
   only); 12GB+ = full H3 workflows.

**Why**
Low-VRAM video is a tiered market, not one workflow: speed (LTX 2.5),
quality-per-VRAM (H3 no-mask LoRA), and wrapper convenience (wan2gp).

### The human method, distilled
1. Delete the most expensive stage instead of optimizing it (no masking at
   all, not faster masking).
2. The identity carrier is a format decision (LoRA vs sheet vs RefMods),
   made on creation-time cost and bleeding behavior, not model quality.
3. Budget the operating point first (5s / 0.4MP / 8 steps at 6GB); every
   failure in the thread is someone exceeding one of those three numbers.
4. Seed-hunt and latent-anchor; identity is a search problem at this VRAM.

**Depth status:** FULL (author recipe + 27 substantive comments; node-level
wiring is inference-labeled). Variant of the existing
`minimax-h3-character-swap-comfyui` skill (SAM3 color-inversion workflow):
same tool, different workflow, hence a new variant skill.

---
## 3. "Apparently this is called Pebblecrete, so I made it as a fully customizable shader in Blender!" (Nompen_art)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x082j7/apparently_this_is_called_pebblecrete_so_i_made/ |
native Reddit video (v.redd.it clip) | r/proceduralgeneration post 1x082j7 (score 93, 7 comments)

Tools used: **Blender** (shader nodes, inferred; author did not name the
editor, but "shader" + Blender-subjacent post + "fully customizable" points to
a node-group shader; labeled inference).

This audit is thin by necessity: the post has no text and the 7 comments are
reactions ("Would you mind sharing how you did it and/or the sourcecode?",
"this looks so tactile", nostalgia about pebblecrete planters). No parameters
were disclosed.

### Phase 1: Exposed-aggregate surface model (inference)

**Do**
1. Build the pebble population procedurally (inference: Voronoi cells or
   distributed instances for the aggregate stones; per-pebble color/size
   variation).
2. Build the matrix (the concrete/binder between pebbles) as a separate
   shading domain.

**Check**
- Close-up: individual pebbles read as embedded stones with their own
   albedo, not as noise on flat concrete.

**Why**
Pebblecrete (exposed aggregate) is two materials in one surface: the recipe
must keep pebble and matrix separable so each is art-directable, which is
what "fully customizable" promises.

### Phase 2: Expose parameters (inference)

**Do**
1. Promote pebble size, density, color palette, matrix color, and grout depth
   to shader inputs (inference: a node group with exposed sockets).

**Check**
- One slider changes pebble scale across the whole surface without breaking
   the embedding.

**Why**
A material recipe earns "fully customizable" only if the art-directable
knobs are top-level inputs, not buried nodes.

### The human method, distilled
1. Name the real-world material first ("apparently this is called
   Pebblecrete"), then match its structure (aggregate + matrix), not just
   its look.

**Depth status:** DEPTH-LIMITED (no workflow detail; source code asked for
but not shared). A media download would add render frames only. No skill:
thin evidence stays in the report.

---

## 4. "I've been creating a lot of procedural deep space VFX in recent years. Here's some galaxies showreel!" (Petrundiy2)

Source: https://www.reddit.com/r/vfx/comments/1wzzgux/ive_been_creating_a_lot_of_procedural_deep_space/ |
native Reddit video (showreel) | r/vfx post 1wzzgux (score 137, 17 comments)

Tools used: **Blender** (Geometry Nodes + shader editor; creator-confirmed).
Creator: Petrundiy2, tutorials at https://youtube.com/@astrodemiurgevfx.

This audit reconstructs the pipeline from the creator's own answers across
the comment thread. The exact node graphs are not shown (inference-labeled);
every technique and number below is quoted or directly paraphrased from the
creator.

Author's framing, quoted: "I'm most proud of the setup for barred spiral
galaxies, as well as the deep-field gravitational lensing (check out the
ellipticals in the last flyby!)"

### Phase 1: Galaxy presets as node monsters

**Do**
1. Build each galaxy type (barred spiral hardest) as a Geometry Nodes +
   shader preset. Creator, quoted: "I was working on a procedural galaxy
   generator for Blender for a long time, and each galaxy preset consists of
   geometry nodes and shader parts. The hardest ones contain ~1500-1600
   nodes overall."

**Check**
- Preset count vs node count: complexity lives in the preset, not in
   per-shot work.

**Why**
~1500-1600 nodes per preset is the cost of entry for astro-grade realism;
the investment amortizes because every shot reuses presets.

### Phase 2: Two representations, split by role

**Do**
1. Stars: point clouds. Nebulae/glow: volumes. Creator, quoted: "Point
   clouds for stars and volumes for pretty much everything else."

**Check**
- Star fields stay as points until render; never mesh them.

**Why**
Points are the cheapest carrier for millions of unresolved light sources;
volumes are the cheapest carrier for soft emission. One representation per
physical role.

### Phase 3: Distance-based crossfade (the core method)

**Do**
1. Far field: render the galaxy's total glow as a volumetric material.
   Creator, quoted: "the overall glow of a galaxy from a distance is
   determined by billions of stars. A computer is physically incapable of
   creating and storing such a large number, so the overall glow is
   determined by a volumetric material."
2. On approach: fade in resolved stars while the background volume fades,
   preserving total glow energy. Creator, quoted: "as one approaches,
   resolved stars should appear, while the background fades, and ideally,
   the overall glow energy should be preserved. This is a delicate matter."
3. Note the resolution floor: "at certain distances, resolved stars cannot
   be seen at all; they are too small. At other distances, they appear (and
   this is partially implemented in my setup). The next task is to fade the
   background and do so in a way that it eventually transforms into stars."

**Check**
- Flythrough: brightness must not pop at the crossfade distance; total
   emitted energy stays constant across the transition.

**Why**
You cannot store billions of stars, so the far field must be a statistical
glow and the near field must be discrete stars; the crossfade between them
is the whole technique, and energy preservation is what makes it invisible.
Proceduralism gives "literally infinite detail on any scale" (creator), so
the crossfade never runs out of resolution, only out of careful tuning.

### Phase 4: Gravitational lensing as real 3D

**Do**
1. Spawn refractive meshes on elliptical galaxies; scale the effect strength
   with galaxy size. Creator, quoted: "The gravity lensing is a 3D effect.
   I spawned a bunch of tricky refractive meshes on elliptical galaxies,
   and the strength of the effect depends on the size of the galaxy."

**Check**
- Ellipticals in the last flyby: background visibly warps around them
   (the shot the author is "most proud of").

**Why**
A 2D post trick would break on camera moves; refractive meshes keep the
lensing correct from any angle, which is what sells the deep-field flyby.

### Phase 5: Deep field as instanced scattering

**Do**
1. Instance the procedural galaxy presets as points scattered inside
   filament-like density structures ("domains").
2. Add cosmological redshift to the instanced galaxies.

**Check**
- Large-scale structure: galaxies cluster along filaments, not uniformly.

**Why**
The universe has structure at every scale; instancing presets into
filament domains reuses the Phase 1 investment to fill a deep field.

### Phase 6: Flythrough finishing

**Do**
1. Allow flying into/through galaxies (the setup supports it).
2. Keyframe the brightness of emissive regions for realism on approach.
   Creator, quoted: "You definitely can fly into or through them, but I
   think you'll have to keyframe the brightness of emissive regions a bit
   to make it more realistic. The scaling of these effects are a hard part."

**Check**
- A veteran astronomer-VFX commenter (Redd411, ex-LightWave hypervoxels)
   gave one nitpick: "point star sizes/luminosity could use a bit more
   randomness and distribution bit more organic."

**Why**
Procedural scale-invariance gets you 95%; the last 5% is hand-tuned
exposure and organic distribution jitter.

### The human method, distilled
1. Split the problem by physical role (points for stars, volumes for glow),
   never by what is convenient to model.
2. When the true count is unrepresentable (billions of stars), render the
   statistic (volumetric glow), then crossfade to instances with energy
   preserved.
3. Do lensing in 3D or not at all; camera moves expose 2D tricks.
4. Build presets once (~1500 nodes), instance everywhere (filament domains).

**Depth status:** FULL (creator's technique answers + numbers + principles;
exact node wiring is inference-labeled).

---

## 5. "How I'm generating a container port in my game" (mflux)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1x088up/how_im_generating_a_container_port_in_my_game/ |
native Reddit video (v.redd.it clip) | r/proceduralgeneration post 1x088up (score 148, 10 comments)

Tools used: **Godot** (creator-confirmed: "It's Godot. Love this engine."),
**glTF/GLB** interchange (planned). Game: "Ultrapolis", a cyberpunk diorama
"like Townscaper and tiny glade". Creator: mflux, "long time developer of
all things procgen, way back during the days of processing, then working on
Spore, then 'cyberpunk city simulator'."

### Phase 1: Procedural port generation in-engine

**Do**
1. Generate the container port procedurally inside Godot (the video's
   breakdown, per commenter Loud_Campaign5593: "this is really well broken
   down. i love to see the logic behind procedural gen").
2. Use shader tricks where geometry would be wasteful: decals and interior
   mapping (creator-confirmed as the non-1:1 features).

**Check**
- In-engine: does the port read as a working container terminal at diorama
   scale?

**Why**
Diorama scale (Townscaper-like) means the camera never gets close enough to
justify modeled interiors; decals + interior mapping buy the detail for
free.

### Phase 2: Schema-first export

**Do**
1. Plan scene export as bundles of glb files carrying custom properties.
2. Document the schema (custom property names, meanings, value ranges) so
   third parties can write their own importers. Commenter zante2033's
   suggestion, endorsed by the creator: "your own bundle can contain a bunch
   of glb files, which have their own custom properties you can document...
   Saves you working too hard on collapsing everything to geometry. Let
   people make their own importers."
3. Creator's commitment, quoted: "Yes I plan to add this. Some features are
   shader tricks so it won't be 1:1 (decals and interior mapping) but I will
   try my best."

**Check**
- A third party can write an importer from the documentation alone, without
   asking the author.

**Why**
Documenting the interchange schema is cheaper than collapsing everything to
baked geometry, and it turns the procgen output into a platform others can
build on. Honesty about the lossy parts (shader tricks don't round-trip)
is part of the schema.

### The human method, distilled
1. Generate in the engine the game ships in (Godot), not in a DCC.
2. Fake with shaders what the camera will never inspect (decals, interior
   mapping).
3. Export as documented data (glb + custom-property schema), not as frozen
   geometry; let others write importers.

**Depth status:** FULL (creator's engine, game, export plan, and shader
tricks all stated; in-video generation steps are inference-labeled).

---

## 6. "I made a rowan tree for my game" (tramdrey)

Source: https://www.reddit.com/r/3Dmodeling/comments/1wzwy7c/i_made_a_rowan_tree_for_my_game/ |
native Reddit video (v.redd.it clip) | r/3Dmodeling post 1wzwy7c (score 84, 17 comments)

Tools used: **Photoshop** (default hard-edge brush), game engine with
**masked-opacity material** (engine unnamed). Numbers: **one texture, 1300
faces**.

### Phase 1: Draw the leaves

**Do**
1. In Photoshop, draw leaf clusters with the default hard-edge brush.
   Creator, quoted: "Didn't use something special I think. This is a default
   hard edge brush in photoshop I used for drawing."

**Check**
- Leaf edges are crisp in the bitmap; no soft anti-aliased fringes.

**Why**
The crispness of the final in-engine leaf is decided at draw time: a hard
brush bakes the silhouette the alpha mask will later cut.

### Phase 2: Build the tree from cards

**Do**
1. Model the tree as alpha cards (textured planes), "one of the most popular
   tree modeling technique" (creator).
2. Keep the whole tree to one texture and 1300 faces (creator: "Yep! One
   texture, 1300 faces.").

**Check**
- In-engine with masked opacity: "when you setting the material use masked
   opacity - it also makes the edges hard in the engine" (creator).

**Why**
Masked (alpha-test) opacity keeps the hard drawn edges hard in the engine;
alpha blending would soften them and add sort-order cost. One texture =
one draw call class; 1300 faces = a solved budget, stated, not estimated.

### Phase 3: Know when cards are enough

**Do**
1. Do not attach every leaf and branch for physics. Creator, quoted: "In
   most cases you don't need separate leaves for your tree, but it depends
   on your style and wishes. But the only situation where you need to attach
   every leaf and branch to each other is when you simulate real tree
   physics, but I can't imagine who needs it in the game :D."

**Check**
- Ask: does anything in the game simulate this tree? If no, cards stand.

**Why**
Per-leaf geometry is a physics requirement, not a visual one; paying it
for looks alone is pure waste ("All this modeling stuff is pure magic in
the details tbh").

### The human method, distilled
1. The default brush is enough; crispness comes from the alpha-cut
   discipline, not the tool.
2. State the budget as numbers (1 texture, 1300 faces), not adjectives.
3. Geometry follows simulation need, never visual ambition alone.

**Depth status:** FULL (exact tools, brush, material mode, tri/texture
budget, and quoted principles all from the creator).

---
## Per-repo have-vs-need

### Aegis (primary)

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|------------|----------|--------|---------------|----------------|
| MiniMax H3 no-masking character-swap LoRA recipe (ComfyUI) | #2 | NEED | No AI-video stage; `intake/` is concept-to-input only | watchlist (trailer bucket; BACKLOGGED row added) |
| Character sheets (.safetensors identity bundles) / RefMods | #2 | PARTIAL | No scored-identity acceptance; OmniChar row is the template | backlog: fold into P1 acceptance-spec gap work |
| Reference-latent injection anti-drift trick | #2 | NEED | No video-gen stage at all | watchlist (folded into the H3 recipe row) |
| Houdini attribute-workflow pave solver (grid/hex) | #1 | NEED | trellis-pipe has no attribute-driven distribution/tiling stage | watchlist: solver pattern for tiling/repeat-structure stages |
| Pebblecrete exposed-aggregate shader recipe (Blender) | #3 | NEED | No material-library aggregate recipe; no PBR material policy (verified NEED) | watchlist |
| Procedural galaxy pipeline (GeoNodes, points+volumes, distance crossfade) | #4 | NEED | No astro/VFX stage | watchlist (cinematics bucket) |
| Documented glb custom-property export schema | #5 | PARTIAL | Manifest/provenance conventions exist (`docs/evidence/`, install receipts) but no documented interchange schema for procgen output | watchlist: schema-first interchange pattern |
| Alpha-card foliage recipe (1 texture, 1300 faces, masked opacity) | #6 | NEED | No per-asset perf budgets (verified P1 gap) | adopt as evidence: backlog the perf-budget gap with this as a human-verified exemplar |

### 2d3d

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|------------|----------|--------|---------------|----------------|
| Documented glb custom-property export schema | #5 | NEED | P1 gap: no asset import validation gate (`qa/asset_validate.py`, roadmap rec 9) | **adopt now as reference**: schema-first interchange is the second independent prior art for rec 9 (joins Godot 4.5 creature JSON manifest) |
| Alpha-card foliage recipe (1 texture, 1300 faces) | #6 | NEED | P1 gap: no production-conversion stage for generated meshes (roadmap rec 20) | backlog as reference budget for rec 20 |
| Character sheets / scored identity | #2 | NEED | NEED: generated hawk/boar art (OpenAI no credit; procedural stand-ins) | watchlist: identity-consistency pattern for when generation resumes |
| Procedural galaxy pipeline | #4 | NEED | Projection painting + procedural textures exist; astro VFX out of scope | skip (out of scope), watchlist row kept for Aegis |
| Pave solver / pebblecrete | #1, #3 | NEED | Procedural texture generators exist (`pipeline/proc/make_textures.py`) | watchlist: pebblecrete recipe class could extend make_textures.py |

### Desktop City

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|------------|----------|--------|---------------|----------------|
| Godot procgen city + documented glb export schema | #5 | PARTIAL | Extensive Godot procgen (`tools/city_*`, `street_kit.py`, `procedural_art.py`) but no documented export schema for procgen output | backlog: document a procgen-output schema (same engine, same diorama-city problem as mflux) |
| Galaxy-pipeline distance crossfade (volumetric far / resolved near) | #4 | NEED | P1 gap: shader-driven skyline fill has no equivalent | **backlog as design template** for the skyline-fill gap: far field as shader/volume output, resolved geometry near, energy-preserving crossfade |
| Pave solver (grid/hex attribute workflow) | #1 | PARTIAL | `street_kit.py`, tiling probes exist; no attribute-workflow multi-pattern solver | watchlist |
| Pebblecrete aggregate shader | #3 | NEED | Procedural art tools exist; no exposed-aggregate recipe | watchlist |
| Alpha-card foliage recipe | #6 | PARTIAL | Own trees (`tools/city_trees.py`); technique family matches | watchlist: verify city_trees.py against the 1-texture/masked-opacity discipline |

### Solarempire

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|------------|----------|--------|---------------|----------------|
| Documented glb custom-property export schema | #5 | PARTIAL | `manifest.json` per asset, glTF-as-source-of-truth (direction v1.1 S11), per-class export profiles | watchlist/backlog: custom-property schema complements the manifest convention |
| Alpha-card foliage recipe | #6 | PARTIAL | Per-asset audit + optimization reports with measured figures (e.g. Aurelia Ring Station 3.1M -> 300k tris, silhouette IoU 0.998) | watchlist: same budget philosophy, already practiced |
| Galaxy pipeline / pave solver / pebblecrete | #4, #1, #3 | NEED | Out of pipeline scope | skip |
| H3 character-swap recipe | #2 | NEED | No video stage | skip |

## Gap recommendations (highest-leverage NEEDs)

1. **Desktop City skyline fill <- galaxy crossfade.** The P1 "shader-driven
   skyline fill" gap now has a concrete design template: Petrundiy2's
   far-volumetric / near-resolved crossfade with energy preservation. Next
   step: spike a two-tier skyline in the Godot procgen (impostor/volume tier
   far, authored-building tier near) and measure the crossfade distance where
   the pop disappears.
2. **2d3d import-validation gate <- schema-first interchange.** Two
   independent prior-art points now (Godot 4.5 creature JSON manifest +
   mflux's documented glb custom properties). Next step: when building
   `qa/asset_validate.py` (rec 9), require a written schema of custom
   properties per asset class, not just code checks.
3. **Aegis per-asset perf budgets <- human exemplar.** "One texture, 1300
   faces" for a background tree is the kind of stated budget the P1 gap
   needs. Next step: seed the budget table with human-verified exemplars
   (this tree, the 2026-10-04 Godot creature pipeline numbers) before
   deriving budgets from generated assets.
4. **Aegis acceptance spec <- failure-mode catalog.** The H3 thread's
   failure modes (seed dependence, face drift, first-gen-works-then-ignores)
   belong in the "what good means" spec as explicit must-fail controls.
   OmniChar's scored identity (sface + DINOv2) remains the template.
5. **Aegis foundry tiling <- attribute-workflow solver.** The Houdini pave
   solver pattern (design decisions in attributes, dumb instanced geometry)
   is the candidate shape for any trellis-pipe repeat-structure stage.
   Watchlist for now.

## Explicit non-goals

- **Qwen3VL-32B-minimax Q2.gguf**: dependency note folded into the H3 recipe
  watchlist row, not a tool in its own right.
- **Posts #7 (Houdini holiday render) and #8 (amoeboid cell)**: no tooling
  signal in post text or comments; correctly skipped per the downweight rule.
- **wan2gp / LTX 2.5 as adoptions**: low-VRAM video tiers are bucketed on
  the watchlist; no repo has a video stage to adopt them into.
- **Galaxy pipeline for 2d3d/Solarempire**: out of pipeline scope; kept on
  the watchlist for Aegis cinematics only.

## Watchlist trending

Curated from `references/tooling-watchlist.md` (the trend script's token
overlap produced 27 spurious "seen again" hits on generic tokens like
"blender"/"houdini"; those were reverted, and the four genuine reappearances
below were annotated by hand):

- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27,
  WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-03,
  2026-10-05, 2026-10-08, 2026-10-09) **TRENDING** (7 sightings; today's
  ComfyUI thread is the latest)
- comfyui-minimax-h3-studio (first seen 2026-10-03, BACKLOGGED; seen again
  2026-10-09) (today's no-masking LoRA recipe is the same problem class,
  different workflow)
- OmniChar/.char portable character format (first seen 2026-10-05,
  BACKLOGGED; seen again 2026-10-08, 2026-10-09) **TRENDING** (character-sheet
  identity-carrier debate maps directly onto it)
- Godot 4.5 .NET procedural creature pipeline (first seen 2026-10-04, WATCH;
  seen again 2026-10-09) (mflux's glb schema joins its JSON manifest as
  P1 import-validation prior art)

New rows appended (9): MiniMax H3 no-masking character-swap LoRA recipe;
Houdini multi-row pave solver; pebblecrete aggregate shader; procedural
galaxy generator (Blender); Ultrapolis Godot procgen + glb export schema;
Photoshop alpha-card foliage; wan2gp; LTX 2.5; Qwen3VL-32B-minimax Q2.gguf.

## skill_library artifacts staged

In `~/workspace/video-tooling-scout-public/` (ready to publish; browser
upload happens with Ehsan present, never unattended):
- New variant skill: `skills/minimax-h3-character-swap-nomask-lowvram/`
  (same tool as `minimax-h3-character-swap-comfyui`, no-masking LoRA workflow)
- New skills: `skills/procedural-galaxy-generator-blender/`,
  `skills/godot-procgen-city-glb-export-schema/`,
  `skills/handdrawn-foliage-alpha-cards/`
- Full report copied to `docs/scout-reports/have-vs-need-2026-10-09.md`;
  `docs/scout-reports/README.md` index updated
- Watchlist synced to
  `video-tooling-scout/references/tooling-watchlist.md`; README skills
  table + count updated
- DEPTH-LIMITED audits (#1 pave solver, #3 pebblecrete) stayed in the report
  only, never padded into skills/

## Run notes

- Arctic Shift: r/photogrammetry HTTP 422 (index-side; not a read failure).
  Old-Reddit/PullPush fallback not needed (Arctic Shift returned comments).
- No approval gates hit anywhere in this run; no processes killed.
- Next run: same 2-day window cadence; watch for mflux's glb schema doc and
  any pebblecrete source-code release (both promised in comments).
