---
name: ai-3d-format-export-guide
description: "Choose between GLB, FBX, OBJ, USD, and STL for an AI asset by destination, with each format's failure mode and the post-export checks that catch it. Trigger when deciding what file an AI asset should ship as."
---

# Format Export Guide for AI 3D Assets

## Purpose

This skill picks an export format by destination instead of by
generator default, and names how each format fails so the failure is
recognized instead of mistaken for a broken asset. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The core method is: destination
first, format second, verified import always.

## Source

CustomUse learn articles (article text, audited 2026-10-27):

- https://customuse.com/learn/glb-vs-obj-for-web-3d-and-ai-assets
- https://customuse.com/learn/obj-vs-fbx-for-3d-workflows
- https://customuse.com/learn/glb-vs-fbx-for-ai-3d-assets

## Tools used

Tools used: DCC tools and engines as export and import endpoints. No
converter tool is prescribed; the decision table and the import proof
are the deliverable.

## Phase 1: Decide by destination

**Do**
1. Match the format to where the asset is going:
   - GLB: static PBR, web, real-time, and self-contained delivery.
     Geometry and PBR materials travel in one file.
   - FBX: rigs, animation, and engine handoff. The long-standing
     default for rigged and animated assets.
   - OBJ: simple static handoff only. Broadly supported, but carries
     no rig or animation.
   - USD: studio scene assembly and larger studio or virtual
     production pipelines.
   - STL: 3D printing geometry only. No materials, no rig, no
     texture.
2. Decide the format at the intent stage, before generation, not after
   it: re-exporting late costs the checks below a second time.

**Check**
- Can you name the destination and the one format it ingests most
  reliably?
- If the generator exports only one format, is it the one your
  destination needs? If not, stop and re-plan.

**Why**
Every format is a bundle of trade-offs, not a quality ranking. The
"best" format for a web viewer is the wrong format for a rigged
character, and no converter restores data the format never carried.

## Phase 2: Know how each format fails

**Do**
1. Learn the failure contrasts before they happen:
   - OBJ fails quietly: missing rig, animation, and material data
     simply never arrives, and the static mesh looks fine.
   - FBX fails loudly: import errors, warnings, and broken rigs
     announce themselves.
   - GLB degrades the motion: animation and rig fidelity suffer
     first.
   - FBX degrades the look: material fidelity suffers first.
2. When an import looks wrong, check the format's known failure first
   before blaming the mesh.

**Check**
- Imported but missing animation? That is an OBJ-shaped failure, or a
  GLB motion failure, not necessarily a broken rig.
- Imported but materials look wrong? Check the FBX material path
  before re-texturing.

**Why**
Format failures masquerade as asset failures. Knowing the shape of each
failure turns a day of rework into a ten-minute diagnosis.

## Phase 3: Verify the import, every time

**Do**
1. Import the exported file into the real destination tool, not a
   viewer.
2. Verify scale, material slots and texture paths, skeleton (where
   applicable), and axis orientation on import.
3. For animated assets, verify the rig and at least one animation
   survives the round trip. For static assets, verify the PBR maps
   survived as separate maps.

**Check**
- Scale correct, slots intact, maps connected, skeleton present
  where required?
- Would you sign off on this file without reopening the generator?

**Why**
Export is not done when a file exists; it is done when the destination
reads it correctly. The import proof is the only check that catches
format loss, and it is cheap compared with discovering it in a build.

## The human method, distilled

1. Destination first, format second, generator default never.
2. GLB for self-contained PBR, FBX for rigs and engines, OBJ for
   simple static handoff, USD for studio assembly, STL for print.
3. OBJ fails quietly, FBX fails loudly, GLB degrades motion, FBX
   degrades look. Diagnose by failure shape.
4. Import proof is mandatory. A file nobody imported is not an export.

## AAA studio practice

Production pipelines do not pick one format and defend it; they
allocate formats to stages and write the allocation down as a
contract:

- **Hybrid pipelines are the technically correct allocation, not a
  transitional failure.** FBX remains appropriate for compact
  editable character and animation exchange, Alembic for stable
  high-volume caches, glTF for runtime delivery and web-oriented
  interactive publication, and USD when assets must be assembled,
  revised, referenced, and shared across many departments
  (https://accesson.kr/ijcon/assets/pdf/59585/journal-22-2-30.pdf).
  This confirms this skill's destination-first rule and extends it:
  a single asset may legitimately ship as FBX for the animators,
  glTF for the web viewer, and USD for the assembled scene, and the
  skill's decision table should be read per consumer, not per
  asset.
- **A production pipeline needs a documented format contract.**
  Cross-compatibility is not semantic equivalence: FBX importers may
  interpret rig constraints, units, or materials differently, and
  USD may preserve scene description that a given DCC application
  does not fully consume, so a pipeline needs a documented contract
  specifying supported schemas, units, naming, coordinate systems,
  materials, and validation rules
  (https://accesson.kr/ijcon/assets/pdf/59585/journal-22-2-30.pdf).
  The contract, not the format name, is what makes an export
  repeatable.
- **FBX versus GLB is a production-versus-deployment split.** FBX
  remains the standard for DCC interoperability and game-engine
  asset pipelines (editing and development), while GLB leads for
  deployment in browsers and AR/VR runtimes, with smaller files,
  faster parsing, and first-class standardized PBR material
  definitions, at the cost of editability after export
  (https://88cars3d.com/2026/03/26/fbx-vs-glb-choosing-the-best-3d-format-for-ar-vr-and-web-based-3d-experiences/).
  This sharpens the skill's failure-mode table: a GLB that lost
  editability did not fail; it was the wrong format for an editing
  consumer.

**Do (automation additions, appended to the phases above)**
1. Write a one-page format contract per project
   (`format_contract.md`): for each consumer (animators, engine,
   web viewer, print), the format, the schema version, units,
   coordinate system, naming rule, and material rules. Phase 1's
   decision is then a lookup in this file, not a fresh judgment.
2. Extend Phase 3's import proof with a contract check: does the
   imported file match the contract's schema, units, and naming?
   A file that imports but violates the contract fails the proof.
3. When one asset serves multiple consumers, export once per
   consumer from the same source and record all outputs in the
   export manifest (see the engine-export skill), so no consumer
   silently receives another consumer's format.

**Check**
- Does the project have a format contract, and does every export
  name its consumer?
- Did the import proof check the contract, or only that the file
  opened?

## Depth status

FULL (article text).
