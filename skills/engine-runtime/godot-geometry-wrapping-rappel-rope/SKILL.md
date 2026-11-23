---
name: godot-geometry-wrapping-rappel-rope
description: "Add a geometry-wrapping rappel rope in Godot: fake the last Curve3D segment as a tension-pulling pivot or pendulum, wrap it with physics shape casts, and clamp every non-input force along the rope axis. Trigger when a player must rappel from an anchor and the rope must wrap and unwrap around level geometry without a RigidBody3D simulation."
---

# Godot Geometry-Wrapping Rappel Rope

## Purpose

This skill reconstructs the exact workflow AsyncInvestigations demonstrates for a rappel rope that wraps around level geometry, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: fake the last segment of a geometry-wrapped `Curve3D` as a tension-pulling pivot or pendulum, and let physics state queries, not rigid-body motion, decide where the rope wraps.

## Source

Creator: AsyncInvestigations. Post: "I added geometry-wrapping rope the player can rappel from and here is how I did it:" https://www.reddit.com/r/godot/comments/1y341pv/i_added_geometrywrapping_rope_the_player_can/ (r/godot post 1y341pv, score 41, 3 comments; full post text read) | 2026-11-23 scout run, audit 2.

## Tools used

Godot (version unstated; the scripting language is not named by the author — every API and class name below is Godot's). `Curve3D`, `RayCast3D`, `PhysicsDirectSpaceState3D.get_rest_info()`, capsule colliders, `MeshInstance3D`.

## Phase 1: Decide against a fully physics-based rope

**Do**
1. Test a fully physics-based rope that relies on `RigidBody3D` motion, then reject it.
2. Fake "the last segment of a geometry-wrapped Curve3D as a tension-pulling pivot or pendulum depending on player state" instead.

**Check**
- The deciding test is anchoring against movable objects: the author "wanted the anchor and move-able objects the rope wraps against to remain solid and prevent unexpected jumps in rope length at tension thresholds".

**Why**
The stated reason is determinism of rope length at tension thresholds. Freezing everything was the alternative the author rejected; the `Curve3D` plus shape-cast route avoids it while keeping anchors solid. No performance reason is stated; do not invent one.

## Phase 2: Anchor with a raycast against the `anchorable` group

**Do**
1. Cast a `RayCast3D` from the player camera to get anything in the group `anchorable`, including physics objects.
2. Start the curve with 2 points: the anchor and the player.

**Check**
- The anchor must be a member of `anchorable`. Anything outside the group is not anchorable by this cast.

**Why**
The raycast from the camera makes the anchor the thing the player is looking at, and the group gate is what keeps non-anchor geometry out of the rope system.

## Phase 3: Sync a capsule collider and mesh to every rope segment, every frame

**Do**
1. "Every frame my code counts the rope segments and creates or moves a capsule collider to line up with it."
2. "It simultaneously syncs a `MeshInstance3D` to render the capsule."
3. Put the shapes in the default physics engine on "a single `collision_mask` layer to let the player grab on to and let go of the rope", and reuse the shapes for shape-cast queries.

**Check**
- Collider and visible mesh must line up segment-for-segment each frame. A mismatch would show as the rope rendering somewhere the player cannot grab, or vice versa. The author states the sync, not a numeric tolerance.

**Why**
One shape serves three jobs (collision for the player, rendering, and the shape-cast queries in Phase 4), so the rope's visual, physical, and query representations cannot drift apart.

## Phase 4: Wrap the curve by shape-casting the last segment

**Do**
1. Each frame, take "the adjacency collision shape that's synced to the last rope segment" and run a `PhysicsDirectSpaceState3D.get_rest_info(query)` query.
2. "If it returns a collision with geometry I insert a new path control point offset from said point by the rope radius in the direction of the collision normal."
3. As the player moves around level geometry, "the rope they are attached to cleanly splits so they always have direct line of sight to the pivot".

**Check**
- Line of sight to the pivot is the invariant: the split must preserve a direct line from player to pivot at all times.

**Why**
The author states the purpose directly: "This is important because I'm faking tension by capping player velocity on the axis of the last curve segment." Wrapping is what makes the fake tension axis follow the geometry instead of cutting through it.

## Phase 5: Clamp all non-input forces along the rope axis, and fake the pendulum

**Do**
1. "I only let the player extend or contract the rope with direct input velocity. Any other forces on the player are fully clamped along the rope's axis."
2. Check the unwrapping condition every frame "by shapecasting between the player's harness and the point at `pivotIndex-1`. If its empty, remove the active pivot from the curve and swap the pivot index."
3. "I also check for unwrapping along the length of the rope with the casts debounced to 3 per frame."
4. Add "a centering force when the player is hanging below the pivot. This acts like a pendulum by taking the `sin` of the angle of the gravity vector and applying it tangent to the pendulum arm." The author links the standard pendulum model (Wikipedia, Pendulum (mechanics)) for the diagrams.

**Check**
- Unwrap only when the harness-to-`pivotIndex-1` shapecast is empty. The 3-per-frame debounce bounds the unwrap checks along the rope's length.
- The pendulum check is the hanging-below-pivot state; the centering force applies only then.

**Why**
Clamping every non-input force along the axis is what makes the fake tension hold: nothing else is allowed to stretch or slacken the rope except the player's own extend/contract input. The `sin` centering force is the pendulum behaviour.

## Failure modes

- **Rope length jumps at tension thresholds:** the failure the author designed against by rejecting the `RigidBody3D` route. If rope length jumps, check whether anchors or wrapped objects are moving under physics instead of remaining solid.
- **Rope cuts through geometry:** the wrapping query in Phase 4 is not inserting control points. Check that the adjacency shape is synced to the last segment and that the new point is offset by the rope radius along the collision normal.
- **Pivot lost behind geometry:** the line-of-sight invariant in Phase 4 is broken. The curve must split so the player always has direct line of sight to the pivot.
- **Movable objects supporting the player's weight:** unanswered in the source. A commenter asks: "Are the objects touched by the rope affect by physics? I feel like the chair shouldn't be supporting the player's weight." The author did not answer. Do not assume the rope moves objects; the post says anchors and movable objects "remain solid".
- **Unwrap checks costing too much per frame:** the author's bound is 3 unwrap casts per frame along the rope's length. No frame-time benchmark is stated.

## The human method, distilled

1. "Godot's static physics state queries make it surprisingly easy." Query the physics state directly (`get_rest_info`, shape casts) instead of building a physics simulation and fighting it.
2. Fake the one segment that matters (the last, tension-bearing segment) and let queries handle the rest (wrapping, unwrapping).
3. Bound the per-frame work explicitly: unwrap casts "debounced to 3 per frame".

**Depth status:** FULL. Complete written breakdown with exact API names, group name, debounce count, and the pendulum rule, from the author's full post text. Missing only: Godot version, rope radius value, frame-time benchmarks, and the answer to the movable-objects question.
