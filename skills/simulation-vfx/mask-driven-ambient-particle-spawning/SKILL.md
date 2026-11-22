---
name: mask-driven-ambient-particle-spawning
description: "Spawn ambient particles (falling leaves, pollen, embers) only where they belong, using a painted black-and-white mask sampled at spawn time: one camera-following GPUParticles3D system, rejection sampling in script or a mask-reading particle shader, and the head-to-head stress test that killed the per-tree alternative at 2,000 trees. Trigger when ambient particles must fall only in specific areas of a map without hand-placing hundreds of emitters."
---

# Mask-driven ambient particle spawning

## Purpose

This skill reconstructs the mask-driven ambient particle workflow end to end, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: paint where the effect is allowed on a top-down map image, run one particle system that follows the player, and let the mask decide every spawn point, so leaves fall only under trees and never over open fields, with no emitter placed by hand anywhere on the map.

## Source

Creator: beforethesunsets44 (game: Before the Sun Sets, a first-person fantasy melee game; engine not named in either reel, and the editor frame in the first reel only reads as Unreal, which is not claimed here).

- Reel 1, the technique: https://www.instagram.com/reel/Dfcz13dh8PA/ (posted Nov 7, 2026, 92 comments, 30 s). Caption: "Falling leaves.." Full local transcription (faster-whisper tiny, 7 segments), 12 frames read firsthand, work dir `~/workspace/custom-skills/local-video-summarizer/work/Dfcz13dh8PA/`. The creator states the whole method in one line: he took a top-down screenshot of his map, painted everything black, painted the tree areas white, and the system only spawns leaves where the mask is white.
- Reel 2, the stress test: https://www.instagram.com/reel/DfnDulBBqsv/ (posted Nov 11, 2026, 32 comments, 44.4 s). Caption: "My method vs your method.." Full local transcription (faster-whisper tiny), 12 frames read firsthand, work dir `~/workspace/custom-skills/local-video-summarizer/work/bts-DfnDulBBqsv/`. The creator tests his mask method against a viewer-suggested per-tree method at over 2,000 trees. All FPS figures in this skill are his spoken figures on an unnamed machine, never verified measurements (see Phase 5).

Godot APIs below were verified firsthand from the Godot Engine documentation (class pages for GPUParticles3D, Image, and the particle shader reference, plus the complex emission shapes tutorial; URLs in the reference list at the end). The Godot paths have not been run hands-on in this session.

AAA reference (read firsthand): Matt Vainio (lead VFX artist, Sucker Punch), "How stunning visual effects bring Ghost of Tsushima to life", PlayStation.Blog, https://blog.playstation.com/2021/01/12/how-stunning-visual-effects-bring-ghost-of-tsushima-to-life/

## Mask vs per-actor: pick the right one

This skill is the **mask method**: one global system, spawn positions gated by a painted mask. The alternative is the **per-actor method**: every tree carries its own particle effect, playing only near the player.

- Use the mask method when the effect must cover a whole map or biome, when tree counts are in the hundreds or thousands, and when the placement rule is "only where trees are" rather than "this exact tree looks like that". The mask scales with particles on screen, not with placements on the map.
- Use the per-actor method only when a small number of hero trees each need visibly different leaves, and you can afford one particle system per tree. The reel's stress test is the cautionary evidence: at 2,000+ trees the per-actor version ran at 17 FPS against the mask method's ~50 FPS, triggered a system memory-pressure warning, and then crashed the engine. The per-actor advantage the viewer claimed (customize leaves per tree) was stated but never demonstrated in the reel.
- Both methods share one limit: neither knows anything about wind, landing, or interaction unless you add it. The mask decides *where* particles start, nothing else.

## Tools used

An image editor (any layer-based editor; the creator painted in an editor over a screenshot), Godot 4.x (Forward+ or Mobile renderer for the script path; see the Compatibility caveat in Phase 3), one GPUParticles3D node, and optionally a custom `particles` shader for the GPU path in Phase 4.

## Phase 1: Paint the mask

**Do**
1. Take a top-down screenshot of the whole map from the editor. Use a top-down orthographic view if the editor offers one, so the screenshot has no perspective distortion; if only a perspective top view exists, take it from directly above at a fixed height and note that the edges will be slightly stretched.
2. Keep the screenshot as the bottom layer. Add a paint layer above it. Fill the paint layer black.
3. Paint white over every area where the effect is allowed: the canopy footprint of each tree or tree cluster for falling leaves, the meadow for pollen, the scorched ground for embers. Paint the *area the effect falls through*, not the trunk points: leaves spawn across the canopy footprint, so white should cover the crown, slightly wider than the trunk.
4. Export the paint layer alone as a grayscale PNG. One channel carries the data; read the red channel and ignore the rest. Keep the screenshot file next to it: it is the alignment reference for Phase 2 and the repaint base when the map changes.
5. Resolution guidance [this skill's own, not a measured number]: 1 pixel per 1-2 m of map is plenty for spawn gating. A 1,300 m map at 1 px/m is a 1300x1300 image, about 1.7 MB uncompressed. Higher resolution buys nothing, because a spawn point only needs a yes/no answer, and the leaf's fall drift blurs the boundary anyway.

**Check**
- Toggle the paint layer over the screenshot: every white blob sits on trees, no white sits on paths, fields, water, or buildings. One stray white blob over an open field is a visible bug later (leaves falling from a clear sky), so check the edges of the map, where painting discipline slips.
- The exported PNG is black and white only. Any gray from a soft brush is fine (the threshold in Phase 3 treats it as a hard yes/no), but a colored export means the wrong layer was exported.

**Why**
- The mask is the placement rule, written once, in the same picture as the map. Hand-placing emitters writes the same rule hundreds of times, once per emitter, and every map edit then requires re-placing emitters. Repainting one layer is the whole maintenance job.
- Painting the canopy footprint instead of trunk points is what makes the effect read as "leaves falling from trees" from the ground: the spawn area matches what the player sees overhead.

## Phase 2: Align mask space to world space, with landmarks

**Do**
1. Record the world-space rectangle the screenshot covers: the world XZ coordinates of the image's four corners, and which image edge is world -Z (or +Z). Store these four numbers plus the image size in a manifest file next to the mask (see Agent automation). Do not assume the mapping: image row 0 is the top of the screenshot, and whether that is world -Z or +Z depends on the camera orientation used for the screenshot.
2. Write one probe function, `world_to_mask(world_xz) -> Vector2i`, that converts a world XZ position to a mask pixel: subtract the rectangle minimum, divide by the rectangle size, multiply by the image size, and flip the row if the screenshot's top edge is the far side. Clamp the result inside the image; a position outside the rectangle returns "outside", never a wrapped pixel.
3. Establish the mapping empirically with three landmarks, not by reasoning about it. Pick three widely separated, unmistakable features (a distinctive tree cluster, a bridge, a rock), read their world XZ from the editor, compute their mask pixels with the probe function, and check that those pixels land on the right features in the screenshot.
4. Import the mask so pixel reads are exact: no VRAM compression (Godot import: Compression Mode Lossless), filter nearest if the mask is also used as a texture. A compressed or sRGB-remapped mask returns blended values at boundaries and lies about edge pixels.

**Check**
- All three landmarks land on the correct features in the screenshot. If even one is mirrored or offset, the mapping is wrong: fix the flip or the rectangle before touching any particle code. A mirrored mask is the most common failure of this whole workflow, and it looks exactly like the bug the mask was built to fix (leaves over fields, none under trees).
- A probe at a known white pixel returns red above 0.5; a probe at a known black pixel returns red below 0.5. If both return the same value, the import settings are destroying the data (see Failure modes).

**Why**
- The mask is only useful if a world position and a pixel mean the same place. Every downstream step trusts the probe function, so the probe function is verified against the world, not against the formula that produced it.

## Phase 3: One system that follows the player (script path)

**Do**
1. Create exactly one GPUParticles3D node for the effect. Set `local_coords` to `false` (the default): with local coordinates off, particles use global coordinates and stay in world space when the node moves, which is what a following emitter needs. With local coordinates on, every emitted leaf would travel with the node and the forest would appear to move with the player.
2. Grow `visibility_aabb` to cover the spawn volume plus the full fall distance (the default is an 8 m box; a leaf system needs a box spanning the follow radius horizontally and canopy height to ground vertically). The doc's own guidance: grow the box if particles suddenly appear or disappear when the node enters or exits the screen. Use the editor's Particles > Generate AABB tool after a test run, then pad it.
3. Give the node a ParticleProcessMaterial for the fall behavior: downward gravity, small initial downward velocity, damping so leaves flutter rather than plummet, and a scale or color curve over lifetime if the leaf should fade or shrink before landing. Turbulence is optional and costs GPU time; the reel's leaves are simple falling quads with no visible turbulence, so start without it.
4. Set `amount` to the maximum number of leaves visible at once (spawn radius area x fall time x spawn rate), not to a large round number: the system allocates for the full `amount` whether or not particles are visible (per the class doc note on `amount`), so oversizing costs memory and GPU time on every frame. Tune density later with `amount_ratio`, which does not restart the system or resize the buffer.
5. Write the spawner script. On a timer (once per spawn tick, not once per frame unless the rate demands it), repeat: pick a random XZ point inside the follow radius around the player; convert it with the Phase 2 probe; read the mask with `Image.get_pixel(x, y)` (GDScript) or `Image.GetPixel(x, y)` (C#); accept the point if red is above 0.5; retry up to 8 times [this skill's own cap]; if no white point is found, spawn nothing this tick. Emit each accepted leaf with `GPUParticles3D.emit_particle(xform, velocity, color, custom, flags)` (C#: `EmitParticle`), passing `EMIT_FLAG_POSITION | EMIT_FLAG_VELOCITY` (C#: `EmitFlags.Position | EmitFlags.Velocity`), with the transform at canopy height above the accepted XZ and a small downward velocity.
6. Move the node to the player's XZ every frame (Y at canopy height). Do not parent it to the player: a parented node with local coordinates off still works, but moving it in script keeps the follow behavior explicit and debuggable.
7. Load the mask once at startup: `load("res://masks/forest_mask.png") as Texture2D`, then `get_image()` for the `Image` used by `get_pixel`. Keep the `Image` in memory for the spawner's lifetime; reloading it per spawn is the easiest way to turn a cheap system expensive.

**Check**
- Stand at a forest edge: leaves fall under the trees, the open field beside the player stays empty. Stand deep in open ground: nothing spawns at all (the retries exhaust and the tick spawns nothing). Stand deep in forest: a steady fall with no visible gaps or clumps.
- The scene has exactly one GPUParticles3D for this effect. If a second one appears for a "special" grove, that is the per-actor method re-entering through the back door; fold the grove into the mask instead.
- Frame time does not change measurably when the player crosses from field to forest. If it does, the spawn rate or `amount` is wrong, not the mask.

**Why**
- One system means one draw call and one particle buffer for the whole effect, however large the map is. Rejection sampling makes the mask the single source of truth for placement, so the placement rule is edited in one image, not in scene data.
- The retry cap is what keeps the open-field case cheap: without it, a player standing in a huge field makes the spawner loop forever looking for a white pixel that is not nearby. Skipping the tick is correct behavior, not a failure.

**Compatibility caveat (verified):** `emit_particle` is only supported on the Forward+ and Mobile rendering methods, not Compatibility. On a Compatibility target, use the Phase 4 shader path or a process material with an emission shape (see the editor-native variant below) instead of the script path.

## Phase 4: Scale it on the GPU (shader path)

**Do**
1. Keep the same single GPUParticles3D node and the same follow behavior from Phase 3. Replace the process material with a ShaderMaterial running a `particles` shader.
2. Set the emission shape to a box covering the follow radius (a `ParticleProcessMaterial` box shape is not needed here: with a custom process shader, the initial positions come from the emission shape configured on the node; use the box shape and let the shader gate positions). Pass the mask as a `uniform sampler2D` with filter nearest, plus uniforms for the mask's world-space origin and world size (the Phase 2 rectangle).
3. In `start()`: read the particle's initial position from `TRANSFORM` (which starts at `EMISSION_TRANSFORM` plus the emission shape offset). Convert its XZ to mask UV with the origin/size uniforms. Sample the mask. If the sample is black, re-roll: pick a new XZ from a hash of `RANDOM_SEED` and the attempt index, up to 8 attempts [this skill's own cap], resampling each time. If no white point is found, set `ACTIVE = false` so the particle never renders. If white, keep the position and set the fall velocity.
4. In `process()`: apply gravity and damping exactly as the Phase 3 material did, and integrate `TRANSFORM` from `VELOCITY`. Keep the mask lookup out of `process()`: the spawn decision is made once at birth, and re-checking it every frame buys nothing.
5. Editor-native variant (no shader): set the process material's emission shape to Points and use the editor's GPUParticles3D > Create Emission Points From Node on a source mesh whose surface covers only the valid area (for example, a flat mesh built from the white mask cells). The documented command bakes the mesh surface into the emission point texture, and `emission_point_count` then caps how many of those points are used. This variant bakes the mask into the scene at authoring time, so it does not follow map edits until re-baked; prefer the shader path when the map still changes.

**Check**
- The same three edge tests as Phase 3 pass identically (forest edge, open ground, deep forest). The shader path must be behaviorally identical to the script path; any difference means the UV mapping in the shader disagrees with the probe function, which is a Phase 2 bug, not a shader bug.
- Frame time at the same particle count is equal to or better than the script path. If the shader path is slower, the mask texture is being sampled with the wrong filter (linear filtering on a data texture costs nothing extra, but a mipmapped mask blurs edges; verify filter nearest and mipmaps off).
- The mask texture is sampled with `texture()` on a `sampler2D` uniform. If the shader fails to compile with the sampler, check that the uniform is declared at file scope and the texture is assigned in the inspector; particle shaders support sampler uniforms, but an unassigned uniform samples black, which silently kills every particle.

**Why**
- Moving the spawn decision to the GPU removes the script from the per-spawn path entirely: emission rate is then bounded by the GPU, not by GDScript/C# calls per particle. The mask stays the single source of truth; only the reader changes.
- Killing rejected particles with `ACTIVE = false` at birth is cheaper than letting them fall and hiding them: a dead particle costs no draw time.

## Phase 5: The stress test (replicate the reel's, on your machine)

**Do**
1. Build the test scene at the map's maximum load: every tree in the forest, no culling, the same condition the reel used ("no culling" per the transcript's context). Record the tree count.
2. Run the mask method and record: FPS, frame time, memory, and stability over at least 60 seconds of play, including walking the forest edge and standing still in open ground.
3. If a comparison is needed, build the per-actor variant on the same map (one particle system per tree, playing only near the player) and run the identical 60-second pass. Record the same four numbers. Expect the per-actor cost to grow with tree count even for trees the player cannot see, because each system carries its own buffer and draw call.
4. Watch for the memory-pressure warning and any crash, and record them as results, not as interruptions. The reel's per-actor run showed a system memory-pressure warning, an unexplained FPS jump from 17 back to 60, and then an engine crash; the creator honestly reported not knowing what the jump meant.
5. Re-run any anomalous result before believing it. An FPS jump with no code change is a measurement artifact (a stall clearing, a cache warming, a background process ending), not a finding. Two runs that disagree mean the test is not controlled; fix the test (close background apps, fix the camera path, fix the duration) and run a third.

**Check**
- The mask method holds its frame rate and finishes the 60 seconds without warnings at full tree count. The per-actor variant, if built, is measurably worse on at least two of the four numbers (FPS, frame time, memory, stability).
- The numbers are labeled with the machine, the renderer, and the tree count. An FPS figure without those three is not a result; it is an anecdote. The reel's figures (~50 FPS mask vs 17 FPS per-actor at 2,000+ trees) are the creator's spoken figures on an unnamed machine and are cited here only as his evidence, never as a benchmark for your hardware.

**Why**
- The test, not the theory, decides between methods. Per-actor systems look cheaper on paper ("only near the player") because the off-screen cost is invisible in the editor; the stress test makes it visible. The reel's crash is the point: the failure mode of the per-actor method is not ugliness, it is instability at scale.

## The human method, distilled

1. **One rule, written once.** The mask is the placement rule. Everything else reads it.
2. **Verify the mapping against the world.** Three landmarks beat any formula for mask-to-world alignment.
3. **One system follows the player.** Cost scales with what is on screen, never with how big the map is.
4. **Skip, don't search.** A failed spawn tick in open ground is correct behavior; an unbounded retry loop is a hitch.
5. **Test at maximum load, no culling.** The comparison that matters is the one at the worst case, not the showcase case.
6. **Re-run anomalies.** An unexplained jump is a broken test, not a result.

## Failure modes

- **Mirrored or offset mask.** Leaves fall over fields and not under trees, exactly the bug the mask was built to fix. Fix: re-run the Phase 2 landmark check; the flip or the rectangle is wrong. Never "fix" it by repainting the mask mirrored; the manifest is wrong, not the painting.
- **Mask reads as all black or all white.** Import settings destroyed the data (VRAM compression, sRGB remap) or the probe function clamps wrong. Fix: import Lossless, verify the two probe values in Phase 2, and check the probe clamps out-of-rectangle positions to "outside" instead of wrapping to the opposite edge.
- **Leaves pop in and out at the screen edge.** `visibility_aabb` is still the 8 m default. Fix: grow it to the spawn volume plus fall distance, or run Particles > Generate AABB and pad the result.
- **The whole forest drifts with the player.** `local_coords` is true. Fix: set it false so emitted leaves stay in world space.
- **Hitch when standing in open ground.** Unbounded rejection retries. Fix: cap retries (8) and skip the tick when they exhaust.
- **Frame rate drops when entering the forest, even though the mask is right.** `amount` is oversized, or the spawn rate is too high for the fall time. Fix: size `amount` to the visible maximum and tune density with `amount_ratio`, which does not restart the system.
- **Blocky mask edges.** A low-resolution mask with hard edges reads as stripes of leaves starting and stopping along a visible line. Fix: blur the mask slightly, or modulate the sampled value with a noise pattern at spawn time, the way Sucker Punch did when their first biome-map pass came out blocky (see AAA practice). Do not raise the mask resolution past 1-2 px/m; the boundary softness is a sampling problem, not a resolution problem.
- **Mask drift.** The map was edited (trees moved, forest extended) and the mask was not repainted. Leaves now fall where trees used to be. Fix: repaint from a fresh screenshot; the manifest's painted date against the map's edit date is the check (see Agent automation).
- **Per-actor regression.** A later edit adds per-tree emitters for a "special" grove. Fix: fold the grove into the mask. One system is the architecture; exceptions are how the 2,000-system version comes back.
- **`emit_particle` silently does nothing.** The project targets the Compatibility renderer, where `emit_particle` is unsupported. Fix: use the Phase 4 shader path or the editor-native emission-points variant on that target.
- **Shader path kills every particle.** The mask uniform is unassigned (samples black) or the UV mapping disagrees with the probe function. Fix: assign the texture in the inspector, verify filter nearest, and re-run the Phase 2 landmark check against the shader's uniforms.

## AAA studio practice

- **Sucker Punch, Ghost of Tsushima (PS4, 2020).** The shipped game hit the exact same problem and went through the same three approaches, documented by lead VFX artist Matt Vainio. First, per-tree effects: "we placed an effect in the trees that were grown procedurally around the island. This failed pretty quickly because the environment was instancing hundreds of trees in small spaces, which, while fine for geometry, was too expensive for particle systems." Restricting them to ~50 feet from the player "felt like a failure when the view distances were so far", and a leaf dropped from a 40-foot canopy might not even fall into view before a horse rider passed the tree. Second, growth-system circles pushed in from the mask edges using the same masks and expressions as the environment: it mostly worked but left large gaps, cost performance as emitter counts rose, and was fragile, because changing growth rules to fix one area broke other forests. Third, the biome map: a rendering programmer's real-time growth-mask data, piggy-backed by VFX, so "the particle system [could] know what biome any specific particle was created in". The first pass was blocky; noise modulation made it organic. The result: "we were able to remove hundreds of grown particle systems from the environment and replace it with a single system that followed the camera and was much more accurate to the environmental biomes." Tens of thousands of leaves can be on screen at once, all driven by one global wind that trees, grass, cloth, and particles share, with per-biome variants (leaves in forests, pampas fluff in fields, ash in burnt areas). The lesson that transfers directly: the winning architecture is one camera-following system reading biome data at spawn time, and the mask is allowed to carry more than one channel. A three-channel mask (red = forest, green = field, blue = burnt) drives three ambient effects from one image, the way Ghost's biome map drives per-biome particle variants. Source: https://blog.playstation.com/2021/01/12/how-stunning-visual-effects-bring-ghost-of-tsushima-to-life/
- **The reel's own evidence.** The Before the Sun Sets stress test is the same experiment at indie scale with the same outcome: mask ~50 FPS vs per-tree 17 FPS plus a memory warning and a crash at 2,000+ trees, on the creator's unnamed machine. It is cited as his spoken evidence, not as a benchmark. Its honest unresolved thread (the unexplained 17 to 60 FPS jump) is itself the practice: report the anomaly, do not explain it away.

## Agent automation

- **Mask manifest.** Keep `mask-manifest.json` next to each mask: mask path, source screenshot path, world rectangle (min/max XZ), image orientation (which edge is world -Z), image size, painted date, and the three landmark probes with their world XZ and expected mask pixels. A build or scene-load check fails if the mask file is missing, the rectangle does not match the map bounds, or any landmark probe lands on the wrong pixel value.
- **Alignment gate.** On mask import or map edit, run the three landmark probes automatically and fail the import when any probe disagrees with its recorded value. A flipped or stale mask must never reach a playtest silently.
- **Edge test.** Scripted playtest: teleport the player to three positions (forest edge, open ground center, deep forest), wait 2 seconds at each, and count spawned particles whose XZ falls on black mask pixels. The count must be zero at all three. Any positive count is a Phase 2 mapping bug.
- **Perf gate.** At full tree count with no culling, record FPS, frame time, memory, and draw calls with the ambient system on and off. Fail when the system costs more than the recorded budget [budget is the project's own, not a number from this skill] or when the scene contains more than one GPUParticles3D for the same ambient effect (the per-actor regression detector: count GPUParticles3D nodes parented under foliage or tree scenes and fail above one per effect).
- **Drift check.** Compare the mask's painted date against the map scene's last edit date; warn when the map is newer than the mask. A warned mask is repainted from a fresh screenshot before the next playtest, not after a bug report.
- **Threshold check.** The 0.5 threshold and the 8-retry cap are this skill's own defaults. Record them in the manifest so a later tuning pass changes them deliberately instead of discovering them as magic numbers in the spawner script.

## Valkyrie note

This maps directly onto Valkyrie's existing data. The Pellune map is authored, not procedural, with deterministic seeded scatter on authored masks, so the mask the workflow needs already exists as authored data: reuse the same authored masks the scatter uses, instead of painting a second mask from a screenshot. One camera-following system fits the fixed iso camera well, because the spawn radius is the visible area, which is small and constant. Valkyrie is Godot 4.7.2 with C#, Forward+, so both the script path (`Image.GetPixel`, `GpuParticles3D.EmitParticle` with `EmitFlags.Position | EmitFlags.Velocity`) and the shader path are available; the Compatibility caveat on `emit_particle` does not apply. The sim still needs CPU positions for citizen pathing and collision, but ambient leaves need none of that: they are pure atmosphere, and the mask keeps them out of gameplay systems entirely.

## Comment-thread evidence (first-page comments, verified in raw JSON)

The creator answered the technique debate himself, and his answers are load-bearing for this skill:

- **Why the mask exists.** The trees are not actors. Asked why per-tree effects would not work, he replied: "the trees aren't objects, the engine show them all as one object (like as foliage) not evry tree as its own actor." Every per-tree emitter or script proposal dies on that fact: there is no per-tree object to attach anything to. (Reel Dfcz13dh8PA comments.)
- **The method's stated limit.** He concedes it himself: "i agree that this method might not work if the world has different layers!" A single flat mask cannot distinguish stacked vertical layers (canopy vs undergrowth, bridges over forest). Multi-layer worlds need one mask channel per layer, which is why Phase 4 generalizes to channels.
- **The serious counter-proposals, and why they do not apply here.** Viewer David proposed ISMC/HSMC instance transforms via `GetInstanceTransform` without separate actors; SAIyonara and Feelali proposed FOV plus radius plus camera-follow pooling (spawn only in a circle around the player, in view, following the camera); Martin proposed a pooled particle system spawning at radius around nearby trees; David separately proposed tag-based proximity checks for "Tree" objects. Rico's caution supports the mask side: cheap instances must stay cheap, and spawning new actors on top doubles streaming cost. All four proposals assume per-instance access or per-object queries the creator says he does not have, since his foliage is one merged object. They are recorded here so a reader with a different foliage setup (true instanced meshes with transform access) can pick the pooled variant instead; for merged foliage, the mask stands.

Coverage note: comment fetches return a first page only (50 of 92 read on the Nov 7 reel, 20 of 32 on the Nov 11 reel). Later pages may hold more.

**Depth status:** PARTIAL (both source reels read firsthand with full transcripts and frames; Godot APIs verified from the official documentation; AAA lineage documented from the Sucker Punch post read firsthand; neither Godot path has been run hands-on in this session; the FPS figures are the creator's spoken numbers on an unnamed machine; the engine in the reels is unnamed).

## References

- Reel 1 (technique): https://www.instagram.com/reel/Dfcz13dh8PA/
- Reel 2 (stress test): https://www.instagram.com/reel/DfnDulBBqsv/
- Ghost of Tsushima VFX (Sucker Punch): https://blog.playstation.com/2021/01/12/how-stunning-visual-effects-bring-ghost-of-tsushima-to-life/
- GPUParticles3D class (amount, amount_ratio, local_coords, visibility_aabb, emit_particle, EmitFlags): https://docs.godotengine.org/en/4.0/classes/class_gpuparticles3d.html
- Image class (get_pixel, get_pixelv): https://docs.godotengine.org/en/4.0/classes/class_image.html
- Particle shaders (start/process, TRANSFORM, VELOCITY, ACTIVE, EMISSION_TRANSFORM, RANDOM_SEED): https://docs.godotengine.org/en/4.0/tutorials/shaders/shader_reference/particle_shader.html
- Complex emission shapes (emission point textures, Create Emission Points From Node): https://docs.godotengine.org/en/4.1/tutorials/3d/particles/complex_shapes.html
- ParticleProcessMaterial (emission shapes, emission_point_texture, emission_point_count): https://docs.godotengine.org/en/4.0/classes/class_particleprocessmaterial.html

Cross-links: `simulation-vfx/niagara-explosion-sprite-sheets-godot` (Godot particle import path), `simulation-vfx/smoke-flipbook-particles` (another camera-facing ambient particle technique), `simulation-vfx/ue-wind-shader-grass` (painted flow-map driving vegetation motion, the shader-side cousin of a painted mask), `simulation-vfx/godot-vfx-pack-shell-stacking` (Godot VFX composition).
