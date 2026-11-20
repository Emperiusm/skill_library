---
name: godot-vertex-animation-texture-crowds
description: "Bake any Blender animation into vertex animation textures (VAT) and play it back on the GPU in Godot: position + normal textures, MultiMeshInstance3D crowds with a unique animation per instance, the 8-bit jitter fix with measured precision, and the Birdteeth indie case. Trigger when a Godot scene needs hundreds of animated characters, creatures, or baked simulations without per-frame CPU skeleton cost."
---

# Vertex animation textures (VAT) for Godot crowds

## Purpose

This skill reconstructs the vertex animation texture workflow end to end, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: bake each animation once into textures (one pixel per vertex per frame), ship the mesh as a static mesh, and replay the animation in the vertex shader, so the CPU does no skeleton work per frame and one draw call renders the whole crowd.

## Source

Creator: stonequailgames (game: Birdteeth, an indie game about birds and teeth). Instagram reel: https://www.instagram.com/reel/Df5WQoyvQop/ (posted Nov 18, 2026, 1,898 likes, 91 comments; 50 comments read). Caption: "Yes, your GPU." Music: C418, "Haggstrom". Full local transcription (faster-whisper tiny), 12 frames read firsthand, work dir `~/workspace/custom-skills/local-video-summarizer/work/Df5WQoyvQop/`.

Reference tutorial (read firsthand, all numbers below are from it unless noted): "Vertex Animation Textures", Mighty Professional Tutorials, https://mightyprofessionalgaming.com/tutorials/vertex-animation-textures.html

Godot shader (read firsthand, MIT licensed): "Vertex animation with instancing (VAT)", godotshaders.com, https://godotshaders.com/shader/vertex-animation-with-instancing/

Blender bakers (verified via Blender Extensions listings): OpenVAT, https://openvat.org/ (GPL-3.0, shader templates MIT); Vertex Animation Toolkit, https://extensions.blender.org/approval-queue/vat/?report_compatibility_issue&version=1.0.12

Houdini reference: SideFX Labs Vertex Animation Textures 3.0 docs, https://www.sidefx.com/docs/houdini/nodes/out/labs--vertex_animation_textures-3.0.html

Crowd-scale reference: "Crowd Sim Remaster" (6,000+ spectators, UE5, Houdini VAT + HISMs), https://www.kaleycho.com/work/crowd-sim-remaster/ and the 80.lv breakdown, https://80.lv/articles/6-000-agents-on-one-game-thread-novel-high-performance-framework-for-gpu-driven-crowd-systems

## VAT vs BAT: pick the right one

This skill is **VAT** (vertex animation textures): the texture stores final vertex **positions**. The sibling skill `engine-runtime/bone-animation-textures-gpu-instancing` is **BAT** (bone animation textures): the texture stores **bone matrices** and the vertex shader still does skinning.

- Use VAT when the motion has no usable skeleton: cloth, destruction, fluid/baked simulations, geometry-nodes animation, or a crowd where you want zero runtime rig cost. VAT also works for skeletal clips, but it throws the rig away at bake time.
- Use BAT when you need to keep the skeleton alive at runtime (per-bone control, partial-body overrides) and only want the CPU skeleton evaluation gone.
- Both share the same limits: no runtime blending between very different clips without warping, no IK, no interaction with the baked motion, and the triangle count still decides the GPU cost. Read the BAT skill's Phase 3 before sizing a crowd: 2M on-screen triangles was too many for low-end devices even with LODs.

## Tools used

Blender 4.2+ with OpenVAT (or the Vertex Animation Toolkit); Godot 4.x (Forward+ for blending; Compatibility renderer works without blending); the AnimatedMultimeshInstance3D addon, https://github.com/shadecoredev/AnimatedMultimeshInstance3D (bakes and plays VAT directly in Godot); the godotshaders.com VAT shader (MIT).

## Phase 1: Understand the layout before touching a tool

**Do**
1. Lay the animation out as a grid: **X axis is the vertex index, Y axis is the frame**. The pixel at (vertex *i*, frame *j*) holds vertex *i*'s position at frame *j*. Two textures: positions (RGB = XYZ) and normals (same layout, RGB = normal remapped from [-1, 1] to [0, 1]).
2. Sample texel centers, never seams: `u = (vertex_id + 0.5) / vertex_count`, `v = (t * framerate + 0.5) / frame_count`. Without the +0.5, bilinear filtering averages two unrelated vertices and the mesh smears sideways.
3. Encode positions through a bounding box, because an 8-bit channel only holds [0, 1]: `pixel = (position - bbox_min) / (bbox_max - bbox_min)`. Decode in the shader: `position = pixel * (bbox_max - bbox_min) + bbox_min`. Ship bbox_min/bbox_max as shader uniforms (two `float4`s).
4. Compute the bounding box over **every frame**, not the rest pose. A vertex that swings outside the box encodes above 1.0, a UNORM texture clamps it to 1.0, and the vertex visibly stops at the box wall.
5. Know which vertex you are. Importers split vertices at UV seams and hard edges and reorder them, so `VERTEX_ID` in the shader is often not the vertex the bake called *i*. The portable answer is to bake each vertex's normalized index into a spare UV channel (Houdini's `uv2`, OpenVAT's `uv1.x`), which travels with the vertex through any reordering.

**Check**
- A 16-vertex banner over 32 frames bakes to a 16 x 32 texture (512 pixels, one per vertex per frame). Vertex 5 at frame 12 lives at u = 5.5 / 16 = 0.34375, v = 12.5 / 32 = 0.390625.
- The decode is one texture sample plus one lerp per vertex. If the shader does more than that to place a vertex, something is wrong.

**Why**
- A texture is a 2D array of numbers to the GPU; nothing says the tuple has to be a color. The whole trick is choosing what to store and where. The half-texel offset is what makes bilinear filtering blend frames (useful) instead of blending neighboring vertices (garbage).

## Phase 2: Bake in Blender with OpenVAT

**Do**
1. Install OpenVAT from Blender Extensions (Preferences > Get Extensions, search "OpenVAT"), or install the Vertex Animation Toolkit from disk. Both are Blender-native: if it deforms in Blender's viewport (armature, cloth, soft body, shape keys, geometry nodes, simulations, third-party plugins), it can be recorded.
2. **Bake your simulations first** (Cache > Bake All Dynamics). VAT reads the simulated result; unbaked cloth or particles abort the bake on purpose.
3. Select one mesh (a collection bakes combined into a single mesh). Set the frame range. Choose 16-bit PNG or half-float EXR output, never 8-bit for characters (see Phase 4 for the numbers).
4. Run the encode. OpenVAT writes: position texture (+ separate normal texture if asked), a JSON sidecar with per-channel min/max bounds, and the proxy mesh as FBX or glTF. The proxy carries the VAT lookup UV (`uv1.x` = normalized vertex id, which survives glTF vertex splits). Keep that UV set; the shader reads block coordinates from it.
5. Vertex Animation Toolkit alternative: same bake, then Quick Export writes `.glb` + `positions.exr`/`.png` + `normals.png`. Settings that matter: Positions `OFFSETS` (motion relative to bind pose, smaller numbers) or `ABSOLUTES` (world space); Normalize on = PNG output, off = OpenEXR Half (exact, bigger); Wrap `NONE` (one long strip), `WRAP` (near-square, GPU-friendly), `WRAP_CROP` (wrapped + empty space cut, smallest).

**Check**
- Dry-run first with OpenVAT's Bake (manual): it validates without writing files and creates an `export_mesh` in-scene. If it errors on unbaked dynamics or a topology change, fix the source animation, never the texture.
- The output texture's width is the vertex count (or the wrapped width) and its height is the frame count. A 2,048-vertex, 64-frame pedestrian at half float is 1 MiB of position data.

**Why**
- The bake is the only place the animation exists as data. Everything downstream (precision, looping, lighting) is decided by the bake's format and bounding box, so a bad bake cannot be fixed in the shader.

## Phase 3: Play it back in Godot with MultiMeshInstance3D

**Do**
1. Easiest path: use the AnimatedMultimeshInstance3D addon (https://github.com/shadecoredev/AnimatedMultimeshInstance3D). It bakes and plays VAT animations directly in Godot, no Blender round-trip needed for Godot-authored animation.
2. Shader path (godotshaders.com VAT shader, MIT): bind two `filter_nearest` textures (`vertex_animation` and `normal_animation`, RGBF format), set `total_frame_count` (image width in pixels) and `total_vertex_count` (image height in pixels), and a `sampling_fps` for the downsampled bake (default 5.0). The shader desyncs instances with a per-instance time offset (`TIME - INSTANCE_ID * 0.19`) and interpolates between adjacent frames by mixing the current and next frame samples (`frame_blend = mod(texture_frame, 1.0)`), so a sparse bake still plays smooth.
3. Per-instance animation selection uses the `INSTANCE_CUSTOM` buffer (Forward+): Red packs the main animation's starting frame (16 bits) + length in frames (16 bits); Green packs the blend animation's start + length; Blue holds the blend timestamp (32 bits); Alpha holds blend duration + blend-out time. Update it with `set_buffer()` when an instance switches animation; nothing else travels between CPU and GPU per frame.
4. Import settings (the forum-tested gotchas): EXR VAT textures must be **Lossless or VRAM Uncompressed**; any compression destroys the encoded positions. **Disable mipmaps** on VAT textures (a mip averages neighboring vertices and neighboring frames into nonsense). Removing the unused alpha channel saves 25% when the shader does not read it.
5. Layout warning: the godotshaders shader lays the texture out **frames across X, vertices down Y** (width = frames, height = verts), while the Birdteeth reel and the Mighty Professional convention lay it out **vertices across X, frames down Y**. Both work; a baker and a shader must agree. Check the layout before debugging anything else.

**Check**
- Tens of thousands of animated meshes render in a single draw call inside MultiMeshInstance3D, each on its own animation and time offset. If the draw-call count grows with instance count, the MultiMesh is not set up.
- A downsampled bake plays smooth: the frame interpolation is visible when scrubbing time slowly. If motion steps, the interpolation mix is missing or the sampler is point-filtered on V.

**Why**
- The only per-instance state is a time offset and the INSTANCE_CUSTOM pack. The CPU issues one draw call for the whole crowd; the GPU reads positions from a texture. That is the entire performance story.

## Phase 4: Fix the jitter (the Birdteeth problem, solved)

**Do**
1. Diagnose first: Birdteeth's reel shows the failure clearly. The bird plays back correctly, then a close-up of the feet shows visible jitter ("It's a little jittery for now, but we have a solution in mind"). The cause is quantization: 8-bit channels give 256 steps per axis, and small vertices swim between steps every frame.
2. Apply the standard fix: bake at **16-bit half-float** (EXR on disk, half float in VRAM). Precision in a 2 m bounding box:

| Format | Bits/channel | Step in a 2 m box | Bytes/vertex/frame | Notes |
|---|---|---|---|---|
| R8G8B8A8_UNORM | 8 | ~7.8 mm (worst error ~3.9 mm) | 4 | Smallest, visibly quantized. Only for large props at a distance. |
| Split 8-bit (two textures) | 16 (two 8-bit lerps) | ~30 µm | 8 | High byte + low byte per axis, reassembled in the shader. Works on hardware without HDR sampling. |
| R16G16B16A16_FLOAT | 16 | ~1 mm worst case, shrinking toward the box minimum | 8 | The common default. Houdini VAT 3.0 recommends HDR output when the budget allows. |
| R32G32B32A32_FLOAT | 32 | ~0.1 µm | 16 | Rarely needed for bounds-normalized positions. |
| BC6H | block-compressed | depends on each 4x4 block (lossy) | 1 | 8x smaller than half float, but a block spans 4 unrelated vertices x 4 frames, so error depends on vertex order. Test per asset. |

3. Worked example (same 2 m box): the hand at 1.42 m encodes to 0.71 in 8-bit, stored as 181, decoding to 1.4196 m (0.4 mm off, worst case 3.9 mm). As a 16-bit split value it is 46,530, splitting into high byte 181 and low byte 194, decoding to 1.420005 m (0.005 mm off).
4. If half-float is not available (mobile/WebGL targets without float-texture support), use split 8-bit: split each normalized coordinate into a high byte and a low byte across two RGB8 textures (Wildlife Studios packs X-high, X-low, Y-high in one texture and Y-low, Z-high, Z-low in the second), reassemble with `value = high * 256 + low` in the shader.
5. Normals have three options, cheapest first: (a) compress into the position texture's **alpha channel** via octahedral encoding (two numbers fit in the one spare channel; Houdini documents this as lossy, "medium-quality normals"; the loss shows most on glossy surfaces, matte hides it); (b) a separate normal texture, RGB = normal * 0.5 + 0.5 (8-bit is usually enough; very smooth glossy surfaces can band); (c) a rotation texture holding a quaternion per vertex per frame, which also carries the tangent so tangent-space normal maps follow the deforming surface.
6. Birdteeth's exact fix is **unconfirmed** (they have not posted the follow-up). Their own hint is "it involves an unused channel in the images!", after rejecting vector images ("GPUs don't play the best with vector images"). The leading hypothesis, labeled as such: they pack the normals into the position texture's alpha channel (the documented Houdini option above), which frees the second texture to carry a low-byte position sample for split-8-bit precision. The verified standard fix, independent of their hint, is 16-bit half-float. Do not present the hypothesis as their answer.

**Check**
- At the fixed iso camera distance, feet and hands hold still between frames. If vertices still swim, check the format first (8-bit PNG is the usual culprit), then the bounding box (a box measured from the rest pose instead of all frames clamps vertices at the wall).
- The alpha-channel packing is only a win if the shader reads it. Verify the normal decode, don't assume the channel is wired up.

**Why**
- Quantization error scales with the bounding box, not the mesh. A 2 m character at 8-bit swims at ~8 mm steps; the same bake in a tight per-part box or at 16-bit is invisible. Precision is a bake-time choice, not a runtime tweak.

## Phase 5: Collision, blending, and the limits that stay

**Do**
1. Handle collision on the CPU, separately from the animation. VAT moves vertices on the GPU; the CPU never knows where they are. Birdteeth's answer to exactly this question: "Since our game doesn't need precise collisions, we actually just approximate all our birds with spheres." Use sphere (or capsule) approximations per instance, driven by the instance transform, not the deformed mesh.
2. Keep one baked LOD per VAT mesh, or disable LOD switching on it. Unreal's AnimToTexture rule (from the BAT skill): the plugin generates textures for one LOD only, so LODs without baked textures show artifacts.
3. Do not blend between two animations whose vertex positions differ a lot; the shader lerps positions, and the in-between is a warped mesh that never existed. Blend only between similar clips, or cut hard.
4. Loop cleanly: with `WRAP` addressing and a texture exactly `frame_count` rows tall, the bilinear filter blends the last row into row 0 correctly. `CLAMP` addressing holds the last pose for a frame and then jumps. The fixes are hand interpolation with an explicit wrap, or appending a copy of frame 0 after the last frame and stopping the playhead one frame early.
5. Never lerp across a cut. If two clips sit back to back in one texture, clamp V inside each clip's rows (Wildlife Studios does this for stacked clips), or point-sample assets whose frames don't correspond.
6. Disable mipmaps (Phase 3) and remember MultiMesh has no frustum culling or LODs: for hundreds of thousands of instances, implement culling yourself.

**Check**
- Collision proxies match the instance transform every frame. If a bird's feet clip through the ground, the proxy is wrong, not the texture.
- Loop seams are invisible: render the last frame and the first frame of a loop and diff them. A pop at the seam means the wrap or the appended frame 0 is missing.

**Why**
- VAT buys animation cost, nothing else. Every system that needs to know where a vertex is (collision, IK, foot placement, interaction) still needs a CPU-side answer, and the honest one is usually a sphere.

## The human method, distilled

1. **Bake once, read in the shader.** Per-frame CPU work per instance does not scale; a texture fetch does.
2. **Precision is decided at bake time.** Format and bounding box are the jitter fix; no shader tweak rescues an 8-bit bake.
3. **Sample texel centers.** The +0.5 offset is the difference between exact values and a smeared mesh.
4. **Separate animation from physics.** The GPU animates; the CPU collides with spheres.

## Failure modes

- **8-bit quantization jitter.** The Birdteeth feet. Fix: 16-bit half-float, or split 8-bit where float textures are unavailable. Never ship 8-bit VAT for a character the camera gets close to.
- **Mipmaps or compression on VAT textures.** Both average encoded positions into nonsense. Lossless/uncompressed, no mipmaps, filter nearest on the VAT samplers.
- **Bounding box measured from the rest pose.** Vertices that swing outside it clamp to 1.0 and stop at the box wall. Measure over all frames.
- **Baker/shader layout mismatch.** Vertices-across vs frames-across are both in use. A transposed texture plays back as garbage, not as a slightly wrong animation.
- **Blending distant clips.** The lerp between two unrelated poses is a warped mesh. Blend similar clips only, or cut.
- **Loop seam pop.** CLAMP addressing or a missing appended frame 0. Use WRAP with an exact frame-count height, or hand interpolation.
- **Topology change mid-bake.** VAT needs constant topology (same vertex IDs start to finish). A modifier that changes vertex count stops the bake; fluid/remeshing sims need the fluid VAT mode (pool of triangles + lookup table), not soft-body VAT.
- **The 1M-zombie comment is unverified.** A commenter on the Birdteeth reel claims 1 million fully animated zombies at 8,000 tris each at ~15fps with VAT. That is an anecdote, not a benchmark; do not quote it as a number.

## AAA studio practice

- **Epic Games, The Matrix Awakens / City Sample (Unreal Engine 5).** The AnimToTexture plugin ships with UE 5.4+ and is the production version of this technique: it bakes skeletal animation into textures and replays it in the material, and the City Sample's MassCrowd map uses it for the background pedestrians. Distant pedestrians are vertex-animated static meshes; the nearest ones stay fully rigged MetaHumans. One baked LOD per mesh (see Phase 5). Source: https://www.unrealcode.net/AnimationTextures.html
- **Naughty Dog did this on PS1.** Crash Bandicoot's characters used vertex animation: every vertex stored every frame at 30 fps, because the PS1 could not evaluate skeletal weighting at runtime. VAT is the same idea with a texture instead of a vertex stream. Source: https://all-things-andy-gavin.com/tag/sgi/
- **Wildlife Studios, Tennis Clash (mobile).** The mobile crowd pipeline behind Tennis Clash ran a test scene of more than 2,000 animated instances on a low-end Samsung Galaxy S6, using split-8-bit encoding and stacked clips with V clamped per clip. The split-byte packing in Phase 4 is their method.
- **Kaley Cho, crowd sim remaster (UE5, 2026).** 6,000+ animated spectators in real time from Houdini VAT + Hierarchical Instanced Static Meshes. The ROP settings that matter: Method Soft (constant topology), Raster Depth 16-bit floating point (8-bit at an 80-unit position range quantizes to ~0.31-unit steps, "enough to see the geometry swim"; 16-bit drops it to ~0.001), Pack Normals into Position Alpha, Engine Unreal. Source: https://www.kaleycho.com/work/crowd-sim-remaster/
- **NVIDIA, skinned instancing (2007).** Bryan Dudash's DirectX 10 demo packed every bone matrix of every frame into one texture and ran 9,547 instanced characters at ~34 fps on a GeForce 8800 GTX (GPU Gems 3, Chapter 2). The texture-as-animation-database shape dates to this demo.
- **Half-Life: Alyx Workshop Tools (Source 2).** Documents importing Houdini VAT bakes, the baked-simulation use case: a sim with no rig replays in-engine from textures.

## Agent automation

- **VAT manifest.** Keep `vat-manifest.json` per character: clips with frame ranges, texture size, texel format, bake date, bounding box min/max, and the layout convention (vertices-across or frames-across). A bake script regenerates every texture from the manifest and fails if any clip's frame range is missing, any texture is stale relative to its source clip, or the layout flag disagrees with the shader.
- **Precision gate.** Record the format and the bounding-box size per bake; compute the worst-case step (box side / 255 for 8-bit, box side / 2048 for half-float) and fail the bake when the step exceeds 2 mm for a character the camera approaches, or 8 mm for distant crowd members. [Thresholds are this skill's own, not studio numbers.]
- **Import-settings gate.** After import, verify each VAT texture is Lossless/VRAM Uncompressed with mipmaps off and filter nearest; log a failure for any compressed or mipmapped VAT texture.
- **Loop-seam check.** At each loop join, render the last frame and the first frame, diff the two frames, and flag pops above a recorded pixel-diff threshold.
- **Triangle-budget gate.** Record on-screen triangle count per crowd tier in the manifest and profile on the lowest target device class (see the BAT skill's Phase 3: 2M triangles was too many for low-end devices even with LODs). A tier that drops the device below its target frame rate is a fail; the fix is fewer triangles, never more VAT.
- **Clip-boundary check.** For stacked clips in one texture, verify V is clamped inside each clip's rows; log a failure for any blend across a cut.

## Valkyrie note

VAT plus MultiMeshInstance3D is the crowd path for Valkyrie: one autonomous citizen per player plus ambient creatures means hundreds of animated meshes, and VAT moves all of it to a single draw call with zero CPU skeleton cost. Two Valkyrie-specific warnings: the fixed iso camera sits close enough to see feet, so the 8-bit jitter Birdteeth shows would be visible here (bake half-float); and the sim still needs real CPU positions for citizen pathing and collision, so pair VAT with sphere/capsule proxies per citizen, exactly as Birdteeth does for birds.

**Depth status:** PARTIAL (complete Godot shader read firsthand, Blender bakers and precision numbers verified from sources, AAA lineage documented; the Godot addon path has not been run hands-on in this session, and Birdteeth's exact jitter fix is unconfirmed, offered as a labeled hypothesis).
