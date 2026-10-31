# Video tooling scout — have-vs-need, 2026-10-31

Depth mode: `pre-approved` (max 2 media downloads per run, Ehsan 2026-09-27).
Depth-escalation usage this run: **1 download attempted, 1 succeeded, 0 skipped.**
Download #1: Olivio Sarikas "FREE + LOCAL: Image to 3D for LOW Vram"
(https://www.youtube.com/watch?v=0eIjJinYgmk) — no captions existed, so the
deepened pipeline (download + 12-frame review) was the only route to tooling
evidence; it succeeded cleanly with no approval gate. Download #2 was not
needed: every other audited video had full post text and/or author comments.

**YouTube source: BACK ONLINE for this run.** The `scan_youtube.py` CA bundle
(`~/workspace/skills/video-summarizer/.venv/.../certifi/cacert.pem`) had lost
its Hatch Sandbox Egress CA (stale/never appended; system CA has rotated since
the saved copy in `local-video-summarizer/.venv/hatch-egress-ca.pem`).
Appended the current `/usr/local/share/ca-certificates/hatch-egress-ca.crt`
to the bundle per AGENTS.md; all 11 channels scanned clean, 3 videos found in
the 2-day window. Note: YouTube metadata extraction remains degraded — titles
and uploaders resolve, but durations, descriptions, and captions return null
for every video tested (5/5), so the deepened pipeline is currently the only
way to audit YouTube candidates.

## Gap alerts

**No new P1/P2 gap matches this run.** Every extracted tool was checked against
`references/p1-gaps.md` by keyword and by meaning.

One P2 strengthening (not new): the agentY UPDATE post (r/comfyui 1xjbipg)
adds remotion-based motion graphics/video editing, a WorldLabs API update
(high-quality splats from single generated images), an image/video annotation
tool for giving feedback by drawing, and grok-via-OpenAI-compatible-endpoint
setup to yesterday's P2 match ("MCP-driven DCC loop: MCP presets for Blender,
Maya, Houdini, After Effects"). The existing `comfyui-agenty-ai-agent` skill
is expanded with these details this run; the P2 row itself is unchanged.

## Videos scanned and deeply analyzed

Reddit scan: 44 video posts across 23 subreddits, last 2 days (2026-10-29 to
2026-10-31), min score 20. YouTube scan: 3 videos across the 11 configured
channels (RyanKingArt, DefaultCube, Ducky3D, JoshGambrell, MaxHayArt,
BlenderSecrets, GDQuest, KaizenTutorials, Brackeys, Entagma, OlivioSarikas).

Deep analysis (8 cap):

| # | Video (title) | Creator | Source | Sub | Depth |
|---|---------------|---------|--------|-----|-------|
| 1 | I built a real-time vehicle damage plugin for UE5: dents, scraped paint, doors that tear off, shattering glass and dirt, all replicated in multiplayer | Rim2812 (Dmitriy Vergasov) | youtu.be/v8xo_57B3sQ; r/unrealengine post 1xjhp5j (score 50, 5 comments) | r/unrealengine | FULL (author post text + author comments; YouTube has no captions, download not needed) |
| 2 | ComfyUI Motion Previs Studio — 3D Camera Blocking, Character Animation, Open | navarisun | v.redd.it/u1jw4i5q2oyh1; r/comfyui post 1xjr2ia (score 39, 2 comments) | r/comfyui | FULL (author post text, 3,881 chars) |
| 3 | Open-H3-Regenerate-2K for ComfyUI: refinement nodes, noise controls and comparison examples | imlo2 | v.redd.it/li33sky01lyh1; r/comfyui post 1xjbwoe (score 24, 18 comments) | r/comfyui | FULL (author post text + author comments w/ parameters) |
| 4 | Opsis: an open-source, self-hosted Higgsfield-style studio built on ComfyUI graphs (Apache) | sanchezrobertodev | v.redd.it/os8ikk55dmyh1; r/comfyui post 1xjhrq6 (score 21, 6 comments) | r/comfyui | FULL (author post text; comments are snark, no tooling) |
| 5 | 3D Character I did for Zbrush 2027 beta testing program | Clear-Counter-640 | v.redd.it/0ykme5q3vmyh1; r/3Dmodeling post 1xjls24 (score 196, 34 comments) | r/3Dmodeling | FULL (author post text + author workflow comments) |
| 6 | Terrain3D v1.1.0 Released | TokisanGames | v.redd.it/5mj8t8ts6oyh1; r/godot post 1xjrkgv (score 632, 30 comments) | r/godot | FULL (author comments; post has no selftext) |
| 7 | FREE + LOCAL: Image to 3D for LOW Vram | Olivio Sarikas | youtube.com/watch?v=0eIjJinYgmk (Olivio Sarikas, 2026-10-30) | YouTube channel scan | FULL (deepened: download + 12 frames read directly; no captions, no transcript) |
| 8 | Generative Lexicon Press — generative, audio-reactive typography for TouchDesigner | uisato | v.redd.it/xj09h67x5myh1; r/vfx post 1xjgqub (score 20, 1 comment) | r/vfx | PARTIAL (author post text; 4K walkthrough video exists but is uncaptioned and was not deepened this run) |

Also re-audited (skill expansion, not counted in the 8): agentY UPDATE post
(r/comfyui 1xjbipg, Admirable-Agency-578) — expands the existing
`comfyui-agenty-ai-agent` skill.

## 1. "I built a real-time vehicle damage plugin for UE5" (Rim2812 / Crushform)

Source: https://youtu.be/v8xo_57B3sQ ("Unreal Engine Crushform — Vehicle
Damage", uploader Dmitriy Vergasov) | r/unrealengine post 1xjhp5j (score 50,
5 comments) | Fab listing 21b0af9c-2005-4930-9af2-be5cc53c2bd4 | Docs
dmvergasov.github.io/crushform/ | Discord discord.gg/ggVNZhSYdM

Tools used: Unreal Engine 5.6–5.8; lattice-based deformation (a lattice wraps
the car body); dents drawn in the material with World Position Offset; Nanite
(kept working, no fractured meshes); explicitly NO Chaos Destruction;
server-authoritative damage with client-side prediction; Chaos Vehicles
compatible out of the box; generic adapter for other vehicle systems;
Blueprint-only projects supported; full C++ source included. Tested on
Windows.

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: **deform one Nanite asset with a
lattice and draw the damage in the material, so nothing ever fractures.**

### Phase 1: Wrap the body in a damage lattice

**Do**
1. Add the Crushform lattice component to the vehicle; the lattice wraps the
   car body and takes every hit: its direction, speed, and contact area.
2. A pole craters the panel; a wall flattens the nose; a glancing blow drags
   the dent along the side.
3. Measure each hit as the body's change of speed (delta-v), NOT as a force.

**Check**
- Drive into different obstacles at different speeds and angles; dents vary
  with hit direction/speed/contact area, not just hit/not-hit.
- Swap vehicles of different mass; dent tuning stays valid.

**Why**
"a hit is measured as the body's change of speed (delta-v), not as a force,
so tuning doesn't depend on the vehicle's mass." One tuning pass works for
every car.

### Phase 2: Draw dents in the material, keep one Nanite asset

**Do**
1. The material draws dents with World Position Offset. There is no Chaos
   Destruction and no fractured meshes: the car stays one asset.
2. The physics collision crumples along with the visible dents.
3. Paint scrapes off where the metal moved, with scratches and chips around
   the impact.

**Check**
- Verify the vehicle is still a single Nanite mesh in the outliner after
  heavy damage; Nanite keeps working.
- Confirm collision matches the visible dent (drive the wrecked nose into a
  wall — it contacts where the dent is).

**Why**
No fractured meshes means no asset-swapping pipeline, no LOD re-bakes, and
Nanite never breaks. Visual damage and collision damage are the same event.

### Phase 3: Attach the damage vocabulary

**Do**
1. Doors, hood, and trunk swing loose and tear off (separate actors on
   detach, per the feature list).
2. Laminated and tempered glass cracks, shatters, and throws shards.
3. Tyres get contact patch and bulging sidewall.
4. Each wheel reads the physical material under it and sets the dirt it puts
   on the body (dust, mud, snow, water/wetness), plus rolling sound and
   particles. (Author comment: "a car driven through snow ends up with snow
   on it, but the ground itself never changes and weight doesn't come into
   it.")
5. Environment reacts: trees fall, poles bend, fences break into debris.
6. Impact and rolling sounds, plus a layered engine sound.

**Check**
- Drive through snow, then mud; the body accumulates the matching dirt type
  per wheel path.
- Tear a door off; it becomes a separate physical object.

**Why**
Damage is a surface-state system (per-wheel material reads) plus a detach
system (doors/glass), not a single deformation slider. The one-way surface
rule ("surfaces only go one way for now") keeps the simulation cheap.

### Phase 4: Replicate server-authoritative with client prediction

**Do**
1. Run damage server-authoritative with client-side prediction; the driver
   (typo in post: "rver") confirms it.
2. Late joiners receive the same wreck state.
3. Alternatively simulate the car on the owning client.

**Check**
- Two clients hit the same car; both see identical dent patterns after the
  server confirm.
- A player joining mid-session sees the wreck, not a pristine car.

**Why**
Damage state is replicated truth, not a local cosmetic. Late-join
consistency is a first-class feature, not an afterthought.

### Phase 5: Know the limits

**Do**
1. Damage is visual plus collision. Mass, handling, and the engine stay the
   vehicle's own: read the damage (per-side zones, events) and cut engine
   power or pull the steering yourself.
2. Chaos Vehicles works out of the box; other vehicle systems plug in
   through a generic adapter.

**Check**
- A wrecked car still drives with stock handling until you script the
  power/steering cuts from damage events.

**Why**
The plugin deliberately does NOT simulate handling damage — that stays the
game's design decision, exposed through per-side zones and events.

### The human method, distilled
1. "Tuning doesn't depend on the vehicle's mass" — measure inputs in
   mass-independent units (delta-v) so one setup covers the whole garage.
2. "The car stays one asset, Nanite keeps working" — deform and shade the
   existing asset instead of fracturing it into a destruction pipeline.
3. Damage is replicated state from the start; late-joiners get the same
   wreck.

**Depth status:** FULL (author post text + author comments; YouTube has no
captions so the deepened download was not needed — the Reddit post is the
primary breakdown, corroborated by the video title/uploader).

## 2. "ComfyUI Motion Previs Studio" (navarisun)

Source: https://www.reddit.com/r/comfyui/comments/1xjr2ia/ | native Reddit
video v.redd.it/u1jw4i5q2oyh1 | r/comfyui post 1xjr2ia (score 39, 2 comments)

Tools used: open-source, local-first interactive 3D previsualization studio
designed to work alongside ComfyUI. Dual 3D viewports (free-orbit scene
editor + live cinematic camera viewfinder). Camera control: dolly, orbit,
tracking, crane, handheld, whip pan, customizable trajectories. Character
animation: procedural walking, running, jumping, combat actions, gestures,
interactive FK/IK bone posing. Scene building: 3D environments, props,
lighting rigs, reference-image-based scene configuration. Cinematic framing:
adjustable focal lengths, depth of field, aspect ratios, shot composition.
24fps timeline with camera and character keyframes. Control passes: MP4
previsualization, OpenPose skeletons, depth maps, alpha masks, camera
transformation matrices. AI integration: local Ollama/LM Studio models or
cloud models for natural-language scene direction and reference analysis.
ComfyUI API bridge for a MiniMax H3 Ref2VA workflow. Targets video models
with reference inputs: LTX-2.5, MiniMax H3, Seedance.

This audit reconstructs the exact workflow shown in the video, step by step,
so another agent can follow the same process. The video's core method is:
**direct the scene in 3D first (camera + blocking + keyframes), then send
control passes into generation — never prompt blind.**

### Phase 1: Build the scene in 3D

**Do**
1. Assemble the environment, props, and lighting rigs in the free-orbit
   scene editor; use reference-image-based scene configuration to match a
   look.
2. Block character positions with procedural animation presets (walk, run,
   jump, combat, gestures) or pose bones directly with FK/IK.
3. Set focal length, depth of field, and aspect ratio per shot; watch the
   live cinematic camera viewfinder alongside the editor.

**Check**
- The viewfinder shows the exact framing the video model will be asked to
  match.

**Why**
"We have increasingly powerful video generation models, but precise control
over camera movement, character blocking, spatial composition, and action
choreography is still challenging." 3D blocking is the control mechanism
prompts can't provide.

### Phase 2: Keyframe on the 24fps timeline

**Do**
1. Keyframe camera moves (dolly, orbit, tracking, crane, handheld, whip
   pan, custom trajectories) and character animation on a 24fps timeline.
2. Plan every shot before any generation happens.

**Check**
- Scrub the timeline; camera and character motion read correctly in the
  viewfinder at 24fps.

**Why**
Previs is shot planning, not generation. The timeline is the contract the
later generations must honor.

### Phase 3: Export control passes

**Do**
1. Export MP4 previsualization, OpenPose skeletons, depth maps, alpha
   masks, and camera transformation matrices.
2. Optionally use Ollama/LM Studio or cloud models for natural-language
   scene direction and reference analysis.

**Check**
- Each control pass (depth, pose, mask, camera matrix) matches the timeline
  frames 1:1.

**Why**
Control passes are the deterministic bridge between the 3D block and the
stochastic video model. The studio's output is structured data, not just a
video.

### Phase 4: Generate through ComfyUI

**Do**
1. Submit the previs video and reference images to ComfyUI through the
   direct local API bridge (implemented for the MiniMax H3 Ref2VA
   workflow), and view the generated result back in the studio.
2. Target workflow: 3D Scene → Camera & Character Animation → Control
   Passes → ComfyUI → AI Video.

**Check**
- The generated shot matches the previs camera move and blocking; where it
  drifts, adjust the 3D scene, not the prompt.

**Why**
"The whole goal is to escape that prompt spiral of endless retries and bad
takes, and instead block out the scene first, direct the camera properly,
and then send a much clearer setup into generation." (Author, replying to a
music-video use case: "Music videos are a perfect fit for this, especially
when camera motion and shot planning really matter.")

### The human method, distilled
1. Block in 3D before generating a single frame.
2. Export deterministic control passes (pose/depth/mask/camera matrices) as
   the interface to the video model.
3. Iterate on the scene, not the prompt.

**Depth status:** FULL (detailed author post text; comments add only a use-case endorsement).

## 3. "Open-H3-Regenerate-2K for ComfyUI" (imlo2)

Source: https://www.reddit.com/r/comfyui/comments/1xjbwoe/ | native Reddit
video v.redd.it/li33sky01lyh1 | r/comfyui post 1xjbwoe (score 24, 18
comments) | Repo github.com/o-l-l-i/ComfyUI-Olm-Open-H3-Regenerate-2K |
NVIDIA nvlabs.github.io/Sana/Open-H3-Regenerate-2K/ |
github.com/NVlabs/Sana/tree/sol-engine/models/Open-H3-Regenerate-2K |
huggingface.co/Efficient-Large-Model/Open-H3-Regenerate-2K

Tools used: ComfyUI custom nodes wrapping NVIDIA's Open-H3-Regenerate-2K
(published merged adapters, Sharp curve branches, learned latent upscaler).
Refines existing 24fps video or native MiniMax-H3 latents. Adjustable noise,
upscale-only mode, memory controls. Longer clips via independent windows
(visible boundaries possible). Example workflows, test clip, and detailed
comparison images in the repo. Competing option: Kijai's LoRA (author thinks
it contains the refiner only).

This audit reconstructs the exact workflow shown in the video, step by step.
The video's core method is: **take an existing 24fps generation (or H3
latents) and run NVIDIA's merged refiner/upscaler over it with adjustable
noise, in independent windows for long clips.**

### Phase 1: Feed it 24fps video or H3 latents

**Do**
1. Load a 24fps video (the node raises
   `ValueError("H3 refinement expects 24 fps; resample in your video loader
   first")` otherwise — author has since added a feature so the node can
   digest different-fps inputs itself).
2. Or feed native MiniMax-H3 latents directly.

**Check**
- The example: 1344x768 source refined to 2560x1440, two steps from noise
  0.5.

**Why**
The refiner is trained on 24fps H3 output; off-rate inputs break its
temporal assumptions. The author fixed the footgun in the node rather than
documenting around it.

### Phase 2: Set noise and mode

**Do**
1. Choose upscale-only mode (adds texture/definition, minimal change) or
   noise mode; the README compares upscale-only vs noise 0.5 / 0.6 / 0.7.
2. For longer clips, process in independent windows (boundaries may show).
3. Dial memory controls down if VRAM is tight.

**Check**
- Compare the three noise levels on your own footage; faces, jewelry,
  lettering, and small patterns WILL change (commenters: talking and
  emotional scenes "get butchered"; low-res sources look better after
  refinement).

**Why**
The merged LoRA is refiner + LightX2V's FL2VA Turbo + LMS Sharp adapter in
one ("For these few steps the refiner is merged with LightX2V's FL2VA Turbo
and the LMS Sharp adapter into a single LoRA"). Do not stack another turbo
LoRA on top — commenter tested Kjai's LoRA + light2x turbo + lms lora
manually stacked and it looked worse than the merged one; "They already
have turbo lora unlike Kjai's one so dont stack more turbo."

### Phase 3: Fit it in VRAM

**Do**
1. Author tested on Windows, RTX 5090 (32 GB VRAM), 128 GB RAM; "probably
   runs at least on an RTX 4090, and you can dial down a few settings to try
   to make it fit." Smaller cards unvalidated.
2. Expect high RAM and VRAM consumption.

**Check**
- Watch VRAM during the first window; reduce window size or settings before
  the full run.

**Why**
The learned latent upscaler plus merged adapters is heavy by design; the
author is explicit that this is a 4090-class tool.

### The human method, distilled
1. "IMHO it's a bit like SoL-Refiner when it comes to output" — calibrate
   expectations against a known refiner before adopting.
2. When users hit the 24fps wall, fix the node (fps digestion), don't write
   a FAQ.
3. Ship comparison images (upscale-only vs 0.5/0.6/0.7) so users pick noise
   from evidence, not vibes.

**Depth status:** FULL (author post text + author comments with exact
parameters, VRAM numbers, and failure modes).

## 4. "Opsis: self-hosted AI film studio" (sanchezrobertodev)

Source: https://www.reddit.com/r/comfyui/comments/1xjhrq6/ | native Reddit
video v.redd.it/os8ikk55dmyh1 | r/comfyui post 1xjhrq6 (score 21, 6 comments)
| Repo github.com/sanchezrobertodev/opsis | License: Apache (per post title)

Tools used: Opsis — self-hosted AI film studio; simple forms on top of real
ComfyUI graphs. Local GPU path: Wan 2.2 5B and FLUX.2 klein 4B on a 12 GB
card, core nodes only. RunPod path: LTX-2.5, Wan 2.2 14B Fast, VACE,
Wan Animate-2, Uni3C, Wan-Move on a serverless ComfyUI worker. Graph-to-form:
an API-format graph plus a small `.map.yaml` (which node inputs to fill)
becomes a form with a price estimate. Studios: video and image, motion
control, object swap, characters, faceless studio, cinema studio, 3D
blocking. Mock mode by default (click through everything with no GPU and no
keys). Hosted models optional with your own keys: Veo, Kling, Seedance,
ElevenLabs.

This audit reconstructs the exact workflow. The core method is: **a ComfyUI
API-format graph plus a `.map.yaml` becomes a priced form; the same studio
runs local, on RunPod, or in mock mode.**

### Phase 1: Pick a studio and a compute target

**Do**
1. Choose a studio: video and image, motion control, object swap,
   characters, faceless studio, cinema studio, or 3D blocking.
2. Run on your GPU (Wan 2.2 5B + FLUX.2 klein 4B on a 12 GB card, core
   nodes only) or on RunPod (LTX-2.5, Wan 2.2 14B Fast, VACE, Wan Animate-2,
   Uni3C, Wan-Move on a serverless ComfyUI worker).

**Check**
- The form shows a price estimate before you run (RunPod path).

**Why**
The 12GB local path uses small models and core nodes only; the heavy path
is priced serverless. The user picks the cost/quality point per shot.

### Phase 2: Fill the form, not the graph

**Do**
1. Fill the simple form; behind it, the `.map.yaml` maps your inputs onto
   the real ComfyUI graph's node inputs.
2. To add a new workflow, write YAML, not code: API-format graph +
   `.map.yaml`.

**Check**
- New workflows appear as forms with price estimates, no code deploy.

**Why**
"a new workflow is YAML, not code." The graph stays the source of truth;
the form is a generated view.

### Phase 3: Try everything in mock mode first

**Do**
1. Click through every studio in mock mode (default): no GPU, no keys.
2. Add your own keys only for the hosted models you actually use (Veo,
   Kling, Seedance, ElevenLabs).

**Check**
- The full flow works end-to-end in mock before spending GPU time or money.

**Why**
Mock-by-default removes the setup tax; keys are per-model and optional.

### The human method, distilled
1. Forms over graphs: expose only the inputs that matter, priced.
2. Three compute targets (local 12GB / RunPod serverless / mock) cover the
   whole cost curve.
3. Work in progress, feedback welcome — the author positions it as an open
   build, not a launch.

**Depth status:** FULL (author post text; the 6 comments are all snark —
"slop" accusations, a backward-feet callout at 0:25, a lamp continuity
complaint — with zero tooling signal; noted as hostile-thread evidence, not
evidence of the tool).

## 5. "3D Character I did for Zbrush 2027 beta" (Clear-Counter-640)

Source: https://www.reddit.com/r/3Dmodeling/comments/1xjls24/ | native Reddit
video v.redd.it/0ykme5q3vmyh1 | r/3Dmodeling post 1xjls24 (score 196, 34
comments)

Tools used: ZBrush (2027 beta; author worked with Maxon directly testing new
tools, under NDA for specifics). Dynamesh, extract, remesh, extrude,
subdivide, alphas. Decimation Master. Marmoset Toolbag (renders).

This audit reconstructs the exact workflow. The core method is: **one
Dynamesh for the whole character, extract the pieces, remesh/extrude/
subdivide for sharp edges, alphas for micro-detail — no booleans anywhere.**

### Phase 1: Block the whole character as one Dynamesh

**Do**
1. Start the entire character as a single Dynamesh.
2. Extract pieces out of that Dynamesh (author: "Not a single Boolean
   actually, it started as a dynamesh for the whole character, then making
   pieces by extracting out of that dynamesh").

**Check**
- Pieces separate cleanly with no boolean seams to clean up.

**Why**
Extraction from one Dynamesh keeps every piece in the same sculptural
language; booleans would introduce hard-surface seams into an organic
character.

### Phase 2: Harden edges with remesh/extrude/subdivide

**Do**
1. Remesh, extrude, and subdivide the extracted pieces to get sharp edges.
2. Use alphas for the small details.

**Check**
- Edges read sharp at render distance; micro-detail comes from alphas, not
  geometry.

**Why**
Topology operations (remesh/extrude/subdivide) carry the form; alphas carry
the detail. The author's machine: 5950X, 64 GB DDR4 — "I just needed mesh
resolution to use some alphas and the only way was to subdivide it"
(optimization would have taken "10 times more" than the brute-force
subdivide; he works 2–3 pieces per day on personal time).

### Phase 3: Decimate and render

**Do**
1. Decimate the 250M-polygon character with Decimation Master down to 10M.
2. Export to Marmoset Toolbag for the final renders.

**Check**
- 250M → 10M (25x reduction) with silhouette and alphas intact.

**Why**
Sculpt at absurd density, render at sane density; Decimation Master is the
bridge, Marmoset is the presentation.

### The human method, distilled
1. "Not a single Boolean" — extraction over booleans for organic hard
   pieces.
2. Idealized proportion check: the 8-head figure style ("that's the ideal
   proportions most artists use, specially for women, that longer legs add
   more feminine") vs 7.5 heads for a realistic street human — pick the
   proportion system before sculpting.
3. The author is shipping a project-based beginner tutorial pack (sphere,
   orange, keyboard, gun, Fortnite-style full character) — watch his
   Instagram for the release.

**Depth status:** FULL (author post text + author comments; NDA blocks the
actual 2027-beta tool specifics, which is stated, not hidden).

## 6. "Terrain3D v1.1.0 Released" (TokisanGames)

Source: https://www.reddit.com/r/godot/comments/1xjrkgv/ | native Reddit
video v.redd.it/5mj8t8ts6oyh1 | r/godot post 1xjrkgv (score 632, 30 comments)

Tools used: Godot 4; Terrain3D v1.1.0 (open-source heightmap terrain plugin);
tessellation shader producing geometry with light and shadow casting;
collision on an entirely separate, non-tessellated system.

This audit reconstructs the exact mechanics from the author's comments (the
post has no selftext). The core method is: **heightmap terrain with
tessellated rendering and a decoupled, lower-detail collision shape —
runtime-editable, but no true 3D tunnels.**

### Phase 1: Edit the heightmap

**Do**
1. Modify the heightmap's vertices or textures, including creating
   depressions or holes, at edit time or at runtime ("Terrain3D can be
   modified at runtime").
2. Do NOT expect 3D mesh tunnels: "A 3D mesh tunnel cannot be created out
   of a heightmap" — a digging game punches a 2D hole into the heightmap,
   not a 3D cavity.

**Check**
- Depressions and holes render and collide; overhangs/tunnels are
  impossible by construction.

**Why**
Heightmap = 2.5D. The author is explicit about the ceiling so users don't
design around a feature that can't exist.

### Phase 2: Render with tessellation, collide separately

**Do**
1. Rendering: "It is tessellation, which produces geometry, as you can see
   from the wire frame, and light and shadow casting."
2. Collision: "Collision runs on an entirely different system from the
   renderer. The collision shape is not tessellated at this time" — lower
   detail than the first-seconds wireframe.

**Check**
- Visual mesh is dense and shadow-casting; collision is a coarser proxy.

**Why**
Decoupling lets the renderer go dense (tessellation) while physics stays
cheap. Tessellated collision is future work ("could be considered in the
future, but not at the same level of detail").

### Phase 3: Generate at runtime from code

**Do**
1. "Look at the code generated demo if you want to procedurally generate
   maps at runtime."
2. "This is a game engine terrain editor, designed for realtime use. Play
   with the demo." (Demo videos live on the author's X/Discord.)

**Check**
- Procedural maps generate in-game, not just in the editor.

**Why**
The plugin is a realtime terrain editor first, an asset second — runtime
generation is a designed-in path, demonstrated in code.

### The human method, distilled
1. "Myself included, lol. That's why we made it, so we could have terrain"
   — scratch-your-own-itch plugin; the author team needed terrain for their
   own game.
2. Answer the hard question directly (tunnels: no; collision: separate,
   coarser) instead of marketing around it.

**Depth status:** FULL (30 comments, author answers carry exact mechanics;
post selftext is empty).

## 7. "FREE + LOCAL: Image to 3D for LOW Vram" (Olivio Sarikas / ComfyUI-ldoi)

Source: https://www.youtube.com/watch?v=0eIjJinYgmk (Olivio Sarikas,
2026-10-30) | found by the YouTube channel scan | no captions, no
transcript; deepened via download + 12 frames, all read directly.

Tools used: ComfyUI-ldoi custom nodes (nynxz/ldoi on GitHub); requires
ComfyUI 0.22+ with TripoSG support; standard TripoSG graph + two ldoi
nodes; DINOv3 ViT-H/14 and FLUX.2 VAE as denoiser conditioning; BiRefNet
for background removal; MeshLab (Screened Poisson surface reconstruction);
Blender 4.5.4 (voxel remesh).

This audit reconstructs the exact workflow from on-screen frames (GitHub
README, ComfyUI graph, MeshLab, Blender). The core method is: **single
image → TripoSG-based fp16 splat in ComfyUI → Screened Poisson mesh in
MeshLab → voxel remesh in Blender — all local, ~3.8 GB of fp16 weights.**

### Phase 1: Install the nodes and weights

**Do**
1. Clone into `ComfyUI/custom_nodes` and restart ComfyUI (frame shows the
   folder `ComfyUI-ldoi` freshly added 30.10.2026 in a portable
   ComfyUI_windows_portable install).
2. Download the five fp16 weights into ComfyUI's standard folders:

| File | Folder | Size | Source |
|------|--------|------|--------|
| ldoi_fp16.safetensors | models/diffusion_models | 0.74 GB | nynxz/ldoi |
| ldoi_decoder_fp16.safetensors | models/vae | 0.58 GB | nynxz/ldoi |
| dino_v3_vit_h.safetensors | models/clip_vision | 1.68 GB | VAST-AI/TripoSplat |
| flux2-vae.safetensors | models/vae | 0.34 GB | VAST-AI/TripoSplat |
| birefnet.safetensors | models/background_removal | 0.44 GB | Comfy-Org/BiRefNet |

**Check**
- Five files, ~3.78 GB total, in the folders above; ComfyUI 0.22+ with
  TripoSG support.

**Why**
"The first two are ldoi's own weights (the denoiser and the coarse or
gaussian decoder) in ComfyUI's file layout... The other three are the same
encoders ldoi uses: DINOv3 ViT-H/14 and the FLUX.2 VAE condition the
denoiser." If you already run TripoSplat in ComfyUI, you have the three
encoders. fp16 throughout is the low-VRAM story.

### Phase 2: Run the image-to-splat graph

**Do**
1. Drag `workflow/ldoi_image_to_splat.png` into ComfyUI, or open it from
   Templates → Custom Nodes → ComfyUI-ldoi; it's the standard TripoSG
   graph with the ldoi files and the two ldoi nodes.
2. Load Image: the object photo; "a transparent PNG's own alpha can be
   used" — otherwise BiRefNet cuts the object out.
3. The two ldoi nodes run the denoiser/decoder; Save Splat writes the
   result (node shows model_3d, model_info, camera_info inputs; 3D viewer
   shows the splat on a grid — frame shows a fox).
4. Create Video: 24 frames, 24fps, 360° turntable, MP4 output; Save Video.

**Check**
- The splat in the 3D viewer matches the input object from multiple
  angles; the turntable video shows no view-collapse.

**Why**
Transparent-PNG alpha is the cheap segmentation path; BiRefNet is the
fallback. The turntable video is the acceptance check before meshing.

### Phase 3: Convert the splat to a mesh

**Do**
1. Export the point cloud/mesh from the splat; open MeshLab.
2. Run Screened Poisson surface reconstruction on the exported layer
   (frame shows layers `ldoi_00002` point cloud → `Poisson mesh`, with the
   reconstruction dialog open on the fox model).

**Check**
- The Poisson mesh is watertight where the splat had coverage.

**Why**
MeshLab is the open-source mesh surgery step: "the open source system for
processing and editing 3D triangular meshes... editing, cleaning, healing,
inspecting, rendering, texturing and converting meshes."

### Phase 4: Remesh in Blender

**Do**
1. Import into Blender 4.5.4; add a Remesh modifier: Voxel mode, Voxel
   Size 0.1 m, Adaptivity 0.0, Smooth Shading (frame shows these exact
   settings on a stylized head mesh).

**Check**
- Even voxel topology at 0.1 m, ready for sculpt/detail passes.

**Why**
Voxel remesh erases the Poisson mesh's uneven triangulation and gives a
uniform base for further work.

### The human method, distilled
1. Keep everything fp16 and local — the whole pipeline fits modest VRAM
   because no single weight exceeds 1.68 GB and the total is ~3.8 GB.
2. Reuse the TripoSG ecosystem (encoders, folder layout) instead of
   shipping a parallel stack.
3. Splat → Poisson → voxel remesh: three open tools, each doing the one
   conversion it's best at.

**Depth status:** FULL (deepened pipeline: media download + 12 frames read
directly; no captions or transcript exist; every value above is from
on-screen text in the frames).

## 8. "Generative Lexicon Press" (uisato, TouchDesigner)

Source: https://www.reddit.com/r/vfx/comments/1xjgqub/ | native Reddit video
v.redd.it/xj09h67x5myh1 | r/vfx post 1xjgqub (score 20, 1 comment) |
4K walkthrough on YouTube (CVAS-w8300o) | project files on Patreon and
uisato.studio/tools

Tools used: TouchDesigner generative typography system; 25 layouts; words
and letters become structures, patterns, erasures, animated sequences; sound
drives movement, highlights, and page changes; optional Writing Partner
generates new passages locally through Ollama (from a concept, writing
mode, and language). Deeply inspired by Ksawery Komputery's "Symphony in
Acid".

This audit reconstructs the workflow from the author's post. The core
method is: **written passages become moving compositions across 25
audio-reactive layouts; an optional local Ollama partner writes the
passages.**

### Phase 1: Supply the passage

**Do**
1. Use your own written passage, or generate one locally with the Writing
   Partner (Ollama; inputs: concept, writing mode, language).

**Check**
- The passage reads well aloud — it will be performed, not just displayed.

**Why**
Local Ollama keeps the writing step private and free; the passage is the
score the layouts perform.

### Phase 2: Compose across layouts

**Do**
1. Arrange the 25 layouts into a sequence; words and letters become
   structures, patterns, erasures, and animated sequences.
2. Adjust how each layout responds to sound: sound drives movement,
   highlights, and page changes.

**Check**
- Play the passage audio; each layout's motion, highlights, and page
  turns lock to the sound.

**Why**
The system is an instrument, not a template: the same passage plays
differently per layout and per audio input.

### The human method, distilled
1. Name the influence precisely ("Symphony in Acid" — "one of the most
   amazing generative works ever created") so users know the target
   aesthetic.
2. Ship the project files (Patreon + studio site) and a 4K walkthrough —
   the product is the system, not a render.

**Depth status:** PARTIAL (author post text only; the 4K walkthrough video
exists but is uncaptioned and was not deepened this run — a download +
frame review would add the actual node/layout mechanics; one comment, no
tooling).

## agentY UPDATE — skill expansion (not a new audit)

The r/comfyui UPDATE post (1xjbipg, Admirable-Agency-578, score 69, 10
comments) adds to yesterday's FULL agentY audit. New details folded into the
existing `automation/comfyui-agenty-ai-agent` skill this run:

- WorldLabs API update: high-quality splats from single generated images.
- Grok works via its OpenAI-compatible endpoint: enter endpoint URL + API
  key in the settings panel, restart the agent; grok then sees the
  workflow, adjusts the canvas directly, and builds workflows in separate
  ComfyUI tabs while you talk in the side panel.
- Annotation tool: give feedback by drawing on images/videos.
- Uninstall: delete the agentY repo folders and the agent custom node in
  the ComfyUI folder (API keys can be re-set via the settings panel; or
  re-run the installer).
- Platform support: Windows + Apple Silicon listed; Linux/macOS installer
  scripts exist (`install_agent.sh` covers macOS and Linux) but Linux is
  untested by the author — readme updated only if a user confirms.
- Packaged as an MCP itself: Claude can orchestrate multiple agentY
  instances (which use other LLMs).
- Builds motion graphics and edits video using remotion, editable inside
  ComfyUI's own image/video/3D viewer.

## Have-vs-need: Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Lattice + WPO vehicle damage, Nanite intact, no Chaos Destruction | #1 Crushform | NEED | No vehicle-damage/runtime-deformation stage; `ue/` is a packaging stage only | watchlist: runtime tech, not pipeline scope; Aetheria-side interest only |
| Single-image to 3D, fp16, ~3.8 GB local (ComfyUI-ldoi/TripoSG) | #7 ldoi | PARTIAL | HAVE: image-to-3D via TRELLIS-2 (`runtime/worker`, `gen_server`) | watchlist: lighter-weight local alternative to TRELLIS-2 for intake experiments; BiRefNet-then-alpha segmentation pattern reusable |
| Control-pass-driven AI video (previs → pose/depth/mask → H3) | #2 Previs | NEED | No AI-video/previs stage | skip for Aegis scope (trailer tooling bucket) |
| H3 refiner/upscaler nodes (24fps, noise 0.5–0.7, 4090-class) | #3 H3-Regen | NEED | No refinement/upscale stage | watchlist: relevant only if Aegis ever upscales generated video |
| Forms-on-graphs studio (Opsis, .map.yaml → priced form) | #4 Opsis | NEED | No operator-facing generation UI | skip: product pattern, not pipeline |
| Dynamesh-extract + Decimation Master 250M→10M character workflow | #5 ZBrush | PARTIAL | HAVE: weld/merge, xatlas UV, OptiX bake, LODs; NEED: rigging/skinning/retarget (P1) | watchlist: characters bucket; sculpt workflow reference, not a stage |
| TouchDesigner audio-reactive typography (25 layouts) | #8 Lexicon | NEED | No motion-graphics stage | skip: not Aegis scope |

## Have-vs-need: 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Terrain3D heightmap terrain (tessellated render, decoupled collision, runtime editing) | #6 Terrain3D | NEED | Godot 4.7.2 project; no terrain system in inventory | watchlist: 2d3d is a 2D-to-3D side-scroller; terrain relevant only if 3D ground planes enter scope |
| Splat → Poisson mesh → voxel remesh cleanup chain | #7 ldoi | PARTIAL | HAVE: `pipeline/reference/recon_pipeline.py` (Depth Anything 3 + SAM 2); NEED: production-conversion stage (P1, roadmap rec 20) | watchlist: MeshLab Screened Poisson + Blender voxel remesh (0.1 m) is field evidence for the mesh-cleanup facet of the P1 production-conversion gap — not a replacement for retopo/UV/rig/LOD |
| Dynamesh-extract sculpt workflow | #5 ZBrush | NEED | No sculpting stage; pixel-art pipeline | skip: art style mismatch |
| Asset import validation patterns (per-side zones, events) | #1 Crushform | NEED | NEED: asset import validation gate (P1, roadmap rec 9) | skip: Crushform's zones are gameplay events, not an import gate |

## Have-vs-need: Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Terrain3D heightmap terrain | #6 Terrain3D | NEED | Godot project per PRD; no terrain system listed | watchlist: only if ground terrain (not just buildings) enters scope |
| Procedural 3D ice material (glass IOR 1.4, foggy roughness; inner opaque glass) | ice micro-audit (below) | NEED | No ice/snow material in inventory | watchlist: one-recipe material, exact params recorded |
| Everything else today | — | — | — | skip: AI-video/comfy/UE tooling outside cozy-builder scope |

## Have-vs-need: Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Terrain3D heightmap terrain | #6 Terrain3D | NEED | No Godot project exists yet; export budgets reasoned, not measured | watchlist: candidate terrain approach when the Godot client exists |
| Everything else today | — | — | — | skip |

## Watchlist trending (verbatim, corrected)

The auto-matcher flagged three rows; two were token-overlap false positives
(annotated in the watchlist per convention) and are struck below:

- agentY (free MIT AI agent inside ComfyUI, DCC MCP presets, remotion)
  (first seen 2026-10-30, status WATCH; seen again 2026-10-31) — genuine:
  the UPDATE post adds WorldLabs splats, remotion editing, annotation tool,
  and grok-via-OpenAI-endpoint setup.
- ~~comfyui-minimax-h3-studio (BiggerFishy) seen again 2026-10-31~~ — NOT
  genuine: auto-match was token overlap on "ComfyUI Motion Previs Studio"
  (navarisun's 3D-blocking→H3-Ref2VA previs tool); BiggerFishy's SAM3
  color-inversion character-swap never mentioned.
- ~~MiniMax H3 Reference-to-Video character swap seen again 2026-10-31~~ —
  NOT genuine: auto-match was token overlap on "MiniMax H3" for imlo2's
  Open-H3-Regenerate-2K refiner/upscaler wrapper (NVIDIA merged adapters);
  character swap never mentioned.

Eight genuinely new tools appended to `references/tooling-watchlist.md`
(Crushform, Motion Previs Studio, Open-H3-Regenerate-2K, Opsis,
ComfyUI-ldoi, Terrain3D v1.1.0, ZBrush Dynamesh-extract workflow,
Generative Lexicon Press).

## Gap recommendations (highest-leverage NEEDs)

1. **ComfyUI-ldoi as a light intake experiment (Aegis).** TRELLIS-2 is the
   heavy path; ldoi is fp16, ~3.8 GB total, runs local, and its
   splat→MeshLab-Poisson→Blender-voxel-remesh chain is the cheapest
   documented image-to-mesh cleanup loop seen this month. Next step: run the
   `ldoi_image_to_splat` workflow on one Aegis concept image and compare
   against TRELLIS-2 output quality. (watchlist, not backlog — needs the
   comparison first.)
2. **Previs control-pass pattern for any Aegis trailer work.** The
   3D-block → OpenPose/depth/mask/camera-matrix → H3/LTX/Seedance pattern
   is the first fully-specified anti-prompt-spiral video pipeline in the
   scout corpus. Next step: keep on watchlist until trailer work starts;
   the pattern transfers directly.
3. **Terrain3D for the Godot repos (2d3d/Desktop City/Solarempire).** The
   only Godot-native, runtime-editable, open-source heightmap terrain with
   documented tessellation-vs-collision tradeoffs seen in the corpus.
   Next step: evaluate if/when 3D ground enters any Godot repo's scope;
   the heightmap-no-tunnels ceiling is the key design constraint to carry.
4. **H3-Regenerate-2K noise ladder for AI-video QA.** The
   upscale-only-vs-0.5/0.6/0.7 comparison discipline (with the "don't stack
   turbo" rule and the 24fps footgun fix) is a reusable acceptance pattern
   for any refinement stage. Next step: adopt the comparison protocol, not
   the tool, if video refinement enters scope.
5. **agentY P2 evidence keeps compounding.** Three MCP-preset sightings in
   two days (yesterday's presets, today's remotion/annotation/grok
   additions). Next step: keep the Blender-MCP spike pointed at agentY as
   the first tool to try (yesterday's recommendation stands, strengthened).

## Explicit non-goals (found but correctly skipped)

- **Procedural 3D ice system** (deepak365days, r/proceduralgeneration,
  v.redd.it/obqofil75lyh1, score 70, 9 comments): artist-designed, not
  physics-informed ("I design it from artists perspective"). Exact recipe:
  outer = normal glass material, IOR 1.4, smooth roughness for foggy look;
  inside mesh = opaque glass material with roughness so it looks white.
  Recorded here for the materials bucket; too small for its own skill.
  (PARTIAL micro-audit.)
- **1M Soldiers in Godot 4 C# ECS at 300–450 FPS**
  (youtu.be/MhFdQMKtbYk, r/godot 1xjq7vj): no captions; 3 comments are
  unanswered questions (RenderingServer? specs? bespoke ECS?). A media
  download would add frames of a gameplay demo but not the ECS
  implementation — author input is the missing piece. DEPTH-LIMITED;
  theme already covered by the `godot-1m-agent-ecs-impostors` skill.
- **Blender Secrets: Maximilian-inspired Armour** (2026-10-29) and
  **Ryan King: Texture Painting Quick Start** (2026-10-30): YouTube
  channel-scan finds, no captions; beginner/tutorial format, no extractable
  workflow from metadata. Not deepened (download allowance conserved).
- **Excavated pipe Gaussian splat** (AECPLATFORM, r/photogrammetry):
  commercial AEC Platform output ("Processing profile: High Quality, Point
  cloud, Mesh, Gaussian Splat"), no workflow detail; 3DGS already covered
  by existing capture skills.
- **Ad Lumens gaseous planets** (oleoalbedo, r/proceduralgeneration): devlog
  (gas/ice giants, gas dwarfs, brown dwarfs in the satellite tool; rings/
  belts next; LOD tailoring); no extractable workflow, thin comments.
- **MarcoStudio** (13 image/video tools on own ComfyUI, r/comfyui): 2
  comments, post text is a feature list without workflow detail.
- **"This took 12 hours to make and nobody cares..."** (r/comfyui, score
  280, 120 comments): engagement without tooling signal in the scan
  snippet; below the relevance bar for the 8-cap.

## skill_library artifacts staged

In `~/workspace/video-tooling-scout-public/` (push handled by the 09:18
daily-skill-library-push cron; this run stages only):

New skills (8):
- `simulation-vfx/crushform-ue5-vehicle-damage/`
- `ai-video/comfyui-motion-previs-studio/`
- `ai-video/open-h3-regenerate-2k-refine/`
- `ai-video/opsis-comfyui-film-studio/`
- `characters/zbrush-dynamesh-extract-decimate/`
- `engine-runtime/godot-terrain3d-heightmap/`
- `capture/comfyui-ldoi-image-to-3d/`
- `ai-video/touchdesigner-generative-lexicon-press/`

Expanded (1): `automation/comfyui-agenty-ai-agent/` (WorldLabs splats,
remotion editing, annotation tool, grok endpoint setup, uninstall, Linux
status).

Also staged: this report at
`docs/scout-reports/have-vs-need-2026-10-31.md`; synced watchlist rows in
`video-tooling-scout/references/tooling-watchlist.md`; new rows in the
grouped table in `skills/README.md`; skill count + category counts updated
in the root README "The skills" table (no chronological prose).

## Depth-escalation summary

- Mode: `pre-approved`, max 2 downloads. Attempted 1, succeeded 1, skipped 0.
- The successful download (Olivio Sarikas ldoi video) hit no approval gate
  and produced a FULL audit from 12 reviewed frames.
- The second slot was unused: all other audits reached FULL/PARTIAL from
  post text + comments, and the remaining YouTube candidates lacked the
  tooling signal to justify a download.
- Infra fix this run: appended the current Hatch Sandbox Egress CA to the
  video-summarizer venv's certifi bundle, restoring the YouTube channel
  scan (11 channels, 3 videos). YouTube metadata extraction is still
  degraded (no durations/descriptions/captions); deepened pipeline remains
  the only YouTube audit route.
