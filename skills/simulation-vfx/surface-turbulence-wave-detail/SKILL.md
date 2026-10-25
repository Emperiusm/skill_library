---
name: surface-turbulence-wave-detail
description: "Add fine surface waves to a cached particle-based liquid simulation without rerunning it: build a fine surface point set, track it with an advection plus repair loop (insert/delete, bend constraint, normal and tangential regularization), then simulate waves on the surface with a locally estimated Laplacian and curvature-driven sourcing, implemented as a three-stage Houdini network. Trigger when a liquid sim looks too smooth up close, when re-simming at higher resolution is too expensive, or when you need iterated wave-detail looks on cached fluid motion."
---

# Surface Turbulence Wave Detail

## Purpose

Add small-scale surface waves to a liquid simulation without rerunning the
base simulation. You track a much finer set of points along the liquid
surface, simulate waves on those points, and use them to modify the final
geometry. The waves react to the liquid's movement and travel across its
surface at scales that would be expensive to resolve in the original sim.

**Source:** "Why 100 Million Particles Still Aren't Enough" by Vojtěch
Pröschl (36:19), https://youtu.be/l5jDmvfzql0. The author implemented the
method as a proof-of-concept Houdini plugin for a project with Stormborn
Studios (VFX supervisor and founder Guran Pavles). Based on Mercier et al.
(2015), "Surface Turbulence for Particle-Based Liquid Simulations"
(https://www.oliviermercier.com/res/publications/surfaceTurbulence/).

**Tools used:** Houdini 21.0.425 Indie (Arch Linux); a Houdini plugin
implementing the paper (proof of concept, not a released product).
Benchmark hardware: AMD Ryzen 9 9950X, NVIDIA GeForce RTX 5090, 128 GB RAM.

The core method throughout: solve motion and surface separately. Pay for
surface tracking once and cache it, then iterate the waves cheaply. "The most
expensive part of the process is already done, which is the surface tracking.
So, we can iterate quickly and see the effect of different wave settings."

## When to use this skill

- A FLIP/particle liquid sim looks detailed from a distance but too smooth up
  close (the author's case: ~100 million particles, 6 hours of compute,
  still missing fine detail).
- Re-simming at a resolution that captures small waves is unaffordable.
- You want to art-direct wave detail (speed, sourcing strength) without
  touching the base motion.

## Prerequisites

- A cached base liquid simulation (the author's: 360 frames, ~105.8M
  particles mean, voxel size 0.01).
- A signed distance field describing the colliders.
- Houdini with a VEX/Python or HDK implementation of the stages below; the
  formulas here are the complete spec.

## Key parameters (from the benchmarked configuration)

- Fine point spacing λ_f = 0.0025 (controls surface density; "Fine scale
  controls the target spacing. So when I reduce this, it gives us a denser
  surface").
- Repair iterations per advection step: 6.
- Point deletion threshold: two points closer than 3/4 of the fine spacing;
  remove the newer one.
- Laplacian neighborhood radius: 2× the target point spacing.
- Wave solver substeps: 5.
- Benchmark scale: 7.98M fine points mean over 360 frames.

## Phase 1: Initialization (build the fine surface)

**Do**
1. Inputs: the existing cached fluid simulation, plus an SDF describing the
   colliders.
2. Construct the fine surface at the starting frame. Fine scale sets the
   target point spacing (benchmark: λ_f = 0.0025).
3. Near collider boundaries, add ghost points: reflected copies of nearby
   surface points (details in the paper).
4. Seed the initial samples. The paper uses rejection sampling. The author
   notes: "I have used a deliberately sparse set of initial points. In
   practice, we would start closer to the target distribution to reduce the
   work."
5. Cache the initial surface so it is never computed again.

**Check**
- The sheet is coherent at the starting frame before any advection.
- Ghost points are present near collider SDF boundaries.

**Why**
Surface tracking needs a coherent starting sheet. Colliders need explicit
boundary handling or tracked points leak through them.

## Phase 2: Surface tracking (advection + repair loop)

**Do**
1. Advect the fine points with the liquid.
2. Apply the bend constraint.
3. Enter the repair loop (6 iterations per advection step in the benchmark):
   a. **Insert** points where gaps exceed the target spacing. The probe
      follows the resulting direction while remaining one target spacing from
      the selected point: probe position x_i − λ_f · r_i/‖r_i‖, where r_i =
      Σ_j W^M_j(x_i) · T_i(x_j − x_i) is the weighted average of neighbor
      directions, projected and normalized.
   b. **Delete** points where the surface is too dense: "If two points are
      closer than 3/4 of the fine spacing, the paper removes the newer one."
      In the implementation, newer points have larger IDs: mark each point
      that has an older neighbor within this radius, then remove all marked
      points together.
   c. **Reapply the bend constraint** (new points may lie outside it).
   d. **Regularize along the normals:** use a circle as the local model of
      the surface in the plane of two neighboring points and their normals;
      project the second normal onto the plane, place the circle center at
      the intersection of the two lines, set the radius to the average of
      the distances from the center to the two points; move along the normal
      by the signed distance σ; average σ over neighbors with the insertion
      weights; calculate all displacements first, then apply them at once.
      Constructions that fail are left out and weights renormalized to sum
      to one.
   e. **Regularize along the tangents:** for the selected point, normalize
      the vectors toward its neighbors, take the weighted average (it points
      toward the more populated side), and multiply by minus half the target
      spacing. "Because the average of unit directions cannot be longer than
      one, the point can move at most half the target spacing in a single
      step." Calculate the correction for every point before moving any of
      them.
4. Recompute updated surface normals at the beginning of each repair
   iteration. (The paper does not describe recomputing normals between
   individual operations; small changes leave stale normals accurate enough.)

**Check**
- The point-count graph no longer grows after insertion/deletion settle.
- A vertical slice through the surface shows a thin sheet, not a thick
  region.
- Point spacing is even across the sheet.

**Why**
Advection stretches and clumps the point set; without the repair loop the
sheet tears (gaps) or balloons (thick region, runaway point count). The
deletion rule is execution-order independent: "Because every check uses the
same set of points, the result doesn't depend on execution order." Tangential
regularization is bounded (half target spacing max) so one step cannot
overshoot.

**Failure mode and fix:** after enabling insertion alone, the point count
grows excessively (visible in the point-count graph). Fix: add deletion as
above. If points still occupy a thick region in the vertical slice, the
normal regularization is missing or under-iterated; if spacing is uneven,
the tangential regularization needs more iterations.

## Phase 3: Wave simulation on the surface

**Do**
1. Wave equation on the height field h(x,y,t) over the surface:
   ∂²h/∂t² = c²Δh, where Δh = ∂²h/∂x² + ∂²h/∂y² and c is the wave propagation
   speed.
2. Estimate the Laplacian in local coordinates:
   - Neighborhood radius: "twice the target point spacing".
   - Build local coordinates around each point: two tangent coordinates plus
     one normal coordinate. Construct the tangent frame from the SDF
     gradient: n_i = ∇φ(x_i)/‖∇φ(x_i)‖, t¹_i = (n_i × e_i)/‖n_i × e_i‖,
     t²_i = n_i × t¹_i, with e_i = argmin over {e1,e2,e3} of |⟨n_i, e⟩| (the
     axis least aligned with the normal).
   - Fit a plane to the height samples with least squares and subtract it (a
     plane has zero Laplacian, so subtracting it changes nothing).
   - Laplacian ≈ Σ 4·w_j·(h_j − h_i)/d² over neighbors; the factor 4 comes
     from the paper's normalization.
   - Do NOT use a quadratic fit: "the paper reports that this can become
     unstable when the wave scale is comparable to the point spacing."
3. Update: height velocity first, then height (the paper's scheme).
4. Source new waves from curvature:
   - Curvature = local surface bending: how neighboring points deviate from
     the local tangent plane. Use its absolute value.
   - Convert curvature to a signed response with a smoothstep between a
     lower threshold (−1 below) and an upper threshold (+1 above). Adjusting
     the thresholds changes which regions respond positively or negatively.
   - Accumulate the amplitude over time (curvature decides grow vs. fade, so
     sourcing grows and fades gradually instead of jumping). The amplitude
     step controls how much it changes per sourcing update.
   - Multiply by a cosine to make the source oscillate between positive and
     negative.
   - Add the source to the existing wave height to form a temporary wave
     height; evolve the waves on the temporary heights; then subtract the
     same source after the wave update. "We want the waves it generates
     without displaying the oscillator's own displacement. Subtracting that
     removes that displacement but retains a change produced by the wave
     update."
5. Split each update into two stages: sourcing first, wave evolution second.
6. Initialize new points' state: the paper does not specify how to initialize
   wave height, height velocity, and accumulated amplitude on newly inserted
   points. The author tested three options:
   - (a) Zero-init: "introduces discontinuity which in my experience leads
     to noise."
   - (b) Weighted average of surviving neighbors: "greatly reduces the
     noise" but stretches values as the fine surface expands.
   - (c) Weighted average for new points while reducing the surviving
     points' wave height and velocity by what they contributed to the
     average.

**Check**
- Waves propagate from splash/curvature regions and travel across the
  surface.
- New-point initialization does not inject noise: compare zero-init vs.
  neighbor-average side by side and keep the quieter one.

**Why**
A quadratic-fit Laplacian destabilizes at the wave/point scale, so the
plane-subtracted weighted sum is the stable estimator. Sources must grow and
fade gradually or the amplitude jumps abruptly as the surface changes.
Subtracting the oscillator after the wave update keeps the generated waves
while hiding the oscillator's displacement.

## Phase 4: Houdini network, visualization, benchmarks

**Do**
1. Structure the Houdini network in three stages: initialization, tracking,
   wave simulation.
2. Cache the track sequence so tracking is computed once.
3. Add a visualization node with switchable views that do not rerun the
   solver: height view (resulting waves), seed-value view (oscillating
   sources), oscillator-amplitude view (how source amplitude builds up and
   fades).
4. Turn off the wave cache to watch the solver run in real time while tuning
   wave speed and thresholds.
5. Benchmark with stated boundaries: "The tracking and wave timings include
   CPU and GPU processing along with transfers between them. They however
   exclude loading the cached inputs from disk and running upstream nodes."
   Reference numbers (360 frames, benchmark config above):
   - FLIP (context, from cache timestamps, includes cache writes):
     ~56.25 s/frame, total ~5.6 h.
   - Tracking: 19.67 s/frame mean (std ~1.53 s), total ~1 h 58 m, peak
     allocated buffers 10.056 GB.
   - Waves (5 substeps): 10.03 s/frame mean (std ~0.77 s), total ~1 h 00 m
     (computed from the per-frame mean), peak allocated buffers 2.261 GB.

**Check**
- Tracking is cached; wave settings iterate quickly without re-tracking.
- Benchmark comparisons state what is included (transfers) and excluded
  (cache I/O, upstream nodes).

**Why**
Separating motion from surface detail is the entire economic argument: pay
for tracking once, iterate the waves cheaply. Honest measurement boundaries
keep the benchmark comparable.

## The human method, distilled

1. **Solve motion and surface separately.** Track once, cache, iterate waves.
2. **Paper as spec, judgment on the gaps.** Where the paper is silent
   (new-point initialization), test the options and keep the comparison.
3. **Order-independent operations.** Deletion checks use one shared point set
   so execution order cannot change the result.
4. **Verify with a deliberately worse copy.** Zero-init vs. neighbor-average
   for new points; thick vs. thin sheet slices; distance-only vs.
   density-compensated height.
5. **Benchmark with stated boundaries.** Transfers in, cache I/O out; FLIP
   times labeled as estimated from cache timestamps.

## AAA studio practice

**Do**
1. Keep the track-once, iterate-waves-cheaply split, because Weta FX used the same split on Avatar: The Way of Water: a post-process that took a finished simulation as input and increased its apparent resolution by simulating detailed Lagrangian water waves on top of it, with wave packets attached to spline curves evolving over the bulk surface to produce high-frequency ripples with dispersive behavior customized to the underlying sim.
2. Automate the iteration loop the skill already implies: cache the tracked surface once, then run a parameter sweep over wave speed and sourcing strength with the wave cache disabled, rendering a short preview per setting. Do not re-track for any wave-setting change; if a change forces a re-track, it belongs in a different pass with its own budget.
3. Automate the cost accounting from the paper: log per-frame seconds split into advection, regularization, curvature, Laplacian, and wave stages (the Mercier et al. 2015 paper reports exactly this split, with regularization dominating at roughly half the total), and flag any stage whose share doubles between runs, since that signals a spacing or neighborhood-radius regression rather than a wave-design choice.

**Check**
- Wave-setting previews are produced from the single cached track with no re-tracking step in the log.
- The per-stage timing split is stored with each preview, and regularization remains the expected dominant cost.

**Why**
The production argument for surface detail as a post-process is economic, not aesthetic: the base sim is the expensive part, and detail that can be layered on top without touching bulk motion is detail you can afford to iterate. Weta's wave-curve method and Mercier's surface-turbulence method are two instances of that same argument, and both keep coarse dynamics untouched by design.

Sources:
- https://unity.com/blog/industry/technology-behind-avatar-the-way-of-water
- http://www.thuerey.de/ntoken/download/Mercier_2015_surfaceWaves.pdf

## Depth status

FULL. Source video downloaded (720p), frames reviewed directly, all 946
caption segments read, the Reddit discussion thread read, and the paper
(Mercier et al. 2015) referenced. Every parameter above is quoted or computed
from the video; inferences are labeled.
