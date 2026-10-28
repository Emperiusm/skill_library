# Video tooling scout: have-vs-need, 2026-10-28

Depth mode: `pre-approved`, max 2 media downloads per run. Depth-escalation
usage this run: 0 downloads attempted, 0 succeeded, 0 skipped on an approval
gate. No audit needed a download: 7 of 8 audits rest on full post text plus
retrieved comments, and the 8th (MOSS Ep40) rests on full YouTube captions
(466 segments, 19 minutes) plus its description. The one NO-TOOLING audit
(Blender to Minecraft) would not have been rescued by a download: the clip
is a showcase, the post selftext is empty, and the author did not answer
link requests in the retrieved comments.

Sources: Reddit scan, last 2 days, 23 subreddits via Arctic Shift
(`scan-2026-10-28.json`: 48 video posts, min score 20). YouTube scan:
DOWN for this run, all 11 channels failed with an SSL certificate error
(`scan-youtube-2026-10-28.json`); a retry with the sandbox egress CA
appended to the cert bundle failed identically, so per the skill the run
continued Reddit-only. Note the failure mode changed from 2026-10-27
(YouTube bot-wall) to today's SSL failure; neither is a content finding.
12 of today's 48 posts overlap the 2026-10-27 scan window; the 12 were not
re-audited (Gaussian-splat portals and the three.js electronics sandbox
were already audited 2026-10-27; the Far Shore, MOPs+ licensing, and
MiniMax H3 custom-node posts were already scanned-not-analyzed 2026-10-27
for lack of disclosed workflow, and nothing new was disclosed since).

## Gap alerts

Two genuine P1-gap matches, both qualified (neither is a drop-in fix):

1. **Desktop City P1, shader-driven skyline fill: PARTIAL FILL from audit 3.**
   The Godot procgen city builds ~700 buildings a lap as plain boxes and
   gets all of its city life from one window shader: 3.6 m floors, whole
   floors lighting up or going dark like real offices, far windows fading
   into a soft glow. That is the shader-carries-the-city pattern the gap
   asks for, transferred from 3D Godot to Desktop City's fixed-view
   sprites it is a pattern to borrow (shader windows on simple geometry),
   not a sprite-ready implementation. Desktop City's inventory still
   lists no skyline-fill equivalent.
2. **Aegis P1, AI-vendor generation/acceptance spec: PATTERN MATCH from
   audit 1.** Freefield's lab runs every one of its 117 apps on a GPU
   with fixed seeds and publishes one example per app with its real time
   and peak VRAM: 48 runs, 710 of 733 cases ok. That is a "what good
   means, measured" gate of exactly the kind the acceptance-spec gap
   lacks. It is a pattern for Aegis intake, not a spec Aegis can adopt
   as-is: Freefield tests finished ComfyUI apps, Aegis intake needs
   per-asset-type acceptance criteria.
3. **Explicitly NOT a gap alert: audit 2 and the rigging P1.** The 1M
   soldiers post uses fully rigged/skinned Mixamo soldiers only for the
   nearest few thousand agents and GPU impostors for the rest. That is a
   rendering budget trick, not a rigging/retarget stage for the Aegis
   foundry, so it does not fill the rigging P1. Likewise it gives FPS
   benchmarks, not per-asset tri/texel/draw-call budgets, so it does
   not fill the perf-budget P1. No audit this run fills the import
   validation gates, mesh compression, mesh refinement, or production
   conversion P1s.

## Videos deeply analyzed

| # | Video | Creator | URL | Source |
|---|-------|---------|-----|--------|
| 1 | "Freefield: Higgsfield rebuilt on ComfyUI, 117 apps, open weights only (MIT)" | neuregex | https://v.redd.it/z144fzxo13yh1 (r/comfyui post 1xh73t4, score 239); code https://github.com/neuregex/freefield; demo https://youtu.be/N7mv2v3Txeo | Reddit clip; full post text + 20 comments |
| 2 | "1M Soldiers in Godot 4 C# at 300-450 FPS - ECS-Style Data-Oriented Design" | (author handle not in retrieved data; post 1xh7eiw) | https://v.redd.it/vguzjsf073yh1 (r/godot, score 38) | Reddit clip; full post text + 3 comments |
| 3 | "Has anyone else tried building a procedural generated low poly city in Godot?" | CrashBamBoomClick | https://v.redd.it/vtq8wwiyk3yh1 (r/godot post 1xh8vg4, score 32) | Reddit clip; full post text + 7 comments |
| 4 | "Software PBR + Raytracer + L1 SH GI inside CyberVGA (JIT x64, no GPU required)" | exp_function | https://v.redd.it/6h7gavyy8zxh1 (r/GraphicsProgramming post 1xgnzeb, score 56) | Reddit clip; full post text + 8 comments |
| 5 | "I turned Blender creatures into real Minecraft blocks (my add-on exports the animation, MC plays it live)" | (author handle not in retrieved data; post 1xh6294) | https://v.redd.it/ru7ginxlw2yh1 (r/blender, score 126) | Reddit clip; empty selftext + 12 comments |
| 6 | "I fixed the window + raindrop shader breakdown" | Longjumping_Height30 | https://v.redd.it/3m8qwyadp2yh1 (r/godot post 1xh4iqc, score 234) | Reddit clip; 78-char post text + 17 comments |
| 7 | "RTX 3060 12GB + MiniMax H3: Native 2336x1312 Snow Leopard Video | 243 Frames, 4 Steps, 33 Minutes" | (author handle not in retrieved data; post 1xgu6b8) | https://v.redd.it/kg08qhr2t0yh1 (r/comfyui, score 24) | Reddit clip; full post text + 12 comments |
| 8 | "MOSS Image in ComfyUI | Text to Image, Words & Layout (Ep40)" | pixaromadesign / pixaroma | https://youtu.be/l4R96NemQS8 (r/comfyui post 1xgwtyb, score 39); 19 min, 13,752 views | YouTube captions (466 segments) + description |

Scanned, not analyzed (8-video cap; overlaps and lower-ranked items):
"Mastery of Blender?" (r/blender, score 996; a question about a reference
clip, no workflow disclosed); the winter-biome pixel naval game
(r/godot, score 1008; showcase, no workflow); "Despair physics"
Euphoria-style procedural balancer (r/proceduralgeneration; a principle
only, no parameters, solver settings, or code, plus a commenter-linked
delirium-physics repo the author did not claim); Claude + Remotion +
PixelLab.ai cutscenes (r/aigamedev; proof of concept, prompts quoted but
no timings, node settings, or asset pipeline detail); the 12 overlapping
posts from 2026-10-27 (see header); remaining showcase clips with no
tooling signal (Mauser render, football games, knitting, whale, candle
and flamethrower sims, all under the relevance bar once tooling signal
is weighted).

## 1. "Freefield: Higgsfield rebuilt on ComfyUI, 117 apps, open weights only (MIT)" (neuregex)

Source: https://v.redd.it/z144fzxo13yh1 | r/comfyui post 1xh73t4 (score 239)

Tools used: **ComfyUI + Comfy SDK** (host), **FLUX 3 Klein** (Create
Image), **MiniMax H3** (Create Video, Extend Video), **LTX-2.5, Wan 2.1
and 2.2, Qwen-Image-Edit, Z-Image, SeedVR2, Stable Audio 3, MiniMax
Music 3** (open-weights model roster, no API nodes), **Modal** (L40S or
H100 hosting) or any ComfyUI instance pointed at it. License: MIT.
Demo soundtrack made in Freefield with MiniMax Music 3.

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: rebuild a closed
product as 117 small ComfyUI apps generated from one file format, then
prove each app with a fixed-seed lab run.

### Phase 1: Cover the product surface with apps, not one mega-workflow

**Do**
1. Enumerate the target product's tools and apps: Higgsfield shows 129;
   Freefield covers 95 of them with 117 apps (image, video, VFX, audio).
2. Include: Create Image with FLUX 3 Klein; Cinema Studio (a still, or
   a shot from that still with Higgsfield's 33 camera moves); Create
   Video and Extend Video with MiniMax H3; Re-shoot (a new camera angle
   on a clip already shot); Relight; Effects (24 LoRAs); Morph; Mixed
   Media; Dub; Face Swap; Depth Map; Video Background Remover; Inpaint
   with a brush; Photodump; Moodboard; and 72 template apps such as an
   AI Influencer builder, Packshot, Bullet Time, or Victory Card.
3. Use open weights only, no API nodes.

**Check**
- Count apps against the target's list: 117 apps, 95 of 129 covered.
  The author is explicit that coverage is partial, not total.

**Why**
A product is a bundle of small tools, not one pipeline. Covering it
app-by-app keeps each piece shippable and testable on its own.

### Phase 2: Make every app one folder, generated from one format

**Do**
1. Each app is one folder: an `app.json` plus a ComfyUI workflow in API
   format.
2. Generate the web UI, the model downloads, the VRAM map, and the tests
   from those files, not by hand.
3. Convert any other ComfyUI workflow into a draft app with one command:
   `tools/import_workflow.py`.
4. Chain apps with "Use in...": send a result to another app (author's
   example: an AI Influencer portrait to Image to Video).

**Check**
- A new workflow becomes a draft app with one command; the UI, download
  list, VRAM map, and tests all regenerate from the app files.

**Why**
Quoted principle, author's own framing: the format is the product.
When UI, downloads, VRAM guidance, and tests all derive from
`app.json` + workflow, adding app 118 costs one folder, not a rewrite.

### Phase 3: Prove each app in the lab with fixed seeds

**Do**
1. Run every app on a GPU with fixed seeds; publish one example per app
   with its real time and peak VRAM.
2. Record the lab totals: 48 runs, 710 of 733 cases ok.
3. Let the lab pick the image model, not taste: six prompts on five open
   models with the same seed; FLUX 3 Klein followed them best.
4. Fix failures in batches, not one by one. Author (neuregex, comment):
   "I built a flagging system that every example that came out wrong got
   flagged, then I collected the flags and fixed them in batches, and
   kept repeating that until they all gave good results."
5. Answer the QA question directly (comment, on whether every run was
   QA'd): the flagging loop above is the QA system.

**Check**
- Every app has a published example, a real time, and a peak VRAM
  figure; the lab pass rate is a number (710/733), not an impression.

**Why**
Fixed seeds turn "it worked once" into a repeatable claim, and batch
flag-fixing turns QA from a chore into a loop that converges. This is
the acceptance-spec pattern flagged at the top of this report.

### Phase 4: Ship on rented GPU or any ComfyUI, with a VRAM map

**Do**
1. Run on Modal (L40S or H100) or point Freefield at any ComfyUI.
2. Read the docs' VRAM map for what fits on a 24 GB card before running.
3. Install note from a commenter (KeyTumbleweed5903): "it downloads
   everything u need - u may need to get a hugging face token"; the
   same commenter reports it "installed without any issues what so
   ever" and worked on first tries.

**Check**
- The docs answer "does this app fit my card?" before the run starts;
  the installer pulls its own models (plus a Hugging Face token where
  gated).

**Why**
A 117-app bundle that only runs on one machine is a demo. A VRAM map
plus a Modal-or-local choice makes it a tool other people can actually
run.

### The human method, distilled
1. Take the vendor's "open source" claim literally and rebuild the whole
   surface, not one app: the contest asked for one cloned app, the
   author cloned the platform (commenter Ok_Ad4148: "I thought the
   Comfy.org contest was to pick an app in Higgsfield and clone it, not
   duplicate the entire Enchilada!").
2. One file format generates everything downstream (UI, downloads,
   VRAM map, tests); never hand-maintain four copies of the same facts.
3. Flag every bad example, fix in batches, repeat until the lab is
   green; publish the pass rate.
4. Pick models by same-seed shootout, not by announcement hype.

**Depth status:** FULL (full post text, 20 comments including the
author's QA method, model roster, lab numbers, and install reports;
the demo video itself was not transcribed, and no per-app workflow JSON
was inspected, so per-app node settings are not claimed here).

## 2. "1M Soldiers in Godot 4 C# at 300-450 FPS" (post 1xh7eiw)

Source: https://v.redd.it/vguzjsf073yh1 | r/godot post 1xh7eiw (score 38)

Tools used: **Godot 4.6 (.NET / C#)**, **Forward+ renderer**,
**Mixamo** (soldier model/animation), **GPU impostors** (distant
soldiers). Test PC: Core i5-12600K, RTX 4070 Ti, 32 GB DDR5, NVMe SSD.
Settings: 1920x1080, 60 Hz monitor, VSync off (uncapped), running
inside the editor with JIT.

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: simulate everyone,
render only what is near, and let cost scale with camera distance, not
with army size.

### Phase 1: Store soldiers as arrays, not objects

**Do**
1. Give each soldier an index into structure-of-arrays data: position,
   yaw, HP, animation time, team, state, and so on.
2. Run logic as batch passes over that data. The author is explicit
   this is NOT a formal ECS framework: "no entities, components, queries
   or system scheduler". It is ECS-style separation of data and
   behavior plus data-oriented design taken "to the extreme".
3. Simulate all 1,000,000 agents at once: AI, movement, collisions,
   combat, respawn, two armies chasing, fighting, dying, respawning.

**Check**
- The simulation count is 1,000,000 agents, not 1,000,000 rendered
  characters. Any claim otherwise misreads the post.

**Why**
Batch passes over flat arrays are cache-friendly and branch-light;
per-soldier objects with per-frame virtual calls are what would make
1M agents impossible. The author separates the two halves of ECS/DOD
and takes only the data-oriented half to the extreme.

### Phase 2: Render near soldiers fully, distant soldiers as impostors

**Do**
1. Fully rig and skin only the nearest few thousand soldiers at any
   moment (Mixamo model/animation).
2. Draw the rest as GPU impostors.
3. Let scaling follow the camera: "Cost depends on how many soldiers
   are near the camera, not on the total."

**Check**
- FPS is reported across all modes, graphics levels, and camera
  positions in the video; the headline numbers are 300-450 FPS
  overall, dropping to ~180 at Ultra, because "GPU load grows mainly
  with graphics level (Ultra costs the most)" while "scaling with
  soldier count is mostly CPU-side (simulation, pose, culling)".

**Why**
Rendering cost must scale with what the camera sees, or the army size
is capped by the GPU. Simulation cost scales with army size and stays
on the CPU, where batch passes carry it.

### Phase 3: Report the measurement honestly, including what was not tested

**Do**
1. Measure inside the editor with JIT, VSync off, and say so: "FPS
   shows performance headroom rather than what the monitor displays."
2. State the untested configurations plainly: "Not yet tested: a
   release export (no editor, no debug engine) and NativeAOT. I expect
   release to be faster, but I haven't measured it yet."

**Check**
- Any reuse of the 300-450 FPS figure must carry the editor/JIT caveat
  and the untested-release caveat with it.

**Why**
A benchmark without its conditions is a marketing number. The author's
own caveats are what make the number usable: headroom in-editor,
release expected faster but unmeasured.

### The human method, distilled
1. Simulate everyone, render only the near field; never let render cost
   scale with total count.
2. Take the data-oriented half of ECS (flat arrays, batch passes) and
   skip the framework ceremony when it adds nothing.
3. Report the rig you actually measured on, and name what you have not
   measured yet.

**Depth status:** FULL (full post text with hardware, settings, and
caveats; comments add nothing beyond praise, so no comment technique
is claimed).

## 3. "Procedural generated low poly city in Godot" (CrashBamBoomClick)

Source: https://v.redd.it/vtq8wwiyk3yh1 | r/godot post 1xh8vg4 (score 32)

Tools used: **Godot 4.7 with C#**, **SurfaceTool** (building boxes),
**one custom window shader** (no window textures), native Mac and
Windows builds. Context: a test track for an anti-gravity racer; the
track pipe runs through the city.

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: generate a city of
plain boxes at load time, then let one shader do all the visual work
that textures would normally do.

### Phase 1: Generate the city on a grid at track load

**Do**
1. Lay the city on a grid of 56 m blocks, 1 to 4 buildings per block,
   with random heights, colours, and window styles.
2. Generate in C# when the track loads: around 700 buildings a lap.
3. When the pipe hits a tower, split the tower around a 21.5 m hole;
   the top part floats, with a hexagon ring at every tunnel.

**Check**
- Building count is per lap (~700), not per scene; the city is
  generated, not placed by hand.

**Why**
Generation at load keeps the track data tiny (a seed and rules, not
700 placed buildings) and makes every lap's city a function of the
grid rules.

### Phase 2: Build everything from boxes, chopped for culling

**Do**
1. Make every building from boxes with SurfaceTool.
2. Chop the city into 256 m tiles so culling works.

**Check**
- If distant tiles still cost full draw time, the 256 m chop is not
  doing its job; culling is the point of the chop, not the boxes.

**Why**
Plain boxes are cheap to generate and cheap to draw; the performance
work is spatial (tiles for culling), not geometric detail.

### Phase 3: Replace window textures with one shader

**Do**
1. Use no window textures at all. One shader: 3.6 m floors, whole
   floors light up or go dark like real offices.
2. Let far windows fade into a soft glow "so you don't get that stripy
   mess" (author's words).
3. Take the commenter's interior-mapping tip seriously: Roucan
   suggested interior mapping for window detail ("faking the stuff on
   the other side of windows"), and the author replied the windows are
   already "one shader with a cell per window, so faking a room behind
   each one should drop right in", and that the same trick might fix
   wall ledges.

**Check**
- Near: individual floors read as lit or dark offices. Far: windows
  dissolve into glow instead of aliasing into stripes. If far windows
  still stripe, the fade distance is wrong.

**Why**
A shader window is resolution-independent and costs no texture memory;
a texture atlas at city scale either blurs or stripes. The shader
also makes the lit/dark office pattern a rule (whole floors), not a
painted texture.

### Open questions the author asked (not answered in the thread)
1. Verts: "how do you add detail (roofs, ledges, setbacks) without the
   vert count blowing up?" No answer in the retrieved comments beyond
   the interior-mapping suggestion.
2. Textures: "has anyone compared that to a texture atlas for a big
   city? which looked better and ran faster?" Unanswered in the
   retrieved comments. Do not present either as settled.

### The human method, distilled
1. Generate plain, then shade smart: put the visual budget in one
   shader, not in geometry or textures.
2. Make far-field behavior a first-class rule (fade to glow), not an
   afterthought, because cities are mostly seen from far away.
3. Ask the two questions that decide the next iteration (detail without
   verts, shader versus atlas) instead of guessing.

**Depth status:** PARTIAL (full post text with grid, tile, floor, and
hole numbers, plus the interior-mapping comment exchange; no shader
code, no vert counts, and the author's two questions are open, so the
shader itself cannot be reimplemented from this audit alone).

## 4. "Software PBR + Raytracer + L1 SH GI inside CyberVGA" (exp_function)

Source: https://v.redd.it/6h7gavyy8zxh1 | r/GraphicsProgramming post 1xgnzeb (score 56)

Tools used: **CyberVGA** (author's engine), **C89** (native DOS
target) / **C17** (modern Win64 port), **JIT-compiled SSE** (runtime
code generation into a VirtualAlloc executable buffer),
**FSR 2** (optional, GPU only). Distribution promised: a new SDK
version with example map and documentation, via
https://expfunction.itch.io/cybervga, "in a few days" (author's words
at post time; not verified as shipped).

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: keep a DOS-era
fixed-point software engine, then JIT-compile only its hot paths to SSE
on modern multi-core CPUs and add a probe-based GI pass on top.

### Phase 1: Compile the hot paths at runtime, not at build time

**Do**
1. Bake the world as triangle soup into a world sidecar file via a
   direct-threaded octree module (leaves hold a predetermined number
   of triangles).
2. At runtime, compile the hot paths to SSE into a VirtualAlloc
   executable buffer: direct-threaded octree traversal, AABB slab
   tests, fog volume early-outs, L1 SH evaluation, material/GI bounce
   stubs.
3. Run the raytracer on multiple worker threads, each processing tiles;
   workers call into the generated code for their tile's rays.
4. Answer the "why JIT?" question the thread asked (VictoryMotel,
   NegativeEntr0py): the author defends JIT over hand-written SSE and
   over plain MSVC-optimized code in the comments, but the retrieved
   comment bodies are truncated at 800 characters, so the full defense
   is not quoted here. Inference (labeled): the JIT lets the engine
   specialize traversal/shading code to the baked world at load time.

**Check**
- The generated code path is exercised per tile per worker; if a tile
  renders without calling into it, the JIT is decorative.

**Why**
A software raytracer lives or dies on its inner loop. JIT-compiling
that loop to SSE, specialized to the baked octree, buys modern-CPU
speed without abandoning the engine's software-rendering roots or its
DOS-era fixed-point design.

### Phase 2: Add GI as a probe grid, not as full path tracing

**Do**
1. Build a grid of L1 spherical-harmonics probes: Fibonacci sphere rays
   per probe, temporal blending between frames.
2. Send primary hits through a full GGX PBR path with
   roughness/metalness, then sample the probe irradiance for the
   diffuse bounce.
3. Cluster emissive surfaces into virtual point lights.
4. Add one-bounce reflections with roughness falloff; liquids get
   refraction plus absorption plus caustics.
5. Judge the result the author's way: "The color bleeding and the
   split-screen direct vs GI+reflections actually look pretty good."

**Check**
- Split-screen direct versus GI+reflections is the author's own
  verification view: color bleeding must be visible on the GI side
  and absent on the direct side.

**Why**
L1 SH probes are cheap enough for a software renderer and capture the
effect that sells GI (color bleeding, soft diffuse bounce) without
paying for full multi-bounce path tracing per pixel.

### Phase 3: Keep upscaling optional and GPU-gated

**Do**
1. Offer FSR 2 as optional, because "it runs on the GPU" (author's
   words); the raytracer itself requires no GPU.

**Check**
- The no-GPU claim holds only with FSR 2 off; with it on, a GPU is in
  the path.

**Why**
Optional GPU features must not silently become requirements, or the
engine's defining constraint (software-only) evaporates.

### The human method, distilled
1. Preserve the engine's identity (fixed-point, software roots) and
   modernize only the hot loop, by JIT, not by rewrite.
2. Buy GI with probes and one bounce, not with brute-force path
   tracing, when the budget is a software renderer.
3. Verify with a split-screen (direct versus GI+reflections) so the
   improvement is visible, not asserted.

**Depth status:** PARTIAL (full post text with the JIT, probe, PBR,
and liquid recipes; comment bodies truncated by the fetcher at 800
characters, so the author's detailed JIT defense is summarized, not
quoted, and no code, timings, or probe counts are published in the
post).

## 5. "Blender creatures into real Minecraft blocks" (post 1xh6294)

Source: https://v.redd.it/ru7ginxlw2yh1 | r/blender post 1xh6294 (score 126)

Tools used: claimed in the title only: a **Blender add-on** (unnamed)
that exports animation, and **Minecraft** playing it live. No version,
no add-on name, no download link, no settings in any retrieved source.

What was actually retrieved: post selftext is empty. 12 comments
retrieved; they ask for the link ("Link?", "is the non blocky version
available to download?", "Does it matter? It looks awesome.",
"Literally blew my mind! Can you interact with them?",
"Where did you get that dragon asset + animation from?") and the
author did not answer any of them in the retrieved comments. One
commenter jokes "Holy alembic", which is not evidence the pipeline
uses Alembic; it is not claimed as such here.

**Depth status:** NO-TOOLING (showcase clip with a title claim and no
extractable workflow; a media download would add the clip's visuals
but not the add-on, its settings, or its export format, since none are
named anywhere retrieved). Kept in the report and watchlist only, with
an explicit unverified flag; do not cite this as a verified tool.

## 6. "Window + raindrop shader breakdown" (Longjumping_Height30)

Source: https://v.redd.it/3m8qwyadp2yh1 | r/godot post 1xh4iqc (score 234)

Tools used: **Godot shader** (window + raindrop water simulation;
engine version and shader file not stated in retrieved sources),
plus **bounce lighting and an emissive material** (author comment).
No shader code, uniform values, or resolution figures are published
in the retrieved sources.

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: give every
raindrop a heightmap, derive light from its slopes, and desynchronize
every pane so the rain never reads as a loop.

### Phase 1: Build each raindrop from a heightmap

**Do**
1. Give each raindrop a heightmap: tallest at the center, lowest at the
   edges (commenter Longjumping_Height30, who is the author, describing
   the method).
2. Infer how light is pushed around from the heightmap: "the
   differences between cells are used for slope and direction of
   slope" (author comment, truncated by the fetcher; the sentence is
   quoted only as far as retrieved).

**Check**
- A drop must read as a lens, not a decal: light bends by slope, so
  the center and the rim behave differently.

**Why**
Heightmap-plus-slope is the whole trick: once the surface shape is
known per cell, lighting follows from geometry instead of from a
painted raindrop texture.

### Phase 2: Desynchronize panes with torus sampling

**Do**
1. Give each pane of glass its own sample point: "each pane of glass
   uses its position to sample a random point on a torus that the
   water sim covers" (author comment).
2. Accept the visible consequence the author names: panes are "not
   entirely in sync with all other panels", and "its easier to notice
   the raindrops are different" across panes.
3. Respond to the sync critique (Friendly-Mingus asked whether timing
   or pattern could be randomized between panes) with this mechanism
   rather than with a global offset: per-pane position drives the
   sample, so desync is structural, not a tweak.

**Check**
- Two adjacent panes must not show the same drop pattern at the same
  time. If they do, the per-pane sampling is not wired to position.

**Why**
Synchronized rain reads instantly as a loop, however good one pane
looks. Position-driven sampling breaks the loop without storing a
separate simulation per pane.

### Phase 3: Finish with bounce light, emissive, and taste checks

**Do**
1. Add bounce lighting and an emissive material (author comment:
   "Yes, plus bounce lighting and an emissive material").
2. Take the one taste critique in the thread seriously: the tarp at
   the start "feels a little bit too shiny" (eveningdreamer). The
   author did not dispute it in the retrieved comments.

**Check**
- The scene should feel like rain outside, not like a shader demo:
  commenter Akrucious reports the sound and level design "actually
  made me feel like it was raining outside", which is the perceptual
  bar this shader is judged against in the thread.

**Why**
A rain shader is judged by weather feel, not by drop count. Bounce
light and emissive sell wetness; an over-shiny tarp breaks it.

### The human method, distilled
1. Derive light from shape (heightmap slopes), not from painted
   textures.
2. Desynchronize by construction (position-sampled torus), not by
   hand-tweaking offsets per pane.
3. Let the thread's taste critique stand: one too-shiny surface is a
   real defect report, not noise.

**Depth status:** PARTIAL (method reconstructed from the author's own
comments, which are the only technical source; post text is 78
characters, no code or parameters are published, and the video itself
was not frame-reviewed, so this audit cannot be executed as code from
the skill alone).

## 7. "RTX 3060 12GB + MiniMax H3: Native 2336x1312 Snow Leopard Video" (post 1xgu6b8)

Source: https://v.redd.it/kg08qhr2t0yh1 | r/comfyui post 1xgu6b8 (score 24)

Tools used: **MiniMax H3 Singularity Ref2VA V2 (INT8)**, **DMAD 4-step
LoRA (weight 1.0)**, **Comfy Kitchen INT8 Sparse attention**
(`video_budget = 0.10`), **ComfyUI** (host), **Starlight Precise 2.6**
(commenter enhancement pass, not the author's pipeline). Hardware:
RTX 3060 12 GB, 32 GB system RAM.

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: generate natively
at 3 MP on a 12 GB card by stacking every low-VRAM trick at once, and
never upscale as a substitute for native resolution.

### Phase 1: Set the native-resolution target and refuse the upscale shortcut

**Do**
1. Target native 2336x1312 (3.06 MP), no upscaling, 243 frames at
   24 FPS (~10 seconds).
2. Start from the author's own history: "I started experimenting with
   local AI video generation at around 0.3MP, relying on upscaling for
   higher-resolution output", then moved to native generation "after a
   lot of workflow optimization and testing".
3. Take the author's fine-detail claim as a reported observation, not
   a measured benchmark: "the difference in fine detail between
   upscaled low-resolution video and native high-resolution generation
   is huge" (author, comment, from experience, not from a controlled
   comparison in the post).

**Check**
- The output resolution must be the generation resolution (2336x1312
  in the sampler), not a post-hoc upscale of a smaller generation.

**Why**
Upscaling invents detail; native generation (in the author's
experience) preserves it. The whole recipe exists because the author
stopped accepting the upscale substitute.

### Phase 2: Stack the low-VRAM recipe exactly

**Do**
1. Model: MiniMax H3 Singularity Ref2VA V2 (INT8).
2. LoRA: DMAD 4-step, weight 1.0.
3. Inputs: 1 starting frame + 2 snow leopard reference images.
4. Sampler: `res_multistep`. Scheduler: `simple`.
5. Sparse attention: Comfy Kitchen INT8 Sparse, `video_budget = 0.10`.
6. Memory optimization: 4096-row chunks.
7. Accept the cost: sampling speed 426.86 s/it, total generation time
   1989.93 seconds (33m 09.93s) for 243 frames.

**Check**
- If any one element is dropped (INT8 model, 4-step LoRA, sparse
  attention at 0.10, chunked memory), the 12 GB claim is no longer the
  author's claim; the recipe is a stack, not a menu.

**Why**
No single trick fits 3 MP on 12 GB. INT8 halves weights, the 4-step
LoRA cuts sampling passes, sparse attention at a 0.10 budget cuts the
attention matrix, and chunking caps peak memory. Each trick buys a
different slice of the budget.

### Phase 3: Calibrate against other 12 GB results in the thread

**Do**
1. Record the commenter corroboration, labeled as commenter results,
   not the author's: JinnTsui reports 25-second videos on an RTX 3060
   12 GB with 32 GB RAM, including 1280x768, 600 frames in 1,347
   seconds (22m 27s) with H3 + DMAD 4-step.
2. Record the mechanism commenters propose for why 12 GB cards survive
   at all (froschquark): "the 'magic' is simply the memory
   optimizations which does not let you go OOM but just shuffles the
   data into RAM and later also into system pagefile". Labeled as a
   commenter hypothesis, not a measured fact.
3. Note the open question (Danny_Stock): if 3 MP for 10 seconds takes
   33 minutes, the same workflow should in theory give 1 MP for well
   over 10 seconds; unanswered in the retrieved comments.
4. Note the enhancement fork, not part of the recipe: ThoughtCounter
   ran the video through Starlight Precise 2.6 at 1:1 (no upscale).

**Check**
- Corroboration counts only when the card class matches (12 GB +
  32 GB RAM); results on larger cards do not validate this recipe.

**Why**
A single 33-minute run is a proof, not a budget table. The thread's
other 12 GB runs are what turn one result into a usable expectation
for the same hardware class.

### The human method, distilled
1. Generate at the target resolution natively; do not let upscaling
   stand in for resolution.
2. Stack low-VRAM tricks (INT8, few-step LoRA, sparse attention with
   a stated budget, chunked memory) and publish every setting, so the
   recipe is reproducible rather than inspirational.
3. State the limit honestly: the author calls this "my highest
   successfully completed native-resolution H3 test so far, not a claim
   about the GPU's absolute limit".

**Depth status:** FULL (full post text with every sampler, LoRA,
attention, chunk, and timing number, plus commenter corroboration on
the same hardware class; no workflow JSON was inspected, so node
wiring beyond the named settings is not claimed).

## 8. "MOSS Image in ComfyUI | Text to Image, Words & Layout (Ep40)" (pixaroma)

Source: https://youtu.be/l4R96NemQS8 | 19 min, 13,752 views, captions
(466 segments, ASR track) + description. ASR garbles creator/brand
names in places ("PixArt-Alpha" for Pixaroma nodes, "Laura" for LoRA);
settings and workflow names below are taken from the description and
from caption passages where the meaning is unambiguous, and ASR-only
wordings are not quoted as exact terms.

Tools used: **MOSS Image by OpenMOSS** (SFT checkpoint recommended;
base files are for LoRA training), **ComfyUI 0.42 or newer**,
**Pixaroma nodes 1.4.219 or newer**, **FLUX.2 VAE** (the small FLUX 2
VAE, "a different file from the normal one"), **speed LoRA** (4 steps).
License: Apache 2.0, paid work allowed. Workflows: 9, free, one per
chapter, at pixaroma.com. Existing library skill expanded by this
audit: `ai-video/moss-image-comfyui-recipe` (2026-10-21 recipe).

This audit reconstructs the exact workflow shown in the video, step by
step, so another agent can follow the same process. Every phase has three
parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The video's core method is: MOSS Image is not
an edit model, it is a text-rendering model, so every workflow is built
around giving it exact words (quoted, boxed, or same-seed swapped) and
never asking it to change a picture in place.

### Phase 1: Install to the version gate, with the SFT checkpoint

**Do**
1. Check versions first: double-click the canvas, add a version check.
   MOSS Image needs ComfyUI 0.42 or newer and Pixaroma 1.4.219 or newer;
   older versions need updating (Pixaroma help page has per-install
   steps).
2. Download models first (three files): the model goes in diffusion
   models in a MOSS folder (create it if missing); take the model with
   SFT in its name ("That's the finished model. The base files are made
   for training LoRAs"); the text encoder goes in text encoders; the
   VAE goes in the VAE folder (small FLUX 2 VAE).
3. Restart ComfyUI or press R to refresh the lists.
4. Learn the node colour convention, shared by all nine workflows:
   orange nodes load the models; blue nodes are the only ones you
   change, numbered in order; green nodes do the work; the red node
   saves. Outputs go to ComfyUI's output folder, each workflow in its
   own folder.
5. Expect the first run to take longer: ComfyUI loads about 13 GB of
   models from disk; after that they stay loaded.

**Check**
- Version check shows ComfyUI 0.42+ and Pixaroma 1.4.219+ before any
  workflow runs; the SFT (not base) checkpoint is loaded.

**Why**
Most "MOSS doesn't work" failures are version or checkpoint failures,
not model failures. The colour convention is what makes nine workflows
learnable as one pattern instead of nine separate puzzles.

### Phase 2: Write text-to-image prompts the MOSS way

**Do**
1. Workflow 1, text to image: describe in order: kind of image, then
   the person and what each hand does, the place, the light, and the
   camera.
2. Put words that must appear in the image in double quotes, e.g.
   "pizza cafe on the wall". Skip "masterpiece" / "best quality";
   describe what to see instead.
3. Seed control: F keeps the same image, R makes a new one every run.
4. After the first run, about 9 seconds per image on the creator's card
   (card model not stated in captions; do not assume one).
5. Workflow 2, prompt helper: type a short idea (creator's example: a
   poster for a summer jazz night on a rooftop); the helper (the same
   text encoder that reads the prompt) writes the long prompt in about
   2 seconds. Toggle between the AI-written prompt and the prompt as
   typed. Read the shown text and put the words you want in the idea
   in double quotes, because the helper invents details: in the
   creator's run it invented a date ("I never asked for that date. The
   helper made it up"). Two seeds: the AI-prompt seed rerolls the
   written prompt; the image seed makes a new image from the same
   prompt without re-running the helper.
6. Failure mode the helper exposes: with the prompt as typed, small
   poster lines came out made up; with the AI-written prompt, every
   line read right, including place, time, and free entry under the
   title. The fix is fuller prompts, not more steps.
7. RTX 30-series failure mode (creator): the run can stop with a CUDA
   error; restart ComfyUI, open the gear on the AI-prompt node, and
   turn off faster writing.

**Check**
- The sign on the wall is spelled right (creator's check on workflow
  1: one hand pours the milk, the other holds the cup, sign spelled
  right). For posters, every line reads right, not just the title.

**Why**
MOSS's differentiator is legible words, and words are only legible
when they are specified: quoted, complete, and checked. Vague prompts
produce made-up small text, which is the model's predictable failure,
not bad luck.

### Phase 3: Go fast with the 4-step speed LoRA, for drafts only

**Do**
1. Workflow 3: add the speed LoRA (the one new file in download
   models, in a LoRA folder under MOSS). Prompt and size work the same
   as workflow 1.
2. On the K sampler, keep 4 steps and CFG 1: "The LoRA was made for
   exactly that."
3. Expect about 1 second per run on the creator's card, a new version
   every run, "great for trying ideas and seeds".
4. Accept its limits: big words stay right, but small lines can gain
   or lose a word, and skin comes out a little smoother. "When every
   word counts, use workflow one for the final image. The same prompt
   and seed there give you a similar image, not the same one."

**Check**
- Speed is ~8x the full workflow ("about eight times faster" per the
  creator); if a fast run is used as a final, its small-text errors
  are the user's fault, not the model's surprise.

**Why**
Draft speed and final accuracy are different jobs. The LoRA buys the
first and must never be mistaken for the second.

### Phase 4: Put words in pictures, then lay them out in boxes

**Do**
1. Workflow 4, words in pictures: every word goes in double quotes;
   give each line its own quotes on its own line, and MOSS keeps the
   line breaks. Describe the letters (e.g. big, bold chalk letters)
   and what they are on (e.g. the chalkboard).
2. Creator's checks: a chalkboard menu (title, today's menu, five
   lines each with a price) came out right on four seeds out of four.
   A book cover works only when the title is described as part of the
   painting ("hand-painted and lit by the lighthouse"), not pasted on:
   "A title just placed on a painting can look pasted on like it was
   added later."
3. Rule: the smaller the letters, the more room for a mistake, so for
   a lot of words pick a bigger size. Things that usually carry words
   (books in the background) get made-up letters unless you give the
   words.
4. Workflow 5, layout with boxes (Pixaroma layout-boxes node): a small
   canvas shaped like the image; each box is one thing (object or
   text). Click to select, drag a corner to resize, drag inside to
   move, undo steps back. Step 1 is size (box canvas takes the same
   shape); step 2 boxes for the creator's skincare ad: headline at
   top, bottle in middle, small line at bottom. A text box has its
   exact words plus a short description of the letters; an object box
   has one full description. Colours go in the words; box colour only
   helps you see them. Step 3 prompt describes the whole image (kind,
   background, colours, light); do not name the boxes there.
5. Boxes are guides, not cutouts: "The bottle fills its box roughly
   with its own shape and shadow." For a person/character, type its box
   number in the character boxes on the MOSS node.
6. Workflow 6, same picture, new words: same prompt, same seed (keep
   seed on F), changing words in square brackets split by a vertical
   bar (creator's example: Anna, Mark, Sophia, Leo). One run makes one
   image per name, about 9 seconds each, shown together in an image
   grid. Two bracket groups make every combination (two colours x two
   names = four images). Caveat: "It's not always exactly the same
   image though. Sometimes a small thing changes. The steam moves or
   an extra candle shows up."

**Check**
- Menu: every word and every price right, across seeds. Ad: headline,
  bottle, and small line all spelled right and each sitting in its
  box. Name swap: same cup, same light, new name on each.

**Why**
Quoted words control spelling; boxes control placement; same-seed
brackets control variation. Each mechanism answers a different
question (what words, where, which variant), and conflating them is
how text renders go wrong.

### Phase 5: Know the three honest failures, then work with your own pictures

**Do**
1. Failure 1, words you did not give: a sign or poster in the
   background can come out with made-up letters. Fix: give the words
   in double quotes, or let the workflow-2 helper write them.
2. Failure 2, editing: MOSS is not an edit model. "It does not change
   an image you give it." In the creator's edit/restyle tests it did
   not keep the image (hair and face changed). No edit workflow is in
   this episode; the creator points to FLUX 3 Klein (Ep39) or FLUX 2
   for edits today, and notes MOSS edit LoRAs were emerging but not
   supported in a normal ComfyUI release at recording time.
3. Failure 3, big sizes: asking for a big size directly gives a
   different image (same prompt and seed, 2048 gave a different
   person). Fix: find the image at normal size, then enlarge with
   workflow 8.
4. Workflow 7, image to prompt to image: load an image (creator's: a
   small bakery with its name on the sign); the text encoder looks at
   it and writes a detailed prompt in about 2 seconds; pick 1536 when
   the image has small words so the AI sees them bigger. Result is a
   new image, not a copy ("Rosie's bakery came back right, but it's a
   new image"). Add a change at the end of the idea in the AI prompt
   (e.g. "but at night with warm light in the window").
5. Workflow 8, upscale 2x keeping the picture: make the image in
   workflow 1, paste the same prompt, same size, same seed; step 4
   denoise for the second pass, 0.35 is a good start. About 50 seconds
   on the creator's card; the example goes to 2048x2560 with real
   detail in hair, beard, and latte art, sign staying right.
6. Workflow 9, upscale any picture: load any image, pick the size
   before it doubles (1024 becomes 2048), denoise 0.25 is a good start
   (0.15-0.20 for small faces in a group photo). Needs one new file,
   an upscale model in upscale models. About 30 seconds. Caveats:
   it repaints lightly, so small details can change; it does not
   repair (scratches on an old photo stay); on photos skin and hair
   can come out too smooth ("With the upscale model alone, the skin
   looks plastic. The MOSS pass helps a little, but it still doesn't
   look like real skin"); illustrations and 3D images benefit most.

**Check**
- Upscale check: same barista, same sign, more detail, not a different
  person. Edit check: if the face changed, you asked an edit question
  of a generation model; use the FLUX route instead.

**Why**
Every failure here has a named workaround that respects what the
model is: generate at normal size then upscale, quote the words you
want, and never ask MOSS to edit. The episode's honesty about failures
is what makes the nine workflows trustworthy.

### The human method, distilled
1. Quote every word that must be spelled right; never let the model
   guess small text.
2. Use boxes for placement, same-seed brackets for variants, and the
   full workflow (not the speed LoRA) for finals.
3. Read the helper's shown text before running: invented dates and
   details are visible there, before they are baked into an image.
4. Generate small, then upscale; never generate big directly, and never
   ask a generation model to edit.

**Depth status:** FULL (full captions + description, 9 workflows with
settings, timings, and failure modes; creator's GPU model is not stated
in captions, so timings are reported as "on the creator's card", and
ASR name garbles are not quoted as terms).

## Have-vs-need tables

Status key: HAVE = repo evidence cited in its inventory; PARTIAL = repo
has a weaker/manual version; NEED = absent in the inventory (not
"probably missing"). Recommendations are per repo, not global.

### Aegis (primary)

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| ComfyUI app-bundle format (app.json + API workflow, generated UI/downloads/VRAM/tests) | Audit 1 (Freefield) | NEED | Inventory: intake/ concept-to-input, no app-bundle format, no generated VRAM map | Backlog: the format is the portable idea; adopt the one-folder-per-app shape for intake tools before adopting any single model |
| Fixed-seed lab QA with published time + peak VRAM per app | Audit 1 | NEED | Inventory: QA gates + multi-view render QA exist, but no per-output fixed-seed lab with published pass rate | Adopt now (pattern): add a lab-style pass-rate gate to intake; this is the acceptance-spec pattern, see gap alert |
| MiniMax H3 native 3MP low-VRAM stack (INT8, DMAD 4-step, sparse 0.10, 4096 chunks) | Audit 7 | NEED | Inventory: no AI-video stage; trailer use is future | Watchlist: relevant only when Aegis needs a trailer; the stack's value is its published settings, not its subject |
| MOSS Image text-rendering workflows (quoted words, layout boxes, same-seed variants) | Audit 8 | NEED | Inventory: no text-rendering image stage in foundry | Watchlist: intake-side candidate for posters/covers with legible text; expands existing moss skill, not a foundry stage |
| GPU impostor crowd rendering (near rigged, far impostors) | Audit 2 | PARTIAL | Inventory: LOD generation in foundry, deterministic Rust zone sim with SoA store in backend; no crowd impostor stage | Backlog: pattern for any future large-crowd scene; not a foundry fill |
| Rigging/skin/retarget stage | Audit 2 (Mixamo near-field only) | NEED (unchanged) | Inventory: explicitly absent; P1 gap row stands | No change: do not mark HAVE on Mixamo use in a demo |
| Per-asset perf budgets | Audits 2, 3 (FPS figures, open vert question) | NEED (unchanged) | Inventory: explicitly absent; P1 gap row stands | No change: FPS is not a per-asset budget |
| Software JIT raytracer / L1 SH GI | Audit 4 | NEED | Inventory: OptiX baking exists, no software JIT raytracer | Skip: retro-engine research, not a foundry stage |
| Blender-to-Minecraft live export | Audit 5 | NEED (unverified claim) | Inventory: UE packaging stage, no Minecraft export | Skip until the author publishes the add-on |

### 2d3d

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Godot shader-window city (boxes + window shader, 256 m culling tiles) | Audit 3 | PARTIAL | Inventory: projection painting + shaders/projection.gdshaderinc, proc texture generators; no procgen city stage | Backlog: shader-window trick is transferable to 2d3d's 2D/3D camera work as a background-city method, not as a core pipeline |
| Godot window/raindrop shader (heightmap slopes, torus desync) | Audit 6 | PARTIAL | Inventory: projection shaders exist; no weather/window shader | Watchlist: weather-feel technique for future scenes |
| Godot 1M-agent SoA crowd | Audit 2 | NEED | Inventory: Godot 4.7.2 Mobile renderer, Jolt; no crowd sim | Skip: 2d3d is a side-scroller, not a crowd sim; pattern only |
| Freefield app-bundle + lab QA | Audit 1 | NEED | Inventory: 286 gdUnit4 cases, 198 QA gates, manifest/provenance installer; no app-bundle lab | Backlog: lab pass-rate reporting is a QA-reporting pattern 2d3d's gates could borrow |
| Asset import validation gate | (none this run) | NEED (unchanged) | Inventory: roadmap rec 9, P1 gap row stands | No change |
| Production conversion (retopo/UV/rig/LOD/compression) | (none this run) | NEED (unchanged) | Inventory: roadmap rec 20, P1 gap row stands | No change; audit 5's unverified Minecraft export is not a conversion stage |

### Desktop City

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Shader-driven city fill (shader windows on plain boxes) | Audit 3 | NEED (pattern match) | Inventory: no skyline-fill equivalent; every building authored/generated; P1 gap row stands | Adopt now (pattern): prototype shader-window boxes as distant skyline fill behind sprite cities; see gap alert. Full adoption needs a sprite-rendering test, since Desktop City ships sprites, not 3D scenes |
| Procgen city generation (56 m grid, random heights/colours) | Audit 3 | PARTIAL | Inventory: tools/procedural_art.py, building_families.py, facade_parts.py, city_* family; generation exists in 2D sprite form | Backlog: grid + random-height rules are already the shape of Desktop City's generators; the new piece is the shader, not the grid |
| MOSS text-rendering workflows | Audit 8 | NEED | Inventory: sprite contract + standards, no AI text-image stage | Watchlist: posters/menus for in-game signage art, if ever AI-generated |
| Freefield 117-app bundle | Audit 1 | NEED | Inventory: standalone tools/, no app-bundle format; PRD DEC-12 forbids requiring Aegis services | Skip as a dependency; borrow the one-folder format only if a local tool bundle is ever wanted |
| 1M-agent crowd / JIT raytracer | Audits 2, 4 | NEED | Inventory: cozy idle city-builder; no crowd sim or raytracer | Skip |

### Solarempire

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Godot 1M-agent SoA + impostors | Audit 2 | PARTIAL | Inventory: Godot 4.7.x native client direction (ADR 0016), per-class export profiles, LOD0-LOD3 + HLOD proxy; no crowd sim | Watchlist: impostor pattern is adjacent to its HLOD proxy thinking, for fleet scenes if counts ever grow |
| Godot shader city / window shader | Audits 3, 6 | NEED | Inventory: Blender asset pipeline stages (audit/prepare/segment/retopo/rig/uv/bake/lods/export); no Godot shader city stage | Watchlist: background-city and weather shaders for the Godot client, after the client exists |
| Freefield lab QA pattern | Audit 1 | PARTIAL | Inventory: per-asset audit + optimization reports with measured figures (e.g. 3,104,038 tris to 299,998-tri LOD0) | Backlog: Solarempire already publishes measured reports; Freefield's fixed-seed pass rate is the one reporting habit it lacks |
| Godot import validation gate + re-measured export budgets | (none this run) | NEED (unchanged) | Inventory: ADR 0003, P1 gap row stands; no Godot project yet | No change |
| MiniMax H3 / MOSS / CyberVGA | Audits 4, 7, 8 | NEED | Inventory: Meshy GLB + concept PNG pipeline; no AI-video or software-raytracer stage | Skip for the asset pipeline; trailer/marketing use only |

## Watchlist trending

Note on method: `bin/trend_watchlist.py` over-matched again this run
(bare "ComfyUI" / "MiniMax H3" tokens annotated unrelated rows such as
Scumble, the ComfyUI Asset System, Pocket AI, SelfLift, SyncTile, Chain
Director, RefMod, the storyboard-grid row, and the documentary-pipeline
row). Those 21 annotations were reverted before saving, following the
2026-10-27 precedent; only the genuine reappearances below were kept.
The script's raw snippet is therefore NOT pasted verbatim, because it
contains false reappearances.

Genuine reappearances (applied 2026-10-28):

- AI video generation (MiniMax H3) (first seen 2026-09-27, WATCH):
  audits 1 and 7 both run MiniMax H3; fourth straight week of MiniMax
  H3 as the dominant AI-video tool in the scan.
- ComfyUI custom nodes wrapping intake/ stages (2026-09-27, WATCH):
  Freefield is built entirely as ComfyUI apps plus the Comfy SDK.
- Shader-driven skyline fill (2026-09-27, WATCH): audit 3's shader
  city is a new, concrete instance of this row, and the P1 gap alert
  above.
- FLUX 3 Image Klein (2026-10-16, WATCH): Freefield uses FLUX 3 Klein
  for Create Image (role: product image model inside the bundle, not
  the standalone announcement post).
- MOSS-Image (2026-10-21, WATCH): audit 8 is the Ep40 workflow pack
  for the same model (role: 9 free workflows, not the release post).
- Qwen Image Edit (2026-10-23 row, WATCH): Freefield lists
  Qwen-Image-Edit in its open-weights roster (role: one model among
  nine in the bundle, version not stated as 2.1 in the Freefield post;
  the row's 2.1 version tag is the earlier post's, not Freefield's).

New watchlist additions (append-only, 7 rows):

- Freefield: Higgsfield rebuilt on ComfyUI (117 apps, MIT).
- Godot 1M-agent ECS-style SoA crowd + GPU impostors (Godot 4.6 C#).
- Godot procgen shader-window city (SurfaceTool boxes, no window
  textures).
- CyberVGA JIT software raytracer (SSE, L1 SH GI, no GPU).
- MiniMax H3 native 3MP low-VRAM recipe (INT8, DMAD 4-step, sparse
  attention).
- Godot window + raindrop shader (per-pane torus sampling, heightmap
  normals).
- Blender creature animation to live Minecraft blocks add-on
  (unverified; title claim only).

## Gap recommendations (highest-leverage NEEDs)

1. **Prototype shader-window skyline fill for Desktop City (audit 3,
   P1).** Next step: render a test strip of SurfaceTool-style boxes
   with the 3.6 m floor shader through Desktop City's Blender sprite
   path and compare it against an authored skyline at the game's fixed
   view. If it reads at sprite resolution, the P1 gap closes as a
   background method; if it does not, the gap stays open with evidence.
2. **Borrow Freefield's lab reporting for Aegis intake (audit 1, P1
   pattern).** Next step: pick one intake tool, run it on fixed seeds,
   and publish example + time + peak VRAM + pass rate in its report.
   That single report is the acceptance-spec template; do not write a
   spec document first.
3. **Keep the 1M-agent impostor rule as a design rule, not a tool
   (audit 2).** Next step: wherever a future scene needs crowds, write
   the rule into its design doc now (simulate all, fully render near,
   impostor far, cost scales with camera distance) so no scene is
   designed around rendering every agent.
4. **Bank the MiniMax H3 3MP recipe as the low-VRAM reference (audit
   7).** Next step: when any trailer or video task hits a 12 GB card,
   start from INT8 + DMAD 4-step + sparse 0.10 + 4096-row chunks and
   record whether the 33-minute/243-frame budget reproduces, instead
   of re-deriving a low-VRAM stack from scratch.
5. **Do not chase the Minecraft add-on (audit 5).** Next step: none,
   until the author publishes a link. Any follow-up that treats the
   title as a verified tool would repeat the exact proxy-trust failure
   this scout is built to avoid.

## Explicit non-goals (found but correctly skipped)

- "Mastery of Blender?" and the winter-biome naval game: showcase /
  question posts with no workflow; engagement alone does not make a
  pipeline finding.
- "Despair physics": a real principle (fully simulated puppet, balance
  controller placing feet and stiffening joints from momentum) with no
  parameters, solver, or code; reportable as an idea, not executable.
- Claude + Remotion + PixelLab.ai cutscenes: prompts quoted, pipeline
  settings absent; a proof of concept, not a cutscene pipeline.
- CyberVGA (audit 4) as a product: fascinating render tech, but a
  retro software engine is not a stage any of the four repos needs.
- The 12 overlapping posts: already covered 2026-10-27; re-auditing
  them would double-count one week's evidence as two.

## skill_library artifacts staged

Staged in `~/workspace/video-tooling-scout-public/` (push is the
separate 09:18 daily-push step; this run does not push, and the known
token block stands: the staged `.github/workflows/ci.yml` still needs
Workflows read/write on the skill_library token, so a push that
includes it will fail with the same 403 seen 2026-10-25 and
2026-10-27 night; the 09:18 push must still exclude ci.yml or it will
fail on that file):

- NEW `automation/freefield-comfyui-higgsfield-clone` (audit 1).
- NEW `engine-runtime/godot-1m-agent-ecs-impostors` (audit 2).
- NEW `procgen-worlds/godot-procgen-shader-city` (audit 3).
- NEW `engine-runtime/cybervga-software-raytracer-jit` (audit 4).
- NEW `ai-video/minimax-h3-native-3mp-lowvram` (audit 7).
- NEW `materials-shaders/godot-window-raindrop-shader` (audit 6).
- EXPANDED `ai-video/moss-image-comfyui-recipe` (audit 8: Ep40's 9
  workflows, version gate, colour convention, speed LoRA, layout boxes,
  same-seed variants, three failure modes, both upscales).
- Audit 5: no skill (NO-TOOLING, report only, per the skill's step 8).
- Full report copied to `docs/scout-reports/have-vs-need-2026-10-28.md`
  in the staging mirror, with the scout-reports index updated, the
  watchlist rows synced to the mirror's
  `video-tooling-scout/references/tooling-watchlist.md`, and README
  category counts updated (126 to 132 skills: automation 13 to 14,
  engine-runtime 30 to 32, procgen-worlds 21 to 22, ai-video 19 to 20,
  materials-shaders 11 to 12).
