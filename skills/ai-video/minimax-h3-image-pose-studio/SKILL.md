---
name: minimax-h3-image-pose-studio
description: "Use foxdit's all-in-one MiniMax H3 Image workflow with Pose Studio: text-to-image, image-to-image, ref-to-image, and pose transfer in one ComfyUI file, with the pose driven by a posable dummy with proportion sliders instead of a prompt, character sheets made in Krea 2, and a template prompt (subject_definition, retention_analysis, detailed_description). v1.1 improves pose adherence. Includes the two-character workaround (build one at a time) and the Qwen 2.1 Pose Studio alternative. Trigger when a character needs the same identity in many poses from H3 Image."
---

# H3 Image Pose Studio Workflow (All-in-One, v1.1)

## Purpose

This skill reconstructs the H3 Image Pose Studio workflow from the author's post, comments, and the downloaded video's frames, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: one workflow file that does text-to-image, image-to-image, ref-to-image, and pose transfer, with the pose driven by a posable dummy instead of a prompt.

## Source

Creator: foxdit. Reddit post:
https://www.reddit.com/r/comfyui/comments/1xt7k7p/h3_image_allinone_workflow_w_pose_studio_lots_of/
(r/comfyui post 1xt7k7p, score 99, 23 comments) | YouTube video:
https://youtu.be/xStAw4T-imM (203 s, downloaded and 12 frames reviewed) |
2026-11-12 scout run, audit 7. Workflow on Civitai:
https://civitai.com/models/3045966/h3-image-w-pose-studio-other-advanced-features-foxfuressence

This is a distinct workflow from the official H3 Image skill (`minimax-h3-image-native-comfyui`): same model, different workflow (Pose Studio node suite, all-in-one modes, template prompt). Do not merge them.

## Tools used

**ComfyUI**, **MiniMax H3 Image**, **Pose Studio** node suite, **Krea 2** (character reference sheets; author's Krea 2 workflow on Civitai, models/2788964). Commenter-mentioned: official **Pose Studio for Qwen 2.1** (separate, from the Pose Studio GitHub).

## Phase 1: Load the workflow

**Do**
1. Download the workflow .json from Civitai (models/3045966) and drag the file from your download folder onto the open space in ComfyUI; it will load in.
2. Use Comfy Manager to download the custom nodes used in the workflow.
3. This is v1.1, released the night the post went up; it "improves pose adherence quite a bit" over v1.0.

**Check**
- Frames reviewed from the downloaded video show the ComfyUI graph with Custom Resolution, Aspect Ratio, and Output Resolution Options node groups, and a detailed prompt panel. If those node groups are missing, the custom nodes did not install.

**Why**
- Drag-and-drop loading is the whole install story. If loading the .json is the hard part, the workflow is broken; here it is one gesture.

## Phase 2: Build the character sheet first

**Do**
1. Create character reference sheets in Krea 2. The author's Krea 2 workflow is on Civitai (models/2788964).
2. You do not strictly need a character sheet, "but with most models, it helps a lot to establish identity." For photoreal results, play with the template prompt to get shots that look natural.
3. Follow the author's template prompt structure, visible in the reviewed frames: subject_definition, retention_analysis, detailed_description (the frame shows "a photorealistic girl in [..]", "preserve the character's identity, appearance, style, colors and proportions", and a detailed description beginning "Generate a close up high angle expressive photo...").

**Check**
- Success "really depends on your character sheet + pose + whether or not you nudged the model with a little prompting" (author). If identity drifts, the sheet is the first suspect, not the pose.

**Why**
- The sheet is the identity. The pose is the action. Mixing the two jobs into one image is how identity breaks.

## Phase 3: Pose with the dummy, not the prompt

**Do**
1. Pose the character with the Pose Studio dummy (frames show the "Easy Character Posing" panel with a posable mannequin and sliders). The author: "it gives direct control over pose."
2. Use the sliders to adjust the dummy's proportions; the model "has the common sense to go with the proportions of the character in your ref image" and the template prompt states it explicitly, but the sliders help the model stay true to the pose.
3. For two characters in one pose: the author has not tried it and cannot comment. His suggested workaround is to put one character in an image, load that image back in, and then place the second, rather than doing both at once. "I usually just bring them together in h3 via prompting."

**Check**
- Commenter Purple-Dragonfruit37: "the prompt guidance is really important!" and "Tried a couple of different poses, but dont really seem like the characters followed the poses." If poses are ignored, prompt guidance (not the dummy) is the fix the thread converged on.
- Note the official Pose Studio for Qwen 2.1 exists separately: "if you have a good finetune of Qwen 2.1 you may prefer the image style over H3 Image." The author's workflow is not an official port of Pose Studio ("which would include a lora to make it work better").

**Why**
- A dummy is a direct manipulation: you see the pose before you generate. A prompt is a request. Direct control fails less often than a request, and when it fails, the failure is visible in the dummy, not hidden in the prompt.

## The human method, distilled

1. Identity from the sheet, pose from the dummy, background and lighting from the prompt. One job per input.
2. v1.1 over v1.0: pose adherence is a versioned fix, not a prompt trick.
3. Two characters at once is untested; build them one at a time and composite.

**Depth status:** PARTIAL (downloaded video + 12 frames reviewed + 22 comments; the video has subtitles but the fetch hit HTTP 429, so no transcript; the Civitai workflow page was not retrieved, so node-level detail beyond the frames is unverified).
