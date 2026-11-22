---
name: scripted-thrown-weapon-projectile
description: "Build a scripted thrown-weapon projectile in Godot 4: a spinning sword, axe, or spear driven by manual transform updates in _physics_process (the Before the Sun Sets pattern), with swept hit detection, a one-shot impact burst plus decal, and a recall, boomerang-return, or respawn recovery. Trigger when a game needs a throwable melee weapon whose arc, spin, and return are authored rather than physics-simulated."
---

# Scripted thrown-weapon projectile (Godot transfer of the Before the Sun Sets pattern)

## Purpose

This skill reconstructs a thrown-weapon workflow end to end, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: the weapon is a scripted actor, not a simulated body. Each physics frame the script advances its position along an authored path and spins only its visible mesh, a swept query decides whether anything was hit along the way, and a small state machine (held, thrown, stuck, returning, held) owns the whole lifecycle including recovery. The creator's version is Unreal Blueprint; the implementation below is a Godot 4 transfer of the same pattern, labeled as such throughout.

## Source

Creator: beforethesunsets44 (game: Before the Sun Sets, Unreal Engine). Instagram reel: https://www.instagram.com/reel/Da5xRBYBYYG/ (posted July 17, 2026, 146 comments, 7.1 s, music-only, no on-screen text). Full local transcription (faster-whisper tiny, empty: no speech), 12 frames read firsthand, work dir `~/workspace/custom-skills/local-video-summarizer/work/bts-Da5xRBYBYYG/`.

What the reel actually shows, frame by frame: an Unreal Blueprint EventGraph with Set World Location / Set World Rotation nodes driving a sword mesh; a Blender viewport with two low-poly arms on an armature gripping swords, timeline at frame 61 (the throw animation being authored on a first-person arms rig); a Niagara system named "Blood_NS" with emitters "Minimal" and "CompletelyEmpty...", Spawn Burst Instantaneous, Add Velocity In Cone, previewing a red splatter burst; gameplay of a gray sword tumbling end-over-end toward a black-robed spearman, a red blood burst on impact, and the figure collapsing; closing shots of a knight and an archer with thrown swords arcing through a purple sky.

What the reel does NOT show (do not invent any of it as the creator's method): no throw rules (range, damage, retrieval, cooldown, ammo); the Blueprint nodes are too small to read exactly, so the precise motion logic (arc shape, spin rate, homing) cannot be determined; whether the thrown sword is recovered, respawns, or is lost is unresolved; the knight and archer closing shots are not clearly connected to the throw. Every number in this skill marked "starting point" is this skill's own tuning suggestion, not the creator's.

Godot sources (all read firsthand): RigidBody3D, Area3D, Node3D, Basis, PhysicsDirectSpaceState3D, PhysicsRayQueryParameters3D, GPUParticles3D, ParticleProcessMaterial, and Decal class documentation, docs.godotengine.org (4.x); "Using decals" tutorial, docs.godotengine.org; "Shooting with Raycasts", Godot 4 Recipes, https://kidscancode.org/godot_recipes/4.x/3d/shooting_raycasts/index.html

## Scripted vs physics: pick the right one

The creator drives the sword with Set World Location / Set World Rotation nodes: the script owns the transform every tick. That is the scripted pattern. The alternative in each engine is a simulated body: Unreal's ProjectileMovementComponent (velocity, gravity, bounce, homing) or Godot's RigidBody3D (forces and impulses, the simulation computes movement, rotation, and collision response).

- Use the scripted pattern when the flight must be authored: a fixed arc, a spin that reads at a glance, a return path that comes back to the hand, a stick-then-recall beat. You pay for that control with responsibility: you own hit detection, because a scripted transform has no physics response.
- Use a RigidBody3D when the weapon must react to the world: bouncing off walls, knocking props around, tumbling to rest on the floor. Godot's docs warn directly against changing a RigidBody3D's transform every frame ("changing this from a process loop may result in strange behavior... use _integrate_forces"), which is exactly what the scripted pattern does, so do not mix the two: a body is either simulated or scripted, never both on alternating frames.
- The middle option, RigidBody3D with `continuous_cd` (continuous collision detection: "tries to predict where a moving body will collide... more precise, and misses fewer impacts by small, fast-moving objects"), keeps simulation and fixes the fast-mover miss. It still cannot author a return path or a readable spin; if you need either, go scripted and add the swept query in Phase 4.

## Tools used

Godot 4.x (Forward+ if decals are used; the Compatibility renderer does not render decals); Blender for the throw animation on the wielder's rig; no addons required. C# note: Valkyrie uses Godot with C#. The sketches below are GDScript, matching the documentation; the C# API uses the same calls with PascalCase names (`_PhysicsProcess`, `RotateObjectLocal`, `IntersectRay`, `ContinuousCd`).

## Phase 1: Write the weapon contract before building anything

**Do**
1. Decide the lifecycle as a state machine with five states: HELD, THROWN, STUCK, RETURNING, HELD. Every transition is named before any scene is built: throw input moves HELD to THROWN; a hit moves THROWN to STUCK (embed) or to a despawn (shatter); recall input moves STUCK to RETURNING; arrival at the hand moves RETURNING to HELD; a timeout moves any airborne state to recovery (see step 3).
2. Decide the recovery rule, because the reel never shows one. Three honest options, pick exactly one per weapon: (a) manual recall, the Leviathan Axe model: the weapon sticks where it lands until the player recalls it, and the return can hit on the way back; (b) automatic boomerang return: after a fixed range or flight time the weapon steers home on its own; (c) despawn and respawn: the weapon vanishes on impact or timeout and a fresh copy appears in the hand. Record the choice in the weapon's tuning file; a weapon with no recovery rule is a weapon the player can lose forever.
3. Set the tuning values as exported variables on the projectile script, all labeled starting points for this skill: flight speed, spin rate in radians per second, maximum range or flight time before automatic return, stick time before a stuck weapon can be recalled, return speed. One starting set that reads on screen: speed 20 m/s, spin about 12 rad/s (roughly two end-over-end tumbles per second), return speed slightly faster than flight speed so the return feels eager, not lazy.
4. Decide what the weapon can hit while returning. The God of War reference (see AAA practice) found return hits "basically mandatory". Default to: the return path uses the same hit detection as the throw, with the same damage, unless the design explicitly says the return is harmless.

**Check**
- The state machine is written down with every transition named, including the timeout transition. If any state has no exit, the design is unfinished.
- The recovery rule is one of the three options above, written in the tuning file. "The player picks it up" is not a recovery rule unless a pickup interaction is also specified.

**Why**
- A thrown weapon is a lifecycle problem before it is a physics problem. The reel's visible failure mode is exactly this gap: a great-looking throw with no shown recovery. The state machine forces the recovery decision up front, where it is cheap.

## Phase 2: Build the projectile scene (detection separate from display)

**Do**
1. Scene root: `Area3D` named `ThrownWeapon`. Area3D is a detection region, not a physical barrier: it "detects when other CollisionObject3Ds enter or exit it" and emits `body_entered` / `area_entered` signals. That is the whole hit-detection contract: the script moves the area, the area reports overlaps.
2. Child 1: `CollisionShape3D` with a `SphereShape3D` sized to cover the spinning blade's swept volume (a sphere of roughly half the blade length). Use a sphere, not a box matching the blade: the blade spins, so a box would tumble and report false hits at the corners.
3. Child 2: `MeshInstance3D` with the weapon mesh. The spin is applied to THIS child only (Phase 3), never to the root, so the collision shape stays a stable sphere while the visible blade tumbles.
4. Child 3 (optional, recommended): a trail. A fading ribbon or a short GPUParticles3D trail emitted while THROWN makes the arc readable at distance. Keep it a child of the root, not of the spinning mesh, or the trail inherits the spin.
5. Collision layers: put the projectile on its own layer (for example layer 5, "projectiles"). Set its mask to the layers it may hit (enemies, world) and NOT to the thrower's layer. Set the thrower's hurtbox `monitorable` true and the projectile's `monitoring` true: area-to-area detection needs monitoring on the seer and monitorable on the seen, with matching layer/mask bits, and the `area_entered` signal (not `body_entered`) for area-to-area pairs.
6. Spawn the projectile from a muzzle point slightly in front of the thrower's hand, offset along the aim direction, so the first frame does not start inside the thrower. Exclude the thrower's RID from every swept query in Phase 4 as well, as a second guard.

**Check**
- In the editor, the sphere shape encloses the blade at every spin angle. Rotate the mesh child through a full tumble by hand and watch the sphere: if any blade tip exits the sphere, enlarge it.
- With the game running and the weapon held, no hit signal fires. If one fires at spawn, the spawn offset is too small or the thrower is on a masked layer.

**Why**
- Separating detection (stable sphere on the root) from display (spinning mesh child) is what makes the scripted pattern safe. The creator's reel shows the same separation in Unreal terms: the Blueprint drives the actor transform while the mesh is a child that can tumble. A spinning collision shape is the classic source of phantom hits.

## Phase 3: Throw and spin in `_physics_process`

**Do**
1. Drive all motion in `_physics_process(delta)`, never `_process`. Physics queries and Area3D signals run on the physics tick; moving the projectile on the render tick desyncs it from the detection it depends on.
2. On throw: record the throw origin, the aim direction (a normalized Vector3), and the flight speed. Hide or swap the held weapon mesh on the wielder at the same moment, and spawn the projectile at the muzzle point from Phase 2.
3. Each physics frame while THROWN: compute the next position as `position + direction * speed * delta`, then apply gravity as a downward adjustment to `direction` if the design wants an arc (bend `direction` toward down by a small gravity factor per frame), or keep `direction` fixed for a flat throw. Then run the swept query from Phase 4 BEFORE assigning the new position: if the query reports a hit before the destination, stop at the hit point instead.
4. Spin the mesh child only: `mesh_child.rotate_object_local(Vector3.RIGHT, spin_rate * delta)`. `rotate_object_local` rotates around an axis in the object's own local space, which is what an end-over-end tumble is: the blade's own long axis stays put while the blade rotates around its short axis. Use the mesh child's local X axis if the blade is modeled along Y; the axis is whichever local axis is perpendicular to the blade and to the flight direction. Do not accumulate Euler angles on `rotation`: repeated Euler edits drift and can shear the basis (the Basis docs warn that rotating axes individually shears the basis; `Node3D.orthonormalize()` exists to repair it). If the mesh ever looks skewed after long flights, call `orthonormalize()` on the mesh child when the weapon returns to the hand.
5. Play the throw animation on the wielder, not on the projectile. The creator authors the throw on the arms rig in Blender (timeline frame 61 in the reel); the projectile spawns at the animation's release moment. In Godot: an AnimationPlayer or AnimationTree clip on the wielder, with a method call track or a timed signal at the release frame that spawns the projectile. The projectile scene itself carries no throw animation.

**Check**
- At half speed (Engine.time_scale 0.5 or a debug slow-motion toggle), the blade tumbles end-over-end around its short axis and the arc reads as one smooth curve. If the blade cartwheels sideways or corkscrews, the spin axis is wrong: try the other local axis.
- The spin rate is frame-rate independent: the same throw at 30 fps and 144 fps shows the same number of tumbles over the same distance. If it does not, the angle is not multiplied by `delta`.
- The throw animation's release frame and the projectile spawn coincide within one physics frame. If the blade visibly pops out of the hand early or late, the call track is on the wrong frame.

**Why**
- The spin is display; the flight is the script. Keeping them on different nodes (Phase 2) and different clocks (physics tick for flight, release frame for the animation) is what keeps a scripted throw looking physical instead of puppeted.

## Phase 4: Swept hit detection (the phase that prevents tunneling)

**Do**
1. Understand the failure first: a scripted projectile moves in discrete steps per physics frame. At 20 m/s and 60 physics ticks per second, each step is 0.33 m. A thin enemy, a fence post, or a wall thinner than the step size can sit entirely between two sampled positions, and the Area3D overlap check never sees it. That is tunneling, and the faster the weapon, the worse it gets.
2. Simple gate (sufficient for most thrown weapons): each physics frame, before moving, cast a ray from the current position to the intended next position with `PhysicsRayQueryParameters3D.create(from, to)`, exclude the projectile's own RID and the thrower's RID, and pass it to `get_world_3d().direct_space_state.intersect_ray(query)`. The returned dictionary holds `collider`, `position`, `normal`, and `rid`, or is empty when nothing was hit. If it reports a hit, stop at `position`, run the impact from Phase 5, and do not advance further. This is the documented raycast pattern (Godot 4 Recipes, "Shooting with Raycasts": "Game physics engines often break down when trying to handle very fast-moving objects. The solution is to cast a ray... and detect the first thing that would be hit").
3. Robust gate (use when the weapon is large or very fast): replace the ray with a shape cast. `PhysicsDirectSpaceState3D.cast_motion` "checks how far a Shape3D can move without colliding" and returns the safe and unsafe proportions of the motion; a result of `[1.0, 1.0]` means no collision. Advance only the safe proportion of the step, and treat anything below 1.0 as a hit at that fraction. This catches edge cases the thin ray misses, because it sweeps the actual sphere shape.
4. Keep the Area3D signals as the second layer, not the only layer: `area_entered` on an enemy hurtbox is the clean damage hook, but it fires on overlap transitions, so a spawn that starts already overlapping a hurtbox may never fire (the signal needs a transition). The swept query is the authority for "did the flight path cross anything"; the area signal is the authority for "which hurtbox did it touch". When they disagree, trust the swept query for position and the area signal for identity.
5. During RETURNING, run the same swept query along the return path. If the return path crosses a wall and the design says the weapon returns through walls (the axe model: it comes back regardless), skip world layers in the return query's mask but keep enemy layers. If the design says walls block the return, keep the full mask and let the weapon stick again. Record which behavior the weapon uses; it is a design decision, not an accident.

**Check**
- The tunneling test: place a 0.1 m thick wall, throw at point-blank range at full speed, and confirm a hit registers every time across 20 throws. Then double the speed and repeat. If any throw passes through, the swept query is missing or its exclude list is swallowing the wall.
- The identity test: the hit reports the enemy that was visually struck, not a bystander behind it. If the wrong body is reported, the mask includes a layer it should not, or the exclude list is empty.
- The spawn test: throwing with an enemy standing against the thrower still launches cleanly. If the weapon sticks instantly, the spawn offset or the exclude list is wrong.

**Why**
- A scripted projectile has no physics engine watching its back. The swept query is the physics engine, written by hand, one ray or one shape cast per frame. Skipping it is how fast weapons fly through walls in shipped games.

## Phase 5: Impact feedback (burst, decal, stick)

**Do**
1. On a confirmed hit, freeze the projectile at the hit point and switch state to STUCK (or despawn, per the Phase 1 contract). Do not let it keep advancing into the target for even one frame; the visible symptom is the blade sinking into the enemy.
2. Fire the impact burst: a `GPUParticles3D` with `one_shot = true` and `explosiveness = 1.0` ("if 1, all particles are emitted simultaneously"), `amount` set to the burst size, and a `ParticleProcessMaterial` with `direction` set to the hit normal (or the reverse flight direction for a blood-style burst), `spread` controlling the cone (the creator's Niagara burst uses "Add Velocity In Cone", which is the same shape), and `initial_velocity_min` / `initial_velocity_max` giving the spray its range. Restart it with `restart()`, not by setting `emitting = true`: the docs warn that for one-shot emitters, setting emitting "will not restart the emission cycle until after all active particles finish processing", and `restart()` avoids the delay. Spawn the burst as a child of the scene root, not of the projectile, so freeing the projectile does not kill the burst mid-flight.
3. Leave a mark on static surfaces: a `Decal` node placed at the hit point, oriented so its local Y axis follows the surface normal (decals project down their local -Y within their AABB; the "Using decals" tutorial covers creating decals during gameplay "such as bullet impacts"). Decals only render in the Forward+ and Mobile rendering methods, not Compatibility, so confirm the project renderer before relying on them. Pool the decals (a fixed ring of reusable slots that fade out) rather than spawning one per hit: every visible decal is a clustered element sharing a finite budget with lights and reflection probes.
4. Stick beat (only for the STUCK state): hold the weapon embedded for a short, visible moment before it can be recalled, with a small wiggle as it frees itself. This is the God of War detail (see AAA practice): the axe "sticks for a second before being recalled and even has a small wiggle before it's freed... so that players would feel as though the axe was truly wedged". Implement it as a 0.15 to 0.3 s timer (starting point, tune by feel) during which recall input is ignored, plus a two-frame rotation wobble on the mesh child.
5. Apply the hit itself through the area signal or a direct call on the collider: `if collider.has_method("apply_damage"): collider.apply_damage(damage)`. Keep damage out of the projectile script's movement code; the projectile reports the hit, the target decides what a hit means.

**Check**
- The burst fires exactly once per hit, at the hit point, oriented along the normal. If it fires twice, both the swept query and the area signal are triggering impact; gate impact on a `has_hit` flag set by whichever fires first.
- The burst keeps playing after the projectile is freed or recalled. If it vanishes with the weapon, it is parented to the projectile.
- The decal lies flat on the surface and fades. If it skews through the wall, its Y axis is not aligned to the normal. If it never appears, check the renderer (Compatibility shows nothing).

**Why**
- The reel's impact reads because three things land on the same frame: the blade stops, the red burst erupts, the enemy collapses. Any one of them alone looks broken. The burst is the cheapest of the three and the easiest to get wrong by parenting it to the thing that gets freed.

## Phase 6: Return or recover

**Do**
1. Manual recall (option a): on recall input while STUCK, switch to RETURNING. Each physics frame, steer toward the wielder's hand: `direction = (hand_position - position).normalized()`, advance by return speed, run the Phase 4 swept query with the return mask, and keep the spin going (the axe returns spinning). On arrival within a catch radius of the hand, switch to HELD, show the held mesh again, and free the projectile. Keep hit detection live during the return unless the design says otherwise.
2. Automatic boomerang return (option b): when flight time or range exceeds the tuned limit, switch to RETURNING without input and follow the same steering. Add a visible cue that the return has started (a sound, a glint, a slight speed-up) so the player reads the state change.
3. Despawn and respawn (option c): on impact or timeout, free the projectile and re-show the held mesh after a short delay. No return flight exists; the delay is the whole recovery feel, so tune it (starting point: 0.25 s) rather than leaving it at zero.
4. Timeout fallback (all options): a hard cap on total lifetime (starting point: 10 s). Whatever state the weapon is in when the cap hits, free it and restore the held mesh. This is the guard against the lost-weapon bug: a weapon stuck inside geometry, or one whose return path can never reach the hand, must come back anyway.
5. Catch feel: on arrival, play a short catch animation or sound and a one-frame speed carry-through on the wielder (the axe reference: the catch must "feel strong" but "casual, like he does it all the time", with momentum carried through so the player feels the weapon's speed). Do not freeze the player during the catch; the scrapped God of War version that forced Kratos to stand still was rejected for exactly that reason.

**Check**
- Throw, stick, recall, catch: the full loop runs 20 times in a row without a lost weapon, a doubled weapon, or a weapon stuck in a wall. If any loop leaves the held mesh hidden and no projectile in flight, the state machine has a missing transition.
- The return path crosses an enemy: the enemy takes the return hit if the design says so, and nothing happens if it says harmless. If both happen on different runs, the return mask is not fixed.
- The timeout fires: force a stick inside geometry (throw into a corner seam) and confirm the weapon returns to the hand within the cap.

**Why**
- The return is the mechanic players remember (the axe recall was "one of the earliest gameplay/combat prototypes" and the most talked-about part of the weapon). A throw without a satisfying return is a consumable, not a weapon.

## The human method, distilled

1. **Script the flight, don't simulate it.** When the arc, spin, and return are the design, own the transform every physics frame and write the hit detection yourself.
2. **Detection and display are separate nodes.** A stable sphere detects; a spinning mesh child performs. Never spin the shape.
3. **Sweep the step, don't sample the endpoint.** A fast weapon lives between frames; the ray or shape cast is what makes it solid.
4. **The state machine is the feature.** Held, thrown, stuck, returning: if a transition is unnamed, the weapon can be lost.
5. **Impact is three things on one frame.** Stop the blade, fire the burst, mark the surface. Parent the burst to the world, not the weapon.
6. **The return is the weapon.** Decide recall, boomerang, or respawn before building, and make the return hit (or explicitly harmless) on purpose.

## Failure modes

- **Tunneling through thin targets.** A step larger than the target's thickness skips the overlap check. Fix: the Phase 4 swept query every physics frame; for simulated bodies, `continuous_cd` instead.
- **Spinning collision shape.** A box shaped like the blade tumbles and reports hits at the corners. Fix: spin the mesh child only, keep a sphere on the root.
- **Area3D never fires.** The usual causes, in order: the seer's `monitoring` is off, the seen's `monitorable` is off, the layer/mask bits do not overlap, or the code listens to `body_entered` for an area-to-area pair (it needs `area_entered`). All four must align.
- **Self-hit on the first frame.** The projectile spawns inside the thrower or the thrower is on a masked layer. Fix: muzzle offset plus the thrower's RID in every query's exclude list.
- **Double impact.** Both the swept query and the area signal fire impact. Fix: a `has_hit` flag; the first reporter wins, the second is ignored.
- **Burst dies with the weapon.** A one-shot burst parented to the projectile is freed with it. Fix: spawn bursts under the scene root. Restart with `restart()`, not `emitting = true`, or the second throw in quick succession silently fails to burst.
- **Decal never appears.** The project runs the Compatibility renderer, which does not render decals. Fix: Forward+ or Mobile, or skip decals and use the burst alone.
- **Skewed mesh after long flights.** Repeated basis rotation accumulates shear. Fix: `orthonormalize()` on the mesh child when the weapon returns to the hand; prefer `rotate_object_local` over Euler accumulation.
- **Lost weapon.** No timeout fallback, or a return path blocked forever by geometry. Fix: the hard lifetime cap in Phase 6, which restores the held mesh unconditionally.
- **Return hits feel random.** The return mask differs from the throw mask without a design reason. Fix: one mask decision per weapon, recorded in the tuning file, applied to both directions.

## AAA studio practice

- **Santa Monica Studio, God of War (2018), the Leviathan Axe.** The recall was "one of the earliest gameplay/combat prototypes" the team built, from a proposal by lead systems designer Vince Napoli after lead animator Mehdi Yssef's previs showed Kratos throwing the axe. Three decisions from Napoli's account that transfer directly: hitting enemies on the return "was basically mandatory" (satisfying on purpose and by accident); the axe sticks for a beat and wiggles before freeing itself, "so that players would feel as though the axe was truly wedged"; the recall starts weighty, "almost like a mini-attack", and the catch stays casual with momentum carried through. The scrapped version that forced Kratos to stand still with his hand raised was rejected because it limited movement and would get old. Source (read firsthand): ComicBook coverage of Napoli's blog, https://comicbook.com/gaming/news/god-of-war-leviathan-axe-recall/
- **The creator's own indie case (this skill's source).** Before the Sun Sets shows the minimal viable version of the same pattern: one Blueprint actor, manual transform nodes, one Niagara burst, one Blender-authored throw on an arms rig. No return is shown, which is precisely the gap Phase 1 and Phase 6 exist to close. The lesson is division of labor: animation authored in Blender, motion scripted in the engine, feedback from a burst system. That division survives the engine transfer intact.

## Agent automation

- **Weapon tuning manifest.** Keep one tuning resource per thrown weapon (speed, spin rate and axis, max range/time, stick time, return speed, return mask behavior, recovery option, damage). A validation script fails the build when: the spin axis is not a unit vector, no recovery option is selected, the return mask is unset, or the timeout cap is missing. Tuning values are data, never literals buried in the movement code.
- **Tunneling test (headless).** Spawn the projectile at a known speed toward a 0.1 m wall, run the physics frames headless, and assert a hit registers within the expected frame count. Repeat at double speed. A miss at either speed fails the gate; the fix is the swept query, never a bigger collision shape.
- **Lifecycle test (headless).** Script the full loop 20 times (throw, hit, recall, catch) plus one forced corner-stick case, and assert: no lost weapons, no duplicate held meshes, the held mesh is visible at the end of every loop, and the timeout restores the hand in the stuck case.
- **Return-hit test.** Place an enemy on the return path and assert it takes damage when the weapon's return mask says so, and takes none when the weapon is configured harmless. A result that varies run to run means the mask is not fixed.
- **Burst-parent check.** After an impact, free the projectile immediately in the test and assert the burst node still exists under the scene root until its lifetime ends.
- **Decal budget check.** Count live decals after a 30-second combat soak; if the pool is unbounded, cap it (a fixed ring of reusable slots) before the clustered decal budget is shared with lights and probes.

## Valkyrie note

Fit is partial, and the split is clean. What transfers: the whole scripted-projectile pattern (spin, arc, swept hit, burst, return) is exactly what a citizen's thrown spear, axe, or god-hand tool needs, and the sim's deterministic tick pairs naturally with `_physics_process`-driven motion plus a swept query. The state machine also matches Valkyrie's citizen command model: a thrown weapon is a short-lived sim entity with a lifecycle, not a physics toy. What does not transfer: the first-person arms throw animation (Valkyrie's fixed iso camera never sees the wielder's arms; the throw animation must be a full-body citizen animation, authored for the citizen rig, with the projectile spawning at its release frame), and the blood-burst specifics (Valkyrie's painted palette wants a stylized burst, not the creator's red splatter). The return-hit decision matters more here than in a first-person game, because a returning weapon crossing the iso battlefield will pass other citizens: decide explicitly whether it can hit them, and record it in the tuning file.

**Depth status:** PARTIAL (creator's reel read firsthand with all 12 frames; Godot transfer grounded in documentation read firsthand, but not run hands-on in this session; the creator's exact motion logic, spin rate, and recovery rule are unknown and are not claimed here; tuning numbers are this skill's starting points, to be verified by the headless tests above).
