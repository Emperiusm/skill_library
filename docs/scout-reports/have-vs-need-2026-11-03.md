# Video tooling scout: have-vs-need 2026-11-03

Run: daily-video-tooling-scout, 2026-11-03 08:18 EST. Depth mode: pre-approved (max 2 media downloads; 2 attempted, status below).
Reddit scan: 55 video posts across 23 subreddits (2026-11-01 to 2026-11-03), Arctic Shift API. One subreddit (GraphicsProgramming) warned once (HTTP 522) but returned results via fallback.
YouTube scan: 11 channels in the last 2 days (yt-dlp, certifi bundle was stale after the sandbox proxy CA rotation; refreshed per AGENTS.md, then all 11 channels scanned clean).
Deep analyses: 8 (cap).

## Gap alerts

None. No extracted tool fills any row in references/p1-gaps.md this run:
- The meshlet pipeline post (1xmncnq) is engine-level rendering, not an Aegis intake/foundry stage; it does not fill the P1 mesh-compression, perf-budget, or mesh-refinement gaps (no budgets, no deviation metrics, no pipeline artifact).
- IV Studio's MCP GPU controls (1xmp6dh comment) are infra automation (start/stop RunPod/Modal GPUs), not the P2 agentic-DCC loop (agents driving Blender/UE and iterating visually). Related, not a fill.
- The Godot tool stack post (1xmk0uz) names TrenchBroom/Blockbench/GIMP but discloses no import-validation, budget, or QA procedure; it does not touch the 2d3d or Solarempire P1 import-gate gaps.
- EasyComfee V2 / the open-source ComfyUI video app are studio UIs on ComfyUI, not acceptance specs.

## Audits

### 1. "~2 billion triangles (mostly instanced) at 60 fps with the new MeshletDrawingPipeline in three.js r187" (Sara_KumoDeck)

Source: https://www.reddit.com/r/threejs/comments/1xmncnq/2_billion_triangles_mostly_instanced_at_60_fps/ | r/threejs post 1xmncnq (score 32, 1 comment) | native Reddit clip (v.redd.it)

Tools used: three.js r187, WebGPURenderer, `MeshletDrawingPipeline` (PR #35191 by sunag); procedural sandstone canyon + ruined temples scene (1,967,478,960 triangles), low-camera flythrough stress test.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: let the GPU cull clusters before rasterization so instance count stops being the bottleneck.

### Phase 1: Build the stress scene

**Do**
1. Procedurally generate a sandstone canyon with ruined temples (tool undisclosed in retrieved text).
2. Populate it with instanced meshes until the scene holds 1,967,478,960 triangles, per the author's on-screen counter.
3. Fly a low camera through the canyon for the stress path.

**Check**
- The triangle counter on screen is the verification; the author publishes the exact number (1,967,478,960), not a round estimate.
- Sustained 60 fps during the flythrough.

**Why**
Mostly-instanced geometry means the same few meshes repeat; the cost is in draw submission and vertex processing, which is what the pipeline attacks.

### Phase 2: Switch the renderer to the meshlet pipeline

**Do**
1. Use three.js r187's WebGPURenderer with `MeshletDrawingPipeline`.
2. Each geometry is split once into clusters (the post body truncates at "into cl"; meshlets = small clusters of triangles processed as a unit, the standard definition). [Inference: the remaining mechanism was not retrievable; labeled as such.]

**Check**
- Compare fps before/after the pipeline switch at the same triangle count.
- The author reports the pair (1.967B tris, 60 fps) as the headline result.

**Why**
Meshlet/cluster culling rejects whole clusters on the GPU before vertex processing, so triangles behind the camera or smaller than a pixel never cost rasterization time. Instancing plus cluster culling is what makes 2 billion triangles feasible.

### The human method, distilled
1. Benchmark with the extreme case first: build a scene far past what you need, then measure. The counter is exact because the claim is extreme.
2. Ship the measurement, not the adjective: "~2 billion triangles ... at 60 fps" is the whole post.

**Depth status:** DEPTH-LIMITED (post body truncated by the scan at "into cl"; old.reddit and PullPush post-body routes both blocked this run; only 1 praise comment retrievable). A media download would not add tooling detail here (native clip, no captions expected); the missing piece is the author's writeup, which no download recovers.

Tooling extracted: `MeshletDrawingPipeline` (three.js r187, PR #35191 by sunag) — genuinely new watchlist entry. No repo uses three.js/WebGPU as an engine today, so this is pattern-only for Aegis (GPU-side culling) and the Godot repos (render budgets). Concrete benchmark data (2B tris / 60 fps) is per-asset-budget-adjacent evidence for the Aegis P1 perf-budget gap but does not fill it (no tri counts, texel densities, or budgets proposed for any repo pipeline).

### 2. "Robotic hands that play any MIDI file on a piano in real time" (enamore22)

Source: https://www.reddit.com/r/threejs/comments/1xmfm6f/robotic_hands_that_play_any_midi_file_on_a_piano/ | r/threejs post 1xmfm6f (score 159) | 25 of 31 comments retrieved | native Reddit clip

Tools used: three.js (WebGL render), Claude Opus 5.5 (the author built the whole thing with it), custom MIDI parser + fingering solver (author's own code), Blender (tooling-hit, role undisclosed; likely the hand models).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: precalculate which finger plays every note, drop what cannot be played, then render.

### Phase 1: Parse the MIDI into playable events

**Do**
1. Read any MIDI file (author tested Westworld intro, Severance TV intro, Debussy Clair de Lune, Rush E).
2. Expand each note to pitch, start time, duration, velocity.
3. Detect "impossible" notes in a fingering precalculation pass and drop them, rather than failing mid-performance.

**Check**
- Clair de Lune test: about 160 keys beyond reach; the piece still played well "all things considered", per a commenter who tried it.
- Rush E test: hands jump around and collapse in the crazy sections. The author: "I didn't care to handle that insanity."

**Why**
A robot that attempts everything looks broken on impossible input; a robot that visibly drops impossible notes looks deliberate. The precalculation is the product: realtime input is an open question (author: "The fingering requires precalculation though. I should try and see what the lag is like.").

### Phase 2: Assign fingers with thumb special-casing

**Do**
1. Assign each playable note to a hand and finger in the precalculation.
2. Special-handle thumbs on overlapping notes; tuck the thumbs when the hands come close together (author's own fix, stated in comments).

**Check**
- Watch the 5:46 mark (commenter-verified): both thumbs take turns on the same key.
- Pinky joints lighting up around 0:25 was lighting reflection, not keystroke highlighting; a commenter asked for actual note-light-up as a feature request.

**Why**
Thumbs collide in close hand positions; generic finger assignment produces interpenetration. The author fixed the specific failure he saw instead of generalizing.

### Phase 3: Render cinematically in three.js

**Do**
1. Animate the robot hands against the MIDI timeline.
2. Use cinematic camera motion (commenters single this out: "can't remember the last time I saw something this cinematic in 3js") with a Westworld-intro aesthetic.

**Check**
- Commenter test: feeding the Westworld MIDI "worked out great"; feeding the Severance intro produced the collapsing/blurring the author warned about. The render is deterministic per input, not cherry-picked.

**Why**
Realistic finger motion is the whole point (the author was annoyed by unrealistic piano playing in media); the cinematic camera sells the Westworld riff.

### The human method, distilled
1. Fix the specific visual failure you see (thumb tucking), not the general case.
2. Drop impossible input loudly in precalculation rather than attempting it live.
3. Let users bring their own MIDI: three commenters tested their own files, which is stronger verification than any demo reel.

**Depth status:** PARTIAL (post text + 25/31 comments; no code, parameters, or model sources; Blender's role undisclosed).

Tooling extracted: Claude-Opus-built MIDI fingering solver with impossible-note dropping and thumb special-casing. No attach point in any repo pipeline (not an asset tool; SKIP), but the precalculation pattern (reject impossible input before the expensive step) is a portable design principle for validation gates.

### 3. "Fake frustum culling shader" (partybusiness)

Source: https://www.reddit.com/r/godot/comments/1xm802w/fake_frustum_culling_shader/ | r/godot post 1xm802w (score 56) | 13 of 14 comments retrieved | native Reddit clip

Tools used: Godot 4 (shader + GDScript), test statues from the Scan the World project (MyMiniFactory "Cicero" 3D print by the author of the post).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: discard pixels the reference camera cannot see, to visualize what real frustum culling removes.

### Phase 1: Build the camera-discard shader

**Do**
1. Write a Godot shader that discards pixels not visible to a given camera.
2. Pass the camera data (projection matrix, transform) from a GDScript to the shader as uniforms.
3. Compute per-pixel visibility: the author changed one line to `view_pos = (camera_projection_matrix * camera_transform_matrix * MODEL_MATRIX * vec4(0.0, 0.0, 0.0, 1.0)).xyz;` (testing the origin point).

**Check**
- Statues vanish when the reference camera cannot see them. The author admits "there's no performance benefit" — it is a visualization, not an optimization.
- Failure noted by the author: testing a single point makes objects disappear too soon when half on-screen.

**Why**
The point is pedagogical: show what real frustum culling would remove. Discarding per-pixel is the simplest correct visualization.

### Phase 2: Correct toward real culling behavior (community)

**Do**
1. Test against the mesh's bounds, not one point: pass the AABB as uniforms, since it is "not directly available in the shader" (author).
2. For per-face instead of per-pixel culling, declare `varying flat vec3 view_pos;`.
3. Remember Godot culls on the Mesh AABB, not per-vertex/per-surface (TheDuriel).

**Check**
- TheDuriel: the one-point test pops "too soon, when they're half on-screen ... that's exactly how it works! And why the frustum check usually considers the AABB of the object, and expands the camera frustum by around 20% in all directions."
- In a Godot "mesh", a "surface" is each contiguous strip of vertices/faces sharing a material; a surface is drawn at once, so per-surface is the finest real culling granularity.

**Why**
Real engines test volumes, not points, and pad the frustum (~20%) so edge cases don't pop. The fake shader is most useful when its errors match the real engine's errors.

### The human method, distilled
1. Build the fake version to see what the real system sees.
2. When the fake disagrees with the engine, the engine's rule (AABB + 20% frustum pad) is the spec.

**Depth status:** PARTIAL (post text + 13 comments with one line of shader code; full shader not published).

Tooling extracted: Godot camera-discard visualization shader — genuinely new watchlist row (WATCH). Commenter game-puzzle spin-off (different cameras render different objects; aim them to pass rooms) is a design idea, not tooling. No P1 gap touched (shader trick, not an import/budget/QA stage).

### 4. "EasyComfee V2: an open-source creative studio on top of ComfyUI" (sintetizacom)

Source: https://www.reddit.com/r/comfyui/comments/1xljadr/easycomfee_v2_an_opensource_creative_studio_on/ | r/comfyui post 1xljadr (score 46) | 14 comments retrieved | native Reddit clip

Tools used: ComfyUI (backend), EasyComfee V2 (author's open-source studio app, one-click install); Higgsfield.ai UI as the design reference.

This audit reconstructs what the evidence supports; it is deliberately thin because the evidence is thin.

### Phase 1: Ship a studio UI over ComfyUI

**Do**
1. Wrap ComfyUI workflows in a user-friendly, simple-to-install interface (author: "Installation happens with one click").
2. Copy the Higgsfield UI's colors and design language (commenter observation across all competition submissions: "they all copy Higgsfield's UI colors and design"; author confirmed the reference is "Higgsfield.ai").
3. Develop theme (color) selector next (author's stated next step).

**Check**
- Author's bar: a satisfactory result "despite the limitations of my machine" — low-spec machine compatibility is a stated goal.
- A commenter asked for the workflow to be shared; it was not posted in the retrieved comments.

**Why**
The thesis is onboarding: new users should not need 30 nodes and multiple text encoders for a simple lipsync (a commenter's literal question). The UI is the product.

### The human method, distilled
1. One-click install is the feature; the workflows underneath are commodity.
2. If your machine is weak, say so: it sets the performance bar honestly.

**Depth status:** DEPTH-LIMITED (post body blocked; comments are social + support; no workflow, nodes, or parameters disclosed). A media download would not add tooling detail (native clip, no captions expected).

Tooling extracted: EasyComfee V2 (open-source Higgsfield-UI-clone studio on ComfyUI) — new watchlist row, WATCH. Same class as FrameForge (2026-10-29 row, also a Higgsfield Build Competition entry); note the cluster, don't merge (different authors, different apps).

### 5. "I built a free, open-source film studio on top of ComfyUI + MiniMax H3" (r/comfyui post 1xmp6dh)

Source: https://www.reddit.com/r/comfyui/comments/1xmp6dh/i_built_a_free_opensource_film_studio_on_top_of/ | r/comfyui post 1xmp6dh (score 37) | 1 comment retrieved | native Reddit clip

Tools used: ComfyUI + MiniMax H3; the product is called "IV Studio" (name surfaces only in the single comment: "Can an MCP tool start or shut down a RunPod or Modal GPU, or are those controls only in IV Studio's UI?"); MCP tooling for GPU lifecycle on RunPod/Modal.

Workflow: idea to finished short film inside one open-source studio app. No phases recoverable from the evidence: the post body was blocked (old.reddit bot-walled, PullPush 522) and the only comment asks about MCP GPU start/stop controls, which implies the app exposes MCP tools that start/shut down RunPod or Modal GPUs, or that those controls live only in its UI.

**Depth status:** DEPTH-LIMITED (1 comment; post body unavailable; app name itself is commenter-supplied). A media download would not recover the workflow (native clip); the missing piece is the post body and the repo link.

Tooling extracted: IV Studio (open-source ComfyUI+H3 film studio, MCP GPU lifecycle) — new watchlist row, WATCH. MCP GPU start/stop is adjacent to the P2 agentic-DCC gap (infra automation vs agents driving DCCs) — related evidence, not a fill; no gap alert.

### 6. "I replaced the in-scattering in a cloud raymarch with a tiny neural network" (r/GraphicsProgramming post 1xlt1w6)

Source: https://www.reddit.com/r/GraphicsProgramming/comments/1xlt1w6/i_replaced_the_inscattering_in_a_cloud_raymarch/ | r/GraphicsProgramming post 1xlt1w6 (score 640) | 25 of 51 comments retrieved | native Reddit clip | cross-posted as 1xlt59n (score 48, 5 comments)

Tools used: custom cloud raymarcher (engine undisclosed in retrieved text), a tiny neural network replacing the analytic in-scattering function.

This audit reconstructs the approach and, unusually, the community's technical verdict, which is the most valuable part of the evidence.

### Phase 1: Swap the analytic in-scattering for a learned one

**Do**
1. Train a tiny neural network to approximate the in-scattering term of the cloud raymarcher.
2. Compare against the author's own analytic baseline and a ground truth.

**Check**
- The author's claim (from the truncated title): "then che[cked/compared]..." — the comparison is the post.
- Community audit of the comparison (James20k, score 4): the implementation looks broken — likely an sRGB/linear mixup — so the "ground truth" comparison is invalid and "analytic cloud models are way better than this."

**Why**
In-scattering is expensive per march step; a tiny NN could be cheaper than evaluating the analytic model if it generalizes.

### Phase 2: Read the expert pushback before adopting

The retrieved thread is a substantive technical review, worth preserving verbatim in spirit:

- Worth-Competition134 (score 8): the comparison lacks multiscattering and "a few hacks for the analytic model, which artificially boosts your arbitrary target"; shipped cloud raymarchers cost "around a millisecond ... for the entire sky ... back on Xbox One". "Instead of reinventing the wheel, which so much of this 'neural' stuff is..."
- blackrack (score 2): "for something like this it'd be better to precompute a small radiance table, unless OP is willing to put in enough training and data to generalize the neural network."
- PyroRampage (score 8): "Neural graphics like NERFs for example or Gaussian Splats ... are literally overfit per scene" — generalization is the crux; a per-scene overfit NN is not a technique, it is a bake.
- wektor420 (score 4): KANs (Kolmogorov-Arnold Networks) "were designed for such uses."
- brownianhacker: try L0/L1 sparsity on weights to shrink layer sizes; genetic algorithms are slower than backprop for this.
- heliosythic: was implementing Horizon's Nubis system from the papers and stalling; "training a NN sounds like a fun detour. But the performance hit is unfortunate."
- deftware (score 2): the analytic model "just needs more retro-reflectivity to be closer to ground truth"; and the closer: "nothing ever needs to be 'accurate', it only ever needed to be good enough to fool someone's eye."

### The human method, distilled
1. When the NN beats your baseline, suspect your baseline first (sRGB/linear, missing multiscattering).
2. A neural replacement that only works per-scene is a bake with extra steps; ship a precomputed radiance table instead.
3. "Good enough to fool someone's eye" is the actual acceptance criterion.

**Depth status:** PARTIAL (post snippet + 25/51 informed comments; no network architecture, layer sizes, training data, or timings disclosed).

Tooling extracted: tiny-NN in-scattering replacement — new watchlist row, WATCH, with the community verdict attached (loser vs analytic + precomputed tables on current evidence). No P1 gap touched.

### 7. "We open-sourced our video app that runs on your ComfyUI (H3 VFX LoRAs, Qwen, Flux)" (devdef)

Source: https://www.reddit.com/r/comfyui/comments/1xmnxtj/we_opensourced_our_video_app_that_runs_on_your/ | r/comfyui post 1xmnxtj (score 49) | 5 comments retrieved | native Reddit clip

Tools used: ComfyUI server as render backend; MiniMax H3 VFX LoRAs, Qwen, Flux (model stack from the title); the app self-installs a portable ComfyUI + all models.

Workflow from the comments:
1. Install the app; it installs a portable ComfyUI version and all models for you — "you don't need to use the ComfyUI gui" (devdef, author).
2. The app drives the ComfyUI server as a headless render backend.
3. It also runs the user's copy and cloud models ("It runs my copy and my cloud models. No side code needed." — skulleyb, who built a Claude skill driving it; "Did this using Claude and made it a skill").
4. Open question from a commenter: is it fully plug-and-play so ComfyUI can be ignored completely?

**Depth status:** DEPTH-LIMITED (post body blocked; 5 comments; the app's own name never appears in the retrieved text). A media download would not add workflow detail (native clip).

Tooling extracted: unnamed open-source ComfyUI video app (self-installing portable backend, H3 VFX LoRAs / Qwen / Flux) — new watchlist row, WATCH. The Claude-skill angle (agentic control of the app, no side code) is adjacent to the P2 agentic-DCC gap; note as related evidence, not a fill.

### 8. "Part 1: How to Make Tacos in Blender" (Ryan King Art) — deepened pipeline

Source: https://www.youtube.com/watch?v=kw86xAKwW04 | Ryan King Art | 1,398 s | 4,141 views | uploaded 2026-11-02 | Part 2 ("nrHKyMnUI74", uploaded 2026-11-03, 94 views) covers the fillings and was not audited

Tools used: Blender (version not verifiable from frames), Luminance HDR 2.6.1 (HDRI browser), `small_hangar_02_1k.hdr` (hangar-interior environment), author's "Ultimate Materials" asset library (backdrop), author's Gumroad store (ryankingart.gumroad.com). Render settings frame-verified: 2048x2048, 100%, 24 fps.

Depth-escalation record: download #1 of 2 attempted under the pre-approved allowance; succeeded (36 MB, 720p, no approval gate). 12 frames extracted from the download and reviewed by the scout. Captions: none published (innertube returned "Sign in to confirm you're not a bot"; metadata via oEmbed only). Local Whisper transcription is a local-machine step per the skill (model download uncompletable in the sandbox). Comment thread: praise-only, no corrections or parameters.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: fold a subdivided box into a U-shell, displace it, then let a Voronoi-plus-noise network paint the toast.

### Phase 1: Block the shell from a box

**Do**
1. Start with a cube, scaled into a tall rectangular slab (frame-verified: 630 verts, 768 tris).
2. In Edit Mode, Right Orthographic view, shape it into the shell profile: a half-dome arch, the cross-section of the folded taco.
3. Fold into the U-shell with a slightly irregular lip.

**Check**
- The arch reads as a taco shell from the front before any material. Too tight reads as a bent plane; too loose reads as a bowl.

**Why**
A box keeps the topology a clean grid; the arch profile does the design work before subdivision hides the construction.

### Phase 2: Subdivide and displace

**Do**
1. Add a Subdivision modifier, then a Displace modifier after it (stack frame-verified).
2. Displace to break the perfect fold: slight waviness so it reads as a real tortilla.

**Check**
- Rendered preview ("Rendering Done", Camera Perspective): gentle surface variation, no faceting. Facets mean subdivision too low; a melted fold edge means displacement too strong.

**Why**
Real tortillas are uneven; a mathematically clean fold is the fastest way to make food look fake. Displacement after subdivision puts imperfection at render density while the base mesh stays editable.

### Phase 3: Light with an HDRI plus one area key

**Do**
1. Set the environment to `small_hangar_02_1k.hdr`, picked by browsing HDRIs in Luminance HDR 2.6.1.
2. Add an Area key light: Emission Strength 3.000, white, 6000K, Square shape, Size 1 m, Spread 180 degrees (all frame-verified).
3. Lock Camera Perspective; the backdrop is a plane.

**Check**
- One soft shadow under the shell; the fold interior reads without crushing. If crushed, raise the HDRI contribution before touching the key.

**Why**
One HDRI plus one key is the whole design; food needs soft wrap, not drama. Auditioning HDRIs in a dedicated browser is faster than doing it inside Blender.

### Phase 4: Paint the tortilla toast with Voronoi plus noise

**Do**
1. Principled BSDF, Roughness 0.600, Specular 0.500.
2. Base Color through a Color Ramp fed by Voronoi Texture (3D, Distance to Edge, Scale 100.000, Detail 0.0, Roughness 0.500, Lacunarity 0.0, Randomness 1.000) plus Noise Texture (Scale 50.000, Detail 12.000), both through a Mapping node (Point, Location/Rotation 0). Frame-verified ramp stop at Position 0.746.
3. Bump node (Strength 1.000, Distance 0.002, Height 0.100 px) into Normal, fed by the same network.
4. Rename the object "Taco Shell"; save as `Tacos Tutorial_1.blend`.

**Check**
- Irregular dark-toast blotches on tan with subtle relief. Uniform dots mean Noise too low; dirty-looking toast means the dark ramp stop too far left.
- Mid-tutorial the shell was flat gray (Hex #ADADAD, Value 0.677): the pre-texture state, not the target.

**Why**
Distance-to-Edge Voronoi makes cell-boundary patterns that read as toast char; Noise breaks procedural regularity. Bump from the same network keeps color and relief registered at 2048px.

### Phase 5: Dress the set with the material library

**Do**
1. From the "Ultimate Materials" Asset Browser library, assign a neutral material to the backdrop plane (Principled, white-ish Base Color, Roughness 0.600, Specular 0.500).

**Check**
- The backdrop falls into a soft gradient; if it competes, it is too dark or too glossy.

**Why**
The backdrop is infrastructure. One drag from the library keeps the tutorial's time on the shell.

### The human method, distilled
1. Spend the modeling budget on the silhouette (the fold); modifiers and materials do the rest.
2. Break procedural perfection twice: in geometry (displace the fold) and in shading (noise over the Voronoi).
3. Light food like a product photo: one big soft source, one HDRI, done.

**Depth status:** FULL (frame-verified; 12 frames reviewed). Caveats: no captions/description existed, so the narration's reasoning is unaudited; Displace texture/strength not legible in frames; Part 2 (fillings) not audited.

Tooling extracted: Voronoi Distance-to-Edge + Noise tortilla-toast recipe; `small_hangar_02_1k.hdr` lighting choice; Ultimate Materials library workflow. New watchlist row (WATCH). Skill `blender-taco-shell-voronoi-tortilla` staged (materials-shaders).

## Per-repo have-vs-need

### Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Meshlet/cluster GPU culling pattern | #1 MeshletDrawingPipeline | NEED | Inventory: UE packaging stage, no meshlet/cluster-culling stage | watchlist: pattern only; no three.js/WebGPU in Aegis |
| Precomputed radiance table over NN in-scattering | #6 cloud raymarch debate | NEED | No cloud/volume rendering in inventory | skip: no attach point; verdict recorded for the record |
| Voronoi+Noise mottling recipe (toast/char) | #8 taco shell | PARTIAL | Foundry has material/texture stages (ORM packing, xatlas UV, OptiX bake); this exact recipe not present | watchlist: technique-transfer candidate for foundry material library |
| ComfyUI studio apps (EasyComfee V2, IV Studio, unnamed) | #4, #5, #7 | NEED | intake/ has concept-to-input generation; no studio UI | skip: AI-video bucket, not intake tooling |
| MIDI-driven animation | #2 robot hands | NEED | No MIDI/score-driven animation anywhere | skip: no attach point |

### 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Godot camera-discard culling visualization | #3 fake frustum shader | NEED | Inventory: shaders/projection.gdshaderinc, no culling-viz tool | watchlist: adopt if visibility debugging arises; the AABB+20%-pad rule is the transferable lesson |
| Voronoi+Noise mottling recipe | #8 taco shell | PARTIAL | pipeline/proc/make_textures.py (seeded procedural textures); this exact recipe not present | watchlist: candidate for make_textures.py recipe set |
| TrenchBroom/Blockbench/GIMP stack | r/godot post 1xmk0uz (not deep-audited) | NEED | No level-editor/mesh-editor stage in inventory | skip: showcase post, no workflow disclosed |
| MIDI-driven animation | #2 robot hands | NEED | No MIDI tooling | skip: no attach point |

### Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Godot camera-discard culling visualization | #3 fake frustum shader | NEED | Godot city renderer; no culling-viz tool cited | watchlist: same as 2d3d |
| Meshlet/instancing perf pattern | #1 MeshletDrawingPipeline | NEED | City-scale instancing; no meshlet stage | watchlist: pattern only (Godot, not three.js) |
| MIDI-driven animation | #2 robot hands | NEED | None | skip |

### Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Godot camera-discard culling visualization | #3 fake frustum shader | NEED | No culling-viz tool cited | watchlist |
| Voronoi+Noise mottling recipe | #8 taco shell | NEED | No procedural-texture recipe cited | watchlist: candidate if surface mottling needed |

## Watchlist trending
- MiniMax H3 Reference-to-Video character swap + motion transfer (ComfyUI, local RTX 5070 Ti) (first seen 2026-10-24, status WATCH; seen again 2026-10-29, 2026-10-31, 2026-11-03) **TRENDING**
- FrameForge (open-source ComfyUI movie app, spacesimeco-hue) (first seen 2026-10-29, status WATCH; seen again 2026-11-03)
- Opsis (self-hosted AI film studio, forms on ComfyUI graphs, Apache) (first seen 2026-10-31, status WATCH; seen again 2026-11-03)
- Godot procgen shader-window city (SurfaceTool boxes, no window textures) (first seen 2026-10-28, status WATCH; seen again 2026-11-03)
- Godot window + raindrop shader (per-pane torus sampling, heightmap normals) (first seen 2026-10-28, status WATCH; seen again 2026-11-03)
- Godot compute-shader creature brain (teninogamestudio, Godot 4.7 C#) (first seen 2026-10-29, status WATCH; seen again 2026-10-30, 2026-11-03) **TRENDING**
- three.js environment perf recipe (compute-shader frustum culling, cross-billboards, alphaTest, Claude-placed godrays) (first seen 2026-10-30, status WATCH; seen again 2026-11-03)
- Godot silk-boss VFX (vector shapes + custom pixelation shader) (first seen 2026-11-02, status WATCH; seen again 2026-11-03)
- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-03, 2026-10-05, 2026-10-08, 2026-10-09, 2026-10-11, 2026-10-16, 2026-10-23, 2026-10-24, 2026-10-27, 2026-10-28, 2026-10-29, 2026-11-01, 2026-11-03) **TRENDING**
- SelfLift dual sampling + Color Transfer stitching recipe (MiniMax H3, ComfyUI) (first seen 2026-10-08, status WATCH; seen again 2026-10-11, 2026-10-16, 2026-10-21, 2026-10-24, 2026-10-29, 2026-11-03) **TRENDING**
- MiniMax H3 no-masking character-swap LoRA recipe (0.4 MP @ 8 steps, 6GB VRAM) (first seen 2026-10-09, status BACKLOGGED; seen again 2026-10-11, 2026-10-16, 2026-10-24, 2026-10-29, 2026-11-03) **TRENDING**
- SyncTile MiniMax H3 single-trajectory long-video nodes (NyckM/Bruxosdovfx-SyncTile-MiniMax-H3-v5.4, v5.5) (first seen 2026-10-23, status BACKLOGGED; seen again 2026-10-24, 2026-10-29, 2026-11-03) **TRENDING**
- MiniMax H3 Chain Director V1.0 (ComfyUI Director node, Single + Chain modes) (first seen 2026-10-25, status BACKLOGGED; seen again 2026-10-29, 2026-11-03) **TRENDING**
- 2x2 storyboard-grid reference prompting for MiniMax H3 (GPT image 2 grids) (first seen 2026-10-27, status BACKLOGGED; seen again 2026-10-24, 2026-10-29, 2026-11-03) **TRENDING**
- Automated AI documentary pipeline (Claude visual bible + Qwen Image 2.1 + Claude QA + MiniMax H3 + Qwen3-TTS + RTX Video Super Resolution) (first seen 2026-10-27, status WATCH; seen again 2026-10-29, 2026-11-03) **TRENDING**
- MiniMax H3 native 3MP low-VRAM recipe (INT8, DMAD 4-step, sparse attention) (first seen 2026-10-28, status WATCH; seen again 2026-10-29, 2026-11-03) **TRENDING**
- MiniMax H3 Face Refiner workflow (cgpixel23, 6GB VRAM) (first seen 2026-10-29, status BACKLOGGED; seen again 2026-11-03)
- MiniMax H3 toy-to-real transition (Time-Ad-7720) (first seen 2026-10-29, status WATCH; seen again 2026-11-03)
- Genjutsu (Higgsfield commercial AI video model) (first seen 2026-10-03, status WATCH; seen again 2026-11-03)
- Freefield: Higgsfield rebuilt on ComfyUI (117 apps, MIT) (first seen 2026-10-28, status WATCH; seen again 2026-10-29, 2026-11-03) **TRENDING**
- ComfyUI custom nodes wrapping intake/ stages (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-03, 2026-10-05, 2026-10-16, 2026-10-21, 2026-10-22, 2026-10-23, 2026-10-27, 2026-10-28, 2026-10-29, 2026-11-03) **TRENDING**
- Scumble (free inpainting editor, own ComfyUI or API keys) (first seen 2026-09-30, status WATCH; seen again 2026-10-02, 2026-10-16, 2026-10-21, 2026-10-29, 2026-11-03) **TRENDING**
- ComfyUI native Asset System (pre-release) (first seen 2026-10-01, status WATCH; seen again 2026-10-02, 2026-10-16, 2026-10-21, 2026-10-29, 2026-11-03) **TRENDING**
- comfyui-minimax-h3-studio (BiggerFishy; SAM3 + color-inversion character-swap workflow, MIT) (first seen 2026-10-03, status BACKLOGGED; seen again 2026-10-09, 2026-10-16, 2026-10-21, 2026-10-29, 2026-11-03) **TRENDING**
- Pocket AI + Tensor Master (mexxmillion ComfyUI front-end + GPU job dispatcher, Vast rentals) (first seen 2026-10-03, status WATCH; seen again 2026-10-16, 2026-10-21, 2026-10-29, 2026-11-03) **TRENDING**
- OmniChar/.char portable character format + ComfyUI-Omnichar node pack (first seen 2026-10-05, status BACKLOGGED; seen again 2026-10-08, 2026-10-09, 2026-10-21, 2026-10-22, 2026-10-29, 2026-11-03) **TRENDING**
- Flux klein 9B/4B distilled variants + CCTech/Flux Klein ComfyUI node pack (first seen 2026-10-05, status WATCH; seen again 2026-10-16, 2026-10-17, 2026-10-21, 2026-10-22, 2026-10-29, 2026-11-03) **TRENDING**
- YEDP Action Director (ComfyUI 3D viewport; Mixamo/FBX/GLB; OpenPose/Depth/Canny/Normal/Shaded/Alpha passes) (first seen 2026-10-05, status WATCH; seen again 2026-10-16, 2026-10-21, 2026-10-29, 2026-10-29, 2026-11-03) **TRENDING**
- RefMod (ComfyUI custom nodes, character identity without LoRA training) (first seen 2026-10-16, status BACKLOGGED; seen again 2026-10-21, 2026-10-29, 2026-11-03) **TRENDING**
- FLUX 3 Image Klein (5.6B, Black Forest Labs, native ComfyUI) (first seen 2026-10-16, status WATCH; seen again 2026-10-21, 2026-10-22, 2026-10-28, 2026-10-29, 2026-11-03) **TRENDING**
- ComfyUI 0.36 native loops recursion bug (PR #16227 / #16556) (first seen 2026-10-21, status WATCH; seen again 2026-10-29, 2026-11-03) **TRENDING**
- Pixaroma FLUX 3 Klein 19-workflow pack (ComfyUI 0.41+, Pixaroma 1.4.223+) (first seen 2026-10-22, status WATCH; seen again 2026-10-29, 2026-11-03) **TRENDING**
- ComfyUI-MAINodes (commenter suggestion, not creator-confirmed) (first seen 2026-10-24, status WATCH; seen again 2026-10-29, 2026-11-03) **TRENDING**
- agentY (free MIT AI agent inside ComfyUI, DCC MCP presets, remotion) (first seen 2026-10-30, status WATCH; seen again 2026-10-31, 2026-11-03) **TRENDING**
- ComfyUI Motion Previs Studio (3D blocking -> control passes -> ComfyUI) (first seen 2026-10-31, status WATCH; seen again 2026-11-03)
- Open-H3-Regenerate-2K ComfyUI wrapper (NVIDIA merged refiner/upscaler) (first seen 2026-10-31, status WATCH; seen again 2026-11-03)
- ComfyUI-ldoi (image-to-3D TripoSG, fp16, low VRAM) (first seen 2026-10-31, status WATCH; seen again 2026-11-03)
- LayerShop (ComfyUI image-editing front-end; v0.17 regions) (first seen 2026-11-01, status WATCH; seen again 2026-11-03)
- sprite_h3 (fmmix, open-source ComfyUI sprite tool) (first seen 2026-11-02, status WATCH; seen again 2026-11-03)

NOTE (scout, 2026-11-03): of the 39 auto-matches above, only "AI video generation (Minimax H3...)" is a genuine reappearance (MiniMax H3 named in 2 new posts: the IV Studio film-studio post and the open-source video-app post with H3 VFX LoRAs). The other 38 were token-overlap false positives (generic "ComfyUI"/"MiniMax H3"/"Higgsfield"/"Godot"/"frustum culling" matches) and are annotated as "not a genuine reappearance" on their watchlist rows. The trend script's **TRENDING** flags on those rows are carried over from prior genuine runs, not earned today.

New watchlist rows this run (8): MeshletDrawingPipeline (three.js r187); EasyComfee V2; IV Studio; open-source ComfyUI video app (devdef, unnamed); tiny-NN in-scattering replacement (with loser verdict); Godot fake frustum culling shader; MIDI fingering precalculation; Voronoi tortilla-toast material.

## Gap recommendations (highest-leverage NEEDs)

No P1/P2 gap alerts this run, so no "adopt now" items. The honest list:
1. Godot camera-discard culling visualization (watchlist): the AABB + ~20% frustum-pad rule is the transferable lesson for 2d3d/Desktop City/Solarempire visibility debugging. Adopt if a culling bug ever needs demonstrating.
2. Voronoi Distance-to-Edge + Noise mottling (watchlist): candidate recipe for 2d3d's `pipeline/proc/make_textures.py` and Aegis's foundry material library when surface mottling is needed.
3. MIDI fingering precalculation pattern (design principle): "reject impossible input in precalculation before the expensive step" ports directly to validation-gate design (2d3d rec 9, Aegis UE gate). Not a tool adoption.
4. MeshletDrawingPipeline benchmark (pattern only): 2B tris at 60 fps via instancing + cluster culling is a reference point for render-budget discussions, not an adoption (no three.js in any repo).

## Explicit non-goals

- Neural in-scattering replacement: community verdict is that it loses to analytic + precomputed tables; recorded as a negative result, not adopted.
- EasyComfee V2 / IV Studio / unnamed ComfyUI video app: AI-video studio UIs; no attach point in any repo pipeline (Aegis intake is asset generation, not film production).
- Robotic MIDI hands: demo, not a pipeline tool; the precalculation principle is the takeaway.
- Ryan King Art "Procedural Marble Sculpt Material" + "Tacos Part 2", Josh Blender Bros "Floaters", Olivio Sarikas voice-typing video: scanned but not deep-audited this run (8-audit cap); Floaters and the marble tutorial are candidates for the next run.
- r/GraphicsProgramming duplicate cross-post 1xlt59n: same neural-cloud content as 1xlt1w6, not separately audited.

## Depth-escalation record

- Mode: pre-approved, max 2 media downloads.
- Attempted: 1 (Ryan King Art Tacos Part 1, kw86xAKwW04). Succeeded: 1 (36 MB 720p, no approval gate, no retry).
- Skipped: 0. Second download not used (8-audit cap reached).
- Local Whisper transcription: not attempted (sandbox cannot download the model; local-machine step per the skill).

## skill_library artifacts staged

- skills/characters/midi-driven-robot-hands-fingering/SKILL.md (new)
- skills/engine-runtime/godot-fake-frustum-culling-shader/SKILL.md (new)
- skills/materials-shaders/blender-taco-shell-voronoi-tortilla/SKILL.md (new)
- docs/scout-reports/have-vs-need-2026-11-03.md (this report)
- video-tooling-scout/references/tooling-watchlist.md (8 new rows synced; 38 false auto-match annotations added; 1 genuine reappearance annotated by the trend script)

## Run notes

- YouTube scan was fully down at run start (all 11 channels SSL-failed: the sandbox egress proxy CA had rotated and the video-summarizer venv's certifi bundle was stale). Fixed per AGENTS.md: refreshed the bundle from /usr/local/share/ca-certificates/hatch-egress-ca.crt (backed up the old bundle as cacert.pem.bak-2026-11-03). All 11 channels then scanned clean, 5 videos in the 2-day window, 0 warnings. Also ran update-ca-certificates + appended the CA to the system bundle for the /usr/bin/python3 path.
- yt_download.py resolves yt-dlp via shutil.which; cron worker envs have no PATH, so the first download attempt failed with FileNotFoundError on the broken local-video-summarizer venv path. Retried with explicit PATH=/home/hatch/.local/bin:/usr/bin:/bin and it worked.
- Reddit full post bodies unrecoverable this run: Arctic Shift posts API rejects the ids param (400), PullPush returned HTTP 522 for all 8 posts, old.reddit.com is bot-walled ("Welcome to Reddit" interstitial). Audits use scan snippets + comments, which the skill anticipates for native Reddit video.
