---
name: retrocrunch-ps1-godot-conversion
description: "Convert any model into a PS1-style Godot 4 scene with Retrocrunch: give it OBJ/glTF/FBX and a triangle budget, get back a .glb, an indexed .png, lossless .png.import settings, and a .tscn with the PS1 material already assigned. Trigger when a Godot project needs the PS1 look without hand-building the shaders."
---

# Retrocrunch: PS1-style Godot 4 scene conversion

## Purpose

This skill reconstructs the exact workflow of Retrocrunch, a free tool by Laegh that converts any model into a PS1-style Godot 4 scene, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: give it a model and a triangle budget, get back a Godot scene that already looks like a PS1 game.

## Source

Creator: Laegh

Source: https://www.reddit.com/r/godot/comments/1xoo4c6/free_tool_convert_any_model_into_a_ps1style/ | r/godot post 1xoo4c6 (score 47, 12 comments, 10 retrieved) | native Reddit clip

Repo: https://github.com/bbayram-l/retrocrunch (open source) | itch.io: https://laegh.itch.io/retrocrunch (sample pack with converted models and ready `.tscn` files)

Models in the clip: Lion Head by Tina and Boombox by Thomas Paul Mouilleron (CC0, Poly Haven). The code was written with an AI coding assistant (author-disclosed; the author reviews what it writes; the godot-ModTeam flagged AI-generated post text in the thread).

Depth: FULL — tool spec fully stated by the author in post text + comments, with exact outputs, material parameters, and the open-source repo linked for verification; no hands-on run this run.

## Tools used

Retrocrunch (free, Windows, open source). Inputs: OBJ, glTF, FBX. Outputs: `.glb`, indexed `.png`, `.png.import` (lossless settings), `.tscn` with PS1 material. Runs locally.

## Phase 1: Convert with a triangle budget

**Do**
1. Give Retrocrunch an OBJ, glTF, or FBX model.
2. Choose a triangle budget.
3. Retrocrunch writes: a `.glb`, an indexed `.png`, and a `.png.import` with lossless settings ("no VRAM compression smearing the palette").

**Check**
- The indexed palette survives import: lossless `.import` settings mean the palette is not smeared by VRAM compression.

**Why**
- The triangle budget is the design input: the PS1 look is a polygon count as much as a shader. The lossless import setting is what protects the palette, which is the other half of the look.

## Phase 2: Get a ready PS1 scene

**Do**
1. Retrocrunch writes a `.tscn` with a PS1 material already assigned: vertex snapping, affine warping, 15-bit colour with the console's dither table.
2. Rigs, skin weights, and animation clips survive the conversion.
3. Optionally add the 240-line screen pass over the whole game.

**Check**
- Drop the folder into a Godot project and open the scene: the sample pack on the itch page ships converted models with ready `.tscn` files for exactly this check.

**Why**
- The material is the look: vertex snapping + affine warping + 15-bit colour + dither table are the four PS1 artifacts, and shipping them pre-assigned means the user never has to build the shader themselves.

## Phase 3: The rest of the tool (author's comment)

**Do**
1. 8-direction sprite sheets with a billboard scene.
2. Normal maps for 2D sprites (CanvasTexture).
3. Block-built levels with baked AO and collision.
4. All in the same download.

**Check**
- [inference] Each of these is a separate feature of the same tool; no usage detail was given for any of them.

**Why**
- Retrocrunch is a small PS1 pipeline, not a single converter: the sprite, normal-map, and level features cover the rest of a PS1-style game's asset needs.

## The human method, distilled

1. **Budget first, shader second.** The triangle budget and the PS1 material are both inputs to the same conversion; neither alone makes the look.
2. **Write the import settings, don't leave them to defaults.** Lossless `.import` is what keeps the palette honest.
3. **Ship a sample pack.** Ready `.tscn` files are the proof the tool works and the onboarding.

## Failure modes

- **VRAM compression smears the palette.** This is the exact failure the lossless `.png.import` setting exists to prevent; if the palette looks wrong after import, check the import settings before blaming the material.
- **The tool is Windows-only and local.** It runs on Windows; no web or Linux build is mentioned.
- **The sprite/normal-map/level features have no usage detail in the source.** Do not invent their workflows; the source names them only.
- **AI-assisted code, author-reviewed.** The author states the code was written with an AI coding assistant and that he reviews what it writes; the repo is public for verification.

## AAA studio practice

Naughty Dog built the original PS1 look under the same constraints Retrocrunch recreates, and their production rules map directly onto this tool's inputs. Source: Andy Gavin's Crash Bandicoot postmortem, https://all-things-andy-gavin.com/tag/sgi/

- **The triangle budget is a hard contract, not a suggestion.** Crash himself was 512 polygons, a month spent settling that number, and Naughty Dog enforced a visible-polygon budget per view (800 for Crash 1, 1,300 for Crash 2 and 3) with visibility and occlusion precomputed on an SGI workstation farm. Retrocrunch's triangle budget is the same discipline as an input: set it per asset, then verify the output is inside it, don't eyeball it.
- **Vertex colors beat textures where the camera gets close.** Naughty Dog used shaded, untextured polygons with corner (vertex) colors on characters instead of textures, because that dodged the PS1's affine texture warping and stretching. Crash's pupils were 2-polygon quads so they could never vanish below a pixel. The rule for Retrocrunch conversions: for hero or close-up assets, prefer vertex colors, or subdivide large textured planes (smaller triangles mean less warp per triangle; the real PS1 games did exactly this). Subdivision source: https://dev.to/tommy91dev/how-to-get-the-ps1-look-in-godot-4-vertex-snapping-affine-warping-dither-57mo
- **Bake once, pay nothing at runtime.** Crash's characters used vertex animation: Naughty Dog stored the location of every vertex, every frame, at 30 fps, because the PS1 could not match the 3-4 joint weighting of PowerAnimator at runtime. Retrocrunch is the same shape: all the PS1 work happens at conversion time (baked .glb, indexed palette, pre-assigned material) and costs nothing per frame.
- **Precompute the expensive decisions offline.** Visibility and polygon sorting were precomputed for hours on a 5-8 machine farm because the PS1 had no z-buffer and no easy sort. A conversion tool is the modern version of that farm: spend conversion time so the game doesn't spend frame time.
- **What Retrocrunch does not emulate: the missing z-buffer.** The PS1 had no depth buffer, so one triangle could completely cover another based on draw order; emulator-derived PS1 renderers use one flat depth value per triangle to fake this. Source: https://jettelly.com/blog/recreating-the-ps1-s-rendering-quirks-in-godot/ Retrocrunch's material (snap, affine warp, 15-bit color, dither) does not claim draw-order emulation, so if overlapping geometry sorts wrong in a converted scene, that is the known gap, not a material bug. [inference: the gap is inferred from the jettelly description of PS1 draw-order behavior against Retrocrunch's stated material features.]

## Agent automation

- **Batch conversion manifest.** Write `retrocrunch-manifest.json`: one row per asset with `input`, `triangle_budget`, and the four expected outputs (`.glb`, indexed `.png`, `.png.import`, `.tscn`). A script runs Retrocrunch once per row and fails the run if any of the four outputs is missing.
- **Budget gate.** After each conversion, read the `.glb` JSON chunk, sum the triangle counts across mesh primitives, and fail the row if the total exceeds the manifest's `triangle_budget`. Log `asset, budget, actual, pass/fail` to `retrocrunch-budget-log.csv`.
- **Warp-risk check.** Before conversion, list source triangles whose longest edge exceeds a recorded threshold (set per asset; default the mesh's median edge length x4) as affine-warp risks; either subdivide those faces or switch them to vertex colors, per the Naughty Dog rule above. Record the decision per asset in the manifest.
- **Palette gate.** Parse each `.png.import` as text and fail the row if the lossless setting is absent or off; this is the automated version of the skill's Phase 1 check.
- **Conversion regression log.** Keep `retrocrunch-log.jsonl` with one line per conversion (asset, budget, outputs, gate results). Re-running the manifest must reproduce identical outputs, or the log must say what changed.

**Depth status:** FULL (tool spec fully stated by the author in post text + comments, with exact outputs, material parameters, and the open-source repo linked for verification; no hands-on run this run).
