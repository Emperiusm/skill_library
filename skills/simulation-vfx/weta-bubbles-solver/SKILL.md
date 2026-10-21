---
name: "weta_bubbles"
description: "Implement a two-way coupled bubbles solver from the Weta FX whitepaper in vanilla Houdini nodes. Trigger when building a production fluid solver from a paper."
---

# Two-Way Coupled Bubbles Solver | Weta FX Whitepaper Implementation

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Implement the paper, don't approximate it: a two-way coupled bubbles solver built from the whitepaper's equations in vanilla Houdini nodes.

## Source

Creator: CdvrSzf

Source: https://v.redd.it/eh53g0sb82qh1 | r/houdini post 1wiqmdp (score 286) | native clip (demo, not tutorial)

## Tools used

Tools used: Houdini (vanilla nodes only, no custom plugins), Gas Project Non Divergent Variational (the vanilla projection node doing the heavy lifting), FLIP/Whitewater-adjacent tooling as the baseline being replaced, the Weta FX two-way coupled bubbles whitepaper (Equations 17/18, Section 3.4, Section 3.5 fb clamp).

**Do**
1. Start from the limitation of Houdini's native Whitewater solver: its one-way coupling model. The FLIP velocity field pushes the bubbles; buoyancy is a constant vector.
2. Confirm where that breaks: it holds up for mid- and background elements but "falls short for hero-scale simulations," which is what forces artists onto the Pyro + POP Advect by Volumes workaround.

**Check**
- The hero-scale test is the acceptance criterion. If the fix only improves background elements, it is not worth a custom solver.

**Why**
Rewriting a solver starts with a precise statement of the native one's failure mode. One-way coupling is fine until the bubbles are the subject; the whitepaper implementation exists because hero shots needed the water to push back.

## Phase 1: Define what the native solver cannot do

## Phase 2: Adopt the whitepaper, scope the simplification

**Do**
1. Work from the Weta FX whitepaper on two-way coupled bubbles.
2. Implement the inertia-unaware case (theta = 0) from Equation 18 first. The creator is explicit: the inertia-aware system is not yet implemented, "but I'm actively working on it."

**Check**
- Scope honesty matters here: theta = 0 is a stated simplification, not a hidden one. The inertia-aware case is open work, named as such.

**Why**
A full whitepaper replication is a multi-month project; shipping the theta = 0 case first gets a working two-way solver into shots while the harder case is still in development. The simplification is a sequencing decision, not a compromise of the method.

## Phase 3: Model bubbles as ideal spheres with f@pscale radii

**Do**
1. Treat each bubble as an ideal sphere with radius stored in the f@pscale attribute.
2. [inference] This is the POP-level particle representation; the sphere assumption is what makes the volume math tractable.

**Check**
- Every downstream force and multiplier is a function of bubble volume derived from this radius, so the pscale values have to be trustworthy before anything else.

**Why**
"Ideal sphere" is the modeling contract with the paper. It trades bubble-deformation realism for a volume integral you can actually compute, and the creator's results show the organic look comes from the coupling, not the bubble shape.

## Phase 4: Rasterize bubble volume onto the voxel grid

**Do**
1. Rasterize each bubble's volume onto a voxel grid. This rasterized volume is "the primary multiplier for all forces and operations."
2. From the collective bubble volume, derive the displaced liquid volume and adjust the fluid's density and velocity accordingly.

**Check**
- The rasterization is where particle space becomes grid space. If the volume field is wrong, every force built on it is wrong in the same direction.

**Why**
Two-way coupling needs the water to know where the bubbles are in its own language, which is a grid. Volume as the primary multiplier means every force scales with how much water was actually displaced, which is the physical content of the whole method.

## Phase 5: Project pressure with a vanilla Gas Project Non Divergent Variational

**Do**
1. Build the pressure projection from the vanilla Gas Project Non Divergent Variational node, with what the creator calls "a few minor simplifications," replicating the core logic of the Weta paper.
2. Implement the theta = 0 system as a one-phase variational projection: collect a combined velocity field (fw * u + fb * v) with one effective density (water density + implicit drag force contribution), run it through Gas Project Non Divergent Variational, then decompose the result back to the water velocity.
3. Add the fb clamp from Section 3.5 to keep the system stable.

**Check**
- The other implementer in the thread (diskl0sure) got stuck at exactly this stage and proposes the same Utemp = fw * u + fb * v blend, with an open question about algorithm order: the paper's Section 3.4 says "With the solution for P available, u is readily computed from the first equation in (17)," implying velocity and pressure are evaluated simultaneously via Equation 18, and diskl0sure suspects they "got the algorithm order wrong during the Newton iterations."
- The creator's decisive result: "There is no synthetic buoyancy vector here: upward motion emerges physically, driven by the fluid pressure gradient from high-pressure zones to low-pressure ones."

**Why**
The no-synthetic-buoyancy result is the proof the projection is right. Constant-vector buoyancy is what the native solver does; if your two-way solver still needs one, you have rebuilt the one-way solver. The fb clamp is the stability price of the combined-field formulation.

## Phase 6: Time it on real shots (M4 Max benchmarks)

**Do**
1. Run the canonical tests and record wall-clock times. The creator's numbers, on a MacBook Pro M4 Max:
   - Rubber Toy test: 1 hour 43 minutes (demo video, 00:16)
   - Underwater head test: 1 hour 35 minutes (demo video, 00:06)
   - Sphere falling into water: about half an hour ("noticeably faster")
2. Treat optimization as open work: "The solver needs to be improved, and I think I have a little room for optimization."

**Check**
- [inference] RAM requirements were asked about (kastef) but not answered with numbers in the visible thread. Do not quote a RAM figure.

**Why**
Sim times are the production reality check. Sub-2-hour hero sims on a laptop put this in the usable range for real shots, but the spread between tests (30 min vs 103 min) says scene-dependent cost dominates, which is where optimization effort should go first.

## Phase 7: Name the remaining work

**Do**
1. Finish the foam solver on the water surface.
2. Fix the remaining "unpleasant technical limitations" (the creator's phrase; unspecified in the thread).
3. Pursue the inertia-aware system from Equation 18.

**Check**
- A community member already wants the HDA ("Lol somebody just needs to make a whitewater solver 2.0 hda that people can download"), and the creator has not committed to releasing one. Do not present an HDA as available.

**Why**
Shipping the roadmap publicly is how a solo whitepaper implementation becomes a tool other artists can use. The foam solver and the technical limitations are the gap between a working solver and a usable one; the inertia-aware case is the gap between the simplification and the paper.

## The human method, distilled

1. **Name the native solver's exact failure mode first.** One-way coupling with constant-vector buoyancy is fine for background, fatal for hero. That is the whole justification.
2. **Implement the scoped case, ship it, then extend.** Theta = 0 from Equation 18 is a stated simplification and a working solver beats a complete plan.
3. **Ideal spheres buy you the volume integral.** The organic look comes from the coupling, not from deforming the bubbles.
4. **Rasterize volume to make particles speak grid.** The rasterized bubble volume is the primary multiplier for every force; displaced liquid volume drives the density and velocity adjustments.
5. **Vanilla nodes can carry the paper's core logic.** Gas Project Non Divergent Variational plus a combined field (fw * u + fb * v), one effective density, decomposition back to water velocity, and the Section 3.5 fb clamp.
6. **No synthetic buoyancy is the test of correctness.** If upward motion does not emerge from the pressure gradient, you have rebuilt the one-way solver.
7. **Benchmark on real shots, optimize what varies.** 1h43m, 1h35m, and ~30m on an M4 Max; the scene-dependent spread is where the optimization lives.

## Depth status
 DEPTH-LIMITED (the clip's node graph and exact parameter values beyond f@pscale are unseen; the reconstruction is grounded in the unusually detailed comment thread, but sim internals, the foam solver, and the inertia-aware path are not visible in the sources. [inference] marks the thin spots).

---

---

# Agentic DCC workflows: reconstructions

Reconstructions of three audited videos. Same format as the cinematic-cavern guide:
source line, tools used, phased sections each with Do / Check / Why, exact
parameters and names wherever the source gives them, distilled principles.
Anything inferred is marked [inference].

---
