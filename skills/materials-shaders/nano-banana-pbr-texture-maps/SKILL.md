---
name: nano-banana-pbr-texture-maps
description: "Generate a complete PBR texture set from one AI image: ChatGPT writes the prompt, Nano Banana Pro draws a 2K 1:1 base color, then converts that same image into normal, ambient occlusion, roughness and displacement maps one at a time with a do-not-reposition instruction, checked by flipping between maps for pixel registration, and assembled in Blender with Node Wrangler. Trigger when a texture set is needed fast from AI generation, or when derived maps must stay registered to a base color."
---

# Nano Banana Pro PBR Texture Maps (ChatGPT Prompts, Blender Assembly)

## Purpose

This skill reconstructs the exact workflow Blender Bros shows in
"Creating 3D Textures is Basically Cheating Now...": ChatGPT writes the
prompt, Nano Banana Pro draws the base color, then Nano Banana Pro
converts that same image into the other four maps one at a time, and
Blender assembles them with Node Wrangler. Every phase has three parts:
**Do** (the action), **Check** (how the human verifies it), and **Why**
(the principle). The core method is: convert, never regenerate; the
do-not-reposition instruction is what keeps the maps registered. The
creator's claim that the result is "mathematically accurate" is his
claim, not a verified measurement, and this skill says so wherever it
matters.

## Source

Creator: Blender Bros / Josh Gambrell. Video: "Creating 3D Textures
is Basically Cheating Now...",
https://www.youtube.com/watch?v=3eHXIzavmHs (15:11, 30,392 views,
uploaded 2026-11-07). Audited in the 2026-11-21 scout run, audit 6.
Evidence: the full ASR captions (412 segments) plus the description,
read firsthand. No media download was used. MaterialWorks 2.0 is
pitched inside this video but is NOT used in the demonstrated
workflow; see Phase 5.

## Tools used

ChatGPT (prompt writing), Nano Banana Pro (image generation, via the
Prompt Edit platform; any Nano Banana platform works per the author),
Blender with the Node Wrangler add-on, Cycles, an HDRI for the check
render. Whisper Flow (dictation) is how the author speaks prompts into
the computer; it is optional.

## When to use this skill

- A PBR texture set (base color, normal, AO, roughness, displacement)
  is needed quickly from AI generation.
- Derived maps must stay pixel-registered to a base color image.
- Deciding whether an AI-generated normal/AO map is trustworthy
  enough to use: use the overlay check in Phase 3, and do not take
  "mathematically accurate" on faith.

## Prerequisites

- Access to ChatGPT (or another prompt-writing model) and to a Nano
  Banana Pro platform (Gemini, AI Studio, Prompt Edit, or any
  third-party platform with Nano Banana built in).
- Blender with Node Wrangler enabled (Preferences, Add-ons).
- A texture subject in mind (the video's example is concrete: "clear
  chips, indentations, the shadows, kind of looking like the rock on
  a side of a mountain almost, a natural concrete-looking texture").

## Phase 1: Get ChatGPT to write the Nano Banana prompt

**Do**
1. Give ChatGPT a basic instruction, not a finished prompt: "generate
   me a prompt for Nano Banana Pro to create a concrete base color
   texture map. Don't generate anything right now except for the base
   color... clear chips, indentations, the shadows, kind of looking
   like the rock on a side of a mountain almost, a natural
   concrete-looking texture. Create a prompt so that way Nano Banana
   Pro can generate that for me."
2. Add the one thing ChatGPT's prompt misses: "we want it to be a 1
   by 1 square texture" (the generation platform can set that as a
   preset).
3. Do not generate in ChatGPT. The author's judgment, quoted: "why
   don't I generate these in Chat GPT? It's because it's garbage...
   Nano banana is significantly better." GPT writes the prompt; Nano
   Banana draws the image.
4. Dictate if faster: the author uses Whisper Flow to speak into the
   computer. Typing works the same.

**Check**
- ChatGPT's prompt must be "very, very specific as to what it wants"
  before it is pasted anywhere. Vagueness at this step is the
  failure mode; the fix is rewriting the instruction, not
  regenerating blindly. Feeding reference images is optional: "as
  long as you explain what you want, then Chat GPT is going to
  actually give you a decent prompt".

**Why**
Prompt-writing and image generation are split across two models on
purpose: GPT is good at writing the specific prompt, Nano Banana is
good at drawing the texture. Using one model for both jobs wastes
the strength of each.

## Phase 2: Generate five base-color candidates, pick one

**Do**
1. Use any Nano Banana platform ("there's a million different places
   to get Nano banana. You have the Gemini, you have this AI studio...
   Use whichever one you want. They're all basically the same").
   The author uses Prompt Edit, "like 10 15 cents to generate one of
   these".
2. Paste the ChatGPT prompt in, choose 1:1 aspect ratio and 2K, and
   generate five versions "just so I can see like what type of a
   texture map I want".
3. Wait "maybe a minute or two" for the generation.
4. Pick the one you like most. The author picks one 2K 1:1 concrete
   map. "This would normally have required you going out, taking a
   picture of like a rock or concrete or something and you would
   have had to do like post-processing effects removing the lighting
   the shadows."

**Check**
- Zoom in on the candidates before choosing: the pick is judged on
  the chips, indentations, and shadow detail at full resolution, not
  on the thumbnail.

**Why**
Generating five costs more than one, but the conversion steps that
follow only need one map, and a bad base color poisons all four
derived maps. The extra generations are the cheap part; a wrong pick
is the expensive part.

## Phase 3: Convert the same image into normal, AO, roughness, displacement

**Do**
1. Download the chosen base color and feed it back to Nano Banana
   with a new prompt, one map at a time.
2. For the normal map, get ChatGPT to write the conversion prompt
   from the image: "I want you to write me a prompt for Nano Banana
   that will tell it to turn this into a normal map. It should not
   reposition any of the pixels or details or anything. All it needs
   to do is convert this into a normal map." ChatGPT's prompt adds
   "the actual normal map information here. The RGB colors that we
   want for a mathematically accurate normal map."
3. Paste the prompt into Nano Banana, drop the generated image in as
   the reference image, 1:1, 2K, one generation ("I only need one
   generation for this... It's only three credits for this which is
   pennies literally").
4. Download the normal map and flip between it and the base color:
   "if I go between them, they are literally perfectly overlaid on
   top of each other. Everything... There's no sort of
   repositioning."
5. Repeat the same ChatGPT-prompt-then-convert loop for the ambient
   occlusion map ("do the same exact thing, but this is going to be
   for an ambient occlusion map"), the roughness map, and finally
   the displacement map ("this one we can physically in the Cycles
   rendering engine like displace it off the surface... better than
   just a regular bump map").

**Check**
- The overlay flip is the acceptance check for every map: base and
  derived must align pixel for pixel with no repositioning or
  redrawing. The author checks it for the normal map and the AO map
  on camera; apply the same check to the rest.
- No numeric alignment measurement is shown in the video.
  "Perfectly overlaid" and "mathematically accurate" are the author's
  visual judgments, not measurements. A render test (Phase 4) is the
  only independent check shown. Do not quote "mathematically
  accurate" as a verified property of AI-converted maps.

**Why**
Converting the same image, with an explicit do-not-reposition
instruction, is what keeps the five maps registered to each other.
Generating each map independently from a text prompt would drift;
converting the chosen image keeps one set of chips, indentations, and
shadows across all five maps.

## Phase 4: Assemble in Blender with Node Wrangler and check in Cycles

**Do**
1. Add a plane, scale it up, apply the scale. Turn on the Node
   Wrangler add-on in Preferences.
2. In the Shader Editor, add a material, press Ctrl+Shift+T, and load
   the maps. Rename the files AO, base color, normal, roughness,
   displacement first ("Just rename them. Not a big deal") because
   Node Wrangler keys off the names.
3. Wire it: displacement into the displacement input, normal through
   a Normal Map node, roughness into the roughness value, base color
   into base color.
4. Wire the AO manually: Shift+A, Mix (Color), set to Multiply.
   Connect base color to the first slot and AO to the second, then
   drag the result into Base Color. ("I think we actually need to
   flip these. The base color should go into the first slot and that
   should go into the second.")
5. Load a simple HDRI, switch to Cycles, and look.
6. Set the AO multiply factor to 0.4 ("Unless you want like a harsh
   shadow... if this is set to zero, it's just going to give it the
   full base color... if you want more of a shadow, set that up to
   one... a normal shadow, you could do maybe 0.5"). Do not push the
   normal strength hard: "Don't go crazy, though. It's just going to
   look weird."
7. Play with the displacement scale ("a little bit heavier if you
   want"), the color (ColorRamp, Hue Saturation Value, or a Mix node
   "for a hint of whatever color"), then add a Solidify modifier,
   apply it, and run Smart UV Project ("because this is using UV
   coordinates... You could use generated if you prefer").
8. Keep the tiling restrained: "You just don't really want this to
   tile too much or it's going to be pretty obvious." Add a bevel
   for a concrete slab example.

**Check**
- The Cycles render with the HDRI is the check: "yep, I can see
  everything loaded in." Judge the displacement read by comparing
  the scale at zero against the scale turned up ("how clean that
  height information comes in compared if this was set to zero").
- Decide the resolution by the use before generating: "If you want a
  higher resolution, you would need to obviously generate at a
  higher resolution. That could be more credits... Is it like a
  super high quality thing? Is it some background element?"

**Why**
Node Wrangler does the mechanical wiring from file names, so the
human work is the two manual decisions: the AO multiply (a look
decision, 0.4-0.5 for normal, 1.0 for harsh) and the displacement
scale. Everything else is naming discipline plus one render check.

## Phase 5: Separate the MaterialWorks pitch from this workflow

**Do**
1. Treat the MaterialWorks mentions as a product pitch, not as steps
   in this workflow. At 08:22: "we have a texturing plugin that has
   already been built off of... mathematically accurate textures like
   this. It's called Material Works, and we just released our 2.0
   version, which has decals, trim sheets, and a full grunge
   generation system built in. All you have to do is install that,
   drag it into Blender, and then you get access to our entire
   library of hard surface details, textures, trim sheets, decals."
2. At 14:38, the pitch repeats with the vendor claim: "It has about
   21 million different texturing permutations. You don't really even
   need to generate your own textures, but if you do want to do that,
   you can also load those into Material Works as well... 50% off for
   the next 48 hours."
3. Record the cost claim for the demonstrated workflow separately:
   "five different texture maps... All these maps I generated in
   under 60 seconds for under a dollar. Honestly, under 50 cents
   using AI" and "I did this in 5 minutes, not even." Those are the
   creator's claims for one concrete example, not a measured average.

**Check**
- No MaterialWorks install, node, library item, or parameter appears
  in the captions. If a future audit cites this video for
  MaterialWorks, it is citing a pitch, not a demonstration.

**Why**
Separating the pitch from the workflow keeps the record honest: the
transferable method is ChatGPT-to-Nano-Banana map conversion, and
MaterialWorks is a separate, untested product claim inside the same
video.

## Failure modes

- **Maps drift apart.** Generating each map from a text prompt
  instead of converting the chosen image repositions pixels. The
  fix is Phase 3: convert the same image, with the
  do-not-reposition instruction, every time.
- **Node Wrangler mis-wires.** File names that do not match the
  expected AO / base color / normal / roughness / displacement
  names break the automatic wiring. Rename before Ctrl+Shift+T.
- **AO in the wrong slot.** Base color must go in the first Mix
  slot, AO in the second. The author corrects himself on camera;
  check the slot order before judging the render.
- **Over-tiling, over-strong normals, over-high displacement.** All
  three read as fake at a glance. Keep tiling restrained, normal
  strength moderate, and displacement scale just high enough to
  read.
- **Believing "mathematically accurate".** No measurement in the
  video proves it. The overlay flip and the Cycles render are the
  checks; the claim is not.

## The human method, distilled

1. Split the models: ChatGPT writes, Nano Banana draws.
2. Generate five, convert one: the pick is cheap, the conversion is
   the commitment.
3. Convert, never regenerate: the do-not-reposition instruction is
   what keeps the maps registered.
4. Flip between maps to check registration; render in Cycles to
   check the look. The author's "mathematically accurate" is a
   claim, not a measurement, until a render proves it.
5. Name the pitch: a product mentioned in a tutorial is not a step
   in the tutorial.

## Depth status

FULL: 412 ASR caption segments plus the description; every prompt
instruction, map, price, and Blender value quoted above is in the
captions. Caveat: the "mathematically accurate" and cost claims are
the creator's, unverified by any measurement in the video.
