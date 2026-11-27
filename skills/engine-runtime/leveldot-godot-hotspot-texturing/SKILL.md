---
name: leveldot-godot-hotspot-texturing
description: "Model and texture a Godot level in Leveldot, a standalone level design tool made in Godot: start from a primitive box with a hotspot material, extrude/inset/subdivide faces (Shift+Z extrude), rotate faces into arches, texture on the fly with no manual UV mapping, then export into Godot and walk the level. DEPTH-LIMITED: no transcript; workflow reconstructed from 12 frames read firsthand, the post text, and the author's comments. Trigger when in-editor level authoring in Godot is fought by EditorInterface limits and shortcut conflicts, and the seam to Godot can be an export instead of a plugin."
---

# Leveldot: Extrude + Hotspot Texturing in a Standalone Godot Level Editor

## Purpose

This skill models and textures a level in one standalone tool, with no manual UV mapping, then exports it into Godot. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: material on the primitive first, extrude to grow the structure, texture rides on the face, export and walk it.

## Source

- Video: "Its So Fun To Texture and Model In My Godot Level Editor | Leveldot #3" by Leveldot Editor — https://www.youtube.com/watch?v=6UiPqeQn6pk (109.5 s). YouTube metadata was bot-walled and oEmbed-only, with no captions; the media was downloaded (depth-escalation download 1 of 2) and 12 frames were read firsthand. No transcript exists, so no spoken wording is quoted.
- Post: r/godot 1y58xyl (score 47, 7 comments, all retrieved, including the author's explanations). Scout audit 2026-11-26, audit 1.

## Tools used

Leveldot (standalone level design tool made in Godot, for Godot; the author's own tool, in development); Godot (editor and runtime, for the exported level). No version, license, file format, or release state was disclosed; do not claim Leveldot is released.

## Phase 1: Start from a primitive with a hotspot material already on it

**Do**
1. Open Leveldot (standalone; top bar shows File/Edit/Select/Mesh/Texture/Create/Window/Help, plus Play and Export).
2. Start with a primitive box: frame 0 shows `Box_001`, Primitive Box, Size 2.0 x 2.0 x 2.0, with a concrete texture already applied and the move gizmo on it.

**Check**
- The right-hand Scene panel lists the box under Level 4; the left Surface panel shows the material as "Universal hotspot concrete" (frame-read).

**Why**
The material is assigned before modelling starts, so every face created later already carries texture. The post's framing: "Extruding + hotspot texturing = pure gold."

## Phase 2: Extrude faces to grow the structure

**Do**
1. Select faces and extrude: frame 1 shows "Extrude Faces (2.0, 0.0, 0.0)" with 2 faces selected on the box, stretching it into a slab.
2. Use the Add & Modify tools in the left panel: Extrude, Inset, Subdivide, Push Thru, Opening, More tools (frame-read, all frames).
3. Frame 3's status text reads (frame-read): "1 face, texture and material in the side column - Inset - Shift+Z extrude", i.e. inset and extrude are the paired operations for shaping a wall from a face.

**Check**
- The extruded geometry keeps the concrete texture on the new faces without a UV step; the bottom status bar reports the selection ("Selected: Box_001 Face") and the operation applied.

**Why**
Per the post: "Being able to model and texture geometry on the fly without worrying about manual UV mapping makes the whole process so much more enjoyable." Extrusion is the primary modelling verb; texturing rides along on the face, not on a separate UV pass.

## Phase 3: Inset, scale, and rotate faces into an arch/tunnel

**Do**
1. Inset and scale faces: frame 5 shows a scaled face (Scale Y x1.00, frame-read) forming the front plate of a curved structure.
2. Rotate faces into the curve: frame 6 shows "Extrude Faces applied" on a curved wall segment; frame 8 shows the rotate gizmo on a face inside a stone arch/tunnel.

**Check**
- View the arch from inside and outside (frame 8 is the inside view): the stone texture must read continuously around the curve with no visible UV seam work.

**Why**
[Inference: the arch is built from repeated extrude/rotate operations on faces of one box, not from imported geometry; no import step appears in any frame.] The same two verbs (extrude, rotate) produce both flat walls and curved openings.

## Phase 4: Export into Godot and walk the level

**Do**
1. Export from Leveldot into a Godot project (the Export control is in the top bar in every frame; no export settings are legible in any frame, and none are stated here).
2. Open the exported level in the Godot editor: frame 9 shows the Godot editor with a `level_4` scene, a PlayerCharacter node, and the concrete walls/floor from Leveldot in the 3D view, with movement variables in the inspector.
3. Play and walk through it: frame 11 is a first-person view down a concrete walkway with shadows falling across it.

**Check**
- The in-editor view must match the Leveldot view: same concrete texture, same arch, same proportions. The walkthrough is the final check, not a screenshot.

**Why**
The author built the tool standalone precisely so the Godot side stays a plain level: "I open godot, i want to create my level: leveldot." (comment, author's words, spelling as written). The export, not an editor plugin, is the seam.

## AAA studio practice

- **Blockout first, from primitives, and preserve the hand-authored work when a procedural pass runs over it.** Insomniac's *Marvel's Spider-Man* started from "just a big gray box, designer gray box of Manhattan", judging building spacing and heights from the swinging angle before art work began. In the SIGGRAPH 2019 account of the same pipeline, buildings are blocked in by designers using primitives and then procedurally modularized as a starting point for artist iteration, and the procedural systems were improved specifically to preserve hand-authored work if it continues to meet specifications. That is the production form of Leveldot Phase 1 and 2: a primitive box first, extruded into structure, with the authored shape treated as the thing to preserve, not as a draft to be overwritten by the next tool pass. Sources: https://gamesbeat.com/spider-mans-new-york-makes-webslinging-even-better/ and https://history.siggraph.org/wp-content/uploads/2022/09/2019-Talks-Santiago_Procedural-System-Assisted-Authoring.pdf
- **The AAA direction for level tooling is a unified, always-playable editor, which makes Leveldot's standalone choice a deliberate divergence, not the studio norm.** Ubisoft Massive's Snowdrop engine, presented at GDC 2014 for *Tom Clancy's The Division*, unifies the game and the editor so the project is always playable, with a node-based system running in real time, and procedural environment creation from a limited set of blocks. Leveldot's author chose the opposite seam for a stated Godot-specific reason: inside Godot he would be limited by the EditorInterface API and fighting its native shortcuts, while standalone he can build exactly what he wants and exporting to Godot is still easy. Record that divergence honestly: standalone is justified here by the EditorInterface limits the author names, not by claiming AAA studios build standalone level editors. Sources: https://mcvuk.com/development-news/ubisoft-snowdrop-engine-allows-us-to-work-better-not-bigger/ and http://www.polygon.com/2014/3/19/5524924/the-division-video-snowdrop-game-engine
- **UV-free texturing has a named shader technique, triplanar projection, and it is not proven to be what Leveldot does.** Adobe's Substance 3D Stager documentation states triplanar projection does not rely on the object having UVs at all, projecting the material from the X, Y, and Z axes with seams that can be blended in real time, and that it is best suited to seamless, repeating textures such as rock, plaster, and wood. The same technique is described as the answer for models that have not been UV-mapped, where a single projection would streak and three projections blended by surface normal take over. Leveldot's "hotspot" texturing rides on the face during extrusion with no manual UV step, which is the same user-visible result, but no frame or comment in this skill's evidence names triplanar projection or any other projection method for it. Do not claim Leveldot uses triplanar projection until its projection method is verified firsthand. Sources: https://helpx.adobe.com/substance-3d-stager/desktop/features/material-projections.html and https://iquilezles.org/articles/biplanar/

**Agent automation**

Write `leveldot-manifest.json` beside every level, with exactly these fields: starting primitive size, operation list in order (extrude, inset, subdivide, rotate, with face counts as shown in the status bar), material name per starting face, export settings exactly as shown in Leveldot (empty if none were legible, never filled in from another tool), Godot scene name, and walkthrough result. Fail the run if the export settings field is filled from memory instead of from the Leveldot UI. Then run these gates in order: (1) material-first gate, the primitive must show its material in the Surface panel before any extrusion, mirroring Phase 1; (2) texture-continuity gate, view the arch or curved structure from inside and outside and record whether the texture reads continuously with no UV seam work, mirroring Phase 3; (3) export-parity gate, the Godot editor view must match the Leveldot view in texture, arch, and proportions, and any mismatch is recorded before the walkthrough; (4) projection-verification gate, record Leveldot's actual projection method from its own UI or docs before using the word triplanar for it, per the AAA section above. No version, license, file format, or release state for Leveldot may be entered into the manifest, because none was disclosed. [Inference: the manifest and gates are agent design built from the skill's own frame-read checks.]

## The human method, distilled

1. **Separation of concerns, stated by the author:** "seperation of concerns, i want to script: i open godot, i want to create my level: leveldot." (comment; spelling as written).
2. **Standalone on purpose, not by accident:** "Inside Godot I'd be limited by the EditorInterface API and fighting its native shortcuts all the time. Standalone, I can build exactly what I want, and exporting to Godot is still easy." (comment).
3. **Texture while modelling, never as a second pass:** extrude first, texture rides on the face; manual UV mapping is the step being removed.

## Depth status

DEPTH-LIMITED. No captions or transcript: YouTube metadata was bot-walled and oEmbed-only; 12 frames from a media download were read firsthand, plus the full post text and all 7 comments. No spoken parameters, export settings, file format, or release state were recoverable, and none are invented. A transcript would add the author's spoken settings and the export details; it would not add a UV workflow, because the video's point is that there is none.
