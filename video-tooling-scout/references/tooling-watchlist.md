# Tooling watchlist (keep-on-the-side list)
Append-only institutional memory for video-tooling-scout. Never delete an
entry; annotate it instead: ADOPTED / BACKLOGGED / SUPERSEDED / SKIPPED.

| Date seen | Tool / stage | Seen in | Status | Note |
|-----------|--------------|---------|--------|------|
| 2026-09-27 | Auto-rig + animation retarget stage | r/3Dmodeling "revived 2013 model" + seed run | BACKLOGGED | Audit-verified gap in trellis-pipe; recommend P1 `runtime/rig` stage |
| 2026-09-27 | Seed-generated texture-LOD pyramid (1:1 world-mapped) | r/proceduralgeneration Minecraft-world post | WATCH | Only if planetary-scale terrain is ever needed |
| 2026-09-27 | ComfyUI custom nodes wrapping intake/ stages | r/comfyui "RESISTANCE" (Minimax H3 via @comfyorg) | WATCH | Ride the ecosystem; vendors already do this; seen again 2026-09-27; seen again 2026-09-28 |
| 2026-09-27 | AI video generation (Minimax H3, Seedance 2.0 Fast) | r/comfyui "RESISTANCE" | WATCH | Revisit when Aegis needs a trailer; seen again 2026-09-27; seen again 2026-09-28 |
| 2026-09-27 | Procedural construction shader (blueprint + rim + reverse-erosion) | r/proceduralgeneration blueprint effect | BACKLOGGED | UE-side material functions first; foundry stage later |
| 2026-09-27 | Shader-driven skyline fill | r/proceduralgeneration cyberpunk skyline | WATCH | Directly relevant to Desktop City scale problem |
| 2026-09-27 | Deterministic-vs-learned bot eval harness | r/RagnarokOnline NN-vs-scripts engine | BACKLOGGED | First real milestone candidate for the `ai` service |
| 2026-09-27 | Nano Banana-class image edit in intake/ | r/comfyui "RESISTANCE" | BACKLOGGED | Define intake's image stage as model-swappable; seen again 2026-09-28 |
| 2026-09-27 | MCP servers driving Blender/Unreal (agentic DCC) | r/Simulated "blender and unreal MCP" | BACKLOGGED | P2: spike Blender MCP behind review stage; agents iterate visually; seen again 2026-09-28 |
| 2026-09-27 | Gaussian Splatting preview in review flywheel | r/photogrammetry frame-extractor comments | WATCH | Fast preview before mesh commit; not a mesh replacement |
| 2026-09-27 | SAM background removal for scan cleanup | r/photogrammetry frame-extractor comments | WATCH | Niche: phone-scan cleanup before intake |
| 2026-09-27 | Planer-class mesh refinement (flatten/sharpen/deviation) | r/photogrammetry Blender add-on ($35, MIT) | BACKLOGGED | P1: fits between weld and qa in trellis-pipe |
| 2026-09-27 | Intelligent frame extraction w/ quality scoring | r/photogrammetry cross-platform extractor | BACKLOGGED | Front door if intake ever accepts video |
| 2026-09-27 | Houdini Engine queued SaaS pattern | r/houdini jewelcore | WATCH | Licensing ($525/head/yr, seats exclude SaaS) is the constraint; seen again 2026-09-27 |
| 2026-09-27 | Mesh compression recipe (8-bit UVs, octahedron normals, patch-grid UV) | r/photogrammetry Cave Expedition devlog | BACKLOGGED | P1: adopt as foundry output standard; answers perf-budget gap |
| 2026-09-27 | Virtual texturing w/ GPU feedback rendering (per-quad, per-light) | r/photogrammetry Cave Expedition devlog | BACKLOGGED | pairs with mesh compression; only if scenes get large |
| 2026-09-27 | Non-manifold weld fix for surface-nets meshing | r/photogrammetry Cave Expedition devlog | WATCH | only if voxel meshing enters foundry |
| 2026-09-27 | Obi Physics (particle-based, SDF collision) | r/photogrammetry Cave Expedition devlog | WATCH | proven rope/ragdoll pattern for Aetheria when gameplay modules exist; seen again 2026-09-27 |
| 2026-09-27 | Squishy Volumes (free Blender MPM soft-body, fracture upcoming) | r/Simulated MPM post | WATCH | free; destruction sim if ever needed |
| 2026-09-27 | Agentic cinematic from game source (Claude reads game, makes trailer) | r/aigamedev tower defense post | BACKLOGGED | validates MCP bet from the other side; review-stage cinematic artifact; seen again 2026-09-27 |
| 2026-09-27 | Facepunch.Steamworks + interpolation netcode pattern | r/unity movement smoothing post | WATCH | jitter lessons for when map/world services are built |
| 2026-09-27 | Procedural ribbon cables (Blender GeoNodes) | r/proceduralgeneration | WATCH | prop-detail stage if ever needed |
| 2026-09-27 | Tideglass.app target-driven real-time GPU fluid sim | r/Simulated | WATCH | Aetheria cinematics bucket; author donates 20% to conservation |
| 2026-09-27 | Light Wrangler Blender add-on (gobo lighting rigs) | r/houdini MOPS post | WATCH | minor; only if render-look work grows |
| 2026-09-27 | SPH fracture/contact modeling (Ansys Autodyn-class explicit FEA) | r/Simulated armor-sim comments (CFDMoFo) | WATCH | pro channels use SPH to simplify fracture+contact; author's open-source sim runs realtime ~28fps; only if destruction ever enters scope |
| 2026-09-28 | konte (agentic multi-shot AI video production system, TS DSL, MIT, github.com/shiwano/konte) | r/comfyui "konte" 90-sec multi-shot video | BACKLOGGED | stable asset addresses (video:shot.05.motion), variants instead of overwrite, explicit accepted takes, downstream staleness, review UI, Claude Code/Codex drive ComfyUI; "wrap, never replace" adapter model; P1 acceptance-spec near-hit + P2 agentic-DCC prior art |
| 2026-09-28 | SYF Motion Blur Pro (free OFX motion-blur plugin) | r/vfx Scrapyard Films announcement | WATCH | free closed binary (author declined GitHub request); Vegas Pro + DaVinci Resolve + OFX hosts; GPU/CUDA, HQ/Fast motion estimation + analytic Only Linear/Rotating/Zooming modes, stackable; post-production bucket only |
| 2026-09-28 | UE 5.8 Media Framework video-in-materials + Light Function projector recipe | r/unrealengine Materials Masterclass Ch8 | WATCH | Media Player/File Media Source/Media Texture (2x2 auto-resize), mosaic UV math w/ static switch, SubUV/Flipbook node, yaw-only blueprint billboard, Media Sound component, light-function projector + r.LightFunctionAtlas.Resolution / r.VolumetricFog.GridPixelSize tuning |
| 2026-09-28 | Codex CLI driving Blender via MCP (mannequin-guided camera motion) | r/comfyui Blender mannequin -> MiniMax H3 | WATCH | ~2-min camera blocking in Blender MCP, render 1080x1080 30fps 5s reference, role-assigned inputs (character/environment/camera motion) in MiniMax H3 ref-to-video; check identity drift/framing/background/loop seam; RTX 5070 Ti, 20 steps @ 53s/iter |
| 2026-09-28 | Tripo Smart Mesh P2.0 (multi-view to 3D + Tripo rigging) | r/aigamedev "How can I get 3d models that looks like this?" (clockwork_blue demo) | BACKLOGGED | 52k tris demo, ~1 hr iteration; clean 4-view turnaround input required; answers P1 rig gap partially (auto-rig stage) |
| 2026-09-28 | GPT Astra (mesh split, UV fix, CC0 texture replacement; Blender MCP looping) | r/aigamedev character thread (clockwork_blue, wimblecraft) | WATCH | agentic mesh-repair step; pairs with Blender MCP P2 gap evidence |
| 2026-09-28 | dream-loop (Claude builds model, grades vs goal image, iterates) | r/aigamedev character thread (FinsAssociate, github.com/achimala/dream-loop) | WATCH | grade-and-iterate loop pattern; same shape as konte acceptance records |
| 2026-09-28 | GrandpaCAD (T-pose character generation + rigging) | r/aigamedev character thread (otivplays/Sarcospam) | WATCH | faster than Meshy/Tripo per user report; Mixamo-compatible output |
| 2026-09-28 | Nilo (nilo.io, free browser 3D gen, LOD settings, GLB/FBX export) | r/aigamedev character thread (Nilo_Team) | WATCH | auto-rig bipedal T-pose only; vendor self-promo, verify independently |
