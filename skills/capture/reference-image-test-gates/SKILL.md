---
name: reference-image-test-gates
description: "Gate a generated or rebuilt 3D model against its reference images before it enters the pipeline: orthographic silhouette renders from Blender, IoU and boundary-fit scores computed in plain Python, thresholds calibrated per project instead of copied, and a human-signed contact sheet. Trigger when a generated model must prove it matches its reference shape before retopology, rigging, or engine import."
---

# Reference-image test gates for generated 3D models

## Purpose

This skill reconstructs the reference-image test-gate workflow end to end, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: prepare a clean reference matte per view, render the model as a flat silhouette from the same view, measure the agreement with numbers (IoU, boundary distance, width profile), calibrate the pass thresholds from the project's own accepted assets, and let a human sign the verdict from a contact sheet. The generator's own report never passes its own gate.

The gate measures shape agreement with the reference. It says nothing about art quality, texture, topology, or rigging. A model can pass every number here and still be ugly, unfused, or unriggable. Those are other gates (see the sibling skill `automation/ai-3d-production-readiness-gates`, which is the decision framework this procedure feeds).

## Source

Thread: r/ClaudeCode, "Why is claude so bad at model creation and how can i help him get better?", posted 19 Nov 2026 by u/ComingDeveloper, 990 points. https://www.reddit.com/r/ClaudeCode/comments/1y0f0k2/why_is_claude_so_bad_at_model_creation_and_how/

Full audit: `~/workspace/your_files/claudecode-model-creation-thread-audit-2026-11-22.md`. Coverage limits, stated plainly: the thread was read via old Reddit on 22 Nov 2026; 394 of 409 comments were captured and 15 never rendered; long comments were truncated mid-sentence in capture. Everything below that describes a commenter's method is the audit's paraphrase, never a verified verbatim quote. Two contributions carry this skill:

1. Reklaw12's test-gate approach (19 points): give reference images from different angles and have the model test its model against each angle, with silhouette comparison called out as the most revealing check for face-shape problems. The thread also compared Fable 5.2 against Astra 6.2; that model comparison is not part of this skill.
2. Present_Flower_6596's measured workflow (5 points): a local Qwen, TRELLIS 3D, Flux, and Blender MCP chain driven by Claude, with an alignment script producing numeric gates and a stated refusal to trust the tool's own report, verified personally instead. The author's numbers (reg_iou 0.872, fit_iou 0.903, 7,840 tris) are one author's values on one asset from their own script. They appear in this skill exactly once, in this paragraph, as a worked example of what a gate report looks like. They are never thresholds. Copying them as thresholds is a process failure (see Phase 5 and Failure modes).

Deliberately excluded: Alzeric's throughput claims from the same thread (180 models in roughly 45 minutes and similar figures). They are unverified anecdotes from one author, the author never checked vert counts, and they describe generation speed, not shape agreement. They do not appear anywhere else in this skill.

Prior art read firsthand (not from the thread): the "Blender image to 3D" skill by majidmanzarpour, which implements silhouette IoU plus width-profile measurement in plain Python with Pillow, a world-registered IoU gate, and per-phase tolerances for hand-built assets. https://innernet.live/skills/majidmanzarpour-blender-image-to-3d . This skill generalizes that measurement pattern to generated models of any origin and adds the calibration procedure and the checker-separation rule. That skill's tolerance values (0.85 blockout, 0.90 forms) were calibrated for its own hand-built pipeline and are cited here only as an example that calibrated values exist, never as values to copy.

## When to use this skill, and when not

Use it when a model was generated (image-to-3D, text-to-3D, or a generator plus Claude/Blender cleanup) and must prove it matches a reference before expensive downstream work (retopology, rigging, texturing, engine import). Use it at blockout and again after any revision that moves mass: proportions are cheapest to fix before detail exists.

Do not use it as a substitute for the readiness framework: if the question is "can this asset be handed to the next person," run `automation/ai-3d-production-readiness-gates` and use this skill as the shape-measurement step inside it. Do not use it on models with no reference: with nothing to compare against, there is no gate, only taste. Do not use it to judge surface quality: a silhouette cannot see texture, edge flow, or deformation.

The nearest existing check is one line in `capture/comfyui-ldoi-image-to-3d` ("compare each silhouette against the input image" for a 4-frame turntable, visual only, no numbers). This skill replaces that visual check with a measured procedure wherever the check matters. It does not expand that skill, because the procedure is generator-independent and that skill is a TripoSG-specific pipeline.

## Tools used

Blender 4.2 or newer, run headless (`blender --background --python <script> -- <args>`). In this workspace a Blender 4.5.0 install was previously verified at `~/workspace/tools/blender/blender-4.5.0-linux-x64/blender`; confirm it still resolves before relying on it, and otherwise resolve the binary once (`$BLENDER_BIN`, then `blender` on PATH) the way the prior-art skill does.

Python 3.10 or newer with Pillow and numpy for measurement. OpenCV (`cv2`) or SciPy for the boundary-fit distance transform; if neither is installed, boundary-fit is recorded as not measured, never faked (see Phase 4). No GPU is needed for the Workbench path; the Cycles fallback path needs only a CPU (see Phase 2).

## Phase 1: Reference intake and matte preparation

**Do**
1. Copy every reference image into `<asset>/ref/` under a descriptive name before anything else. Images pasted into a conversation arrive as temporary files; the gate scripts load references from disk, so the copy is what makes a later re-run reproducible.
2. For each image, record a VIEWS entry in `<asset>/gate-brief.md`: view type (front, side, back, top, three-quarter, concept), whether it is an orthographic sheet or a perspective concept, estimated camera azimuth and elevation, the lens if it is a photo (0 means orthographic), how much of the image height the subject fills, and where the ground line sits.
3. Orthographic sheets are the only views the gate measures proportions from. Perspective concepts are silhouette-only: they can catch a wrong outline, never a wrong measurement. If a turnaround or model sheet holds several panels, crop each panel into its own file (`ref/front.png`, `ref/side.png`, `ref/back.png`) sharing one scale and one ground line.
4. Prepare one binary matte per measured view: the subject filled, the background empty. Erase labels, rulers, floor lines, shadows, and anything the model does not include. If the reference is concept art with a painted background, the matte is made by hand (selection plus cleanup) or with a segmentation tool; record which. Save as PNG with an alpha channel or as a black-on-white mask. If the matte is guessed (for example, a soft painted edge cleaned by eye), record that the matte itself is approximate and widen the calibration margin in Phase 5.
5. Record what the reference does NOT show. Every side, dimension, or part with no reference is INFERRED: list it in the brief with the prior used to fill it (symmetry, a second asset, a stated guess). An inferred back is gated against the brief, never against a reference that does not exist.
6. Record pose. The reference pose and the model pose must match (A-pose against A-pose, T-pose against T-pose) before any number is computed. Pose differences are punished by silhouette comparison as shape errors, which is correct behavior for a shape gate and a false failure for a pose mismatch. If the poses differ, fix the pose first and say so in the gate log.

**Check**
- Every measured view has a matte file, a VIEWS entry, and a stated lens (0 for orthographic).
- The matte, overlaid on its reference at 50 percent opacity, covers the subject with no label, ruler, or floor line inside it.
- The INFERRED list is non-empty whenever the reference set is a single image. A single front image with an empty INFERRED list means someone is pretending the back is known.

**Why**
The gate is only as honest as the matte. A dirty matte measures the label, not the model. The orthographic/perspective distinction is the difference between a measurement and an impression, and the INFERRED list is what stops a guessed back from being reported as a verified one.

## Phase 2: Build the gate render rig

**Do**
1. Open the model in Blender headless. Hide everything that is not the subject: reference planes, rulers, ground planes, and any collection whose name contains REF. The render script takes an `--objects` list when the file holds more than the subject; when it is empty, it renders all visible mesh objects except REF collections, and prints the rendered object names so the operator can see what was included.
2. Resolve the render engine at runtime, never by assumption. Engine identifiers moved between Blender versions (EEVEE was `BLENDER_EEVEE_NEXT` in 4.2 to 4.5 and is `BLENDER_EEVEE` again from 5.0). The script below tries each candidate, assigns it, and reads the value back; an identifier that raises `TypeError` is skipped, and if none sticks, the script fails loudly instead of rendering with whatever engine happened to be set. This try-assign plus read-back rule is taken from the render-engines reference read firsthand (https://github.com/jangtrinh/design-os-3d-blender/blob/HEAD/knowledge/30-lighting-render/render-engines.md).
3. Primary path: Workbench. Set `scene.render.engine` to `BLENDER_WORKBENCH`, then set the Workbench shading through `scene.display.shading`: `light` to `FLAT` (no lighting calculation, base color only), `color_type` to `SINGLE` (one flat color for the whole scene), `single_color` to white, `show_shadows` and `show_cavity` to False. Set each attribute only if it exists on the running Blender version, and print the values actually read back. Set `scene.render.film_transparent` to True, image settings to PNG with RGBA color mode. Workbench needs no lights, no materials, and no GPU on macOS or Windows.
4. Fallback path, headless Linux without a GPU: Cycles on CPU. Set the engine to `CYCLES`, `scene.cycles.device` to `CPU`, `scene.cycles.samples` to 1, and put a white emission material on `view_layer.material_override` (verified in the Blender Python API: `material_override`, "Material to override all other materials in this view layer", https://docs.blender.org/api/4.1/bpy.types.ViewLayer.html). Film transparency stays on. This path is slower and exists only so a GPU-less container can still run the gate; prefer Workbench wherever it runs.
5. Place one camera per view. Cameras are orthographic: `cam.data.type = 'ORTHO'`, and `cam.data.ortho_scale` equals the world extent covered by the square frame. The render is square (`resolution_x == resolution_y`), so the covered height equals the covered width, and the frame is centered vertically on the ground line plus half the extent. Aim each camera with `to_track_quat('-Z', 'Y')` from a direction built from the view's azimuth and elevation, then assert the camera's forward axis points at the target (dot product above 0.999 after a view-layer update). Azimuth 0 is front (looking from -Y toward +Y), positive azimuth rotates toward +X; elevation 0 is level, 90 is top-down. Record the azimuth, elevation, extent, and ground value per view in the run output. For a perspective reference, use a perspective camera with the recorded lens instead, and record that the view is silhouette-only.
6. Set `clip_start` small (0.01) and `clip_end` generous (100 times the extent) so near/far clipping never eats the subject. Render with `bpy.ops.render.render(write_still=True)` and a filepath per view (`<outdir>/<view>.png`). Without `write_still`, the result stays in memory and the output directory is empty; the script asserts each file exists and is non-empty after its render.

**Check**
- The script prints, per view: engine identifier read back, camera type `ORTHO` (or `PERSP` with lens for perspective views), ortho_scale, camera location, and output path.
- The first render of a new rig is opened and looked at: a flat white subject on transparency, no shading, no ground plane, no reference plane. If the subject is shaded or the background is opaque, the rig is wrong and the run is invalid, not the asset.
- The alpha channel sanity check in Phase 4 passes: the render has both fully transparent and fully opaque pixels. An all-opaque render means film transparency is off; an all-transparent render means the subject was hidden or out of frame.

**Why**
An orthographic camera removes perspective distortion, which is what makes the comparison a measurement instead of a perspective guessing game. Flat single-color shading removes every variable except the outline, which is the only thing this gate measures. The read-back discipline exists because Blender's engine identifiers and shading attributes differ across versions, and a script that assumes them renders with the wrong engine silently.

## Phase 3: Render the silhouettes

**Do**
1. Run the render script once per model revision, into a fresh directory named for the revision (`<asset>/gates/<revision>/`). Never overwrite a previous revision's renders: the gate log compares revisions, and overwritten evidence cannot be compared.
2. Render every measured view from Phase 1, plus the three-quarter view when the asset will be seen from the game camera (for Valkyrie, always: the fixed iso camera is a three-quarter view). Minimum set: front, back, left, right. Top view only when the reference set includes one or the asset's plan shape matters (vehicles, kit pieces, architecture).
3. Also render one gameplay-size strip per view: the same silhouette downscaled so the subject is 128 px tall (the default used by the prior-art skill; change it to the project's actual on-screen subject height and record the value). Thin parts that survive at 512 px but vanish at gameplay size are found here, not in the full-size render.
4. Write a run manifest alongside the renders: Blender version string, engine identifier read back, per-view azimuth/elevation/extent/ground, rendered object names, render size, and the model file's hash and modification time. A gate report whose manifest does not match the model file is stale and fails the run, not the asset.

**Check**
- One PNG per measured view, plus one gameplay strip per view, plus the run manifest, all in the revision directory.
- The manifest's model hash matches the model file. If the model was edited after the render, re-render; do not gate stale evidence.
- The three-quarter render reads as the asset from the game camera. If it does not, the gate views are wrong for the project, not the model.

**Why**
Revision-named directories make the gate history auditable: a later question ("when did the shoulders get wide?") is answered by two directories, not by memory. The gameplay strip exists because a silhouette that passes at 512 px and fails at the size players actually see it at has failed where it matters.

## Phase 4: Measure (IoU, boundary-fit, width profile)

**Do**
1. Run the measure script with the render directory, the matte directory, the comparison mode per view, and optionally the gate manifest with thresholds. Dependencies: Pillow and numpy are required. OpenCV or SciPy is required for boundary-fit; if neither is installed, the script records boundary-fit as not measured and continues with IoU and width profile. It never invents a boundary number.
2. Load each render's alpha channel and threshold it at 127 (of 255) to a binary mask. Antialiased edge pixels land on both sides of 127; that is expected, and the threshold is fixed for the whole project so the bias is constant. Load each reference matte the same way (alpha channel, or luminance for black-on-white masks).
3. Mode A, bounding-box aligned (the Reklaw12-style comparison): crop both masks to their bounding boxes, resize the reference mask to the render mask's size with nearest-neighbor resampling (never bilinear: bilinear invents gray pixels that the threshold then misreads), and compute IoU as intersection over union. Record that the mode is bbox-aligned. This mode cannot see a model that is too short, too tall, or off its axis, because alignment erases scale and placement. Never use it alone for an orthographic sheet.
4. Mode B, world-registered (required for orthographic sheets): the render frame covers the reference matte's exact world window, because the camera extent and ground line were set from the brief in Phase 2. No resizing, no cropping. Compute IoU directly on the full frames. Scale and placement errors count, which is the point. If the reference matte's world window is unknown (no scale cue in the brief), Mode B cannot run: record that, run Mode A, and mark the gate as shape-only, with scale unverified.
5. Boundary-fit: compute the distance transform of each mask's complement (`cv2.distanceTransform` with `DIST_L2`, mask size 5, verified in the OpenCV docs: "Calculates the distance to the closest zero pixel for each pixel of the source image", https://docs.opencv.org/2.4.7/modules/imgproc/doc/miscellaneous_transformations.html; or `scipy.ndimage.distance_transform_edt`). Take the boundary pixels of each mask (mask minus its 4-neighbor erosion, computed with plain numpy shifts, no extra dependency). Average the reference distance transform over the render boundary and vice versa; the symmetric mean is the boundary-fit, reported in pixels and as a fraction of the subject's bounding-box height. IoU punishes area disagreement; boundary-fit punishes outline displacement even when areas match. A model with the right area in the wrong place fails boundary-fit while passing IoU, which is why both are measured.
6. Width profile: split the bounding-box height into 12 horizontal bands. Per band, mean width is mask pixels divided by band height, as a fraction of subject height. Report the largest absolute band deviation between reference and render, and which band it is in ("band 2 of 12, shoulders, render 0.06 wider"). A single number that names its location turns a failed gate into a fix list.
7. Write `gate-report.json` (per view: mode, IoU, boundary-fit in pixels and fraction, max band deviation and its band, matte and render paths, threshold verdicts when a manifest was supplied) and the visual artifacts: an overlay PNG per view (green overlap, red reference-only, blue render-only) and a contact sheet per view (reference matte, render, overlay, gameplay strip side by side). The overlay is the artifact the human reads; the JSON is the artifact the next script reads.

**Check**
- Every view in the run manifest has a row in the JSON. A missing row means the measurement crashed silently, and the gate is not run.
- IoU values are between 0 and 1, boundary-fit is non-negative, and the overlay shows the same disagreement the numbers describe. If the overlay and the numbers disagree, the measurement code is wrong; trust neither until the discrepancy is explained.
- Boundary-fit is either a number or the explicit string "not measured (no cv2/scipy)". A boundary-fit of 0.0 with no library installed is a lie, not a measurement.

**Why**
IoU alone is a blunt instrument: two shapes can share an area and differ everywhere along the edge. Boundary-fit catches the displacement IoU forgives, and the width profile localizes it. The overlay exists because numbers catch drift the eye forgives and the eye catches absurdity the numbers average away; the gate needs both, which is why the human step in Phase 6 is not optional.

## Phase 5: Calibrate thresholds per project

**Do**
1. Assemble a calibration set: 3 to 5 assets of the same class (characters with characters, props with props) that the project has already accepted, or the first asset's successive accepted revisions if no accepted set exists yet. Compute all three measures for every view of every calibration asset with the Phase 4 script.
2. Set each threshold from the calibration set, per view and per measure: threshold equals the lowest passing value observed, minus a margin of 0.02 IoU (this skill's rule, labeled as such, not a measured constant). Boundary-fit thresholds are set the same way, in fraction-of-height units. Width-profile thresholds are set per band group (head bands, torso bands, limb bands) when the class has stable anatomy, otherwise one threshold for all bands.
3. Write the thresholds into `<asset>/gate-manifest.json` (or one manifest per asset class) with the calibration asset identifiers, the date, the Blender and script versions, and the margin rule used. A threshold without its calibration set recorded is an opinion, not a gate.
4. Recalibrate when the asset class changes, the generator changes, the reference style changes (painted concept to orthographic sheet, or the reverse), or the game camera changes. Thresholds do not transfer across any of those boundaries. A threshold copied from another project, another class, or this skill's example paragraphs is rejected on sight in review.
5. First-gate rule: an asset class with no calibration set yet gates provisionally. The numbers are recorded, the contact sheet is reviewed by a human, and the verdict is "provisional pass, calibration pending." The provisional verdict converts to a calibrated threshold only after the calibration set exists. Provisional passes are never backdated into thresholds.

**Check**
- The manifest names its calibration assets and date. If it does not, the thresholds in it are unusable and the gate runs uncalibrated (numbers recorded, verdict provisional).
- No threshold in the manifest equals 0.872, 0.903, 0.85, or 0.90 unless the calibration set independently produced that value and the record says so. Those are other people's numbers (the thread author's, the prior-art skill's). Coincidence is possible; copying is not, and the record is what distinguishes them.
- Thresholds exist per view. A front-view threshold applied to a back view is a category error: backs carry different features and different matte quality.

**Why**
Thresholds are the part of a gate most often faked by copying. A copied threshold encodes another project's tolerance, reference quality, and matte cleanliness, none of which hold here. Calibration from the project's own accepted work is the only procedure that makes the numbers mean "as good as what we already ship."

## Phase 6: Human verification and the verdict

**Do**
1. Compose the contact sheet per view (reference, render, overlay, gameplay strip) and open it. Read the JSON numbers alongside. Write every mismatch as a measurement, not an adjective: "head 12 percent too tall," "shoulder band 2 of 12, 0.06 wider," "left forearm missing from the silhouette in the side view." The prior-art skill's rule, adopted here: mismatches are measurements, because a measurement names its fix and an adjective does not.
2. The human writes the verdict into `<asset>/gate-log.md`: pass, revise, or reject, with the failing checks named and the measurements attached. The verdict is written by the human, or by a separate checker invocation that only reads the JSON and the sheets and writes the log. The script that generated the model, and the script that measured it, never write the verdict. This separation is the Present_Flower discipline from the thread (verify personally rather than trusting the report) and the checker pattern of the sibling skill `automation/predict-verify-checker-pipeline`.
3. Revise means: fix the named measurements in the build or generation inputs, re-render, re-measure, and append a new gate-log entry for the new revision. Never edit the old entry. Reject means: the base is wrong in a way measurement cannot fix (fused parts, wrong pose family, invented back presented as reference) and the asset restarts from generation or blockout.
4. If the operator instructed the run to continue without asking, a provisional pass is allowed only when every number is inside its calibrated threshold AND the overlay shows no visible deviation the numbers missed. Any visible deviation, or any uncalibrated threshold, means revise, and the log says "provisional, human review pending." The sheets stay in the revision directory either way.
5. On pass, the gate log entry records: revision, per-view numbers, thresholds applied, the human's name or the checker invocation, and the INFERRED list from Phase 1 carried forward. The passed revision's renders and report become part of the asset's permanent record and travel with it into retopology or the Terrarium pipeline.

**Check**
- The gate log has one entry per revision, in order, with verdicts and named measurements. A gap in the sequence means a revision was gated informally, and its numbers do not exist.
- No entry's verdict was written by the generating script. If the log and the generation report agree word for word, the separation failed and the verdict is void.
- The passed revision's contact sheets are viewable in the revision directory. A pass without sheets is a claim, not evidence.

**Why**
The human step exists because the numbers have known blind spots (thin parts, matte errors, pose-adjacent features) and the eye has known blind spots (slow drift, small systematic error). Each catches what the other forgives. The separation rule exists because a tool that grades its own work passes its own work.

## The human method, distilled

1. **Matte before measurement.** A dirty matte measures the label, not the model.
2. **Orthographic for proportions, perspective for outline only.** Never measure from a perspective concept.
3. **Same camera, same frame.** The render and the reference must share a view, a window, and a ground line, or the comparison is fiction.
4. **Numbers plus eyes.** IoU, boundary-fit, and the overlay together; neither alone.
5. **Thresholds are earned, never copied.** Calibrate from accepted work, per class, per view.
6. **Measurements, not adjectives.** A mismatch that names its size names its fix.
7. **The checker is not the maker.** The verdict is written separately from generation and measurement.
8. **Silhouette first, detail later.** A normal map restores shading; it cannot restore a missing silhouette.

## Failure modes

- **Bounding-box alignment hides scale errors.** Mode A erases scale and placement by design. Fix: Mode B for every orthographic sheet; Mode A results carry the "shape-only, scale unverified" label.
- **Perspective reference measured as orthographic.** A photo or perspective concept compared through an orthographic camera produces systematic error that looks like a proportions failure. Fix: record the lens per view in Phase 1; perspective views render with a matched perspective camera and gate silhouette only.
- **Pose mismatch scored as shape failure.** A-pose reference against T-pose model fails every view. Fix: match poses before gating; record the pose in the brief.
- **Antialiasing threshold bias.** Edge pixels straddle the 127 threshold, so thin features measure thinner than they are. Fix: fixed threshold for the whole project, and the gameplay-size strip as the arbiter for thin parts.
- **Mirrored views.** A left view rendered as a right view passes IoU against a symmetric reference and fails silently against an asymmetric one. Fix: record handedness per view; asymmetric features (a satchel, a weapon side) are the check.
- **Transparent and translucent parts vanish.** Glass, hair cards, and thin cloth contribute little or nothing to a flat silhouette. Fix: list them as uncovered parts in the brief; gate them by another method, never by this one.
- **Ground-line mismatch.** The model floats or sinks relative to the reference ground line, which Mode B scores as a placement failure and Mode A hides entirely. Fix: set the ground value from the brief and check the contact point in the overlay.
- **Invented back presented as verified.** A single-image reference has no back; gating the back against nothing produces a confident-sounding number. Fix: the INFERRED list; backs gate against the brief.
- **All-opaque alpha.** Film transparency off, or a background plane rendered into the frame, makes the silhouette the whole frame and IoU meaningless. Fix: the Phase 2 alpha sanity check fails the run, not the asset.
- **Copied thresholds.** Thresholds from the thread, from the prior-art skill, or from another class. Fix: Phase 5 calibration; a threshold without a recorded calibration set is rejected in review.
- **Tool self-acceptance.** The generator's report, or the measuring script, writes the verdict. Fix: checker separation in Phase 6; a verdict that matches the generation report word for word is void.
- **Stale evidence.** The model was edited after the render; the report describes a model that no longer exists. Fix: the run manifest hash check in Phase 3; re-render on any edit.
- **Workbench unavailable headless.** On a GPU-less Linux container, Workbench has no GPU context and the render fails or comes back black. Fix: the Cycles CPU fallback in Phase 2, with material override; never silently accept a black render as a silhouette.

## AAA studio practice

- **Valve, Team Fortress 2 (GDC 2008, Jason Mitchell).** Character creation runs in a fixed order: character silhouette first, then interior shapes, then the model sheet, then the 3D model, with the explicit step "match silhouette to model sheet" and design problems solved "using silhouette only." The read hierarchy lists distinctive silhouettes before body proportions. This skill's gate is that step, mechanized: the model sheet is the matte, the match is measured. Source: full text of the GDC 2008 talk, https://archive.org/stream/GDC2008Mitchell/GDC2008-Mitchell_djvu.txt
- **Studio pipeline economics.** A character pipeline survey from Sunstrike Studios states the cost rule this gate exists to exploit: a design change at the silhouette stage costs an hour, while the same change after the sculpt costs days, with a sign-off at the end of each stage. The gate is the sign-off for the silhouette stage. Source: https://sunstrikestudios.com/en/blog/how-game-characters-are-made/
- **The Cinematic Cavern exemplar.** Phase 3 of the depth exemplar for this library states the rule the gate enforces: a normal map can restore shading detail, but it cannot restore a missing silhouette, so the outline must survive decimation and every later stage. Source: `~/workspace/user/files/cinematic-cavern-workflow-guide.md`, read firsthand.
- **Prior art, third-party skill.** The "Blender image to 3D" skill implements the same measurement family (silhouette IoU plus width-profile numbers in Pillow, a world-registered IoU gate, per-phase tolerances, mismatches written as measurements) and contributes the warning this skill adopts: bounding-box alignment cannot see a model that is too short or off its axis. Its tolerances were calibrated for hand-built assets in its own pipeline and are not reused here. Source: https://innernet.live/skills/majidmanzarpour-blender-image-to-3d, read firsthand.

## Agent automation

1. **Gate manifest.** One `gate-manifest.json` per asset class: calibration asset identifiers and dates, per-view thresholds per measure, the margin rule, Blender and script versions, the gameplay pixel height used for the strips. A gate run without a manifest records numbers and a provisional verdict only.
2. **Batch mode.** The measure script accepts a directory of revision folders and writes a summary table (revision, per-view IoU and boundary-fit, verdict) so a batch of generated variants is compared on one page. Variants are never averaged: each variant gets its own row and its own verdict.
3. **Staleness gate.** Before measuring, compare the model file's hash and modification time against the run manifest. A mismatch fails the run with "stale evidence, re-render" and writes nothing. A gate report is never produced from renders of a different model revision.
4. **Determinism.** Same inputs produce the same numbers: fixed alpha threshold (127), fixed band count (12), nearest-neighbor resampling, no randomness anywhere in measurement. If two runs of the same inputs disagree, the scripts changed, and the run is invalid until the change is explained.
5. **Checker separation.** The verdict writer (human or checker invocation) reads only `gate-report.json`, the overlays, and the contact sheets. It never imports the generation code or the render script. Record the checker invocation in the gate log. This is the predict-then-verify discipline of the sibling skill `automation/predict-verify-checker-pipeline`, applied to geometry instead of code.
6. **Coverage audit.** Once per asset class, list the parts the silhouette gate cannot see (glass, hair cards, thin cloth, interior detail) and name the gate that covers each. An uncovered part with no named gate is a hole in the pipeline, recorded in the brief until it is closed.

## Valkyrie note

Valkyrie assets are painted-look, fixed iso camera, authored map. The gate applies to generated props and characters before they enter the Terrarium pipeline (TRELLIS-2 generation, Blender cleanup, engine import): a generated citizen or prop that does not match its reference silhouette does not get retopology time, because silhouette errors are the most expensive errors to fix late and the cheapest to measure early.

Three Valkyrie-specific rules. First, always include the three-quarter view at the iso camera's azimuth and elevation, at gameplay pixel height: the fixed camera means the asset is judged from one direction at one size, and the gate must judge it there too. Second, the gate measures shape agreement only. The painted look (palette, dappled light, full saturation) is invisible to a flat silhouette render by design; do not let a passed gate stand in for a look review, and do not let a look review override a failed gate. Third, citizens are seen at crowd distance as well as up close: run the gameplay strip at both the near-camera height and the crowd height, and record both. A silhouette that reads at 128 px and dissolves at 48 px needs its defining features exaggerated, which is a brief change, not a gate failure to negotiate away.

The Terrarium pipeline's existing stages (generation, Blender cleanup, SeaweedFS storage) gain one stage at the front of cleanup: gate, then clean. A failed gate sends the asset back to generation with named measurements; it never enters cleanup hoping the cleanup will fix the shape.

## Depth status

PARTIAL (thread evidence read firsthand with its coverage limits stated; measurement pattern corroborated by a third-party skill read firsthand; Blender engine, shading, and view-layer APIs verified from the Blender Python API docs and a Blender 5.x bpy reference read firsthand; distance-transform API verified from the OpenCV docs; the render and measure scripts in Phases 2 and 4 are this skill's construction and have not been run hands-on in this session; thresholds are a calibration procedure, not measured values; the Cycles fallback path has not been executed headless here).
