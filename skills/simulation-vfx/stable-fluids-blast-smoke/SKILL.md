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

## AAA studio practice

- **Stable fluids were designed for games first: stability and speed over physical accuracy, with arbitrary time steps.** Jos Stam's "Real-Time Fluid Dynamics for Games" presents a simple, rapid solver for game engines based on the Navier-Stokes equations, emphasising stability and speed so simulations can be advanced with arbitrary time steps and never "blow up", running in real time for reasonable grid sizes on standard PC hardware, with smoke represented as a density field moved through the velocity field. That is the direct lineage of this skill's solver, and it justifies the fixed 30 Hz step plus staggering in Phase 1: stability is the design goal, and the frame budget is managed by scheduling, not by shrinking the physics. Source: http://graphics.cs.cmu.edu/nsp/course/15-464/Fall09/papers/StamFluidforGames.pdf
- **Real-time fluid effects shipped in games by moving the solver to the GPU and treating solid obstacles as part of the simulation.** NVIDIA's GPU Gems 3 chapter on real-time 3D fluids describes the technology behind the GeForce 8 launch demo "Smoke in a Box" and its integration into the game *Hellgate: London*, covering simulation including smoke, water, and fire and interaction with solid obstacles, plus performance and memory considerations, and how to integrate fluid rendering into a rasterization framework. The transferable rule is Phase 2's solid cells plus Phase 4's field rendering: obstacles belong in the solver, and the rendered image comes from the field, not from the particles. Source: https://developer.nvidia.com/gpugems/gpugems3/part-v-physics-simulation/chapter-30-real-time-simulation-and-rendering-3d-fluids
- **Fluid simulation in games stayed rare because it is expensive at small scales and hard to direct, so shipped uses pick dense, turbulent effects and accept the control trade-off.** The GDC presentation on fluid-driven particle effects in Airtight Games' *Dark Void* notes that Stam presented stable fluids in 1999 and fluid simulation for games at GDC 2003, but real 3D fluid simulation took a while to take hold in games, because it is expensive, does not look good at very small resolution or in a very small region, and is viewed as hard to direct and control; *Dark Void* explored Eulerian and particle approaches and found the Eulerian solver the better fit for dense smoke with a lot of turbulent fine-scale motion. The transferable rule is to keep this skill's scope where it wins: dense, architecture-shaped smoke at a scale where the grid reads, and to direct it through solid geometry and divergence sources rather than by scripting the look. Source: https://developer.download.nvidia.com/presentations/2010/gdc/Taking_Fluid_Simulation_Out_of_the_Box_Particle_Effects_in_Dark_Void.pdf

**Agent automation**

Write `blast-sim-manifest.json` per blast, with: grid size (80 by 80) and cell size (4 px), step rate (30 Hz), stagger offset in frames, solid-cell map hash, particle count (about 1,900), and the half-float texture channel assignment (density, temperature, freshness). Fail the blast record if the solid-cell map hash is missing, because without it a wall leak cannot be distinguished from a solver bug. Run these gates per blast: (1) wall-leak gate, after one second of simulated time, assert density in solid cells is zero and record the result, since Phase 2 promises a blast inside a room escapes only through doors and windows; (2) stagger gate, assert no two active blasts share a step frame, by checking the recorded stagger offsets, and log the step time per blast in milliseconds so a frame spike is attributable to one cloud; (3) vorticity overlay gate, save the flow-speed and vorticity overlay described in the companion post for one frame per blast, so the solver quantities are inspected, not only the final render; (4) impulse gate, record one bullet pass and one later blast per test scene and assert the particle displacement is recorded, proving gameplay impulses reach the smoke without separate smoke scripting, as in Phase 3. No frame-time measurement from another engine may be copied into this manifest, since the author disclosed none.

## The human method, distilled

1. Small grids per event, staggered in time, beat one big grid.
2. Let solid geometry shape the effect; do not script the jets.
3. One field, two readers: particles ride it, rendering splats it.

**Depth status:** FULL from the author's full post text. Comments were unretrieved, so no commenter corrections are included.
