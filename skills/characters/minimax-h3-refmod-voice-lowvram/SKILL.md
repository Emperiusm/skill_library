---
name: minimax-h3-refmod-voice-lowvram
description: "Generate MiniMax H3 video with a consistent character AND voice in ComfyUI on a 6 GB GPU: bake face and voice into reusable RefMod files (no LoRA training), build the dataset from scratch with Qwen Image 2.1, and run the low-VRAM section (H3 SLA Attention, Chunk FeedForward, fused turbo int8). Trigger when doing local character-consistent AI video with voice on a low-VRAM card."
---

# MiniMax H3 RefMods: Character + Voice Video on 6 GB VRAM

## Purpose

This skill reconstructs the exact workflow from EzkaProductions' post and
AmberNova Studio's video walkthrough, step by step, so another agent can
generate MiniMax H3 video with a consistent character and voice in ComfyUI
on a 6 GB GPU. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle). The core method
is: bake face and voice into reusable RefMod files once (no LoRA training),
then generate clips with them on a 6 GB card.

Variant note: this is the same tool family as
`minimax-h3-refmod-identity-comfyui` (image-only identity RefMod, 8 photos,
2026-10-16 post) and `minimax-h3-character-swap-comfyui` (SAM3 +
color-inversion masking for video character replacement), but a different
workflow — video generation, identity AND voice carried by RefMod files,
with a dedicated 6 GB low-VRAM section. Do not confuse the three: the
identity skill is image-only with no voice and no low-VRAM section; SAM3
masks and inverts; this one bakes face + voice RefMods and samples video at
8 steps on int8 models.

## Source

- Post: "RefMods for MiniMax H3: consistent character + voice references,
  running on a 6 GB GPU (free workflow)" by EzkaProductions —
  https://www.reddit.com/r/comfyui/comments/1xnxlvv/refmods_for_minimax_h3_consistent_character_voice/
  (r/comfyui, score 146, 12 comments, 11 retrieved)
- Walkthrough: "RefMods: Consistent Characters & Voice in MiniMax H3 (6GB
  VRAM, ComfyUI)" by AmberNova Studio —
  https://www.youtube.com/watch?v=GHfHmrGeISM (312 s, no captions;
  12 frames reviewed from a local download)
- Workflow (free): https://ambernovastudio.gumroad.com/l/qitclz
- Evidence: full post text, 11 comments, full video description, 12
  reviewed frames. No transcript exists, so spoken narration is
  unavailable; every parameter below is frame- or text-verified.

## Tools used

**RefMods** (ComfyUI custom nodes, `ComfyUI-MiniMaxH3Mod` by Luisacaotica);
**MiniMax H3**; **Qwen Image 2.1** (+ Viggle Turbo low-VRAM variant);
**ComfyUI-GGUF** (low VRAM); KJNodes, rgthree-comfy, ComfyUI-Easy-Use,
Comfyroll Custom Nodes, LayerStyle, ComfyUI-Qwen-TTS (optional, Voice
Design); **ComfyUI-PlagueKind-Nodes** (named in the post's install list).

Install (post text):
`git clone https://github.com/Luisacaotica/ComfyUI-MiniMaxH3Mod`,
`git clone https://github.com/PlagueKind/ComfyUI-PlagueKind-Nodes`,
`git clone https://github.com/kijai/ComfyUI-KJNodes`.

## Phase 1: Build the reference dataset from scratch (Qwen Image 2.1)

**Do**
1. If no reference images of the character exist, create the dataset with
   Qwen Image 2.1 (description text: "I also show you how to create a
   complete dataset from scratch using Qwen Image 2.1").
2. Drive the dataset prompts with a CR Prompt List node (frame-verified, 8
   prompts): close-up portrait of the face, straight-on front view, neutral
   relaxed expression, direct eye contact, face filling most of the frame,
   soft even lighting; close-up of the face turned 45 degrees toward the
   left side of the frame, three-quarter view; the same turned 45 degrees
   toward the right; waist-up shot, front view, arms relaxed at the sides,
   direct gaze; full-body shot, frontal view, relaxed A-pose with arms
   slightly away from the torso and feet shoulder-width apart, head level,
   direct eye contact, even soft lighting; full-body shot turned 45 degrees
   toward the right side, three-quarter view, natural stance; full-body rear
   three-quarter view, glancing back over the shoulder at the camera, soft
   rim light.
3. Append the identity lock to every prompt (frame-verified, truncated in
   frame): "Same person as in <image 1>: identical face, hairstyle, skin
   tone, age, outfit and body proportions, same visual style and ima..."
4. Node settings (frame-verified): start_index 0, max_rows 8.

**Check**
- The picker grid shows 8 photos of the same character ("Amb (1)" through
  "Amb (8)"); one is selected and the button reads "USE IT IN A
  GENERATION". The intro frame reads "Reference images 5/8".

**Why**
Eight angles with a locked identity sentence is the dataset: the RefMod
bakes identity from coverage, not from one hero shot.

## Phase 2: Bake the person RefMod

**Do**
1. Feed the references into the "Create / person reference" node
   (frame-verified inputs: ref_image_0, ref_video_0, refs_bundle, mask,
   av_encoder, vae, mask_list).
2. Set (frame-verified): name "Amber", mode "Full Reference", concept_type
   "identity", background_retention 0.00, ref_resolution 1024, pool_h 16,
   pool_w 16, latent_frames 16, Refinement Steps 0, merge "stack",
   motion_only "full".
3. Save with a filename prefix and subfolder; version with _v1, _v2, etc.
   (frame note: "Filename comes from... Keep name + folder... Use _v1,
   _v2, etc.").
4. Author's framing (post text): "You extract a reference **once** (a
   character from 8 images, or a voice from a short audio clip), save it as
   a reusable 'mod,' and load it into any future generation. No retraining,
   no LoRA. Just load the mod and generate."

**Check**
- The saved RefMod loads as one file in the generation workflow; there is
  no per-generation retraining step.

**Why**
Identity lives in the file: "It stores references instead of training a
LoRA, so you can go from a few photos to a finished clip in a single
session" (description text).

## Phase 3: Bake the voice RefMod

**Do**
1. Upload a clean audio sample (frame-verified: "Amber.wav", 0:09) in the
   Audio Mod upload node; the H3 Audio VAE is already selected
   (minimax_h3_audio_vae_fp32.safetensors).
2. Set in "Create / audio reference" (frame-verified): name "Amber",
   max_seconds 30.0, max_tokens 5120, budget_policy "error", concept_type
   "voice"; write a description.
3. Note the node's own caveat (frame-verified): "Use a clean audio sample,
   30sec max for voice... music, sound effects or speech references.
   Speaker identity transfer is not validated."

**Check**
- Voice is a separate RefMod from face: same name ("Amber"), different
  concept_type ("voice" vs "identity").
- For two characters, the author's tip (post text): "keep each character
  and each voice in **separate mod files** and describe each subject
  clearly in the prompt (name + appearance + position)."

**Why**
Face and voice are independent references; a character that looks right
but sounds wrong fails the same way a wrong face does.

## Phase 4: Generate on 6 GB VRAM (low-VRAM section)

**Do**
1. Place the Apply node correctly (post text): "Load H3 RefMods → Apply H3
   RefMod (between the I2V node and the guider)."
2. Use the workflow's dedicated low-VRAM section with the 6 GB models:
   MiniMax H3 fused turbo int8 (MATLOWAI), Qwen Image 2.1 Viggle Turbo,
   and the hybrid ref2va model (smhfacct
   Minimax-H3-fl2va-ref2va-hybrid-models).
3. Set the attention stack (frame-verified): Model Attention Backend
   "comfy_kitchen attention" feeding MiniMax H3 Low VRAM Attention
   (head_chunks 4) and MiniMax H3 Chunk FeedForward (chunks 2,
   seq_threshold 4096); H3 SLA Attention with sparsity_ratio 0.90,
   block_size 64, min_seq_len 8192, dense_last_steps 0, protect_audio
   "protect", enabled "sparse", dense_steps 1, dense_backend
   "comfy_kitchen", disable_fp16_accum "disabled (recommended)",
   stabilize_motion "off", Protect Image/Video Reference "Off",
   tail_correction "off", use_int8_qk "on (experimental)".
4. Load the Video Generation models (frame-verified): unet
   "minimax_h3_hybrid_fl2va_ref2va_825-40-int8.safetensors", clip
   "qwen3vl_32b_minimax_fp8_e4m3fn.safetensors", vae
   "minimax_h3_video_vae_fp8.safetensors", vae_1
   "minimax_h3_audio_vae_fp32.safetensors"; Model Preview Override
   max_resolution 1024, preview_quality 80, suppress_default_preview true,
   preview_fps 12, tiny_vae "taeh3.safetensors".

**Check**
- The workflow has two dedicated video-generation sections; one is built
  specifically for low-VRAM GPUs (6 GB) "with dedicated models that fit
  properly on this kind of graphics card" (description text).
- The author confirmed the 6 GB claim in the comments: "Yes. Try the
  workflow" (in reply to "So you can actually generate consistent
  characters and audio with 6gb vram?").

**Why**
Sparse attention + chunked feedforward + int8 weights is what fits H3 on
6 GB; the recipe is the low-VRAM section, not a smaller prompt.

## Phase 5: Apply the RefMods and sample

**Do**
1. In "Apply H3 RefMod" (frame-verified): Characters/Amber 1.00, retention
   0.85, curve_direction "constant", scramble_seed 1291797728,
   control_after_generate "randomize", curve_shape "linear", curve_value
   1.00, graph_preset "(none)", scramble_mode "shuffle", scramble_keep 1,
   max_total_tokens 0; audio/Amber 1.00.
2. The author's stated strengths (post text) are visual 0.9 for the
   character and audio 0.9 for the voice — the frame shows the walkthrough
   video's 1.00 values; treat 0.9 as the author's setup and 1.00 as the
   video's shown values, not as a contradiction to resolve by guessing.
3. Sample with sampler_name "res_multistep", scheduler "simple", steps 8.
4. Create Video at fps 24, bit_depth auto, color_space sRGB.
5. Starting guidance from the workflow's own note (frame-verified): "Start
   with strength 2.0 and version 1."

**Check**
- The generated frames keep the same face across scenes (Babylon street,
  Amalfi-coast terrace) and the same voice reference throughout.
- Author's honest results (post text): "Visual identity: very consistent.
  Same face, hair and outfit across different scenes" and "Voice:
  Consistent voices from clip to clip."

**Why**
Retention 0.85 with a constant curve is the identity hold: the RefMod
steers every step, and the strength-2.0 starting point is the author's
calibrated default.

## The human method, distilled

1. Bake identity once (face + voice, separate files), prompt scenes forever.
2. Eight angles make the dataset; one angle does not.
3. Fit the model to the card: int8 + sparse attention + chunked feedforward
   is the 6 GB recipe, not a quality compromise to apologize for.
4. Start at strength 2.0, version 1; change one thing at a time.
5. Two characters means two mod files per character and per voice, each
   subject described by name, appearance, and position.

## Failure modes

- **"You don't need refmods for this."** Commenter boobkake22's challenge:
  regular reference-to-video may do the same job for a single clip. RefMod
  pays off across clips (same character and voice, reused), not for a
  one-off.
- **Voice mismatch and babble are open questions.** Commenter
  Beneficial_Fish_7509 asked whether RefMods solve the standard ref2va
  failure modes (wrong voice vs the reference; babbling "when there is
  supposed to be silence") — unanswered in the thread. Test silence and
  voice match explicitly before trusting a voice RefMod.
- **Speaker identity transfer is not validated.** The audio-reference
  node's own caveat; do not claim a cloned voice from one 9-second sample.
- **Generation time and clip length unanswered.** Commenter look_a_dragon
  asked how long generation takes and how long the clips are — no answer
  in the thread.
- **FastH3 not covered.** Commenter xivurs wants this to work for FastH3;
  the workflow shown is standard H3 only.
- **The "slop look" objection.** Commenter seppe0815: "allways the minimax
  a.i slop look." Identity consistency does not fix the base model's look;
  judge the look separately from the consistency.

**Depth status:** FULL (frame-verified parameters from 12 reviewed frames;
no transcript/captions, so spoken narration is unavailable; post text and
comments corroborate the setup).
