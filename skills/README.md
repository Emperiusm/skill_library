# Skills

Every directory here is one executable skill: a `SKILL.md` playbook that teaches one workflow end to end. New skills land here with every daily scout run.

## The skills

| Skill | What it teaches |
|---|---|
| [`cinematic-cavern`](cinematic-cavern/SKILL.md) | Build a cinematic cavern scene end to end: Blender blockout, ZBrush sculpt, game-mesh reduction, Substance bake and PBR materials, Unreal export, scripted repairs, a C++ height-field water solver, player-to-water contact, Houdini waterfall, final assembly. |
| [`resistance-sci-fi-short`](resistance-sci-fi-short/SKILL.md) | Direct an AI-generated sci-fi short: lock keyframes and concepts first, generate shots as repeatable ComfyUI nodes, keep prompt writing manual, edit and grade in an NLE. |
| [`fix-lumpy-photogrammetry-meshes`](fix-lumpy-photogrammetry-meshes/SKILL.md) | Fix lumpy photogrammetry meshes in Blender the Planer way: detect planar regions, snap vertices to fitted planes and intersections, prove fidelity with a deviation report. |
| [`cave-expedition-render-tech`](cave-expedition-render-tech/SKILL.md) | Ship heavy voxel-terrain visuals on a performance budget: mesh compression, virtual texturing, GPU-driven detail, each stage held to its budget. |
| [`ragnarok-woe-gameplay`](ragnarok-woe-gameplay/SKILL.md) | NO-TOOLING negative example: gameplay footage with no extractable workflow. Documents what the scout correctly skips. |
| [`blueprint-construction-effect`](blueprint-construction-effect/SKILL.md) | Author a reverse-erosion construction effect: blueprint preview, climbing rim shader, ember particle finish. |
| [`ro-engine-neural-vs-scripts`](ro-engine-neural-vs-scripts/SKILL.md) | Test game AI empirically: pit deterministic behavioral scripts against a learned policy in a custom engine and measure which wins. |
| [`revive-ancient-model`](revive-ancient-model/SKILL.md) | Revive a legacy 3D model: retexture, rig, animate, let the original forms carry it. |
| [`minecraft-world-one-block`](minecraft-world-one-block/SKILL.md) | Generate massive voxel worlds from one block with deterministic sampling and LOD. |
| [`procedural-building-shader`](procedural-building-shader/SKILL.md) | Fill a cyberpunk skyline with a procedural building shader instead of geometry. |
| [`procedural-backrooms-browser`](procedural-backrooms-browser/SKILL.md) | Ship procedural 3D in the browser: client-side WebGPU with a WGSL pipeline and GLSL fallback. |
| [`adaptive-frame-extractor`](adaptive-frame-extractor/SKILL.md) | Feed photogrammetry only the frames it needs: score frames for quality and overlap, extract the best, skip the rest. |
| [`houdini-jewelry-saas`](houdini-jewelry-saas/SKILL.md) | Productize procedural generation: headless Houdini Engine behind an async queue and server pool with a web UI. |
| [`weta-bubbles-solver`](weta-bubbles-solver/SKILL.md) | Implement a two-way coupled bubbles solver from the Weta FX whitepaper in vanilla Houdini nodes. |
| [`realistic-rust-materials`](realistic-rust-materials/SKILL.md) | Author realistic rust as a layered procedural material system with exposed parameters. |
| [`substance-painter-characters`](substance-painter-characters/SKILL.md) | Texture game characters in Substance Painter: bake mesh maps, build materials in layers, keep the stack editable. |
| [`claude-cinematic-trailer`](claude-cinematic-trailer/SKILL.md) | Direct an AI agent to cut a cinematic trailer from your game, then curate its output. |
| [`blender-mpm-fracture`](blender-mpm-fracture/SKILL.md) | Run 890k-particle Material Point Method sims with Voronoi-cell fracture in Blender. |
| [`houdini-mops-blender`](houdini-mops-blender/SKILL.md) | Drive Blender/Cycles rendering with Houdini motion operators. |
| [`multiplayer-movement-smooth`](multiplayer-movement-smooth/SKILL.md) | Smooth multiplayer movement with client prediction and server reconciliation. |
| [`procedural-ribbon-cables`](procedural-ribbon-cables/SKILL.md) | Generate ribbon cables procedurally with parametric controls instead of modeling by hand. |
| [`leather-patch-generator`](leather-patch-generator/SKILL.md) | Generate leather patch materials with a parametric Substance generator. |
| [`tideglass-fluid-sim`](tideglass-fluid-sim/SKILL.md) | Build a target-driven real-time GPU fluid sim. |
| [`armor-simulation-mode`](armor-simulation-mode/SKILL.md) | Simulate armor impacts with SPH fracture and contact modeling. |
| [`topology-rendering-advice`](topology-rendering-advice/SKILL.md) | NO-TOOLING negative example: beginner modeling Q&A with no extractable workflow. Documents what the scout correctly skips. |
| [`konte-multishot-ai-video`](konte-multishot-ai-video/SKILL.md) | Run multi-shot AI video like a software project: TypeScript DSL, stable asset addresses, non-destructive variants, explicit acceptances, agents driving ComfyUI. |
| [`blender-mcp-camera-minimax`](blender-mcp-camera-minimax/SKILL.md) | Direct AI video camera moves in 3D first: block with Codex CLI plus Blender MCP, render a reference clip, assign role-based inputs in MiniMax H3. |
| [`ue58-video-in-materials`](ue58-video-in-materials/SKILL.md) | Route real video into Unreal materials: Media Framework, procedural scanlines, CRT glass, mosaic UV math, SubUV flipbooks, light-function projectors. |
| [`tripo-smart-mesh-character`](tripo-smart-mesh-character/SKILL.md) | Turn multi-view images into 3D characters with Tripo Smart Mesh P2.0, then rig: clean 4-view turnaround input, ~1 hr iteration. |
| [`syf-motion-blur-pro`](syf-motion-blur-pro/SKILL.md) | Add motion blur with a free OFX plugin: match the algorithm to the motion type, tune length vs strength, stack instances for complex shots. |
| [`ai-character-pipeline`](ai-character-pipeline/SKILL.md) | Turn an AI character concept into a rigged, game-ready 3D asset, two methods: Tripo P2.0 generate-then-repair (recommended), or base-mesh-first with AI-assisted rigging. Meshy not recommended. |
| [`agentic-blender-asset-pipeline`](agentic-blender-asset-pipeline/SKILL.md) | Drive Blender as an agent subroutine (Codex CLI + GPT-6 Astra + Blender MCP): screenshot-measure-execute-assess loop, per-asset ASSESSMENT.md files, non-destructive fit studies, Tripo Smart Mesh modular parts, Mixamo FBX export, level assembly. |
| [`layered-vellum-proxy-colliders`](layered-vellum-proxy-colliders/SKILL.md) | Layer hair sims on top of cloth sims in Houdini Vellum without intersection or tangling: simulate cloth first, then give the hair layer simplified VDB-proxy colliders. |
| [`mass-entity-niagara-crowd`](mass-entity-niagara-crowd/SKILL.md) | Render massive UE crowds without per-agent actors: simulate in custom C++ MassEntity processors, stream transform arrays into Niagara GPU particles, animate with VATs. |
| [`hblink-blender-houdini-bridge`](hblink-blender-houdini-bridge/SKILL.md) | Bridge Blender and Houdini with a live socket link and smart cache: live geometry/UVs/attributes/materials into SOPs or Solaris, RBD caching via rest-fracture plus per-frame transform/velocity point files (35x smaller than Alembic hierarchies), JSON material-rebuild sidecars, beta Blender-rig to KineFX/APEX transfer. |
| [`minimax-h3-character-swap-comfyui`](minimax-h3-character-swap-comfyui/SKILL.md) | Swap a character in video with MiniMax H3 in ComfyUI: SAM3 text-prompt masking, color-inversion repaint signal, saved character units, in-workflow trimming, describe-the-finished-result prompting. |
| [`agentic-multishot-ai-video-farm-crew`](agentic-multishot-ai-video-farm-crew/SKILL.md) | Produce multi-shot AI video with a tiny render farm and a four-agent crew: per-shot jobs with explicit NOT-ALLOWED-TO-CHANGE lock lists, Pocket AI ComfyUI front-end plus Tensor Master GPU-rental dispatch, Coordinator/Prep/Farm-monitor/QC loop, the four canonical mask failures and fixes. |
| [`omnichar-portable-characters`](omnichar-portable-characters/SKILL.md) | Ship consistent AI characters across image and video models: encode face/body/wardrobe into a portable .char once (sface + DINOv2 scored), decode per model into Minimax H3, Krea2, Flux2 dev, or klein 9B/4B. |
| [`vathography-depth-remap`](vathography-depth-remap/SKILL.md) | Turn a photo's hidden depth pass into the artwork: Marigold V2 single-photo depth (Apache 2.0), then Blender compositor Color Ramp remap for volume, mist, and focus. |
| [`one-seed-procedural-game`](one-seed-procedural-game/SKILL.md) | Build a game with zero asset files: one seed generates terrain, towns, people, sky, and audio at startup; props from boxes/spheres/cones, sound from sine waves. |
| [`procedural-galaxy-generator-blender`](procedural-galaxy-generator-blender/SKILL.md) | Build procedural galaxies in Blender with geometry nodes plus shaders: point clouds for stars, volumes for everything else, energy-preserving far-field glow, keyframed emissive flythroughs, 3D gravitational lensing meshes, dust lanes as layered volume roles (absorption/emission/particles), and instanced deep-field domains with cosmological redshift. |
| [`procedural-pixel-creature-generator`](procedural-pixel-creature-generator/SKILL.md) | Generate pixel-art creatures in code (Godot 4.5 / C#): seed-driven bodies, limbs, faces, markings, rigs, and multi-directional animations, with frame counts derived by the rigging engine; export transparent PNG sprite sheets plus a JSON manifest (directions, frames, pivots, timing). |
| [`procedural-pixel-creature-generator-seed-web`](procedural-pixel-creature-generator-seed-web/SKILL.md) | Generate pixel creatures from a single seed on the web: 35 body types grown by mask plus cellular automata, 8 sizes from 8 px to 1024 px, 8 animations, 7 palettes; export transparent PNG, GIF, sprite strip, or 12-creature sheet; shareable seed URLs. |
