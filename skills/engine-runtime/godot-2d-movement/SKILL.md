---
name: godot-2d-movement
description: >
  Implement 2D kinematic character movement in Godot 4.7 with CharacterBody2D and
  move_and_slide(): platformer run/jump with gravity, top-down 8-direction motion,
  slope handling, and reading collisions. Use when coding a 2D player or enemy
  controller, a platformer or top-down character, or fixing move_and_slide()/
  is_on_floor() behavior in a .tscn with a CharacterBody2D.
---

# Godot 2D Movement (4.x)

Build responsive 2D character controllers with `CharacterBody2D` and the argument-less
`move_and_slide()`. Targets **Godot 4.7**.

## When to use

- Use when scripting a 2D player/enemy that moves and collides: platformer (gravity +
  jump) or top-down (free 8-direction), slope walking, or wall/floor detection.
- Use when `move_and_slide()` "does nothing", the character sinks through floors, or
  `is_on_floor()` is always false.

**When *not* to use:** dynamic rigid bodies, areas, raycasts, collision layers →
`godot-physics`; tile-based levels → `godot-tilemap`; full platformer game template →
the `platformer` genre skill; engine-agnostic feel tuning → `physics-tuning`.

## Core workflow

1. **Use `CharacterBody2D`** with a `CollisionShape2D` child. It is script-driven: it
   does not fall or react to forces on its own.
2. **Set the `velocity` property, then call `move_and_slide()`** (no arguments in 4.x).
   The method reads `velocity`, moves the body, slides along surfaces, and updates
   `velocity` to reflect what actually happened.
3. **Do it in `_physics_process(delta)`** — `move_and_slide()` uses the physics step's
   delta internally, so do not multiply `velocity` by `delta` yourself.
4. **Platformer:** add gravity to `velocity.y` each tick, jump by setting `velocity.y`
   negative when `is_on_floor()`.
5. **Top-down:** build a direction from input and scale by speed; set
   `motion_mode = MOTION_MODE_FLOATING` so there is no "floor/wall" distinction.
6. **Read results** with `is_on_floor()`, `is_on_wall()`, `get_wall_normal()`, and
   `get_slide_collision(i)` after the call.

## Patterns

### 1. Platformer controller (gravity, jump, slopes)

```gdscript
extends CharacterBody2D

@export var speed := 200.0
@export var jump_velocity := -400.0
@export var gravity := 1200.0          # pixels/sec^2 (tune to taste)

func _physics_process(delta: float) -> void:
    # Apply gravity while airborne.
    if not is_on_floor():
        velocity.y += gravity * delta

    # Jump only when grounded (Input action set in Project Settings > Input Map).
    if Input.is_action_just_pressed("jump") and is_on_floor():
        velocity.y = jump_velocity

    # Horizontal input: -1, 0, or 1.
    var dir := Input.get_axis("move_left", "move_right")
    if dir != 0.0:
        velocity.x = dir * speed
    else:
        velocity.x = move_toward(velocity.x, 0.0, speed)   # decelerate to a stop

    move_and_slide()   # 4.x: no arguments; uses and updates `velocity`
```

### 2. Top-down 8-direction movement

```gdscript
extends CharacterBody2D

@export var speed := 220.0

func _ready() -> void:
    motion_mode = CharacterBody2D.MOTION_MODE_FLOATING  # no floor/ceiling concept

func _physics_process(_delta: float) -> void:
    # get_vector returns a normalized-ish Vector2 from four input actions.
    var input := Input.get_vector("move_left", "move_right", "move_up", "move_down")
    velocity = input * speed
    move_and_slide()
```

### 3. Reading slide collisions after moving

```gdscript
func _physics_process(delta: float) -> void:
    # ... set velocity ...
    move_and_slide()
    for i in get_slide_collision_count():
        var c := get_slide_collision(i)
        var other := c.get_collider()
        if other and other.is_in_group("enemies"):
            take_damage(1)        # touched an enemy while moving
```

### 4. Coyote time (forgiving jump just after leaving a ledge)

```gdscript
@export var coyote_time := 0.1
var _coyote := 0.0

func _physics_process(delta: float) -> void:
    if not is_on_floor():
        velocity.y += gravity * delta
        _coyote -= delta
    else:
        _coyote = coyote_time

    if Input.is_action_just_pressed("jump") and _coyote > 0.0:
        velocity.y = jump_velocity
        _coyote = 0.0
    # ... horizontal input + move_and_slide() ...
```

## Pitfalls

- **3.x signature is gone.** `move_and_slide(velocity)` (returning the new velocity) was
  removed. In 4.x set the `velocity` property and call `move_and_slide()` with no args.
  `move_and_slide(velocity, Vector2.UP)` will not parse.
- **Multiplying velocity by delta.** `move_and_slide()` already accounts for the physics
  delta. Setting `velocity = dir * speed * delta` makes the body crawl.
- **Movement in `_process`** instead of `_physics_process` causes frame-rate-dependent,
  jittery motion. Always move in `_physics_process`.
- **`is_on_floor()` always false** when `up_direction` is wrong (default `Vector2.UP`),
  there is no `CollisionShape2D`, or you never called `move_and_slide()` this frame.
- **Sinking through floors** usually means the collision shape is missing/zero-sized, the
  floor body is on a layer this body's mask doesn't include, or you moved the body via
  `position +=` instead of velocity + `move_and_slide()`.
- **Slope slipping while idle:** keep `floor_stop_on_slope = true` (default) and set a
  `floor_snap_length` so the body sticks to downward slopes.

## References

- For one-way platforms, moving platforms, jump buffering, variable jump height, and
  `move_and_collide()` (manual collision response), read `references/controller-recipes.md`.

## Related skills

- `godot-physics` — collision layers/masks, areas, raycasts, rigid bodies.
- `godot-tilemap` — building the levels this character walks on.
- `godot-animation` — driving sprite/skeletal animation from movement state.
- `camera-systems` — follow camera, deadzone, and look-ahead that track this character.
- `platformer` / `input-systems` — full genre template and rebindable input.

## AAA studio practice

Sources:
- Maddy Makes Games, Celeste (designer Maddy Thorson's forgiveness write-up): the shipped platformer widens timing and positioning windows in the player's favor with coyote time (jump still works shortly after leaving a ledge), jump buffering (a press shortly before landing fires on the landing frame), corner correction, and lift momentum storage. https://maddymakesgames.com/articles/celeste_and_forgiveness/
- Game-feel practice in Godot (Manuel Sanchez, with Godot code): coyote time around 0.1 seconds and an input buffer around 0.12 seconds are the paired timers that solve the same "player was almost on time" problem from both sides, and values should be settled by playtesting feel, not by theory. https://www.manuelsanchezdev.com/blog/game-feel-principles-animated-godot

**Do**
1. Add jump buffering alongside the existing coyote-time pattern (Pattern 4): store a buffer timer on jump press, and fire the jump when either the buffer is alive and the body lands, or coyote time is alive. Agent-executable step: implement both timers as exported variables (coyote_time, jump_buffer) so tuning needs no code edit.
2. Automate the forgiveness test: script a headless playtest that presses jump N frames after leaving a ledge and N frames before landing, for N across the window, and logs which presses produce a jump. The pass criterion is that presses inside the window always jump and presses outside never do.
3. Add corner correction as a follow-up pattern [inference from Celeste, not in the original skill]: when a jump bonks a corner, nudge the body sideways by a small amount instead of stopping it dead, and verify with the same headless test at ledge corners.
4. Tune by feel, Celeste style: record a short playtest with each timer value, keep the value only if testers report the jump feeling fair, and log the chosen values in the skill's pattern comments.

**Check**
- Jump buffering and coyote time are both present, both exported, and both covered by the headless timing test.
- The timing test output lists the exact frame window that works, so a regression is visible as a changed window, not a vague "feels off."

**Why**
Celeste's lesson is that a platformer controller is judged by its forgiveness windows, not by its physics accuracy. The existing skill already has coyote time; the AAA addition is the paired buffer, the automated timing test, and tuning by playtest rather than by constant.
