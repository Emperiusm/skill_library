---
name: sdf-collision-custom-terrain
description: "Bake a signed distance field for custom terrain with overhangs and caves, and collide spheres, capsules, ropes, and particles against it in Godot 4 with no physics-server SDF shape: Blender BVHTree baking, trilinear CPU sampling, gradient push-out, sphere-cast CCD, and a two-tier near/far field. Trigger when heightmap collision cannot represent the terrain because it has overhangs, caves, or undercuts."
---

# SDF collision for custom terrain in Godot

## Purpose

This skill reconstructs the signed distance field (SDF) collision workflow end to end, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: bake the terrain once into a 3D grid of signed distances, then answer every collision question with grid lookups, because one sample costs the same whether the terrain is a flat plane or a cave full of passages. Godot has no SDF shape in its physics server, so the field lives beside the physics server, not inside it: the physics server keeps handling everything else, and a small custom solver resolves SDF bodies against the field.

## Source

Creator: moonmilkgames (game: Cave Expedition, a Unity caving game built on a custom renderer). Three Instagram reels, all read firsthand with full local transcriptions and 12 frames each:

- https://www.instagram.com/reel/DfIH6FXjFU6/ (Oct 30, 2026, 32.9 s): "Cheaper collision for my caving game." Claims: testing collision against an SDF is "very cheap"; the SDF can represent any shape; sampling cost does not depend on shape complexity ("It's the same amount of sampling"); near the player he upscales collision quality "to an insane level" so it matches what is seen. No resolution, memory, timing, bake method, or code is stated.
- https://www.instagram.com/reel/DfKstl7ESfJ/ (Oct 31, 2026, 40.7 s): "Making my game's physics match its cave walls." Claims: storing volumetric information is "taxing on memory"; by analogy with his virtual texturing system he "needed a virtual SDF sort of thing"; high resolution collision only close to the player and where it matters. No implementation is shown, and the narration says he "needed" the virtual SDF, which reads as a plan, not a demonstrated build. "Precision Pit" is a labeled place on the cave map in the reel, not a confirmed system name. Do not cite it as one.
- https://www.instagram.com/reel/DfFjG3rDhjB/ (Oct 29, 2026, 25.9 s): ropes are strings of small spheres colliding against the SDF; the rope asset's own SDF generator and collider were incompatible with his terrain, so he integrated his own SDF solution into the asset and got collision against the low-resolution SDF. The asset is identified as Obi only from documentation screenshots (menu path "Create -> Obi -> Obi Distance Field"), never spoken aloud. The screenshots carry the only hard numbers in all three reels, and they describe the documentation example, not his terrain: a distance field of 636 kilobytes with an effective resolution of 512^3, greater resolution near the surface, with Max Error and Max Depth adaptive subdivision parameters. Do not attribute 636 KB or 512^3 to Cave Expedition's terrain.

Comments: checked, zero gems. The three reels drew 3, 1, and 0 comments respectively, with no creator replies. One viewer asked whether the virtual SDF is "like a voxel collision with LODs" and got no answer; that interpretation is unconfirmed and is not used here. No comment quote is used in this skill.

Honesty boundary for the whole skill: the reels are concept-level. They prove the idea and the cost argument, not an implementation. Every construction step below (baking, sampling, resolving, paging) is this skill's refinement research, grounded in the Godot docs and the cited SDF literature, and labeled as such where it goes beyond the reels.

## SDF vs the Godot shapes you already have

Godot's physics server offers exactly nine shape types, and none of them is an SDF. The `Shape3D` class list (stable docs) is: BoxShape3D, CapsuleShape3D, ConcavePolygonShape3D, ConvexPolygonShape3D, CylinderShape3D, HeightMapShape3D, SeparationRayShape3D, SphereShape3D, WorldBoundaryShape3D. The `PhysicsServer3D.ShapeType` enum confirms the same set. So an SDF collider cannot be plugged into a `CollisionShape3D`; it must be sampled by custom code. The one built-in SDF collision consumer in Godot is `GPUParticlesCollisionSDF3D`, which only affects `GPUParticles3D` (see Phase 3).

Pick by the terrain, in this order:

- **HeightMapShape3D** when the terrain is a heightfield with no overhangs. It is a real physics-server shape, faster than a concave mesh, slower than primitives (Godot docs). It cannot model overhangs or caves, by construction: one height per (x, z). Holes are made by assigning very low values. If your terrain fits this description, stop here and use it. An SDF would cost memory and a parallel solver for nothing.
- **ConcavePolygonShape3D** (trimesh) when the terrain is a static mesh with overhangs and the triangle count is modest. It is the slowest shape type in the docs, and its cost grows with local triangle density, which is exactly the case SDFs beat.
- **Custom SDF sampling** when the terrain has overhangs, caves, arches, or undercuts AND one of these holds: many dynamic objects query the same static terrain (ropes, particles, projectiles, citizens), or the mesh is too dense for a concave shape, or collision must match fine surface detail the physics mesh cannot carry. That is the Cave Expedition case, and the only case this skill is for.

## Tools used

Blender 4.x with a Python bake script (`mathutils.bvhtree`: `FromObject`, `find_nearest`, `ray_cast`); Godot 4.4 (GDScript primary, C# transliteration flagged where given); `ImageTexture3D` and `GPUParticlesCollisionSDF3D` from the Godot docs for the GPU/particle routes.

## Phase 1: Decide, and write the decision down

**Do**
1. Answer three questions about the terrain, in writing, before baking anything: (a) Does any surface overhang another surface at the same (x, z)? (b) Does any enclosed or semi-enclosed void exist (cave, tunnel, arch)? (c) How many dynamic objects will query the terrain per physics tick, and are any of them fast enough to tunnel?
2. If (a) and (b) are both no, use HeightMapShape3D and close this skill. Record the decision and the reason in the project: "heightfield, no overhangs, SDF not justified."
3. If either is yes, define the field bounds: an axis-aligned box that covers every collidable surface, plus a margin of at least one cell on every side. Record the box min corner, the cell size, and the resolution per axis in a manifest (see Agent automation). The field is static: moving terrain needs a rebake, which Phase 6 prices explicitly.
4. Set the sign convention once and never vary it: **negative inside solid, positive outside, zero on the surface**. Every formula below assumes it.

**Check**
- A top-down plot of the terrain with the field box drawn shows the box covering all collidable geometry with margin. A heightfield-only terrain has a written no-SDF decision, not a baked field.
- The manifest exists before the bake starts. Baking without recorded bounds is how fields end up offset by one cell and silently wrong.

**Why**
- The bake is the most expensive step and the field is the least forgiving artifact: a wrong box, a flipped sign, or an unjustified field wastes the whole downstream effort. The creator's cost argument ("complexity for free") is only true after the field exists; building it is where the cost lives.

## Phase 2: Bake the field (Blender BVHTree route)

**Do**
1. Prepare the source mesh: one closed, manifold mesh (or a set of closed meshes combined). Open meshes break the sign test in step 3: a ray can exit through a hole and flip the parity count. Check watertightness first (Blender: Select All by Trait > Non Manifold in Edit Mode; zero non-manifold edges on the collision mesh, or fix them before baking).
2. Build a BVH tree from the evaluated mesh: `bvh = mathutils.bvhtree.BVHTree.FromObject(obj, depsgraph)` (docs: `FromObject`, `FromPolygons`, `FromBMesh` constructors are verified in the Blender Python API reference). Work in world space: apply the object's transform to the evaluated mesh, or transform each grid point into object space, and record which you did.
3. For each grid point `p`, compute the unsigned distance with `bvh.find_nearest(p)`, which returns the nearest surface point and its distance. Determine the sign with a ray parity loop: cast `bvh.ray_cast(p, direction)`; on a hit, advance the origin just past the hit point and cast again; count hits; odd means inside (negative), even means outside (positive). Use one primary direction (+X) and, if a cast lands exactly on an edge or returns an ambiguous result, repeat with a second direction and take the majority. Cap the loop (this skill's default: 32 crossings) and flag any point that hits the cap instead of guessing its sign.
4. Clamp the stored value to a band: `clamp(d, -max_dist, +max_dist)` where `max_dist` is this skill's default of 4 to 8 cells. Far-field exactness is worthless (nothing collides there) and the clamp keeps the float range meaningful near the surface, which is where the AGX reference notes sampled fields are accurate.
5. Write the grid as a flat `PackedFloat32Array` in the layout `index = x + res_x * (y + res_y * z)`, with a sidecar JSON recording bounds min, cell size, resolution per axis, sign convention, source mesh name and hash, and bake date. Export as a `.bin` plus `.json`, or as a Godot `.res` holding the array. Start at 64^3. Measure bake time before raising resolution: a Python BVH loop over millions of points is slow (minutes at 128^3 is normal), and the jump-flooding GPU route in AAA practice is the production answer, not the first bake.
6. Memory budget, this skill's arithmetic (float32, one value per cell): 64^3 = 1 MiB, 128^3 = 8 MiB, 256^3 = 64 MiB, 512^3 = 512 MiB. A full 512^3 float field is not a plan; it is the reason Phase 6 exists. The Obi documentation example (636 KB at an effective 512^3) achieves its size with adaptive octree subdivision, not a dense grid; do not compare dense-grid memory against it.

**Check**
- Probe test before any gameplay use: pick at least 20 points with known answers (5 deep inside, 5 clearly outside, 10 within one cell of the surface, including one inside a thin wall and one inside an overhang). Compare the sampled field value and sign against the mesh (ray_cast from the probe point). Fail the bake if any sign is wrong or any near-surface distance is off by more than half a cell.
- Render a slice: write one horizontal slice of the field as a grayscale image and look at it. The zero contour must trace the terrain outline. A shifted, mirrored, or sign-flipped field is visible in one glance and invisible in gameplay until something falls through the floor.

**Why**
- The bake is the only place the field's truth is established. A sampled field is an approximation everywhere except the surface band, so the probe test measures the approximation where it matters, and the slice render catches the offset/mirror/sign errors that numbers alone hide.

## Phase 3: Store the field and sample it (the query contract)

**Do**
1. Keep the `PackedFloat32Array` in memory as the query store, alongside the manifest (bounds, cell size, resolution). CPU queries read the array directly; do not route hot queries through `Image.get_pixel`, which allocates a `Color` per call.
2. Implement the sampler. Convert a world point to fractional grid coordinates, clamp to the grid, and trilinearly interpolate the 8 surrounding cells. In GDScript (primary verified path, API names from the Godot docs):

```gdscript
func sample_sdf(p: Vector3) -> float:
    var g: Vector3 = (p - bounds_min) / cell_size
    var x0: int = clampi(int(floor(g.x)), 0, res_x - 2)
    var y0: int = clampi(int(floor(g.y)), 0, res_y - 2)
    var z0: int = clampi(int(floor(g.z)), 0, res_z - 2)
    var fx: float = clampf(g.x - x0, 0.0, 1.0)
    var fy: float = clampf(g.y - y0, 0.0, 1.0)
    var fz: float = clampf(g.z - z0, 0.0, 1.0)
    var c000: float = _at(x0, y0, z0)
    var c100: float = _at(x0 + 1, y0, z0)
    var c010: float = _at(x0, y0 + 1, z0)
    var c110: float = _at(x0 + 1, y0 + 1, z0)
    var c001: float = _at(x0, y0, z0 + 1)
    var c101: float = _at(x0 + 1, y0, z0 + 1)
    var c011: float = _at(x0, y0 + 1, z0 + 1)
    var c111: float = _at(x0 + 1, y0 + 1, z0 + 1)
    var x00: float = lerpf(c000, c100, fx)
    var x10: float = lerpf(c010, c110, fx)
    var x01: float = lerpf(c001, c101, fx)
    var x11: float = lerpf(c011, c111, fx)
    var y0v: float = lerpf(x00, x10, fy)
    var y1v: float = lerpf(x01, x11, fy)
    return lerpf(y0v, y1v, fz)
```

   `_at(x, y, z)` returns `data[x + res_x * (y + res_y * z)]`. Points outside the box clamp to the edge values; treat a query outside the box as "no collision here" at the call site (return a large positive value), never as a field value, because edge clamping fabricates a wall at the box boundary.
3. Implement the gradient by central differences, one cell step `h = cell_size`, following Inigo Quilez's documented form (6 taps, division by `2h` dropped because the result is normalized):

```gdscript
func sdf_gradient(p: Vector3) -> Vector3:
    var h: float = cell_size
    return Vector3(
        sample_sdf(p + Vector3(h, 0, 0)) - sample_sdf(p - Vector3(h, 0, 0)),
        sample_sdf(p + Vector3(0, h, 0)) - sample_sdf(p - Vector3(0, h, 0)),
        sample_sdf(p + Vector3(0, 0, h)) - sample_sdf(p - Vector3(0, 0, h))
    ).normalized()
```

   The 4-tap tetrahedral variant (Quilez, same article) trades two taps for a slightly noisier normal; use it only if profiling shows the gradient dominating the query budget. Guard the normalize: if the gradient length is near zero (the point is equidistant to two surfaces, the medial axis), keep the last valid normal instead of normalizing noise.
4. Optional GPU/particle route, verified in the Godot docs: build an `ImageTexture3D` with `create(Image.FORMAT_RF, width, height, depth, false, slices)` where `slices` is one `Image` per Z layer, and hand it to `GPUParticlesCollisionSDF3D.texture` for GPU particle collision. Or bake directly in the editor: select the `GPUParticlesCollisionSDF3D` node and click Bake SDF; every visible `MeshInstance3D` within `size` is baked, at `resolution` 16^3 to 512^3. Limits, stated in the docs: baking is editor-only (no bake method in exported projects), pre-baked `Texture3D`s can be loaded in exports, the process material must use `COLLISION_RIGID` or `COLLISION_HIDE_ON_CONTACT`, and it affects `GPUParticles3D` only. The `thickness` property exists to stop tunneling at speed. Do not assume the baked texture's distance encoding matches your own bake: probe it with a known sphere before trusting its values for CPU queries (see the Check in Phase 2).

**Check**
- Unit test on an analytic field: build a tiny field from a sphere SDF (`length(p - center) - radius`, exact math, no bake) and assert the sampler returns the analytic distance within half a cell and the gradient points radially outward within a small angle tolerance, at 50 random points. If the sampler fails on exact data, the trilinear code is wrong, not the bake.
- The gradient at a flat-wall probe points along the wall normal. A gradient pointing along the wall means the axis mapping (x/y/z vs res order) is transposed; fix the layout, not the data.

**Why**
- The query contract is the whole technique: sign says which side, magnitude says how far, gradient says which way out. Everything in Phases 4 to 7 is arithmetic on these three answers, and the cost of one query is the cost of one trilinear sample, constant regardless of how complex the terrain is. That is the creator's "same amount of sampling" claim, made executable, and it is also its limit: the constant is per sample, and a query that needs many samples (gradient, capsule, CCD) pays many constants.

## Phase 4: Resolve spheres and capsules against the field

**Do**
1. Sphere resolve (the primitive everything else is built from). For a sphere with center `c` and radius `r`: sample `d = sample_sdf(c)`. The sphere penetrates when `d < r`. Push-out: `c += normal * (r - d)` where `normal = sdf_gradient(c)`. Apply a small safety margin, this skill's default 0.02 cells: treat penetration as `d < r + margin` so the solver does not jitter on interpolated noise near the surface (the safety-margin practice is documented in the tektite SDF collision reference for sampled fields). Kill the inward velocity component on contact (slide), or reflect it scaled by a bounce factor for particles (the particle response in the tektite SDF physics reference).
2. Capsule resolve: sample at points along the capsule segment, spaced at most one radius apart with a minimum of 3 samples, and take the deepest penetration. Push the whole capsule out along that sample's gradient. This is an approximation (it can miss an edge that threads between samples); the sample spacing rule bounds the miss to less than the radius. Label it as such; a capsule that must never clip a thin edge needs the sphere-cast in Phase 5 instead.
3. Run the resolve inside `_physics_process`, after integrating velocity and before rendering the frame, on objects that are NOT physics-server bodies for terrain contact. A `CharacterBody3D` keeps its physics-server collision for everything else (props, characters) and adds the SDF resolve as a second pass for terrain only. A `RigidBody3D` cannot take an SDF shape, so do not try: SDF-resolved objects are kinematic/custom-integrated by design. Record this split in the object: "terrain contact: SDF; everything else: physics server."
4. Iterate the resolve 2 to 3 times per tick for stacked contacts (sphere resting in a corner needs more than one push-out to settle). Cap iterations and record the cap; an object that never settles is a field-resolution problem, not an iteration problem.

**Check**
- Drop test: a sphere dropped onto a flat field region rests with its center exactly one radius above the zero surface, within the safety margin, and does not sink or jitter over 600 ticks. Roll test: the same sphere rolls down a slope without catching on cell boundaries; catching means the gradient is noisy, which means the field is too coarse or the margin is zero.
- Corner test: a sphere pushed into a 90-degree inside corner settles at the corner, not through either wall. Tunneling through a corner is the capsule/edge sampling gap in step 2, not a sign error.

**Why**
- The SDF answers the only two questions a resolver needs (how deep, which way), so the resolver is ten lines. The work is in the sampling and the margins, not in the solver. Keeping the physics server for everything else avoids rebuilding collision layers, groups, and broadphase behavior that already work.

## Phase 5: Sphere-cast CCD for fast movers

**Do**
1. For any object whose per-tick displacement exceeds the thinnest wall it can meet, replace the discrete sphere test with a sphere cast (the tektite reference's CCD construction): march from the start position along the motion direction, stepping by `sample_sdf(p) - radius` each iteration. The step guarantee holds only while the field never overestimates distance; for a sampled field, keep a conservative epsilon and cap the steps (this skill's defaults: epsilon 0.001 cells, cap 64 steps), and fall back to the discrete test when the cast reports no hit.
2. On a hit at distance `t`, stop the object at `t / displacement` of its motion (first contact), then resolve the remaining motion as a slide along the surface. On an origin that starts the tick already penetrating (negative field value at the start point), treat it as an overlap to resolve per Phase 4, not as a fresh collision event.
3. In GDScript, the loop mirrors the reference exactly:

```gdscript
func sphere_cast(origin: Vector3, direction: Vector3, max_dist: float, radius: float) -> float:
    var t: float = 0.0
    for i in range(64):
        var d: float = sample_sdf(origin + direction * t) - radius
        if d < 0.001:
            return t
        t += d
        if t > max_dist:
            break
    return -1.0
```

**Check**
- Bullet test: a sphere of radius 0.25 moving 50 units in one tick toward a 0.1-unit wall stops at the wall instead of appearing on the far side. A discrete-only build fails this test by construction; that failure is the reason this phase exists.
- The step count stays bounded on open ground: a cast into empty space must exit via the `max_dist` break, not the step cap, or the epsilon is too small.

**Why**
- Discrete tests sample instants; fast motion lives between instants. The SDF's distance value is a safe step size by definition, which turns CCD from a sweep-volume problem into a loop. The sampled-field overshoot caveat is real, which is why the epsilon, the cap, and the discrete fallback are part of the phase, not optional extras.

## Phase 6: Two-tier field, the "virtual SDF" (only when one field cannot fit)

**Do**
1. Do not build this phase unless Phase 2's memory table forces it: a single field at the resolution the near-player detail needs does not fit the budget. The creator's "virtual SDF" is a stated need and an analogy to virtual texturing, not a demonstrated build; this phase is this skill's design from that analogy, plus the Obi adaptive-field precedent (Max Error / Max Depth subdivision, finer near the surface).
2. Two fields, one rule: a coarse field covering the whole terrain (this skill's default: 1 to 2 m cells) and a fine field covering a box around the player (this skill's default: 0.25 m cells, 32 m box). Query the fine field inside its box, the coarse field outside it. At the box boundary, blend over a 2-cell overlap band by taking the minimum of the two sampled distances (min is the correct union for SDFs) so objects crossing the boundary do not pop.
3. Page the fine field: when the player moves, the fine box follows in whole-cell steps (never fractional steps, which would resample the whole field every frame), and only the newly entered slabs are rebaked. Rebake cost is a budget line in the manifest, measured, not assumed. If the terrain is static, prebake fine-field tiles for the whole map offline and stream them from disk instead of baking at runtime; runtime baking exists only for edited terrain.
4. Keep one manifest per tier with its own bounds, cell size, and bake date, and one query function that hides the tier choice. Callers never pick a tier.

**Check**
- Boundary walk test: a sphere walks across the fine-box boundary in both directions with no pop, sink, or jitter. A pop means the overlap blend is missing or the fine box moved by a fractional cell.
- Memory check: coarse plus fine resident memory stays under the budget from Phase 2 with the player anywhere on the map. A fine box that grows with the map is a coarse field with extra steps.

**Why**
- Volumetric data is the most expensive data there is, and the creator's own framing says so ("taxing on memory"). The only affordable answer is to spend resolution where contact happens and nowhere else, and to make the tier boundary invisible. If the whole map fits in one field at the needed resolution, this phase is pure overhead: skip it.

## Phase 7: Ropes and particles as sphere chains

**Do**
1. Model a rope as a chain of spheres (the reel's representation: "a string of many small little spheres"), each sphere resolved against the field per Phase 4, with distance constraints between neighbors solved after the collision pass. No rope-mesh collider is needed; the spheres are the collision shape, exactly as the creator's integration does with Obi's solver.
2. For particles (`GPUParticles3D`), prefer the built-in route first: `GPUParticlesCollisionSDF3D` with an editor-baked texture (Phase 3, step 4). For `CPUParticles3D` or custom particle code, resolve each particle as a Phase 4 sphere with radius zero (a point query) plus the velocity reflect/slide response, batched: one sample per particle per tick, no gradient unless the particle penetrated.
3. Keep rope spheres small relative to the cell size (this skill's rule: sphere diameter no larger than one cell, ideally half a cell). A rope sphere wider than a cell can straddle a thin wall and sample open space on both sides while intersecting the wall between samples.

**Check**
- Rope drape test: a rope dropped over a rock edge hangs against the edge, each sphere resting on the field surface, with no sphere sunk into the rock and no sphere floating a cell above it. A floating rope means the margin is too large or the field is coarser than the rope.
- The rope count and sphere count are recorded with the tick cost. Cost scales with sphere count, not rope complexity, which is the same per-sample argument as the terrain.

**Why**
- Sphere chains turn the hardest collision pair (deformable rope vs arbitrary terrain) into the cheapest query in the system. That is the reel's actual contribution beyond the terrain case: the field is queried by the simplest possible shapes, so the solver stays simple while the terrain stays complex.

## The human method, distilled

1. **Decide before baking.** Heightfield, concave mesh, or SDF is a terrain-shape decision, and the wrong one wastes the bake.
2. **The bake is the truth.** Probe it, slice it, and look at it before any gameplay code trusts it.
3. **Sign, magnitude, gradient.** Every query is one of these three answers; if a resolver needs a fourth, the resolver is wrong.
4. **Samples are the budget.** Count samples per tick (sphere 1, gradient 6, capsule N, cast up to 64), not objects, because samples are what the field charges for.
5. **Resolution follows contact.** Spend cells where bodies touch the terrain and nowhere else; the virtual-SDF tiering is a budget tool, not a feature.
6. **Keep the physics server.** The SDF is a second opinion on terrain contact, not a replacement physics engine.

## Failure modes

- **Thin features vanish.** A wall thinner than one cell may not appear in any sample. Fix: raise resolution locally (Phase 6 fine tier), or add a primitive collider for that wall, and record it as an exception. Never silently trust a field whose cell size exceeds the thinnest collidable feature; the thin-feature gate in Agent automation exists for this.
- **Gradient noise on the medial axis.** Where two surfaces are equidistant, the gradient is undefined and central differences return noise. Fix: keep the last valid normal, and never normalize a near-zero gradient.
- **Tunneling at speed.** Discrete sphere tests miss thin walls. Fix: Phase 5 sphere-cast CCD, or the `thickness` property on the particle route. A fast object with no CCD is a known hole, not a bug to chase later.
- **Field/visual mismatch.** Collision resolves against a coarser field than the rendered mesh, so bodies float or sink relative to what is seen. Fix: the parity probe gate (Phase 2) plus a render-vs-collision log, modeled on the parity gate in the `godot-terrain3d-heightmap` skill. The creator's "matches exactly what you see" is a resolution claim; verify it, do not assume it.
- **Sign flip from open meshes.** The parity loop counts crossings; a hole in the mesh flips the count past the hole. Fix: closed meshes only, watertight check in Phase 2, and the cap-flag rule for ambiguous points.
- **Box-boundary walls.** Clamped edge samples fabricate a wall at the field box edge. Fix: margin in Phase 1, and "outside the box means no collision" at the call site.
- **Memory blowup.** A dense 512^3 float field is 512 MiB. Fix: the Phase 2 table, the Phase 6 tiers, or an adaptive (octree-style) field like Obi's, which is a separate implementation, not a flag.
- **Physics-server bypass confusion.** SDF-resolved objects do not collide with physics-server bodies through the server, and layers/groups do not apply to field queries. Fix: the split recorded in Phase 4, step 3, enforced in code review: every SDF-resolved object documents which system handles each contact pair.
- **Stale fields after edits.** Editing the terrain without rebaking leaves collision describing the old terrain. Fix: the manifest's source-mesh hash gate; a changed hash fails the build until a rebake runs.
- **The "virtual SDF" is a plan, not a demo.** The creator's reel states the need and the analogy; no paging mechanism, page size, or streaming result is shown. Phase 6 is this skill's design, labeled as such. Do not cite the reel as proof the paging works.

## AAA studio practice

- **AGX Dynamics, SDF collision tutorial.** Production SDF collision in a commercial physics SDK: fields built once from closed triangle meshes into grids, distance queries answered in constant time however complex the mesh, accurate in a narrow band around the surface and coarser further away, with SDF-vs-primitive and SDF-vs-SDF pairs, demonstrated on tight non-convex contacts (hanging chains, a nut turning down a bolt). The narrow-band accuracy note is the reason for this skill's clamp band and safety margin. Source: https://www.algoryx.se/documentation/complete/agx/html/data/python/tutorials/tutorial_signedDistanceField.agxPy
- **Obi (Virtual Method), adaptive distance fields.** The rope asset's own SDF format, shown in the reel's documentation screenshots: adaptive subdivision controlled by Max Error (subdivide while the stored distance error exceeds tolerance) and Max Depth (cap on subdivisions), greater resolution near the surface, with the docs example at 636 KB for an effective 512^3 field. This is the verified precedent for Phase 6's adaptive idea, and the reason dense grids are not the only storage shape. The figures are the documentation example's, not Cave Expedition's. Source: identified from the reel's frames; the asset's documentation as shown on screen.
- **Tektite Tutorials, SDF collision detection and SDF physics.** The query contract this skill is built on, read firsthand: containment as a sign check, penetration depth plus separation direction as magnitude plus gradient, sphere casting for CCD with the safe-step guarantee and its sampled-field overshoot caveat, the vertex/edge sampling gap for non-convex penetration, and the performance profile (one fixed query-heavy shape against many cheap dynamic shapes; precompute once at build time; two dense dynamic meshes stay cheaper mesh-vs-mesh). Sources: https://tutorials.tektite.studio/signed-distance-fields/sdf-collision-detection/ and https://tutorials.tektite.studio/signed-distance-fields/sdf-physics-and-particle-systems/
- **Tan et al., RTSDF (arXiv 2210.04449).** Jump flooding (Rong and Tan, 2006) over a voxelized scene to generate approximate SDFs on the GPU in real time, stored as a 3D texture, refined with ray tracing near surfaces because the raw jump-flooded field reads blocky. This is the production bake route when the Blender Python bake in Phase 2 is too slow: voxelize, flood, refine near the surface. Source: https://arxiv.org/pdf/2210.04449
- **Inigo Quilez, normals for SDFs.** Central differences (6 taps) and the tetrahedral technique (4 taps) for estimating the gradient, with the division by 2h dropped before normalization. The gradient code in Phase 3 follows this article directly. Source: https://iquilezles.org/articles/normalsSDF/
- **Godot's own particle SDF.** `GPUParticlesCollisionSDF3D` is the engine's shipped proof that baked SDF collision is the right shape for the many-queries-one-static-field workload: editor baking over visible meshes, resolutions 16^3 to 512^3, a thickness property against tunneling. Its limits (particles only, editor-only baking) are the reason the custom CPU path in this skill exists at all. Source: https://docs.godotengine.org/en/4.4/classes/class_gpuparticlescollisionsdf3d.html

## Agent automation

- **SDF manifest.** Keep `sdf-manifest.json` per field tier: bounds min, cell size, resolution per axis, sign convention, clamp band, source mesh name and hash, bake date, bake tool and version. A bake script regenerates the field from the manifest and fails if the source hash changed without a rebake, if the manifest is missing any field, or if the stored array length disagrees with the resolution product.
- **Memory budget gate.** Compute resident bytes from the manifest (cells times 4) and fail the build when a tier exceeds its budget (this skill's defaults: 64 MiB for the coarse field, 16 MiB for one fine tile). Thresholds are this skill's own, not studio numbers.
- **Parity probe gate.** On every bake, run the Phase 2 probe set (inside, outside, near-surface, thin wall, overhang) and fail the bake on any wrong sign or any near-surface error beyond half a cell.
- **Thin-feature gate.** Measure the thinnest collidable wall in the source mesh (narrowest cross-section) and fail the bake when the cell size exceeds half of it, unless that wall is recorded as a primitive-collider exception.
- **Gradient-degeneracy log.** During a playtest capture, log every query whose gradient length falls below 0.1 after normalization input (near-zero gradient); a cluster of them at one location marks a medial-axis trap that needs a hand-placed normal or a resolution bump.
- **Tier-boundary check.** At each fine-box move, sample the overlap band and fail the frame if the two tiers disagree by more than one cell anywhere in the band; disagreement means the fine tile is stale.
- **Rebake trigger.** Any edit to the source mesh, the bounds, or the cell size marks the manifest dirty; the next build rebakes before any test runs. Never test gameplay against a dirty manifest.

## Valkyrie note

Be honest about the fit, because the honest answer is mostly no. Pellune's terrain is a Terrain3D heightmap: an authored heightfield with no overhangs, caves, or undercuts in the current spec. HeightMapShape3D (or Terrain3D's own collision) already covers that terrain inside the physics server, with no bake, no parallel solver, and no memory table. Building SDF collision for Pellune as specified would spend the bake, the memory, and the solver split for capability the map does not use. Do not build it for the island as it stands.

The skill earns its keep in exactly two future cases. First, if Pellune grows caves, arches, sea cliffs with undercuts, or any structure where one (x, z) needs two surfaces, the decision in Phase 1 flips and this skill is the collision design. Second, the rope and particle pattern in Phase 7 is usable now without any terrain field at all: sphere chains and particles can sample a cheap analytic or heightfield-derived distance (a heightfield query is one height lookup, cheaper than a field sample) for ropes, vines, and debris. The pattern transfers; the full field does not, yet. Build the field when the map needs it, not before.

**Depth status:** PARTIAL (reels read firsthand with transcripts and frames; Godot shape-type, HeightMapShape3D, ImageTexture3D, and GPUParticlesCollisionSDF3D behavior verified from the Godot docs; the query contract, gradient forms, and CCD loop verified from the cited SDF literature; the Blender bake route verified against the BVHTree API reference; no hands-on Godot implementation was run in this session, the two-tier paging is this skill's design from the creator's stated analogy rather than a demonstrated build, and the creator's cost and upscale claims carry no measured numbers).

## Cross-links

- `engine-runtime/cave-expedition-render-tech`: the same game's Unity render-tech survey; its SDF claims are flagged prior-audit unverified, and it contains no Godot implementation. This skill is the Godot implementation side; read that skill for the render-tech context, not for collision numbers.
- `engine-runtime/godot-terrain3d-heightmap`: heightfield terrain and the render-vs-collision parity gate this skill's probe gate is modeled on. Read it first when the Phase 1 decision says heightfield.
- `engine-runtime/godot-vertex-animation-texture-crowds`: the format reference for this skill, and its Phase 5 collision note (GPU-animated meshes need CPU-side sphere proxies) is the same separation this skill enforces between animation and collision.
