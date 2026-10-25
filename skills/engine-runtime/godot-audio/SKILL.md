---
name: godot-audio
description: >
  Play and mix audio in Godot 4.7: AudioStreamPlayer (2D/3D variants), audio buses
  with volume/mute and effects, music vs SFX routing, db/linear volume, and precise
  sync-to-beat playback timing. Use when playing sounds or music in a Godot project,
  routing AudioStreamPlayer nodes to buses, adjusting bus volume via AudioServer, or
  syncing gameplay to the beat.
---

# Godot Audio (4.x)

Play SFX and music, route them through buses, control volume in decibels, and time
gameplay to the beat. Targets **Godot 4.7**.

## When to use

- Use when playing sound effects or music, routing audio to buses (Master/Music/SFX),
  adjusting volume/mute from code, adding bus effects (reverb, compressor), positional 3D
  audio, or syncing events to music.

**When *not* to use:** engine-agnostic audio *design* (adaptive music structure, mixing
philosophy, ducking patterns) → `audio-design`; importing/encoding assets outside Godot.

## Core workflow

1. **Pick the player node:**
   - `AudioStreamPlayer` — non-positional (music, UI, global SFX).
   - `AudioStreamPlayer2D` / `AudioStreamPlayer3D` — positional; volume/pan from distance.
2. **Assign an `AudioStream`** to `stream` (`.ogg` for music/loops, `.wav` for short SFX)
   and `play()`. Set `autoplay` for music that starts with the scene.
3. **Route to a bus.** Set the player's `bus` to a named bus (e.g. `"Music"`, `"SFX"`).
   Define buses in the Audio panel (bottom dock); each can have volume, mute, solo, and
   effects.
4. **Control volume in dB**, not linear (audio is logarithmic). `0 dB` = unchanged,
   `-80 dB` ≈ silent. Convert with `linear_to_db`/`db_to_linear`.
5. **Drive volume/mute from code** with `AudioServer` by bus index.
6. **For rhythm**, compute precise playback time using output latency compensation.

## Patterns

### 1. One-shot SFX (fire-and-forget)

```gdscript
@onready var sfx: AudioStreamPlayer = $Sfx   # stream assigned in the editor

func play_jump() -> void:
    sfx.pitch_scale = randf_range(0.95, 1.05)   # slight variation avoids fatigue
    sfx.play()

# For many overlapping copies, use an AudioStreamPlayer with an
# AudioStreamPolyphonic stream, or spawn short-lived players and free on `finished`.
```

### 2. Set a bus's volume and mute via AudioServer

```gdscript
func set_music_volume(linear_0_to_1: float) -> void:
    var bus := AudioServer.get_bus_index("Music")
    # Convert a 0..1 slider to decibels; clamp avoids -inf at 0.
    AudioServer.set_bus_volume_db(bus, linear_to_db(maxf(linear_0_to_1, 0.0001)))

func toggle_sfx(muted: bool) -> void:
    AudioServer.set_bus_mute(AudioServer.get_bus_index("SFX"), muted)
```

### 3. Crossfade between two music tracks

```gdscript
@onready var a: AudioStreamPlayer = $MusicA
@onready var b: AudioStreamPlayer = $MusicB

func crossfade_to(stream: AudioStream, secs := 1.5) -> void:
    b.stream = stream
    b.volume_db = -40.0
    b.play()
    var tw := create_tween().set_parallel(true)
    tw.tween_property(a, "volume_db", -40.0, secs)   # fade out current
    tw.tween_property(b, "volume_db", 0.0, secs)     # fade in next
    tw.chain().tween_callback(a.stop)
    var tmp := a; a = b; b = tmp                      # swap roles
```

### 4. Beat-accurate timing (compensate for output latency)

```gdscript
@onready var music: AudioStreamPlayer = $Music

func get_playback_time() -> float:
    # Add time since the last audio mix, subtract output latency, for sub-frame accuracy.
    var t := music.get_playback_position() + AudioServer.get_time_since_last_mix()
    return t - AudioServer.get_output_latency()
```

## Pitfalls

- **Treating volume as linear.** `volume_db`/`set_bus_volume_db` are decibels. Setting
  `volume_db = 0.5` is nearly full volume, not half. Map sliders with `linear_to_db`.
- **`linear_to_db(0.0)` is `-inf`.** Clamp the linear value to a small minimum (e.g.
  `0.0001`) before converting, or special-case 0 → mute.
- **Bus name typos fail quietly.** `get_bus_index("Muisc")` returns `-1`; calls then error
  or no-op. Match the exact bus name from the Audio panel.
- **Short SFX cut off** when the same player is retriggered. Use separate players, an
  `AudioStreamPolyphonic`, or `AudioStreamPlayer` per-shot freed on `finished`.
- **Music doesn't loop** unless the import/stream loop is enabled (`.ogg` import has a
  Loop option; `AudioStreamWAV` has `loop_mode`).
- **Syncing to `get_playback_position()` alone is jittery** — it updates per audio mix,
  not per frame; add `get_time_since_last_mix()` and subtract `get_output_latency()`.
- **3D audio inaudible** → no `AudioListener3D`/`Camera3D` to hear it, or `max_distance`/
  attenuation too tight, or wrong bus muted.

## References

- For the bus layout (`.tres`), adding effects (reverb/compressor/EQ) and side-chain
  ducking, `AudioStreamPolyphonic`/`AudioStreamInteractive`, microphone capture, and
  procedural audio with `AudioStreamGenerator`, read `references/buses-and-effects.md`.

## Related skills

- `audio-design` — engine-agnostic adaptive music, mixing, and ducking practice.
- `godot-animation` — syncing animation/Tween to `get_playback_position()`.
- `godot-ui-control` — volume sliders wired to `AudioServer`.

## AAA studio practice

Sources:
- Game Developer, Game Audio Theory: Ducking (bus hierarchy practice): sounds are grouped into a bus hierarchy (Master, then Music/SFX/Voice sub-buses, then finer groups such as weapons under SFX) so a whole class of sounds can be adjusted, ducked, or troubleshot in one place instead of per sound, and ducking rules mix channels interactively at runtime. https://www.gamedeveloper.com/audio/game-audio-theory-ducking
- Ovani Sound, AAA Game Audio Hacks: Ducking (Godot-specific ducking write-up): the ducking pattern is a separate bus plus a transition that lowers the ducked bus and raises the priority bus over a time, triggered by gameplay state, usable for dialogue, cutscenes, and priority sounds. https://ovanisound.com/blogs/news/aaa-game-audio-hacks-ducking

**Do**
1. Adopt the bus hierarchy as a rule, not a suggestion: Master, then Music, SFX, Voice, then sub-buses (for example, Weapons and Footsteps under SFX). Agent-executable step: define the full bus layout once in the project's default bus layout resource, and route every new AudioStreamPlayer to a named bus at creation, never to Master directly except for the bus outputs themselves.
2. Automate the bus-name check from the Pitfalls: script a scan of all .tscn files and scripts for bus name strings, compare against the bus layout, and fail on any name that returns bus index -1, instead of discovering quiet buses at runtime.
3. Add side-chain style ducking as a standard pattern (from the references' ducking note): when Voice plays, tween the Music and SFX buses down by a fixed dB amount over a short time, and restore them when Voice ends. Reuse the existing crossfade tween pattern (Pattern 3) for the duck, so the implementation stays in one idiom.
4. Automate the volume-mapping check: script a test that sets each volume slider to 0, 0.5, and 1.0 and asserts the bus dB values follow linear_to_db (with 0 clamped, not -inf), catching the linear-vs-dB pitfall before it ships.

**Check**
- No AudioStreamPlayer routes directly to Master except bus outputs.
- The bus-name scan passes with zero unmatched names.
- Voice playback ducks Music/SFX and restores them, verified by logged bus dB values before, during, and after.

**Why**
Production audio is a hierarchy with rules, not a pile of per-sound volumes. The bus layout is what makes mixing, ducking, muting, and troubleshooting possible at scale, and every one of those operations in this skill already goes through AudioServer, so the hierarchy is free once it is enforced by script.
