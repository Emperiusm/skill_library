---
name: godot-signals-groups
description: >
  Build event-driven, decoupled Godot 4.7 gameplay with signals and node groups:
  declare and emit custom signals, connect with Callables (incl. bind/one-shot),
  and broadcast to many nodes via groups and call_group. Use when wiring node
  communication in a Godot project, replacing tight references with signals,
  emitting/connecting events, or porting 3.x connect("sig", self, "method") code.
---

# Godot Signals & Groups (4.x)

Decouple nodes with the observer pattern (signals) and act on many nodes at once
(groups), instead of hard-coding references between scenes. Targets **Godot 4.7**.

## When to use

- Use when a node needs to tell others "something happened" (player died, item picked
  up, wave cleared) without holding direct references to them.
- Use when you need to address a whole category of nodes at once ("pause all enemies",
  "save every checkpoint").

**When *not* to use:** raw signal *syntax* basics → `godot-gdscript`; scene structure
and instancing → `godot-nodes-scenes`. For cross-scene global events, emit from an
autoload (see `godot-nodes-scenes`).

## Core workflow

1. **Decide the direction.** A child/sub-scene should *emit* a signal upward; the parent
   *connects* to it. This keeps the child reusable and ignorant of who listens.
2. **Declare typed signals** on the emitter; `emit()` them when the event occurs.
3. **Connect with a Callable** (`sig.connect(_on_sig)`), optionally in the editor's Node
   dock. Use `CONNECT_ONE_SHOT` for fire-once, `bind()` to pass extra context.
4. **Use groups for broadcast**: add nodes to a named group, then iterate
   `get_tree().get_nodes_in_group(...)` or `call_group(...)`.
5. **Disconnect when needed** (e.g. before freeing a long-lived listener) and check
   `is_connected()` to avoid duplicate connections.

## Patterns

### 1. Emit upward, connect from the parent

```gdscript
# coin.gd (reusable pickup — knows nothing about the player or HUD)
extends Area2D
signal collected(value: int)

func _on_body_entered(body: Node) -> void:
    if body.is_in_group("player"):
        collected.emit(10)
        queue_free()
```

```gdscript
# level.gd (the parent wires the coin to game state)
func _ready() -> void:
    for coin in get_tree().get_nodes_in_group("coins"):
        coin.collected.connect(_on_coin_collected)

func _on_coin_collected(value: int) -> void:
    GameState.add_score(value)
```

### 2. Connect flags: one-shot and bind extra arguments

```gdscript
func _ready() -> void:
    # Fire exactly once, then auto-disconnect.
    $Door.opened.connect(_on_door_opened, CONNECT_ONE_SHOT)
    # bind() appends arguments supplied at connect time (after the signal's own args).
    $RedButton.pressed.connect(_on_button.bind("red"))

func _on_button(color: String) -> void:
    print("Pressed the %s button" % color)
```

### 3. Groups: broadcast to many nodes

```gdscript
func pause_all_enemies() -> void:
    # Call a method on every node in the "enemies" group (no-op if missing).
    get_tree().call_group("enemies", "set_paused", true)

func count_enemies() -> int:
    return get_tree().get_nodes_in_group("enemies").size()
```

Add a node to a group from code or via the editor's Node > Groups tab:

```gdscript
func _ready() -> void:
    add_to_group("enemies")        # remove_from_group("enemies") to leave
```

### 4. Await a signal inline

```gdscript
func open_chest() -> void:
    $AnimationPlayer.play("open")
    await $AnimationPlayer.animation_finished   # pause until it emits
    spawn_loot()
```

## Pitfalls

- **3.x connect signature is gone.** `connect("died", self, "_on_died")` →
  `died.connect(_on_died)`. The target is implied by the Callable. The legacy
  `Object.connect("died", Callable(self, "_on_died"))` works but the method-name string
  form does not.
- **Duplicate connections fire handlers multiple times.** Connecting again in `_ready()`
  after re-adding a node stacks callbacks. Guard with
  `if not sig.is_connected(cb): sig.connect(cb)`.
- **Connecting to a freed node errors.** Disconnect long-lived listeners, or rely on
  Godot auto-disconnecting when the *connected object* is freed (it does for nodes).
- **Groups are global to the SceneTree**, not per-scene. Two levels using the same group
  name share membership. Namespace group names if that matters.
- **`call_group` silently ignores nodes lacking the method.** Typos in the method name
  fail quietly — prefer a typed signal when the contract matters.
- **Signal args must match.** Emitting with the wrong arg count/types raises an error;
  declare typed params and emit exactly those.

## AAA studio practice

- **Observer pattern: producers must not know their consumers.** The
  observer pattern's production value is that subjects register observer
  callbacks and notify them when an event occurs, without the subject knowing
  who is listening; a gate, a UI element, and a quest tracker can all react
  to "player entered arena" independently, and deregister when they no longer
  care (e.g. after the boss is defeated, the gate stops locking).
  Source: https://shaggydev.com//2022/06/01/observer-pattern/
- **Event contracts are APIs: breaking one silently breaks unknown consumers.**
  Event-driven-architecture guidance stresses that producers publish events
  without knowing whether one, ten, or zero consumers listen, that adding a
  consumer requires no producer code change, and that once an event is
  published it becomes an API, so changing its arguments can silently break
  downstream consumers the publisher does not know about. Debugging also
  gets harder because cause and effect are separated in time.
  Source: https://www.conduktor.io/glossary/event-driven-architecture
- **Apply Rare's test discipline to events (cross-reference).** Rare's
  Sea of Thieves automated-testing practice (see
  `godot-gdscript-headless-testing`) ran tests constantly so regressions in
  behaviour were caught the day they appeared; the same discipline applies
  to signal contracts, which otherwise rot silently.
  Source: https://www.gamedeveloper.com/production/-i-sea-of-thieves-i-devs-share-automated-testing-tips-at-gdc-2019

Agent-executable steps (Do / Check / Why):

- Do: treat every signal declaration as a versioned contract: typed
  parameters (Pattern 1), a comment stating what the signal means and when
  it fires, and no argument changes without updating every connected handler
  in the same change. Renaming a signal or changing its args is a
  breaking-change commit, labelled as such.
- Do: prefer signals over `call_group` whenever the contract matters
  (Pitfalls already warns `call_group` silently ignores missing methods):
  use groups only for best-effort broadcast ("pause all enemies"), and
  signals for anything where a missed delivery is a bug ("player died").
- Do: add a headless test that instantiates the emitter, connects a counting
  handler, triggers the event, and asserts the handler fired exactly once
  with the expected arguments; add a second test that disconnects (or frees)
  the listener and asserts no duplicate or stale firing on a second trigger.
  This catches the duplicate-connection pitfall as a regression, not as a
  playtest anecdote.
- Check: (1) grep for `call_group` uses and confirm each is best-effort, not
  contractual; (2) every signal has typed params and a contract comment;
  (3) the event test suite passes, including the disconnect case.
- Why: decoupling only pays off if the contract is stable and tested.
  Untyped, undocumented signals plus silent `call_group` failures give you
  the debugging cost of event-driven architecture with none of its
  independence.

## References

- For connection flags, deferred connections, custom signal arguments, awaiting with
  timeouts, and signals vs. direct calls trade-offs, read `references/signal-patterns.md`.

## Related skills

- `godot-gdscript` — signal/`await` syntax fundamentals.
- `godot-nodes-scenes` — autoloads for global event buses.
- `game-ai` — state machines that often drive and consume these events.
