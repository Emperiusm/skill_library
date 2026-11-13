---
name: trixope-h3-filmmaking-comfyui
description: "Make feature-length films in ComfyUI with the triXope MiniMax H3 nodes: H3 Screenwriter turns any screenplay into a shot list with timestamped story beats and locked-name four-panel character reference sheets, Film Auteur runs the whole H3 pipeline in one node with cross-shot reference conditioning that never re-encodes finished shots, H3 Upscaler upscales and details faces, and the Video Timeline Editor exports libx264 MP4 with no external NLE. Trigger when a script needs to become a finished film in one automated run."
---

# triXope: Fully Automated Feature-Length MiniMax H3 Filmmaking in ComfyUI

## Purpose

This skill reconstructs the triXope filmmaking workflow from the author's post,
step by step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it), and
**Why** (the principle). The core method is: script in, finished film out, no
intervention.

## Source

Creator: Visible-Project-2354 (triXope). Reddit post:
https://www.reddit.com/r/comfyui/comments/1xunyzm/fully_automated_featurelength_minimaxh3/
(r/comfyui post 1xunyzm, score 98, 24 comments). Repo:
https://github.com/triXope/ComfyUI-triXope (install via ComfyUI Manager or drop
into custom_nodes/). The repo includes a basic workflow that is the exact
workflow used to generate the sample video. 2026-11-13 scout run, audit 3.

This is a distinct workflow from the other MiniMax H3 long-form skills in this
library: it is the triXope script-to-screen node set, not the Add Guide
22-frame-overlap recipe (`minimax-h3-addguide-longform-automation`), not the
SelfLift stitching recipe (`minimax-h3-selflift-long-video`), and not the
SyncTile single-trajectory nodes (`minimax-h3-synctile-long-video`). Do not
merge them.

## Tools used

**ComfyUI-triXope custom nodes** (H3 Screenwriter, Film Auteur (H3), H3
Upscaler, Video Timeline Editor), **MiniMax H3**.

## Phase 1: Write the screenplay with H3 Screenwriter

**Do**
1. Feed in a raw screenplay (typed, loaded, or Whisper-transcribed).
2. Screenwriter outputs a complete shot list, including feature-length scripts,
   with timestamped story_beats for micro-direction: framing, action, dialogue,
   and a 3-12 s duration per shot.
3. Let Screenwriter build ready-made reference prompts for every character
   (four-panel sheet: front, strict side profile, rear, face), prop, and
   location.
4. Keep names locked across every prompt, so references and shots always match.

**Check**
- Every character, prop, and location has one locked name used in every
  prompt; a name that drifts between shots breaks continuity downstream.

**Why**
Locked names are the continuity mechanism. The model cannot keep a character
consistent if the prompt calls them something different in shot 40 than in
shot 4.

## Phase 2: Shoot the film with Film Auteur (H3)

**Do**
1. Run the whole H3 pipeline in one node: conditioning, shot planning,
   sampling.
2. In image mode, render the reference prompts as stills in one pass.
3. In video mode, pass any number of reference images, a full storyboard set,
   or text only.
4. Rely on cross-shot context: each shot's tail carries into the next, keeping
   characters, wardrobe, and sets consistent across cuts, including with
   text-to-video.

**Check**
- Shot 500 looks as clean as shot 1. The author is explicit about why: context
  is reference conditioning only, so finished shots are never re-encoded or
  stacked, and there is "no degradation."

**Why**
Re-encoding finished shots is how long-form AI video normally rots.
Conditioning on the tail instead of re-rendering the shot is the invariant
that makes feature length possible at all.

## Phase 3: Upscale with H3 Upscaler

**Do**
1. Upscale in pixel or latent mode.
2. Apply the face swap/detailer for face accuracy, the experimental smart
   sharpener (Refine), DLSS5, and Color FX as needed.

**Check**
- The demo run upscaled from 0.2 MP to 1080p; the author notes the face
  detailer was run quickly and "is not perfect," and that the settings can be
  adjusted to improve its accuracy.

**Why**
Upscaling after generation is cheaper than generating at 1080p, and the face
detailer is where the quality budget goes, since faces are where viewers look.

## Phase 4: Edit and export with the Video Timeline Editor

**Do**
1. Assemble in the editor's two image lanes and two audio lanes, with scrub
   preview, trim, A/V link, and undo/redo.
2. Export a libx264 MP4 with one click and no external NLE.

**Check**
- The exported MP4 is the finished film; no round-trip through Premiere or
  Resolve is needed.

**Why**
The point of the node set is end-to-end automation; an export that requires an
external editor would break the "script to screen" promise.

## Phase 5: Run it fully automated, at any length

**Do**
1. Run the whole chain in a single run with no intervention. The demo video was
   generated as text-to-video at 0.2 MP and upscaled to 1080p entirely with
   these nodes in a single run, "without ever needing to intervene," with
   system RAM and VRAM "way under load."
2. For long runs, let the nodes swap temp files to disk so RAM and VRAM always
   remain clean; the author claims any length, "even as long as 2+ hours."

**Check**
- The picture-in-picture size comparison in the video is the actual ratio from
  before and after the upscale; the author disclaims quality ("This post is not
  to showcase quality, but that fully automated long runs is entirely
  possible") and notes no cherry-picking.

**Why**
Disk-swapping temp files is what converts a long film from a memory problem
into a patience problem. That is the difference between a demo and a pipeline.

## The human method, distilled

1. Lock the names first; continuity is a naming discipline before it is a
   model capability.
2. Never re-encode a finished shot; context is conditioning, not stacking.
3. Automate the boring parts (shot list, references, upscale, edit, export) so
   the human's job is the screenplay.
4. Prove automation with a full unedited run, not a cherry-picked clip.

## Failure modes

- **Face detailer run quickly.** The demo's face detailer was run on quick
  settings and shows it. Budget time for the detailer pass; it is the visible
  quality bottleneck.
- **Names drifting between shots.** If a character's name changes between
  prompts, the reference sheets stop matching and continuity breaks. The
  locked-name rule is load-bearing, not cosmetic.
- **Treating this as a quality showcase.** The author is explicit that the post
  demonstrates that fully automated long runs are possible, not that the output
  is finished quality.

**Depth status:** PARTIAL (full post text, 3,761 characters, with node-level
detail; the 24 comments could not be retrieved: Arctic Shift HTTP 422, old
Reddit JSON 403, PullPush API 403).
