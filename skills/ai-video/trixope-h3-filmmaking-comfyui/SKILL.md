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

## AAA studio practice

Script-to-screen as one pipeline, with references locked before volume, is
how studios are now running AI video. Runway and Lionsgate expanded their
partnership in June 2026 (Lionsgate took equity; the original September 2024
deal was the first Hollywood studio plus applied-AI-company partnership),
with Runway tools used "across pre-visualization, storyboarding and
final-frame production" and a custom model trained on Lionsgate's 20,000+
title library (John Wick, Hunger Games, Twilight), exclusive to Lionsgate
filmmakers. Source: Runway, "Runway and Lionsgate Expand Partnership",
https://runway.com/news/company-news/runway-and-lionsgate-expand-partnership

Runway's AI previs discipline fixes the order: script, breakdown, shot list,
reference frames, lock references, motion clips/animatic, director/DP
review, shooting plan/techvis. The load-bearing rule is "lock references
before generating volume, not after" and "prompt text alone will not hold
them." In a fully generative pipeline "there is no crew. Previs and
production collapse into one loop, because the frame you approve becomes the
frame a video model animates and the shot list becomes the generation queue."
The limit is flagged too: AI previs "does not produce measurable space", so
rigs, performers, and set builds still need traditional previs/techvis.
Source: Runway, "What is AI previs?", https://runway.com/resources/ai-previs

The shot list itself is a structured, numbered inventory: shot number, scene
ref, framing, angle, movement plus speed, subject/action, lens, lighting,
duration, and "what the shot reveals". Pipeline order: "script, script
breakdown, shot list, storyboard, animatic, generation or shoot day. Each
stage inherits the decisions of the one before it." Consistency comes from
structure: "When each shot entry includes structured references to characters
and locations, the shot list becomes a consistency map", with two to three
reference images gathered per character at the shot-list stage, not after
generation starts. Source: Runway, "AI shot list: how to build a
camera-ready plan", https://runway.com/resources/ai-shot-list

The never-re-encode invariant has a studio-grade justification in Pixar's
USD pipeline: USD layering is non-destructive "very much like Photoshop
does, with a set of individually stacked operations which can be turned on
or off without affecting any of your data", variants let artists swap
shape/shading/texture per shot without touching geometry, and "Pixar is keen
on leaving the rendered pixel as intact as possible to avoid unnecessary
pixel filtering and ensuing image degradation during post-processes."
(Applying USD layering to a ComfyUI video pipeline is an analogy, not a
Pixar-endorsed practice for AI video; Pixar's source is about 3D scene
data.) Source: Pixar, "Pixar's USD Pipeline",
https://renderman.pixar.com/stories/pixars-usd-pipeline

ILM StageCraft shows the same forward-flow principle at full production
scale: over 50 percent of The Mandalorian Season One was filmed on a 20 ft
high, 270-degree LED wall (75 ft diameter volume) with Unreal Engine/Helios
real-time rendering and camera-tracked perspective-correct imagery, and
StageCraft 2.0 is "an end-to-end solution; everything from the early stages
of previz and working with the art department, all the way through motion
capture, and now, working with live pixels on set". Previs assets flow
forward into final pixels instead of being thrown away; the triXope analogue
is that the approved storyboard/reference frame becomes the shot, not a
disposable sketch. Source: ILM, "Groundbreaking LED Stage Production
Technology Created for Hit Lucasfilm Series 'The Mandalorian'",
https://www.ilm.com/groundbreaking-led-stage-production-technology-created-for-hit-lucasfilm-series-the-mandalorian/

The pre-AI version of the four-panel reference sheet is Weta Digital's
Hobbit workflow: digi-doubles built from "scans and photographic reference
of the actors. In particular, turntable shoots of the characters in costume,
plus close-up photography of pieces of clothing, armor and make-up", with "A
CG turntable of the final character could then be easily compared to the
original reference", and a shared "Gen Man" base asset adapted per
character. Source: fxguide, "Weta Digital's models supe on The Hobbit",
https://www.fxguide.com/fxfeatured/weta-digitals-models-supe-on-the-hobbit/

For the timeline editor, DNEG moved its editorial pipeline onto Foundry's
Hiero, which combines "multi-shot management, conform, editorial and review
workflow functionality with the shared Nuke timeline" and "lets them monitor
progress and share feedback in context": "Hiero's Python API allowed us to
build a one-stop shop for our entire editorial pipeline... Custom soft
effects, timeline-driven Nuke farm rendering, and even ShotGrid cut
comparisons built directly into our own panels. Our team can conform,
publish, and track changes against production without ever leaving the
timeline." Source: AWN, "DNEG Moves Its Editorial Pipeline onto Foundry's
Hiero", https://www.awn.com/news/dneg-moves-its-editorial-pipeline-foundrys-hiero

One caution from a directly comparable ComfyUI production pipeline: Ubisoft
La Forge built a 3-stage ComfyUI pipeline (texture synthesis, material
estimation, 2x/4x upscale) because "ComfyUI provides us with an efficient
framework to build integrated workflows", but artists judged the results
"not production-ready yet" and upscaling "suffer[s] from error accumulation
along the pipeline". Upscale last, on locked masters, and never chain
upscales. Source: Ubisoft La Forge, "Generative Base Material",
https://www.ubisoft.com/en-us/studio/laforge/news/1i3YOvQX2iArLlScBPqBZs/generative-base-material-an-opensource-prototype-for-pbr-material-estimation-debuting-at-siggraph-asia-2025

No GDC talk was found that directly documents long-form AI-video continuity;
the strongest material is the ILM StageCraft and previs practice above.

### Agent automation

- **Shot manifest and reference-lock gate.** Emit one machine-readable
  manifest per film (JSON): shot_id, scene, story_beat timestamp,
  framing/angle/movement/speed, lens, lighting, duration, reveals/purpose,
  locked character/prop/location names, and reference-image file paths plus
  hashes. Agent check before any generation: every name in the manifest
  resolves to exactly one reference sheet, and every shot references the
  sheet by hash, not by re-typed name. Add a Weta-style approval gate:
  render a CG/reference turntable still per character and require a
  side-by-side pass before that character's shots are queued.
  (Grounded in Runway's shot-list and lock-references-first rules and Weta's
  turntable comparison.)
- **Immutable masters and layered finishing manifest.** Write finished shots
  once to `shots/<shot_id>/master.*` and never overwrite them; upscale,
  face-detail, and grade outputs go to separate `variants/` paths recorded
  in the manifest with source hash plus parameters. The export step reads
  the manifest, not the timeline, and verifies each timeline clip's source
  hash matches its master before libx264 encode (a DNEG-style conform
  check); log any hash mismatch and halt that shot instead of re-encoding
  silently. (Grounded in Pixar's non-destructive layering and DNEG's
  conform/publish/track pattern; the USD-to-AI-video mapping is an analogy.)
- **Per-take transcript and searchable dailies log.** After each shot, append
  a log line: shot_id, duration, dialogue, characters present, reference
  hashes used, VRAM/RAM peak, temp-file swap events, and a 1-frame
  contact-sheet path. This makes the "shot 500 looks as clean as shot 1"
  claim checkable instead of asserted. (Modeled on Netflix's Media
  Production Suite per-take transcript and searchable-moments pattern, as
  reported second-hand from the IBC 2026 keynote; cite as such.)

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
