---
name: "houdini_net_break_topo_wedge"
description: "Break a net in slow motion for commercial VFX: curve-spline knot modeling, glue constraints to kill jitter and untangling, procedural art-directed cuts, TOPs wedge runs to dial stretch/stress breakage limits. Cheap constraints before expensive solvers; when a parameter is a guess, wedge it. Trigger when tearing or breaking cloth-like geometry under art direction."
---

# Houdini Net-Break Sim with TOPs Wedge Parameter Sweeps

## Purpose

This audit reconstructs the exact four-step recipe from Chemical-Zebra-5469's
post on commercial work with Derede Studios for Under Armour & Dick's
Sporting Goods, step by step, so another agent can follow the same process.
Every phase has three parts: **Do** (the action), **Check** (how the human
verifies it), and **Why** (the principle). The recipe's core method is: model
the net as clean geometry first, then art-direct the tear with cheap
constraints and batch parameter sweeps — never hand-tune breakage at
slow-motion fidelity.

Related: `layered-vellum-proxy-colliders` (VDB-proxy colliders for layered
cloth) is the same problem class — taming cloth solves — with a different
workflow (proxy colliders instead of glue constraints and wedges).

## Source

Creator: Chemical-Zebra-5469

Source: https://www.reddit.com/r/Houdini/comments/1wz6wld/net_break_sim/
(native Reddit video; r/Houdini post 1wz6wld, score 162, 6 comments;
cross-posted to r/Simulated) | 2026-10-08 scout run. The recipe is the
author's own selftext; comments are fan praise and add nothing technical.

## Tools used

Tools used: **Houdini** — curve/spline modeling, **glue constraints**,
procedural cuts, **TOPs wedge runs**.

## Phase 1: Model knots as clean curves

**Do**
1. Build the net with **curve-based spline modeling** so every knot is
   clean geometry.

**Check**
- Knots are closed, predictable curves with no jitter; the net cannot
  untangle at the modeling level.

**Why**
Starting from clean procedural geometry means the constraints in the next
phase bind to predictable points instead of messy mesh intersections. Knot
quality is a modeling problem, not a solver-tuning problem — getting this
wrong makes every later phase fight the geometry.

## Phase 2: Pin the knots with glue constraints

**Do**
1. Apply **glue constraints** to eliminate knot jitter and untangling.
2. Do not reach for a full constraint network or a heavier solver: the
   requirement is only that the net stays coherent until the tear starts.

**Check**
- Pre-tear, the net holds its shape under tension with no knot slippage.

**Why**
Glue constraints are cheaper than full constraint networks and exactly
match the shot's requirement: coherence before the break, breakage at the
break. Expensive solvers the shot doesn't need are a cost, not a feature.

## Phase 3: Cut procedurally, under art direction

**Do**
1. Tear the net with **procedural cuts**, not a uniform shatter.
2. Let the director re-aim the tear: the cuts are parameters, so a new
   tear path is a parameter change, not a rebuild.

**Check**
- The tear path follows the art direction; torn edges read as fiber, not
  clean slices.

**Why**
The commercial needed a *directed* break (a slow-motion hero moment).
Procedural cuts keep the director's options open: "dial it in" is a
number, not a remodel.

## Phase 4: Wedge the breakage limits in TOPs

**Do**
1. Run **TOPs wedge runs** to dial in the stretch/stress limits at which
   the net breaks.
2. Review the wedge outputs as a matrix of takes; the wedge that breaks at
   the art-directed tension is the one that ships.

**Check**
- The chosen wedge breaks exactly where the director wants, at slow-motion
  inspection — no hand-tweaked "looks about right" single run.

**Why**
Breakage parameters are not tunable by hand at slow-motion fidelity; the
eye catches a wrong threshold instantly. TOPs batch sweeps turn "guess the
threshold" into a reviewable matrix. This is the production-grade version
of "try random seeds until one looks good": a *parameterized* sweep with
named inputs, reviewable as a set. Whenever a parameter is a guess, wedge
it and review the matrix instead of hand-tuning.

## The human method, distilled

1. **Clean geometry before dynamics.** Knot quality is modeling, not
   solver tuning.
2. **Cheap constraints first** (glue), expensive solvers only when the shot
   demands them.
3. **When a parameter is a guess, wedge it in TOPs and review the matrix**
   — never hand-tune a breakage threshold at slow-motion fidelity.
4. **Procedural cuts keep the director's options open**: the tear is a
   parameter, not a remodel.

## Failure modes

- Knot jitter pre-tear: the geometry wasn't clean — go back to Phase 1,
  don't raise solver substeps.
- Tear looks like a clean slice: the procedural cuts aren't fiber-aware;
  re-art-direct the cut pattern, not the solver.
- Breakage looks right at speed but wrong in slow motion: the threshold
  was hand-tuned — re-wedge it in TOPs (Phase 4) and pick from the matrix.

**Depth status:** PARTIAL. The four phases are the author's exact words;
no solver values, wedge counts, substep counts, or frame numbers were
given, and none were invented. The wedge matrix structure (which
parameters were wedged beyond stretch/stress limits) is not specified.
