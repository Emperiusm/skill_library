# Video tooling scout — have-vs-need, 2026-10-30

Depth mode: `pre-approved` (max 2 media downloads per run, Ehsan 2026-09-27).
Depth-escalation usage this run: **0 downloads attempted, 0 succeeded, 0 skipped**.
All 8 deep-analyzed videos are native Reddit video (v.redd.it); the deepened
download pipeline applies to YouTube/Vimeo, and no YouTube/Vimeo video made
the top-8 cut this run, so the allowance was not needed.

**YouTube source: DOWN for this run.** `bin/scan_youtube.py 2` scanned all 11
channels (RyanKingArt, DefaultCube, Ducky3D, JoshGambrell, MaxHayArt,
BlenderSecrets, GDQuest, KaizenTutorials, Brackeys, Entagma, OlivioSarikas)
and returned 0 videos: every channel failed with
`SSL: CERTIFICATE_VERIFY_FAILED (self-signed certificate in certificate chain)`
via yt-dlp — the sandbox egress proxy MITM issue from AGENTS.md, not a
channel problem. Continued with Reddit only per the skill; a dead source
never blocks a run.

## Gap alerts

One genuine gap match this run (P2):

- **agentY** (free, MIT-licensed AI agent that lives inside ComfyUI) matches
  the P2 gap **"MCP-driven DCC loop (agents drive Blender/UE, iterate
  visually)"** by meaning. agentY ships **MCP presets for Blender, Maya,
  Houdini, and After Effects** (github.com/szprivate/agentY, MIT, Windows and
  Apple Silicon), runs on cheap/local LLMs (Qwen, DeepSeek, Ollama, Strata),
  builds workflows it has never seen from web research, and judges its own
  outputs against the brief, re-rendering what misses. This is the most
  concrete, free, agent-in-DCC pipeline evidence to date for that P2 row,
  and it should move the Blender-MCP spike from "prior art" to "try this
  one first."

No P1-gap matches this run.

## Videos scanned and deeply analyzed

Reddit scan: 42 video posts across 23 subreddits, last 2 days (2026-10-28 to
2026-10-30), min score 20. 28 URLs were new since the 2026-10-29 scan.
YouTube scan: 0 videos (source down, see above).

Deep analysis (8 cap; native Reddit video -> full post text + top comments):

| # | Video (title) | Creator | Source | Sub | Depth |
|---|---------------|---------|--------|-----|-------|
| 1 | A 1:1 Earth-scale procedural planet, from orbit to a beach in a single frame | Fresh-Daikon-9408 | v.redd.it/o4qzk7ja1hyh1 (score 213, 41 comments) | r/proceduralgeneration | FULL |
| 2 | Tired of writing prompts? Or using expensive agents? #OpenSourceHiggsfield | u/Admirable-Agency-578 (posts agentY by szprivate) | v.redd.it/myx5e5kp3gyh1 (score 67, 3 comments) | r/comfyui | FULL (author post text) |
| 3 | Diffusion Models for Procedural Cities | bart1259 | v.redd.it/ms31kghwdfyh1 (score 189, 23 comments) | r/proceduralgeneration | FULL |
| 4 | Production-ready 3D heads with MetaHuman topology from photos (KeenFace) | nord_little (KeenTools) | v.redd.it/h9s9os0asdyh1 (score 67, 25 comments) | r/vfx | FULL (author post text + demo feedback) |
| 5 | Update on the forest environment I posted earlier | PerceptionCharming | v.redd.it/5v8577fvyfyh1 (score 51, 11 comments) | r/threejs | FULL (author post text; numbers, no code) |
| 6 | Draconia Malfoy [Malfoid] - Female Draco Fanart | I-HAYDEN-I | v.redd.it/ya3wurewhfyh1 (score 118, 38 comments) | r/3Dmodeling | PARTIAL (author workflow named, no parameters; comments are off-topic drama) |
| 7 | So I can't draw, but at least the pixels don't rotate. | ScalableVectorShapes | v.redd.it/qqxk1r2uihyh1 (score 191, 16 comments) | r/godot | PARTIAL (post text + author comment; no source for the DynamicOutline2D node) |
| 8 | God simulator built with Claude Code | Dependent-Block-1319 | v.redd.it/wv33ej245kyh1 (score 46, 27 comments) | r/aigamedev | NO-TOOLING (only "used Claude Code" named; no workflow) |

## 1. "A 1:1 Earth-scale procedural planet, from orbit to a beach in a single frame" (Fresh-Daikon-9408)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xiw889/a_11_earthscale_procedural_planet_from_orbit_to_a/ | native Reddit video | r/proceduralgeneration post 1xiw889 (score 213)

Tools used: custom C++ 3D engine written from scratch (started as a 2012
Unity prototype; author: "No I am not using Blender anymore, this is a c++
3D engine from scratch"); libnoise "complex planet" example **ported to
HLSL**; compute shaders; multi-layered coherent noise (Perlin, ridged
fractal); double-precision camera positioning.

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: **the terrain is a function, not
data — every frame the compute shader rebuilds exactly the geometry the
view needs, from scratch.**

### Phase 1: Get a sphere from a displaced cube

**Do**
1. Build a sphere from a subdivided cube.
2. Displace it with a single Perlin noise layer.
3. (Author's starter recipe, given as advice): next add fractal noise
   (fBm, ridged) for mountains; then add camera-following LOD
   (quadtrees or clipmaps); then move the noise into a compute shader.

**Check**
- From orbit: does the planet read as a planet with relief, not a golf ball?
- Fly down: does the near field resolve without popping?

**Why**
"Getting one continuous scale from orbit to the ground was the whole
point." The two walls the author hit in 2012 were (a) rebuilding meshes
fast enough to show both the far horizon and the ground under the camera,
and (b) floating-point precision at planetary scale.

### Phase 2: Stack coherent noise over the whole sphere

**Do**
1. Take libnoise's "complex planet" example as the noise-stack base.
2. Port the stack to HLSL: multi-layered coherent noise (Perlin,
   ridged fractal, others) for mountain ranges, plains, oceans.
3. Evaluate per vertex in the planet's fixed frame: "you stack some
   coherent noises (perlin noise, ridged fractal noises, others) then at
   each frame you pass vertex coordinates into this stack, and it gives
   you elevated coordinates."

**Check**
- Sample landmarks the author used: buttes, mesas, a gorge cut into a
  plateau, close-up rock. Do the landforms vary beyond one noise look?

**Why**
There is **no pre-generated planet** and **no stored terrain at all**.
Every point on the sphere is an elevation function of noise layers;
everything else (vegetation, forests, snow, sand) sits on top of it.

### Phase 3: Rebuild the view's geometry every frame — no tiles, no streaming

**Do**
1. Each frame, a compute shader builds **one grid**: a cube face centred
   under the camera, projected onto the sphere.
2. Make it nested rings that **double in size outward** (geometry clipmaps
   on a sphere): dense near the camera, coarse far away. "No quadtree,
   no chunks. It's a single grid centred under the camera, with nested
   rings that double in size outward."
3. Recompute heights on the GPU per vertex through the noise stack:
   "Each frame, a grid around the camera, dense nearby and coarse far
   away, asks that function for its heights on the GPU."
4. Budget: **around 700 to 1,100 rings, under a million vertices.**

**Check**
- Move the camera fast: the ship can go "from the Sun to the Earth in a
  second and the terrain keeps up." If detail lags behind the camera,
  the per-frame rebuild is too slow.
- Watch for popping while zooming: there should be none, because there
  is no tile to split, merge, or stream.

**Why**
"Speed costs nothing that way: there's nothing to stream, so nothing
can lag." The classic planetary-engine problem (streaming + refining
meshes progressively) is sidestepped by rebuilding from the function
each frame.

### Phase 4: Hold precision and kill shimmer

**Do**
1. Evaluate each vertex in the planet's **fixed frame**, with the **camera
   position in doubles** to stay precise at planetary scale.
2. **Filter out noise octaves finer than the local mesh cell**, so the
   far mesh doesn't shimmer.
3. Derive normals from neighbouring vertices.
4. Add fine detail (rock, sand) **in the pixel shader, not the mesh**.

**Check**
- Orbit view: does the far horizon shimmer? If yes, an octave slipped
  through the cell-size filter.
- Ground level: do fine surface details hold up when the mesh is coarse?

**Why**
Precision and anti-aliasing are done mathematically, not with more
geometry. The author is honest about the gap: "the large-scale relief is
still a noise stack, with no tectonic plates behind it, so the features
don't nest the way real landscapes do." Next step is a **drainage pass
that traces rivers and watersheds from the relief**, already following
valleys, meant to drive coasts, vegetation, and clearings top-down.

### The human method, distilled
1. **Delete the pipeline stage that hurts.** Streaming, chunking, and
   LOD-splits were the 2012 walls; the author removed the concept
   ("no quadtree, no chunks") instead of optimizing it.
2. **Order of attack, stated verbatim:** "1. a sphere from a subdivided
   cube, displaced by one Perlin noise; 2. fractal noise (fBm, ridged)
   to get mountains; 3. a level of detail that follows the camera (look
   up quadtrees or clipmaps); 4. then move the noise to a compute
   shader."
3. Read a good base (libnoise's complex planet) rather than designing a
   noise stack from scratch.
4. Admit the gap plainly: noise stack without tectonics means features
   don't nest like real landscapes; the drainage pass is the stated fix.

**Depth status:** FULL (author post text + 41-comment thread with
detailed technical answers; no invented parameters; price/cost not
stated, engine is closed-source side project — "Right now you cannot
try it").

---
## 2. "Tired of writing prompts? Or using expensive agents? #OpenSourceHiggsfield" — agentY (szprivate)

Source: https://www.reddit.com/r/comfyui/comments/1xirbr2/tired_of_writing_prompts_or_using_expensive/ | native Reddit video | r/comfyui post 1xirbr2 (score 67)

Tools used: agentY (github.com/szprivate/agentY), **MIT-licensed**, Windows
and Apple Silicon; ComfyUI (the agent lives inside ComfyUI with its own
image, video, and 3D viewers); any LLM, "including cheap ones like Qwen and
DeepSeek, or fully local and free with Ollama or Strata"; **MCP with
presets for Blender, Maya, Houdini, After Effects, and more**; remotion
(for motion graphics and video editing); Slack integration; built-in
tagging system, project memory, and long-term memory.

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The tool's core method is: **the agent lives inside the DCC-adjacent
workflow tool, plans with memory, builds unseen workflows from web research,
and self-judges outputs against the brief.**

### Phase 1: Run it on cheap or local LLMs

**Do**
1. Install agentY (MIT, Windows / Apple Silicon).
2. Point it at any LLM: Qwen or DeepSeek for cheap, Ollama or Strata
   for fully local and free.

**Check**
- Does the agent still complete a brief on the cheapest backend? The
  product's claim is that it does.

**Why**
"No expensive agents" is the pitch: the agent layer is decoupled from
frontier-model APIs.

### Phase 2: Brief it, let it research

**Do**
1. Give the agent a brief.
2. It "builds workflows it has never seen, from what it finds on the
   web" — i.e. it researches node graphs / workflows online rather than
   only replaying templates.

**Check**
- Ask for a workflow type you know it has never seen; inspect the
  built graph for coherence before running it.

**Why**
(Labelled inference) This is an agent, not a macro recorder: the
workflow-building is the value, and the failure mode to watch is a
graph that looks right but miswires a node.

### Phase 3: Let it judge and re-render

**Do**
1. The agent "judges its own outputs against your brief and re-renders
   what misses."
2. Build "entire agent image generation pipelines with loops and
   pre-planned agent or human reviews, right within ComfyUI."

**Check**
- Review the re-rendered takes against the brief: did the second pass
  fix the miss, or drift?

**Why**
This is the konte pattern from the watchlist (acceptance records,
variants instead of overwrite, explicit review points) shipped as a
product feature rather than a hand-built harness.

### Phase 4: Parallelize per shot

**Do**
1. "Runs several agents in parallel, one per shot if you like."

**Check**
- Check shot-to-shot consistency (identity, style) when running parallel
  agents.

**Why**
Multi-shot throughput without one agent's context window being the
bottleneck.

### Phase 5: Drive the DCCs over MCP

**Do**
1. Enable the MCP presets for **Blender, Maya, Houdini, After Effects**.
2. Use the agent to build motion graphics and edit video via **remotion**.
3. Use the tagging system to reuse images created in the system, and
   project/long-term memory across sessions.

**Check**
- In a DCC, verify the agent's action against the brief before
  accepting: MCP is a two-way door.

**Why**
This is the P2 MCP-driven-DCC-loop gap as a shipped product: an agent
inside the workflow tool, driving the DCCs over MCP, with review points.

### The human method, distilled
1. Free the agent from the expensive model ("cheap ones like Qwen and
   DeepSeek, or fully local and free with Ollama or Strata").
2. Let the agent research before it builds ("builds workflows it has
   never seen, from what it finds on the web").
3. Make judgment explicit: the agent grades its own outputs and
   re-renders what misses; pre-planned agent or human reviews are
   part of the pipeline design.

**Depth status:** FULL (author's full post text; 3 praise-only comments add
nothing. Third-party verification of the MCP presets and the re-render
quality: none yet — author's claims, treated as such.)

---
## 3. "Diffusion Models for Procedural Cities" (bart1259)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xinh91/diffusion_models_for_procedural_cities | native Reddit video | r/proceduralgeneration post 1xinh91 (score 189, 23 comments)

Tools used: **custom diffusion model trained from random weights from
scratch** (not a fine-tune); rasterized OpenStreetMap data of the
Netherlands (rasterization script `02_mill_tiles` in the training folder);
Stable Diffusion VAE (tried for fine-tuning, **abandoned — "VAE decoding
was blurry"**, sensible because SD was not trained on maps); code at
github.com/bart1259/CityDiffusion2; dataset at
huggingface.co/datasets/bart1259/netherlands_512_2m; model at
huggingface.co/bart1259/CityDiffusion2; author's custom editor for building
worlds.

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: **train a diffusion model from
scratch on rasterized map data so it generates city layouts with the
right spatial statistics, then edit and extend them in a purpose-built
editor.**

### Phase 1: Rasterize the map vectors into images

**Do**
1. Take OpenStreetMap vector data for the Netherlands.
2. Rasterize it with the `02_mill_tiles` script (in the repo's training
   folder); "Road networks are also rasterized the same way."
3. Produce 512x512 tiles representing 1km x 1km.

**Check**
- Look at the sample: github.com/bart1259/CityDiffusion2 docs
  training_data.png. Roads, rural/urban/water mixes must be legible as
  pixels.

**Why**
Diffusion on the vector representation is "likely impossible" (author's
own judgment, confirmed by a commenter); pixels are the tractable
representation.

### Phase 2: Train from scratch, not fine-tune

**Do**
1. Initialize a diffusion model **with random weights** and train from
   scratch on the Netherlands dataset ("Pretrained from random weights
   on the dataset" — the author's phrase; read as: no pretrained
   checkpoint used).
2. Predict noise on pixels directly (the latent-noise route was tried
   and dropped).

**Check**
- Author's failure note: fine-tuning Stable Diffusion with its VAE gave
  blurry decodings. If the outputs look map-blurry, the VAE is the
  suspect.

**Why**
SD was "probably not trained on maps"; training the VAE alongside would
have taken too long, so the author changed to predicting noise on
pixels. Honest engineering: pick the representation the models can
actually learn.

### Phase 3: Generate conditioned layouts, extend with context

**Do**
1. Condition generation on rural/urban/water mix settings.
2. Use the author's editor to create custom procedural worlds: the model
   "can generate conditioned on rural/urban/water mix settings and
   extend a map while preserving existing context."

**Check**
- Extend an existing map: does the continuation preserve the existing
  context (roads continue, density matches)?

**Why**
The model is an authoring assistant, not a one-shot generator; the
editor is part of the product.

### Phase 4 (roadmap, author-stated): go vector

**Do**
1. The model currently outputs **only raw pixels** — "only considers a
   1km x 1km area for context so it has no understanding of what roads
   are major or if it should continue a river." (Author's own limitation
   note.)
2. Planned: a mini LLM that generates maps as **vectors**, "so its
   easier to use for downstream applications" (i.e. a game engine can
   consume it). The author is still figuring out "what the training
   objective should look like."

**Check**
- (Inference) Any vector-output attempt should be judged on
  road-network connectivity, not just pixel plausibility.

**Why**
Pixels are a stepping stone; the destination is engine-consumable
vectors. The author is open about the gap: ask the community for
training-objective ideas.

### The human method, distilled
1. **Train bespoke when the domain is off-distribution:** general
   pretrained models (SD) fail on maps; training from scratch on the
   domain data is the answer, and the author says so plainly.
2. **Representations first:** pixels now because diffusion needs them;
   vectors later because engines need them. The ordering is deliberate.
3. **Admit the context limit:** 1km x 1km with no notion of major roads
   or continuing rivers — stated by the author, not discovered by
   critics.

**Depth status:** FULL (author post text + 23-comment technical thread
with the author's detailed ML answers; architecture hyperparameters and
training compute not disclosed).

---
## 4. "Production-ready 3D heads with MetaHuman topology from photos (KeenFace)" (KeenTools / nord_little)

Source: https://www.reddit.com/r/vfx/comments/1xihge4/productionready_3d_heads_with_metahuman_topo | native Reddit video | r/vfx post 1xihge4 (score 67, 25 comments)

Tools used: **KeenFace** (keenface.ai), a new web tool from the KeenTools
team; inputs: reference photos — "a few web grabs or full studio shots,
doesn't really matter"; outputs: head mesh in **native MetaHuman
topology**, full PBR maps (Base Color, Normal, Roughness, Specular),
**clean bald base mesh** (no baked hair or geometry artifacts);
downstream: UE or any DCC for rigging, sculpting, animation.

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: **feed photos, get a head that
slots into an existing MetaHuman pipeline — topology compatibility is
the product, not the reconstruction alone.**

### Phase 1: Collect reference photos

**Do**
1. Gather a few reference photos of the subject: web grabs or full
   studio shots ("doesn't really matter").

**Check**
- Likeness in, likeness out: the author claims "a solid likeness."
  (Inference: photo coverage still matters — front/side angles — but
  the author does not specify a minimum set.)

**Why**
The input bar is deliberately low: casual photos, not a scan rig.

### Phase 2: Run the web tool

**Do**
1. Feed the photos to KeenFace (web tool, installable-locally status
   unknown — one commenter warns "if it's not installable locally, you
   can't rely on it").

**Check**
- Does the head come back with a clean bald base (no baked hair)? The
  author lists this explicitly; one demo user reported the textures
  "produced are really low-res and don't hold up at all" — so verify
  texture resolution before committing.

**Why**
Baked hair and messy artifacts are the failure modes this product
claims to avoid.

### Phase 3: Drop into the MetaHuman pipeline

**Do**
1. Take the head mesh (native MetaHuman topology) into UE or any DCC.
2. Rig, sculpt, or animate as normal — the topology is the compatibility
   guarantee.

**Check**
- The honest objection from the thread: "I'm not gonna have the whole
  studio change our base topology for MetaHuman's one, so 'production
  ready' is a big stretch." Verify the topology fits YOUR pipeline
  before buying.

**Why**
Topology compatibility is the whole value proposition; a studio on a
different base topology gets nothing.

### The human method, distilled
1. **Sell the interface, not the algorithm:** the pitch is "native
   MetaHuman topology," i.e. this fits the pipeline you already have.
2. **Low input bar, high compatibility bar:** casual photos in,
   production topology out.
3. Known community caveats, attributed: texture resolution questioned
   by a demo user; pricing criticized (~$30 for 2 heads, per a
   commenter — vendor pricing not confirmed on-page by this run);
   topology lock-in objection from a studio user.

**Depth status:** FULL (author's full announcement comment with
deliverables list + 25-comment thread including demo feedback and
objections; price and exact mesh specs are single-commenter claims).

---
## 5. "Update on the forest environment I posted earlier" (PerceptionCharming)

Source: https://www.reddit.com/r/threejs/comments/1xiqih2/update_on_the_forest_environment_i_poste | native Reddit video | r/threejs post 1xiqih2 (score 51, 11 comments; comments are feature requests, no tooling detail)

Tools used: three.js; compute shaders (frustum culling); instanced
meshes; Claude (top-down screenshot analysis for godray placement);
cross-billboards; alphaTest materials; procedural ambient/footstep
audio system.

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it),
and **Why** (the principle). The video's core method is: **instance
everything, cull per-instance on the GPU, billboard at distance, and
use cheap tests (alphaTest) instead of expensive blending.**

### Phase 1: Animate cheaply with instancing

**Do**
1. Trees: 500 total, 6 models, each with leaves + log meshes.
2. Add subtle leaf movement, a falling-leaf system, spores in the air,
   and improved fake godrays ("fake light shafts instead of a
   physically accurate effect").
3. Merge all godrays into **a single instanced mesh**; fade them when
   the camera gets near.
4. Place godrays by asking Claude to "take images from top of the map
   and find gaps through trees," then place the shafts on those exact
   spots.

**Check**
- Do the shafts sit in real gaps (no shafts inside trunks)? The
  Claude-placement step is the check.

**Why**
(Labelled inference) Fake light shafts are cheap; placing them in real
tree gaps sells the effect. One instanced mesh keeps the draw calls
flat.

### Phase 2: Cut the frame cost

**Do**
1. Add **frustum culling in compute shaders** so individual instances
   stop rendering when off-screen: "frustum culling to the trees in
   compute shaders which stop individual instances from rendering."
2. Add **cross billboards for distant trees**: "after a certain
   distance, only 4 triangles are rendered per tree."
3. Switch leaf material from **transparent to alphaTest** — "made a
   huge difference."
4. Share materials across the environment to help load time.
5. Result: **8 fps -> 27-35 fps on M1 Mac at max settings** (3-4x
   improvement).

**Check**
- Watch the cross-billboard switch distance in the video ("You might
  see them switching in the video") — if the pop is visible, the
  switch distance is too close.

**Why**
Transparency sorting and per-pixel blending were the cost; alphaTest
is a single comparison. Per-instance culling and 4-triangle billboards
remove geometry the eye can't resolve anyway.

### Phase 3: Ground interaction and audio

**Do**
1. Grass bends and flattens where the player walks and slowly springs
   back, leaving a trail: "just added two spheres with camera and
   attached them to my grass system."
2. Audio: one ambient sound + footstep sounds for mud and grass, each
   with **5 variants selected randomly** so the same sound doesn't
   repeat.

**Check**
- Walk in a loop: does the trail fade naturally? Do footsteps avoid
  obvious repetition?

**Why**
Persistence (trail) and variation (5 randomized variants) are the two
cheap tricks that make a loop feel alive.

### The human method, distilled
1. **Measure the real bottleneck:** 8 fps on M1 Mac at max settings was
   the baseline; the fix order was culling, billboards, then
   alphaTest.
2. **Use AI for placement, not for art:** Claude analyzed top-down
   screenshots to find tree gaps for godrays — a planning task, not a
   generation task.
3. Budget honesty: the video was recorded on an RTX 4080 at 4K with 2x
   pixel density (effectively 8K), "locked at 60fps due to my screen
   refresh rate" — the headline number is display-capped.

**Depth status:** FULL (author's full post text with exact numbers:
500 trees, 6 models, 2 draw calls per tree type + 1 for the billboard,
4 triangles per distant tree, 8 -> 27-35 fps, 5 audio variants; no
code or shader source disclosed).

---
## 6. "Draconia Malfoy [Malfoid] - Female Draco Fanart" (I-HAYDEN-I)

Source: https://www.reddit.com/r/3Dmodeling/comments/1xinv9d/draconia_malfoy_malfoid_female_draco_ | native Reddit video | r/3Dmodeling post 1xinv9d (score 118, 38 comments; comments are franchise-controversy drama, zero tooling discussion)

Tools used: ZBrush (sculpt), Substance (texturing — author says
"textured in Substance"), Blender (render, shaders, compositing).
Pipeline named by the author, no parameters disclosed.

This audit reconstructs the workflow the author named, so another agent
can follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: **an illustrated look from 3D —
mixed PBR with an emissive map blending lights with textures, instead
of a classic PBR render.**

### Phase 1: Sculpt with the folds (ZBrush)

**Do**
1. Sculpt the character in ZBrush; the author focused on improving
   "my sculpt with the folds" (cloth folds on the outfit).

**Check**
- (Inference) Cloth folds read at silhouette and in close-up; check
  both.

**Why**
The author's stated improvement target for this piece.

### Phase 2: Texture in Substance

**Do**
1. Texture in Substance ("textured in Substance").

**Check**
- No parameters disclosed.

**Why**
(Inference) Standard PBR authoring; the stylization happens in the
render, not the texture set.

### Phase 3: Render the illustration mix in Blender

**Do**
1. In Blender, render "a mix of an illustration with 3D rather than
   the classic PBR render."
2. Use "mixed PBR with some emissive map, blending the lights with the
   textures," plus "some shaders and compositing."

**Check**
- Compare against a straight PBR render: the piece should read
  illustrated, not physically shaded.

**Why**
The emissive-map blend is the stylistic choice: light becomes part of
the illustration rather than a physical simulation.

### The human method, distilled
1. Pick one thing to improve per piece (here: cloth folds).
2. Change the look at render time (PBR + emissive mix), not by
   re-authoring the assets.

**Depth status:** PARTIAL (author named the three-tool pipeline and the
core stylistic choice; no brush names, map resolutions, shader node
graphs, or compositing settings disclosed; 38 comments add nothing on
tools). Stays in the report only — no skill (thin evidence; the
ZBrush/Substance/Blender character pipeline is already covered by
existing library skills).

---
## 7. "So I can't draw, but at least the pixels don't rotate." (ScalableVectorShapes)

Source: https://www.reddit.com/r/godot/comments/1xiyqcl/so_i_cant_draw_but_at_least_the_pixels_don | native Reddit video | r/godot post 1xiyqcl (score 191, 16 comments)

Tools used: **Scalable Vector Shapes 2D** (Godot Asset Library, by
renevanderark); author's custom **DynamicOutline2D** tool node (draws
around multiple ScalableVectorShape2D nodes, placed behind the hat and
forehead, uses **Geometry2D.merge_polygons** under the hood);
**Subviewport**; Godot pixel snap.

This audit reconstructs the workflow the author described, so another
agent can follow the same process. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: **draw with vector shape tools and a
compositor, render through a Subviewport with pixel snap — vector
input, pixel-art output, no rotation blur.**

### Phase 1: Draw with shape tools, not pixels

**Do**
1. Build the character from vector shapes (ScalableVectorShape2D nodes)
   instead of drawing pixels by hand.
2. "No Shaders, No AI, just a Subviewport and Scalable Vector Shapes
   2D."

**Check**
- Zoom and rotate: do the pixels stay aligned?

**Why**
The pixels don't rotate because the renderer, not the art, enforces
the grid: "it's really just godot that renders this stuff so well
aligned (as long as the pixel snap is on)."

### Phase 2: Add a merged outline node

**Do**
1. Build (or use the author's) **DynamicOutline2D**: a tool node that
   draws an outline around multiple assigned shape nodes.
2. Place it behind the relevant shapes (author: behind the hat and the
   forehead).
3. Merge with **Geometry2D.merge_polygons**.

**Check**
- Where shapes overlap (hat meets forehead), is the outline continuous
  instead of doubled? Merged polygons are the fix.

**Why**
Outlines around individual shapes would double up at overlaps; merging
the polygons first gives one clean outline.

### The human method, distilled
1. **Let the engine do the discipline:** pixel snap alignment is a
   renderer setting, not an art skill.
2. **Build the missing tool instead of faking it:** the author wrote
   DynamicOutline2D rather than hand-drawing outlines.
3. (Community verdict, quoted) "ur literally drawing just with shape
   tools and a compositor this is a valid art discipline."

**Depth status:** PARTIAL (post text + author's own comments; the
DynamicOutline2D node source not disclosed; no parameters beyond
Geometry2D.merge_polygons and pixel snap).

---

## Per-repo have-vs-need

Aegis baseline: `references/aegis-pipeline-inventory.md` (2026-09-26 audit;
trellis-pipe foundry, intake/, review/, runtime/lods, no rigging stage).
2d3d baseline: Godot 4.7.2 side-scroller, reference-driven art pipeline,
pixelize+manifest installer, QA gates. Desktop City baseline: standalone
Godot asset pipeline (tools/procedural_art.py, city_* families,
city_trees.py), PRD DEC-12 independence from Aegis. Solarempire baseline:
tools/asset-pipeline (Blender stages incl. rig.py), per-class export
profiles, glTF/GLB source of truth.

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Per-frame planet geometry clipmaps (libnoise->HLSL, no streaming) | #1 planet | NEED | No planetary-scale terrain in trellis-pipe; cinematic-cavern is static authoring | watchlist: not Aegis scope |
| agentY (agentic ComfyUI, MCP to DCCs) | #2 agentY | NEED | intake/ has concept-to-input generation; no agentic MCP DCC loop (P2 gap row) | **backlog**: free MIT tool, matches P2 gap; spike vs agentic-blender-asset-pipeline prior art |
| Diffusion city-layout gen (CityDiffusion2) | #3 cities | NEED | No layout-generation stage in foundry | watchlist: pixel-only output, no vectors yet |
| KeenFace photo->MetaHuman head | #4 KeenFace | NEED | No character-intake stage; no rigging stage (P1 gap) | watchlist: characters bucket; paid (~$30/2 heads, single-commenter claim) |
| Illustrated PBR+emissive render (ZBrush/Substance/Blender) | #6 Draconia | PARTIAL | bake_optix, uv_xatlas, review/ exist; no art-bible/style enforcement (NEED) | skip: style choice, not a stage |
| three.js env perf recipe (compute cull, billboards, alphaTest) | #5 forest | PARTIAL | runtime/lods exists; no per-instance compute culling or alphaTest-over-transparency policy | watchlist: field evidence for the P1 perf-budget gap (8 -> 27-35 fps, real numbers) |
| Vector->pixel-art Godot workflow | #7 SVS | NEED | Aegis is UE/3D; no pixel-art pipeline | skip for Aegis |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Per-frame planet clipmaps | #1 | NEED | Not a planetary game | skip |
| agentY | #2 | PARTIAL | pipeline/image_client.py exists with fail-closed $20 spend gate; agentY is a cheaper/free alternative agent front-end | watchlist: could sit in front of the AI image client |
| CityDiffusion2 | #3 | NEED | Not a city game | skip |
| KeenFace | #4 | PARTIAL | Generated character art absent (roadmap beads 9le.25, p06.10, 9le.9); procedural rigs are stand-ins | watchlist: photo->head could feed character concepts |
| ZBrush/Substance/Blender character pipeline | #6 | PARTIAL | Projection painting + pixelize exist; no sculpt stage | skip: pipeline is 2D-projected, not 3D-sculpted |
| Env perf recipe (instancing, billboards) | #5 | NEED | Godot Mobile renderer; no 3D env | watchlist: instancing/billboard principles transfer |
| Scalable Vector Shapes 2D + pixel snap | #7 | NEED | Pixel-art game; pixelize pipeline exists but no vector-authoring workflow | **watchlist (high relevance)**: vector->pixel-art feeds the toon/pixel look and the P1 art-bible work; try the asset with one sprite |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Planet clipmaps | #1 | NEED | Not planetary | skip |
| agentY | #2 | PARTIAL | AI inputs optional (tools/tripo_key.py, tools/seed_browser.py) | watchlist |
| CityDiffusion2 (OSM-conditioned layout gen) | #3 | NEED | tools/city_* families + procgen_* probes exist (hand-authored); no learned layout generation | **watchlist (high relevance)**: OSM-raster conditioning concept maps to the city_* tools; revisit when vector output lands |
| KeenFace | #4 | NEED | No people pipeline | skip |
| Draconia pipeline | #6 | NEED | Sprite-based | skip |
| Forest env perf recipe | #5 | PARTIAL | city_trees.py exists; no instancing/culling/billboard recipe documented | **watchlist**: alphaTest-over-transparency, compute-shader frustum culling, cross-billboards are directly transferable to tree rendering |
| Vector->pixel workflow | #7 | PARTIAL | Headless Blender sprite render exists; no vector-authoring input | watchlist: vector sources could feed the iso-sprite pipeline |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Planet clipmaps | #1 | NEED | Space game; planetary surfaces out of scope | skip |
| agentY | #2 | NEED | No agentic tooling | watchlist |
| CityDiffusion2 | #3 | NEED | Not a city game | skip |
| KeenFace (MetaHuman-topology heads) | #4 | NEED | Rigging stage present (stages/rig.py); profiles/CHARACTER.json; publish_characters.py | **watchlist**: paid head generator as character-intake candidate; verify texture res + topology fit before any spend |
| Draconia pipeline | #6 | PARTIAL | prepare/segment/retopo/texture stages exist; sculpt is generation-side | skip |
| Env perf recipe | #5 | NEED | Client-side rendering (Godot PC client); no perf recipe documented | watchlist |
| Vector->pixel workflow | #7 | NEED | Not a pixel-art project | skip |

## Gap recommendations (top 5)

1. **Spike agentY against the P2 MCP-DCC gap.** Free, MIT, runs on local
   LLMs, ships MCP presets for Blender/Maya/Houdini/AE, and bakes in
   konte-style acceptance loops with human review points. Concrete next
   step: run it on a Blender task from the existing
   agentic-blender-asset-pipeline skill and compare. (Aegis: backlog.)
2. **Fold the forest perf recipe into the P1 perf-budget work.** The
   prepared fix artifact is at
   `~/workspace/your_files/gap-fixes/aegis-pipeline/perf-budgets.md`;
   add the field numbers: alphaTest over transparency (8 -> 27-35 fps
   on M1 Mac), compute-shader per-instance frustum culling, 4-triangle
   cross-billboards at distance. Concrete, measured, citable.
3. **Try Scalable Vector Shapes 2D for 2d3d's art bible.** Vector-drawn,
   pixel-snapped pixel art (no shaders, no AI) plus a merge-polygons
   outline node directly serves the P1 written-art-bible gap
   (toon/pixel look). Concrete next step: install the asset and render
   one existing sprite through it.
4. **Track CityDiffusion2's vector roadmap for Desktop City.** Pixel-only
   today (1km^2 context limit, author's own caveat); the OSM-raster
   conditioning idea is the transferable part for the city_* tool
   family. Revisit when vector output exists.
5. **Keep KeenFace on the Solarempire character watchlist.** Native
   MetaHuman topology is the compatibility bet; verify texture
   resolution and the ~$30/2-heads pricing independently before any
   spend, and weigh the studio lock-in objection from the thread.

## Explicit non-goals

- **UE5 Barcelona 4K walkthrough** (YouTube, r/unrealengine): demo video,
  no tooling discussion found in the post text; not analyzed.
- **God simulator with Claude Code** (r/aigamedev, 27 comments): the only
  tooling fact is "used Claude Code for development"; no workflow
  detail. NO-TOOLING audit.
- **Ad Lumens: gaseous planets** (r/proceduralgeneration, 0 comments):
  no post text, no discussion; nothing to extract.
- **Opus5.5 Low-to-Max in Three.js** (r/aigamedev): model name only, no
  workflow. **Openjutsu one-click character swap** (r/comfyui): demo
  only, no technique disclosed. **ComfyUI H3 take manager**
  (r/comfyui): tool announcement, no workflow. **Halloween blender
  cloth sim** (r/3Dmodeling): showcase, no technique. **GDScript
  sandbox RPG alpha**, **Godot 4 mobile bullet hell**, **FLIP water
  tutorial**, **diegetic UI** (r/godot): no extractable tooling above
  the 8-cap.
- **YouTube source down** (SSL verify failed on all 11 channels via the
  sandbox proxy): reported above; Reddit only this run.
- **Draconia** stays report-only: no skill (thin evidence; pipeline
  class already covered by library skills).

## Watchlist trending

Paste from `bin/trend_watchlist.py --date 2026-10-30` (false positives
corrected in place in `references/tooling-watchlist.md`):

## Watchlist trending
- MCP servers driving Blender/Unreal (agentic DCC) (first seen 2026-09-27, status BACKLOGGED; seen again 2026-09-28, 2026-10-05, 2026-10-06, 2026-10-07, 2026-10-30) **TRENDING** — genuine: agentY's MCP presets for Blender/Maya/Houdini/AE
- Hand-painted stylized character texturing (Substance Painter + ZBrush + Arnold Maya, toon aiStandardSurface variant) (first seen 2026-10-07, status WATCH; seen again 2026-10-21, 2026-10-30) **TRENDING** — partial: same tool pair (ZBrush+Substance) for stylized character texturing via the Draconia audit, different finishing technique than the toon-aiStandardSurface variant
- Codex CLI driving Blender via MCP (first seen 2026-09-28, status WATCH; seen again 2026-10-30 [auto-match was token overlap on "MCP"/"Blender" for agentY's MCP presets, a different tool; not a genuine Codex CLI reappearance])
- GPT Astra (first seen 2026-09-28, status WATCH; seen again 2026-10-30 [auto-match was token overlap on "MCP"/"Blender" for agentY's MCP presets, a different tool; not a genuine GPT Astra reappearance])
- Substance Painter 3D-space blur filter (first seen 2026-10-12, status WATCH; seen again 2026-10-30 [auto-match was token overlap on "Substance" for Draconia's Substance texturing; no blur filter mentioned; not a genuine reappearance])
- Godot compute-shader creature brain (first seen 2026-10-29, status WATCH; seen again 2026-10-30 [auto-match was token overlap on "compute shader" for the planet geometry clipmap; no NN/simulation here; not a genuine reappearance])

## New watchlist rows (appended 2026-10-30)

Six new rows appended to `references/tooling-watchlist.md`:
per-frame rebuilt geometry-clipmap rings (planetary terrain);
agentY (ComfyUI AI agent, DCC MCP presets);
CityDiffusion2 (diffusion on rasterized OSM);
KeenFace (photos -> MetaHuman-topology heads);
three.js environment perf recipe (compute-shader culling, cross-billboards,
alphaTest, Claude-placed godrays);
Scalable Vector Shapes 2D (Godot vector -> pixel-art).

## skill_library artifacts staged

Six new skills staged in `~/workspace/video-tooling-scout-public/`:
`procgen-worlds/per-frame-planet-geometry-clipmap`,
`automation/comfyui-agenty-ai-agent`,
`procgen-worlds/city-diffusion-osm-training`,
`characters/keenface-metahuman-heads`,
`engine-runtime/threejs-forest-env-perf`,
`engine-runtime/godot-scalable-vector-shapes`.
Full report staged at `docs/scout-reports/have-vs-need-2026-10-30.md`.
Watchlist rows synced into the repo mirror
`video-tooling-scout/references/tooling-watchlist.md`.
Push via `bin/push_skill_library.py` + verification below.
