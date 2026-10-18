# NeuralAlchemist Tripothon S1 Live Audit: The Agentic Game-Asset Pipeline

**Source:** https://www.youtube.com/watch?v=zTAJlOoT6pw
**Title:** "Last week of the Hackathon! Tripothon S1 Game build GPT ASTRA"
**Creator:** NeuralAlchemist (TQStudios.Dev, @NeuralAlchemist, neuralalchemist_ on Twitch)
**Captured:** 2026-09-28, from the beginning of the live. ~6.5 hours (23,368 s) of 720p.
**Game:** "A Gift For m'Lord" (aGiftFormLord), beta launching Oct 5. www.tqstudios.dev
**Audit depth:** FULL. Visual review of 48 full-resolution frames across the entire capture plus terminal/prompt text. Full transcript processing separately.

## The pipeline in one paragraph

This is the most complete agentic 3D game-asset pipeline captured on video to date. The loop is: **Tripo** (AI image concept with Nano Banana, then image-to-3D via Smart Mesh P2.0, quad topology) generates modular parts; **OpenAI Codex CLI running GPT-6-Astra ultra**, wired into **Blender 5.2.2 LTS via Blender MCP** (`uvx mcp-for-blender`), performs fit studies, writes per-asset ASSESSMENT.md files, executes Blender Python to reshape geometry, fix mechanics, and match materials to references, verifying its own work with viewport screenshots; the human directs and corrects (hinge placement, door fit, gear details); characters go **Blender to Mixamo** via baked-texture FBX; modular pieces assemble in a web-based **Level Workshop** (localhost:5187) and export JSON; **Unity Asset Store** kits serve as style/proportion reference. The stated philosophy, from his chat: "OOP is key in game dev" and "build everything once as often as possible."

## Tool inventory (exact, as observed)

| Tool | Version / detail | Role |
|---|---|---|
| OpenAI Codex CLI | v0.157.1 | Agentic coding harness |
| Model | GPT-6-Astra ultra (switched from GPT-6-Sol max mid-session) | Reasoning + tool use |
| Blender | 5.2.2 LTS | DCC, all modeling/assembly |
| Blender MCP | `uvx mcp-for-blender install-addon` | Agent-to-Blender bridge |
| Tripo Studio | studio.tripo3d.ai, Smart Mesh, quad output | Image-to-3D generation |
| Tripo image gen | Nano Banana model | Concept/reference images |
| Mixamo | (browser tab open) | Character auto-rigging |
| Level Workshop | 127.0.0.1:5187/level-editor.html | Modular level assembly, JSON export |
| Unity Asset Store | KINGDOM: Stylized Modular Castle Environment, Polyart Studio, $74.50 (50% off $149) | Reference kit |
| Discord | Tripothon S1 Hacker Community | Sharing progress (Safe.mp4) |
| Token usage (one session) | 1,059,649 total; 894,520 input (+29,473,024 cached); 165,129 output (77,880 reasoning) | Scale of agentic context |

Host machine is Windows (`C:\Users\cpere\code_projects\games\aGiftFormLord`), PowerShell (`Get-Item -LiteralPath`, `Get-Content -LiteralPath ... -Encoding UTF8`).

## Project structure (as observed)

```
aGiftFormLord/
  assets/source/architecture/bank-vault/bank-vault.blend      # vault door workshop
  assets/source/architecture/bank-building/bank-building.blend
  assets/source/architecture/bank-building/ASSESSMENT.md
  assets/source/architecture/bank-building/match_reference_stone.py
  assets/source/architecture/bank-building/textures/worn_rock_natural_01_{height,disp,roughness,rough}_4k.png
  assets/source/architecture/bank-building/textures/stone-castle-reference-2026-09-28.png
  assets/source/hand-of-king/hand-of-king-cleaned.blend       # character master
  assets/source/hand-of-king/mixamo/hand-of-king-mixamo.fbx   # baked, embedded textures
```

Convention: `assets/source/<category>/<asset-name>/` holds the `.blend` master, generated exports go in subfolders (`mixamo/`), assessments live next to the asset, reference images are user-supplied and copied into the project.

## Asset 1: The bank vault door (part-by-part safe build)

The centerpiece. Built and refined live as separable parts: ornate frame/ring, the door itself, spoke wheel, gear train (large and small gears), combination dial, hinges, swing arm, locking rods/catches.

### Workflow

1. **Fit the door to the frame.** The agent reshapes the door rim to follow the frame opening. Human prompt: "the door needs to be sized right for the hole and needs to close flush to the ring of the frame." Agent response: "I'll tighten the fit to the frame opening and move the closed door back until its rim sits flush with the frame ring."
2. **Seal requirement.** Human: "door needs to SEAL, it needs to be the shape of the hole on the frame at the end of the day. youre deforming the swingarm to" [truncated]. The agent had been deforming the swing arm to compensate; the human redirects it to fix the door shape instead.
3. **Hinge correction (human-in-the-loop).** Human: "you have the hinges for the swing arm all wrong as well, the 2 extra loose hinges should mount the right ends of swing arm to the door, on the inside of the fork. the left" [truncated]. The agent cannot reason out hinge mechanics from vision alone; the human supplies the mechanical constraint.
4. **Hinge-cut review.** The agent runs a dedicated review pass (`/root/hinge_cut_review`), diagnoses: "The source door is slightly oval, which explains the uneven fit. I'm reshaping its rim to follow the frame opening." It also removes a forward offset on the locking rods "so they can engage the catches."
5. **Motion review.** A second pass (`/root/vault_motion_review`) validates the opening animation ("Vault - Opening Anima..." visible in Blender).
6. **Detail pass.** Human: "dd some more of the small gears with the round texture holes. Make this look good" (reads as "add some more of the small gears...").

### What this demonstrates

The agent does real mechanical reasoning (oval door, rod offsets, flush seating) but needs human correction on assembly mechanics. The pattern is: agent proposes via viewport screenshot, human corrects in plain language, agent re-executes. Every review is a named, repeatable pass.

## Asset 2: The bank building (agentic AAA pass)

1. **Fit study.** The agent saves "a separate fit-study scene and left it open in Blender. Original assets are preserved." Nothing destructive; studies are separate scenes.
2. **ASSESSMENT.md.** Written per asset at `assets/source/architecture/bank-building/ASSESSMENT.md`. The captured assessment covers:
   - **Vault fit:** "The entrance proportions match almost exactly."
   - **Walkability:** "The room has no floor."
   - **Geometry:** "Roof/trim junctions, malformed faces, and inconsistent edges need targeted cleanup."
   - **Textures:** "The 8K image contains blurry detail and baked lighting. Stone, blue roofing, gold, and windows need separate m[aterials]."
   - **Back wall:** "Plan for 20 recessed ingot slots, five columns by four rows, with individually placed ingots."
3. **Gameplay constraint from the human.** "the building does not need a floor, it will be placed on a foundation. also do not place built in ingotsm, they are game items placed by players." Agent: "Understood, the foundation will provide the floor, and the back wall needs 20 empty slots for player-placed ingots."
4. **The AAA instruction.** Human: "go ahead and make this building a AAA asset." This is the standing order that triggers the full cleanup/material pass.
5. **Material matching to reference.** Human: "I want the stone to look AAA and have a color/ texture that looks like the image I just downloaded. do a cuncurrent research" (concurrent). The agent:
   - Copies the user-supplied reference into the project as `textures/stone-castle-reference-2026-09-28.png`.
   - Writes `match_reference_stone.py` (edited live, +18 lines) that scans texture variants (`worn_rock_natural_01_{height,disp,roughness,rough}_4k.png`) and applies them.
   - Reports: "The final stone pass combines the reference's warm cream palette with scanned relief and roughness. I'm checking the full building and a close-[up], then saving the materials with their textures packed into the Blender file."

## Asset 3: The castle (Tripo concept-to-modular-mesh)

1. **Concept image in Tripo** (Nano Banana model). Prompt visible: "make the platform around the building more symetrical." Iterated in the Edit Image panel with history.
2. **Image-to-3D via Smart Mesh.** Prompt fragment: "beige castle with blue conical towers arched windows and a large cen..." Output: quad topology, 24,060 quads. Cost meter visible: 26,740 credits.
3. **Modular intent.** The castle is generated as separable pieces for the Level Workshop kit (towers, walls, windows as placeable parts), consistent with the "build everything once" philosophy.

## Asset 4: The hand-of-king character (human workflow)

Human prompt: "lets save the current progress on the model we have open in blender, export him in a format managable for mixamo rigging and" [truncated]. The agent:
1. Calls `blender.get_viewport_screenshot` and `blender.get_scene_info` (6 materials).
2. Saves the character master: `assets/source/hand-of-king/hand-of-king-cleaned.blend`.
3. Exports `assets/source/hand-of-king/mixamo/hand-of-king-mixamo.fbx` **with baked, embedded textures** for Mixamo rigging.
4. Opens the vault workshop scene with "all parts organized separately and ready to assemble."

The Mixamo leg (upload, rig, animate) was not captured in the sampled frames; the browser tab was open. Treat rigging/animation as prepared-but-not-demonstrated in this capture.

## Asset 5: Level assembly (Level Workshop)

A web-based level editor at `127.0.0.1:5187/level-editor.html` ("LEVEL WORKSHOP - A Gift For M'Lord"):
- Placeable game objects: Tree, Stone node, Farm plot, Peasant house, Bridge, Pig, War horse.
- Modular kit pieces: spiral stairs, straight/corner ramps, crenellations, cone/frustum, lancet window, ring/arc.
- 322-324 scene objects; Move/Rotate/Size gizmos; 0.25 m snap; Z-mirror; Export JSON.
- The castle is assembled from the Tripo-generated modular pieces here. "Layout, not decoration" note visible: pieces need walk-through collision ("Solid in walk-through").

## The agent's operating pattern (the real workflow to copy)

1. **See:** `blender.get_viewport_screenshot` after every change. The agent looks at its own work.
2. **Measure:** `blender.get_scene_info` (object counts, material counts), `blender.get_addon_status`.
3. **Do:** `blender.execute_blender_code` with generated Python. Blender MCP is installed via `uvx mcp-for-blender install-addon` (disable/enable in Preferences after update).
4. **Assess in writing:** per-asset ASSESSMENT.md with fit, walkability, geometry, textures, and a punch list. Preview images rendered alongside.
5. **Never destroy:** fit studies are separate scenes; "Original assets are preserved."
6. **Take human correction literally:** hinge placement, door sealing, gameplay constraints (no floor, no built-in ingots) are applied as stated.
7. **Report like a contractor:** "Worked for 12m 50s", "Worked for 6m 44s", file paths, what was saved where.

## Demonstrated vs inferred

- **Demonstrated:** the full agent-Blender loop, vault door part refinement, bank building AAA pass, Tripo concept-to-mesh, character master save + Mixamo FBX export, level assembly, reference-kit browsing, Discord sharing.
- **Not demonstrated in this capture:** the Mixamo rigging/animation session itself, the final Unity import, any UV-unwrap-specific work (materials were matched, not unwrapped on camera), the exact Tripo text prompt tails (truncated in frame).
- **Inferred:** the live began ~6.5 hours before capture end (23,368 s of media); the "22:24" in the working title was not the stream start.

## Why this matters (gap analysis)

This is the first captured instance of the **agentic DCC workflow**: an AI coding agent driving Blender as a subroutine (screenshot, measure, execute, assess) under human art direction. It maps directly onto the known pipeline gap of AI-assisted mesh splitting, UV, material, and assembly cleanup, but goes further: the agent performs fit studies, mechanical correction, and material matching as named, repeatable passes. The "build everything once" modular philosophy (OOP for game assets) is the organizational principle that makes the agent's output reusable: every asset is separable parts, every study is non-destructive, every assessment is a file.

## Follow-ups

- Full transcript (6.5 h) is processing; spoken prompts and narration will be folded into a v2 of this audit.
- The live was still running at capture end; a second capture can extend coverage (Mixamo session, Unity import) if warranted.
