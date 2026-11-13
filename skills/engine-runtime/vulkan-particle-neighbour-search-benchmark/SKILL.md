---
name: vulkan-particle-neighbour-search-benchmark
description: "Benchmark a Vulkan 2D particle simulation against its CPU twin: implement Atencio et al. 2025 circumference-sampled neighbour search on a uniform grid, port it to two GLSL compute shaders with atomicAdd and a dedup array, and measure honestly. GPU was 2.85x at 8000 particles and 5.33x at a 512x512 grid on an i7-7700 + GTX 1080 Ti, short of the paper's 'orders of magnitude' claim, with an impulse cap of 1.0 labelled as a cheat. Includes the synchronisation fixes, the timestep settling behaviour, and the scope-cut lesson from a 3-month MSc dissertation. Trigger when porting a sequential physics algorithm to GPU compute, or when a benchmark needs to be fair instead of flattering."
---

# Vulkan 2D Particle Simulation: CPU vs GPU Neighbour-Search Benchmark

## Purpose

This skill reconstructs the Vulkan particle-simulation benchmark from the author's post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: implement the same neighbour search twice, once on CPU and once on GPU, and measure whether the paper's "orders of magnitude" claim survives contact with hardware.

## Source

Creator: Hauntir. Reddit post:
https://www.reddit.com/r/GraphicsProgramming/comments/1xss30q/first_graphics_programming_project_in_vulkan_2d/
(r/GraphicsProgramming post 1xss30q, score 30, 3 comments) | 2026-11-12 scout run, audit 8. Project repo (not retrieved this run):
https://github.com/Dozuu-Touryou/variable-particle-simulation
Main reference paper: Atencio et al. 2025 (neighbour search for varying-size particles). Note: the post was removed by the r/GraphicsProgramming mods for a missing AI disclosure, per the mod-team comment.

## Tools used

**Vulkan**, **GLSL** compute shaders, **C++**; main reference paper **Atencio et al. 2025**. Learning resources: "Learn Modern Vulkan in 2 Hours (Dynamic Rendering, No Render Passes!)" (YouTube), Vulkan Lecture Series by **@cgtuwien**, **Vulkanised** conference talks, Vulkan documentation, rastergrid article on memory barriers and image layouts, "Collision Response - Impulse Methods" (Eugene Kenny).

## Phase 1: Learn Vulkan from the standard path

**Do**
1. Spend a couple of weeks on theory using YouTube, mainly "Learn Modern Vulkan in 2 Hours (Dynamic Rendering, No Render Passes!)", plus the Vulkan Lecture Series by @cgtuwien and talks from the Vulkanised developer conference.
2. Spend a few more weeks on boilerplate (heavily referencing the "Learn Modern Vulkan" video) until a single static circle renders. Reference the Vulkan documentation throughout.
3. This was a 3-month MSc Computer Science conversion dissertation; the original plan (multi-layer clothing collision at 60 fps) was dropped after reading papers that needed multivariable calculus, machine learning, GPU hardware, and graphics API knowledge the author did not yet have.

**Check**
- The scope cut is the lesson: the author changed the project to "picking up the basics of a modern graphics API" as a learning outcome, rather than failing at the clothing problem in 3 months.

**Why**
- A dissertation with a finishable scope beats an ambitious one with no result. The benchmark below only exists because the scope was cut.

## Phase 2: Implement the Atencio neighbour search on CPU

**Do**
1. Follow Atencio et al. 2025: sample points on the circumference of circular particles and record their presence in each affected cell of a uniform grid representing the simulation space. Then sample points from half a radius around the circumference and check collision only against particles in cells where a point was sampled.
2. Mimic the paper's Algorithm 2 pseudocode with minor differences (radians rather than degrees as the angle unit). The helper-function definitions were not in the pseudocode, so the author combined experimentation with ideas from "Collision Response - Impulse Methods" (Eugene Kenny).
3. Keep the architecture simple: one Application class with 50+ data members and 60+ member functions. The author left it that way on advice from a Vulkanised talk: "abstracting Vulkan properly is difficult and it should not be attempted by a beginner."

**Check**
- The CPU version is the fairness baseline for the GPU comparison; both implementations follow the same approach "so that the comparison with the CPU version later on would be as fair as possible."

**Why**
- A benchmark is only meaningful if both sides implement the same algorithm. The CPU version is the control group.

## Phase 3: Port to GPU with two compute shaders

**Do**
1. Split the GPU physics update across two compute shaders.
2. Fix synchronisation first: lack of synchronisation between CPU and GPU work and between the two compute shaders was the first blocker; the rastergrid article on memory barriers and image layouts plus the Vulkan documentation sorted it out.
3. Fix data races with `atomicAdd()` when adding particle indices to cells' arrays of occupying indices. Make each thread responsible for one particle, updating no other particle's data.
4. Add a deduplication array: excessive velocity was applied to particles whose area overlapped multiple neighbouring cells. This "only ameliorated the issue, rather than completely eliminating it", possibly due to the dedup array's capacity limit or other undiagnosed factors.

**Check**
- Validation-layer errors are the signal during this phase. If the validation layers are quiet and the particles move, the synchronisation is right; if particles gain impossible velocity, the dedup array is the suspect.

**Why**
- Parallelism breaks the sequential assumption in the paper's pseudocode. The fixes (atomics, one-thread-per-particle, dedup) are the price of the port.

## Phase 4: Measure, and cap the impulse

**Do**
1. Measure both implementations on an Intel Core i7-7700 CPU and an NVIDIA GeForce GTX 1080 Ti GPU.
2. Results: GPU faster by 2.85x when simulating 8000 particles, and 5.33x when a grid resolution of 512x512 cells was used. This fell short of the paper's "orders of magnitude" claim.
3. Add the artificial measure that makes stacked particles settle: in the helper `resolveCollision()`, `if (impulse > 1.0) impulse = 1.0;`. The author is explicit that this "feels like cheating by artificially shrinking the natural force that should be applied" and that lowering the threshold further helps only up to a point.
4. Note the timestep behaviour: particles do not settle completely even at a 1/1920-second timestep. A larger timestep (1/60 s) makes particles more restless; a smaller one (1/480 s) makes them more settled, assumed because the update loop runs more often, the velocity damper is applied more often, and collision resolution runs more often, so there is less interpenetration.

**Check**
- The author's own hypotheses for the shortfall: insufficient data range (more particles might approach the claimed speedup, if the trend holds), the port's optimisation level, or old hardware.
- The open question the author puts to the subreddit: a GPU implementation that still mimics the circumference-sampling neighbour search but optimises the remaining shader logic for a much larger speedup, and an alternative to the impulse cap for making stacked particles come to a halt.

**Why**
- A benchmark that contradicts the paper is more useful than one that confirms it, provided the shortfall is reported with the hardware and the workarounds attached. The impulse cap is documented as a cheat, not hidden as a tuning constant.

## The human method, distilled

1. Cut the scope until the project finishes in the time available.
2. Implement the same algorithm twice; the CPU version is the control.
3. Report the number that embarrasses the paper (2.85x, not "orders of magnitude") with the hardware attached.
4. Label a hack as a hack: the impulse cap is in the code and in the write-up.

## AAA studio practice

The author's port follows the canonical GPU particle recipe almost exactly, and the canonical sources name the tradeoffs the author discovered by hand.

- **NVIDIA CUDA Particles (Simon Green, 2007).** The reference implementation for particle systems with local interactions on a uniform grid: subdivide the space into uniformly sized cells with the cell size equal to the particle size (double its radius), assign each particle to a cell by its center point, and rebuild the grid from scratch every timestep. Two grid-build paths are documented: atomic operations (simple, needs atomic support) and sorting by hash (the fallback for hardware without atomics).
  (http://developer.download.nvidia.com/compute/cuda/1.1-Beta/x86_website/projects/particles/doc/particles.pdf)
  The direct parallel: the author's atomicAdd cell-index build plus one-thread-per-particle update is the atomic path, and the dedup array is the fix for the exact failure the paper's design anticipates (a particle overlapping multiple cells being processed twice).
- **Locally perfect spatial hashing (Haug).** The fixed-radius near-neighbors problem on the GPU is usually solved by imposing a regular grid and searching adjacent cells, but hash collisions make hash tables tricky to implement efficiently on the GPU. The locally perfect approach constructs spatial hash functions that preserve equivalence classes between positions and buckets, eliminating hash collisions in the immediate vicinity of a particle and removing the need for hash-table bookkeeping.
  (https://haug.codes/blog/locally-perfect-hashing/)
  The direct parallel: if the dedup array's capacity limit is the remaining velocity bug, a collision-free hash is the next fix to try before blaming the solver, and the skill's open question (an alternative to the impulse cap) is the same problem stated from the solver side.

**Agent automation**

1. **Benchmark manifest.** Keep `particle-benchmark.json` per run: particle count, grid resolution, hardware (CPU model, GPU model), CPU time, GPU time, and speedup. A check asserts the speedup is reported with the hardware attached; a speedup with no hardware is not a result.
2. **Scaling sweep.** Measure at three or more particle counts and three or more grid resolutions and record the speedup curve, not a single point. The author's hypothesis (more particles might approach the paper's claim) becomes a testable curve; a flat or falling curve at higher counts falsifies it.
3. **Impulse-cap disclosure.** Any artificial force cap in the solver (such as `if (impulse > 1.0) impulse = 1.0;`) must be logged in the manifest with its threshold, the reason it was added, and the settling behavior it buys. A cap that is not logged is a hidden tuning constant; a logged cap is a documented hack.
4. **Dedup-capacity log.** Record the dedup array's capacity, the maximum occupancy reached per frame, and any frame where occupancy hit capacity. If impossible velocity appears on a frame where occupancy hit capacity, the dedup array is the prime suspect, per the author's own diagnosis.

**Depth status:** FULL (8,150-character post text with method, code-level detail, benchmarks, hardware, and failure analysis; the linked GitHub repo was not retrieved; note: the post was removed by the r/GraphicsProgramming mods for a missing AI disclosure).
