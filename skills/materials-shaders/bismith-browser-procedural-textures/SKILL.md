---
name: bismith-browser-procedural-textures
description: "Generate procedural textures in the browser with bismith.dev: start from a starter template, preview tiling live, export greyscale diffuse and separate height maps. Trigger when a texture is needed with zero install and the tiling must be checked before export."
---

# bismith.dev: Browser Procedural Textures

## Purpose

This skill reconstructs the author's exact workflow, step by step, so another
agent can follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The tool's core method is: build procedural textures in the browser from a
starter template, preview tiling live, export the maps.

## Source

Creator: european_impostor. Reddit post:
https://www.reddit.com/r/proceduralgeneration/comments/1xwgwio/bismithdev_a_free_procedural_texture_generator/
(r/proceduralgeneration post 1xwgwio, score 43, 3 comments) | 2026-11-15
scout run, audit 5. Longer video: https://youtu.be/tjT-hcB0bT4
("Bismith.dev Showcase", N2trogen, 558 s, 13 views, no captions).

## Tools used

bismith.dev (free browser procedural texture generator, https://bismith.dev).

## Production practice

Labeled production practice, not AAA: no studio adoption of bismith itself
was found. The AAA anchor is the procedural-texturing discipline bismith
is a browser version of, and the tiling preview is where the two meet.

- **AAA procedural texturing is node-graph, non-destructive, and tileable-first (Naughty Dog, Uncharted 4, GDC 2016).** Naughty Dog adopted Substance Designer for Uncharted 4's environment textures: "By swapping the height map and tweak a few parameters the developers can get a whole new texture set," and Substance became "a sort of content management system including meshes, Maya files, bitmaps, high polygon meshes," outputting the texture. "80% of the textures used in the E3 demo involved the use of Substance" ([DualShockers, GDC 2016 report](https://www.dualshockers.com/amazing-uncharted-4-pictures-show-environments-and-more-naughty-dog-talks-texture-design-at-gdc/)). The bismith equivalent of that discipline: never bake a one-off texture when a parameter change gives a variant, and treat the template as the asset, not the export.
- **The payoff AAA studios cite is iteration speed and reuse (Naughty Dog, Bradford Smith, 80 Level).** "For me, the main advantages are flexibility, modularity, and reuse. Procedural materials can also allow for faster workflow iteration over time (the initial cost of creation is still there, but updates can propagate across assets and variations can be created incredibly fast)." Smith: "I would say that 90% of my textures are fully procedural these days," built from reusable custom nodes around artistic principles ([80 Level](https://80.lv/articles/benefits-of-procedural-materials)). Bismith's starter templates are the same idea at zero install: the template is the reusable node graph; the export is a snapshot.
- **Tileable is the whole product, and AAA scale proves it (Playground Games, Forza Horizon 4; Ubisoft Quebec, Assassin's Creed Odyssey).** "We used Substance Designer to create almost all our... tileable textures.... Almost every... art asset in Forza Horizon 4 had some part of it run through Substance Designer or Substance Painter" (Don Arceta, Playground Games). Ubisoft Quebec: "Thanks to Substance, with a small team of artists we were able to make the productivity rise, creating 1,500 materials to make the world of Ancient Greece back to life" (Vincent Derozier) ([Adobe, Substance 3D in games](https://www.adobe.com/products/substance3d/discover/3d-in-games.html)). The commenter's praise for bismith ("upvoted for easy preview of tiling") is the same bar: a texture that does not tile is unusable, and the preview is where you find out, before export, not after.

## Phase 1: Start from a template

**Do**
1. Open https://bismith.dev.
2. Click File, then New Project, to get a list of starter templates; pick one
   apart to learn the tool (author's instruction).

**Check**
- The template list is the learning path; the author points new users at it
  rather than at docs.

**Why**
- A procedural tool's templates are its documentation. (Inference, labeled.)

## Phase 2: Preview tiling live

**Do**
1. Use the tiling preview to check the texture repeats.

**Check**
- Commenter CorgiCabal (score 2): "upvoted for easy preview of tiling;
  looks superior to other 'online noise generator' i've tried" and "i'd like
  a 3x3 grid next to the 5x5 grid."

**Why**
- Tiling preview is the feature that separates a texture tool from a noise
  toy: a texture that does not tile is unusable, and the preview is where you
  find out.

## Phase 3: Get a greyscale output

**Do**
1. To get diffuse-only greyscale: set the Diffuse gradient to a grayscale
   ramp (right-click on the gradient).
2. Disable Tonemapping in the postprocessing list on the left, "to stop it
   altering the colours" (author).

**Check**
- Commenter CorgiCabal: "it took me entirely too long to figure out how to
  just get a greyscale output. it seems to default to brownish, which maybe
  the defaults shouldn't go that way?" The author answered with the two steps
  above, and added: "What sort of greyscale output are you looking for?
  Height is available as a separate map."

**Why**
- The tool defaults to a colored diffuse; greyscale is a two-step opt-out,
  and height is a separate export, not a gradient mode.

## Phase 4: Export with a manifest and a tiling gate

The tool's two sharp edges are the ones the thread found: tiling you only
trust after preview, and a greyscale path hidden behind two steps. Make
both explicit.

**Do**
1. For every export, write `texture-manifest.json` next to the files:
   template name, Diffuse gradient setting (including the greyscale ramp
   when used), Tonemapping on or off, height map exported or not, and the
   export resolution.
2. Run the tiling gate before calling a texture done: save the 3x3 and 5x5
   preview renders (the commenter's requested 3x3 grid is the stricter
   check; the 5x5 is what the tool shows). If a seam is visible in either,
   the texture is not done, whatever it looks like at 1x1.
3. Save the greyscale path as a starter template of your own (greyscale
   Diffuse ramp, Tonemapping off), so the two-step opt-out becomes one
   click for the next texture. Name it after its use (e.g.
   `greyscale-height-starter`), not after the tool default.

**Check**
- `texture-manifest.json` exists and its settings match the exported
  files; a re-export from the manifest alone reproduces the same maps.
- The 3x3 and 5x5 preview renders are saved with the texture, seam-free.
- The greyscale starter template exists and loads in one click.

**Why**
- Naughty Dog's rule is that a parameter change, not a rebuild, makes the
  variant. A manifest is the parameter record; without it, every export
  is a one-off, and the tool is a noise toy instead of a texture pipeline.

## The human method, distilled

1. Templates first: pick one apart before building from scratch.
2. Tiling preview is the product, not a nicety.
3. Defaults matter: a brownish default cost the author a confused user; the
   greyscale path should be one click, not two hidden steps. (Inference from
   the exchange, labeled.)

**Depth status:** PARTIAL. Post plus 3 comments plus the longer video's
metadata and description (558 s showcase, 13 views). No captions exist for
the video. One media download was used in the scout run but transcription
failed (Whisper model download blocked in the sandbox; not retried). FULL
depth needs a transcript or the author's own breakdown of the node/effect list.
