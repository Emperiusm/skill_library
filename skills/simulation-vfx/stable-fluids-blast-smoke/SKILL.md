---
name: stable-fluids-blast-smoke
description: "Make explosion smoke that pours out of doors and windows with a small stable-fluids solver: one 80x80 CPU grid per blast at a fixed 30 Hz, staggered steps, blast as a pressure divergence source, solid cells for walls, about 1,900 particles riding the velocity field, rendered through a half-float density/temperature/freshness texture. Trigger when game smoke must react to blasts and bullets and be shaped by architecture instead of hand-placed emitters."
---

# Per-Blast Stable-Fluids Smoke for a Browser Game

## Purpose

This skill makes explosion smoke that is shaped by the level itself. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: give every blast its own small solver grid, let the blast be a pressure divergence source so architecture shapes the flow, and render particles through a half-float field rather than drawing the grid directly.

## Source

- Post: "2D smoke for my browser game: a small stable-fluids grid per explosion, with particles riding it" by Fit-Heat4806 — https://www.reddit.com/r/GraphicsProgramming/comments/1y4cqb4/ (score 20, 2 comments; comments unretrieved, Arctic Shift HTTP 422). Evidence: the author's full post text (1,203 characters, all five bullet points with exact numbers).
- Companion post by the same author: "[OC] explosions as a fluid simulation" — https://www.reddit.com/r/Simulated/comments/1y3njn6/ (score 248, 14 comments, no selftext). It shows the same solver and adds only this description: "rockets, grenades and bullets push it around, and it pours out of doors and windows. Top right is the solver's flow speed and vorticity." The two posts are one audit; no new parameters come from the companion post.
- Language, engine, and frame-time measurements were not disclosed and are not invented here. Scout audit 2026-11-25.

## Tools used

A custom CPU stable-fluids solver in a browser game (language/engine not stated); half-float texture rendering; a full-screen post pass. No named engine, library, or shader tool.

## Phase 1: Give each blast its own grid

**Do**
1. Allocate one 80x80 grid with 4 px cells per blast.
2. Step the solver on the CPU at a fixed 30 Hz. If several blasts are active, stagger their steps across frames so two clouds never step in the same frame.

**Check**
- Multiple simultaneous clouds stay cheap because their steps are spread over frames rather than stacked in one frame.

**Why**
Per-blast grids localise cost and let each explosion have its own flow field. Staggering is the frame-budget control: it trades per-cloud update latency for a flat frame cost.

## Phase 2: Solve with stable fluids

**Do**
1. Use a stable-fluids solver: semi-Lagrangian advection, vorticity confinement, and a pressure projection.
2. Make the blast itself a divergence source in the pressure solve.
3. Mark house walls, trees, and rocks as solid cells, so a blast inside a room can only escape through the door and windows, which is where the jets come from.

**Check**
- Smoke pours out of doors and windows and forms jets there; a blast inside a room does not leak through walls. The companion post's overlay shows flow speed and vorticity, the two solver quantities the author chose to display.

**Why**
Solid cells plus a divergence source make architecture do the shaping work. The jets are an emergent result of the pressure solve meeting solid geometry, not hand-placed emitters.

## Phase 3: Ride particles on the velocity field

**Do**
1. Spawn about 1,900 particles per blast that ride the velocity field.
2. Let later blasts shove existing smoke with a shock, and let bullets push particles aside along their path.

**Check**
- Rockets, grenades, and bullets visibly push the smoke around (companion post description).

**Why**
Particles are the visible smoke; the field is the physics. Coupling them this way means every gameplay impulse (blast, bullet) automatically becomes a smoke impulse, with no separate smoke scripting.

## Phase 4: Render through a half-float field

**Do**
1. Splat particles as streaks into a half-float texture holding density, temperature, and freshness.
2. In a full-screen pass, blur that into a soft body, draw the raw density on top as wispy strands, light it by the density's slope, and colour it from fire to soot to grey by temperature.

**Check**
- The result reads as a soft smoke body with wispy strands on top, lit by its own density gradient, cooling from fire colour to grey.

**Why**
Rendering the field, not the particles, is what makes it look like smoke rather than dots. Temperature as the colour driver ties the look to the simulation state, so cooling is automatic.

## The human method, distilled

1. Small grids per event, staggered in time, beat one big grid.
2. Let solid geometry shape the effect; do not script the jets.
3. One field, two readers: particles ride it, rendering splats it.

**Depth status:** FULL from the author's full post text. Comments were unretrieved, so no commenter corrections are included.
