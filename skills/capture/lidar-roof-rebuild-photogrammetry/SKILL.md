---
name: lidar-roof-rebuild-photogrammetry
description: "Complete a ground-level photogrammetry model by rebuilding its unseen top from national survey LiDAR: keep the scan where photos saw the stone, rebuild terrace and crest from IGN LiDAR HD, sample stone texture from the scan, account for the model in percentages. Trigger when a scan is missing its roof."
---

# LiDAR Roof Rebuild for Photogrammetry

## Purpose

This skill reconstructs the exact workflow NicolasDiolez demonstrates for finishing a photogrammetry model whose top the ground photos could never see, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: keep the scan where the photos really saw the stone, and rebuild the parts they could not see from survey LiDAR.

## Source

Creator: NicolasDiolez. Post: "My Arc de Triomphe scan finally has a roof (rebuilt from the French national LiDAR)" https://www.reddit.com/r/photogrammetry/comments/1xzg4rb/ (score 36, 4 comments; full post text and comments read) | Model on Fab: https://www.fab.com/listings/4be462aa-5aa9-4c4a-9dc3-3ce00be1683e | 2026-11-19 scout run, audit 7.

## Tools used

RealityCapture (Realityscan in the post), IGN LiDAR HD (French national survey, open data), Blender Python, Claude Fable 5.2. No AI-generated images or textures.

## Phase 1: Scan what the ground can see

**Do**
1. Photograph the monument from the ground: 3,372 photos in this case.
2. Reconstruct in RealityCapture. From the ground, the top cannot be seen, and up there the software "could only guess."

**Check**
- The old model was incomplete at the top; that incompleteness is the problem statement, not a surprise. This was one of the author's oldest photogrammetry models, and the roof had always been missing.

**Why**
A photogrammetry model is only as complete as its viewpoints. Ground photos cannot see a roof, so no amount of photo count fixes the top.

## Phase 2: Rebuild the unseen top from national LiDAR

**Do**
1. Take the terrace, the cornice tops, and the crest from IGN LiDAR HD, the French national survey, open data, plus documentation.
2. Rebuild those parts in Blender, with the code written by Claude Fable 5.2: the author directed it and reviewed every version.
3. Take the stone on the rebuilt parts from the scanned stone itself. No AI-generated images or textures; everything comes from the author's photos and the LiDAR.

**Check**
- The author's own assessment of the model: Fable 5.2 is "insane at 3D modeling" (author's words), and the human directed and reviewed every version.

**Why**
LiDAR is the authority where photos cannot reach, and the scan is the authority for surface appearance. Splitting the two jobs (shape from LiDAR, stone from the scan) keeps each source honest.

## Phase 3: Clean the base and account for the whole model

**Do**
1. Remove people and cars at the base.
2. Account for the final model: 68% scan, 21% rebuilt, 11% repaired.

**Check**
- The percentages are the provenance record: most of the model is measured, a fifth is survey-rebuilt, a tenth is cleanup.

**Why**
A percentage split is a claim about evidence: it says exactly how much of the model is observed and how much is reconstructed, so a user knows what to trust.

## Phase 4: Open questions

**Do**
1. Note the two questions commenters asked and the author did not answer: a "making of" guide was requested, and a commenter asked what input Claude takes and what output it gives (photos in, Blender mesh out? clean or optimized? token cost?).

**Check**
- The LiDAR processing parameters and the Fable prompts are undisclosed; the workflow above is the method, not a reproducible recipe at the parameter level.

**Why**
An unanswered "how" is a depth limit, not a failure: the method is clear and the parameters are not, and the skill says so instead of inventing them.

## Failure modes

- **Letting the software guess the roof:** the old model did this, and the top was wrong. Never ship a guessed roof when survey LiDAR exists for the site.
- **AI textures on rebuilt parts:** the author used none. Sampling stone from the scan keeps the rebuilt parts in the same material as the measured parts.
- **Unreviewed generated code:** Fable wrote the Blender Python, but the author directed and reviewed every version. Generated modeling code without review is a defect source, not a shortcut.

## AAA studio practice

- **DICE, GDC 2016, "Star Wars: Battlefront and the Art of Photogrammetry" (Keneth Brown, Andrew Hamilton).** Photogrammetry was combined with traditional modeling for all assets and worlds: real locations (Finse, Norway; Death Valley, California) and original Lucasfilm props were photographed from every angle and reconstructed, then retouched like a traditional high-topology sculpt. Three disciplines from that talk apply directly here: plan the shoot from a breakdown of which assets are needed per session (so you do not shoot too many or too few photos); overlap is "the single most important thing," achieved by shooting from further away to cover more of the object at once; and shoot from all possible angles to prevent time-consuming retouching. DICE's load-bearing caveat is also this skill's: black-and-shiny surfaces defeat the solver (Darth Vader's helmet was the tricky case). Source: https://www.3dmag.com/inspiration/3d-scanning-star-wars-battlefront/ ; https://www.gamedeveloper.com/audio/capturing-iconic-look-and-sound-in-i-star-wars-battlefront-i-
- **Terrestrial LiDAR + UAV photogrammetry merged for heritage (ISPRS Archives, 2019).** Two Indonesian heritage buildings (Vredeburg Fort Museum, Kotagede Great Mosque) were documented by merging terrestrial laser-scanner point clouds with UAV photogrammetry point clouds via Iterative Closest Point (ICP) registration into one reference system, with a reported 20.60 mm RMS registration error, then visualized interactively in Unity at LOD3. This is the published version of this skill's core split: the survey instrument is the authority for geometry the photos cannot reach, and the photos are the authority for texture. Source: https://isprs-archives.copernicus.org/articles/XLII-2-W17/39/2019/
- **Notre-Dame laser scanning (Andrew Tallon, Vassar College).** The art historian placed a laser scanner in more than 50 positions inside and around Notre-Dame and collected over a billion measured points, accurate to about five millimetres; after the 2019 fire, that scan data aided the actual reconstruction of the vaulted ceilings. The cautionary contrast is Assassin's Creed Unity: Ubisoft's Notre-Dame was an artistic vision, not a scientific reconstruction, and the studio said so publicly. The rule for this skill: a LiDAR-rebuilt part is a measured part and is labeled as such; a hand-modeled part is an artistic part and is labeled as such, and the two are never presented as the same kind of evidence. Sources: https://www.gpsworld.com/3d-mapping-of-notre-dame-will-help-restoration/ ; https://bigthink.com/the-present/notre-dame-3d/

**Agent-executable upgrades**

1. **Provenance manifest (`provenance.json`).** One entry per model part: source (scan / LiDAR-rebuilt / repaired), the LiDAR dataset and tile ID (e.g. the IGN LiDAR HD tile), the scan photo set it draws texture from, and the running percentage split. The author's 68/21/11 split becomes a file, recomputed after every edit instead of asserted once.
2. **Registration error gate.** Align the LiDAR point cloud to the scan mesh (CloudCompare CLI, ICP) and record the RMS error in the manifest before any rebuild starts. The ISPRS paper's 20.60 mm RMS is the published reference point for a merged heritage model; the gate is the recorded RMS for this model, with the threshold set per project and logged (label: agent-set threshold, not a published studio number).
3. **Unseen-top audit.** Before rebuilding, list the mesh regions with no photo coverage from the RealityCapture camera-coverage report. That list is the rebuild list: every rebuilt part traces to a named coverage gap, and no part is rebuilt that the photos already cover.
4. **Texture-source gate.** Every texture file used on a rebuilt part must trace to a photo from the scan set; log the source photo hash per texture in the manifest. A rebuilt part carrying a texture with no scan-photo source fails the gate. This is the executable form of the author's "no AI-generated images or textures" rule.
5. **Generated-code review log.** When an agent writes the Blender Python (as Fable 5.2 did here), log each version with the human's review decision before it runs. Generated modeling code without a recorded review is a defect source, not a shortcut.

## The human method, distilled

1. Keep the scan where it saw, rebuild where it did not: never let the software guess the roof.
2. AI writes, the human inspects: Fable wrote the Blender Python, the author directed and reviewed every version.
3. Account for the model in percentages: 68/21/11 is the provenance.

**Depth status:** PARTIAL (method, tool names, and the 68/21/11 split are disclosed; LiDAR processing parameters and Fable prompts are not. The skill records the method and marks the undisclosed parts rather than inventing them).
