---
name: jet-studio-godot-mcu-editor
description: "Build a Godot-flavored game editor for microcontroller targets: reuse Godot 4's UI/theme/icons and node conventions in an interface-only app, bridge a C++17 software runtime via GDExtension, design a strict GDScript subset (JetScript) that compiles to bytecode for a small on-board VM, and measure FPS plus RAM on real 320x240 SPI hardware. Trigger when building editor tooling for severely constrained targets."
---

# Jet Studio: A Godot App That Makes Games for Tiny SPI Displays

## Purpose

This skill builds a game editor for microcontroller targets out of Godot
itself, step by step, so another agent can follow the same process. Every
phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The core method is: reuse a real
editor's entire UX so the constraint work concentrates in the runtime and
the language subset, not the tooling.

## Source

Reddit, fedyfaustoITA (full post text + 2 comments, 2026-10-29):

- https://www.reddit.com/r/godot/comments/1xi3imx/ - "Jet Studio: a Godot
  app (GDScript + GDExtension) that makes games for tiny SPI displays"
- Open source: https://github.com/fedyfausto/JetStudio (prototype v0.5.0)
- Demos: physics (https://www.youtube.com/watch?v=Qyh9KQlXAAA), JetRun
  (https://www.youtube.com/watch?v=o8o237eqnMw), Jet Blaster
  (https://www.youtube.com/watch?v=085BnOyN1vA)

Evidence note: post text only; no code reviewed, videos not watched. FPS
numbers are the author's on real hardware. Jet is by CubeCoders (third
party, not the post author).

## Tools used

Godot 4 (interface-only app: the editor); GDScript (editor logic); C++
GDExtension (wraps the runtime); Jet runtime (C++17, software renderer, by
CubeCoders); JetScript (GDScript-like language compiling to bytecode, small
VM on the board). Targets: Arduino Nano ESP32 or STM32 boards with a
320x240 ILI9341 SPI display.

## Phase 1: Reuse Godot's editor UX wholesale

**Do**
1. Build the editor as a Godot 4 app reusing Godot's UI, theme, editor
   icons, and conventions: Scene dock, Inspector, FileSystem dock, scene
   tabs, undo/redo, Create Node dialog, Change Type, "Create Root Node"
   for new scenes.
2. Provide 2D and 3D views with Godot's navigation; Play runs the scene
   inside the editor.
3. Mirror Godot's node names and properties: Node3D, MeshInstance3D,
   Camera3D, CharacterBody3D (`move_and_slide()`), RigidBody3D, Area3D,
   CPUParticles3D, Node2D, Sprite2D, AnimatedSprite2D, Camera2D, the 2D
   bodies, Controls, Timer.
4. Mirror Godot 4 signals: a Signals dock with the "Connect a Signal to a
   Method" dialog; propose `_on_timer_timeout`, add the method to the
   receiver's script, show the slot icon in the script gutter.

**Check**
- A Godot user's muscle memory works: "Godot's default node script
  template works as is."
- Play in the editor looks like the board (the same runtime renders both).

**Why**
"the editor itself is a Godot 4 app... I reused Godot's UI, theme and
editor icons and kept its conventions everywhere I could." Familiarity is
the onboarding strategy; the new thing is the target, not the tool.

## Phase 2: Design JetScript as a strict GDScript subset

**Do**
1. Support the idioms that matter: `extends`, `@export`, `@onready`,
   `$Path`, `signal`, `emit()`/`connect()`, `match`, typed vars,
   `preload()`/`instantiate()`, autoloads.
2. Compile JetScript to bytecode; the board carries only a small VM.
3. Make unsupported features compile errors with clear messages, not
   crashes: `float` is 32-bit (single-precision FPU); no `await`, no
   lambdas, no `class_name`, no inner classes.

**Check**
- Every Godot idiom either works or fails loudly at compile time.
- The VM footprint fits the target class (320 KB RAM devices).

**Why**
Constraint-first language design: the subset is honest about the hardware.
Clear compile errors beat runtime mysteries on a board with no debugger.
Failure modes: silent wrongness on unsupported features is the enemy; the
author chose loud compile errors instead.

## Phase 3: Bridge the C++17 software runtime with a GDExtension

**Do**
1. Implement the independent game runtime in C++17 with a software
   renderer (Jet, by CubeCoders).
2. Wrap it in a C++ GDExtension so the Godot editor drives it.
3. Render the editor's views with the same runtime, so Play in the editor
   is the board's view.

**Check**
- "It is not a Godot fork, and it does not export Godot projects." The
  runtime is independent; the editor is a frontend.
- Editor view and hardware output agree visually.

**Why**
Decoupling the runtime from the editor keeps the hardware target honest:
no export magic, just a small VM plus a software renderer that fits. The
GDExtension is the seam; everything on either side of it is ordinary.

## Phase 4: Measure on real hardware; estimate RAM before building

**Do**
1. Measure on real hardware (320x240 ILI9341 over SPI). Author's numbers:
   Arduino Nano ESP32: 2D shooter ~84 fps, OutRun-style racer ~60 fps,
   3D physics demo ~60 fps. Nucleo-F746ZG (320 KB RAM, no PSRAM): shooter
   ~83 fps.
2. Put Build & Flash and a serial monitor in the editor.
3. Estimate the RAM a scene needs before building.

**Check**
- FPS numbers come from real boards, not emulators.
- The RAM estimate catches scenes that would OOM the board before the
  flash step wastes a cycle.

**Why**
On a 320 KB device the budget is the feature. Measuring first and
estimating before building is the whole portability story.

## AAA studio practice

- **Unify the game and the editor so the project is always playable.**
  Ubisoft Massive's Snowdrop engine (GDC 2014, built for Tom Clancy's The
  Division) was created in-house on the philosophy "to do things better,
  not bigger": a node-based system at its core, where "the game and the
  editor are unified, and everything in the engine runs in real time, which
  means that the ongoing project is always playable." Its integrated
  editor lets developers bring the editor up while playing, move content,
  and continue. Applied here: Jet Studio already follows this rule (Play
  in the editor is the board's view); the automation step is formalizing it
  into a regression check, so "editor view and hardware output agree
  visually" is measured, not assumed.
  Source: https://www.otakustudy.com/video-game/2014/03/ubisoft-share-dev-diary-qa-new-snowdrop-engine/
- **On constrained hardware, offer a language ladder, not a single
  compromise.** Panic's Playdate is a shipped constrained-target device
  built on a microcontroller (STM32F-class, 168 MHz, 16 MB RAM, 400x240
  1-bit screen, no GPU), and Panic shipped it with an official SDK for both
  Lua and C plus Pulp, a no-coding web tool: a ladder from low-code to
  native, so each developer picks the rung that fits their constraint.
  Applied here (labeled: Playdate is a commercial indie console, not a AAA
  platform, but the closest shipped example of language-tiering for
  constrained targets): JetScript is Jet Studio's middle rung. The
  automation upgrade below is the tier checker: static analysis on every
  save rejects unsupported constructs (await, lambdas, class_name, inner
  classes) with the exact compile error the on-board VM would emit and
  points the author at the supported idiom, enforcing the Phase 2 rule of
  loud compile errors before the flash step.
  Source: https://functionallyimperative.com/p/playdate-a-love-letter-to-constraints

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Add a JetScript subset linter that runs on every script save: parse for
   the banned constructs from Phase 2 (await, lambdas, class_name, inner
   classes, double-precision float assumptions) and emit the VM's compile
   error inside the editor before flash; the loud-error rule made
   automatic.
2. Add a RAM-budget ledger: assign each node type and script allocation a
   conservative byte estimate, total them per scene, and fail the build
   when the estimate exceeds the target board's RAM (e.g. 320 KB on the
   Nucleo-F746ZG), before the flash step wastes a cycle; Phase 4's
   "estimate before building" made automatic.
3. Add a hardware agreement test: run a fixed reference scene through the
   editor runtime and through the real board over serial, capture both
   framebuffers, and diff them; a mismatch fails CI, proving "editor view
   and hardware output agree visually" with evidence.

**Check**
- Unsupported JetScript constructs are caught at save time with the VM's
  error message, not at flash time.
- The RAM ledger fails a scene that would OOM before any hardware is
  touched; the framebuffer diff passes only when editor and board agree.

**Why**
Constraint-first design only works when the constraints are enforced by
tools, not remembered by authors. The linter enforces the language subset,
the ledger enforces the RAM budget, and the framebuffer diff enforces the
"what you see is what ships" promise; the three guarantees that make a
tiny-target editor trustworthy.

## The human method, distilled

1. Convention over invention: every Godot convention the author could
   reuse, he reused; invention was reserved for the runtime and the
   language subset.
2. Honest constraints: unsupported = compile error with a clear message.
3. Prototype discipline: v0.5.0, Linux only, no audio yet, open source on
   GitHub. Ship the slice that proves the loop, then ask Godot users which
   features they would miss most.

**Depth status:** FULL (post text + comments; no code or video inspected).
