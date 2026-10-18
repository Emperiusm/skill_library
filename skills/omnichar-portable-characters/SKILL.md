---
name: "omnichar_portable_characters"
description: "Ship consistent AI characters across image and video models with the portable .char format: encode face/body/wardrobe references once with the ComfyUI-Omnichar custom nodes, then decode the same file into Minimax H3, Krea2, Flux2 dev, or klein 9B/4B. Trigger when a character must keep the same face, body, and clothes across every model and shot."
---

# OmniChar Portable Characters: One .char, Every Model

## Purpose

This skill teaches the OmniChar workflow end to end: build a character once as
a portable `.char` file, then feed the same identity to any supported
generator. Every phase has three parts: **Do** (the action), **Check** (how
the human verifies it), and **Why** (the principle). The core method is:
encode once, decode per model.

## Source

Creator: ashishsanu (omnichar). Source post:
https://www.reddit.com/r/comfyui/comments/1wwmstf/one_char_model_consistent_face_body_cloths_now/
(video demo: https://v.redd.it/w19nx5ws09th1). Repo:
https://github.com/omnichar/ComfyUI-Omnichar (public, GPL-3.0; created
2026-10-02). Audited 2026-10-05.

## Tools used

ComfyUI (Python 3.10+); custom node pack **ComfyUI-Omnichar**
(`git clone https://github.com/omnichar/ComfyUI-Omnichar` into
`ComfyUI/custom_nodes`, then `pip install -r requirements.txt`, restart
ComfyUI); **omnichar-sdk** (Apache-2.0, dependency-free `.char` reader,
`pip install omnichar-sdk`); character builders: **Encode Character** node or
**Omnichar Studio** (omnichar.org, own GPU) or **Omnichar Cloud**
(cloud.omnichar.org). Supported generators: **Minimax H3**, **Krea2**,
**Flux2 dev**, **klein 9B**, **klein 4B**. Identity scoring at encode time:
cropped face scored by **sface** and **DINOv2** (author's stated method).

## The .char format

A `.char` file holds a character's reference images, its locked description,
and often a trained LoRA. Put `.char` files in `ComfyUI/models/characters/`;
the loader lists whatever is there. To share one folder with Omnichar Studio,
set `INLINE_CHARACTERS_DIR` to the Studio characters directory and both read
the same files.

## The nodes

| Node | Inputs | Outputs |
|---|---|---|
| Load Character | `char`, `char_path` | `char` |
| Decode Character | `char`, `style`, `clip`, `prompt`, `arch`, `max_references`, `size_from`, `fit` | `conditioning`, `references`, `refs`, `sheet`, `prompt` |
| Character Reference | `refs`, `index` | `image`, `role`, `count` |
| Character References Split | `refs` | `image_0` to `image_4`, `count` |
| Character Reference Latent | `conditioning`, `refs`, `vae` | `conditioning` |
| Apply Character LoRA | `model`, `clip`, `char`, `strength`, `arch`, `min_key_coverage` | `model`, `clip` |
| Encode Character | `name`, `description`, `resolution`, `face`/`body`/`cloths` (3 slots each) | `char` |
| Save Character | `char`, `filename`, `overwrite` | `path` |

## Phase 1: Install

**Do**
1. `cd ComfyUI/custom_nodes && git clone https://github.com/omnichar/ComfyUI-Omnichar`
2. `cd ComfyUI-Omnichar && pip install -r requirements.txt`
3. Restart ComfyUI.

**Check**
- The eight nodes above appear in the node menu. If they show as missing
  after an install-by-URL, follow the README installation steps, then retry
  with the direct git URL (the author's fix for the "installed with url
  still showing same" failure).

**Why**
The nodes are thin wiring: the `.char` format is read by the standalone
SDK, so installation is just cloning plus the reader dependency.

## Phase 2: Encode the character

**Do**
1. Collect references: face, body, and wardrobe, three slots each.
2. In **Encode Character**, set `name`, `description` (the locked character
   description), and `resolution`; wire the face/body/cloths images into
   their slots.
3. **Save Character** with `filename` to write `<name>.char` into
   `ComfyUI/models/characters/`.

**Check**
- Encode Character sorts references by role so face comes first; prompts
  address images by number, so slot order is the contract. The author's
  method "encodes character prompts [and a] cropped face which is scored by
  sface & dinov2": the identity is scored at encode time, not eyeballed
  later.

**Why**
Identity becomes data: one file, one locked description, one scored face,
reusable by every generator instead of a prompt you retype per model.

## Phase 3: Decode into the target model

**Do**
1. **Load Character** reads the `.char`.
2. **Decode Character** resolves it into `conditioning`, `references`,
   `refs`, `sheet`, and `prompt`.
3. Route by model family, preserving reference order:
   - One-batch models: wire `references`.
   - Numbered-slot models (MiniMax H3): `refs` into **Character References
     Split**, or one **Character Reference** node per slot.
   - Latent-reference edit models (FLUX.2): `refs` into **Character
     Reference Latent** on both positive and negative conditioning.
4. If the character carries a LoRA: **Apply Character LoRA** on MODEL and
   CLIP, setting `strength`, `arch`, and `min_key_coverage`.

**Check**
- "Reference order is preserved, because a prompt addresses images by
  number." Verify slot N in the prompt matches image N before generating.

**Why**
Each model family consumes references differently (batch, slots, latents);
decoding adapts one resolved set at the last step instead of rebuilding
per-model reference packs.

## Phase 4: Generate

**Do**
1. MiniMax H3: start from the default MiniMax ComfyUI workflow with the
   split references in numbered slots; adjust params and resolution. The
   author notes the character part itself needs no heavy specs beyond what
   MiniMax requires.
2. FLUX.2 Klein 9B: use the shipped references-as-latents workflow
   (`workflows/` in the repo) to an image.

**Check**
- Benchmark from the thread (16 GB VRAM, 32 GB RAM, same reference images
  both ways): raw reference-image prompting OOM'd above 0.8 MP; the `.char`
  path completed at 1 MP and was judged better than reference images. If
  you OOM with references, encode first.

**Why**
Pre-encoding and scoring the identity once is cheaper than re-resolving raw
reference images on every run: less VRAM, same face every time.

## Phase 5: Keep the voice consistent (2026-10-08 expansion)

Added from ashishsanu's follow-up post and its comments
(https://www.reddit.com/r/comfyui/comments/1wz405c/ — "Omni .char now with
consistent voice, just by dropping a few seconds sample audio: Minimax
H3"). Same tool family, new capability: the character now carries a voice,
not just a face, clothes, and body.

**Do**
1. Load an audio sample of **a few seconds (commenters converge on 5
   seconds max)** with good vocal range — e.g. the character talking
   between sentences, covering highs and lows. Per ashishsanu: "good to
   have a vivid audio sample with different types of notes being covered."
   Per Hrmerder: "less is generally much much better as long as there is a
   tonal range in those few seconds."
2. In the voice prompt, instruct H3 to **take only the vocal timbre** from
   the reference and generate delivery appropriate to the scene contents.
   ThaSipah's recipe: "Load Audio node with a max of five seconds, with a
   clip with good range, then my `<audio 1>` instruction is to only take
   the vocal timbre and H3 should generate delivery appropriate to the scene
   contents, and it's better than anything I've tried."
3. Test the dumb version first: Hrmerder's "`<audio x>` is the voice of
   (whomever) from `<image x>`" reportedly works "about 90 percent of the
   time" before adding any machinery.

**Check**
- Generated speech matches the character's scene emotion, not the
  reference sample's emotion: timbre from the sample, acting from the shot.

**Why**
Splitting timbre from delivery lets one short sample cover any scene: the
voice stays the character's, the acting follows the shot. Five vivid
seconds beat a minute of flat reading because the model needs the timbre
envelope, not content.

**Caveat:** one commenter calls the demo quality "abysmal" (Terrible_Scar);
the voice recipe is reported working by the author and two independent
commenters, but judge the output yourself.

## The human method, distilled

1. "Build a character once, use it across image and video models": identity
   is a file, not a prompt.
2. Encode once, decode per model: keep one resolved reference set and adapt
   it at the last step.
3. Score the identity at encode time (sface + DINOv2 on the cropped face)
   instead of judging consistency by eye afterward.
4. Constrain the reference to the smallest sufficient signal: 5 seconds of
   timbre, not 60 seconds of delivery (Phase 5).
5. Know the roadmap limits: multi-character support is stated as next, not
   shipped; one character per generation for now.

## Failure modes

- **Nodes missing after install-by-URL**: follow the README install steps,
  then the direct git URL (author's prescribed fix).
- **OOM with reference images past ~0.8 MP on 16 GB VRAM**: pack the same
  references into a `.char` and regenerate; the encoded path completed 1 MP
  on the same card.
- **Wrong face in a slot**: reference order is the addressing scheme; check
  that prompt image numbers match the role-sorted order (face first).
- **Voice sounds like the sample's emotion, not the scene's**: the prompt
  is leaking delivery, not just timbre — restate the timbre-only
  instruction (Phase 5).
- **Flat voice**: the sample had no tonal range — re-record 5 vivid seconds
  (Phase 5).

**Depth status:** FULL (repo README with exact node I/O + author comments
with method detail and VRAM benchmarks) for the `.char` format; PARTIAL for
the voice recipe (author + two commenter reports, one quality complaint
unaddressed).
