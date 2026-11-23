---
name: comfyui-trellis2-character-pipeline
description: "Generate a game character from one reference image with Claude driving ComfyUI's native TRELLIS.2 pipeline: a pose-locked A-pose or T-pose reference with spread fingers, watertight shell check, Blender retopology and rigging handoff, and GLB export. Trigger when a character must be generated locally from concept art without paid image-to-3D services."
---

# Claude-driven ComfyUI + TRELLIS.2 character pipeline

## Purpose

This skill reconstructs the local image-to-3D character workflow end to end, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: Claude builds and runs a ComfyUI workflow around the native TRELLIS.2 image-to-3D model, the generation output is a watertight mesh in a known rest pose, and Blender turns that mesh into a rigged, engine-ready character. Claude never sculpts geometry by writing Blender Python: the generative model makes the shape, code only moves it through gates.

## Source

Thread source (read firsthand via old Reddit, read-only, 22 Nov 2026): "Why is claude so bad at model creation and how can i help him get better?", r/ClaudeCode, https://www.reddit.com/r/ClaudeCode/comments/1y0f0k2/why_is_claude_so_bad_at_model_creation_and_how/ (posted 19 Nov 2026 by u/ComingDeveloper, 990 points). The procedure comes from the top comment (720 points) by u/Alzeric and its reply chain.

Coverage limits, stated plainly because they bound what this skill may claim:

- 394 of 409 comments were captured; 15 never rendered and nothing about them is asserted here. Long comments were truncated mid-sentence by the page view, so several replies (including one success report and one failure report for this exact procedure) are known only as fragments. No ending was invented for any of them.
- Alzeric's provenance is his own trial and error. No documentation was cited, and when asked, he pointed only to his own experiments. This skill therefore treats the thread as the idea source and rebuilds every executable step from the official ComfyUI and Blender documentation cited below. Nothing in the phases below rests on the thread alone.
- Throughput figures from the thread are deliberately not repeated anywhere in this skill. They are unverified self-reports, and repeating them would turn anecdote into a benchmark.
- Alzeric's own quality caveat stands and is part of this skill: in his replies he says Tripo and Meshy give better model quality than the local TRELLIS-2 route. The local route wins on cost and ownership, not on quality. If quality is the deciding factor and the budget allows a paid service, this is the wrong pipeline; see `automation/ai-3d-tool-selection` for the comparison discipline.

Reference documentation (all read firsthand for this skill):

- ComfyUI TRELLIS.2 tutorial (updated 13 Nov 2026): https://docs.comfy.org/tutorials/3d/trellis2
- ComfyUI blog, "Trellis.2 and Pixal3D Are Now Native in ComfyUI": https://blog.comfy.org/p/trellis2-and-pixal3d-are-now-native?img=https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b1c0b11-4110-4f61-90b4-eec63a27a787_2048x1024.png%22&open=false
- TRELLIS.2 repository (Microsoft Research): https://github.com/microsoft/TRELLIS.2
- Blender Manual, 3D Print Toolbox: https://docs.blender.org/manual/it/3.6/addons/mesh/3d_print_toolbox.html
- Blender Manual, Remeshing (Voxel and Quad/QuadriFlow): https://docs.blender.org/manual/zh-hant/latest/modeling/meshes/retopology.html
- Blender Manual, Rigify basic usage: https://docs.blender.org/manual/ru/4.1/addons/rigging/rigify/basics.html
- AccuRIG (Reallusion, free auto-rigging tool): https://actorcore.reallusion.com/static-page/auto-rig/pre_page/accurig/accurig.html?471181
- ComfyUI API references: https://www.runflow.io/blog/comfyui-api-endpoints and https://codingkit.com/comfyui/api/

## When to use this skill, and when to use a sibling

Dedup map, checked by reading the closest skills in full before this skill was written:

- Use THIS skill for the generation stage itself: ComfyUI plus TRELLIS.2, Claude-built workflow, pose-locked reference, watertight check, and the handoff into Blender. No other skill covers that end-to-end chain.
- `characters/ai-3d-character-pipeline` owns the downstream character discipline: reference preparation, modular parts, classification, the movement test, rig standards, and the engine proof, built from Tripo/Hunyuan sources. This skill defers to it from Phase 7 onward instead of restating it. Read it before rigging.
- `capture/ai-3d-image-to-3d-reconstruction` owns the generator-agnostic repair loop and the six-point sign-off (triangle budget, edge flow, material slots, scale, PBR cleanliness, verified import). If the generated mesh fails sign-off, its repair loop is the procedure.
- `materials-shaders/ai-3d-retopology-uv` owns retopology and UV repair depth. Phase 6 here gives the decision ladder and the limits; that skill gives the wireframe and UV procedure.
- `capture/comfyui-ldoi-image-to-3d` is the sibling ComfyUI image-to-3D skill for a different backend (TripoSG splat, low VRAM, MeshLab Poisson plus voxel remesh). Use it when the target is a static prop on a small GPU, not a rigged character.
- `automation/ai-3d-tool-selection` owns the generator comparison (brief, scoring, retest). Use it before committing to TRELLIS-2 over a paid service.

## License: read this before shipping anything

TRELLIS.2's model and code are released under the MIT License, which permits commercial use of generated outputs. That is the official repository's own license statement, confirmed in the repository listing.

The nuance, stated exactly: the ORIGINAL TRELLIS.2 pipeline depends on two NVIDIA rendering libraries, nvdiffrast (mesh rasterization) and nvdiffrec (PBR rendering), distributed under the NVIDIA Source Code License, which restricts usage to non-commercial research and evaluation. The thread's warning that TRELLIS-2 "can't be used commercially" overstates this: it confuses a dependency license with the model license.

The native ComfyUI integration removes the issue for this pipeline: ComfyUI reimplemented the 3D pipeline in PyTorch and SciPy with no nvdiffrast, no nvdiffrec, no compiled CUDA extensions, and no PyTorch downgrade. Running TRELLIS.2 through the native ComfyUI nodes therefore carries no non-commercial dependency. Two cautions remain: (1) if you ever run the ORIGINAL repository code directly instead of the ComfyUI route, the NVIDIA dependency terms apply to that toolchain; (2) the license covers the model, not your input images, so only feed it art you own or hold rights to use.

## Tools used

- ComfyUI (portable install, current nightly build with native TRELLIS.2 support; see Phase 1 for the version gate)
- TRELLIS.2 weights (Comfy-Org repackaged): `trellis_2_int8_convrot.safetensors`, `trellis_2_shape_vae_bf16.safetensors`, `trellis_2_texture_vae_bf16.safetensors`, `dino_v3_L_naf_fp32.safetensors` (the equivalent `dino_v3_vit_l.safetensors` from the TRELLIS.2 repo also works), `birefnet.safetensors`
- Blender 4.2+ (portable install; 3D Print Toolbox and Rigify are bundled addons)
- An NVIDIA GPU (see the hardware gate in Phase 1)
- Claude Code (or any Claude agent session) driving ComfyUI through its HTTP API on port 8188

## Phase 1: Install and verify the two portable apps

**Do**
1. Install the portable builds side by side: ComfyUI portable (`ComfyUI_windows_portable` on Windows, the equivalent portable layout on Linux) and portable Blender. Record both absolute paths in a `paths.md` file at the project root, exactly as Alzeric's procedure requires: Claude gets paths, not vague install names. Example entries: `comfyui: D:\00-coding\AI\ComfyUI_windows_portable` and `blender: <path to the portable Blender folder>`. Use the real paths on the machine; never invent them.
2. Update ComfyUI to the current nightly build. The native TRELLIS.2 nodes ship in recent ComfyUI; if the template workflow is missing or nodes fail to import at startup, the install is outdated. That is the documented failure mode, not a broken workflow.
3. Download the five weight files listed in Tools used into ComfyUI's standard folders: diffusion model to `models/diffusion_models/`, both VAEs to `models/vae/`, the DINOv3 encoder to `models/clip_vision/`, BiRefNet to `models/background_removal/`. Both diffusion checkpoints (TRELLIS.2 and Pixal3D) are listed by the tutorial because the shared template workflow contains both pipelines and the switch selects one; download both if you use the shared template, or only the TRELLIS.2 checkpoint if you build a TRELLIS.2-only graph.
4. Check the startup flags before the first run. Do NOT launch ComfyUI with the `--use-ck-attention` flag: it silently corrupts TRELLIS.2's shape generation stage, producing broken output with no error. If shape results look wrong and no error appeared, check the startup flags first.
5. Apply the hardware gate honestly. The official TRELLIS.2 repository requires an NVIDIA GPU with at least 24 GB of memory, verified on A100 and H100, Linux only. The ComfyUI native integration ships int8 weights (`trellis_2_int8_convrot.safetensors`) that run on less VRAM, but ComfyUI publishes no VRAM figure for that build, and this skill publishes none either. On a card below 24 GB, treat the first run as a hardware test: if it runs out of memory, the documented fallbacks are the int8 weights, a lower generation resolution, or a hosted/paid service. Do not promise a 16 GB card will work; one thread report claims it, and that report is unverified.

**Check**
- `paths.md` exists with both real absolute paths, and Claude can read them.
- ComfyUI starts with no failed node imports, and the template "Pixal3D & TRELLIS.2: Image to Model" is present in the Template Library.
- `GET http://127.0.0.1:8188/object_info` returns node definitions including the TRELLIS.2 stages (see Phase 3). If they are absent, the build is outdated; update, do not hand-write node definitions.
- A first test generation completes without an out-of-memory error. If it does not, the hardware gate in step 5 applies.

**Why**
Portable installs keep the whole toolchain reproducible and movable: paths in one file, no system-wide installs to drift. The version gate matters because the native nodes are new; an older ComfyUI silently lacks them, and debugging a missing node as a broken workflow wastes the session. The flag check matters because silent corruption is the worst failure mode: broken geometry with no error message looks like a bad model, not a bad launch flag.

## Phase 2: Lock the pose in the reference image

**Do**
1. Start from a reference image that already shows the pose you want the character to keep: for humanoids, an A-pose (arms slightly out, legs straight) or a T-pose (arms straight out), neutral stance, face visible, fingers spread and separated. The thread's pose spec, in the creator's own short fragment, is "A or T pose with spread fingers."
2. Enforce the spec on the INPUT, not on the output. This is a derivation, labeled as such: the native TRELLIS.2 nodes expose no pose parameter, and TRELLIS.2 is a single-image conditioned model, so the output pose follows the input image. There is no setting that re-poses a character after generation. A mid-action reference bakes that action into the topology forever, which is also the rule in `characters/ai-3d-character-pipeline` Phase 1.
3. Check the fingers specifically before generating: spread, separated, visible against the background. Fused or occluded fingers in the reference become fused geometry in the mesh, and no retopology step reliably separates them. Hands are the highest-risk detail zone; inspect them first, in the reference, not after generation.
4. Keep the background clean and the character isolated. The workflow's first stage removes the background with BiRefNet and crops the subject to a centered canvas, with a switch to skip background removal. A busy background that survives the cutout becomes invented geometry. If the cutout eats fingers or thin straps, fix the reference (simpler background, higher contrast at the edges) rather than disabling background removal.
5. Supply front, side, and back references for the HUMAN art-direction check in Phase 4, even though the generator consumes one image. The back the model invents is where character work most often breaks, and a second view is the only cheap way to catch it.

**Check**
- The reference is a true neutral pose: arms symmetric, legs straight, face forward, fingers spread and countable.
- Would a second artist generate the same character from this reference? If not, the reference is not finished.
- The BiRefNet cutout keeps every finger and strap. If any are eaten, fix the reference and re-cut.

**Why**
Generation quality is bounded by reference quality, and pose is the one property that cannot be fixed downstream. Retopology can fix edge flow, rigging can fix deformation, but nothing downstream re-poses a fused mid-action mesh. The pose spec costs nothing at this stage and is nearly unrecoverable later.

## Phase 3: Claude builds the ComfyUI workflow

**Do**
1. Give Claude the `paths.md` file from Phase 1 and one instruction: build the generation workflow from the official template, do not invent nodes. The template is "Pixal3D & TRELLIS.2: Image to Model" in ComfyUI's Template Library, and the workflow JSON is downloadable from the tutorial page. Start from the template file; never hand-author a node graph from memory.
2. Set the pipeline switch. The template contains both the Pixal3D and TRELLIS.2 pipelines; set the `Boolean (Switch to Trellis2)` node to `true` so the workflow loads the TRELLIS.2 checkpoint and its conditioning automatically.
3. Verify the node inventory against the running ComfyUI before queuing. Query `GET http://127.0.0.1:8188/object_info` and confirm these core nodes exist: `Trellis2Conditioning`, `EmptyTrellis2LatentStructure`, `Trellis2ShapeStage`, `Trellis2UpsampleStage`, `Trellis2TextureStage`, `VaeDecodeShapeTrellis`, `VaeDecodeTextureTrellis`. Confirm the post-processing nodes the template uses: `RemeshMesh` (DC remesh), `DecimateMesh` (QEM decimation), `UnwrapMesh` (UV unwrap), `FillHoles`, `WeldVertices`, `MeshSmoothNormals`, `BakeNormalMapFromMesh`, `BakeAmbientOcclusion`, and the export nodes `SaveGLB` / `Save3DAdvanced` plus `Preview3DAdvanced`. If any node is missing, the ComfyUI build is outdated: update it (Phase 1), do not substitute a custom-node pack with a similar name. Custom-node packs for TRELLIS.2 exist and predate the native integration; they are not this pipeline, and they reintroduce the dependency and environment problems the native route removes.
4. Wire the input. The `LoadImage` node takes the Phase 2 reference. Leave background removal on unless the reference already has a clean transparent background; the workflow crops the subject to a centered canvas after removal.
5. Save the workflow in BOTH formats before the first run: the UI workflow JSON (layout plus graph) as `workflow_ui.json`, and the API-format export (File, Export (API), which strips layout data and keeps only the executable graph) as `workflow_api.json`. Claude executes the API format; the UI format is the human-readable record. Never hand-edit the API JSON node IDs: export it from a working UI graph.
6. Claude executes through the ComfyUI HTTP API, which runs on port 8188 by default and has no authentication, so it stays on localhost and is never exposed to a network. Submit with `POST http://127.0.0.1:8188/prompt`, body `{"prompt": <workflow_api.json contents>}` plus a `client_id` UUID. The response returns a `prompt_id`; poll `GET /history/{prompt_id}` for completion and outputs. This is the standard ComfyUI API shape, verified against the API references cited above. If Claude instead runs ComfyUI by hand in the UI, that is equally valid; what is not valid is editing the workflow JSON by hand and queuing it without the export step, because hand-edited graphs drift from what the UI would produce.

**Check**
- The workflow file on disk is an export of the official template, with only the switch, the input image, and the output path changed. Diff it against the template before the first run if anything else was touched.
- Every node in the graph exists in the live `object_info` response. A node that exists in the JSON but not in the server is a failed import, not a typo to fix by renaming.
- The `Boolean (Switch to Trellis2)` node reads `true` in the submitted JSON. A run with the switch off silently generates a Pixal3D model instead, which is a different model with different quality characteristics.
- The `prompt_id` returns a completed history entry with a saved 3D file. A queued job with no history entry has not finished; do not read a partial output.

**Why**
The template is the contract: it encodes the stage order (structure, shape plus upsample to the 1536 target resolution, texture with PBR voxels, then post-processing) that the model authors and ComfyUI tested together. Hand-built graphs skip stages or wire incompatible nodes, and the failure looks like a bad model. The API route exists so Claude can run the pipeline without a human clicking through the UI, but the API format is unforgiving about hand edits, which is why the export step is mandatory. The switch check exists because the shared template's default is Pixal3D, and generating with the wrong model and blaming TRELLIS.2 is an easy, silent mistake.

## Phase 4: Generate and inspect before touching Blender

**Do**
1. Queue one generation from the Phase 2 reference. The three diffusion stages run in sequence (structure, shape, texture), followed by the post-processing chain (DC remesh, QEM decimation, UV unwrap, baking of base color, normal, and ambient occlusion maps). Wait for the history entry; do not read the output directory mid-run.
2. Inspect the mesh in the `Preview3DAdvanced` node, then open the saved file from `ComfyUI/output/3d/ComfyUI/`. Check in this order: pose (does the output hold the A/T-pose with spread fingers?), silhouette (does the outline match the reference from front, side, and back?), fingers and thin parts (are they present and separated, or fused?), and texture (does the PBR set read correctly, with no baked lighting baked into the color map?).
3. Render a turntable or at least four orthographic views (front, left, back, right) and compare each silhouette against the reference image. This is the thread's test-gate idea in its cheapest form; the fuller measured gate (IoU and boundary-fit scores) is the sibling refinement candidate and is not required here, but the four-view comparison is. A front view that matches proves nothing about the back.
4. Decide: accept, repair, or regenerate. Accept only if the pose holds, the silhouette matches on all four views, and the fingers are separated. Repair in Blender (Phase 5 onward) only for shell and topology problems on an otherwise correct shape. Regenerate from a fixed reference if the pose drifted, the back is invented wrong, or the fingers fused: those are input problems, and no downstream step fixes them.

**Check**
- The saved file exists in the output directory and matches the `prompt_id` in the run log. Stale files from earlier runs are the classic false positive.
- Pose, silhouette, fingers, and texture each have an explicit pass or fail recorded in the run log before Blender opens. A mesh with no recorded verdict does not enter Phase 5.
- Generation settings are recorded with the output: workflow JSON filename, checkpoint filenames, seed if the workflow exposes one, and the reference image hash. A regeneration that cannot reproduce the first run's settings is a new experiment, not a retry.

**Why**
Inspection is the cheapest gate in the pipeline and the only one that can reject a bad generation before Blender time is spent on it. The four-view rule exists because single-image generation invents unseen sides from priors, and the invented back is where failures hide. Recording the verdict matters because the most expensive mistake in this workflow is polishing a mesh whose pose was wrong from the start.

## Phase 5: Prove the shell is watertight

**Do**
1. Import the generated GLB into Blender (File, Import, glTF 2.0). Keep the original generated file untouched as the bake source; work on a duplicate. Remeshing destroys UVs and data layers, so the original is the only copy that still carries the generated texture mapping.
2. Run the watertight check with the 3D Print Toolbox, a bundled Blender addon (enable it in Preferences, Add-ons, Mesh, 3D Print Toolbox; in Blender 4.2 and newer it is installed via Blender Extensions). In the 3D Print tab, run the Solid check. Watertight means zero non-manifold edges and zero bad contiguous edges: every edge connects to exactly two faces, and neighboring face normals agree. The Check All operation runs every check at once; the Solid result is the gate, the rest (intersections, degenerate faces, thin faces) is diagnostic.
3. For a scripted gate that Claude can run headless, use bmesh directly: every edge must have exactly two linked faces. In `bpy` terms: `non_manifold = [e for e in bm.edges if len(e.link_faces) != 2]`; the gate passes only when that list is empty. The equivalent toolbox operator is `bpy.ops.mesh.print3d_check_solid()` after enabling the addon with `bpy.ops.preferences.addon_enable(module='object_print3d_utils')`. Record the non-manifold edge count in the run log, not just pass or fail.
4. If the shell is not watertight, repair in this order: first `Fill Holes` (the ComfyUI post-processing chain already includes a FillHoles node; if holes survive it, the Blender-side equivalent is Mesh, Clean Up, Fill Holes); then the toolbox's Make Manifold cleanup, which fixes bad normals, fills holes, and removes empty edges and faces; then, if holes persist, a voxel remesh (Phase 6), which rebuilds the surface and closes the shell by construction. Do not rig or export a mesh that fails the Solid check: rigging a leaky shell bakes the leak into every deformation, and export carries it into the engine.
5. Check the texture survival at this point. If the ComfyUI post-processing already baked base color, normal, and ambient occlusion maps, confirm the maps are present and bound to the Principled BSDF inputs in Blender. If a remesh step destroyed the UVs, the texture must be re-baked from the original (Phase 6), not painted back by hand.

**Check**
- Solid check reads 0 non-manifold edges and 0 bad contiguous edges, recorded as numbers in the run log.
- The original generated file is untouched on disk, and the working duplicate is the only mesh being modified.
- The texture maps survived the import, or their loss is recorded with a re-bake planned in Phase 6.

**Why**
"Watertight" is the thread's word for the requirement, and it is a real gate, not a figure of speech: a mesh with open boundaries has no defined inside, which breaks boolean-style cleanup, breaks remeshing assumptions, and produces visible holes under deformation. The count matters because a single non-manifold edge and a thousand of them need different repairs; a boolean pass/fail hides that. Keeping the original untouched matters because every destructive cleanup step in this phase and the next is lossy, and the only recovery from a bad cleanup is the original file.

## Phase 6: Retopologize for deformation

**Do**
1. Decide by destination, using the classification from `characters/ai-3d-character-pipeline` Phase 3: static, mechanical, or deforming. Only deforming assets (characters, creatures) need deformation topology. A static prop stops at the Phase 5 shell plus decimation; a deforming character continues through this phase. Write the classification down before retopologizing.
2. Run the movement test FIRST, on the generated mesh, before committing to any retopology: bend the joints and watch for pinching, collapsing, or tearing. The test decides the route: good proportions with poor edge flow means retopologize; fused limbs, a locked mid-action pose, or intersections everywhere means regenerate from a better reference (Phase 2), not retopologize. This is the movement test from the sibling skill, applied here at the handoff point.
3. If retopology is the verdict, work in this order, cheapest first:
   a. Try QuadriFlow first, on the cleaned manifold mesh: Properties, Object Data, Remesh, mode Quad, QuadriFlow Remesh. Set the target with Mode Faces (a face count, default 4,000, approximate), keep Use Mesh Symmetry on unless the character is deliberately asymmetric, and set Smooth Normals on. QuadriFlow needs a manifold mesh with consistent normals; if it refuses with the "needs to be manifold" error, the Phase 5 shell was not actually clean, and the fix is Phase 5, not QuadriFlow settings.
   b. If QuadriFlow refuses or the shell is full of overlaps, voxel remesh first, then QuadriFlow on the result. The Voxel remesher rebuilds the surface from a 3D grid, which cleans up intersecting geometry, but it loses all mesh data layers including UVs, and anything thinner than a voxel (fingers, straps, antennae) fuses or vanishes. Choose the voxel size from the thinnest feature you must keep, not from the triangle target.
   c. External options, in cost order: Instant Meshes, a free standalone field-aligned quad mesher (export OBJ, set the target vertex count, solve the orientation field then the position field, export, import back); Exoside Quad Remesher, a paid Blender addon, for the best automatic quad flow. Both are fallbacks, not defaults.
   d. Manual retopology is the production answer for final deforming-character topology. The Blender manual states this directly: QuadriFlow is not recommended for creating final topology on a mesh that will be deformed, because topology must follow the flow of the geometry and no automatic tool does that reliably. Budget the manual pass for hero characters; use automatic topology for background crowds and test assets only.
4. Rebuild UVs after any remesh, because remeshing deletes them. Smart UV Project followed by Pack Islands is the baseline; the UV procedure and overlap repair live in `materials-shaders/ai-3d-retopology-uv`. Then re-bake the generated texture from the untouched original onto the new UVs: the original is the bake source, the retopologized mesh is the bake target. Never bake from the remeshed mesh onto itself; it has no detail left to transfer.
5. Decimate to the platform triangle budget with the ComfyUI `DecimateMesh` (QEM) result or Blender's Decimate modifier, only AFTER retopology, and only if the retopologized mesh still overshoots the budget. Do not use voxel or quad remeshing merely to reduce face count on a mesh with no geometry problems; Decimate is the tool for that, per the Blender manual.

**Check**
- The classification (static, mechanical, deforming) is written down, and the movement-test verdict with its reason is recorded.
- After remesh: the new mesh is manifold, the UVs exist and pack without overlap, and the re-bake from the original carries the generated detail.
- Thin features survived: count the fingers and straps on the retopologized mesh and compare against the reference. A fused finger is a failed remesh, not a detail to fix in the rig.
- Triangle count is at or under the platform budget, recorded as a number.

**Why**
Retopology is where generated meshes become game assets, and the order matters: QuadriFlow gives better edge flow but cannot clean a broken shell, while voxel remesh cleans the shell but eats thin features and UVs. Running them in the wrong order either fails outright (QuadriFlow refusing) or destroys the texture mapping for no reason. The manual-topology limit is the honest ceiling of this phase: automatic tools produce a quad base, not production deformation topology, and pretending otherwise is how rigged characters tear at the elbows.

## Phase 7: Rig, skin, and movement-test under the rig

**Do**
1. Do not rig until Phases 5 and 6 pass. The pre-rig checklist from the sibling skill applies verbatim: neutral rest pose, correct scale (Rigify assumes 1 unit is 1 meter; a human is about 2 units tall), frozen transforms, separated moving parts, clean topology at the joints.
2. Pick the rigging tool by destination and budget, stating the limits of each:
   a. Rigify (bundled Blender addon, enable in Preferences, Add-ons, Rigging): add a Human meta-rig (includes face and fingers; Basic Human does not), edit the bone positions to match the geometry (keep legs straight in front view, slight bend at knees and elbows so Rigify knows the bend direction), then Generate Rig in the Armature properties. Rigify automates the rig controls and bones only; it does NOT attach the rig to the mesh, so skinning is still manual work. The meta-rig stays available for re-generation; keep it.
   b. AccuRIG (free standalone tool from Reallusion/ActorCore): five guided steps, works with A-pose or T-pose, one mesh or multiple meshes (with limits on rigging meshes separately), exports FBX and USD, and includes finger rigging. Limits: the free version does not create facial bones, it runs on Windows, and exporting requires a free ActorCore account. Use it when the rig must be produced fast and the character needs no facial bones; use Rigify when the rig must stay inside Blender and feed the Godot export.
   c. Mixamo (online auto-rigger): an option the sibling skill records, with the usual costs (upload, account, T-pose requirement, generic skeleton). Use it only when neither Rigify nor AccuRIG fits; do not present it as the default.
3. Skin the mesh (weight paint) and test deformation AGAIN under the rig, not just on the raw mesh: bend elbows, knees, shoulders, and fingers, and watch for pinching, collapsing, tearing, and volume loss. A rig cannot fix topology; if the deformation test fails here, the verdict goes back to Phase 6 (retopology), not to more weight painting.
4. Record the rigging verdict: tool used, bone count, skinning pass or fail per joint, and the movement-test result under the rig. A character with no recorded rig verdict does not enter Phase 8.

**Check**
- Rest pose neutral, scale correct, transforms frozen, moving parts separated?
- Does the rigged mesh deform without tearing at elbows, knees, shoulders, and fingers?
- Is the meta-rig (Rigify) or the AccuRIG project file kept alongside the character for re-rigging?

**Why**
Rigging is the most expensive place to discover a topology problem, which is why every gate before it exists. The tool choice matters less than the discipline: a recorded verdict per joint, a kept re-rig source, and a willingness to send a failure back to retopology instead of painting weights over it. The sibling skill's rule holds here unchanged: topology first, rig second, always.

## Phase 8: Refine, export GLB, prove the import

**Do**
1. Apply all transforms before export: Object, Apply, All Transforms (Ctrl+A), so scale is 1 and rotation is 0 on the object. Characters face -Y in Blender for the glTF convention, and 1 Blender unit is 1 meter. Skinned rigs and physics break when transforms are left unapplied.
2. Export with File, Export, glTF 2.0 (.glb/.gltf), format glTF Binary (.glb): one self-contained file with geometry, materials, and textures inside. Settings that matter, all verified against the exporter documentation: Transform, +Y Up ON (converts Blender Z-up to glTF Y-up; turning it off lays the model on its back); Data, Mesh, Apply Modifiers ON (off by default; without it, mirror, subdivision, and boolean results are lost); UVs and Normals ON; Materials set to Export (Placeholder or No Export leaves a grey model); Images Automatic or JPEG. Leave Data, Compression OFF: Godot cannot open Draco-compressed glTF. The exporter only understands Principled BSDF shaders with Image Texture nodes plugged into Base Color, Metallic, Roughness, Normal, Emission, and Alpha; procedural textures and Geometry Nodes fields do not survive export, so bake or convert them first.
3. For a rigged character, keep Animation ON so the clips travel with the file, and confirm the armature modifier is visible so the skin exports. Never export OBJ for anything animated: it stores static geometry only, with no rig or animation data.
4. Prove the import in the target engine (Godot 4.7 for Valkyrie; Unreal or Unity for other projects): import the GLB, confirm the skeleton, skin weights, and animation survived, and play an animation under the game's lighting. Check the retarget onto the engine skeleton where required, and watch for sliding or popping across the animation set. The engine proof is the only proof that matters; a character that deforms in Blender and breaks in the engine was never ready.
5. Store the asset by stage, separately: reference image, workflow JSON files, generated GLB, Blender working file, retopologized mesh, rig, and exported GLB, each in its own file with the run log tying them together. A failed rig pass reruns only the rig stage, never the generation stage.

**Check**
- Export settings recorded: format, +Y Up, Apply Modifiers, Materials Export, Compression off.
- The engine import shows the skeleton, weights, and at least one animation playing without sliding, popping, or tearing.
- Every stage output exists as a separate file, and the run log links them.

**Why**
Export settings are the classic breakage point because the defaults are wrong for this pipeline: Apply Modifiers defaults off, and +Y Up is easy to disturb. The stage separation rule exists because regeneration re-rolls every decision the earlier stages settled; a pipeline that cannot rerun one stage is a pipeline that restarts the asset on every revision.

## The human method, distilled

1. **Claude builds the workflow; the model makes the shape.** Never let Claude sculpt by writing bpy primitives. The generative model is the sculptor; code is the conveyor.
2. **Pose is an input property.** A-pose or T-pose with spread fingers is enforced on the reference image, because no node in this pipeline re-poses anything.
3. **Gate before Blender.** Pose, silhouette, fingers, and texture are judged on the generated file before any cleanup time is spent.
4. **Watertight before rigged.** A leaky shell poisons every downstream stage; the Solid check is a number, not a feeling.
5. **Topology first, rig second.** Automatic topology is a base, not production deformation topology. Manual retopology is budgeted for heroes.
6. **The template is the contract.** Start from the official workflow, export the API JSON, never hand-edit the graph.
7. **Stage outputs stay separate.** A failed stage reruns alone; regeneration is the last resort, not the retry button.
8. **The engine proof is the verdict.** Blender deformation is a rehearsal; the import is the performance.

## Failure modes

- **Background removal eats fingers.** The BiRefNet cutout clips thin features at the silhouette edge. Fix: higher-contrast reference background, or re-cut with the removal switch adjusted; do not disable background removal and let the background become geometry.
- **Pose drift: the output is not in the reference pose.** The reference was not neutral, or the generation invented a pose from a cluttered image. Fix: fix the reference (Phase 2) and regenerate. No downstream step re-poses the mesh.
- **Fingers fused.** The reference had fingers together or occluded, or the voxel remesh fused them. Fix: spread-finger reference and regenerate; if the remesh fused them, re-run Phase 6 with a smaller voxel size chosen from the thinnest finger, or skip voxel remesh and clean the shell by hand.
- **QuadriFlow refuses with the manifold error.** The mesh is not manifold or normals are inconsistent. Fix: return to Phase 5 and clean the shell; do not force QuadriFlow settings past a dirty shell.
- **Voxel remesh eats thin features or deletes the UVs.** Both are documented voxel behavior, not bugs. Fix: choose voxel size from the thinnest feature, keep the original as bake source, and re-bake onto the new UVs.
- **Shape generation is broken with no error.** Check the ComfyUI startup flags for `--use-ck-attention`, which silently corrupts the shape stage. Remove the flag and re-run.
- **Nodes missing when the workflow loads.** The ComfyUI build is outdated. Update to the current nightly; do not substitute custom-node packs.
- **Wrong model generated (Pixal3D output instead of TRELLIS.2).** The `Boolean (Switch to Trellis2)` node was false in the submitted JSON. Set it true, re-export the API JSON, and re-queue.
- **Out of memory on a sub-24 GB card.** The official requirement is 24 GB. Fall back to the int8 weights, lower the generation resolution, or move the generation to a hosted service. Do not treat one unverified thread report as proof a smaller card works.
- **The model lies on its back in the engine.** +Y Up was off at export. Re-export with it on; never rotate the model by hand to compensate.
- **Textures missing or grey in the engine.** Materials was not set to Export, or the shader uses procedural nodes the exporter ignores. Convert to Principled BSDF with image textures and re-export.
- **The rigged character tears at joints in the engine.** Topology failure, not a rig failure. Return to Phase 6; do not paint more weights over it.
- **Baked lighting in the color map.** The generator painted the reference photo's light into the texture. Re-texture with clean PBR maps; the baked-light trap is documented in `capture/ai-3d-image-to-3d-reconstruction` Phase 3.

## AAA studio practice

Production character practice, as documented in the sibling skills read for this build, draws the same lines this skill draws, harder:

- **Production topology is still hand work.** A real-time production character studio reports that retopology is done by hand because automatic tools still do not produce production-ready topology well enough for proper rigging and animation, and the technical stage is completed manually or carefully checked by hand (documented in `characters/ai-3d-character-pipeline`, citing the RenderHub production report). The automation implication is the reverse of the naive one: automate generation and checks, never the retopology verdict. The movement test stays a human gate.
- **End-to-end AI animation pipelines are built around defect correction.** Tencent Games' Motus pipeline generates skeletons and skinning weights automatically, then automatically detects and corrects animation defects: jitter, mesh penetration, joint anomalies, and foot sliding (documented in `characters/ai-3d-character-pipeline`, citing the Gamescom debut report). The lesson: an automated rig pass is half a pipeline. The other half is an automated defect report, and a character that ships without one is unproven. Phase 7's recorded per-joint verdict is this skill's version of that report.
- **Raw generative meshes are not production-ready.** ComfyUI's own framing for the native TRELLIS.2 integration is that raw generative meshes are rarely production-ready, which is why the release ships the post-processing node set (remesh, decimate, unwrap, bake) alongside the generator (ComfyUI blog, cited above). The pipeline shape in this skill, generation plus a full post-processing and repair chain, is the vendor's own shape, not an addition.
- **Stages must stay separable.** Bake3D's workflow separates generation, rigging, animation, and export so a failed rig pass can be revisited without regenerating the model (documented in `characters/ai-3d-character-pipeline`). Phase 8's stage separation rule is the same principle applied to this pipeline.

## Agent automation

- **Paths manifest.** Keep `paths.md` at the project root with the absolute ComfyUI and Blender paths, the ComfyUI version, and the GPU model and VRAM. Verify both paths resolve before any run; a moved portable install breaks every downstream step silently.
- **Weights manifest.** Record the five weight filenames with expected sizes and checksums in `manifest.md` before the first run, and verify all five before touching the graph. A missing VAE produces a confusing node error, not a clear "file missing" message.
- **Workflow freeze.** Save `workflow_ui.json` and `workflow_api.json` per asset, and record the `prompt_id`, checkpoint filenames, seed, and reference image hash in `run-log.md` for every generation. A generation with no recorded settings cannot be reproduced or fairly retried.
- **Gate log.** Record numbers, not adjectives: Solid check non-manifold edge count, triangle counts after generation, after remesh, and after decimation, the four-view silhouette verdict per view, and the per-joint movement-test verdict. Any gate recorded as "looks fine" is treated as not run.
- **Node inventory gate.** Before queuing, query `object_info` and fail the run if any node in the workflow JSON is absent from the server. Never rename a node to make the JSON load.
- **Stage separation.** Store each stage output separately (reference, workflow JSONs, generated GLB, Blender file, retopologized mesh, rig, exported GLB) so a failed rig reruns only the rig stage. The run log links the stages; no stage overwrites another stage's file.
- **License gate.** Record the route used (native ComfyUI nodes) in the run log. If the original repository code is ever used instead, record the NVIDIA dependency terms as applying to that run, and do not ship its outputs commercially without a license review.

## Valkyrie note

This pipeline feeds the Terrarium/Aegis asset flow directly: TRELLIS-2 image-to-3D generation, Blender cleanup and retopology, then the engine, which is the trellis-pipe shape the foundry already runs. What the thread adds to that flow is the Claude-driven construction (paths file, template workflow, API execution) and the pose-locked reference discipline, not a new backend. Slot this skill in as the generation front end: its exported GLB enters the existing flow at the Blender handoff, and from there the existing test-gate discipline applies (silhouette and multi-angle comparison before acceptance; the fuller measured IoU/boundary-fit gate is a separate refinement candidate, not part of this skill).

Two Valkyrie-specific rules. First, large files go to SeaweedFS via Terrarium, never git or LFS: the generated GLB, the Blender working file, and the baked textures are large files, and the repository rule applies to them unchanged. Second, the painted iso-camera look is a human art-direction check that no step here automates: a mesh can pass every gate in this skill (watertight, rigged, clean topology) and still read wrong under the fixed camera, the full-saturation painted palette, and the dappled light. The Phase 4 four-view inspection and the engine proof under game lighting are where that judgment happens, by a human, before the asset is accepted.

**Depth status:** PARTIAL (thread procedure read firsthand with its coverage limits stated; ComfyUI native node names, weight filenames, stage order, and the ck-attention gotcha verified from the official ComfyUI tutorial and blog; TRELLIS.2 hardware minimum and MIT license verified from the official repository listing; Blender toolbox, remesh, and Rigify behavior verified from the Blender Manual; AccuRIG capabilities and limits verified from Reallusion's pages; the ComfyUI API shape verified from API references. No hands-on run of the ComfyUI workflow was performed in this session: the stage order, node wiring, and export path are documentation-grounded, not executed. The pose enforcement on the input image is this skill's derivation from the single-image conditioning design, labeled as such. The sibling-skill AAA citations are attributed to those skills, not re-verified firsthand here.)
