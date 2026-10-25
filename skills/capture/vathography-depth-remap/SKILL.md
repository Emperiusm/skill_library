---
name: vathography-depth-remap
description: "Turn a photograph's hidden depth pass into the artwork: estimate a detailed depth map from a single photo with Marigold V2 (Apache 2.0, commercial OK), then remap it in the Blender compositor with a Color Ramp to compose volume, mist, and focus. Trigger when a depth map should be shown, not hidden."
---

# Vathography: Depth-Map-as-Artwork with Marigold V2 and Blender

## Purpose

This skill teaches the Vathography workflow end to end: estimate a fine-detail
depth map from a single photograph, then remap it in Blender's compositor
until the volume becomes the artwork. Every phase has three parts: **Do**
(the action), **Check** (how the human verifies it), and **Why** (the
principle). The core method is: a depth map is a technical pass made to be
hidden; Marigold V2 made it detailed enough to show.

## Source

Creator: Karim Joseph Nassar (karijoart), multidisciplinary digital artist,
canton of Bern, Switzerland; practice published 1 October 2026. Intro video:
https://www.youtube.com/watch?v=EjohqO3GP90 (2:37, manual captions). Blender
tutorial: https://www.youtube.com/watch?v=ZALSOni2XQk (3:08, ASR captions,
exact steps). Practice page: https://vathography.com. Audited 2026-10-05.

## Tools used

**Marigold V2** (single-image depth estimation; Apache 2.0 license, free even
for commercial use; team: Igor Pavlovic, Thiemo Wandel, Anton Obukhov, Luca
Bartolomei, Andrey Davydov, Fabio Tosi, Matteo Poggi, Sabine Süsstrunk,
Dengxin Dai). Depth estimation routes: **ComfyUI native Marigold V2
implementation** (https://docs.comfy.org/tutorials/utility/marigold-v2; no
third-party custom nodes needed) or the **Hugging Face demo**
(https://huggingface.co/spaces/toshas/Marigold-V2; free for a few photos a
day; uploads are processed on HF servers, so avoid private images). **Blender**
compositor (Color Ramp node) for the remap.

## Phase 1: Estimate the depth map

**Do**
1. Start with any photograph, including ones already in the archive: "Depth
   estimation is a post process. We can apply it to any photograph we already
   have."
2. Run Marigold V2 via the ComfyUI native implementation. The author warns
   that some community custom nodes have carried malicious code and notes you
   need none for this; stay on the official implementation.
3. For a quick test with no install, use the Hugging Face demo (a few free
   photos a day; do not upload private images).
4. Export the depth map as EXR for Blender.

**Check**
- The V2 release is the enabler: finer detail in a single-photo depth map.
  If the map looks blobby at subject edges, the photo (not the settings) is
  usually the limit; try a higher-contrast capture.

**Why**
The depth map used to be an intermediate pass (Photoshop uses it for lens
blur, never shown). V2's detail crosses the threshold where the volume
rendition carries an artwork on its own.

## Phase 2: Set up the Blender compositor

**Do**
1. Render tab > Color Management: set View to **Standard**, so no view
   transform is applied to the images.
2. Switch to the Compositing tab, click New. Delete the Render Layers node
   and the Group (Output) node (select, X); only the Viewer node stays.
   Disable the backdrop button.
3. Drag-drop the depth EXR into the compositor; connect its image output to
   the Viewer input. In the Image Editor, select the Viewer node from the
   dropdown to preview it.

**Check**
- The preview shows raw depth values with no color transform. If the image
  looks tone-mapped, the View is not Standard.

**Why**
No rendering happens here; the compositor is used as a pure image-remap
bench, so the render nodes are clutter and any view transform would corrupt
the depth values.

## Phase 3: Remap with the Color Ramp

**Do**
1. Add a **Color Ramp** node (Shift+A, search "color ramp") dropped onto the
   connection so it auto-connects.
2. Mist-pass look: set the background stop to white and the foreground stop
   to black; change interpolation to **B-spline** for a gradual haze
   instead of a sharp cut.
3. Isolate a depth range: bring two stops closer together to isolate that
   slice of the depth ("isolating this range of the depth").
4. Colorize freely: stops can be any color (the tutorial demos a blue); "you
   can get creative like this."
5. Image > Save As to export the vathograph.

**Check**
- Read the scene by depth and volume, not light and color. The focus is now
  "the area we choose to highlight", and several subjects at different
  depths can be highlighted at once. If the subject of interest does not
  separate, tighten the stops around its depth slice.

**Why**
Remapping turns a technical grayscale pass into a composed artwork: the
artist chooses what the volume emphasizes instead of accepting the raw
depth output.

## The human method, distilled

1. New capability, new practice: when a hidden pass gets good enough, make
   it the artwork instead of hiding it.
2. Shoot with purpose: "the most interesting vathographs will come from
   photographs taken with purpose"; read scenes by depth and volume at
   capture time, which "draws us to different subjects, different
   compositions, different stories."
3. Keep the toolchain boring: stock ComfyUI plus the stock Blender
   compositor, no exotic nodes, so the practice is reproducible by anyone.

## Failure modes

- **Tone-mapped depth**: Color Management View left on Filmic/AgX; set it
  to Standard before importing the EXR.
- **Cluttered node graph**: Render Layers and Group Output nodes left in;
  delete both, keep only the Viewer.
- **Subject won't separate**: stops too far apart; bring them closer to
  isolate the subject's depth slice, or re-shoot for more depth contrast.

**Depth status:** FULL (manual captions for the intro + 80-segment tutorial
captions with exact Blender steps).

## AAA studio practice

Production compositing has always treated depth as a first-class control
signal, not a hidden pass. Vathography's move (show the depth map) is the
artistic inversion of the studio move (drive focus, fog, and layer order
from the depth map). Both depend on the same discipline: clean,
high-bit-depth depth, and an explicit mapping from depth value to effect.

- **Foundry Nuke ZDefocus.** Nuke's GPU-accelerated ZDefocus node creates
  camera defocusing from a depth pass: choose a focus point and blur the
  image according to the depth map channel, which is how studios match
  lens characteristics between CGI and plate and animate rack focus in
  post without re-rendering.
  Source: https://www.foundry.com/products/nuke-family/nuke/features?ref=discover-the-rookies
- **Marigold depth pipeline (official).** Marigold's depth pipeline
  outputs predictions in [0, 1] with an ensemble mode that improves
  accuracy and yields uncertainty estimates from variance across
  predictions, and exports 16-bit PNG depth (values mapped linearly to
  [0, 65535]), which is the format that survives a compositing round trip
  without banding.
  Source: https://huggingface.co/docs/diffusers/main/en/api/pipelines/marigold
- **Depth-driven layer ordering (See-through pipeline).** Production-style
  layered pipelines mask a global depth map by each layer's alpha, take
  the median depth of the non-transparent pixels, and sort layers back to
  front by that median, splitting a layer when one label spans two
  disconnected depth ranges.
  Source: https://deepwiki.com/jtydhr88/ComfyUI-See-through/2.3-marigold-depth-estimation-pipeline

**Do (agent-executable, automation upgrade)**
1. Add a depth-QC step after Phase 1: export both the 16-bit depth PNG
   and the ensemble uncertainty map. Flag any subject edge where
   uncertainty is high and depth is discontinuous; those edges will
   halo under any remap or defocus, and the fix is a better photo or a
   tighter mask, not a wider Color Ramp stop.
2. Extend Phase 3 with the studio mapping discipline: before colorizing,
   record the depth-value range of each subject (sample the median depth
   inside a mask per subject, as the See-through pipeline does), then
   place Color Ramp stops at those measured values instead of by eye.
   Save the stop positions with the artwork so the remap is reproducible.
3. Add a second, production use for the same depth map as a check: run
   the depth through a ZDefocus-style blur (focal plane at the hero
   subject's median depth) and confirm the subject stays sharp while
   foreground and background fall off. If the hero does not separate
   under defocus, it will not separate under a color remap either.

**Check**
- Depth values for each subject are numbers in the project notes, not
  slider positions remembered by feel.
- The 16-bit depth export, not an 8-bit preview, is the file that enters
  Blender; 8-bit depth banding is visible in any smooth mist gradient.

**Why**
A depth map shown as art is judged like any other image: banding, halos,
and mushy subject separation read as defects, not style. The studio
discipline (measure depth per subject, keep 16-bit precision, check with
defocus) is what keeps a vathograph from being a posterized gradient.
