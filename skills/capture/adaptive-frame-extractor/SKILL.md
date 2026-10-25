---
name: adaptive-frame-extractor
description: "Feed photogrammetry only the frames it needs: score frames for quality and overlap, extract the best, skip the rest. Trigger when extracting frames for SfM pipelines."
---

# Adaptive video frame extractor for photogrammetry/SfM

## Purpose

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Feed photogrammetry only the frames that matter: score frames for quality and overlap, extract the best, skip the rest.

## Source

Creator: WearyFortune7055

Source: https://v.redd.it/d88gwsgctinh1 | r/photogrammetry post 1w77cpe (score 48) | native clip (demo, not tutorial)

## Tools used

Tools used: adaptive-frame-extractor (native C++ desktop app, macOS/Windows/Linux builds, runs locally, no Python setup), COLMAP, Gaussian Splatting / NeRF pipelines, Meshroom/AliceVision (KeyframeSelection, the incumbent the tool is measured against), JPEG and PNG output, CSV per-frame metadata.

**Do**
1. Open the video in the GUI. Scrub the timeline to find the capture sections that matter.
2. Mark multiple timeline regions for the sections you want to keep. Different passes, different takes, or cutting a turntable pause out of the middle of a clip are all region material.
3. Give each region an optional separate output folder so the frames from different passes do not mix downstream.

**Check**
- Regions are the unit of work, not the whole clip. A region you would not run COLMAP on should not send it frames.

**Why**
The camera motion, and therefore the right frame spacing, changes across a capture session. Regions let one extraction pass treat each part on its own terms, and separate folders keep multi-pass scans separable when you get to reconstruction.

## Phase 1: Load video and set timeline regions

## Phase 2: Adaptive extraction (motion-driven spacing)

**Do**
1. Run the adaptive extractor instead of pulling every Nth frame. Frame spacing follows estimated camera motion.
2. Expect: fewer near-duplicate frames when the camera is barely moving, denser frame spacing during faster movement and rotation.

**Check**
- The principle the creator names explicitly: "keyframe" here means frames that are important for Structure-from-Motion reconstruction. The extractor does not distinguish I vs P/B frames, and in the creator's words "in practice an I-frame is not necessarily higher quality or lossless."
- Sanity-check the density balance: if a slow sweep yields the same frame count as a fast one, the motion model is not doing its job.

**Why**
Fixed-interval extraction wastes frames on the boring parts and starves the parts where parallax actually changed. Motion-adaptive spacing spends the frame budget where the geometry information is. This is the tool's whole argument for existing, and it is aimed squarely at Meshroom/AliceVision's KeyframeSelection being, in a user's words, "painfully, painfully slow."

## Phase 3: Manual curation pass

**Do**
1. Use manual extraction of individual frames to add any specific frame you care about, and remove frames you do not want before export.
2. For clips where adaptive logic is wrong for the material (a scan that is all slow, deliberate rotation), fall back to regular fixed-interval extraction, which the app also supports.

**Check**
- Fixed-interval remains in the toolbox on purpose: adaptive is the default, not the only mode.

**Why**
No automation model understands intent. The manual layer is the creator's acknowledgment that artists using this tool know their capture better than the motion estimator does.

## Phase 4: The blur question (creator's position, not a feature)

**Do**
1. Do not build a blur-rejection stage into your expectations of this tool. The creator's stated position: measuring blur and working around blurry frames is "surprisingly tricky to do well" and has "very little payoff."
2. Instead, let registration do the filtering: if a frame is too blurry for structure-from-motion, it will essentially fail to get registered. "No harm done. Perhaps it cause a bit of extra runtime."

**Check**
- This is the contested point of the thread. The counter-ask from the community (NorthernBaseOfficial, Skinkie): a per-frame quality score based on sharpness, exposure, and motion blur, letting the user "quickly remove the weakest ones before exporting."
- Note the community's practical context: TheDailySpank runs "questionable videos" (bad lighting, auto shutter) through Meshroom's KeyframeSelection precisely because its options are richer, despite the speed.

**Why**
Two philosophies collide here. The creator treats blur rejection as an unsolved measurement problem whose failure mode is cheap (unregistered frames cost compute, not correctness). The community wants a score, not a gate: let the human decide on a sorted list. If you implement the score, make it advisory, not automatic, or you have sided with the wrong camp.

## Phase 5: Coverage and overlap check before the long run

**Do**
1. Before export, look at the timeline for sections with too little camera movement or sudden jumps in camera position. In the community's requested version of this feature, those sections get highlighted on the timeline as warnings.
2. Treat a sudden jump as a scan-break risk and a low-movement stretch as a parallax deficit.

**Check**
- The value is measured against the cost of discovery: you want to catch a coverage gap before starting "a long COLMAP or Gaussian Splatting run," not after.

**Why**
Reconstruction failures are cheapest to fix at the frame-selection stage and most expensive to fix after hours of COLMAP. A timeline warning converts a silent downstream failure into a visible upstream decision.

## Phase 6: Export with metadata

**Do**
1. Choose JPEG or PNG output per region.
2. Export and review the extraction summary, plus the CSV with detailed metadata for every selected frame.

**Check**
- The CSV is the audit trail: it records which frames were selected and why, so a failed reconstruction can be traced back to the frame set rather than re-extracted blind.

**Why**
Reproducibility matters in capture work. If a COLMAP run fails on pass three, the summary and CSV let you compare what changed in the frame set instead of guessing.

## Phase 7: Background removal decision (the SAM suggestion)

**Do**
1. Decide whether your subject is an object scan. Proper_Rule_420's case: scanning objects, the background is "useless information" that slows SfM, and they patched the older CLI themselves with "a simple threshold on detected non-moving points," which "worked ok but was not the best."
2. Their recommendation: try SAM (Segment Anything), specifically SAM 3, which they describe as "quite easy to use (input words)" and "actually working great." The creator confirmed the app currently has no background remover ("no it does not") and asked about the use case before committing.

**Check**
- This is a niche need, acknowledged as such by the requester ("it might be a very niche need"), and the creator is still in the use-case-gathering stage. Treat SAM integration as proposed, not shipped.

**Why**
Background masking is a pipeline step, not a quality score: it changes what SfM is allowed to match, not just which frames it gets. The threshold-on-static-points hack worked acceptably, which tells you the bar for a first shipped version is lower than it looks, but SAM 3's text-prompted masks are what make it usable for artists instead of programmers, the exact audience the GUI rewrite was for.

## The human method, distilled

1. **Spend the frame budget on motion.** Adaptive spacing is the whole tool; fixed interval is the fallback, not the rival.
2. **Regions before frames.** Organize the capture into regions first, then let extraction run inside them, with separate output folders per region.
3. **"Keyframe" means SfM-important, not codec-important.** Do not prefer I-frames; an I-frame is not necessarily higher quality or lossless.
4. **Let registration filter blur; do not gate on it automatically.** A blurry frame that fails to register costs runtime, not correctness. If you add a quality score, make it advisory and let the human sort.
5. **Warn before the long run, not after.** Overlap/coverage warnings on the timeline exist to be read before COLMAP or Gaussian Splatting starts, because that is where the cost sits.
6. **Export the audit trail.** The per-frame CSV is what makes a failed reconstruction debuggable instead of repeatable.
7. **Background removal is a pipeline decision, not a quality filter.** Masking changes what SfM may match; thresholding static points is the minimum viable version, SAM 3 with text prompts is the artist-friendly one.

## Depth status
 FULL (post feature list is complete, comment thread is substantive; the native clip's screen-recorded steps are unseen, but the reconstruction is grounded in what the creator and commenters stated).

---

## AAA studio practice

Production capture teams treat frame selection as a coverage contract, not a
sampling rate, and the numbers below are theirs, not this skill's defaults.

- **Epic/Capturing Reality overlap targets.** Epic's RealityCapture guidance
  for simulation creators asks for 80% forward/backward and side/height
  overlap between images, the subject covering 60% or more of the frame, and
  every point of the subject visible in at least two images, with motion
  blur, shallow depth of field, and in-camera stabilization avoided.
  Source: https://forums.unrealengine.com/t/photogrammetry-recommendations-for-simulations-creators/1387350
- **Happy Mushroom's scan-to-Unreal pipeline.** Happy Mushroom shoots
  photogrammetry stills (Sony a7R IV, 60 MP, 90 mm prime for controlled
  props, plus drone and Leica RTC360 lidar where needed), color-corrects in
  Lightroom before the solve because RealityCapture matches on color values,
  then aligns and builds a ~40M-triangle model in RealityCapture before
  simplifying for Unreal.
  Source: https://beforesandafters.com/2020/11/12/getting-photogrammetry-assets-into-unreal-a-guide-from-happy-mushroom/?amp

**Do (agent-executable, automation upgrade)**
1. After extraction, compute an overlap report before any COLMAP run:
   run COLMAP's sparse reconstruction on the extracted set, then count
   registered cameras and mean track length. Treat "registered cameras <
   95% of extracted frames" or "mean track length < 3 views" as a failed
   coverage contract, not a solver setting to tune.
2. Encode the Epic targets as extraction checks: flag any region whose
   consecutive-frame overlap (estimated from matched features, not from
   time spacing) falls below 60%, and flag any frame where the subject
   fills under 60% of the frame for manual review.
3. Automate the blur triage the original skill leaves to registration:
   score every extracted frame with a Laplacian-variance sharpness metric
   (e.g. `cv2.Laplacian(gray, cv2.CV_64F).var()`), write the score into the
   existing per-frame CSV as a new `sharpness` column, and sort weakest
   first for the human curation pass. Keep it advisory, per Phase 4: never
   auto-delete on sharpness alone, because a blurry frame that still
   registers costs only runtime.

**Check**
- The CSV now carries sharpness alongside selection reason, so a failed
  reconstruction can be traced to coverage (registered-camera rate, track
  length) or to quality (sharpness), not guessed at.
- Any region below the 60% overlap floor is re-shot or re-extracted
  denser before the long run, matching Phase 5's warn-before-COLMAP rule.

**Why**
Studios pay for coverage up front because a plausible-looking but
under-constrained reconstruction is the expensive failure: it looks finished
while carrying disconnected components and local distortion. The overlap
contract plus an advisory sharpness score turns the extractor's motion
model into a verifiable gate.
