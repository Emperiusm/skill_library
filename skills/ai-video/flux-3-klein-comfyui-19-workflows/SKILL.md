---
name: flux-3-klein-comfyui-19-workflows
description: "Run FLUX 3 Klein (Black Forest Labs) in ComfyUI for text-to-image, image editing, and multi-image combining using Pixaroma's 19 free workflows: prompt discipline, prompt upsampler, Layout Boxes, inpaint crop/stitch, text edits, character sheets, outpaint LoRA, and ref-image combining up to 10 images. Trigger when generating, editing, or combining images with FLUX 3 Klein in ComfyUI."
---

# FLUX 3 Klein in ComfyUI | 19-Workflow Generate / Edit / Combine Pack

## Purpose

This skill reconstructs the exact workflow pack from Pixaroma's episode 39
(26:37, 658 caption segments + 12 frames reviewed), step by step, so another
agent can run the same workflows. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the principle).
The video's core method is: one model file set does three jobs (generate,
edit, combine); the workflow pack standardizes node roles by color; long,
disciplined prompts and box-scoped edits replace masking and masking
pipelines.

## Source

- Video: "Flux 3 Klein in ComfyUI | Generate, Edit & Combine Images (Ep39)"
  by pixaroma (Reddit: pixaromadesign) —
  https://www.youtube.com/watch?v=ntxxhO9H3bY (26:37, 22,639 views at audit)
- Post: https://www.reddit.com/r/comfyui/comments/1xauho2/flux_3_klein_in_comfyui_generate_edit_combine/
  (score 31, 9 comments)
- Workflows: 19 free ComfyUI workflows, download from the description link
  (pixaroma.com)
- Evidence: full ASR caption transcript + 12 high-res frames from the
  downloaded video, 2026-10-22 scout run. Workflow JSON files themselves were
  not downloaded.

## Tools used

- **ComfyUI 0.41 or newer** (required; check with the version-check node —
  double-click the canvas, add "version check")
- **Pixaroma custom nodes 1.4.223 or newer** (the workflows are built on
  Pixaroma nodes; older installs need an update; the Pixaroma help page has
  update steps for every install type)
- **FLUX 3 Klein model files** (Black Forest Labs): three files — the
  diffusion model, the text encoder, and the VAE. The Hugging Face repo
  needs a free approval (log in, open the FLUX 3 page, click "Agree and
  access repository" — once only)
- **Z-Image Turbo + its text encoder + its VAE + an upscale model** (only
  for the realism pass; four extra files)
- **Black Forest Labs prompt upsampler** (writes long Flux-3-style prompts
  from a short idea; one file)
- **FLUX 3 outpaint LoRA** (only for the outpaint workflow)

## Phase 1: Set up versions and model files

**Do**
1. Confirm versions: ComfyUI ≥ 0.41, Pixaroma nodes ≥ 1.4.223 (the
   version-check node shows both).
2. Open "Download models" first (the top buttons on every workflow). Get
   the free Hugging Face approval for the FLUX 3 repo once.
3. Download the three files: the model goes in `diffusion models/Flux 3`,
   the text encoder in `text encoders`, the VAE in `vae`. Take the model
   **without "base" in its name** — that is the fast (distilled) version.
4. Restart ComfyUI (or press R) to refresh the model lists.
5. Note the license: images may be used for paid work while yearly revenue
   is under $5 million.
6. Add the workflows folder to ComfyUI (the help page shows where to put
   it); they appear in the workflows panel under the episode 39 folder.

**Check**
- The version-check node shows the required versions or newer.
- After restart, the model, text encoder, and VAE appear in their
  dropdowns.

**Why**
The pack is version-gated (ComfyUI 0.41+, Pixaroma 1.4.223+); the
"without base" checkpoint is the speed variant, and the HF approval is a
one-time friction that blocks all downloads if skipped.

## Phase 2: Learn the node color convention

**Do**
1. Orange nodes load the models (touch only when changing files).
2. Blue nodes are the only ones you change — numbered in order
   (step 1, step 2, ...).
3. Green nodes do the work.
4. The red node saves. Outputs land in ComfyUI's output folder, one
   subfolder per workflow (e.g. `flux 3 Klein`, `flux 3 Klein realism`,
   `flux 3 Klein layout`).

**Check**
- Frame evidence: every workflow graph in the video follows this coloring
  (frame_006, frame_010).

**Why**
The convention makes 19 graphs skimmable: you only ever touch the numbered
blue nodes, in order. (Inference: this is also what makes the pack
automation-friendly — the human-input surface is labeled and ordered.)

## Phase 3: Write prompts the way FLUX 3 likes them (applies to every workflow)

**Do**
1. Write long, detailed prompts: the kind of photo, the person, **what each
   hand does**, the place, the light. "The more you describe, the less it
   has to guess."
2. Put words that must appear in the image in **double quotes** (e.g. the
   word Pixar on a T-shirt).
3. When editing or combining, end the prompt with **what must stay** —
   Black Forest Labs' own convention (face, hair, clothes, pose, jewelry).
4. Run times on the author's card: text-to-image ~4 s after the first run;
   image edit ~6 s; restyle ~5 s per row; character sheets ~13 s for both;
   outpaint ~7 s; two-image combine ~9 s; four-image group photo ~19 s.

**Check**
- Compare the short-prompt control vs. the long-prompt run: the short
  prompt ("the same idea in one short line") produced a different woman,
  a plain building, the word on a white sticker, and a broken hand.

**Why**
Short prompts make the model guess; the failure modes below are mostly
short-prompt failures, not model limits.

### Known failure modes and fixes (author's honest section)

1. **Hands:** with a short prompt only 2 of 4 hands came out clean.
   Fix: describe the gesture and give every hand one job → all four
   came out right. Also: "describe everything you want to see, hands
   included."
2. **Soft faces:** faces look too smooth ("almost like plastic") at normal
   size. Fix: generate at 2K, or run the Z-Image realism pass (Phase 5).
   Small faces far away come out worse — keep people close (portraits,
   half-body, selfies).
3. **The "AI look"** (warm glow, blurry background, perfect skin): say
   where the light comes from and what kind of photo it is.
4. **Text:** a handwritten font can change a letter. Use bold capitals,
   quote the words, and check every word; a wrong letter usually goes away
   with another seed.

## Phase 4: Generate — text to image

**Do**
1. Step 1: the prompt (see Phase 3).
2. Step 2: the size (portrait / landscape). Step 3: **F** keeps the same
   picture, **R** makes a new one every run.
3. Press run.

**Check**
- Same prompt + same seed + landscape = the same wide photo; the word on
  the shirt is spelled right (the "Pixar" T-shirt selfie test).

**Why**
Seed control + size switching gives you compositional variants without
re-prompting.

## Phase 5: Generate — Z-Image realism pass

**Do**
1. Load the four extra files (Z-Image Turbo, its text encoder, its VAE,
   an upscale model) from "Download models".
2. Prompt, size, and seed work exactly like Phase 4.
3. Step 4 sets how much the extra pass may change the picture. Start at
   **0.2**. (To try higher, open the gear and add a 0.5 button.)
4. Press run. Takes ~20 s after the first run. The bigger picture is
   saved under `flux 3 Klein realism`.

**Check**
- Drag across the image-compare: pose and text stay the same; up close the
  skin is a little more real and eyes/hair are sharper.
- At 0.5 the author got a different face with brown eyes, fewer freckles,
  and an older look: "A higher number does not mean more realism."

**Why**
The realism pass is a 2× light re-render of the same picture; it works
best on portraits and half-body shots where the face is big. In full-body
pictures the face is small and Flux 3 struggles with it even more.

## Phase 6: Generate — prompt upsampler

**Do**
1. Step 1: your idea in a line or two. Start with the kind of picture
   (e.g. "polished CG animation still") so it keeps that look.
2. The BFL upsampler (one new file) writes the full prompt in ~4 s;
   "Show text" shows what Flux 3 received.
3. Step 4 switches between the AI's prompt and "as typed".
4. On an RTX 30 card, if the run stops with a CUDA error: restart
   ComfyUI, open the gear on "AI prompt", and turn off "faster writing".

**Check**
- "As typed" gave the bunny in a plain doorway; the AI's prompt gave the
  whole cozy burrow home. But a word like "magical" filled the picture
  with glowing mushrooms and sparkles — so for a simple picture, use a
  few calm words; for a prompt you wrote yourself, use "as typed".

**Why**
The upsampler is trained to write prompts the way Flux 3 likes them; the
"as typed" toggle keeps hand-crafted prompts from being overwritten.

## Phase 7: Generate — text in images (product labels)

**Do**
1. No new files. Step 1 has find-and-replace boxes: the big name in the
   first row, the small line in the second.
2. In the prompt, placeholders mark where each line goes, in double
   quotes with the style of its letters.
3. Example: the jar says "Pix-O-Roma" with "wildflower honey" under it.
   For a new label, change only the words (e.g. "lavender honey") and
   run again.

**Check**
- Both lines on the label, spelled right, in the requested style; the jar
  stays the same. Capital letters work best; a wrong letter usually goes
  away with another seed.

**Why**
Words get their own input boxes so label variants are word-swaps, not
re-prompts.

## Phase 8: Generate — Layout Boxes (multi-object + text placement)

**Do**
1. Use the new Pixaroma "Layout Boxes" node: a small canvas with the
   shape of your picture. (ComfyUI has its own box node, but it only
   shows in Nodes 2.0; Layout Boxes works in both looks and gives Flux 3
   exactly the same thing.)
2. Each box is one thing with a number and a short description. Click a
   box to select; corner squares resize it; drag inside to move; drag an
   empty spot to draw a new box. Undo reverts each change. A box can
   also be a text box for words in the picture.
3. Step 1: size (the canvas takes the same shape). Step 2: the boxes
   (e.g. apple left, cappuccino middle, two old books right; colors go
   in the words, box color is only for visibility).
4. Step 3: the prompt describes the whole scene and names each box by its
   number tag. "Show text" shows the prompt with the boxes appended.

**Check**
- Every object lands in its own box with its own shadow — 4 out of 4
  seeds in the author's tests.

**Why**
Bounding-box conditioning removes compositional guessing; the prompt
narrates, the boxes place.

## Phase 9: Generate — image to prompt to image

**Do**
1. Load a picture you like in step 1; in step 2 pick a size close to its
   shape. (Uses the same upsampler file as Phase 6.)
2. Step 5: "As it is" asks for a copy; "plus my extra instructions" adds
   the change from step 4 (e.g. a snowy winter scene with a red knitted
   scarf).

**Check**
- "As it is" is close but not an exact copy — pose and small details
  change. The scarf variant is the same bunny, now in snow.

**Why**
This is for style-transfer-from-reference. To change one thing in the
same picture, use the edit workflows (Phase 10+) instead.

## Phase 10: Edit — change the whole image with an instruction

**Do**
1. No new files. Load your picture in step 1 (e.g. a woman in a red
   dress in a plain studio).
2. Step 2: write the change as an instruction ("Place her on a quiet
   cobblestone street on a sunny morning"), then end with what must stay
   (her face, her hair, the red dress, her pose, the jewelry).
3. Press run (~6 s).

**Check**
- Drag across image compare: face, dress, and pose stay the same.

**Why**
Two limits to know: a new place is easier than new light (the street was
sunny but the light on her stayed soft, like in the studio), and the
whole picture is redrawn, so small details can shift. To change one area
only, use Phase 11.

## Phase 11: Edit — box-scoped inpaint (keep every other pixel)

**Do**
1. Load your picture in step 1. Step 2 is Sketch: pick the box tool,
   drag a box around what you want to change (make the box the size you
   want the new thing to be), and write the change in its note (e.g.
   "Replace it with a dark green leather armchair with rounded arms and
   short wooden legs").
2. "Inpaint Crop" cuts out the box area, Flux 3 changes only that piece,
   "Inpaint Stitch" pastes it back. You can also box an empty spot to
   add something new (e.g. a painting on a wall).

**Check**
- A new armchair in the same spot, the rest of the room exactly the same.
  If a small color change appears around the box: raise the softness on
  "Inpaint Stitch", try color match, or a new seed.

**Why**
Box-scoped editing is the mask-free edit: outside the box, pixels are
guaranteed untouched.

## Phase 12: Edit — change the words in a picture

**Do**
1. No extra downloads. Load the picture in step 1 (e.g. the word "love"
   in orange balloon letters).
2. Step 2: put the old word and the new word in double quotes
   ("Change the word love to Pixar in the same glossy orange balloon
   letters at the same size and in the same place"). To add a line,
   give its words, its letters, and where it goes ("Fantasy stories in
   small brown capitals centered below").

**Check**
- "Pixar" in the same balloon style with the new line under it. "In my
  tests, the spelling was right every time, but the size can change a
  little" — try another seed if the size matters.

**Why**
Flux 3 redraws the words in the same letter style; quoting anchors the
edit to the exact string.

## Phase 13: Edit — restyle a photo (batch of styles in one run)

**Do**
1. Load the photo in step 1. Step 2 is "Prompt each": one style per row
   (e.g. a 3D animated film, a thick oil painting, an anime drawing).
   Turn off rows you don't need, add your own.
2. A good row says what the style is made of (brush strokes, flat
   shading) and ends with what stays. "Ask to keep her likeness, not
   her face. Keeping her face exactly gives you a photo with a filter."
3. Press run once — one picture per row, ~5 s each.

**Check**
- A 3D film character, an oil painting with thick strokes, and an anime
  girl, all clearly her.

**Why**
One run, N styles: batching is the point; "likeness, not face" keeps
the restyle from collapsing into a filter.

## Phase 14: Edit — change season / time of day (relight)

**Do**
1. Step 2 is "Prompt each": one row per version (a snowy winter day, a
   moonlit night, a sunset). The trick: say what the new light does to
   everything — where the snow lands, which lights glow, what happens
   to the furniture. ("When I only wrote keep the furniture unchanged,
   the armchair stayed in daylight under the moon.")
2. Press run once (~16 s for all three).

**Check**
- Snow on the roof and the chair; a blue moonlit night with warm light
  in the window; a warm sunset with long shadows.

**Why**
Relighting needs per-object light instructions; a blanket "keep X
unchanged" keeps its lighting too. On portraits the light changes less —
the model mostly makes a face warmer or cooler.

## Phase 15: Edit — restore and colorize old photos

**Do**
1. Load the old photo in step 1. Step 2: first say what to fix
   (scratches, dust, crease, stain), then name a color for every piece
   of clothing and for the place. ("With just natural colors, they came
   out pale every time.")

**Check**
- The damage is gone and every color is where asked. Honest note: "An
   old photo holds very little detail, so Flux 3 redraws the faces.
   They look right, but they're a likely version of the people, not the
   real ones. Compare them with the original before you share it."

**Why**
Restoration is re-creation: color names are required per item, and
redrawn faces are plausible, not archival.

## Phase 16: Edit — character sheets (turnaround + expressions)

**Do**
1. Load your character in step 1 (whole body for a turnaround).
2. Step 2 is "Prompt each" with one row per sheet; change the clothes
   and colors in both rows to match your character. The tag "ref image
   0" means your loaded image.
3. Step 3: pick a wide size so all views fit side by side. Press run
   (~13 s for both sheets).

**Check**
- The front, three-quarter, side, and back views, plus six expressions,
  of the same character. "The expression sheet came out right on every
  seed I tried. The turnaround sometimes gives two front views, so try
  a few seeds."

**Why**
One reference image → a model-sheet pair: the wide canvas makes the
model lay out consistent views; seeds repair duplicate-view failures.

## Phase 17: Edit — outpaint wider/taller

**Do**
1. This one adds a small outpaint LoRA (link in "Download models").
2. Step 2: "Outpaint" picks the new shape (e.g. 16×9) and adds gray
   bands around your picture.
3. Step 3: keep the first sentence as it is (it is the LoRA's
   instruction); after the word "scene", describe what's in your
   picture.
4. Press run (~7 s). Then "Outpaint Stitch" puts your original picture
   back in the middle, so only the new parts are painted.

**Check**
- "In my tests, the join was invisible, even at full size."

**Why**
The stitch step is the guarantee: your original pixels are restored
into the center, so outpainting can only add, never alter.

## Phase 18: Combine — character into a scene (ref images)

**Do**
1. Same three model files. Picture 1 = the character (the bunny
   explorer); picture 2 = the place (a white room by the sea).
2. Each picture gets a tag in the prompt: "ref image 0" is picture one,
   "ref image 1" is picture two. The prompt says: "place the bunny
   explorer from ref image 0 in the room from ref image 1", then where
   it sits, what each paw does, and what stays the same.
3. "Give every hand or paw one job. Just waving at the camera gave a
   blurry paw that melted into the wall."

**Check**
- The bunny sits in the armchair and waves. The room is similar, but
   not the same — the camera came closer and some things moved.
- Rule: picture 1 sets the shape of the result, so put first the
   picture whose shape you want.

**Why**
Multi-reference combining is prompt-tagged, not masked: ref tags bind
subjects to sources; the scene layout is regenerated, so expect
compositional drift.

## Phase 19: Combine — outfit change

**Do**
1. Picture 1 = the person (a man in a navy blue suit); picture 2 = the
   clothes laid out flat (a black T-shirt with an orange "Pixie Rock"
   band print, faded jeans).
2. The prompt names each piece of clothing, describes the print in
   words, then says how he should stand — then what stays (his face,
   his hair, the gray background).

**Check**
- The same man in the same pose, now in the T-shirt and jeans, the
   print from picture two.

**Why**
Limit: change only what the photo shows. When the author asked for
white sneakers on a thigh-up photo, Flux 3 changed the whole shot to
show his feet — out-of-frame requests reframe the composition.

## Phase 20: Combine — logo on a product

**Do**
1. Picture 1 = the product (a black mug); picture 2 = the logo, best on
   a plain background.
2. The prompt says where the logo goes, its color, and its size ("On
   the side of the mug, in bright glossy orange, about half as tall as
   the mug"). The logo can be black in the source — you pick any print
   color.

**Check**
- The logo printed in orange, following the curve of the mug. "In my
   tests, the logo kept its exact shape every time. The size words steer
   it only loosely, so try a few seeds until one fits."

**Why**
Flux 3 prints onto the surface and follows its curvature; size is a
soft constraint, resolved by seed.

## Phase 21: Combine — group photo (up to 10 refs)

**Do**
1. Load the pictures (e.g. two women, the man in the suit, the bunny).
   "To add a fifth person, wire another Load Image Mini into the next
   free slot. Flux 3 takes up to 10 pictures."
2. Set the scene like a photographer: everyone stands in one row on the
   same floor, left to right; nobody stands in front of anybody. Say
   the size of anyone who isn't an adult (the bunny stands on the low
   wall, its head level with the man's shoulder). Give every hand a job
   (arms around each other's backs).
3. Press run (~19 s for four pictures).

**Check**
- All four on a sunny terrace by the sea, each with their own face and
  clothes. "Look closely and you'll see it can still struggle with
  hands and eyes."

**Why**
Group composition is explicit staging language, not hope: row order,
floor, relative heights, and per-hand jobs are all stated.

## Phase 22: Combine — product ad (3 pictures)

**Do**
1. Picture 1 = the place (the white room) — keep the place FIRST.
   ("With the mug first, Flux 3 made up its own room every time.")
2. Picture 2 = the product (the black mug); picture 3 = the logo.
3. The prompt describes the shot and asks for the framing: "The camera
   moves in close to the side table, the mug with the orange logo, and
   steam rising from the coffee."

**Check**
- A close product shot in the same room, door and sea softly blurred
  behind. "Without it [the framing], the whole room stays in view, and
  the mug comes out tiny." Check the logo at full size — "Sometimes it
  loses its curved base, so try another seed."

**Why**
Input order is semantic: the first picture anchors the world; the
framing sentence is what makes the product the subject.

## AAA studio practice

Studios do not run Flux 3 Klein publicly, but the pack's conventions map
directly onto documented production AI-image pipelines:

- **Prompt engineering as a hiring gate (Round8 Studio / *Lies of P*,
  reported May 2026).** Their "AI Creator" role builds a pipeline of Stable
  Diffusion and Midjourney concept drafts, AI texturing, project-specific
  LoRA/ControlNet training, and post-processing (inpainting, outpainting,
  high-resolution upscaling) "to ensure AI-generated assets meet production
  standards." Candidates must demonstrate "excellent prompt engineering and
  parameter control skills." This is the closest AAA-adjacent analog to the
  pack: prompt discipline plus inpaint/outpaint/upscale passes treated as
  production criteria, not optional polish.
  Source: https://www.invenglobal.com/articles/21761/round8-studio-launches-major-recruitment-drive-introduces-ai-creator-role
- **Batch runs with low-res review passes (Moment Factory, official ComfyUI
  case study, 2026).** The production studio runs custom ComfyUI workflows
  generating 20+ artistic directions at 20-40 iterations per direction,
  reviewing deliberately low-resolution passes for art-direction decisions
  ("not about polish... about validation and decision-making"), then
  inpaints approved regions, preserves composition, and upscales selects to
  18K. One operator drives the workflow while teammates tune prompts and
  select. Matches the pack's "Prompt each" batch rows (Phases 13, 14, 16)
  and the Z-Image realism pass (Phase 5), except the studio separates
  generation from upscaling by approval stage.
  Source: https://blog.comfy.org/p/case-study-how-moment-factory-reimagined
- **Proprietary diffusion as a launch point, never the finish (Blizzard
  Entertainment, reported by The New York Times, May 2023).** "Blizzard
  Diffusion" trained only on Blizzard-owned imagery so artists could turn
  prompt text into Blizzard-style concept launches for characters, outfits,
  and environments; it was used to fit cosmetic headpieces to WoW player
  models. Studio framing: remove repetitive manual work so artists spend
  time on creativity, with AI supplementary to human art direction.
  Source: https://www.gameshub.com/news/news/blizzard-entertainment-ai-concept-art-may-2023-2617179/
- **AI output confined to low-stakes surface area (Squanch Games, *High on
  Life*, shipped Dec 2022).** The studio confirmed Midjourney use for in-game
  movie posters and "finishing touches" to world set decoration; most art
  stayed hand-drawn. The production discipline: novel tools ship in the
  safest surface area first.
  Source: https://www.gamedeveloper.com/business/justin-roiland-revealed-i-high-on-life-i-features-ai-art-and-voice-acting

Notes on what the sources do NOT establish: no named AAA studio was found
publishing Flux-family use in a production pipeline (documented Flux-derived
pipelines are vendor and freelancer work so far); quoted-text prompts,
end-of-prompt preserve-lists, and box-scoped edits instead of masks are the
pack's original workflow contributions, not documented studio conventions,
and are stated as such.

## Agent automation

1. **Drive the pack through the ComfyUI API, not the canvas.** Convert each
   workflow's JSON to a queue payload: blue-node values become a parameter
   dict, everything else stays fixed. POST the payload to
   `http://<host>:8188/prompt` and poll `/history` for the output image
   path. This turns "touch only the blue nodes, in order" (Phase 2) into an
   executable manifest instead of mouse discipline.
2. **Run batch rows as a seed sweep with an acceptance log.** For every
   "Prompt each" workflow, write one JSON job per row per seed
   (rows x 3 seeds), recording for each: workflow name, row prompt,
   quoted words, expected spelling, seed, output path, pass/fail with the
   failure mode quoted from the author ("wrong letter", "duplicate
   turnaround view", "logo lost its base", "blurry paw"). Failures go back
   into the queue with a new seed; the sweep stops when every row passes or
   the budget (set it before running) is spent.
3. **Verify rendered words automatically.** The pack's text workflows
   (Phases 7, 12, 20) make spelling the acceptance gate; an agent can OCR
   the output region (any OCR tool, or zoomed visual inspection) and
   compare the recognized string to the quoted target word list from the
   manifest before marking the row passed.
4. **Match the Moment Factory review ladder.** Generate review-size first,
   inspect, pick winners, then run only the winners through the Z-Image
   realism pass (Phase 5) at 0.2. Never generate full-size on a first
   prompt: the author's honest limits (hands, far faces, drift) are cheapest
   to find at review size.
5. **Keep the honest-limit checks machine-readable.** Add one check per
   author failure mode to the manifest schema: hand count vs. expected
   (visual count), face-size-in-frame for realism eligibility
   (faces too small = full-body warning, Phase 5), every word quoted in the
   prompt spelled in the output (Phase 12/20), center-frame pixels
   identical to the source after Outpaint Stitch (Phase 17). A workflow run
   is done only when all checks pass, not when an image appears.

## The human method, distilled

1. **Touch only the blue nodes, in order.** The color convention is the
   whole operating discipline of the pack.
2. **Describe like the model needs, not like a caption.** Long prompts:
   kind of photo, person, every hand's job, place, light. Quoted words
   for text. "What must stay" at the end of every edit.
3. **Boxes define scope.** Layout Boxes for composition, Sketch boxes
   for inpaint, word boxes for text. Box placement replaces masking.
4. **Strength is a dial, not a virtue.** 0.2 on the realism pass; higher
   drifts identity ("a higher number does not mean more realism").
5. **Seeds are the free variable.** Wrong letter, duplicate turnaround
   view, logo that lost its base — all fixed by another seed.
6. **Know the honest limits.** Hands need jobs; far faces fail; edits
   redraw everything small; combined scenes drift compositionally;
   restored faces are plausible, not archival; out-of-frame asks
   reframe the shot.

## Depth status

FULL — 658 ASR caption segments, 12 high-res frames reviewed (graph
layouts, before/after realism comparison, turnaround sheet, group-photo
graph), full description metadata with chapters. Workflow JSON files were
not downloaded; all parameters above come from the author's narration.

## P1/P2 gap relevance (for the scout run)

- **P1 AI-vendor acceptance spec (aegis intake/):** supporting evidence,
  not a fill. The pack documents a concrete vendor-prompt discipline
  ("give every hand one job", preserve-list endings, box-scoped edits,
  seed-as-repair) plus per-workflow "How to use" / "Nodes info" docs —
  the closest thing to a written "what good means" contract seen in a
  ComfyUI vendor pack this week.
- **Watchlist:** genuine reappearance of "FLUX 3 Image Klein" (2026-10-16
  row — this video is the deep workflow pack for the same model) and of
  "ComfyUI custom nodes wrapping intake/ stages" (Pixaroma 1.4.223 is a
  task-packaged node pack with free downloadable workflows, the same
  ecosystem pattern).
