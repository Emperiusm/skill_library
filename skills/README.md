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

## Procedural generation and worlds (`procgen-worlds/`)

| Skill | What it teaches |
|---|---|
| [`cinematic-cavern`](procgen-worlds/cinematic-cavern/SKILL.md) | Build a cinematic cavern scene end to end: Blender blockout, ZBrush sculpt, game-mesh reduction, Substance bake and PBR materials, Unreal export, scripted repairs, a C++ height-field water solver, player-to-water contact, Houdini waterfall, final assembly. |
| [`godot-procgen-city-glb-export-schema`](procgen-worlds/godot-procgen-city-glb-export-schema/SKILL.md) | Ship a Godot procedural city as documented glb: keep generation procedural in-engine, define the schema of custom glb properties so others can write. |
| [`minecraft-world-one-block`](procgen-worlds/minecraft-world-one-block/SKILL.md) | Generate massive voxel worlds from one block with deterministic sampling and LOD. |
| [`one-seed-procedural-game`](procgen-worlds/one-seed-procedural-game/SKILL.md) | Build a game with zero asset files: one seed generates terrain, towns, people, sky, and audio at startup; props from boxes/spheres/cones, sound from sine waves. |
| [`phosphor-command-code-drawn-procgen`](procgen-worlds/phosphor-command-code-drawn-procgen/SKILL.md) | Ship a code-drawn procedural game: no sprites or textures, deliberate phosphor-CRT radar-scope aesthetic, generate operations per contract with a persistent base-builder layer. |
| [`procedural-galaxy-generator-blender`](procgen-worlds/procedural-galaxy-generator-blender/SKILL.md) | Build procedural galaxies in Blender with geometry nodes plus shaders: point clouds for stars, volumes for everything else, energy-preserving far-field glow, keyframed emissive flythroughs, 3D gravitational lensing meshes, dust lanes as layered volume roles (absorption/emission/particles), and instanced deep-field domains with cosmological redshift. |
| [`procedural-pixel-creature-generator`](procgen-worlds/procedural-pixel-creature-generator/SKILL.md) | Generate pixel-art creatures in code (Godot 4.5 / C#): seed-driven bodies, limbs, faces, markings, rigs, and multi-directional animations, with frame counts derived by the rigging engine; export transparent PNG sprite sheets plus a JSON manifest (directions, frames, pivots, timing). |
| [`procedural-pixel-creature-generator-seed-web`](procgen-worlds/procedural-pixel-creature-generator-seed-web/SKILL.md) | Generate pixel creatures from a single seed on the web: 35 body types grown by mask plus cellular automata, 8 sizes from 8 px to 1024 px, 8 animations, 7 palettes; export transparent PNG, GIF, sprite strip, or 12-creature sheet; shareable seed URLs. |
| [`procedural-ribbon-cables`](procgen-worlds/procedural-ribbon-cables/SKILL.md) | Generate ribbon cables procedurally with parametric controls instead of modeling by hand. |
| [`procgen-racing-track-generator`](procgen-worlds/procgen-racing-track-generator/SKILL.md) | Generate endless arcade racing tracks by polygon seeding, midpoint-displacement, bezier smoothing, and bending straight mesh segments along the. |
| [`raup-shell-morphospace`](procgen-worlds/raup-shell-morphospace/SKILL.md) | Generate every seashell from three numbers: David Raup's morphospace (flare, verm, spire), built as a Blender geometry-nodes / TouchDesigner. |
| [`recursive-tree-spawner-parameter-space`](procgen-worlds/recursive-tree-spawner-parameter-space/SKILL.md) | Drive procedural tree generation by sweeping parameter ranges (not the algorithm): one recursive branch spawner yields one species or many depending. |
| [`runevision-voronoi-terrain-stack`](procgen-worlds/runevision-voronoi-terrain-stack/SKILL.md) | Drive large-scale procedural terrain with Voronoi macro-cells for level-design control over noise: LayerProcGen framework, fast erosion filter, GPU. |

## AI video and film (`ai-video/`)

| Skill | What it teaches |
|---|---|
| [`agentic-multishot-ai-video-farm-crew`](ai-video/agentic-multishot-ai-video-farm-crew/SKILL.md) | Produce multi-shot AI video with a tiny render farm and a four-agent crew: per-shot jobs with explicit NOT-ALLOWED-TO-CHANGE lock lists, Pocket AI ComfyUI front-end plus Tensor Master GPU-rental dispatch, Coordinator/Prep/Farm-monitor/QC loop, the four canonical mask failures and fixes. |
| [`avatar-model-comparison-harness`](ai-video/avatar-model-comparison-harness/SKILL.md) | Evaluate lip-synced AI avatar models with a fixed-input comparison harness: same portrait plus same driving audio, one fixed prompt template, a. |
| [`blender-mcp-camera-minimax`](ai-video/blender-mcp-camera-minimax/SKILL.md) | Direct AI video camera moves in 3D first: block with Codex CLI plus Blender MCP, render a reference clip, assign role-based inputs in MiniMax H3. |
| [`claude-cinematic-trailer`](ai-video/claude-cinematic-trailer/SKILL.md) | Direct an AI agent to cut a cinematic trailer from your game, then curate its output. |
| [`konte-multishot-ai-video`](ai-video/konte-multishot-ai-video/SKILL.md) | Run multi-shot AI video like a software project: TypeScript DSL, stable asset addresses, non-destructive variants, explicit acceptances, agents driving ComfyUI. |
| [`minimax-h3-character-swap-comfyui`](ai-video/minimax-h3-character-swap-comfyui/SKILL.md) | Swap a character in video with MiniMax H3 in ComfyUI: SAM3 text-prompt masking, color-inversion repaint signal, saved character units, in-workflow trimming, describe-the-finished-result prompting. |
| [`minimax-h3-character-swap-nomask-lowvram`](ai-video/minimax-h3-character-swap-nomask-lowvram/SKILL.md) | Swap a character in video with MiniMax H3 + Character Swap LoRA in ComfyUI with no masking: 0.4 MP at 8 steps, runs on 6 GB VRAM. Reference-video. |
| [`minimax-h3-selflift-long-video`](ai-video/minimax-h3-selflift-long-video/SKILL.md) | Stitch seamless long videos with MiniMax H3 in ComfyUI without color shift: SelfLift dual-sampling context mode, differential 0.1 noise at seams. |
| [`resistance-sci-fi-short`](ai-video/resistance-sci-fi-short/SKILL.md) | Direct an AI-generated sci-fi short: lock keyframes and concepts first, generate shots as repeatable ComfyUI nodes, keep prompt writing manual, edit and grade in an NLE. |
| [`syf-motion-blur-pro`](ai-video/syf-motion-blur-pro/SKILL.md) | Add motion blur with a free OFX plugin: match the algorithm to the motion type, tune length vs strength, stack instances for complex shots. |
| [`ue58-video-in-materials`](ai-video/ue58-video-in-materials/SKILL.md) | Route real video into Unreal materials: Media Framework, procedural scanlines, CRT glass, mosaic UV math, SubUV flipbooks, light-function projectors. |

## Simulation and VFX (`simulation-vfx/`)

| Skill | What it teaches |
|---|---|
| [`armor-simulation-mode`](simulation-vfx/armor-simulation-mode/SKILL.md) | Simulate armor impacts with SPH fracture and contact modeling. |
| [`baradur-env-breakdown`](simulation-vfx/baradur-env-breakdown/SKILL.md) | Assemble a large-scale VFX environment as labeled reviewable stages (Base/Tower/Lava/Eye/comp): Nuke-style 3D assembly, 100GB+ smoke-sim cache. |
| [`blender-mpm-fracture`](simulation-vfx/blender-mpm-fracture/SKILL.md) | Run 890k-particle Material Point Method sims with Voronoi-cell fracture in Blender. |
| [`blueprint-construction-effect`](simulation-vfx/blueprint-construction-effect/SKILL.md) | Author a reverse-erosion construction effect: blueprint preview, climbing rim shader, ember particle finish. |
| [`houdini-net-break-topo-wedge`](simulation-vfx/houdini-net-break-topo-wedge/SKILL.md) | Break a net in slow motion for commercial VFX: curve-spline knot modeling, glue constraints to kill jitter and untangling, procedural art-directed. |
| [`surface-turbulence-wave-detail`](simulation-vfx/surface-turbulence-wave-detail/SKILL.md) | Add fine surface waves to a cached particle-based liquid simulation without rerunning it: build a fine surface point set, track it with an advection. |
| [`tideglass-fluid-sim`](simulation-vfx/tideglass-fluid-sim/SKILL.md) | Build a target-driven real-time GPU fluid sim. |
| [`weta-bubbles-solver`](simulation-vfx/weta-bubbles-solver/SKILL.md) | Implement a two-way coupled bubbles solver from the Weta FX whitepaper in vanilla Houdini nodes. |

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

## Automation and bridges (`automation/`)

| Skill | What it teaches |
|---|---|
| [`agentic-blender-asset-pipeline`](automation/agentic-blender-asset-pipeline/SKILL.md) | Drive Blender as an agent subroutine (Codex CLI + GPT-6 Astra + Blender MCP): screenshot-measure-execute-assess loop, per-asset ASSESSMENT.md files, non-destructive fit studies, Tripo Smart Mesh modular parts, Mixamo FBX export, level assembly. |
| [`hblink-blender-houdini-bridge`](automation/hblink-blender-houdini-bridge/SKILL.md) | Bridge Blender and Houdini with a live socket link and smart cache: live geometry/UVs/attributes/materials into SOPs or Solaris, RBD caching via rest-fracture plus per-frame transform/velocity point files (35x smaller than Alembic hierarchies), JSON material-rebuild sidecars, beta Blender-rig to KineFX/APEX transfer. |
| [`houdini-jewelry-saas`](automation/houdini-jewelry-saas/SKILL.md) | Productize procedural generation: headless Houdini Engine behind an async queue and server pool with a web UI. |
| [`houdini-mops-blender`](automation/houdini-mops-blender/SKILL.md) | Drive Blender/Cycles rendering with Houdini motion operators. |
| [`nomad-blender-live-link`](automation/nomad-blender-live-link/SKILL.md) | Verify and use the Nomad Sculpt live link to Blender and other PC apps: install the link, round-trip a sculpt iPad-to-PC and back, and check the. |

## No-tooling examples (`no-tooling/`)

| Skill | What it teaches |
|---|---|
| [`ragnarok-woe-gameplay`](no-tooling/ragnarok-woe-gameplay/SKILL.md) | NO-TOOLING negative example: gameplay footage with no extractable workflow. Documents what the scout correctly skips. |
| [`topology-rendering-advice`](no-tooling/topology-rendering-advice/SKILL.md) | NO-TOOLING negative example: beginner modeling Q&A with no extractable workflow. Documents what the scout correctly skips. |
