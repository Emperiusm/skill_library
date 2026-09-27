---
name: "houdini_jewelry_saas"
description: "Productize procedural generation: headless Houdini Engine behind an async queue and server pool with a web UI. Trigger when serving procedural systems as a product."
---

# Procedural jewelry system on Houdini Engine (B2B SaaS)

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Sell the engine, not the app: headless Houdini Engine behind an async queue and server pool, with deterministic VDB-and-math topology at the core.

## Source

Creator: Plane-Good-6147

Source: https://v.redd.it/im6mq9nu9prh1 | r/houdini post 1wq2fi7 (score 59) | native clip (demo, not tutorial)

## Tools used

Tools used: Houdini Engine (headless geometry engine), VDBs, Houdini math/solver networks (the deterministic core), an async queue and server pool in front of the Engine licenses, a web interface as the user-facing application, community references to docker-based Houdini web-server tooling (e.g. https://github.com/mushyfruit/houdini-web-rendering-interface as prior art).

**Do**
1. Build the jewelry generator as a Houdini asset graph intended to run headless under Houdini Engine, not as a user-facing Houdini session.
2. Use VDBs and Houdini's math throughout. In the creator's words, this makes "topology fully deterministic."

**Check**
- Deterministic topology is the manufacturability prerequisite: the same inputs must produce the same geometry every time, because downstream tolerances and production tooling depend on it.

**Why**
When Houdini runs as a geometry engine behind a web app, there is no artist in the loop to fix a bad cook. The asset has to be a reliable function of its inputs. VDBs give watertight, topology-stable intermediates; Houdini's math keeps the whole graph recomputable rather than hand-tweaked.

## Phase 1: Build the procedural core as a deterministic asset graph

## Phase 2: Put the Engine behind an async queue, not dedicated sessions

**Do**
1. Do not give users dedicated Engine instances. Run requests through an async queue feeding a server pool of Engine workers.
2. The pool exists because of the cook times: base updates return procedural geometry to the web interface in under 1 second; high-precision geometry for production takes around 3 seconds.

**Check**
- The creator's own scaling claim: because base updates take under 1s and production previews take ~3s, "users don't hold dedicated instances open," so "just a few Engine licenses can easily handle hundreds of concurrent requests (which translates to thousands of general users)."

**Why**
The queue is what turns per-seat licensing into a shared resource. A request occupies a license for seconds, not hours, so license concurrency, not user concurrency, is the unit of capacity. This is the load-bearing architectural decision in the whole project.

## Phase 3: Size the license pool from measured cook times

**Do**
1. Measure the two cook tiers separately: interactive base updates (<1s) and production previews (~3s). These numbers are the capacity model.
2. Buy licenses to cover concurrent cooks, not concurrent users. The creator's math: a few licenses for hundreds of concurrent requests.

**Check**
- Keep the two tiers honest: the sub-1s tier is what makes the web UI feel interactive; the ~3s tier is what makes production output trustworthy. If the base tier slips past a second, the queue model still works but the product stops feeling live.

**Why**
Licensing cost is the scaling variable, so every performance win in the asset graph directly reduces the license pool. The queue architecture and the deterministic topology both serve the same goal: minimum cook time per request, because each second of cook time is a slice of a $525/year license.

## Phase 4: Confront the licensing reality before scaling

**Do**
1. Check the Houdini Engine license terms for SaaS use. The comment thread's flag (jwdvfx): "not sure that the standard Houdini Engine seats would cover it being run for other users."
2. Price it: $525 per head per year (per i_am_toadstorm, from SideFX's website). The top-voted skepticism in the thread (i_am_toadstorm, score 4): "The only real concern with scaling up an application like this is the dependency on Houdini Engine... those license costs add up, so the feasibility of something like this really depends on how many simultaneous users you're planning on having. If this is meant to be customer-facing you will not be able to afford it."

**Check**
- The creator acknowledges the scaling question and counters it with the queue math, but does not claim the SaaS licensing question is resolved in the thread.

**Why**
The scaling constraint here is legal, not technical. The architecture scales; whether the standard seat covers a SaaS deployment is a contract question, and it has to be answered with SideFX before the user count grows, because a retroactive answer changes the unit economics of the entire product.

## Phase 5: Validate manufacturing tolerances with real production

**Do**
1. Fine-tune every real-world tolerance against actual production runs, not just against the geometry in the viewer. The creator: deterministic topology is established by the VDB/math core, "but fine-tuning every single real-world tolerance will definitely require direct production testing."

**Check**
- Deterministic geometry is necessary but not sufficient for manufacturing. The check is a produced piece, not a render.

**Why**
Jewelry has to be made, not just previewed. Casting, milling, and setting impose tolerances the asset graph cannot derive from first principles; the feedback loop from the shop floor back into the procedural graph is part of the product, not a one-time calibration.

## Phase 6: Ship as closed B2B, then early access

**Do**
1. Keep it a strictly B2B pipeline tool (the creator's own framing, not a consumer configurator).
2. Launch sequence as stated: closed testing now, Early Access in about a month, waitlist at beka3d.com/jewelcore, live demo access codes by DM for specific workflows or use cases.

**Check**
- The B2B framing is load-bearing: a pipeline tool has fewer, more tolerant users than a consumer product, which is exactly what a seconds-per-cook queue architecture can serve.

**Why**
The go-to-market matches the architecture. "Strictly B2B" means each account is a production pipeline with predictable cook patterns, which is the usage profile an async pool can actually guarantee. The waitlist and demo codes are how you validate the queue under real load before opening the floodgates.

## The human method, distilled

1. **Houdini as engine, not as app.** Headless procedural cooking behind a dedicated interface is a different product category from user-facing CAD.
2. **The queue is the product.** An async queue with a server pool turns per-seat licenses into a shared resource; without it the licensing math does not work.
3. **Size licenses by cook time, not user count.** Sub-1s base updates and ~3s production previews are the capacity model; a few licenses cover hundreds of concurrent requests because nobody holds an instance open.
4. **Deterministic topology first.** VDBs plus Houdini math make the asset a reliable function of its inputs, which is the prerequisite for headless production use.
5. **The scaling constraint is legal.** Standard Engine seats may not cover SaaS-for-other-users; resolve the contract with SideFX before scaling, because it changes unit economics.
6. **Manufacturing tolerances need the shop floor.** Deterministic geometry does not equal manufacturable geometry; production testing is a standing feedback loop, not a milestone.
7. **B2B matches the architecture.** A pipeline tool's predictable cook patterns are what an async pool can guarantee; ship closed, validate under load, then open early access.

## Depth status
 FULL (post numbers and the licensing thread are concrete; the asset internals shown in the clip are unseen, but the SaaS-architecture reconstruction is fully grounded in the creator's stated figures and the comment discussion).

---
