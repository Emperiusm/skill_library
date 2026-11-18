---
name: viggle-motion-transfer-comfyui
description: "Transfer motion from any video onto a character image with the NeuroVigal or Viggle Remake model in ComfyUI on 6GB VRAM: INT8 ConvRot model, Qwen VL auto-prompting, 6 Euler steps at 480p or 720p, RelayVSR 2x upscale, up to 12 seconds with source audio preserved. Trigger when a character needs to perform a motion from a reference video without motion capture."
---

# Viggle Character Motion Transfer in ComfyUI (6GB VRAM)

## Purpose

This audit reconstructs the exact workflow from CG Pixel's tutorial and Reddit post, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: load a character, upload a motion video, let Qwen VL write the prompt, and let the model do the rest.

## Source

Creator: cgpixel23 / CG Pixel. Tutorial: "Viggle in ComfyUI: Character Motion Transfer Made EASY! (6GB VRAM)", https://youtu.be/T5fefIn759o (14 min). Reddit post: "Viggle Character Motion Transfer in ComfyUI – 6GB VRAM + Fully Automated Workflow", https://www.reddit.com/r/comfyui/comments/1xycqcn/viggle_character_motion_transfer_in_comfyui_6gb_vram_fully/ (score 47, 5 comments). Workflow (Google Drive): https://drive.google.com/file/d/1_FoFWRreYRLTG3d9o2MEUiZ2ZOG5Nk2_/view?usp=sharing. Article: https://civitai.com/articles/39038/viggle-in-comfyui-character-motion-transfer-made-easy-6gb-vram. Evidence: full ASR captions (331 segments) mined firsthand, 12 frames from the downloaded video read firsthand, Reddit post text and all 5 comments. 2026-11-17 scout run. Variant note: this is distinct from the earlier Viggle audit (2026-10-02, "Viggle is good": reference-frame discipline, 3 passes good / 5 passes more detail) and from the MiniMax H3 character-swap skills: this is the NeuroVigal/Viggle Remake model with Qwen VL prompting and a 6-step low-VRAM recipe, not masked repainting.

## Tools used

Tools used: **ComfyUI**, **NeuroVigal / Viggle Remake model** (open weights, built on MiniMax H3 + a LoRA; swap and edit modes), **INT8 ConvRot version**, **Qwen VL** (auto-prompting), **RelayVSR** (2x upscaler), **DLSS 5** nodes (optional), **Comfy Kitchen** attention (sparse attention), **MiniMax chunk forward**, **Euler sampler, 6 steps**, **config_animate_H3 custom nodes** (install via `git clone` into ComfyUI custom nodes), **Qwen3-VL text encoder** (named in the workflow as the Qwen VL model; the exact GGUF variant is not stated in the captions).

## Phase 1: Install the model and nodes

**Do**
1. Update ComfyUI to the latest version ("make sure to go to manager and update ComfyUI to the latest version in order to use the Viggle conditioning and Viggle nodes more easily").
2. Install the extra nodes: copy the `config_animate_H3` clone command, open ComfyUI custom nodes in a terminal, `git clone` it there.
3. Download the Viggle Remake model from Hugging Face: the INT8 version, swap mode (there is also an edit mode for editing a video). Alternatively use the LoRA version that converts MiniMax H3 Ref2V into Viggle mode.
4. Load the author's workflow file (Google Drive link above; the workflow itself was not downloaded this run, so no node-by-node inventory beyond what the captions describe is claimed).

**Check**
- The Viggle Remake conditioning nodes appear in ComfyUI; if they do not, the ComfyUI update or the `config_animate_H3` clone is the missing step.

**Why**
The whole workflow is one graph with no subgraphs ("I did not use any sub graph in order to make things more easy"), so a missing node breaks it visibly at load time instead of silently inside a subgraph.

## Phase 2: Set up the motion-transfer graph

**Do**
1. Select the models: Viggle directly, the Qwen VL model, and the INT8 version of the VAE "in order to save some VRAM".
2. Add the optimization nodes: Comfy Kitchen attention with sparse attention, then MiniMax chunk forward "in order to avoid VRAM peaking but also reduce the generation time."
3. Add the keyframe nodes that work directly with the Viggle Remake model (the author: "an important node that you need to include on your workflow").
4. Wire the big Viggle Remake conditioning node: it takes the CLIP, the video, the audio VAE (even though no audio is generated here), the source video, and the reference/target image.
5. Set the sampling: Euler sampler, sigma values set for 6 steps ("it will use only six steps in order to create our video which will help us to boost the video generation speed").
6. Set the resolution from the short edge: Viggle works at 480p or 720p; to change it, set the number to 736 for the higher-resolution version.

**Check**
- The conditioning node shows all five inputs connected (CLIP, video, audio VAE, source video, reference image). A missing reference image means the character is never painted in.

**Why**
Six steps plus INT8 plus sparse attention plus chunked forward is the whole low-VRAM design: every node in this phase exists to keep a 6 GB card from peaking while the model runs.

## Phase 3: Find the paint frames and let Qwen VL write the prompt

**Do**
1. Upload the motion video and set the frame rate to 24 (as for the MiniMax model).
2. Use the frame-finder nodes: they convert the video to images (scale the images down first with Scale Image to Total Pixels), and tell the Viggle conditioning which frames to find and inject/imprint the new reference image on ("pins": frames where the reference image is painted in).
3. Prompting: Qwen VL analyzes the video and auto-generates the prompt. The prompt template combines video description, character description, and motion-transfer instructions. Describe the movement (moving, gesture, dance) and it "can adapt practically to most of the videos."
4. (Author's trick, 9-10 min: use Qwen VL to link the response directly to the original person in the video, so the first character's description is handled automatically; if the replacement is a man, change the description accordingly. If you forget to modify the prompt for the clothes, the outfit from the source video survives: the author's own failed test kept the wrong clothes because the prompt was not updated.)

**Check**
- The frame-finder output shows the frames where the character will be painted; the final prompt reads as a combination of the video description, the character description, and the motion instructions.
- Watch the clothes: a character in the wrong outfit means the prompt still describes the source person.

**Why**
"Image here is going to be painted using some special legal remake conditioning... based on that painting it will try to replace your character and transfer the motion." The paint frame is the anchor: everything else in the video is motion applied to that anchor.

## Phase 4: Generate, upscale, and check the result

**Do**
1. Generate: on the author's setup a 5-second 480p video takes around 20 minutes (post text).
2. Upscale with RelayVSR, a 2x upscaler, to double the resolution "without taking too much time." DLSS 5 nodes are included but optional: bypass or delete them if not installed.
3. Limits, stated by the author: up to 12 seconds, and "the sound is carried out without generation" (audio from the source video is preserved, not synthesized).

**Check**
- Results the author shows: a woman walking on a street (generated with MiniMax H3, used as a replacement test) with lip sync preserved ("it managed to completely change the character while matching the lip sync"); a dancing woman with several different replacement images, all with "perfect character replacement" except the one with the unmodified clothes prompt.
- Failure mode reported in the Reddit comments: faces converge toward the same person ("everyone's face ends up looking practically like the same person" — Far_Patience4517), and one commenter calls the first girl swap "an epic fail". The author's reply: lip sync is handled, "see the first test on my results section at 11:20". Treat face identity as the known weak point; the author's lip-sync claim is demonstrated in the video at 11:20-11:53.

**Why**
The model preserves motion and lip sync because it repaints a character onto the source performance rather than generating a new performance; identity drift is the price, and it shows first in the face.

## The human method, distilled
1. "Load your character reference image, upload your motion video, choose the video duration, let the integrated Qwen VL prompt system analyze the video and handle the prompting, generate the result." (post, quoted: the whole workflow is five user actions.)
2. "It can allow up to 12 seconds and the sound is carried out without generation." (video 0-1 min, quoted.)
3. "Prompting here is very important because it will include video description, character description and the prompt instruction for the motion transfer." (video 4-5 min, quoted.)

## Failure modes
- Face identity drift: replacements converge toward the same face (Reddit comment). Fix: none in the workflow; judge every take on face identity and re-run with a different reference or prompt.
- Wrong outfit: the prompt still describes the source person. Fix: update the character description (including clothes) for every new reference image.
- VRAM peak: the workflow is designed for 6 GB via INT8 + sparse attention + chunk forward. Fix: if it still peaks, drop to 480p (short edge below 736) before changing anything else.
- Lip sync: the author claims it is handled (results at 11:20); a commenter asked specifically whether mouth motion preserves teeth identity. The video demonstrates lip sync on the walking test; teeth identity is not separately demonstrated.

## AAA studio practice
Reference-frame discipline is the standard motion-transfer practice in production: the transfer is only as good as the input video and the chosen reference frame (the 2026-10-02 Viggle audit states the same rule: image-edit the character into the first frame and use that as the reference). The production version of this workflow is built on the same anchor idea, one reference driving the whole shot. Runway's Act-One maps an actor's facial expression, gaze, eye-line, and micro-emotions from a single video input onto a generated character, with no motion-capture rig, and Runway's partnership with Lionsgate builds custom models on the studio's 20,000-title catalog. EbSynth is the older, non-generative form of the same discipline: paint or edit one keyframe and propagate it across the whole shot, preserving the keyframe content at pixel level; the tech was used in production on Richard Linklater's animated feature Apollo 10 1/2: A Space Age Childhood and on an animated sequence in Netflix's Wednesday, and for VFX tasks such as digital makeup and rotoscoping. Wonder Dynamics' Wonder Studio (Autodesk-acquired) does full CG actor replacement with Marvel/ILM validation, and Move AI's markerless mocap carries Sony/Epic adoption; both are the heavier, tracked versions of the same transfer, and both keep a scored acceptance pass per take.

The production version of this workflow adds two gates the skill lacks: a scored identity check per take (face-similarity score against the reference, the same pattern the OmniChar/.char format uses with sface + DINOv2), and a consent record for the source performer, since face replacement requires actor consent under the SAG-AFTRA 2023 AI clause.

Sources:
- Runway Act-One / Act-Two and the Lionsgate partnership (single performance input, facial expression/gaze/micro-emotions, 20,000-title catalog): https://stagerunner.net/runways-just-introduced-a-new-ai-model-that-hopes-to-redefine-motion-capture-for-film-tv-and-games/
- CG Channel, "EbSynth 2 can turn video into animation without using AI" (keyframe propagation, Apollo 10 1/2, Netflix Wednesday): https://www.cgchannel.com/2025/10/ebsynth-2-can-turn-video-into-animation-without-using-ai/
- Wonder Dynamics vs Move AI vs Runway Act-One comparison (Wonder Studio Marvel/ILM validation, Move AI Sony/Epic adoption, SAG-AFTRA consent clause; secondary comparison source, labeled): https://en.ai-pedias.com/compare/wonder-dynamics-vs-move-ai-vs-runway-act-one

### Agent automation upgrade (Do / Check / Why)
**Do**
- After each generation, run an automated face-similarity score (reference image vs sampled output frames) and a lip-sync check, and log both per take; reject takes below threshold automatically and re-run with the next seed.
- Write a paint-frame manifest per take: which frames are pins, the reference-image hash painted at each pin, and the prompt's character description (including clothes) for that take, so a wrong-outfit take can be traced to the prompt that caused it.
- Add a consent note field to the take log: record that the source performer consented or that the source footage is the user's own; refuse to log a take as shippable without it.
**Check**
- The log shows the per-take scores, so a drifted take is rejected by a number instead of by a viewer's comment.
**Why**
- The workflow's only quality gate is the author's eye after a 20-minute generation; scoring the output turns the 20 minutes into a measured take instead of a hope, and the manifest plus consent field are the two production gates the reference-frame discipline already implies.

**Depth status:** FULL (14-min ASR captions, 331 segments, mined firsthand; 12 frames from the downloaded video read firsthand, confirming the ComfyUI graph with Load Video Upload and frame-preview grid; Reddit post text + all 5 comments read firsthand).
