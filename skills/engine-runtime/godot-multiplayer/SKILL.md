---
name: godot-multiplayer
description: >
  Build networked games with Godot 4.7 high-level multiplayer: set up an
  ENetMultiplayerPeer server/client, define RPCs with the @rpc annotation
  (call via rpc()/rpc_id()), set per-node multiplayer authority, and replicate
  state with MultiplayerSpawner and MultiplayerSynchronizer. Use when adding
  multiplayer/networking to a Godot project, writing @rpc functions, or syncing
  player/world state across peers.
---

# Godot Multiplayer (4.x high-level)

Connect peers, call functions remotely with `@rpc`, assign authority, and replicate state
with `MultiplayerSpawner`/`MultiplayerSynchronizer`. Targets **Godot 4.7** (ENet). Treat
all client input as untrusted; keep the server authoritative.

## When to use

- Use when adding networked multiplayer: hosting/joining over ENet, calling RPCs,
  assigning per-node authority, or auto-spawning/syncing nodes across peers.

**When *not* to use:** local split-screen (no networking); raw TCP/UDP/WebSocket protocol
work (low-level `PacketPeer`); HTTP requests. For save/persistence → `save-systems`.

## Core workflow

1. **Create a peer** (`ENetMultiplayerPeer`), call `create_server(port, max)` or
   `create_client(ip, port)`, and assign it to `multiplayer.multiplayer_peer`. The
   server's unique ID is always `1`; clients get random positive IDs.
2. **Handle connection signals** on `multiplayer`: `peer_connected(id)`,
   `peer_disconnected(id)`, `connected_to_server`, `connection_failed`,
   `server_disconnected`.
3. **Define RPCs** with `@rpc(...)`. Call them on a `Callable` via `rpc()` (all peers) or
   `rpc_id(peer_id)` (one peer). Inside, `multiplayer.get_remote_sender_id()` tells you who
   sent it.
4. **Keep RPC signatures identical** on every peer that runs the script — Godot checksums
   all `@rpc` methods in a script; mismatches break silently.
5. **Assign authority** per node with `set_multiplayer_authority(id)`; gate input/RPCs by
   `is_multiplayer_authority()`.
6. **Replicate state** with `MultiplayerSpawner` (auto-instances scenes on clients) and
   `MultiplayerSynchronizer` (auto-syncs selected properties).
7. **Validate on the server.** Don't trust client-reported positions/results.

## Patterns

### 1. Host or join (ENet)

```gdscript
const PORT := 7000
const MAX_PLAYERS := 8

func host() -> void:
    var peer := ENetMultiplayerPeer.new()
    var err := peer.create_server(PORT, MAX_PLAYERS)
    if err != OK:
        push_error("Cannot host: %s" % err); return
    multiplayer.multiplayer_peer = peer
    multiplayer.peer_connected.connect(_on_peer_connected)

func join(ip := "127.0.0.1") -> void:
    var peer := ENetMultiplayerPeer.new()
    peer.create_client(ip, PORT)
    multiplayer.multiplayer_peer = peer
    multiplayer.connected_to_server.connect(func(): print("connected"))

func leave() -> void:
    multiplayer.multiplayer_peer = OfflineMultiplayerPeer.new()
```

### 2. RPCs: client sends input to the server (any_peer, call_local)

```gdscript
func _unhandled_input(event: InputEvent) -> void:
    if event.is_action_pressed("fire") and is_multiplayer_authority():
        request_fire.rpc_id(1)          # send only to the server (id 1)

# Clients may call this; it runs on the server (and locally if server is a player).
@rpc("any_peer", "call_local", "reliable")
func request_fire() -> void:
    var sender := multiplayer.get_remote_sender_id()
    if not _can_fire(sender):           # server-side validation
        return
    spawn_projectile.rpc(sender)        # tell everyone to spawn it

@rpc("authority", "call_local", "reliable")
func spawn_projectile(owner_id: int) -> void:
    _do_spawn(owner_id)
```

### 3. Per-node authority (each player controls their own avatar)

```gdscript
extends CharacterBody2D

func _ready() -> void:
    # The node name is the owning peer's id; that peer is the authority.
    set_multiplayer_authority(name.to_int())

func _physics_process(delta: float) -> void:
    if not is_multiplayer_authority():
        return                          # only the owner reads input & moves
    velocity = Input.get_vector("left", "right", "up", "down") * 200.0
    move_and_slide()
```

### 4. MultiplayerSynchronizer config (editor + replication)

```gdscript
# Add a MultiplayerSynchronizer child; in its Replication editor add the properties to
# sync (e.g. position, velocity). Set "Sync"/"Spawn" flags per property. From code you
# can scope visibility:
@onready var sync: MultiplayerSynchronizer = $MultiplayerSynchronizer

func _ready() -> void:
    # Only replicate this node to a specific peer (e.g. private info).
    sync.set_visibility_for(target_peer_id, true)
```

## Pitfalls

- **RPC signature checksum.** Every `@rpc` method in a script must exist with the same
  declaration on both client and server builds — *even unused ones*. A mismatch causes
  errors that may point at the wrong function. Argument names/count are not checked, but
  the set of RPCs and their annotations are.
- **Default `@rpc` is `"authority"`.** Clients calling it are ignored unless you set
  `"any_peer"`. Use `"call_local"` so the host (also a player) runs it too.
- **NodePaths must match across peers.** RPC routing uses the node's path/name; spawn nodes
  with identical names on all peers (use `MultiplayerSpawner` or `add_child(node, true)` for
  readable, deterministic names).
- **Trusting the client.** Never let clients set authoritative state (health, position,
  hits) directly. Send *intent*, validate on the server, then broadcast results.
- **RPC on non-Node classes fails.** `@rpc` methods must be on `Node`-derived classes, not
  plain `Resource`/`RefCounted`.
- **RPCs don't serialize Objects/Callables.** Pass plain data (ints, strings, arrays,
  dictionaries, PackedArrays).
- **Forgetting to reset the peer.** To disconnect cleanly, set
  `multiplayer.multiplayer_peer = OfflineMultiplayerPeer.new()`.
- **Android needs INTERNET permission** in the export preset or all networking is blocked.

## AAA studio practice

- **Riot Games (Valorant): server-authoritative, high tick rate, server-side
  combat resolution.** Valorant runs on 128-tick dedicated servers (a server
  update every ~7.8 ms), with all combat decisions living on the server: when a
  player shoots, the server rewinds game state to the exact simulation time
  the shooter saw, to give near-perfect hit registration, and caps how far
  back it will rewind so extreme latency cannot become a weapon. Riot also
  enforced fixed 128 Hz physics timesteps on server and client so movement
  ticks align regardless of frame rate.
  Sources: https://www.pcgamer.com/uk/valorant-peekers-advantage-interview/ and https://edgegap.com/blog/game-backend-deep-dive-valorant-riot-games
- **Never trust the client, and never leak what a player should not know.**
  Independent anti-cheat guidance for small multiplayer games states the same
  rule this skill already gives: the authoritative server validates movement
  against maximum speed and collision, enforces cooldowns/ammo/resources, and
  calculates damage and rewards; wallhacks work because the client knows
  things the player should not see, so only send positions of enemies a player
  can actually perceive.
  Source: http://dev.to/aplusgamesstudio/anti-cheat-for-small-multiplayer-games-what-works-4a6g

Agent-executable steps (Do / Check / Why):

- Do: implement the Valorant-shaped checklist as code review gates, not
  aspirations: (1) every RPC that changes health, position, currency, or
  score is `any_peer` to the server only and validated server-side (speed
  cap, cooldown, ammo, line-of-sight where applicable) before any broadcast;
  (2) the server runs movement/physics on `_physics_process` (fixed tick),
  never `_process`, so server and client timesteps do not drift with frame
  rate; (3) the synchronizer's visibility flags hide private or
  not-yet-visible state (Pattern 4) instead of syncing everything to everyone.
- Do: add a headless netcode test (see `godot-gdscript-headless-testing`) that
  starts a server peer and two client peers in one process where possible, or
  as a scripted two-process run, sends an illegal input (teleport beyond max
  speed, fire during cooldown), and asserts the server rejects it and the
  broadcast state is unchanged. This is the Godot analogue of Riot's
  server-rewind/validation discipline, at a scale a small team can run.
- Check: grep all `@rpc` declarations and confirm none of them directly sets
  authoritative state from a client-supplied value without a server-side
  validation call in the same function. Any such RPC fails review.
- Why: Riot's fairness comes from the server being the only decider, at a
  fixed tick, with bounded forgiveness for latency. Godot's authority and
  synchronizer flags are the tools that implement that same contract; using
  them only for movement and trusting clients for damage defeats the design.

## References

- For `MultiplayerSpawner` setup, transfer modes/channels, `SceneMultiplayer`
  authentication (`auth_callback`/`complete_auth`), a lobby skeleton, and dedicated-server
  export notes, read `references/replication-and-rpc.md`.

## Related skills

- `godot-nodes-scenes` — instancing the scenes that get spawned/synced.
- `godot-signals-groups` — connection signals and event flow.
- `godot-export` — exporting a headless dedicated server build.
