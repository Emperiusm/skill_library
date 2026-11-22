---
name: forward-trace-melee-attack-gating
description: "Stop first-person swords and arms clipping through walls and trees: a forward trace from the player that gates the swing when static geometry blocks it, rebuilt from an Unreal Blueprint reel as a Godot 4 workflow with PhysicsRayQueryParameters3D, collision-layer separation, shape-cast upgrades for wide swings, and debug-drawn traces. Trigger when a melee swing, weapon viewmodel, or interaction check needs to know whether a wall is in the way before it fires."
---

# Forward-trace melee attack gating

## Purpose

This skill reconstructs the wall-clipping fix from a 20-second indie reel end to end, step by step, so another agent can follow the same process in Godot. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: prove the clip, trace forward from the player against static geometry only, and let the trace result decide whether the swing fires, with the trace itself drawn on screen so the check is visible.

The reel's fix is a gate, not a hit test. The trace asks one question, "is a wall in the way?", and the swing only fires when the answer is no. Hitting the enemy is a separate system that runs after the gate passes.

## Source

Creator: beforethesunsets44 (game: Before the Sun Sets, an Unreal Engine first-person fantasy melee game). Instagram reel: https://www.instagram.com/reel/DexAg9wh9FL/ (posted Oct 21, 2026, 27 comments). Caption: "fixing clipping in my game.." Full local transcription (faster-whisper tiny), 12 frames read firsthand, work dir `~/workspace/custom-skills/local-video-summarizer/work/bts-DexAg9wh9FL/`.

What the reel shows, in order: the bug (first-person sword and arm clipping straight through tree trunks), the fix (an Unreal Blueprint in the player character: Get Actor Location, forward vector multiplied by 100.0, a Make Array holding WorldStatic, a Line Trace For Objects node, feeding a Branch that gates the attack), the example (a knight in front of the player, attack allowed), and the contrast (red debug trace lines stopping at a tree trunk, captioned "BLOCKED."). The creator's own rule, from the narration: an enemy in front can be hit, but a tree or wall in the way blocks the attack.

What the reel does **not** show: the world distance the 100.0 multiplier represents, the channel setup beyond WorldStatic, what the blocked swing looks like (no blocked animation is visible in the stills), whether the check runs once at attack start or continuously through the swing, or any performance numbers or edge cases. This skill never fills those gaps with invented numbers; every Godot value below that is not the creator's is labeled as this skill's recommendation.

Related reel from the same account, same week, same idea in reverse: De7iNqYhFyY (Oct 25, "Blocking arrows glitch") shows a sword block creating an invisible wall that stops arrows, which the creator put to a viewer vote. It is background, not this skill's source.

## The reel's fix, reconstructed (Unreal side)

The Blueprint, node by node, as read from the reel's frames:

1. **Get Actor Location**: the trace starts at the player's actor location.
2. **Forward Vector x 100.0**: the trace direction is the player's forward vector, scaled by 100.0. That 100.0 is in the reel's Unreal units; the reel never states the world distance, and this skill does not convert it.
3. **Make Array [WorldStatic]**: the object-type filter holds exactly one entry, WorldStatic (static geometry: walls, floors, trees). Enemies are not in the array, so an enemy in front never blocks the trace.
4. **Line Trace For Objects**: a single trace from start to end against that object list. Unreal's object-based traces (the `LineTraceSingleForObjects` family) test against object types rather than trace channels; WorldStatic is the object type for static geometry.
5. **Branch**: hit means blocked (do not attack); no hit means clear (attack fires).

The Godot translation of each node is Phase 2 and Phase 3. The structure is identical; only the API names change.

## Ray vs shape cast: pick the right one

A ray is a line with no thickness. A sword swing is a wide arc. The reel uses a ray because its question is narrow ("is anything directly ahead?"), and that is the right call for a forward gate. It is the wrong call for detecting what a wide swing actually hits.

- Use a **ray** (`intersect_ray`) for the gate: one forward check, cheapest query, exactly the reel's fix. It answers "blocked or clear" and nothing else.
- Use a **shape cast** (`ShapeCast3D`, or `intersect_shape` / `cast_motion`) when the swing itself needs volume: a box or sphere swept along the swing arc, so a blade that passes beside a thin post still registers the post. The Godot docs note shape casting is more computationally expensive than ray casting; pay for it only where the swing is wide.
- Never use the gate ray as the hit test. A ray down the middle of the swing misses enemies at the edges of the arc, and a shape cast used as a gate blocks swings that would have cleared the wall by a hand's width. One query per job.

## Tools used

Godot 4.x (verified against the 4.4/4.3 class docs; the query API below is unchanged across 4.x), GDScript or C# (Valkyrie uses C#; both spellings are given in Phase 3), and one debug-drawing route from Phase 6 (ImmediateMesh, or the Debug Draw 3D addon). No other plugin is required. The sibling skill `engine-runtime/godot-physics` covers raycast mechanics in general; this skill covers only the gating workflow, and defers to it for RayCast3D node basics.

## Phase 1: Reproduce the clip before fixing anything

**Do**
1. Build a repro scene: a flat floor, one tree trunk or wall segment, and the player standing close enough that the sword viewmodel or arm mesh overlaps the trunk when the swing plays. No enemies, no UI, no other systems.
2. Stand the player against the trunk, face it, and play the swing. Watch the blade pass through the trunk.
3. Save this scene as the regression test. It stays in the project permanently; every later phase is verified against it.

**Check**
- The clip is visible from the player's own camera, not just from a side view. The reel's opening frames make the same point: the trunk fills the screen, which is how the player experiences it.
- The swing clips in exactly one repeatable spot (facing the trunk, at arm's length). If it clips everywhere, the viewmodel placement is wrong, not the gate; fix the placement first.

**Why**
- A fix without a repro is unverifiable. The repro scene is also the demo the reel's presentation uses: problem first, then code, then example, then contrast. Keep that order whenever this fix is shown to anyone.

## Phase 2: Separate static geometry from enemies on collision layers

**Do**
1. Put all static geometry (walls, floors, trees, rocks, props that never move) on one collision layer. Call it `world`. Put enemies on a different layer. Call it `enemy`. Put the player body on a third layer. These are this skill's recommended names, not the creator's; the creator's equivalent is the WorldStatic object-type entry.
2. On every static body, confirm the layer is set and the body actually blocks queries (a body on the layer with monitoring off or collision disabled still will not register; check the body's collision settings, not just the layer number).
3. Write the layer numbers down in one place (project settings layer names, or a constants file). The gate query in Phase 3 references the `world` layer by mask, and a renumbered layer silently breaks it.

**Check**
- With the player facing the trunk, a test trace with the `world`-only mask hits the trunk. With the player facing an enemy standing in open ground, the same trace passes straight through the enemy and hits nothing. If the enemy blocks the trace, the mask includes the enemy layer: fix the mask, not the trace.
- The player's own body never appears in the trace. If it does, the exclude list in Phase 3 is missing.

**Why**
- The reel's entire fix rests on the filter containing WorldStatic and nothing else. The Godot equivalent is a mask, and a mask that includes enemies turns the gate into a bug: enemies would block their own attacks. The filter is the fix; the trace is just the delivery mechanism.

## Phase 3: The forward trace that gates the swing

**Do**
1. Run the query inside `_physics_process`, never inside `_process` or an input callback. Direct space-state queries touch the physics server directly; the docs tutorial runs them in `_physics_process`, and querying outside physics processing risks thread crashes or stale space state. For an attack triggered by input: set a flag in the input handler, consume the flag in `_physics_process`, and run the trace there.
2. Build the query from the player's position at chest or weapon height, along the player's forward direction, for the weapon's reach. The reel traces from the actor location (feet-level origin) along the forward vector; in Godot a horizontal ray from the feet hits steps and low obstacles, so raise the origin to the weapon. Reach is this skill's recommendation, not the creator's number: start at 1.0 m and tune it to the weapon's length plus a hand's width, so the gate trips just before the blade would touch the wall.
3. Exclude the player's own body from the query, and set the mask to the `world` layer only. Set `collide_with_areas` false (the default) unless a blocking Area is part of the level design.
4. Gate the swing on the result: empty result means clear, fire the swing. Non-empty result means blocked, do not fire. The reel's behavior is a hard cancel; the alternatives (shorten, deflect, pull back) are Phase 4, and none of them is the reel's behavior.

GDScript (primary spelling; API verified against the Godot 4.4 class docs):

```gdscript
func is_swing_blocked() -> bool:
    var space_state := get_world_3d().direct_space_state
    var from := global_position + Vector3(0.0, 1.2, 0.0) # chest height; tune to the weapon
    var to := from - global_transform.basis.z * reach # reach is this skill's recommendation, start 1.0
    var query := PhysicsRayQueryParameters3D.create(from, to, world_mask, [get_rid()])
    var result := space_state.intersect_ray(query)
    return not result.is_empty()
```

C# (same query; names verified from Godot C# API usage in the wild):

```csharp
public bool IsSwingBlocked(float reach, uint worldMask)
{
    var spaceState = GetWorld3D().DirectSpaceState;
    var from = GlobalPosition + new Vector3(0f, 1.2f, 0f);
    var to = from - GlobalTransform.Basis.Z * reach;
    var query = PhysicsRayQueryParameters3D.Create(from, to, worldMask, new Godot.Collections.Array<Rid> { GetRid() });
    var result = spaceState.IntersectRay(query);
    return result.Count > 0;
}
```

The result dictionary, when a hit occurs, carries `position` (the intersection point), `normal` (the surface normal), `collider` (the object hit), `collider_id`, `rid`, `shape`, and `face_index` (a real number only for ConcavePolygonShape3D, otherwise -1). An empty dictionary means no hit. Read `position` and `normal` in Phase 4; ignore the rest for the gate.

**Check**
- Facing the trunk at arm's length: the query returns a hit, the swing does not fire. Facing the knight in open ground: the query returns empty, the swing fires. Facing nothing: empty, fires. All three cases are checked in the repro scene from Phase 1, from the player's camera.
- The trace fires once per swing attempt, not once per frame while the button is held. If it runs every frame, a wall the player walks past mid-swing cancels swings that already started; that is a different behavior from the reel's, and it reads as broken input.

**Why**
- The gate must be cheap, deterministic, and testable. One query, one mask, one branch, in physics processing: that is the whole mechanism, and anything added to it (continuous checks, multiple rays, per-bone traces) needs its own justification, not momentum.

## Phase 4: Decide what "blocked" does (cancel is the reel; the rest are upgrades)

**Do**
1. Ship the reel's behavior first: blocked means the swing does not fire at all. Give the player feedback that the input registered but was refused: a short weapon-lower or recoil animation, a dull thud sound, or a brief haptic pulse. The reel shows no blocked feedback in its stills; the absence is a gap, not a design choice, and a silent refused input feels like a dead button.
2. Only after the cancel reads correctly, consider one upgrade, and only one:
   - **Shorten:** use the hit `position` from Phase 3 to clamp the swing's reach, so the blade stops at the wall instead of never moving. Needs a swing that can be parameterized by reach; a baked animation cannot be shortened without retargeting.
   - **Deflect:** play a spark/ricochet effect at the hit `position` along the hit `normal`, and cancel the swing. Cheap, readable, and the normal is already in the result dictionary.
   - **Pull back:** move the viewmodel toward the player as the wall approaches (the spring-arm trick from the shipped-practice section below), so the weapon never visually enters the wall even between gate checks.
3. Never stack two upgrades in one pass. Each one changes the feel, and stacked changes cannot be attributed when the feel is wrong.

**Check**
- Blocked at the wall: the player sees or hears something within one frame of pressing attack. No feedback means the gate is indistinguishable from a dropped input, which players report as a bug.
- The upgrade, if added, is visible in the repro scene: shorten shows the blade stopping at the trunk, deflect shows the effect at the trunk's surface, pull-back shows the weapon sliding toward the camera as the player approaches.

**Why**
- A gate that silently eats input is a new bug wearing a fix's clothes. The reel's contribution is the check, not the response; the response is where the game's feel lives, and it needs its own verification.

## Phase 5: Wide swings need a shape cast, not a longer ray

**Do**
1. Identify the failure a ray cannot see: a swing whose arc passes beside a thin post. The center ray clears the post, the blade's edge clips it. Reproduce it in the repro scene with a thin trunk offset half a blade-width from the trace line.
2. Replace the gate query for wide swings with a shape cast: a box matching the blade's swept volume, swept forward along the swing direction. Node route: a `ShapeCast3D` with its `shape` set (a BoxShape3D sized to the blade), `target_position` set in the node's **local** space, and `force_shapecast_update()` called within the physics frame; read `get_closest_collision_safe_fraction()` (0 to 1, how far the shape travels before hitting) to decide blocked vs clear. Code route: `PhysicsShapeQueryParameters3D` (shape, transform, motion, margin) with `intersect_shape`, or `cast_motion`, which returns the safe and unsafe proportions of the motion directly.
3. Keep the ray gate for narrow thrusts and the shape gate for wide swings. Do not replace every ray with a shape cast: the docs state shape casting is more computationally expensive than ray casting, and a gate that runs once per swing attempt does not need volume for a straight stab.

**Check**
- The thin-post case: the shape gate reports blocked where the ray gate reported clear, and the blade no longer clips the post. The straight-ahead trunk case still blocks under both gates.
- The shape cast's `target_position` is local. A global-space target assigned directly sends the cast in the wrong direction whenever the node is rotated; this is the most-reported ShapeCast3D mistake, and it looks like the cast "going all over the place". Convert with `to_local()` or keep the node unrotated and set the target once.

**Why**
- A ray answers a point question; a swing is a volume question. Matching the query's shape to the action's shape is the same principle as the layer filter in Phase 2: the query must test what the player actually does, not a convenient approximation of it.

## Phase 6: Draw the trace, the way the reel's red lines do

**Do**
1. Draw every gate query on screen while developing: a line from the trace origin to the trace end, green when clear, red when blocked, ending at the hit `position` when there is one. The reel's final frame is exactly this: red lines stopping at the trunk, captioned "BLOCKED." Copy that presentation; it is the fastest way to see the check working.
2. Godot has no built-in immediate-mode 3D debug-draw API, so build the line yourself or add the addon. No-plugin route: an `ImmediateMesh` on a `MeshInstance3D`, rebuilt every frame (`clear_surfaces()`, `surface_begin(Mesh.PRIMITIVE_LINES)`, two `surface_add_vertex` calls, `surface_end()`), with an unshaded material and shadows off. Addon route: Debug Draw 3D (C++ GDExtension, GDScript and C# wrappers, autoload singleton; `DebugDraw.draw_line(begin, end, color)` in GDScript, `DebugDrawCS.DrawLine(...)` in C#), remembering to swap in its dummy autoload before export so debug calls cost nothing in release builds.
3. Gate all debug drawing behind a debug-only flag (debug builds, or a developer console toggle). It must never ship in a release build, and it must never be the only way to see the gate: the Phase 4 feedback is the shipped signal, the drawn line is the developer's.

**Check**
- Facing the trunk: a red line from the player stops exactly at the trunk's surface, at the `position` the query returned. Facing open ground: a green line runs the full reach. If the red line stops short of the surface or past it, the drawn endpoints do not match the query endpoints; fix the drawing, not the query.
- With debug drawing off, the gate still works identically. If behavior changes, game logic is reading debug state; remove the dependency.

**Why**
- The reel proves its fix visually, in one frame, with no narration needed. A drawn trace does the same for the developer: the check is either visibly correct or visibly wrong, and no amount of logging replaces seeing the line stop at the wall.

## The human method, distilled

1. **Problem, code, example, contrast.** The reel's presentation order is the method: show the clip, show the fix, show it working on an enemy, show it blocking on a wall. Use the same order for every fix demo.
2. **The filter is the fix.** WorldStatic-only in the reel, world-layer-only here. A trace with the wrong filter is worse than no trace, because it looks correct while blocking the wrong things.
3. **One query per question.** Gate ray for "blocked?", shape cast for "what does the swing sweep?", hit test for "what did it hit?". Never one query doing two jobs.
4. **Prove it from the player's camera.** The trunk filling the screen is the bug report; the red line stopping at the trunk is the fix report. Side views are for debugging, never for verdicts.
5. **A refused input needs feedback.** A gate without a signal reads as a dead button. The check is the engineering; the thud, spark, or lowered weapon is the design.

## Failure modes

- **Enemies block their own attacks.** The mask includes the enemy layer. Fix: mask to the world layer only (Phase 2). The reel's array holds WorldStatic alone; anything else in the filter is a deviation, not an improvement.
- **The player blocks their own trace.** The exclude list is missing, so the ray hits the player's own body at zero distance and every swing is refused. Fix: exclude the player's RID (Phase 3). Symptom: the gate reports blocked while facing open ground.
- **The ray starts inside the wall.** The player is already touching the trunk when they attack; with `hit_from_inside` false (the default), a ray starting inside a shape reports no hit, the swing fires, and the blade clips. Fix: start the ray a short distance behind the player, or add an overlap check at the origin; test this case explicitly in the repro scene by walking into the trunk before attacking.
- **The trace runs in `_process`.** Stale space state, wrong results, or thread crashes. Fix: query in `_physics_process` only, with input flags consumed there (Phase 3).
- **ShapeCast3D target in global space.** The cast goes in the wrong direction whenever the node is rotated. Fix: `target_position` is local; convert with `to_local()` (Phase 5).
- **Thin posts clip the blade's edge.** The center ray clears them. Fix: shape cast for wide swings (Phase 5), not a longer ray.
- **A layer renumber silently breaks the gate.** Masks are numbers; renaming or reordering layers changes what the mask means. Fix: named layer constants in one place, and the Phase 2 check (enemy must not block, trunk must) run after any layer edit.
- **Silent refused input.** The gate works, the player thinks the button is broken. Fix: Phase 4 feedback, verified within one frame of the press.
- **Debug drawing ships in release.** Fix: debug-only flag, and the dummy autoload swap for the addon route (Phase 6).

## AAA studio practice

No studio publishes a "melee wall gate" paper; the shipped answers below come from working developers answering the same bug on the Epic forums, and they agree on one honest point: most games do not eliminate all clipping, because a capsule controls where the body goes, not where animated limbs go. The standard is a combination of collision checks, animation state changes, and IK, applied where the player looks.

- **Spring-arm pullback (Unreal forums, the most-recommended fix).** Attach the first-person arms to a Spring Arm with collision testing on; the arm shortens itself when it touches anything, pulling the weapon back smoothly, and lengthens as space allows. One spring arm per arm is recommended, with the arm mesh placed behind the arm's end so it retracts early. This is the Phase 4 pull-back upgrade, and it handles the between-checks cases a gate cannot.
- **Line trace plus a raise/lower animation (Unreal forums).** Trace forward; when a wall is hit, blend to a "weapon lowered" or "arm raised 90 degrees" animation, driven by the hit distance. Same check as the reel, different response: the weapon visibly adapts instead of refusing.
- **Render the weapon on a separate layer (Source engine, Robo Recall).** The first-person weapon renders in front of everything, so it never visibly clips; the clip still happens geometrically, but the player never sees it. A presentation fix, not a collision fix, and it reads wrong the moment another player or a mirror can see the weapon.
- **IK and Control Rig (Unreal forums, current answers).** FABRIK or Two Bone IK adjusts hands and feet when they approach walls; physics assets on specific bones handle cloth and accessories. IK fixes the limb, not the swing, so it complements the gate rather than replacing it.
- **Animation design as the fallback (Unreal forums).** Alternate animations (wall idle, corner lean, weapon lowered) triggered by the same line-trace or overlap check. When the check cannot decide cleanly, a context animation hides the ambiguity.
- **The reel's own presentation is the stealable artifact.** Problem, readable code, working example, blocked contrast, one-word captions pacing each beat, in 20 seconds. It is the format to copy for every fix demo, including this skill's Phase 1 repro scene.

Sources: "Weapon Clipping Through Wall", Epic Developer Community Forums, https://forums.unrealengine.com/t/weapon-clipping-through-wall/464600 ; "How to prevent a character's animation from clipping through objects", Epic Developer Community Forums, https://forums.unrealengine.com/t/how-to-prevent-a-characters-animation-from-clipping-through-objects/2738129 ; "How to prevent weapons from penetrating the wall?", Epic Developer Community Forums, https://forums.unrealengine.com/t/how-to-prevent-weapons-from-penetrating-the-wall/303378

## Agent automation

- **Layer gate.** A scene-validation script reads the gate query's mask and the project's layer names, and fails when the mask includes the enemy layer, when the world layer has no static bodies, or when any static body sits on the wrong layer. Layer edits re-run this gate automatically.
- **Trace gate.** A headless test scene (the Phase 1 repro) runs three scripted cases: trunk ahead blocks, enemy ahead in open ground does not block, open ground does not block. Any case failing fails the build. The trace length used in the test is recorded in the test, not assumed.
- **Origin-inside gate.** A fourth scripted case: the player starts overlapping the trunk, then attacks. The expected result is blocked (or the overlap check fires); a fired swing is a fail.
- **Debug-draw gate.** A release-build check fails if any debug-draw call or ImmediateMesh debug node remains active outside debug-only flags.
- **Swing-coverage gate.** For each swing in the game, record whether it uses the ray gate or the shape gate, with the reason (narrow thrust vs wide arc). A swing with neither recorded is a fail; the fix is a decision, not a default.
- **Presentation gate.** Every fix demo follows the reel's order (problem, code, example, contrast) and is recorded from the player's camera. A demo recorded from a side view does not count as verification.

## Valkyrie note

Valkyrie is a fixed-iso god game, not a first-person melee game, so the clipping problem itself does not transfer: there is no first-person arm, no viewmodel, and no camera pressed against a trunk. What transfers is the pattern, and it transfers to three Valkyrie systems:

1. **Citizen interactions.** A citizen ordered to chop, mine, or attack walks to a target and acts; a forward trace from the citizen against the world layer, run before the action starts, answers "can the citizen reach this, or is a wall, rock, or building in the way?" before the swing animation plays into the obstacle. Same gate, third-person actor, same branch.
2. **God-hand tools.** Placement and terrain tools that project from the cursor into the world already trace; the gate pattern (static-only mask, drawn trace, blocked feedback) is the check that a placement preview is legal before the player commits it.
3. **The presentation.** The reel's problem/code/example/contrast order is the devlog format that works for Valkyrie's crowd and terrain work too, and it is cheap: one repro scene, one visible check, one contrast shot.

Do not import the first-person specifics: no viewmodel pullback, no raised-weapon blend, no feet-level trace origin. The gate is the transferable part; the first-person response is not.

## Comment-thread evidence (first-page comments, verified in raw JSON)

- **The corner case the creator endorsed.** Commenter Archanger asked: "What if you are next to a corner or a tree and try to attack an enemy Infront of you and you just cant". The creator replied: "thats a great point!!" A pure forward gate has a real failure mode: standing against a wall or tree with an enemy just past it, the player cannot attack at all. The skill's answer is the shape-cast upgrade plus the angled-trace fallback in the failure modes: when the center trace is blocked but a slightly angled trace reaches the enemy, allow the swing (or shorten it) instead of hard-blocking. Do not ship a gate that can soft-lock the player against geometry.
- **The community's preferred fix is bounce-off feedback.** Ktos: "Or maybe make it bounce off? Just a suggestion". Sayori: make attacking an obstacle play "an animation of the sword like sparking and bouncing off". Falltimester: "just make it bounce off rather than creating a new problem". An anonymous commenter proposed the fuller version: a first-person render layer so arms always draw over the world, plus a trace mid-attack, then a bounce-off animation. The blocked-swing feedback phase in this skill (spark burst, recoil animation, sound) is the Godot form of that consensus: a blocked attack must read as a physical bounce, never as a dead input.
- **What the gate must not become.** The same thread shows the failure the gate is fixing (clipping) is less hated than a gate that feels restrictive. Keep the gate narrow (static geometry only, enemy hits always pass), the feedback loud, and the fallback angled trace in place, or players will read the fix as the bug.

Coverage note: comment fetches return a first page only (23 of 27 read on this reel). Later pages may hold more.

**Depth status:** PARTIAL (reel read firsthand with all 12 frames and the Blueprint nodes legible on screen; Godot query, shape-cast, and debug-draw APIs verified against the Godot class docs and reputable sources cited above, but the Godot path has not been run hands-on in this session; no performance numbers exist for the gate, the reel provides none, and none are claimed here).
