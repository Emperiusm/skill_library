---
name: godot-shallow-water-stream-sim
description: "Build a real-time shallow-water stream simulation in Godot 4 with RenderingDevice compute shaders: CPU heightfield prototype first, then a well-balanced staggered-grid shallow-water discretization on the GPU with tuned substeps for stability, and sim-tied visual layers (mesh displacement, advected ripple coordinates, caustics, foam last). Trigger when a Godot game needs a live stream, creek, or pool whose water motion is simulated, not baked or faked."
---

# Shallow-water stream simulation in Godot: CPU prototype, GPU compute, sim-tied water

## Purpose

This skill reconstructs the shallow-water stream workflow end to end, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: one live simulation, every visual layer reads from it, no baked or faked water motion. Build the scheme on the CPU first, port it to Godot compute shaders second, and add foam and caustics last, since they only read from the sim.

## Source

Thread: r/GraphicsProgramming, "breakdown of a real-time stream, shallow water equations on the GPU", by u/Key_Calligrapher6269, submitted 18 Nov 2026: https://www.reddit.com/r/GraphicsProgramming/comments/1xzcqjg/breakdown_of_a_realtime_stream_shallow_water/ (21 of 21 comments captured in the audit; the embedded video was not inspected). Coverage limits, stated plainly: the live demo at stream.mulualem.com was NOT visited or tested. Nothing in this skill asserts anything about that demo's performance, grid size, frame rate, hardware, or code. The author built his demo with three.js WebGPU and TSL; none of that transfers to Godot, and no three.js or TSL detail appears below. The thread author's stated setting of 8 substeps per frame is his setting for his demo, not a recommendation; Phase 4 treats substep count as a tuning parameter with a procedure for choosing it. A tutorial series linked in the thread was removed and unreadable; nothing in this skill comes from it, and it is not cited anywhere below.

Papers (read firsthand for this skill unless labeled otherwise):

- N. Chentanez, M. Muller, "Real-Time Simulation of Large Bodies of Water with Small Scale Details", SCA 2010. PDF read firsthand: https://matthias-research.github.io/pages/publications/hfFluid.pdf . The shallow-water scheme in Phases 2 and 4 (equations, staggered grid, height integration, velocity update, boundary conditions, stability clamps, overshoot reduction) comes from this paper.
- E. Audusse, F. Bouchut, M.-O. Bristeau, R. Klein, B. Perthame, "A Fast and Stable Well-Balanced Scheme with Hydrostatic Reconstruction for Shallow Water Flows", SIAM J. Sci. Comput. 2004. PDF read firsthand: http://publications.imp.fu-berlin.de/478/1/file_2004_siam.pdf . The well-balanced definition and the hydrostatic reconstruction in Phase 3 come from this paper.
- N. Thurey, M. Muller, S. Schirm, M. Gross, "Real-time Breaking Waves for Shallow Water Simulations", Pacific Graphics 2007; and N. Thurey, F. Sadlo, S. Schirm, M. Muller, M. Gross, "Real-time Simulations of Bubbles and Foam within a Shallow-Water Framework", SCA 2007. Titles and venues as reported in the thread audit; the papers themselves were not read for this skill, and no claim below depends on their contents beyond the lineage: breaking waves and foam inside a shallow-water framework are later layers on the same model, not a different model.
- Boundary, what NOT to build: N. Chentanez, M. Muller, "Real-Time Eulerian Water Simulation Using a Restricted Tall Cell Grid", ACM TOG SIGGRAPH 2011. Per the audit's firsthand read, this paper solves the full 3D inviscid Euler equations with an incompressibility constraint and a pressure solve (multigrid Poisson solver) on a tall-cell grid. It is NOT a shallow-water method. It is the boundary of this skill: do not build its grid or its solver for streams and pools. See "What this skill is not" below.

Godot grounding (read firsthand for this skill):

- "Using compute shaders", Godot docs (verified on both the 4.2 and the stable tutorial pages, identical content): https://docs.godotengine.org/en/stable/tutorials/shaders/compute_shaders.html . The full dispatch pattern in Phase 5 (local RenderingDevice, SPIR-V shader creation, storage buffers, uniform sets, compute pipeline, compute list, submit/sync discipline, the 2 to 3 frame sync delay guidance, Forward+ or Mobile only, no RenderDoc on local devices) comes from this tutorial.
- RenderingDevice class reference, Godot 4.4 docs: https://docs.godotengine.org/en/4.4/classes/class_renderingdevice.html . Method signatures verified there: `compute_pipeline_create`, `compute_list_begin`, `compute_list_bind_compute_pipeline`, `compute_list_bind_uniform_set`, `compute_list_dispatch`, `compute_list_add_barrier`, `compute_list_end`, `storage_buffer_create`, `buffer_get_data`, `buffer_update`, `texture_create`, `texture_get_data`, `uniform_set_create`, `barrier`, `full_barrier`, `submit`, `sync`, `free_rid`, `get_rendering_device`, `DATA_FORMAT_R32_SFLOAT`, `TEXTURE_USAGE_STORAGE_BIT`, `UNIFORM_TYPE_IMAGE`.
- RDTextureFormat class reference, Godot 4.3 docs: https://docs.godotengine.org/en/4.3/classes/class_rdtextureformat.html . Properties verified there: `format`, `width`, `height`, `usage_bits`, `texture_type`, `array_layers`, `depth`, `mipmaps`, `samples`.
- Textures in Godot compute shaders (image2D declarations, the format-matching rule, `UNIFORM_TYPE_IMAGE`, sampler uniforms, `texture_get_data` / `texture_update` readback): https://nekotoarts.github.io/blog/Compute-Shader-Textures (read firsthand).
- Texture2DRD pattern (compute output sampled directly by a material shader with no CPU readback): Godot forum, "Draw Compute Shader As Texture", https://forum.godotengine.org/t/draw-compute-shader-as-texture/104081 , and the godot-demo-projects compute texture demo (height data written by a compute shader, read by a material shader, RIDs cycled for history), https://github.com/godotengine/godot-demo-projects/commit/f29a12d6b6643186a0c5091395ce55e3443df1e6 . Both read as search records; the pattern is stated here as reported there, and Phase 6 tells you how to verify it in your own project.
- C# API names: verified against a working Godot 4.4 .NET example post, https://forum.godotengine.org/t/having-difficulties-with-renderingdevice-buffergetdataasync-godot-4-4-net/105520 . The C# mapping in Phase 5 is an API-name mapping from that example, not code run hands-on. Recheck every name against the Godot 4.7 class reference at build time: the grounding pages above are 4.2, 4.3, 4.4, and stable, and no 4.7 docs page was opened for this skill.

## Tools used

Godot 4.x with the Forward+ or Mobile renderer (RenderingDevice is not available in headless mode or with the Compatibility renderer); GDScript and/or C#; GLSL compute shaders (`.glsl` files with the `#[compute]` hint); a CPU prototype in GDScript or C# written first, before any GPU work.

## The state, the equations, and the grid

The simulation state is a heightfield over a flat 2D grid. Each cell stores a bed height and a water depth; each face stores one velocity component. In the notation of the SCA 2010 paper:

- `h[i,j]`: water depth at the cell center.
- `H[i,j]`: terrain (bed) height at the cell center. The bed never changes during the sim.
- `eta[i,j] = h[i,j] + H[i,j]`: water surface height at the cell center. Surface height, not depth, is the quantity that drives flow.
- `u[i+1/2,j]`: x velocity, stored at the face between cell `(i,j)` and cell `(i+1,j)`.
- `w[i,j+1/2]`: z velocity, stored at the face between cell `(i,j)` and cell `(i,j+1)`.

The shallow water equations, as stated in the SCA 2010 paper:

- Height: `Dh/Dt = -h * div(v)`, the depth changes by the divergence of the velocity field.
- Velocity: `Dv/Dt = -g * grad(eta) + a_ext`, the velocity changes by the surface-height gradient plus external acceleration (gravity along the slope, user forces, obstacles).

The grid is staggered (a MAC grid): depths and bed heights live at cell centers, velocities live at faces. The staggering is load-bearing, not cosmetic. A face velocity sits exactly where the flux between two cells is decided, so the height update reads the velocity that belongs to that edge, and the velocity update reads the surface difference across that same edge. A co-located grid (all quantities at centers) needs extra averaging at every edge and invites the checkerboard-style decoupling that staggered storage avoids.

**Well-balanced** has a precise meaning, from Audusse et al. 2004: a scheme is well-balanced when it preserves the lake-at-rest steady state (`h + z = constant`, `u = 0`, where `z` is the bed height) exactly at the discrete level, over a non-flat bed. A scheme that is not well-balanced manufactures waves out of still water wherever the bed slopes, because its discrete flux and its discrete bed-slope source term do not cancel. Phase 3 is the construction that makes them cancel. The thread author's phrase "well-balanced scheme on a staggered grid" names exactly this combination.

## What this skill is not

- Not the tall-cells method. The 2011 tall-cells paper is full 3D Euler with a pressure solve and a multigrid solver. Building it for a stream is building a heavier, more general model than the job needs. The shallow-water model is the cheap model for streams and pools: a height plus velocity field on a grid, no pressure solve.
- Not 3D FLIP, SPH, or particle water. Those solve a different model at a different cost.
- Not baked water. Scrolling normal maps and looping vertex waves are the thing this skill replaces: they cannot react to a rock, a dam, or a player, because nothing is simulated.
- Not a performance claim. No frame rate, grid size, or hardware figure from the thread's demo transfers here; all of those were unstated or unverified. Measure your own grid on your own hardware (Phase 10).

## Phase 1: CPU heightfield prototype first

**Do**
1. Build the sim as plain arrays on the CPU first, in GDScript or C#, with no GPU code at all. One flat bed, one rectangular domain, still water, no inflow. State arrays: `h`, `H`, `u`, `w`, all sized to the grid.
2. Implement one time step as three ordered passes, following the SCA 2010 paper's time splitting: first self-advect the velocity field, then integrate the height field and the velocity field forward in time.
3. Start with the simplest possible scene: a level bed, a constant depth, zero velocity. Then add one raised bed section under a level surface (the paper's teaching case, and the Cinematic Cavern guide's orange-vs-green test: comparing depth alone creates a false wave; comparing surface height keeps it level).
4. Add one disturbance by hand: raise `h` in a few cells, or inject velocity at a face, and watch the wave spread and settle.

**Check**
- Still water over a flat bed stays still, bit for bit, for a thousand steps. If it moves, the update order or the indexing is wrong; fix it here, not on the GPU.
- Still water over a raised bed stays still (this is the lake-at-rest test; it will fail until Phase 3, and that failure is the point: it proves the test can catch the bug).
- A single disturbance spreads as a wave and settles back toward level. Volume in a closed domain is conserved to float tolerance: sum `h` over all cells before and after, and compare.
- No depth ever goes negative in any test. Clamp `h` to zero or above (Phase 4) from the first prototype onward.

**Why**
The CPU prototype is where the scheme is debugged. A GPU port of a broken scheme is undebuggable: you cannot print a compute shader's intermediate state without a readback round trip, and a wrong result on the GPU could be the scheme, the port, the dispatch, or the barrier. A verified CPU reference turns every GPU discrepancy into a porting bug with a known-good answer to diff against.

## Phase 2: Staggered-grid shallow-water discretization

**Do**
1. Lay out the arrays exactly as the state section above: `h` and `H` at cell centers `(i,j)`; `u` at x faces `(i+1/2,j)`, sized `(nx+1) x ny`; `w` at z faces `(i,j+1/2)`, sized `nx x (ny+1)`. Keep the face arrays one wider than the cell grid in their own axis; off-by-one face indexing is the classic first bug in this scheme, and the sizes above make it visible.
2. Height integration: update each cell's depth from the divergence of the face velocities around it (upwind integration, which the paper uses because it guarantees mass conservation). In words: a cell gains what flows in through its four faces and loses what flows out; the flux through a face is the face velocity times the upwind depth at that face.
3. Velocity update: update each face velocity from the surface-height difference across that face, `(-g * (eta[i+1,j] - eta[i,j]) / dx + a_ext) * dt` for a u face, and the matching z form for a w face. Note what is differenced: surface height `eta`, never depth `h`. Differencing depth across a sloping bed manufactures a phantom gradient where the surface is level.
4. Self-advection of velocity: advect the velocity field by itself before the height/velocity integration (the paper's time splitting). The paper uses a modified MacCormack advection scheme with a semi-Lagrangian fallback for stability; implement semi-Lagrangian advection first (sample the velocity field at the backtraced position), and treat MacCormack as the upgrade once the semi-Lagrangian version is verified, since semi-Lagrangian advection is unconditionally stable and its only cost is numerical diffusion.
5. Boundary conditions, per the paper:
   - Reflective faces (walls, banks, static obstacles): the face velocity is set to 0 at the end of every time step and is not updated. A face is also treated as reflective when the water level in a wet cell is not higher than the terrain level in the neighboring dry cell: with epsilon a small constant (the paper uses `1e-4 * dx`), the face at `(i+1/2,j)` is a wall when `h[i,j] <= epsilon` and `H[i,j] > eta[i+1,j]`, or the mirror condition on the other side. Water does not start flowing into a dry cell until its surface is above that cell's bed.
   - Absorbing borders (open water edges): a damping region near the border, 10 cells wide in the paper's examples, where waves decay before reaching the edge. The paper adapts a Perfectly Matched Layer formulation with a damping field; the damping coefficient increases quadratically or cubically from the inner edge of the region to the border, with decay and update constants of 0.9 and 0.1 in the paper's examples. A stream with banks on two sides and open ends uses reflective conditions on the banks and absorbing conditions at the ends.
6. Bed from authored terrain: sample the Pellune terrain height into `H` once at startup (or author `H` directly for a test pool). The sim domain is a rectangle in world space; cells outside the water's footprint are dry (`h = 0`) and stay dry unless water reaches them.

**Check**
- The lake-at-rest test over a flat bed passes exactly. Over a sloped bed it fails until Phase 3; record the failure magnitude (max surface drift per step) so Phase 3 has a before number.
- A wave hitting a reflective wall reflects; a wave entering the damping region decays to negligible amplitude before the border, with no visible reflection back into the domain.
- Dry cells stay dry when the neighboring water surface is below their bed, and start wetting the moment it rises above.
- Mass conservation: in a closed reflective domain, total water volume is constant to float tolerance across the run.

**Why**
Staggering puts each quantity where its update needs it, and differencing surface height instead of depth is what makes the physics right over uneven beds. The boundary rules are part of the scheme, not polish: a stream without absorbing ends rings forever, and a bank without the dry-face rule leaks uphill.

## Phase 3: Well-balanced treatment over varying bed height (hydrostatic reconstruction)

**Do**
1. Implement the hydrostatic reconstruction of Audusse et al. 2004 at every face, before computing the flux. For the face between cell `i` and cell `i+1`, with bed heights `z[i]`, `z[i+1]` and interface bed height `z[i+1/2] = max(z[i], z[i+1])`:
   - Left reconstructed depth: `h[i+1/2-] = max(0, h[i] + z[i] - z[i+1/2])`.
   - Right reconstructed depth: `h[i+1/2+] = max(0, h[i+1] + z[i+1] - z[i+1/2])`.
   - The reconstructed states carry the cell's own velocity unchanged. Apply the same construction in the z direction for w faces.
2. Discretize the bed-slope source term as the discrete gradient of the hydrostatic momentum flux, so that it cancels the flux difference exactly at rest: the source term for a cell is built from the reconstructed depths at its two faces, not from a cell-centered evaluation of the bed slope. The paper's form: the momentum source is `(g/2) * (h[i+1/2-]^2 - h[i-1/2+]^2)` in the cell's momentum update, which is exactly the difference the flux term produces at rest, with opposite sign.
3. Keep the nonnegativity truncation: reconstructed depths are clamped at zero by construction (the `max(0, ...)` above), which is what lets the scheme handle dry states (`h = 0`) without producing negative depths at wetting fronts.
4. Re-run the Phase 2 tests unchanged. Nothing else in the update changes; only the face states and the source term change.

**Check**
- The lake-at-rest test over the raised bed now passes exactly: `eta` constant, velocities zero, to float tolerance, for a thousand steps. This is the definition of well-balanced, and it is the gate for this phase: do not proceed to the GPU port until it passes.
- A small perturbation on top of the resting lake evolves (a ripple spreads) while the background lake stays at rest. The scheme must preserve the steady state AND compute small deviations from it accurately; a scheme that damps everything to stillness passes the first half and fails the second.
- Dry-bed wetting still works: a wetting front advancing onto a dry slope produces no negative depths and no phantom velocity ahead of the front.

**Why**
A cell-centered source term cannot hold a lake at rest over a slope, because its truncation error has a different structure from the flux term's. The reconstruction rebuilds the face states so that, at rest, the flux difference and the source term are the same number with opposite signs. It is a local fix (per face, per step) with a global consequence: still water stays still on any bed, which is the precondition for every visual layer downstream.

## Phase 4: Substeps and stability

**Do**
1. Treat the substep count as a stability tuning parameter, never as a constant. The thread author's "8 substeps per frame" is his stated setting for his demo. It is not a recommendation, not a default, and not transferable: his grid size, cell size, depths, and frame rate were unstated, and substep need scales with all of them.
2. Use explicit integration with the paper's stability measures. The SCA 2010 paper integrates explicitly (it cannot pre-factorize a matrix, since the grid spacing is fixed) and handles the unstable terms specially. Its published stabilizers, used in all of its examples, are:
   - Clamp `h` to zero or above every substep. Negative depth is unphysical and destabilizing; clamping is not optional.
   - Clamp face velocity magnitudes to `0.5 * dx / dt`. This caps the wave speed the scheme will carry, and greatly improves stability in violent scenes.
   - Limit the water depth used in the height integration: replace the averaged depth in the flux with the averaged depth minus an adjustment that caps it from above (the paper's form subtracts `h_adj = max(0, h_avg - h_avg_max)` with `h_avg_max = beta * g * dt^2 / dx` and `beta = 2.0` in all examples). This caps the wavelengths and amplitudes the scheme carries in deep water, and stabilizes the sim while keeping plausible results.
   - Apply the paper's overshoot reduction at sharp wave fronts entering shallow water: detect edges where the surface jumps by more than a threshold (the paper uses `lambda_edge = 2 * dx`) and relax the crest cell's depth toward its neighbors by a factor between 0.1 and 0.5. Without it, waves that shoal onto a shallow shelf develop numerical ripples and overshoot artifacts.
3. Choose the substep count by procedure, and record the result:
   - Start at 1 substep per rendered frame at the target frame time.
   - Run the violent-input test (Phase 10): a large disturbance, the deepest water in the scene, the steepest bed, all at once.
   - If the sim NaNs, explodes, or produces negative depths the clamps cannot contain, double the substep count (halving the step each substep takes) and repeat.
   - Stop at the smallest count that survives the violent test plus a soak test (Phase 10). Record the count together with the grid size, `dx`, `dt`, and max depth in the sim manifest (see Agent automation). A count chosen this way is a property of your scene, not a borrowed number.
   - Re-tune whenever the grid, the cell size, or the max depth changes. Finer cells and deeper water both need smaller steps; the Courant condition for shallow water (`dt` bounded by `dx / sqrt(g * h_max)`, wave speed `sqrt(g*h)`) is the scaling law behind the retune.
4. Keep the render frame rate and the sim step separate: accumulate real frame time, run a fixed number of fixed-size substeps per frame, and carry the remainder. Variable `dt` per frame re-tunes stability every frame; fixed substeps make the stability behavior reproducible.

**Check**
- The violent-input test survives: no NaN, no negative depths, velocities stay within the clamp, and the sim settles afterward instead of ringing forever.
- Halving the substep count from the chosen value breaks the violent test (this proves the count is doing work, not padding), and doubling it changes the visible result only negligibly (this proves the count is converged, not still compensating for a scheme bug).
- Frame time at the chosen count fits the budget on target hardware at the shipping grid size. If it does not, shrink the grid before weakening the clamps: a smaller stable sim beats a larger exploding one.

**Why**
Explicit integration is cheap per step and unstable past its stability limit, and the limit depends on cell size and depth. Substeps buy stability without changing the scheme, but every substep costs a full grid update, so the count is a budget decision made by measurement. The paper's clamps are the other half of the same deal: they trade a bounded amount of physical fidelity (capped wave speed, capped deep-water amplitude) for stability in exactly the violent cases a game produces.

## Phase 5: Compute-shader port (Godot RenderingDevice)

**Do**
1. Confirm the renderer first: compute shaders require a RenderingDevice-based renderer (Forward+ or Mobile). Check the project is not on Compatibility, and that the game does not run headless for this feature. RenderingDevice is not available in headless mode or with the Compatibility rendering method.
2. Write the compute shader as a `.glsl` file. The two header lines are fixed and must not change: `#[compute]` (the Godot-specific hint the editor needs to import the file as a compute shader) and `#version 450`. Declare the workgroup size (`layout(local_size_x = 8, local_size_y = 8) in;` is a reasonable starting point for a 2D grid; 16x16 is the other common choice) and the state bindings:
   - Storage buffers: `layout(set = 0, binding = 0, std430) restrict buffer HeightBuffer { float data[]; }` and matching buffers for `u`, `w`, and the bed. The `restrict` keyword tells the compiler the buffer is accessed from one place only; the tutorial says to always use it when you can. `std430` is the memory layout; the `set` and `binding` numbers must match the uniform set built on the CPU side exactly.
   - Or storage textures, when the rendering shaders must sample the state directly: `layout(set = 0, binding = 0, rgba32f) uniform image2D height_image;` with `imageStore` writes at integer texel coordinates from `gl_GlobalInvocationID.xy`. The image format in the shader (`rgba32f`) must exactly match the `RDTextureFormat` format on the CPU side (`DATA_FORMAT_R32G32B32A32_SFLOAT`); a mismatch is garbage or an error, not a subtle difference. For a single float per cell (depth only), `r32f` in the shader with `DATA_FORMAT_R32_SFLOAT` on the CPU side is the matching pair.
   - One invocation per cell. Guard every access with a bounds check against the grid size (`if (gl_GlobalInvocationID.x >= nx || gl_GlobalInvocationID.y >= ny) return;`), because the dispatch grid is rounded up to whole workgroups and the edge workgroup extends past the domain.
3. Ping-pong the state. A compute invocation must not read a neighbor that another invocation in the same dispatch is writing. Keep two copies of each state array (or texture) and alternate read/write roles each substep, or split the update into separate dispatches (advect pass, height pass, velocity pass) with a barrier between dependent passes. The double-buffered form is the simpler correct one; the multi-pass form matches the paper's time splitting more literally. Either way, never read and write the same buffer in one dispatch.
4. Build the host side in the order the Godot compute tutorial documents:
   - Create the device: `var rd := RenderingServer.create_local_rendering_device()` for a local device (separate thread, CPU readback path), or `RenderingServer.get_rendering_device()` for the global device (required when a Texture2DRD must expose the texture to material shaders; see step 6).
   - Load and compile the shader: `var shader_file := load("res://water_sim.glsl")`, `var shader_spirv: RDShaderSPIRV = shader_file.get_spirv()`, `var shader := rd.shader_create_from_spirv(shader_spirv)`.
   - Create the state: `rd.storage_buffer_create(size_bytes, data_bytes)` for buffers (data as `PackedByteArray`, from a `PackedFloat32Array` via `to_byte_array()`), or `rd.texture_create(format, view, data)` for textures with an `RDTextureFormat` (set `width`, `height`, `format`, `usage_bits`) and an `RDTextureView`.
   - Bind the state: one `RDUniform` per binding (`uniform.uniform_type = RenderingDevice.UNIFORM_TYPE_STORAGE_BUFFER` for buffers, `RenderingDevice.UNIFORM_TYPE_IMAGE` for storage images, `RenderingDevice.UNIFORM_TYPE_SAMPLER_WITH_TEXTURE` for sampled textures with a sampler created by `rd.sampler_create`), `uniform.binding` matching the shader, `uniform.add_id(rid)`, then `rd.uniform_set_create([uniforms], shader, 0)` where the last argument matches the shader's `set`.
   - Create the pipeline once: `var pipeline := rd.compute_pipeline_create(shader)`.
   - Dispatch per substep: `var compute_list := rd.compute_list_begin()`, `rd.compute_list_bind_compute_pipeline(compute_list, pipeline)`, `rd.compute_list_bind_uniform_set(compute_list, uniform_set, 0)`, `rd.compute_list_dispatch(compute_list, groups_x, groups_y, 1)` with group counts rounded up (`ceil(nx / local_size_x)`), `rd.compute_list_end()`. Insert `rd.compute_list_add_barrier(compute_list)` between dependent dispatches recorded in the same list, so a later pass reads finished writes from the earlier one.
   - Submit and synchronize: `rd.submit()`, then `rd.sync()` only when the CPU actually needs the result. The tutorial's guidance is explicit: do not synchronize right away, since it stalls the CPU waiting for the GPU; wait at least 2 or 3 frames before synchronizing so the GPU runs in parallel with the CPU. Read results back with `rd.buffer_get_data(buffer)` or `rd.texture_get_data(texture, 0)` only for validation and debugging, never per frame in the shipping path.
   - Free what you create: RIDs are not freed automatically. Call `rd.free_rid(rid)` for buffers, pipelines, and uniform sets when they are replaced or the sim is torn down.
5. Keep the GLSL scheme identical to the CPU prototype, line for line in behavior: same staggering, same reconstruction, same clamps, same boundary rules, same substep count. The port is a translation, not a redesign. Where GLSL and GDScript differ (integer division, float precision, indexing), the CPU prototype is the reference.
6. Choose the device and texture-sharing path by what consumes the sim:
   - CPU readback path (local device): the sim runs on a local RenderingDevice, and the CPU reads heights back (deferred by 2 to 3 frames) to displace a mesh or drive gameplay. Simplest to debug, costs a readback. Local devices cannot be debugged with RenderDoc.
   - Direct sampling path (global device): the sim textures are created on the global RenderingDevice, and a `Texture2DRD` resource exposes each texture to material shaders: create the `Texture2DRD`, set its `texture_rd_rid` to the texture RID, and assign it to a `sampler2D` uniform in the water material. The texture's `usage_bits` must include `TEXTURE_USAGE_SAMPLING_BIT` and `TEXTURE_USAGE_STORAGE_BIT` (plus `TEXTURE_USAGE_CAN_COPY_FROM_BIT` if the CPU ever reads it). For history (previous-frame state), cycle texture RIDs between frames instead of copying data texture to texture, the pattern the godot-demo-projects compute texture demo uses. A texture created on a local device cannot be shared with the global device this way; if direct sampling is the goal, create the texture on the global device from the start.
7. C# path. Valkyrie is C#. The same RenderingDevice API is available from C# with PascalCase names; the mapping below is verified against a working Godot 4.4 .NET example, and must be rechecked against the 4.7 class reference at build time. The shader file, the GLSL, the bindings, and the dispatch logic are identical; only the host language changes.

   | GDScript | C# |
   |---|---|
   | `RenderingServer.create_local_rendering_device()` | `RenderingServer.CreateLocalRenderingDevice()` |
   | `RenderingServer.get_rendering_device()` | `RenderingServer.GetRenderingDevice()` |
   | `shader_file.get_spirv()` | `shaderFile.GetSpirV()` |
   | `rd.shader_create_from_spirv(spirv)` | `rd.ShaderCreateFromSpirV(spirv)` |
   | `rd.storage_buffer_create(size, data)` | `rd.StorageBufferCreate(size, data)` |
   | `rd.uniform_set_create(uniforms, shader, 0)` | `rd.UniformSetCreate(uniforms, shaderRid, 0)` |
   | `rd.compute_pipeline_create(shader)` | `rd.ComputePipelineCreate(shader)` |
   | `rd.compute_list_begin()` | `rd.ComputeListBegin()` |
   | `rd.compute_list_bind_compute_pipeline(list, pipeline)` | `rd.ComputeListBindComputePipeline(list, pipeline)` |
   | `rd.compute_list_bind_uniform_set(list, set, 0)` | `rd.ComputeListBindUniformSet(list, set, 0)` |
   | `rd.compute_list_dispatch(list, x, y, z)` | `rd.ComputeListDispatch(list, x, y, z)` |
   | `rd.compute_list_end()` | `rd.ComputeListEnd()` |
   | `rd.submit()` / `rd.sync()` | `rd.Submit()` / `rd.Sync()` |
   | `rd.buffer_get_data(buffer)` | `rd.BufferGetData(buffer)` |
   | `rd.free_rid(rid)` | `rd.FreeRid(rid)` |
   | `RDUniform`, `uniform_type`, `UNIFORM_TYPE_STORAGE_BUFFER` | `RDUniform`, `UniformType.StorageBuffer` |
   | `RDTextureFormat`, `format`, `width`, `height`, `usage_bits` | `RDTextureFormat`, `Format`, `Width`, `Height`, `UsageBits` |
   | `PackedFloat32Array.to_byte_array()` | `MemoryMarshal.AsBytes(floatSpan).ToArray()` |

   C# notes: uniform sets take a `Godot.Collections.Array` of `RDUniform`; float data reaches `StorageBufferCreate` as a byte array, built with `MemoryMarshal.AsBytes` over the float span. Async readback exists as `BufferGetDataAsync` with a callback; the forum example that exercises it reports stalls and crashes when misused, so prefer the deferred synchronous readback in step 4 until async readback is verified in your own project.

**Check**
- GPU vs CPU field diff: run the same scene, same grid, same `dt`, same substep count on both implementations, read the GPU `h` field back, and compare cell by cell. Differences must be at float-operation-order level (tiny, scattered), not structural (a region wrong, a boundary wrong). A structural diff means a porting bug: check face indexing first, then the reconstruction, then the barrier placement.
- Dispatch coverage: every cell is written exactly once per substep, including the last partial workgroup at the domain edges. The bounds guard must be present and the group counts must be the ceiling division.
- No per-frame sync stall: frame time with the sim running is close to frame time with the sim dispatched but never read back. If reading back every frame costs milliseconds, the sync discipline is wrong, not the sim.
- Long computations do not trip the Windows TDR (Timeout Detection and Recovery, typically 5 to 10 seconds of driver inactivity): a single dispatch must finish far inside that window; if a grid is ever that large, split it into multiple dispatches.

**Why**
The tutorial's order (device, shader, buffers, uniforms, pipeline, list, submit, deferred sync) is the API's contract; skipping or reordering steps is how "valid texture" and stale-data errors are born. Ping-ponging and barriers are the same rule stated twice: a dispatch must never read state another invocation in the same dispatch is writing. The CPU prototype exists precisely so the GPU port has a known-good answer; use it.

## Phase 6: Sim-tied mesh displacement

**Do**
1. Build the water surface as a grid mesh matching the sim domain: one vertex per sim cell (or per a fixed subdivision of it), positioned over the bed, with UVs mapping 1:1 to sim cells.
2. Displace in the vertex shader from the sim state, not from a second wave function. On the direct-sampling path, the material samples the height texture (via the Texture2DRD) at the vertex UV and offsets the vertex by the sampled surface height. On the readback path, update a vertex buffer from the deferred readback. Either way, the displaced height at a vertex is the sim's `eta` at that cell, and nothing else.
3. Compute normals from the height field, not from a normal map: sample the heights of the neighboring cells (in the vertex or fragment shader) and take finite differences. A normal derived from the same field that displaces the mesh cannot disagree with the silhouette.
4. Handle dry cells explicitly: where `h` is zero or below the dry threshold, the surface mesh must not render as water. Either discard those fragments (or collapse those vertices to the bed) so the mesh never bridges a dry gap with a water sheet, or fade the water material out by depth. The bed mesh underneath must exist and look right on its own, since dry bed is visible wherever the stream is shallow.

**Check**
- The displaced surface matches the sim field at sampled points: pick a cell, read its `eta` from the readback, and compare with the rendered vertex height. They must agree.
- With the camera still and the sim running, the water moves because the sim moves, and stops moving when the sim is paused. If it keeps moving with the sim paused, a time-based shader term is leaking in; remove it.
- Dry banks read as bed, not as a thin water film stretched over rock.

**Why**
Displacement is the first visual layer the camera reads, and it is the layer where a fake is most visible: a scrolling sine wave and a simulated wave look alike in a still frame and nothing alike in motion. Deriving displacement from the sim is what makes the water's motion coherent with its foam, its ripples, and its caustics, because all of them read the same state.

## Phase 7: Advected ripple coordinates

**Do**
1. Keep a second field alongside the sim state: ripple coordinates (a UV offset field), one value per cell, initialized to the cell's own UV.
2. Advect the ripple coordinates with the sim velocity field each substep, semi-Lagrangian style: the new coordinate at a cell is the old coordinate sampled at the backtraced position (cell center minus velocity times `dt`). This is the same advection used for velocity in Phase 2, applied to a passive field. It needs the same ping-pong discipline as the state: never read and write the same field in one dispatch.
3. In the water material, sample the detail ripple/normal texture with the advected coordinates instead of the static mesh UVs. Detail now flows downstream, converges where the flow converges, and stretches where the flow accelerates, because the coordinates themselves are carried by the velocity field.
4. Seed the ripple field with a static noise texture at startup so there is detail to advect; without seed detail, advection moves nothing visible.

**Check**
- Ripples move with the flow: downstream of a rock, the detail pattern streams in the flow direction; in a still pool, the pattern is nearly static. If the pattern drifts against the flow, the advection sign is flipped.
- At a convergence (a narrow gap, a weir lip), the pattern visibly concentrates. If it smears to uniform gray, the advection is over-diffusing; check the sampling filter (point sampling preserves the field; linear filtering diffuses it) and the substep count.
- Pausing the sim freezes the ripple motion. Same leak test as Phase 6.

**Why**
A static ripple texture scrolled by time reads as wallpaper; a texture advected by the velocity field reads as water, because the detail and the displacement share one motion. This is the thread author's "ripple coordinates advected by the velocity field" layer, and it is cheap: one extra advected field, no new solver.

## Phase 8: Caustics pass

**Do**
1. Render caustics as a read-only layer projected into the pool: in the bed/water fragment shader, compute a caustic pattern from the sim's surface state (surface curvature or height variation sampled from the height/normal field) and add it as light on the bed beneath the water surface, masked by water depth so it appears only where water covers the bed.
2. Drive the pattern's motion and intensity from the sim field, not from a looping time uniform. The pattern should sharpen and brighten where the surface converges (wave crests focusing light) and soften where the surface is flat. A static caustic texture scrolled by time is the fake version; a pattern derived from the live height field is the sim-tied version.
3. Keep the caustics pass after displacement and ripples in the build order, and keep it visually subordinate: it is light play on the bed, not a second water surface. If it competes with the surface for attention, reduce its intensity before changing its motion.

**Check**
- Caustics move when the sim moves and freeze when the sim pauses. Same leak test as Phases 6 and 7.
- Caustics are absent over dry bed and faint in deep flat water, strongest in shallow moving water. If they appear uniformly everywhere, the depth mask is missing.
- The pattern never suggests a wave the displacement does not show: sample the same height field the displacement uses, at the same resolution.

**Why**
Caustics are the layer that sells shallow clear water, and they are also the easiest layer to fake badly, because a looping caustic texture looks right in a screenshot and wrong in motion the moment the water's actual motion disagrees with it. Deriving the pattern from the sim field keeps the light and the water in one story.

## Phase 9: Foam last

**Do**
1. Build foam as a read-only field, generated from sim state, never fed back into the sim. Foam appears where the sim says the water is doing something violent: shallow depth over a bed step, high speed, strong convergence, or impact against an obstacle. The SCA 2010 lineage supports this directly: the 2007 Thurey papers (as reported in the audit) treat bubbles and foam within a shallow-water framework, as a layer on the model, not a change to it.
2. Advect the foam field with the velocity field (same semi-Lagrangian advection as Phase 7), with a lifetime: foam is born at generation sites, rides downstream, and fades over a fixed lifetime. Fade by age, not by distance, so slow water keeps foam longer than fast water, which is the visible behavior.
3. Render foam as a masked overlay on the water surface: a noise texture broken up by the foam field value, brighter and more broken where the field is high, absent where it is zero. Keep the foam texture static; all motion comes from the advected field.
4. Add interaction sources the same way: a rock, a weir lip, or a character wading injects foam (and a height disturbance) at the cells it touches, through the same generation rule, as an external input to the sim. Keep "adding water" separate from "disturbing it": a spring adds volume at an inflow cell; a wading character mainly redistributes water already there plus foam at the contact.

**Check**
- Foam appears at the weir lip and the rock impact, advects downstream, and fades. No foam on still deep water, no foam on dry bed.
- Foam motion matches the flow direction everywhere. If foam drifts sideways across the current, its advection is reading the wrong field or the wrong sign.
- Adding foam never changes the sim: run the same scene with foam generation on and off and diff the `h` fields. They must be identical.

**Why**
Foam is last because it only reads the sim, in the thread author's own build order: "foam and caustics come last since they just read from the sim." Building foam first means tuning an effect against a sim that does not exist yet, and re-tuning it every time the scheme changes. Building it last means it inherits a finished, verified motion for free.

## Phase 10: Validation

**Do**
1. Run the full test battery, in this order, recording a pass or fail and the measured number for each:
   - Lake at rest, flat bed: exact stillness, 1,000 steps.
   - Lake at rest, raised bed: exact stillness, 1,000 steps (the well-balanced gate).
   - Closed-pool volume conservation: total volume drift under 0.1 percent over 10,000 steps (this skill's own threshold, not a paper number).
   - Dam break: a wall of water released into a dry or shallow domain advances as a front, no NaN, no negative depths, front speed plausible against `sqrt(g * h)`.
   - Dry-bed wetting: water climbing a dry slope wets cells only when the surface exceeds their bed, with no phantom velocity ahead of the front.
   - Obstacle flow: water diverted around a rock or pier, with a wake downstream and no water inside the obstacle footprint.
   - Violent input: the largest disturbance the game will produce, at the deepest water and steepest bed, survives without NaN or blowup at the chosen substep count.
   - Soak: the stream scene runs 10 minutes unattended. Total volume and mean surface height are logged every 30 seconds; drift or slow gain over the soak is a fail, even if no single frame looks wrong.
   - Frame time: full pipeline (sim dispatches plus all visual layers) measured at the shipping grid size on the lowest target hardware class, with the sim on and the sim off, so the sim's cost is isolated.
2. Fix failures in scheme order, not symptom order: a NaN is fixed in the clamps or the substep count, not by damping the render; a drifting lake is fixed in the reconstruction, not by re-leveling the surface every frame.
3. Re-run the battery after any change to the grid size, cell size, max depth, bed shape, or substep count. The stability tuning is a property of the scene; changing the scene re-opens it.

**Check**
- Every test has a recorded pass criterion written before it runs, and a measured number after. A test without a number is an impression, not a validation.
- The GPU implementation passes the same battery as the CPU prototype, with the field diff from Phase 5 as the bridge between them.
- The soak log is flat. Slow volume gain is the failure mode that ships, because it looks fine for the first minute.

**Why**
Water sims fail in two ways: suddenly (NaN, blowup, visible on the first violent input) or slowly (drift, gain, visible only after minutes). The battery catches both, and the scheme-order fix rule keeps a rendering workaround from masking a solver bug that will return in a different scene.

## The human method, distilled

1. **CPU first, GPU second.** Get the scheme working where you can inspect it, then port it where it runs fast. The port is a translation with a reference answer, not a second invention.
2. **One sim, every layer reads it.** Displacement, ripples, caustics, foam: all derived from the same live state. A layer that moves on its own timer is a fake, and fakes disagree with each other in motion.
3. **Still water over an uneven bed is the first test.** If the scheme cannot hold a lake at rest, nothing downstream is trustworthy. The test is cheap, exact, and decisive.
4. **Compare the right quantity.** Surface height drives flow, not depth. Actual parameters, not borrowed constants: the substep count is measured for your scene.
5. **Stability is tuned, not assumed.** Substeps, clamps, and the Courant scaling are the tuning knobs, and the violent test plus the soak are how you know the tuning holds.
6. **Foam and caustics last.** They only read the sim. Build the thing they read first.
7. **Old techniques, honestly labeled.** The method is 2007 to 2011 literature, and the thread author says so himself. The new part is the packaging: an open, real-time implementation where every layer reads one live sim. Judge it as an implementation, not as research.

## Failure modes

- **Still water waves over a slope.** The source term is not balanced. Fix: hydrostatic reconstruction (Phase 3). Do not fix it by flattening the bed or damping the surface.
- **NaN or blowup after a big splash.** The stability limit is exceeded. Fix: more substeps, smaller `dt`, or the Phase 4 clamps. Check the violent test, not the calm scene.
- **Negative depths.** The `h >= 0` clamp is missing or applied after the height update reads the negative value. Fix: clamp every substep, before the next pass reads the field.
- **Water leaking through a wall or uphill into a dry cell.** The reflective-face / dry-face rule is missing. Fix: the Phase 2 boundary condition, including the epsilon dry-face test.
- **Waves reflecting off open borders.** No absorbing region, or the damping region is too narrow or too weak. Fix: the 10-cell damping band with the coefficient rising toward the border.
- **GPU result differs structurally from CPU.** A porting bug. Fix order: face indexing, reconstruction, barrier placement, dispatch bounds. Diff the fields; do not stare at the render.
- **Black or default-color texture in the material.** The Texture2DRD is bound to a texture owned by a local RenderingDevice, which cannot be shared with the render thread. Fix: create the texture on the global device, or use the readback path.
- **Garbage or error from a storage image.** The shader image format and the `RDTextureFormat` format do not match exactly. Fix: `rgba32f` with `DATA_FORMAT_R32G32B32A32_SFLOAT`, `r32f` with `DATA_FORMAT_R32_SFLOAT`, no exceptions.
- **Frame-time stall every frame.** `sync()` is called immediately after every dispatch. Fix: defer synchronization 2 to 3 frames; read back only for validation.
- **Overshoot ripples where waves shoal onto a shelf.** The edge-reduction fix is missing. Fix: the Phase 4 overshoot reduction at sharp surface jumps.
- **Sim textures blur or smear.** The sim textures are mipmapped or linearly filtered where the field must be read exactly. Fix: no mipmaps on sim textures, point sampling for state reads.
- **Nothing renders, or the project errors on startup.** The project is on the Compatibility renderer or running headless. Fix: Forward+ or Mobile; RenderingDevice is unavailable otherwise.
- **Foam changes the water.** Foam is feeding back into the sim. Fix: foam is read-only by construction; the diff test in Phase 9 proves it.

## AAA studio practice

**Do**
1. Ship the architecture the shipped titles use: a 2D shallow-water grid projected on the ground heightfield, simulated only where it matters, with the frame-time cost as the buying criterion. Fluid Flux (Unreal Engine plugin, used on Senua's Saga: Hellblade II) is the documented instance: its simulation runs on a 2D grid projected on the captured ground heightfield, with fixed axis-aligned simulation areas, a cheap ripple solver that moves with the character, advected foam and caustics, and an async readback system for sampling height and flow. The Godot equivalent of that architecture is this skill: the sim grid projected on the Pellune bed, the sim-tied layers, and deferred readback instead of per-frame sync. (As documented in the sibling skill `simulation-vfx/fluid-forge-ue-water-sim`, from the Fluid Flux forum thread: https://forums.unrealengine.com/t/imaginaryblend-fluid-flux/2420009 .)
2. Treat the player-following sim area as the scaling answer, the way Crimson Desert's water does: simulate the water near the player at full fidelity and preplace or simplify the rest, rather than simulating the whole island at one resolution. The trade (area size vs GPU cost) governs both, and it is decided by the Phase 10 frame-time measurement, not by ambition.
3. Keep the explicit, fixed-cost step structure the SCA 2010 examples use: every substep costs the same grid update, every clamp is applied in every substep, and there is no data-dependent solver iteration whose cost varies per frame. Fixed cost is what makes a real-time water budget plannable.
4. Automate the frame-budget guard: log milliseconds per frame for the sim dispatches and for each visual layer separately, at the shipping grid size, on the lowest target hardware class. If the budget breaks, shrink the grid or the sim area before weakening the clamps or the substep count, since a smaller stable sim beats a larger exploding one.

**Check**
- The sim runs only over its authored domain, not the whole world, and the domain size is a recorded budget decision.
- Per-stage timings exist for sim, displacement, ripples, caustics, and foam, and the sim's share is isolated by the on/off measurement in Phase 10.
- The clamps and substep count are the same in the shipped build as in the validated build; a tuning change re-opens the Phase 10 battery.

**Why**
Real-time water in shipped games is a budget discipline, not a solver showcase: a fixed-cost explicit scheme on a bounded grid, visual layers that read the sim instead of re-solving it, and a measured frame time that decides the grid size. The literature gives the scheme; the shipped titles give the shape of the product around it.

## Agent automation

1. **Sim manifest.** Keep `water-sim-manifest.json` per water body: grid size, `dx`, `dt`, substep count, gravity, clamp constants, bed source, device path (local or global), texture formats, and the Phase 10 frame times. A change to any tuning field without a re-run of the battery is a manifest violation; log it.
2. **CPU/GPU field-diff gate.** After every port change, run the same scene on both implementations, read the GPU field back, and fail the change when any cell differs by more than float-operation-order tolerance, or when any region differs structurally. Record the max diff in the manifest.
3. **Lake-at-rest gate.** The raised-bed lake test runs automatically on every scheme change and must pass exactly (surface drift zero to float tolerance over 1,000 steps). A scheme change that breaks it does not proceed to the GPU port.
4. **Soak log.** The 10-minute soak runs unattended and appends volume and mean-height samples to a log; a drift beyond the Phase 10 threshold fails the run and names the sample where the drift began.
5. **Dispatch audit.** Assert the dispatch group counts are the ceiling division of the grid by the workgroup size, the bounds guard is present in the shader, and a barrier sits between dependent passes in the same compute list. Log a failure for any dispatch that can write outside the domain.
6. **Readback audit.** Assert no per-frame `buffer_get_data` or `texture_get_data` call exists on the shipping path; readback appears only behind a debug flag or a deferred validation timer.

## Valkyrie note

This skill targets Valkyrie's streams and pools on Pellune: Godot 4.7.2 with C#, a fixed iso camera, an authored island (1,298 m square, summit 80 m). Three Valkyrie-specific consequences:

- The water is judged from one fixed camera angle, and the sim-tied layers pattern is what that camera rewards: displacement, ripples, caustics, and foam all reading one live sim stay coherent from the one angle that matters, where four independent fakes would visibly disagree.
- The C# compute path is covered by the Phase 5 mapping table, not by GDScript-only code. Recheck every RenderingDevice name against the Godot 4.7 class reference at build time, since the grounding pages read for this skill were the 4.2, 4.3, 4.4, and stable docs.
- No performance figure from the thread transfers. The demo's grid size, frame rate, and hardware were unstated and unverified, and the phone reports in the thread are two anecdotes, not compatibility evidence; neither appears anywhere in this skill as a number or a claim. Size the Pellune grids by the Phase 10 measurement on target hardware, starting small (one stream reach, one pool) and growing the domain only while the frame budget holds.
- The sim still needs real CPU-side answers for gameplay: a wading citizen, a dammed flow, or a fished pool needs the water height and velocity at a point, which comes from the deferred readback, not from the GPU textures. Keep the readback path working even when the render path uses direct sampling, and sample it at gameplay frequency, not render frequency.

## Depth status

PARTIAL. The Godot compute-shader grounding was verified firsthand in the official docs (compute tutorial on the 4.2 and stable pages, RenderingDevice class reference 4.4, RDTextureFormat class reference 4.3) and the texture-sharing pattern in the nekotoarts article and the Texture2DRD forum and demo-projects records. The SCA 2010 solver sections (equations, staggered grid, height and velocity integration, boundary conditions, stability clamps, overshoot reduction) and the Audusse et al. 2004 well-balanced construction were read firsthand from the papers. The Thurey 2007 papers and the tall-cells boundary are as reported in the thread audit, not read firsthand for this skill. The thread's demo was not visited or tested, and nothing in this skill was run hands-on in Godot: no CPU prototype was executed, no compute shader was dispatched, and no frame time was measured. The C# mapping is an API-name mapping from a working example post, not run code. No performance number in this skill is a measurement.
