---
name: opentwin-3dgs-point-maps
description: "Build a 3D Gaussian splat digital twin from as few as 5 drone photos the way evilspyboy did with OpenTwin: point maps are the base format, the COLMAP plus DroneSplat flow is augmented with stitched CVPR projects, SAM 3.1 removes moving cars, and lidar projects marry separate point maps. Trigger when you need a maintainable 3DGS twin of a real area from cheap drone photos."
---

# OpenTwin: 3DGS Point Maps from 5 Drone Images

## Purpose

This audit reconstructs the exact workflow from evilspyboy's post and comments, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The post's core method is: point maps are the base format; everything else is a replaceable stage around them.

## Source

Creator: evilspyboy. Post: "A lot of cool stuff gets posted in this sub and I try to use it to learn about new tech/projects that can help...", https://www.reddit.com/r/photogrammetry/comments/1xxal2o/a_lot_of_cool_stuff_gets_posted_in_this_sub_and_i/ (score 43, 6 comments). Evidence: full post text (2,777 characters) and all 6 comments read firsthand. 2026-11-17 scout run.

## Tools used

Tools used: **OpenTwin** (author's own project, plans to open source), **COLMAP**, **DroneSplat** (flow augmented, not followed), **SAM 3.1** (remove moving cars), assorted lidar projects (marry separately created point maps), **~12 CVPR 2023-2026 projects** and open-source CV models (unnamed individually by the author), LLM-assisted coding for the integration. Input: a lower-end drone without RTK support.

## Phase 1: Start from the file format you need, not the tool you have

**Do**
1. State the need: digital-twin 3DGS-type files for a specific area, and no publicly available "working" files existed for that country.
2. Build OpenTwin to convert what the author had into point maps, because the file output was needed to continue other work: "I needed the file output to develop something else."
3. Accept the input constraint: a lower-end drone without RTK support, which means "a pretty big variance... even between flights and taking off from the exact same spot."

**Check**
- The demo output above the post is from only 5 images: that is the author's proof the workflow is right before scaling to a bigger area ("I still have to build out an 'augment' workflow... I just need to create a bigger area to load test now").

**Why**
"The most important thing about building software is to always spend a LOT of time figuring out if you actually need to or not." (author comment, quoted.) He built it only because the alternative was $10k+ in hardware/software or hundreds/thousands for a professional, and the output was blocking other work.

## Phase 2: Stitch the pipeline from replaceable parts

**Do**
1. Take the COLMAP + DroneSplat flow as the base workflow, then change out sections "that I thought could be improved" rather than following it whole.
2. Pull sections from about a dozen CVPR 2023-2026 projects and open-source CV models, including some "not for making point maps", and use them to augment the flow.
3. Use lidar projects to marry separately created point maps; use SAM 3.1 to remove cars from the streets that would be moving between pictures.
4. Use LLM-assisted coding for the integration: "this would be integration hell and I needed the file output to continue my other work not this actual application itself... the number of projects I've stitched together would be months (optimistically) otherwise."

**Check**
- Each stitched section must work on the input generally, not just on one set of images: the author warns that LLM-written code "has a habit of making the solution work with the input instead of being universal. I just know what to look for so I keep pulling it up when it does that."
- Consistency rule: "If you can be consistent in your approach it will go a long way."

**Why**
Point maps are the base format and "everything since has that as a stepping stone." Building blocks that work together beat a monolith: "aim for building blocks that work together" (author comment, quoted).

## Phase 3: Maintain the area over time, don't just snapshot it

**Do**
1. Build an "augment" workflow to use older and newer pictures together: enhance common points, throw away changes.
2. Build a "replace" workflow for the reverse (swap in the new state).
3. Aim to maintain an area over time rather than snapshot it once; stitch different days/weeks/months through control points on non-moving objects (brickwork, chimney, outside buildings), per the commenter's own BIM-at-home plan that the author endorses in the same thread.
4. Publish it when done: "I will probably just make this available when I'm done, it uses too many open source projects" to keep closed.

**Check**
- Load-test on a bigger area before calling the workflow right: the 5-image output is a correctness check, not a scale proof.

**Why**
The author's use is maintenance over time (a changing site), so a snapshot pipeline would rot: the augment/replace pair is the design, not an afterthought.

## The human method, distilled
1. "Point maps are the base format and everything since has that as a stepping stone." (author comment, quoted.)
2. "Try not rush to get the end result and aim for more how does what I do today contribute/support/build on/build together." (author comment, quoted.)
3. "Spend a LOT of time figuring out if you actually need to [build software] or not." (author comment, quoted.)
4. "If you can be consistent in your approach it will go a long way." (author comment, quoted.)

## Failure modes
- Non-RTK drone variance: the same takeoff spot gives different positions between flights. Fix: solve the variance as a first-class stage (control points on non-moving objects) instead of assuming the drone's GPS.
- LLM-written stages that work only on the test input: the author's stated failure mode. Fix: test every stitched section on a second, different image set before trusting it.
- Moving cars between pictures: they corrupt the point map. Fix: SAM 3.1 removal before the solve.
- 5-image proof mistaken for scale proof: the author is explicit that the bigger-area load test is still to do.

## AAA studio practice
Point clouds as the base format is standard photogrammetry practice: COLMAP is the standard open-source structure-from-motion solver, and every production capture pipeline (RealityCapture, Metashape, drone mapping) treats the point cloud as the intermediate everything else derives from. The distinctive choice here is designing for maintenance over time (augment/replace workflows, control points on permanent structures) instead of a one-off snapshot, which is how survey-grade digital twins are specified.

### Agent automation upgrade (Do / Check / Why)
**Do**
- Automate the generality check the author does by hand: run every stitched stage against two disjoint image sets (different days, different light) and diff the point maps; any stage whose output changes materially between sets gets flagged for review.
**Check**
- The diff report names the stage and the magnitude of the change, so the LLM-integration failure mode is caught by a test instead of by the author's eye.
**Why**
- The author already knows the failure mode ("making the solution work with the input instead of being universal"); a two-set diff turns that knowledge into a gate.

**Depth status:** FULL (full post text, 2,777 characters, + all 6 comments read firsthand; the ~12 CVPR projects are unnamed by the author, so no individual project is claimed).
