---
name: agentic-blender-asset-pipeline
description: "Drive Blender as an agent subroutine to build game-ready 3D assets: screenshot-measure-execute-assess loop via Blender MCP, per-asset ASSESSMENT.md files, non-destructive fit studies, human-in-the-loop mechanical correction, Tripo Smart Mesh concept-to-modular-mesh generation, Mixamo FBX export with baked textures, and modular level assembly. Trigger when building game assets with an AI coding agent, setting up an agent-driven Blender workflow, or converting AI-generated meshes into assembled game-ready parts."
---

# Agentic Blender Asset Pipeline

## Purpose

Reconstruct the exact workflow NeuralAlchemist uses live to build game assets for "A Gift For m'Lord" (Tripothon S1 hackathon): an AI coding agent (OpenAI Codex CLI, GPT-6-Astra ultra) drives Blender 5.2.2 LTS through Blender MCP as a subroutine, with the human as art director. Every asset goes through the same loop: **See** (viewport screenshot), **Measure** (scene info), **Do** (execute Blender Python), **Assess** (written ASSESSMENT.md + preview renders), **Correct** (human redirects in plain language). The organizing principle: "OOP is key in game dev, build everything once as often as possible." Every asset is separable parts, every study is non-destructive, every assessment is a file.

**Source:** "Last week of the Hackathon! Tripothon S1 Game build GPT ASTRA" by NeuralAlchemist (6.5 h live, captured 2026-09-28). https://www.youtube.com/watch?v=zTAJlOoT6pw

**Tools used:** OpenAI Codex CLI v0.157.1, GPT-6-Astra ultra, Blender 5.2.2 LTS, Blender MCP (`uvx mcp-for-blender`), Tripo Studio (Smart Mesh P2.0, Nano Banana image model), Mixamo, Level Workshop (localhost web level editor), Unity Asset Store (reference kits), Discord.

## When to use this skill

- Setting up an AI coding agent to do 3D modeling work inside Blender.
- Turning AI-generated meshes (Tripo, Meshy) into fitted, mechanical, game-ready parts.
- Running fit studies and mechanical reviews (doors, hinges, gears) agentically.
- Matching materials to a reference image via agent-written Blender scripts.
- Exporting characters for Mixamo rigging with baked textures.
- Assembling modular AI-generated pieces into levels.

## Prerequisites

- Blender 5.2.2 LTS (or current LTS) installed.
- An agentic coding CLI (Codex CLI used here; any MCP-capable agent works).
- Blender MCP addon installed: run `uvx mcp-for-blender install-addon`, then in Blender go to Preferences, Add-ons, disable and re-enable the addon after any update.
- A Tripo account with credits (Smart Mesh generation shown at 24,060 quads; 26,740 credits on account).
- Project layout: `assets/source/<category>/<asset-name>/` with the `.blend` master, exports in subfolders, assessments next to the asset.

## Phase 1: Set up the agent-Blender loop

**Do**
1. Open the agent CLI in the project root (here `C:\Users\cpere\code_projects\games\aGiftFormLord`).
2. Select the strongest available model (here GPT-6-Astra ultra; the session started on GPT-6-Sol max and was switched with `/model`). Expect large context: the observed session used 1,059,649 tokens total (894,520 input + 29,473,024 cached, 165,129 output, 77,880 reasoning).
3. Verify the Blender MCP bridge: call `blender.get_addon_status`. If the addon file was updated, disable/enable it in Blender Preferences, Add-ons.
4. Open the working `.blend` in Blender and leave it open; the agent operates on the live scene.

**Check**
- `blender.get_scene_info` returns object and material counts (e.g. `materials_count: 6`). If it errors, the bridge is down.

**Why**
- The agent never models blind: every action is preceded by a screenshot and followed by one. The bridge is the only integration; no file round-tripping.

## Phase 2: Generate modular parts in Tripo

**Do**
1. Start from a concept image. In Tripo Studio, generate or edit the concept with the image model (Nano Banana). Example edit prompt: "make the platform around the building more symetrical." Iterate in the Edit Image panel until the silhouette reads.
2. Run image-to-3D with Smart Mesh (quad topology). Example generation prompt: "beige castle with blue conical towers arched windows and a large cen..." (write the full description; the tail was truncated in capture).
3. Generate parts, not wholes: towers, walls, windows, stairs as separable pieces. The castle was generated as a kit for the Level Workshop, not as one mesh.

**Check**
- Inspect the quad mesh in Tripo's 3D view (observed: 24,060 quads). Reject generations with fused parts; you need separable pieces.

**Why**
- "Build everything once": a tower generated once is placed ten times in the level editor. Monolithic generations cannot be reused.

## Phase 3: Fit study (non-destructive)

**Do**
1. Prompt the agent to assess fit before changing anything. The agent saves a separate fit-study scene and leaves it open in Blender. Original assets are preserved untouched.
2. The agent writes `ASSESSMENT.md` next to the asset. The observed bank-building assessment format:
   - **Vault fit:** "The entrance proportions match almost exactly."
   - **Walkability:** "The room has no floor."
   - **Geometry:** "Roof/trim junctions, malformed faces, and inconsistent edges need targeted cleanup."
   - **Textures:** "The 8K image contains blurry detail and baked lighting. Stone, blue roofing, gold, and windows need separate materials."
   - **Back wall:** "Plan for 20 recessed ingot slots, five columns by four rows, with individually placed ingots."
3. The agent renders preview images alongside the assessment.

**Check**
- The fit-study scene exists and the original `.blend` is unmodified. The ASSESSMENT.md has a punch list with owners (geometry, textures, layout).

**Why**
- Destructive edits on AI-generated meshes compound errors. The study scene is where the agent is allowed to be wrong.

## Phase 4: Mechanical refinement (human-in-the-loop)

This is the vault-door workflow, the most demanding part. Parts: ornate frame/ring, door, spoke wheel, gear train, combination dial, hinges, swing arm, locking rods/catches.

**Do**
1. State the mechanical requirement in plain language. Observed prompts:
   - "the door needs to be sized right for the hole and needs to close flush to the ring of the frame"
   - "door needs to SEAL, it needs to be the shape of the hole on the frame at the end of the day. youre deforming the swingarm to" (redirect: fix the door, not the arm)
   - "you have the hinges for the swing arm all wrong as well, the 2 extra loose hinges should mount the right ends of swing arm to the door, on the inside of the fork."
2. The agent runs named review passes and reports diagnoses, e.g. `/root/hinge_cut_review`: "The source door is slightly oval, which explains the uneven fit. I'm reshaping its rim to follow the frame opening." It removes the forward offset on the locking rods "so they can engage the catches."
3. A second pass (`/root/vault_motion_review`) validates the opening animation.
4. Detail pass by prompt: "add some more of the small gears with the round texture holes. Make this look good."

**Check**
- After each pass, `blender.get_viewport_screenshot`. Verify: door rim follows the frame opening, door seats flush with the frame ring, rods engage catches, hinges mount on the correct side.

**Why**
- The agent reasons about geometry (oval door, rod offsets) but cannot reliably reason about assembly mechanics from vision. The human supplies mechanical constraints; the agent executes them precisely. Never let the agent "fix" a fit by deforming the wrong part.

## Phase 5: Material matching to reference

**Do**
1. Supply a reference image; the agent copies it into the project (observed: `textures/stone-castle-reference-2026-09-28.png`, labeled "user-supplied downloaded color/style reference").
2. Prompt: "I want the stone to look AAA and have a color/texture that looks like the image I just downloaded. do a concurrent research" (concurrent tool/material research).
3. The agent writes a matching script (observed: `match_reference_stone.py`, +18 lines) that scans texture variants, e.g. `textures/worn_rock_natural_01_{height,disp,roughness,rough}_4k.png`, and applies them to materials.
4. The agent's report format: "The final stone pass combines the reference's warm cream palette with scanned relief and roughness. I'm checking the full building and a close-up, then saving the materials with their textures packed into the Blender file."
5. Pack textures into the `.blend`.

**Check**
- Viewport screenshot of the full asset and a close-up. Material count rises (observed: 28 materials on the bank building). Textures are packed (no missing files on reopen).

**Why**
- AI-generated textures have baked lighting and blurry detail. The reference-matching pass replaces them with scanned PBR variants in the reference's palette.

## Phase 6: Character export for Mixamo

**Do**
1. Prompt: "lets save the current progress on the model we have open in blender, export him in a format managable for mixamo rigging and..."
2. The agent: screenshots the viewport, reads scene info, saves the character master (`assets/source/hand-of-king/hand-of-king-cleaned.blend`), then exports `assets/source/hand-of-king/mixamo/hand-of-king-mixamo.fbx` **with baked, embedded textures**.
3. The agent returns Blender to the workshop scene "with all parts organized separately and ready to assemble."

**Check**
- The FBX exists in the `mixamo/` subfolder with textures embedded (no external texture dependencies). The master `.blend` is saved before export.

**Why**
- Mixamo needs a clean, textured FBX. Baked/embedded textures survive the upload. The master stays in Blender; the FBX is a one-way export artifact.

## Phase 7: Modular level assembly

**Do**
1. Open the Level Workshop (here `127.0.0.1:5187/level-editor.html`).
2. Place kit pieces (spiral stairs, straight/corner ramps, crenellations, cone/frustum, lancet window, ring/arc) and game objects (Tree, Stone node, Farm plot, Peasant house, Bridge, Pig, War horse) with Move/Rotate/Size gizmos, 0.25 m snap, Z-mirror.
3. Mark walk-through collision per piece ("Solid in walk-through... This object blocks the player and camera").
4. Export JSON ("Layout, not decoration": stairs, rings, and ramps use their actual surfaces during walk-through).

**Check**
- Scene object count tracks placements (observed: 322-324). Export JSON succeeds (autosave can fail; export manually).

**Why**
- The level is data, not a Blender scene. JSON export keeps layout separate from art source.

## Reference discipline

- Unity Asset Store kits are bought or browsed as proportion/style reference (observed: KINGDOM Stylized Modular Castle Environment, Polyart Studio). They are not the asset; they calibrate the agent's output.
- Progress is shared as renders/video (observed: vault door parts and `Safe.mp4` posted to the Tripothon S1 Discord `general-chatting-room`).

## Failure modes seen in the capture

- **Agent deforms the wrong part to force a fit** (swing arm instead of door). Fix: state which part must change.
- **Hinge mechanics wrong.** Fix: describe the correct mounting in mechanical terms (which end, which side, inside/outside of the fork).
- **Baked lighting / blurry AI textures.** Fix: the reference-matching material pass, not texture painting.
- **Built-in gameplay items.** The agent placed ingots as geometry; they are player-placed game items. Fix: "do not place built in ingots, they are game items placed by players." State gameplay constraints explicitly; the agent does not know them.
- **Missing floors.** The agent flagged "the room has no floor"; the human clarified "it will be placed on a foundation." Answer the agent's walkability questions with the actual game context.

## What this skill does not cover

- The Mixamo rigging/animation session itself (prepared but not demonstrated in the capture).
- Unity import of the final assets.
- UV unwrapping as a dedicated pass (materials were matched, not unwrapped on camera).

## AAA studio practice

Two production patterns from shipped games map directly onto this pipeline. First, Ubisoft Montreal's Far Cry 5 team built its procedural world pipeline in Houdini with Houdini Engine integrated into the Ubisoft game editor, so artists used Houdini tools inside the editor they already worked in; the team ran nightly builds on build machines that fully refreshed the world daily, and required deterministic generation (identical results from identical inputs on any build machine) because seamless map junctions and nav-mesh generation depended on it. Second, Blender Studio's own asset pipeline (used on Blender Studio productions) enforces the same discipline at the asset level with pre/post push and pull hooks: production-level Python hooks run automatically around every asset push/pull, so validation and processing are not left to an artist remembering to run them. The agent lesson from both: the loop is only production-grade when validation is automatic, deterministic, and runs on every handoff, not when a human remembers to check.

- Source: https://christianjmills.com/posts/procedural-tools-far-cry-5-notes/index.html (notes on Etienne Carrier, Ubisoft Montreal, Far Cry 5 procedural pipeline)
- Source: https://consolebang.com/threads/the-procedural-world-generation-of-far-cry-5.66431/ (Carrier's own account of the Houdini/Houdini Engine pipeline)
- Source: https://studio.blender.org/tools/addons/asset_pipeline (Blender Studio asset pipeline hooks)

### Agent automation upgrade (Do / Check / Why)

**Do**
1. Turn Phase 3's ASSESSMENT.md into a machine-checked gate, not a prose file alone: after every agent pass, run a headless Blender check (via `blender --background --python`) that reports object count, material count, missing textures, non-manifold geometry flags, and whether the fit-study scene left the original `.blend` unmodified (compare file hash before/after). Append the machine report to ASSESSMENT.md; a prose assessment without it is incomplete.
2. Automate the Phase 4 mechanical rule that the human had to enforce by hand: before any fit fix, record which part is allowed to change (door, not swing arm; hinges mount on the stated side) as a constraint line in the task, and require the agent's pass report to name the part it changed. If the changed part is not the constrained part, revert and re-prompt.
3. Automate Phase 6's export gate: after FBX export, verify the file exists in the `mixamo/` subfolder, textures are embedded (no external texture dependencies), and the master `.blend` was saved before export (timestamp order). Fail the export step if any check fails.

**Check**
- Headless report present in ASSESSMENT.md; original `.blend` hash unchanged after a fit study.
- Agent pass report names the changed part and it matches the stated constraint.
- FBX exists, textures embedded, master saved before export.

**Why**
- Far Cry 5's determinism requirement and Blender Studio's hook pattern agree: a pipeline that depends on a human remembering a check will eventually ship the unchecked asset. The agent's job is to make the check run itself on every pass.
