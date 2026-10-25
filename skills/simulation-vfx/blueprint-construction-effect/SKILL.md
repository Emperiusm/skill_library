---
name: blueprint-construction-effect
description: "Author a reverse-erosion construction effect: blueprint preview, climbing rim shader, ember particle finish. Trigger when building grow-in VFX."
---

# Blueprint/Construction effect

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Reverse the process: define erosion as the build unit, run it in reverse for the grow-in, and layer blueprint preview, climbing rim, and ember finish.

## Source

Creator: u/craftymech

Source: https://v.redd.it/e4yyvwdinbqh1 | r/proceduralgeneration post 1wjye2x (score 67) | native clip (demo, not tutorial)

## Tools used

Tools used: Unnamed game engine (the author describes a "procedural build system"; engine not stated). Shaders/materials are the author's own: a transparent blueprint material, a separate orange "rim" shader, and "ember" particle effects. Structures are assembled from individual stones and timber beams (author's procedural stone/timber work, per post text and author history visible in the dataset).

**Do**
1. Structures are built from individual stones and timber beams.
2. The procedural build system carries an "erosion" factor that tears the structure down piece by piece.

**Check**
- Confirm the erosion tears down the *full* structure in a legible order (the author relies on it being readable in both directions).

**Why**
The teardown parameter already encodes the build order. Reusing it as the build parameter means the construction animation is free: the system already knows which stone/beam comes in which order.

## Phase 1: Define the build unit: the erosion factor

## Phase 2: Run erosion in reverse: the grow-in

**Do**
1. To "build" the structure, run the erosion factor in reverse: instead of removing pieces, pieces grow in over time.
2. Keep the growth tied to the existing erosion ordering so the assembly reads as construction, not a dissolve.

**Check**
- Watch the reversed pass once through: does the structure emerge in a plausible building sequence (foundation/first stones before the timber/upper parts)?

**Why**
One parameter drives both teardown and construction; no separate build animation is authored. **[inference]** Reversing a teardown curve is cheaper than authoring a second growth curve, and it guarantees the two directions are exact mirrors.

## Phase 3: Blueprint preview material

**Do**
1. Render the unbuilt/queued structure as a "blueprint" view: a transparent material.
2. Blend specular into that material so the lighting on the preview is not flat.

**Check**
- Rotate the camera around the blueprint ghost: the preview should still read as solid geometry (specular highlights on edges/faces), not a flat overlay.

**Why**
A flat transparent tint would read as UI, not as a structure-to-be. Specular blending keeps lighting information, so the player sees *what* is coming, not just *where*.

## Phase 4: The climbing construction rim

**Do**
1. Add a separate shader that renders an orange "rim" on top of the architecture.
2. Animate the rim so it climbs the structure in sync with the grow-in.

**Check**
- Verify the rim tracks the build frontier: the orange edge should always sit where the next pieces are appearing.

**Why**
The rim separates "already built" from "being built" at a glance. **[inference]** A second shader on top of the geometry is used instead of coloring the geometry itself, so the build highlight never contaminates the final material.

## Phase 5: Ember finish

**Do**
1. Throw in a few "ember" particles for a little extra pizzazz.

**Check**
- **[inference]** Check that the particles read as construction/furnace sparks and do not obscure the structure during the grow-in.

**Why**
Author's own words: finish. A small particle pass sells the "hot work of building" without touching the structural system.

### Community note

Commenter RagingPsychoBandit (score 9) suggested moving away from the "futuristic blue" toward a pencil-sketch-on-paper/papyrus look, evoking medieval or Renaissance architectural sketches. Author craftymech replied (score 4): "Thats an interesting idea, I'll have to experiment a little." No change confirmed.

## The human method, distilled

1. **One parameter, two directions.** If teardown is already parameterized, construction is just erosion in reverse; no second system needed.
2. **Build from parts, not blobs.** Individual stones and beams give the grow-in a legible order for free.
3. **Previews need lighting, not just transparency.** Specular blending keeps the blueprint ghost readable as geometry.
4. **Highlight the frontier, not the result.** A separate climbing shader marks the build edge without touching final materials.
5. **Finish is cheap, structure is not.** Ember particles sell the moment; the build order came from the system itself.

## AAA studio practice

**Do**
1. Drive the whole grow-in from one build-progress parameter, exposed as a single scalar (0 to 1) on a Material Parameter Collection or equivalent global parameter, so every part, the rim shader, and the ember pass read the same value. Virtuos's procedural FX pipeline for Age of Empires II: Definitive Edition shows why this matters at shipped-game scale: destruction and construction effects had to stay smooth in frame rate and hold up under close zoom across many structure types, which is only possible when the effect is procedural and parameter-driven rather than hand-animated per building.
2. Automate the part ordering: assign each stone and beam a build index from its structural role (foundation first, then walls, then timber and roof), store it as a per-instance attribute, and reveal parts by comparing build index against build progress. Do not hand-key reveal order per building.
3. Automate the blueprint preview swap: when build progress is below 1, swap the part material to the transparent blueprint material with specular blending; at progress 1, swap to the final material in the same material function, so preview and final can never drift apart.

**Check**
- Scrubbing the single build-progress parameter from 0 to 1 builds the structure in foundation-first order with no part appearing out of sequence.
- The same parameter drives the rim position and the ember emission window, so all three layers stay in sync.

**Why**
RTS placement systems use the same separation in production: a semi-transparent placement material, with collisions disabled while placing, is applied to the ghost and removed on confirm. The blueprint ghost in this skill is that placement state, and the grow-in is the confirm animation; keeping them on one parameter keeps the two states consistent.

Sources:
- https://www.sidefx.com/community/building-a-high-quality-procedural-effects-pipeline-with-houdini/
- https://gameidea.org/2024/12/13/making-building-placement-system-in-rts-game/

## Depth status
 DEPTH-LIMITED (demo clip, not tutorial; no engine, parameter values, or shader code given; the author describes the *concept*, not the implementation. No Check/Why detail beyond what the post text supports.)

---
