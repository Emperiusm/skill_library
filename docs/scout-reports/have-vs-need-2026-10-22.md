# Video tooling scout: have-vs-need, 2026-10-22

Depth mode: **pre-approved** (max 2 media downloads). Depth-escalation usage:
1 download attempted, 1 succeeded (FLUX 3 Klein Ep39 tutorial, YouTube,
40.1 MB, high/720p). Second slot unused: the remaining three videos were
native Reddit clips, whose tooling signal lives in post text and comments
per the skill (nothing to deepen by downloading a showcase clip).

Scan: 4 video posts across 18 subreddits (2026-10-20 to 2026-10-22),
min_score 20. Coverage is PARTIAL this run: gameassets, proceduralgeneration,
vfx, Simulated, and 3Dmodeling all returned HTTP 429 from Arctic Shift and
were not scanned. The remaining 13 subreddits returned data. Note (repeated
from 2026-10-21): the memory note says the scan list grew to 23 subreddits on
2026-10-20, but `subreddits.yaml` still lists 18 (threejs, GraphicsProgramming,
shaders, VoxelGameDev, RealTimeVFX missing) — reconcile before the next run.

Analysis was parallelized: the godot post and the two blender posts were
deep-analyzed by worker agents (audits below); the YouTube video was
deepened locally (download + 12 frames + 658 ASR caption segments).

## Gap alerts

- **P1 AI-vendor acceptance spec (aegis intake/), new practice evidence:**
  Pixaroma's 19-workflow FLUX 3 Klein pack documents the closest thing to a
  written "what good means" contract seen in a ComfyUI vendor pack this
  week: long-prompt discipline ("the more you describe, the less it has to
  guess"), per-hand jobs ("give every hand one job" fixed 2/4 -> 4/4 clean
  hands), "what must stay" preserve-list prompt endings (BFL's own
  convention), box-scoped edits (pixels outside the box guaranteed
  untouched), and seed-as-repair rules. It does not itself define intake's
  spec, but the six distilled rules are ready input for the fix artifact's
  prompt-contract appendix (see Gap recommendations).
- **Watchlist pattern, genuine reappearance:** Pixaroma 1.4.223 is a
  task-packaged ComfyUI node pack shipping 19 free downloadable workflows
  with version-gated setup (ComfyUI 0.41+) and color-coded node conventions
  (orange=load, blue=change-in-order, green=work, red=save) — the same
  vendor-ships-workflows pattern as the 2026-09-27 "ComfyUI custom nodes
  wrapping intake/ stages" row (minimax-h3-studio, RefMod, OmniChar). The
  ecosystem keeps proving the pattern; intake's automation should expect
  to consume vendor workflow packs, not build them.
- No matches today for the other P1 gaps (rig/retarget, perf budgets,
  import validation, mesh compression, mesh refinement, art bible,
  skyline fill, Godot import gate). The Geometry-Nodes billboard-line
  technique (video 2) is adjacent to 2d3d's P1 art-bible/toon-law gap as
  evidence input, not a fill.

## Videos deeply analyzed

| # | Video | Creator | URL | Duration | Source |
|---|-------|---------|-----|----------|--------|
| 1 | "Flux 3 Klein in ComfyUI \| Generate, Edit & Combine Images (Ep39)" | pixaroma (Reddit: pixaromadesign) | https://www.youtube.com/watch?v=ntxxhO9H3bY | 26:37 | r/comfyui post 1xauho2 (score 31, 9 comments). Depth: FULL (658 caption segments + 12 frames reviewed) |
| 2 | "Pen & Lines" | Scared_Newspaper8957 | https://www.reddit.com/r/blender/comments/1xc803d/pen_lines/ | n/a (native clip) | r/blender (score 32, 2 comments). Depth: DEPTH-LIMITED (one selftext sentence of technique; no node graph/params) |
| 3 | "I made a dubstep Gnome" | cole3d | https://www.reddit.com/r/blender/comments/1xc6j5c/i_made_a_dubstep_gnome/ | n/a (native clip) | r/blender (score 83, 8 comments unretrievable). Depth: DEPTH-LIMITED (selftext only; Arborea named) |
| 4 | "An early mockup for an RPG menu system" | GarsonGames | https://www.reddit.com/r/godot/comments/1xc6qje/an_early_mockup_for_an_rpg_menu_system/ | n/a (native clip) | r/godot (score 40, 9 comments). Depth: NO-TOOLING (UI design showcase) |

## 1. "Flux 3 Klein in ComfyUI | Generate, Edit & Combine Images (Ep39)" (pixaroma)

Source: https://www.youtube.com/watch?v=ntxxhO9H3bY | 26:37 | r/comfyui post 1xauho2 (score 31)

Tools used: ComfyUI 0.41+, Pixaroma custom nodes 1.4.223+, FLUX 3 Klein
model files (Black Forest Labs; three files: model / text encoder / VAE —
take the checkpoint **without "base" in its name**, the fast/distilled
version), Z-Image Turbo (+ its text encoder + VAE + an upscale model, for
the realism pass only), BFL prompt upsampler (one file), FLUX 3 outpaint
LoRA (one file). License: paid work OK while yearly revenue is under
$5 million. HF repo needs a one-time free approval.

This audit reconstructs the pack from the full ASR transcript and 12
frames, so another agent can run the same workflows. Every phase has Do /
Check / Why. The video's core method is: one model file set does three
jobs (generate, edit, combine); the pack standardizes node roles by color;
long disciplined prompts and box-scoped edits replace masking pipelines.

### Phase 1: Setup and the node color convention

**Do**
1. Confirm ComfyUI ≥ 0.41 and Pixaroma ≥ 1.4.223 (version-check node on
   the canvas). Get the HF approval once, download the three files
   (model → `diffusion models/Flux 3`, encoder → `text encoders`, VAE →
   `vae`), restart ComfyUI or press R.
2. Add the episode-39 workflows folder; every workflow follows the color
   convention: **orange** loads models, **blue** (numbered in order) are
   the only nodes you change, **green** does the work, **red** saves.
   Outputs land in ComfyUI's output folder, one subfolder per workflow.

**Check**
- Frame evidence: every workflow graph in the video follows the coloring
  (frames 006, 010); outputs in per-workflow folders (e.g. `flux 3 Klein
  realism`, `flux 3 Klein layout`).

**Why**
Version gating is explicit (the pack won't work on older installs); the
color convention makes 19 graphs skimmable — you only ever touch the
numbered blue nodes, in order. (Inference: this is also what makes the
pack automation-friendly — the human-input surface is labeled and
ordered.)

### Phase 2: Prompt discipline (applies to every workflow)

**Do**
1. Write long, detailed prompts: kind of photo, person, **what each hand
   does**, place, light. "The more you describe, the less it has to
   guess."
2. Put words that must appear in the image in **double quotes**.
3. For edits/combines, end the prompt with **what must stay** — BFL's
   own convention (face, hair, clothes, pose, jewelry).

**Check**
- Short-prompt control: the same idea in one short line produced a
  different woman, a plain building, the word on a white sticker, and a
  broken hand.
- Hands: 2 of 4 clean with a short prompt → all 4 right after describing
  the gesture and giving every hand one job.

**Why**
The pack's failure modes are mostly short-prompt failures, not model
limits: soft plastic-looking faces (fix: 2K or the realism pass; keep
people close), the "AI look" of warm glow + blurry background + perfect
skin (fix: say where the light comes from and what kind of photo it is),
and text errors (fix: bold capitals, quoted words, check every word;
a wrong letter usually goes away with another seed).

### Phase 3: The 19 workflows (generate 6, edit 8, combine 5)

**Generate:**
1. **Text to image** — prompt (Phase 2), size (portrait/landscape),
   seed: F keeps the same picture, R makes a new one every run. ~4 s
   after the first run on the author's card. Same prompt + same seed +
   landscape = the same wide photo.
2. **+ Z-Image realism pass** — needs Z-Image Turbo, its text encoder,
   its VAE, and an upscale model. Light extra pass at 2× size; step 4
   sets the denoise strength: start at **0.2**. ~20 s. Check: pose and
   text unchanged, skin a little more real, eyes/hair sharper. "A higher
   number does not mean more realism" — at 0.5 the face became a
   different face (brown eyes, fewer freckles, older). Best on
   portraits/half-body where the face is big.
3. **+ Prompt upsampler** — one new file (BFL's, trained to write
   prompts the way Flux 3 likes them). Step 1: a line or two ("polished
   CG animation still"); the upsampler writes the full prompt in ~4 s;
   step 4 toggles AI prompt vs "as typed". "Magical" filled the scene
   with glowing mushrooms and sparkles — use calm words for simple
   pictures. RTX 30 CUDA error: restart ComfyUI, turn off "faster
   writing" in the AI prompt gear.
4. **Text in images (labels)** — find-and-replace boxes: big name row 1,
   small line row 2; placeholders in double quotes in the prompt with
   the letter style ("Pix-O-Roma" / "wildflower honey" on a jar; then
   "lavender honey", jar unchanged). Capital letters best; wrong letter
   → new seed.
5. **Layout Boxes** — new Pixaroma node: a small canvas shaped like the
   picture; each box is one object with a number + short description
   (or a text box for words in the image). Click/drag to resize/move,
   draw on empty spots, undo. Step 3 names boxes by number tag. 4/4
   seeds correct in the author's tests. (ComfyUI's own box node is
   Nodes 2.0 only; Layout Boxes works in both.)
6. **Image to prompt to image** — load a picture you like; the AI
   writes the prompt (same upsampler file); "as it is" copies (close,
   not exact — pose and details change) or "plus my extra instructions"
   adds a change (same bunny, now in snow with a red scarf).

**Edit:**
7. **Image edit** — write the change as an instruction, end with what
   must stay (~6 s). A new place is easier than new light (the street
   was sunny, the light on her stayed studio-soft); the whole picture
   is redrawn, so small details can shift.
8. **Box edit** — Sketch box around what changes (make the box the size
   of the new thing); Inpaint Crop cuts the box, Flux 3 changes only
   that piece, Inpaint Stitch pastes it back. Box an empty spot to add
   something new. Seam color shift → raise stitch softness, try color
   match, or new seed.
9. **Text edit** — old word and new word in double quotes ("Change the
   word love to Pixar in the same glossy orange balloon letters at the
   same size and in the same place"). "The spelling was right every
   time, but the size can change a little."
10. **Restyle** — Prompt-each rows, one style per row; rows say what the
    style is made of (brush strokes, flat shading) and end with what
    stays. "Ask to keep her likeness, not her face. Keeping her face
    exactly gives you a photo with a filter." One run, ~5 s each.
11. **Season / time of day (relight)** — rows say what the new light
    does to everything (where snow lands, which lights glow, what
    happens to the furniture); "keep the furniture unchanged" alone left
    the armchair in daylight under the moon. ~16 s for three.
12. **Restore + colorize** — say what to fix (scratches, dust, crease,
    stain), then name a color for every clothing item and the place
    ("natural colors" alone came out pale every time). Honest note: the
    faces are "a likely version of the people, not the real ones" —
    compare with the original before sharing.
13. **Character sheets** — tag "ref image 0" = your character; wide size
    so views fit side by side; ~13 s for both sheets (turnaround +
    six expressions). Expression sheet right on every seed; turnaround
    sometimes gives two front views → try seeds.
14. **Outpaint** — adds a small outpaint LoRA; keep step 3's first
    sentence (the LoRA's instruction), describe the scene after "scene";
    ~7 s. Outpaint Stitch puts the original back in the middle — "in my
    tests, the join was invisible, even at full size."

**Combine:**
15. **Character in a scene** — ref image 0 = character, ref image 1 =
    place ("place the bunny explorer from ref image 0 in the room from
    ref image 1"); every paw gets a job ("Just waving at the camera gave
    a blurry paw that melted into the wall"). Picture 1 sets the output
    shape; the room is similar but not identical (camera moved closer).
16. **Outfit change** — describe the print in words; keep face/hair/
    background. Change only what the photo shows: asking for sneakers
    on a thigh-up photo reframed the whole shot to show his feet.
17. **Logo on a product** — logo best on a plain background; prompt says
    where, color, size. "The logo kept its exact shape every time"; size
    words steer only loosely → try seeds until one fits.
18. **Group photo (up to 10 refs)** — wire another Load Image Mini into
    the next free slot; stage like a photographer (one row, same floor,
    nobody in front, state sizes for non-adults, arms around backs,
    every hand a job). ~19 s for four; still struggles with hands and
    eyes up close.
19. **Product ad** — picture 1 = the place, kept FIRST ("with the mug
    first, Flux 3 made up its own room every time"); ask for the
    framing ("The camera moves in close...") or the mug comes out tiny;
    check the logo at full size (sometimes loses its curved base).

### The human method, distilled

1. Touch only the blue nodes, in order.
2. Describe like the model needs, not like a caption: long prompts,
   hand jobs, quoted words, "what must stay" endings.
3. Boxes define scope: Layout Boxes for composition, Sketch boxes for
   inpaint, word boxes for text. Box placement replaces masking.
4. Strength is a dial, not a virtue: 0.2 on the realism pass; higher
   drifts identity.
5. Seeds are the free variable: wrong letter, duplicate turnaround view,
   logo that lost its base — all fixed by another seed.
6. Know the honest limits: hands need jobs; far faces fail; edits redraw
   everything small; combined scenes drift compositionally; restored
   faces are plausible, not archival; out-of-frame asks reframe the
   shot.

**Depth status:** FULL (658 caption segments, 12 frames reviewed —
graph layouts, before/after realism comparison, turnaround sheet,
group-photo graph — full description metadata with chapters; the workflow
JSON files were not downloaded).

## 2. "Pen & Lines" (Scared_Newspaper8957) — DEPTH-LIMITED

r/blender post 1xc803d (score 32): "i used geometry nodes to make sure
lines always face up and stay flat" (verbatim). 2 comments, both praise.
Technique: yaw-only camera-facing billboard in Blender Geometry Nodes so
pen-style lines keep constant width and stay flat/upright from every
camera angle (no free-billboard roll or edge-on collapse). No node
graph, parameters, or render settings were disclosed; all node-level
detail is labeled inference and the post is not reconstructible from
evidence alone. A media download would add clip frames, not workflow.
Stays in the report; no skill.

## 3. "I made a dubstep Gnome" (cole3d) — DEPTH-LIMITED

r/blender post 1xc6j5c (score 83): gnome + architectural environment
pieces hand-modeled in Blender ("Gnome I Made! Modeled and gnome and
architectural parts of the environment"), trees and foliage from
**Arborea by Sweeper3D** ("Used arborea for the trees and such!",
verbatim). All 8 comments unrecoverable (Arctic Shift 422, old-reddit
302 bot-wall, PullPush 429 even after backoff); animation, rigging,
render, and edit steps undisclosed. Arborea (product facts from
Sweeper3D's own pages): paid Blender nature kit, nearly 800 ready-to-use
assets via docked/popup asset browser, Summer/Autumn/Winter + variation
toggles without re-import, material sliders (color, season, one-click
trunk moss), wind animation presets, GeoNodes vine/ivy/snow generators +
scatter system (one-click scatter from the browser), Blender 4.2+,
Cycles/Eevee. First Blender-native environment-kit row (the TreeSculpt
row is Unity Asset Store). Stays in the report; no skill.

## 4. "An early mockup for an RPG menu system" (GarsonGames) — NO-TOOLING

r/godot post 1xc6qje (score 40): UI mockup showcase on a strict 640×360
canvas. No external tool, plugin, script, or pipeline stage named or
demonstrated beyond Godot's built-in nodes. The only method detail
disclosed (from comments): pencil-and-paper layout references, then
MarginContainers for automatic spacing "as much as possible," manual
part-by-part tweaking, and tween animations ("sometimes just trial and
error"). No extractable tooling workflow; no watchlist additions; no gap
matches. Stays in the report; no skill.

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Model-swappable image backend for intake/ | FLUX 3 Klein pack (video 1) | PARTIAL | intake/ does concept-to-input generation but no model is pinned; no written AI-vendor acceptance spec (P1 gap) | Backlog: evaluate FLUX 3 Klein + Pixaroma pack (paid-work OK under $5M revenue; text rendering; restoration; outpaint) as intake's model-swappable image backend alongside MOSS-Image (2026-10-21) |
| Prompt-discipline / preserve-list contract | FLUX 3 Klein pack (video 1) | NEED | No written AI-vendor acceptance spec (P1 gap) | Gap recommendation #1: feed the six distilled rules (hand jobs, quoted words, preserve lists, box scope, seed-repair, strength dials) into the gap-fix artifact as a prompt-contract appendix |
| Box-scoped pixel-preserving edit | Inpaint Crop + Stitch (video 1) | NEED | trellis-pipe has weld/qa/lods/uv/bake but no edit-acceptance semantics | Backlog: the pixel-exact-outside-box and original-restored-into-center patterns are testable acceptance criteria |
| ComfyUI automation surface | Pack color conventions (video 1) | NEED | No evidence intake/ uses ComfyUI; native-loop recursion bug still unmerged (2026-10-21) | Watch: numbered-blue-input-node convention is a machine-readable contract; the 0.36 loop bug still applies to any loop automation |
| Line-art / toon rendering stage | Billboard lines (video 2) | NEED | No toon line stage in trellis-pipe | Skip: no foundry attach point; evidence input only |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Free/open image backend for image_client.py | FLUX 3 Klein pack (video 1) | PARTIAL | pipeline/image_client.py fail-closed spend gate, $0.00 spent, OpenAI no credit (beads 9le.25) | Backlog: FLUX 3 Klein is a second $0 candidate next to MOSS-Image; commercial OK under $5M; character-sheet + restore workflows suit the hawk/boar art need; evaluate against procedural stand-ins |
| Toon-law evidence (2d3d P1 art-bible gap, rec 2) | Billboard flat lines (video 2) | NEED | No written art bible per inventory | Watch: yaw-only billboard = a named toon-line rule for the art bible's toon law section |
| Blender-native environment kit | Arborea (video 3) | NEED | pipeline/proc are seeded code generators; no purchased asset kits in pipeline | Watch: Arborea as the benchmark environment-dressing option vs. procedural trees; only relevant if environment work grows |
| P1 import-validation gap (rec 9) | — | NEED (unchanged) | qa/asset_validate.py still absent per inventory | No tool today fills it |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Environment dressing kit benchmark | Arborea (video 3) | NEED | tools/city_trees.py + procedural_art.py are code-authored; no external nature kits | Watch: first Blender-native nature kit benchmark; tree/scatter art-direction pattern (placement/variation/season, not branch geometry) is transferable thinking |
| Layout-composition control for generated art | Layout Boxes (video 1) | NEED | AI inputs optional (openai_key.py, tripo_key.py) | Watch: bounding-box compositional control pattern for any generated sprite/concept work |
| P1 shader skyline fill | — | NEED (unchanged) | No equivalent per inventory | No tool today fills it |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Text-rendering image model for concept/marking art | FLUX 3 Klein pack (video 1) | PARTIAL | Concept PNG is visual authority (colour, markings, faction identity); no AI-vendor acceptance spec beyond that | Backlog: FLUX 3 Klein's legible text + layout-JSON-adjacent box control suits faction markings/labels on concept art; pairs with MOSS-Image (2026-10-21) |
| P1 Godot import validation gate | — | NEED (unchanged) | Nothing to validate into yet per inventory | No tool today fills it |

## Watchlist trending

## Watchlist trending
- Flux klein 9B/4B distilled variants + CCTech/Flux Klein ComfyUI node pack (first seen 2026-10-05, status WATCH; seen again 2026-10-16, 2026-10-17, 2026-10-21, 2026-10-22) **TRENDING**
- FLUX 3 Image Klein (5.6B, Black Forest Labs, native ComfyUI) (first seen 2026-10-16, status WATCH; seen again 2026-10-17, 2026-10-21, 2026-10-22) **TRENDING**
- OmniChar/.char portable character format + ComfyUI-Omnichar node pack (first seen 2026-10-05, status BACKLOGGED; seen again 2026-10-08, 2026-10-09, 2026-10-16, 2026-10-21, 2026-10-22) **TRENDING**
- Blender Geometry Nodes flower motion-design setup (first seen 2026-10-15, status WATCH; seen again 2026-10-22)

Accuracy review of the auto-matches (annotated in
`references/tooling-watchlist.md` per the established convention): 3 of
the 4 "seen again 2026-10-22" hits are token overlap, not genuine
reappearances (Flux klein row: overlap on "Flux Klein" for the FLUX 3
family video; OmniChar row: overlap on "character"/"ComfyUI";
GeoNodes-flower row: overlap on "Blender"/"Geometry Nodes" for a
different technique). Only "FLUX 3 Image Klein" is genuine — today's
video is the 19-workflow ComfyUI pack for the same model (FULL audit).
Manual addition: "ComfyUI custom nodes wrapping intake/ stages"
(2026-09-27 row) is a genuine reappearance — Pixaroma 1.4.223 is a
task-packaged node pack with 19 free workflows, continuing the pattern.

New watchlist additions (genuinely new tools/stages):
- Pixaroma FLUX 3 Klein 19-workflow pack (ComfyUI 0.41+, Pixaroma
  1.4.223+) — WATCH
- Z-Image Turbo realism pass (0.2 denoise sweet spot; needs text encoder
  + VAE + upscale model) — WATCH
- BFL prompt upsampler (long-prompt writer for Flux 3; "as typed" toggle;
  RTX 30 CUDA workaround) — WATCH
- Layout Boxes node (Pixaroma bounding-box composition) — WATCH
- Arborea by Sweeper3D (paid Blender nature kit, ~800 assets) — WATCH
- Geometry Nodes upright-billboard flat-line technique (Blender) — WATCH

## Gap recommendations (highest-leverage NEEDs)

1. **Feed the FLUX 3 Klein prompt-discipline rules into the P1
   acceptance-spec fix.** The six distilled rules (describe every hand,
   quote text words, end edits with "what must stay", box-scope edits,
   seed-as-repair, strength-is-a-dial) are the closest thing to a written
   vendor contract seen this week. Concrete next step: append them as a
   prompt-contract appendix to `~/workspace/your_files/gap-fixes/aegis-intake/`
   (fix artifact prepared 2026-10-21, thresholds still CALIBRATE).
2. **Evaluate FLUX 3 Klein as the $0 image backend for 2d3d's
   image_client.py and Aegis intake/.** Paid-work OK under $5M revenue,
   text rendering, restore/colorize, outpaint, character sheets —
   alongside MOSS-Image from 2026-10-21. Concrete next step: run the
   character-sheet and restore workflows against the procedural stand-ins
   (2d3d beads 9le.25).
3. **Adopt the box-scoped edit and outpaint-stitch guarantees as
   acceptance-criteria patterns.** Pixels outside the box exactly
   untouched; the original restored into the center after outpainting —
   both are machine-testable.
4. **Keep Arborea as the Blender-native environment-kit benchmark.**
   Relevant to Desktop City's tree/scatter reference work and any future
   2d3d environment dressing; the art-direction-is-placement-not-geometry
   principle transfers to procedural tree tooling.
5. **Log the yaw-only billboard line technique for 2d3d's art bible.**
   Input to the toon-law section of the P1 art-bible gap (rec 2).

## Explicit non-goals

- The 5 rate-limited subreddits (gameassets, proceduralgeneration, vfx,
  Simulated, 3Dmodeling): coverage gap, not a skip decision — their
  videos were never seen, so no downweight judgment applies.
- GarsonGames' RPG menu mockup: UI design showcase; no tooling signal.
- FLUX 3 Klein for Godot repos (2d3d, Desktop City, Solarempire):
  workflow runs in ComfyUI, not in-engine; its value there is as an
  image source, evaluated per the tables above.

## skill_library artifacts staged

- New skill `skills/ai-video/flux-3-klein-comfyui-19-workflows/` (FULL audit,
  22 phases + distilled method)
- Full report staged at `docs/scout-reports/have-vs-need-2026-10-22.md`
- Watchlist rows synced to the repo mirror's
  `video-tooling-scout/references/tooling-watchlist.md`
- README tables updated (skills/README.md grouped table, root README counts)

## Run notes / infra

- 5 subreddits 429'd this run (gameassets, proceduralgeneration, vfx,
  Simulated, 3Dmodeling); partial coverage noted above. Same host-prompt
  guard applies to Arctic Shift if it recurs.
- Comment fetch: Arctic Shift 422 on the dubstep-gnome post; old-reddit
  302 bot-wall; PullPush 429 persisting after backoff — 8 comments
  unrecoverable. Pen & Lines and godot comments fetched fine via Arctic
  Shift (2 and 9 comments).
- The sandbox venv for the video-summarizer skill is broken
  (`.venv/bin/yt-dlp` missing); worked around with a shim at `~/bin/yt-dlp`
  (exec /usr/bin/python3 -m yt_dlp) since the system python has yt-dlp
  2026.08.19 installed. The YouTube download succeeded with no approval
  gate firing (android client; high/720p, 40.1 MB). Durable fix worth
  considering: repair the skill's venv or document the shim in the
  skill's LOCAL_SETUP.
- Whisper local transcription remains a local-machine step per the skill
  (never attempted in the sandbox; model download forbidden).
- subreddits.yaml still lists 18 subreddits vs. the 23 claimed in the
  2026-10-20 memory note (threejs, GraphicsProgramming, shaders,
  VoxelGameDev, RealTimeVFX missing). Reconcile before the next run.
