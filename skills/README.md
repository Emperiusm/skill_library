# Skills

Every directory here is one executable skill: a `SKILL.md` playbook that teaches one workflow end to end. Skills are grouped by category, one level deep. New skills land here with every daily scout run, each assigned a category when it is created.

## Capture and reconstruction (`capture/`)

| Skill | What it teaches |
|---|---|
| [`adaptive-frame-extractor`](capture/adaptive-frame-extractor/SKILL.md) | Feed photogrammetry only the frames it needs: score frames for quality and overlap, extract the best, skip the rest. |
| [`fix-lumpy-photogrammetry-meshes`](capture/fix-lumpy-photogrammetry-meshes/SKILL.md) | Fix lumpy photogrammetry meshes in Blender the Planer way: detect planar regions, snap vertices to fitted planes and intersections, prove fidelity with a deviation report. |
| [`greenscreen-plate-production-keying`](capture/greenscreen-plate-production-keying/SKILL.md) | Produce pro-level greenscreen plates for keying practice: cinema camera, ProRes RAW, in-frame tracking markers, deliberately kept imperfect plates, shot planning for full 3D-world building. |
| [`spirula-3dgs-anti-floater-capture`](capture/spirula-3dgs-anti-floater-capture/SKILL.md) | Produce clean 3D Gaussian splats with Spirula: plan phone capture around the actual camera moves (4K60), enable normal and depth estimation at SfM. |
| [`vathography-depth-remap`](capture/vathography-depth-remap/SKILL.md) | Turn a photo's hidden depth pass into the artwork: Marigold V2 single-photo depth (Apache 2.0), then Blender compositor Color Ramp remap for volume, mist, and focus. |

## Characters and rigging (`characters/`)

| Skill | What it teaches |
|---|---|
| [`ai-character-pipeline`](characters/ai-character-pipeline/SKILL.md) | Turn an AI character concept into a rigged, game-ready 3D asset, two methods: Tripo P2.0 generate-then-repair (recommended), or base-mesh-first with AI-assisted rigging. Meshy not recommended. |
| [`blender-fake-sim-rigging`](characters/blender-fake-sim-rigging/SKILL.md) | Rig soft-body secondary motion with Blender constraints instead of a simulation: Stretch To + Track To guide bones drive jiggle without cloth sim or. |
| [`layered-vellum-proxy-colliders`](characters/layered-vellum-proxy-colliders/SKILL.md) | Layer hair sims on top of cloth sims in Houdini Vellum without intersection or tangling: simulate cloth first, then give the hair layer simplified VDB-proxy colliders. |
| [`minimax-h3-refmod-identity-comfyui`](characters/minimax-h3-refmod-identity-comfyui/SKILL.md) | Generate images of your own character with MiniMax H3 in ComfyUI without LoRA training: bake identity into a RefMod file from 8 photos with RefMod. |
| [`omnichar-portable-characters`](characters/omnichar-portable-characters/SKILL.md) | Ship consistent AI characters across image and video models: encode face/body/wardrobe into a portable .char once (sface + DINOv2 scored), decode per model into Minimax H3, Krea2, Flux2 dev, or klein 9B/4B. |
| [`revive-ancient-model`](characters/revive-ancient-model/SKILL.md) | Revive a legacy 3D model: retexture, rig, animate, let the original forms carry it. |
| [`substance-painter-characters`](characters/substance-painter-characters/SKILL.md) | Texture game characters in Substance Painter: bake mesh maps, build materials in layers, keep the stack editable. |
| [`reallusion-rigger-apex-rig`](characters/reallusion-rigger-apex-rig/SKILL.md) | Turn a Character Creator 5 / iClone 8 character into a shaded, animatable, render-ready Solaris character in Houdini 22+ with one click: USD/FBX import, Karma CPU/XPU materials, full APEX rig, face puppet and muscle tools, LookAt auto-animation. |

## Procedural generation and worlds (`procgen-worlds/`)

| Skill | What it teaches |
|---|---|
| [`cinematic-cavern`](procgen-worlds/cinematic-cavern/SKILL.md) | Build a cinematic cavern scene end to end: Blender blockout, ZBrush sculpt, game-mesh reduction, Substance bake and PBR materials, Unreal export, scripted repairs, a C++ height-field water solver, player-to-water contact, Houdini waterfall, final assembly. |
| [`godot-procgen-city-glb-export-schema`](procgen-worlds/godot-procgen-city-glb-export-schema/SKILL.md) | Ship a Godot procedural city as documented glb: keep generation procedural in-engine, define the schema of custom glb properties so others can write. |
| [`minecraft-world-one-block`](procgen-worlds/minecraft-world-one-block/SKILL.md) | Generate massive voxel worlds from one block with deterministic sampling and LOD. |
| [`one-seed-procedural-game`](procgen-worlds/one-seed-procedural-game/SKILL.md) | Build a game with zero asset files: one seed generates terrain, towns, people, sky, and audio at startup; props from boxes/spheres/cones, sound from sine waves. |
| [`parametric-ship-generator-isometric`](procgen-worlds/parametric-ship-generator-isometric/SKILL.md) | Generate sci-fi ships as parametric 3D geometry drawn isometrically on a 2D canvas in plain JavaScript: grid-snapped hull segments, taper profiles, fit rules for engines/noses/wings, seed-driven output. |
| [`phosphor-command-code-drawn-procgen`](procgen-worlds/phosphor-command-code-drawn-procgen/SKILL.md) | Ship a code-drawn procedural game: no sprites or textures, deliberate phosphor-CRT radar-scope aesthetic, generate operations per contract with a persistent base-builder layer. |
| [`procedural-galaxy-generator-blender`](procgen-worlds/procedural-galaxy-generator-blender/SKILL.md) | Build procedural galaxies in Blender with geometry nodes plus shaders: point clouds for stars, volumes for everything else, energy-preserving far-field glow, keyframed emissive flythroughs, 3D gravitational lensing meshes, dust lanes as layered volume roles (absorption/emission/particles), and instanced deep-field domains with cosmological redshift. |
| [`procedural-pixel-creature-generator`](procgen-worlds/procedural-pixel-creature-generator/SKILL.md) | Generate pixel-art creatures in code (Godot 4.5 / C#): seed-driven bodies, limbs, faces, markings, rigs, and multi-directional animations, with frame counts derived by the rigging engine; export transparent PNG sprite sheets plus a JSON manifest (directions, frames, pivots, timing). |
| [`procedural-pixel-creature-generator-seed-web`](procgen-worlds/procedural-pixel-creature-generator-seed-web/SKILL.md) | Generate pixel creatures from a single seed on the web: 35 body types grown by mask plus cellular automata, 8 sizes from 8 px to 1024 px, 8 animations, 7 palettes; export transparent PNG, GIF, sprite strip, or 12-creature sheet; shareable seed URLs. |
| [`procedural-ribbon-cables`](procgen-worlds/procedural-ribbon-cables/SKILL.md) | Generate ribbon cables procedurally with parametric controls instead of modeling by hand. |
| [`procgen-racing-track-generator`](procgen-worlds/procgen-racing-track-generator/SKILL.md) | Generate endless arcade racing tracks by polygon seeding, midpoint-displacement, bezier smoothing, and bending straight mesh segments along the. |
| [`raup-shell-morphospace`](procgen-worlds/raup-shell-morphospace/SKILL.md) | Generate every seashell from three numbers: David Raup's morphospace (flare, verm, spire), built as a Blender geometry-nodes / TouchDesigner. |
| [`recursive-tree-spawner-parameter-space`](procgen-worlds/recursive-tree-spawner-parameter-space/SKILL.md) | Drive procedural tree generation by sweeping parameter ranges (not the algorithm): one recursive branch spawner yields one species or many depending. |
| [`runevision-voronoi-terrain-stack`](procgen-worlds/runevision-voronoi-terrain-stack/SKILL.md) | Drive large-scale procedural terrain with Voronoi macro-cells for level-design control over noise: LayerProcGen framework, fast erosion filter, GPU. |
| [`ring-world-shader-curvature`](procgen-worlds/ring-world-shader-curvature/SKILL.md) | Fake a ring world without building one: flat strip holding every biome, curved-space shader bends it into a ring; interaction and lighting agreement are the debts. |
| [`branch-propagation-tree-generator`](procgen-worlds/branch-propagation-tree-generator/SKILL.md) | Generate tree species in C++ from per-level branch propagation rules (end-only vs mid-branch splits, leaf types, angle intervals with upward biases), rendered as low-memory cylinder primitives in custom Vulkan. |

## AI video and film (`ai-video/`)

| Skill | What it teaches |
|---|---|
| [`agentic-multishot-ai-video-farm-crew`](ai-video/agentic-multishot-ai-video-farm-crew/SKILL.md) | Produce multi-shot AI video with a tiny render farm and a four-agent crew: per-shot jobs with explicit NOT-ALLOWED-TO-CHANGE lock lists, Pocket AI ComfyUI front-end plus Tensor Master GPU-rental dispatch, Coordinator/Prep/Farm-monitor/QC loop, the four canonical mask failures and fixes. |
| [`avatar-model-comparison-harness`](ai-video/avatar-model-comparison-harness/SKILL.md) | Evaluate lip-synced AI avatar models with a fixed-input comparison harness: same portrait plus same driving audio, one fixed prompt template, a. |
| [`blender-mcp-camera-minimax`](ai-video/blender-mcp-camera-minimax/SKILL.md) | Direct AI video camera moves in 3D first: block with Codex CLI plus Blender MCP, render a reference clip, assign role-based inputs in MiniMax H3. |
| [`claude-cinematic-trailer`](ai-video/claude-cinematic-trailer/SKILL.md) | Direct an AI agent to cut a cinematic trailer from your game, then curate its output. |
| [`flux-3-klein-comfyui-19-workflows`](ai-video/flux-3-klein-comfyui-19-workflows/SKILL.md) | Run FLUX 3 Klein in ComfyUI across 19 free workflows: text-to-image with Z-Image realism pass and BFL prompt upsampler, text-in-images and Layout Boxes, eight image edits (box inpaint, text edit, restyle, relight, restore, character sheets, outpaint), and five multi-image combines up to 10 reference images. |
| [`konte-multishot-ai-video`](ai-video/konte-multishot-ai-video/SKILL.md) | Run multi-shot AI video like a software project: TypeScript DSL, stable asset addresses, non-destructive variants, explicit acceptances, agents driving ComfyUI. |
| [`moss-image-comfyui-recipe`](ai-video/moss-image-comfyui-recipe/SKILL.md) | Run OpenMOSS MOSS-Image (5B DiT, Apache 2.0) in ComfyUI: starter settings 1024x1024/50 steps/CFG 3/shift 5, layout-JSON text rendering, INT8/INT4 quants for 8 GB cards, riding the Turbo LoRA/ControlNet community wave. |
| [`minimax-h3-character-swap-comfyui`](ai-video/minimax-h3-character-swap-comfyui/SKILL.md) | Swap a character in video with MiniMax H3 in ComfyUI: SAM3 text-prompt masking, color-inversion repaint signal, saved character units, in-workflow trimming, describe-the-finished-result prompting. |
| [`minimax-h3-character-swap-nomask-lowvram`](ai-video/minimax-h3-character-swap-nomask-lowvram/SKILL.md) | Swap a character in video with MiniMax H3 + Character Swap LoRA in ComfyUI with no masking: 0.4 MP at 8 steps, runs on 6 GB VRAM. Reference-video. |
| [`minimax-h3-selflift-long-video`](ai-video/minimax-h3-selflift-long-video/SKILL.md) | Stitch seamless long videos with MiniMax H3 in ComfyUI without color shift: SelfLift dual-sampling context mode, differential 0.1 noise at seams. |
| [`resistance-sci-fi-short`](ai-video/resistance-sci-fi-short/SKILL.md) | Direct an AI-generated sci-fi short: lock keyframes and concepts first, generate shots as repeatable ComfyUI nodes, keep prompt writing manual, edit and grade in an NLE. |
| [`syf-motion-blur-pro`](ai-video/syf-motion-blur-pro/SKILL.md) | Add motion blur with a free OFX plugin: match the algorithm to the motion type, tune length vs strength, stack instances for complex shots. |
| [`ue58-video-in-materials`](ai-video/ue58-video-in-materials/SKILL.md) | Route real video into Unreal materials: Media Framework, procedural scanlines, CRT glass, mosaic UV math, SubUV flipbooks, light-function projectors. |
| [`minimax-h3-synctile-long-video`](ai-video/minimax-h3-synctile-long-video/SKILL.md) | Generate long MiniMax H3 videos (tested 600 frames / 25 s at 4K) with one denoising trajectory: SyncTile blends overlapping tiles x 124-frame windows at every model call; 0.5 MP draft, 3D latent upscale, 4K refine. |
| [`minimax-h3-reference-video-character-swap`](ai-video/minimax-h3-reference-video-character-swap/SKILL.md) | Swap a character in video with MiniMax H3's Reference-to-Video workflow in ComfyUI: source footage supplies motion, Krea 2 and Qwen Image supply references, no mocap; watch for smearing in fast motion and missing facial detail in wide shots. |

## Simulation and VFX (`simulation-vfx/`)

| Skill | What it teaches |
|---|---|
| [`armor-simulation-mode`](simulation-vfx/armor-simulation-mode/SKILL.md) | Simulate armor impacts with SPH fracture and contact modeling. |
| [`baradur-env-breakdown`](simulation-vfx/baradur-env-breakdown/SKILL.md) | Assemble a large-scale VFX environment as labeled reviewable stages (Base/Tower/Lava/Eye/comp): Nuke-style 3D assembly, 100GB+ smoke-sim cache. |
| [`blender-mpm-fracture`](simulation-vfx/blender-mpm-fracture/SKILL.md) | Run 890k-particle Material Point Method sims with Voronoi-cell fracture in Blender. |
| [`blueprint-construction-effect`](simulation-vfx/blueprint-construction-effect/SKILL.md) | Author a reverse-erosion construction effect: blueprint preview, climbing rim shader, ember particle finish. |
| [`chaos-flesh-dataflow-soft-body`](simulation-vfx/chaos-flesh-dataflow-soft-body/SKILL.md) | Build a UE 5.8 Chaos Flesh soft-body asset with DataFlow: mesh prep rules, Static-to-Tet-Mesh template, tet density tuning, the missing Set-Flesh-Default-Properties fix, deformable solver wiring. |
| [`houdini-net-break-topo-wedge`](simulation-vfx/houdini-net-break-topo-wedge/SKILL.md) | Break a net in slow motion for commercial VFX: curve-spline knot modeling, glue constraints to kill jitter and untangling, procedural art-directed. |
| [`surface-turbulence-wave-detail`](simulation-vfx/surface-turbulence-wave-detail/SKILL.md) | Add fine surface waves to a cached particle-based liquid simulation without rerunning it: build a fine surface point set, track it with an advection. |
| [`tideglass-fluid-sim`](simulation-vfx/tideglass-fluid-sim/SKILL.md) | Build a target-driven real-time GPU fluid sim. |
| [`weta-bubbles-solver`](simulation-vfx/weta-bubbles-solver/SKILL.md) | Implement a two-way coupled bubbles solver from the Weta FX whitepaper in vanilla Houdini nodes. |
| [`corridor-key-2-ai-chroma-keyer`](simulation-vfx/corridor-key-2-ai-chroma-keyer/SKILL.md) | Pull production chroma keys with Corridor Key 2.0: one-click key, rough alpha-hint mattes only for hard shots, Magic Mask into the hint channel, despill discipline, IBK core-matte edge pass, train-your-own-model recipe. |
| [`houdini-ocean-emergence-shot`](simulation-vfx/houdini-ocean-emergence-shot/SKILL.md) | Sell a creature emerging from the ocean in Houdini + Nuke: spectrum amplitude down and high-frequency detail up, pre-emergence bulge with bow shock, upward custom velocity field, foam as a separate pass, slow drainage, VEX stepping fix. |

## Materials and shaders (`materials-shaders/`)

| Skill | What it teaches |
|---|---|
| [`handdrawn-foliage-alpha-cards`](materials-shaders/handdrawn-foliage-alpha-cards/SKILL.md) | Hand-draw game foliage as alpha cards: one texture, low face count, default hard-edge brush in Photoshop, masked-opacity material in-engine for crisp. |
| [`leather-patch-generator`](materials-shaders/leather-patch-generator/SKILL.md) | Generate leather patch materials with a parametric Substance generator. |
| [`procedural-building-shader`](materials-shaders/procedural-building-shader/SKILL.md) | Fill a cyberpunk skyline with a procedural building shader instead of geometry. |
| [`realistic-rust-materials`](materials-shaders/realistic-rust-materials/SKILL.md) | Author realistic rust as a layered procedural material system with exposed parameters. |
| [`substance-painter-3dspace-blur-filter`](materials-shaders/substance-painter-3dspace-blur-filter/SKILL.md) | Remove UV seam artifacts in Substance Painter with a custom 3D-space blur filter that samples neighbors by 3D proximity from a baked Position Map. |
| [`toon-2d-in-3d-dynamic-texture`](materials-shaders/toon-2d-in-3d-dynamic-texture/SKILL.md) | Render a classic DBZ cel look in 3D: fake light direction with a target point instead of a real light, drive drawn cel shapes on a dynamic texture, verify with extreme-zoom closeup animation. |
| [`ue58-gradient-animated-materials`](materials-shaders/ue58-gradient-animated-materials/SKILL.md) | Build four gradient-driven animated materials in Unreal Engine 5.8's Material Editor (matrix-code streaks, dissolve-swap between two textures. |
| [`ultratex-comfyui-ai-texturing`](materials-shaders/ultratex-comfyui-ai-texturing/SKILL.md) | Texture any untextured mesh locally in ComfyUI with UltraTex: one reference image in, 2K PBR textures out, free, on 6 to 16 GB GPUs; GGUF workflow for 6 to 8 GB cards, Klein BASE model required. |

## Engine and runtime (`engine-runtime/`)

| Skill | What it teaches |
|---|---|
| [`ascii-raymarched-world-grid`](engine-runtime/ascii-raymarched-world-grid/SKILL.md) | Build a single-file raymarched web game world on a 2048x2048 one-byte-per-cell material grid: place settlements first, bake roads with a Dijkstra. |
| [`cave-expedition-render-tech`](engine-runtime/cave-expedition-render-tech/SKILL.md) | Ship heavy voxel-terrain visuals on a performance budget: mesh compression, virtual texturing, GPU-driven detail, each stage held to its budget. |
| [`godot-decoupled-rules-json-movie-maker`](engine-runtime/godot-decoupled-rules-json-movie-maker/SKILL.md) | Build a Godot game with engine-decoupled rules: game logic in a plain library with no Godot dependency, each rule a small class behind a. |
| [`mass-entity-niagara-crowd`](engine-runtime/mass-entity-niagara-crowd/SKILL.md) | Render massive UE crowds without per-agent actors: simulate in custom C++ MassEntity processors, stream transform arrays into Niagara GPU particles, animate with VATs. |
| [`multiplayer-movement-smooth`](engine-runtime/multiplayer-movement-smooth/SKILL.md) | Smooth multiplayer movement with client prediction and server reconciliation. |
| [`procedural-backrooms-browser`](engine-runtime/procedural-backrooms-browser/SKILL.md) | Ship procedural 3D in the browser: client-side WebGPU with a WGSL pipeline and GLSL fallback. |
| [`ro-engine-neural-vs-scripts`](engine-runtime/ro-engine-neural-vs-scripts/SKILL.md) | Test game AI empirically: pit deterministic behavioral scripts against a learned policy in a custom engine and measure which wins. |
| [`seeded-squad-sim-deterministic-replay`](engine-runtime/seeded-squad-sim-deterministic-replay/SKILL.md) | Build a seeded, exactly-reproducible browser simulation: one seed determines terrain, weather, and forces; separate RNG streams per system; an event. |
| [`webgpu-black-hole-raytracer`](engine-runtime/webgpu-black-hole-raytracer/SKILL.md) | Build an interactive, physically-grounded Kerr black-hole renderer in the browser with WebGPU: backwards ray integration through Kerr spacetime per. |
| [`unity-dots-fake-ragdoll-crowds`](engine-runtime/unity-dots-fake-ragdoll-crowds/SKILL.md) | Render 10,000-character crowds with fake ragdolls: premade collapse clips plus deterministic launch, baked vertex anims, sub-1000-tri meshes, no armatures, 3 LODs; plus the no-full-ECS arrays-plus-Burst alternative. |
| [`godot-2d-movement`](engine-runtime/godot-2d-movement/SKILL.md) | Implement 2D kinematic character movement in Godot 4.7 with CharacterBody2D and move_and_slide(): platformer run/jump with gravity, top-down 8-direction motion, slope. |
| [`godot-3d-essentials`](engine-runtime/godot-3d-essentials/SKILL.md) | Set up a Godot 4.7 3D scene: Node3D transforms, Camera3D, lighting (DirectionalLight3D/OmniLight3D), WorldEnvironment for sky/ambient/tonemap/post, MeshInstance3D materials. |
| [`godot-animation`](engine-runtime/godot-animation/SKILL.md) | Animate in Godot 4.7 three ways: AnimationPlayer for keyframed clips (incl. call and signal tracks), AnimationTree with state machines and blend spaces for character. |
| [`godot-audio`](engine-runtime/godot-audio/SKILL.md) | Play and mix audio in Godot 4.7: AudioStreamPlayer (2D/3D variants), audio buses with volume/mute and effects, music vs SFX routing, db/linear volume, and precise. |
| [`godot-csharp`](engine-runtime/godot-csharp/SKILL.md) | Use C#/.NET in Godot 4.7: partial classes extending nodes, the PascalCase lifecycle (_Ready/_Process/_PhysicsProcess), [Export] fields, [Signal] delegates as C# events. |
| [`godot-export`](engine-runtime/godot-export/SKILL.md) | Export and build a Godot 4.7 project for distribution: install export templates, define export presets (Windows/macOS/Linux/Web/Android), run headless command-line exports. |
| [`godot-gdscript`](engine-runtime/godot-gdscript/SKILL.md) | Write idiomatic GDScript for Godot 4.7: static typing, the node lifecycle (_ready/_process/_physics_process), @export/@onready/@tool annotations, signals, and await for. |
| [`godot-gdscript-headless-testing`](engine-runtime/godot-gdscript-headless-testing/SKILL.md) | Run GDScript test suites from the command line with `godot --headless`, using a SceneTree/MainLoop runner script that exits non-zero on failure so CI can gate merges. Use. |
| [`godot-multiplayer`](engine-runtime/godot-multiplayer/SKILL.md) | Build networked games with Godot 4.7 high-level multiplayer: set up an ENetMultiplayerPeer server/client, define RPCs with the @rpc annotation (call via rpc()/rpc_id()), set. |
| [`godot-nodes-scenes`](engine-runtime/godot-nodes-scenes/SKILL.md) | Structure a Godot 4.7 project with the scene tree and node composition: build reusable scenes, instance PackedScenes at runtime, navigate the tree safely, and register. |
| [`godot-physics`](engine-runtime/godot-physics/SKILL.md) | Use Godot 4.7 physics bodies and detection in 2D and 3D: RigidBody, StaticBody, Area, and CharacterBody; collision layers vs masks; contact/overlap signals; and raycasts. |
| [`godot-resources`](engine-runtime/godot-resources/SKILL.md) | Design data-driven Godot 4.7 games with custom Resource classes: define typed data with class_name + @export, save/load .tres/.res files, instance and duplicate resources. |
| [`godot-shaders`](engine-runtime/godot-shaders/SKILL.md) | Write Godot 4.7 shaders in the Godot Shading Language: canvas_item shaders for 2D and spatial shaders for 3D, with vertex/fragment functions, uniforms (source_color. |
| [`godot-signals-groups`](engine-runtime/godot-signals-groups/SKILL.md) | Build event-driven, decoupled Godot 4.7 gameplay with signals and node groups: declare and emit custom signals, connect with Callables (incl. bind/one-shot), and broadcast to. |
| [`godot-tilemap`](engine-runtime/godot-tilemap/SKILL.md) | Build and edit tile-based 2D levels in Godot 4.7 with TileMapLayer and TileSet: paint layers, set up collision/navigation/custom-data on tiles, autotile with terrain sets. |
| [`godot-ui-control`](engine-runtime/godot-ui-control/SKILL.md) | Build Godot 4.7 user interfaces with Control nodes: anchors and offsets for responsive layout, Container nodes (VBox/HBox/Grid/Margin) for automatic arrangement, Theme. |
## Automation and bridges (`automation/`)

| Skill | What it teaches |
|---|---|
| [`agentic-blender-asset-pipeline`](automation/agentic-blender-asset-pipeline/SKILL.md) | Drive Blender as an agent subroutine (Codex CLI + GPT-6 Astra + Blender MCP): screenshot-measure-execute-assess loop, per-asset ASSESSMENT.md files, non-destructive fit studies, Tripo Smart Mesh modular parts, Mixamo FBX export, level assembly. |
| [`hblink-blender-houdini-bridge`](automation/hblink-blender-houdini-bridge/SKILL.md) | Bridge Blender and Houdini with a live socket link and smart cache: live geometry/UVs/attributes/materials into SOPs or Solaris, RBD caching via rest-fracture plus per-frame transform/velocity point files (35x smaller than Alembic hierarchies), JSON material-rebuild sidecars, beta Blender-rig to KineFX/APEX transfer. |
| [`houdini-jewelry-saas`](automation/houdini-jewelry-saas/SKILL.md) | Productize procedural generation: headless Houdini Engine behind an async queue and server pool with a web UI. |
| [`houdini-mops-blender`](automation/houdini-mops-blender/SKILL.md) | Drive Blender/Cycles rendering with Houdini motion operators. |
| [`nomad-blender-live-link`](automation/nomad-blender-live-link/SKILL.md) | Verify and use the Nomad Sculpt live link to Blender and other PC apps: install the link, round-trip a sculpt iPad-to-PC and back, and check the. |
| [`steam-publish`](automation/steam-publish/SKILL.md) | Publish or update a game on Steam with Steamworks and SteamPipe: configure depots and packages, upload builds with steamcmd, set a build live on a branch, and run the release. |
| [`itch-publish`](automation/itch-publish/SKILL.md) | Publish and update a game on itch.io: create the project page and upload builds with the butler CLI (butler push) to named channels. Use for itch.io publishing, butler push. |
## No-tooling examples (`no-tooling/`)

| Skill | What it teaches |
|---|---|
| [`ragnarok-woe-gameplay`](no-tooling/ragnarok-woe-gameplay/SKILL.md) | NO-TOOLING negative example: gameplay footage with no extractable workflow. Documents what the scout correctly skips. |
| [`topology-rendering-advice`](no-tooling/topology-rendering-advice/SKILL.md) | NO-TOOLING negative example: beginner modeling Q&A with no extractable workflow. Documents what the scout correctly skips. |
