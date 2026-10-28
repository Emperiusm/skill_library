---
name: ai-3d-scene-cinematic-vfx
description: "Direct AI 3D for VFX and cinematic work from a scene, not a prompt: scene-as-source-of-truth, camera and blocking control, continuity across cuts, and an eight-question readiness checklist. Trigger when a sequence, not a single frame, must hold together."
---

# Scene, Cinematic, and VFX Workflows for AI 3D

## Purpose

This skill judges VFX and cinematic work by whether one change survives
without breaking the rest: camera, light, subject, and continuity
across cuts, not single-asset quality. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The core method is: store decisions as scene
data, direct like a film set, and gate tools on the readiness
checklist before committing them to a sequence.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/ai-3d-for-vfx-artists
- https://customuse.com/learn/ai-scene-generation-assets-to-worlds
- https://customuse.com/learn/ai-3d-tools-for-vfx
- https://customuse.com/learn/ai-vfx-tools-3d-creative-stack
- https://customuse.com/learn/ai-3d-for-cinematic-content

Evidence note: the VFX readiness checklist section of one member
article was read firsthand by the parent agent; all substantive
sections were read.

## Tools used

Tools used: AI generators (Meshy, Tripo, Hunyuan and similar) for raw
assets; scene-anchored workspaces for camera, blocking, lighting, and
continuity; DCC tools and engines for handoff (FBX, GLB, USD export).
The strongest category for directed work is the scene-anchored
workspace, not any single generator.

## Phase 1: Build the scene before rendering anything

**Do**
1. Build the scene as the source of truth: geography, camera and lens,
   character poses and blocking, prop positions, and lighting, all
   stored as scene data rather than described in prompts.
2. Work in layers from assets to worlds: individual assets, assembled
   sets, lit environments, and finally sequenced shots. Maturity
   rises with how much of the stack persists between renders.
3. Treat AI rendering as a layer on top of the scene, not as a
   per-frame prompt: the scene holds the lighting and the camera, so
   the render inherits them.

**Check**
- Can you point to the stored camera, lens, pose, and light values?
- If the prompt box disappeared, would the scene still exist?

**Why**
Prompt-only tools re-interpret the description every run, so camera,
character, props, and lighting drift. A scene stores decisions; a
prompt re-guesses them. That is the entire difference between a shot
and a sequence.

## Phase 2: Direct the shot like a film set

**Do**
1. Set the exact camera and lens, and store them as data.
2. Pose characters and block the scene explicitly, in world space.
3. Preserve the same scene across shots: every shot inherits the same
   geography and look, so a camera move or a changed element
   re-renders only the affected shots while everything else stays
   locked.
4. Run two-shot acceptance tests: render two shots from the same
   scene and confirm continuity (same geography, same light, same
   subject) holds across the cut.

**Check**
- Do two shots from the same scene match on geography, light, and
  subject?
- Can one element change without a full reroll of the sequence?
- Is the element change recorded as a named override layer with the
  shots it affects, not as a re-published scene?

**Why**
VFX is decided one constraint at a time: this camera, this lens, this
blocking, this key light, held without drift across every cut. A tool
that cannot hold those constraints cannot hold a sequence, however
good its single frames look.

## Phase 3: Run the eight-question readiness checklist

**Do**
1. Before committing any AI 3D tool to a sequence, run it through
   these eight pass/fail questions:
   - Can I set the exact camera and lens? Pass means camera and lens
     stored as data, not a prompt.
   - Can I control character pose and blocking? Pass means pose and
     world-space placement are explicit.
   - Can I preserve the same scene across shots? Pass means the scene
     persists and is reusable.
   - Can I change one element without breaking the rest? Pass means
     element-level edits without a full reroll.
   - Can I export the assets and references I need? Pass means
     FBX, GLB, and USD plus frame and note export.
   - Can teammates review the setup, not just the output? Pass means
     a shared canvas or review surface.
   - Can I build a sequence, not just a single frame? Pass means shot
     chaining and continuity tooling.
   - Does it fit my existing handoff (comp, engine, DCC)? Pass means
     clean integration with current tools.
2. Weight the checklist toward the hardest current shot.

**Check**
- If a tool fails several questions, is it priced as a reference
  generator rather than a pipeline component?
- Are the failures recorded, so the team does not rediscover them
  mid-sequence?

**Why**
A tool that fails the checklist can still be useful for mood
exploration or quick references. The failure is only expensive when
it is discovered after the tool was committed to a sequence.

## Phase 4: Stack the five jobs and hand off cleanly

**Do**
1. Staff the VFX stack as five jobs, not one tool: generation, scene
   layout, texturing, render-layer control, and a workspace tying
   them together.
2. Inspect generated assets before they enter shots: topology, UVs,
   scale, and materials typically need cleanup first. Treat generated
   output as a concept-to-blockout accelerator, then run the
   production checklist and export to the pipeline.
3. Hand off through standard interchange (FBX, GLB, USD) and verify
   scale, axis orientation, and that materials and UVs survived.

**Check**
- Does every job in the stack have an owner and a handoff format?
- Did assets survive export with scale, axes, materials, and UVs
  intact?

**Why**
No single tool covers the stack, and pretending one does is how
sequences end up with beautiful frames that cannot be comped, lit, or
continued. The stack framing keeps each job's requirements visible.

## AAA studio practice

Production VFX and cinematic work stores the scene as composable
data and edits it with sparse overrides, not full re-publishes:

- **USD as the scene language.** USD is the core of Pixar's pipeline
  and the first publicly available system for robustly interchanging
  and augmenting whole scenes: assets assemble into sets, scenes,
  shots, and worlds in a single scenegraph, and departments edit
  non-destructively through overrides, with one consistent API
  across modeling, shading, animation, lighting, FX, and rendering.
  A controlled benchmark found a sparse USD update layer was only a
  small fraction of the base file where FBX and Alembic updates
  required republishing nearly complete files.
  (Sources: https://openusd.org/release/intro.html?ref=confusing-acronym.com and https://accesson.kr/ijcon/assets/pdf/59585/journal-22-2-30.pdf)
- **Dual-format assets and a modular real-time pipeline.** Milk
  VFX built its real-time pipeline modularly so hybrid shots mix
  Unreal-generated elements with Houdini USD-pipeline elements,
  integrated at compositing; assets are designed dual-format
  compatible so they move between Houdini and Unreal, scene
  import/export runs through an in-house plug-in suite, and
  rendering uses Lumen or path tracing per shot with final polish
  in compositing.
  (Source: https://vfxvoice.com/welcoming-the-cultural-shift-to-virtual-production/)
- **The camera drives the scene, live.** ILM's StageCraft renders
  the LED-volume environment live from tracked camera position and
  orientation, so perspective, lighting, distortion, and depth of
  field update as the camera moves; roughly half of The
  Mandalorian's scenes were shot inside the volume.
  (Source: https://techcrunch.com/2020/02/20/how-the-mandalorian-and-ilm-invisibly-reinvented-film-and-tv-production/)
- **Automation (agent-executable):** store camera, lens, blocking,
  and light values as USD layer data (never prompt text); make an
  element change as a sparse override layer and log the layer name
  plus the shots it affects, instead of re-publishing the scene;
  run the dual-format import check (Houdini and Unreal both open
  the asset with scale, axes, materials, and UVs intact) as a
  pass/fail record; save the two-shot continuity captures as files
  per shot pair. (Inference: these steps apply the USD and
  dual-format practices above to this skill's Phases 1-2.)

## The human method, distilled

1. Scene first, render second. Decisions stored as data survive;
   decisions described in prompts drift.
2. Direct like a film set: camera, lens, blocking, light, all explicit.
3. Two shots must match. Continuity is the acceptance test.
4. Eight-question checklist before committing a tool to a sequence.
5. A tool that fails the checklist is a reference generator. Price it
   as one.

## Depth status

FULL (article text).
