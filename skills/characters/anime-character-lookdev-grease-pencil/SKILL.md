---
name: anime-character-lookdev-grease-pencil
description: "Take an illustrated character into 3D and keep the illustrated feeling: Maya blocking, ZBrush detail, Blender lookdev, Substance Painter textures, Grease Pencil outlines with noise, Eevee render. Trigger when a character has to look drawn, not realistic."
---

# Illustrated character lookdev: Maya, ZBrush, Blender, Grease Pencil

## Purpose

This skill reconstructs the exact workflow ManiSalguero used for a 3D study of Laios from Dungeon Meshi, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: translate an illustration into 3D by keeping the illustrated feeling at every stage, and let the hardest part (hair) dictate the method.

## Source

Creator: ManiSalguero

Source: https://www.reddit.com/r/blender/comments/1xoz6o4/laios_dungeon_meshi_3d_project_blender_painter/ | r/blender post 1xoz6o4 (score 1344, 28 comments, 25 retrieved) | cross-post r/Substance3D 1xoz68m (1 comment) | native Reddit clip

Reference: Maeka's fan illustration of Laios from Dungeon Meshi. ArtStation: https://www.artstation.com/artwork/QxarVZ. The author shares the modeling and lookdev process on Patreon.

Depth: PARTIAL — full tool chain + phase order + author technique notes from post text and 25 comments; no brush names, no parameter values, no map/layer detail; the hair method is undisclosed beyond "Grease Pencil and noise".

## Tools used

ZBrush, Maya (blocking; originally an Arnold project), Substance 3D Painter, Blender (final modeling, posing, cameras, lookdev), Grease Pencil, Eevee.

## Phase 1: Blocking in Maya

**Do**
1. Block the character in Maya, establishing proportions and silhouette from the reference illustration.
2. The project started as an Arnold project in Maya (author: "it was originally an Arnold project, but I decided to go to Blender").

**Check**
- The blockout reads as the character from the illustration's angles before any detail work.

**Why**
- Blocking first separates proportion decisions from detail decisions; the illustrated silhouette is the thing that has to survive every later stage.

## Phase 2: Detail sculpt in ZBrush

**Do**
1. Take the Maya blockout into ZBrush and add the final details there (author: "It was mostly modeled in ZBrush, and the blocking in Maya").
2. Spend the most time on the hair: "the most difficult area was, for sure, the hair! It took me so much time to understand and translate the shapes to make them work well in 3D."

**Check**
- The hair reads as the illustration's hair shapes, not as realistic hair: the test is shape translation, not strand fidelity.

**Why**
- Illustrated hair is a set of deliberate shapes; translating shapes is a design problem, not a simulation problem. The author names this as the single hardest part of the whole project.

## Phase 3: Finish in Blender

**Do**
1. Bring the detailed sculpt into Blender to finish the modeling, set the final position, cameras, and lookdev (author: "after having my details in ZBrush, I went to Blender to finish the modeling, final position, cameras, and look dev").

**Check**
- The final pose and camera framing match the illustration's staging.

**Why**
- Blender is the lookdev stage, not the modeling stage: the decision of where the project "lives" is made here, which is why the Arnold-to-Blender switch happened at this point.

## Phase 4: Textures in Substance Painter

**Do**
1. Texture in Substance Painter (author: "Substance Painter for the textures was really fun too!").

**Check**
- [inference] The textures support the illustrated look rather than pushing toward realism; no maps, generators, or layer details were disclosed.

**Why**
- Painter is the texture stage in a pipeline whose look is decided in Blender. No technique detail was given, so do not invent a layer stack for this step.

## Phase 5: Outlines with Grease Pencil + noise

**Do**
1. Draw the outlines with Grease Pencil. The author states the rule plainly: "For the outlines, you need Inverted Hull or Grease Pencil."
2. Add noise to the inner lines: "You can have the inner lines from any painting software, but I like to add a bit of noise to them for the movement."

**Check**
- The outlines read as hand-drawn lines with slight movement, not as clean vector edges.

**Why**
- Noise on the lines is what sells the illustrated feeling in motion: perfectly clean lines read as CG, slightly noisy lines read as drawn. This is the author's stated reason for the noise.

## Phase 6: Final render in Eevee

**Do**
1. Render the final look in Eevee (author: "A lot of grease pencil and noise and Eeve for the final render :)").

**Check**
- The render keeps the illustrated feeling from the reference at the final camera angles.

**Why**
- Eevee is the right renderer for a toon/illustrated look: the look is a shading choice, and Eevee evaluates it in real time while the artist iterates the Grease Pencil lines.

## The human method, distilled

1. **Translate shapes, don't simulate them.** The hair problem is solved by understanding the illustration's shapes and rebuilding them in 3D.
2. **Outlines need a dedicated method.** Inverted Hull or Grease Pencil; there is no default outline.
3. **Noise is movement.** A little noise on inner lines makes a still illustration feel alive.
4. **Switch tools at the lookdev boundary.** Model where the detail tools are (ZBrush), finish where the look is decided (Blender).

## Failure modes

- **Realistic hair on an illustrated character.** The failure the author names is translating the shapes wrong; strand realism is not the goal and will not fix it.
- **Clean outlines read as CG.** Without the noise pass, the lines lose the drawn feeling the whole pipeline is built to preserve.
- **No brush or parameter detail exists in the source.** Do not invent ZBrush brush names, Painter layer stacks, or Grease Pencil settings for this workflow; the source discloses the tool chain and the outline rule, nothing finer.

## AAA studio practice

Two shipped AAA pipelines do exactly what this skill does by hand: make 3D read as 2D illustration.

- **Arc System Works, Guilty Gear Xrd (GDC 2015, technical artist Junya Motomura).** The team's tenet was to "kill everything 3D": 3D models that read as hi-res 2D sprites, with intentionally limited animation, character-specific lighting, and hand-keyed animation in cutscenes. The concrete techniques: handcrafted face normals (edited normals on faces, not the mesh's geometric normals, for a clean anime look); outlines from an inverted model, the same Inverted Hull method the Laios author names as the alternative to Grease Pencil; normal maps used for *less* detail, flattening surfaces instead of adding it; about 40,000 triangles per character so the look survives close-ups; four months per character. Sources: https://www.polygon.com/2015/5/26/8663003/guilty-gear-xrd-cel-shading-making-of and https://videohighlight.com/v/yhGjCzxJV3E
- **Tango Gameworks, Hi-Fi Rush (GDC 2024, graphics programmers Kosuke Tanaka and Takashi Komada).** A deferred toon renderer in Unreal Engine 4 stylizes the entire game, characters and environment, at 60 fps at native resolution. The director's rule was "no color gradations, and nothing that would feel 3D", with three keywords defining the style: "Colorful", "Sharp", "Clean". The custom passes: deferred tone rendering, comic shader, toon light, static shadow map, global illumination, and a toon face shadow implementation. The lesson for this skill: modern lighting (deferred lights, volumetric fog, ambient occlusion, bloom) is restyled into the 2D look, not dropped, so Eevee's real-time lighting is an asset to the illustrated look, not a threat to it. Sources: https://80.lv/articles/the-making-of-hi-fi-rush-s-3d-toon-rendering-style and https://www.unrealengine.com/developer-interviews/hi-fi-rush-was-inspired-by-shaun-of-the-dead-and-futurama?lang=es-ES
- **The Grease Pencil + noise rule is the Blender version of Xrd's outline discipline.** Xrd gets hand-drawn lines from an inverted hull plus hand-keyed per-frame variation; this skill gets the same two ingredients from Grease Pencil outlines plus noise on the inner lines. The noise is not decoration, it is the per-frame variation that keeps lines from reading as clean vector edges.

## Agent automation

- **Face-normal audit.** Run Blender headless with a script that loads the character file and reports, for the head mesh, how many vertices carry custom split normals that differ from the geometric normals. Log `character, head_mesh, custom_normals_count, pass/fail` (pass = count above zero, i.e., the face normals were deliberately edited, per the Xrd rule). If the count is zero, the face is running on raw geometric normals and will shade like CG, not illustration.
- **Outline record.** Keep `outline-record.json` per character: method (Grease Pencil or Inverted Hull), outline color, thickness at three distances (near, mid, far), noise amount on inner lines. Render the character at those three distances and check the outline reads at each; log the render paths in the record.
- **Stepped-animation check.** A headless Blender script that reads the animation curves and reports whether keyframe interpolation is stepped/constant at the target frame rate (the Xrd anime feel comes from stepped animation, not smooth interpolation). Log the interpolation mode per animated object; smooth interpolation on a toon character is a fail.
- **Shadow-band check.** Render one test frame per character, sample the luminance histogram of a lit-to-shadow transition on the face or costume, and count distinct bands. Log the band count; a smooth gradient (many bands) violates the "no gradations" rule and is a fail.
- **Character lighting manifest.** Keep `character-lighting.json`: one entry per character with key-light direction, shadow color, rim color, and the reference illustration it was matched against. Xrd lights each character individually; the manifest is what makes that reproducible instead of a per-shot accident.

**Depth status:** PARTIAL (full tool chain + phase order + author technique notes from post text and 25 comments; no brush names, no parameter values, no map/layer detail; hair method undisclosed beyond "Grease Pencil and noise").
