---
name: rind-godot-pbr-texture-painter
description: "Paint PBR textures directly in the Godot editor with Rind: non-destructive layer stacks, channel-ticked brushes (color, roughness, metallic), masks, material presets, and the exact shortcuts for brush, eraser, blur, smudge, and clone. Trigger when you need hand-painted PBR textures without round-tripping to a separate painting app."
---

# Rind: PBR Texture Painting Inside Godot

## Purpose

This skill reconstructs the Rind texture-painting workflow, step by step, so another agent can paint PBR textures inside the Godot editor the same way. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: load a model from any DCC, build a non-destructive layer stack, and paint material channels (color, roughness, metallic) with brushes that know which channels they touch.

## Source

- Post: "I made a PBR texture painter that runs in the Godot Editor" by tauecar — https://www.reddit.com/r/godot/comments/1xn31es/i_made_a_pbr_texture_painter_that_runs_in_the/ (r/godot, score 176, 13 comments)
- App: https://flareno.itch.io/rind
- Docs: https://docs.flare.no/ (read in full for this skill: introduction, workspace, layers, brushes and tools)
- Evidence: full author post + 13 comments + official docs (2026-11-04 scout run). Price undisclosed in retrieved text.

## Tools used

Rind (texture painter by tauecar); Godot (runs in the editor and as a desktop app); models authored in Blender/Maya; Claude (large parts of the code; base skeleton and first version hand-written by the author).

## AAA studio practice

- **Bake first, paint second (Frozenbyte, Trine series — official internal wiki).** "The info of the high poly mesh is baked into 2D texture maps that can be used on the low poly mesh. This way you get the details of the dense high poly mesh in a much more optimized form that can be used in real time in the game." The bake set: "Bake at least these maps: Normal... World space normal, it's used by many masking generators... ID... AO... Curvature... Position" — and "First bake only the Normal map and test that everything works". Concrete parameters: "Dilation: 16 (2-4 for the color ID map)", "Anti-aliasing: Subsampling 8x8 (Consider lowering for AO, ID and Thickness, for example 4x4)", "Match: By Mesh Name", "Ignore backface: on"; "It's a good idea to bake AO and Thickness separate from the other maps and with a lower AA setting, since they take a lot of time to bake" ([wiki.frozenbyte.com](https://wiki.frozenbyte.com/index.php/3D_Asset_Workflow:_Baking_and_Texturing)).
- **Paint the mask, not the color (Frozenbyte).** "In Substance Painter workflow a lot of the things are done by using mask and painting the mask with black or white revealing the color of the fill layer, less of painting actual colors on things"; "Each layer has color, metal, rough, normal and height channels which can be turned on and off" — Rind's channel-ticked brushes map 1:1 onto this discipline ([wiki.frozenbyte.com](https://wiki.frozenbyte.com/index.php/3D_Asset_Workflow:_Baking_and_Texturing)).
- **Iterative hero assets, reused broadly (Ready at Dawn, *The Order: 1886*).** Senior Environment Texture Artist Bobby Rice: "Ready at dawn practices a iterative process. This means that nothing is truly done after an asset is created initially"; their in-house material system was "a similar system to DDO through what we call the compositor. It was really no different than any other PBR commercial software except that it was proprietary"; "every texture, like the brick, took probably a total of 2 to 3 weeks... these particular textures were re-used throughout 90% of the game" ([polycount.com](https://polycount.com/discussion/comment/2258184/)). Transferable discipline (inference): hero materials get versioned recipes plus a visual gate before reuse; reuse broadly instead of painting one-offs.
- **Texel density + material over mesh (Ubisoft Toronto, *Rainbow Six Siege X*).** Texture artists Ryan Gao and Ramil Laudico: "We also pay close attention to texel density to ensure every surface has a consistent finish and look cohesive compared to each other"; "For the ponds in Skyscraper, we switched from using clutter meshes (think hundreds of generated pebbles whose polycount is very demanding on a game's engine) to displacement mapping (a single, smart texture with improved depth and dimensionality) resulting in a more realistic look and better game performance" ([toronto.ubisoft.com](https://toronto.ubisoft.com/people-of-ubisoft-toronto-meet-ryan-gao-and-ramil-laudico-texture-artists/)).

## Phase 1: Load the model

**Do**
1. Load a model "created in a 3D software of your choice (e.g. Blender, Maya)" (docs).
2. Work in the Godot editor, or run Rind as a normal desktop application ("thanks to Godot's flexibility").
3. Agent-executable: hard-block painting until a bake set passes auto-verification — bake-first, Frozenbyte-style. Script the ordered bake presets: Normal first at low resolution as the smoke test ("First bake only the Normal map and test that everything works"), then World Space Normal + Curvature + Position, then ID, then AO/Thickness last with lower AA ("they take a lot of time to bake"). Concrete parameters: Dilation 16 (2–4 for the ID map), AA 8x8 (4x4 for AO/ID/Thickness), Match by Mesh Name, Ignore Backface on. The skill's existing bake step becomes a scripted checklist, not a manual judgment call.

**Check**
- The model appears in the main viewport; the menu offers save, bake, and reimport.
- The bake-preset log shows Normal-first smoke test passing before the remaining maps bake; painting actions stay disabled until the set verifies.

**Why**
The pitch is freedom from the "shackles of EvilCorp^tm" (author's words): no separate proprietary painter in the loop.

## Phase 2: Build the layer stack

**Do**
1. Press Shift+A and choose a layer type:
   - **Paint layer** / **Material layer** (a material layer starts with a color fill; "Rind doesn't separate the concept of fill and paint layers").
   - **Material layer, paint to reveal**: starts with a blacked-out mask — paint a material onto parts of the model.
   - **Group**: holds other layers (Ctrl+G puts the selection in a new group); groups get their own masks, opacity, and blend mode.
   - **Adjustment layer**: applies color or roughness adjustments to the layers below it.
   - **Text**, **Image decal**, **Material preset** (ready-made materials built from layers).
2. Give a material layer a Base fill plus painted strokes ("this layer is orange here, and blue over here").
3. Reorder by dragging; right-click for Rename, Duplicate, Delete.
4. Agent-executable: encode Frozenbyte's "paint the mask, not the color" rule — every paint layer must be a fill layer plus a mask, with channel ticks (color/metallic/roughness/normal/height) explicitly set per layer. The agent verifies each layer has an explicit channel-tick record before it can be painted.

**Check**
- The stack reads bottom-up: "Layers above override layers below."
- Alt+click a layer to solo it on the model; Esc exits. The eye icon hides/shows.
- The layer audit shows fill + mask + explicit ticks on every paint layer; bare color layers are flagged.

**Why**
Non-destructive layers: "each layer can be changed, reordered or deleted when you change your mind" — the Substance Painter concept, inside Godot.

## Phase 3: Paint the channels

**Do**
1. Select the brush (B or 1); it "paints the ticked channels in the toolbar" — color, roughness, metallic. Untick a channel to leave it alone.
2. Press C to pick a color; the Material swatch sets color + roughness + metallic to a real material (gold, steel, rubber).
3. Control the stroke: Size with F + mouse ([ and ] too); Opacity with Shift+F; Flow (builds toward Opacity over repeated strokes; strokes cannot exceed Opacity); Softness (0% = crisp edge).
4. Pick a preset: Soft square, Soft round, Hard round, Ink pen, Airbrush, Flat bristle, Chalk, Smudge.
5. Choose the stroke type in the toolbar: Paint (default, paints along the drag), Stamp (click to place, drag to size — "very useful for stamping patterns"), Line (straight line from drag start to end); Shift+click draws a straight line from the last stroke's end.
6. With a pen, let pressure change size, flow, opacity, or all three (Response curve in brush settings).
7. Alt+click the model to pick up all channels under the cursor. Shift+X toggles mirror painting.

**Check**
- Cursor color tells you the mode: white = painting into a layer, blue = masks, red = erasing.
- Hovering shows contextual status text: what a click would do, brush properties, shortcut hints.
- Right-click the model → "Preview on the model" paints a preview stroke where you clicked.

**Why**
Channel-ticked painting is the PBR difference: you paint material properties, not just color. The cursor color and hover text are the guardrails against painting into the wrong channel.

## Phase 4: Mask, erase, repair

**Do**
1. Use masks to localize content: masks are black/white images — white = let content through, black = none, grey = partial.
2. Erase with the eraser (2; E toggles brush/eraser; hold Ctrl while painting to erase without switching).
3. Blur with R (or 3) — works on masks too (hold Ctrl+Shift while painting to blur without switching).
4. Smudge with J (or 4); raise Paint to mix in the brush color like a wet brush.
5. Clone with V (or 5): Ctrl+click sets the source; Aligned keeps the source distance across strokes; copy from This layer or All layers.
6. Undo a whole stroke with Ctrl+Z; remove just the stroke end with Alt+Z ("handy when you only want to remove parts of a stroke, not the whole stroke").
7. Agent-executable: automate the two export conventions — (a) per-map engine-ready files plus one combined work file with all layers (Frozenbyte: per-map TGA to version control, combined layered file as the work file), and (b) a texel-density check that computes pixels-per-unit across materials and flags any surface deviating from the target density (Ubisoft Toronto's consistency rule). Both are pure computation, no artist judgment.
8. Agent-executable: store Rind material presets as versioned, inspectable layer-stack recipes (fill layer + mask + parameters) rather than flat presets — replayable, diffable, and iterable, like Ready at Dawn's "compositor" recipe discipline.

**Check**
- The mask view (bottom-left) shows the raw mask; toggle under View > Mask preview.
- Every layer has its own Opacity slider in layer properties — distinct from the viewport stroke-opacity slider.
- The export manifest lists the work file plus every engine map; the texel-density report shows all materials within the target band or flags the outliers.

**Why**
Masks + non-destructive layers mean a painted detail is never committed: reduce the mask or the opacity instead of repainting.

## Phase 5: How it was built (the author's process)

**Do** (the author's account, quoted from the comments)
1. "I have been a software engineer for over 5 years (and hobbyist for 10+) and wrote the base skeleton and first version of the application by hand."
2. "The initial proof of concept was written by hand by me and took about 1 month."
3. "I have used Claude to write large parts of the code" — after 4 months of intense work on this version.
4. "Every image, UI text (1000s of lines), documentation or other asset is human made, either freely available (such as CC0) or created by me. Every feature is planned, designed and tested by me, by hand. Nothing was reverse-engineered or cloned."

**Check**
- "It should work on most hardware, so long as you have the video memory to paint at the resolution you choose." A commenter on an RTX 5090 Mobile (24 GB VRAM) expects no issues; another calls it "super fast and responsive."
- The author wrote full docs before asking for purchases: "I've taken the time to write up some documentation, so you can learn about the app before making any purchase decision." Contact email on the itch page; free copies available on request ("ask for a free copy or cat pictures").

**Why**
Hand-write the skeleton, let the agent scale the code — but keep every user-facing surface human-made. Docs-before-purchase is the trust mechanism for a paid tool from an indie author.

## The human method, distilled

1. The docs are the product (full manual published before the sales ask).
2. Hand-write the skeleton; let the agent scale the code (1-month hand PoC, then Claude for large parts).
3. Human-made everything the user sees (images, UI text, docs).
4. Don't clone: every feature planned, designed, and tested by hand.

**Depth status:** FULL for the painting workflow (docs read: exact keys, brush names, presets, layer model). Inference: itch price undisclosed (page not opened); Godot-editor integration mechanism undisclosed.
