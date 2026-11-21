# Video tooling scout: have-vs-need, 2026-11-21

Run: daily scout, 2-day Reddit window (2026-11-19 to 2026-11-21) plus a
14-day YouTube channel window. Depth mode: `pre-approved` (max 2 media
downloads). Report kept in the goal workspace (the old
`~/workspace/your_files/video-tooling-scout/` path is stale per goal context);
the public copy is published to `docs/scout-reports/` in skill_library.

## Gap alerts

No P1 gap is fully filled today. Four near-hits, all labeled as near-hits,
not fills:

1. **P1 rigging / skinning / retarget (aegis) and 2d3d production
   conversion: a face rig exists in the wild, but it is a shader trick
   with no method.** The Adventure Time face rig plugin (audit #2) makes
   an animatable face whose "art itself is a shader so no pre made assets
   or something". No rigging method, skeleton, skinning weight, or
   retarget step is disclosed, and the itch page timed out on fetch. It
   is evidence that solo devs paper over the rig gap with shader faces,
   not evidence the gap is solved. The prepared fix route (Tripo P2.0 /
   Mixamo) stands.
2. **P1 written art bible (2d3d): the stylized-shader devlog is a
   complete look-dev spec in miniature.** "Before implementing any
   shaders, one of the most essential aspects of achieving a convincing
   stylized 3D aesthetic is making the right textures. Shaders alone
   cannot establish a cohesive art style." Four lighting components
   (base, shadows, ambient occlusion, highlights), modified mesh
   normals for faces, adjustable shadow softness, AO painted into the
   diffuse, specular plus rim, glowing-iris emission. That is the
   shape a 2d3d art bible entry should take: textures first, then the
   shader, with the decisions written down. It is Godot/anime-specific,
   so it is a pattern to adapt, not a bible to copy.
3. **P1 AI-vendor acceptance spec (aegis intake): the Nano Banana
   overlay check is the only verified acceptance step in today's
   AI-texture workflow.** The author flips between the generated base
   color and each derived map and checks they are "literally perfectly
   overlaid on top of each other" with no repositioning. That check is
   real and cheap. The same video's claim that the maps are
   "mathematically accurate" is the creator's claim only, unverified,
   and must not be adopted as a fact. The acceptance-spec gap stands;
   the overlay check is a candidate step inside it.
4. **P2 MCP-driven DCC loop (aegis): Meltbelt is agent-written, but
   not MCP-driven, and the loop is undisclosed.** "All of the code,
   shaders, textures, etc, is written by Opus 5.5 and a little Fable"
   in Godot with C++ for the liquid sim. The human's stated workflow
   is "playtest, write a list all the stuff" (truncated in the
   300-character snippet). No MCP, no DCC loop, no prompt or review
   step is disclosed. It corroborates the Nov 20 age-of-sail finding
   that agent-written games are shipping with a playtest loop, not
   that the MCP route is the working answer.

## Depth-escalation usage

- Mode: `pre-approved`, allowance 2 downloads. Attempted 0, succeeded 0,
  skipped 0, approval gates hit 0.
- All four new YouTube candidates had full ASR captions, so no download
  was needed for any of them: MOSS (252 caption segments), Qwen-Image-2.1
  (244), Nano Banana texture maps (412), glitch render (523). Captions
  plus descriptions carry every audit below except #1 and #2, which are
  native Reddit videos.
- No Whisper transcription was attempted (sandbox cannot fetch model
  weights; per skill, that is a local-machine step, never attempted here).
  No model files were downloaded.

## Videos scanned

- Reddit: 32 video posts listed across 23 subreddits, 2-day window.
  Arctic Shift returned HTTP 429 for **comfyui** on the scan pass, so
  that sub's posts are missing from this scan. PullPush returned HTTP
  429 when full post text was requested for the top posts, so audits
  #1 and #2 rest on the scan's 300-character snippets plus comments.
  A text fetch of the Meltbelt Reddit page was blocked by policy
  (`reddit.com` blocked for `browser.open`); the itch page for the
  face-rig plugin timed out. Both recoveries would have required the
  live browser, which this loop forbids, so neither was attempted and
  both gaps are recorded here.
- YouTube: 11 configured channels, 14-day window. First pass: all 11
  failed with SSL CERTIFICATE_VERIFY_FAILED. The egress CA was appended
  to the correct venv bundle
  (`~/workspace/skills/video-summarizer/.venv`, certifi `cacert.pem`,
  176 to 177 certificates) and the re-scan recovered: **13 videos
  found, 0 warnings**. The CA bundle had lost the previously appended
  CA; the skill's CA note should name the `skills/video-summarizer`
  venv explicitly, as in the 2026-11-20 run notes.
- Deep-analyzed (8): Meltbelt, Adventure Time face rig plugin, Stylized
  Character Shader, gitbonsai, MOSS Image int8 + upscale, Nano Banana
  PBR texture maps, glitch render in Blender 5.3, Qwen-Image-2.1
  (re-scan, already audited 2026-11-17, not re-audited).
- Re-scanned, already audited 2026-11-20 (not re-audited): Gingerbread
  House Parts 5, 6 and 7, Darth Maul in Blender, MiniMax H3-Image GGUF
  guide. The Qwen-Image-2.1 video is the same video ID already made
  into a skill on 2026-11-17; today's scan is a re-scan of that video,
  not a new workflow.
- Not deep-analyzed (thin or no workflow in the retrieved text):
  Tony Hawk pixel low-poly hybrid (score 49, relevance 21.0; comments
  are praise only, no method), wurq8 procedural trees/water (one
  substantive comment, no parameters), Blender VFX Breakdown: Battle
  of Fort McHenry (breakdown claim, comments are historical-research
  discussion, no workflow), cloud-Blender game cinematic (agent-built
  scene claim; a commenter says it duplicates an earlier train scene
  by Kamome Ashizawa and asks for sourcing), Blender parody (score
  1,135, zero tooling signal), next-generation Godot simulation
  (score 470, no post text retrieved), 3D-printing showcase and
  speedsculpt (showcase only), Grokbot IDEAS and Imagination Studio
  (YouTube, not summarized; no workflow in the description snippets),
  3D Emojis in Blender (YouTube, 57 minutes, project files for sale;
  not summarized), Rendering Really Is This Simple (YouTube, course
  pitch in the description; not summarized).

## 1. "A mining game where everything actually melts (waifu included)" (Professional_Job_307)

Source: https://www.reddit.com/r/aigamedev/comments/1y1u0jv/a_mining_game_where_everything_actually_melts/ (score 102, 14 comments, 0 retrieved) | https://v.redd.it/rseiinwitx2i1

Tools used: Godot, C++ (liquid sim and heat mechanics), Claude Opus 5.5, "a little Fable".

This audit reconstructs the workflow from the 300-character scan snippet
only, step by step, so another agent can follow what is actually
disclosed. Every phase has three parts: **Do** (the action), **Check**
(how the human verifies it), and **Why** (the principle). The video's
core method is: melt asteroids with a laser, sort the molten metal with
a tractor beam, and let the agent write the code while the human
playtests. Evidence beyond the snippet was not retrievable this run.

### Phase 1: Melt and sort, in Godot with a C++ sim

**Do**
1. Build the game in Godot. Put the liquid simulation and the heat
   mechanics in C++, not GDScript.
2. The loop, as stated: "you melt asteroids with a laser and sort the
   molten metal with a tractor beam."

**Check**
- *Inference:* the snippet names the two sim systems (liquid, heat)
  and the two verbs (melt, sort) but no class, node, parameter, or
  performance number. Nothing in the retrieved text lets a reader
  verify the sim.

**Why**
A liquid/heat sim is the game's central system, so it lives in C++
while the rest of the game lives in Godot. That split is the only
architectural decision disclosed.

### Phase 2: Let Opus 5.5 write everything, playtest, write a list

**Do**
1. "All of the code, shaders, textures, etc, is written by Opus 5.5
   and a little Fable."
2. "My workflow is playtest, write a list all the stuff" (snippet ends
   mid-sentence; the rest of the sentence was not retrieved).

**Check**
- No comment evidence: Arctic Shift returned zero comments for a post
  reporting 14, and the old-Reddit/PullPush fallbacks also returned
  nothing. The playtest-list step cannot be verified beyond the
  author's own truncated sentence.

**Why**
*Inference:* the pattern matches the Nov 20 age-of-sail loop
(playtest, hand the transcript/notes to the agents), but the Meltbelt
post does not disclose a transcript, a harness, or a review step, so
the match is a hypothesis, not evidence. The loop as disclosed is
playtest, then write a list. What happens to the list is undisclosed.

### The human method, distilled
1. Agent writes the code, shaders, and textures; the human playtests.
2. Playtest findings become a written list. (What the list feeds, and
   how it is reviewed, is not disclosed.)
3. The sim systems that define the game are C++; everything else is
   Godot.

**Depth status:** DEPTH-LIMITED (300-character snippet only; 0 of 14
comments retrievable; full post text blocked by the PullPush 429 and
the Reddit text-fetch policy block. A media download would add only
the clip's visuals, not the method, so no download was spent here.)

## 2. "I made an adventure time face rig plugin for my hobby video game !!" (MOHGAM_YT)

Source: https://www.reddit.com/r/godot/comments/1y1j53j/i_made_an_adventure_time_face_rig_plugin_for_my/ (score 51, 2 comments, 2 retrieved) | https://v.redd.it/mqf2tclfyu2i1 | Plugin: https://mohgam.itch.io/adventure-time-style-face-rig-plugin-godot

Tools used: Godot (plugin), a shader (the face art itself). No rigging
tool, node, or parameter is disclosed.

This audit reconstructs what is disclosed, step by step. Every phase has
three parts: **Do**, **Check**, and **Why**. The video's core method is:
the face is a shader, not pre-made assets, and it can be animated.

### Phase 1: Build the face as a shader, not as assets

**Do**
1. Make the face rig as a Godot plugin.
2. Make "the art itself is a shader so no pre made assets or something".

**Check**
- The author states the shader claim directly in the post. No shader
  code, node setup, or parameter is disclosed, so the claim cannot be
  checked further from the retrieved text.

**Why**
A shader face needs no pre-made face assets: the expression lives in
the shader, so the same face can be animated without swapping art.

### Phase 2: Leave the hard parts in work, ship the plugin anyway

**Do**
1. "There is still work to do on the facial hair style and smile
   curve, but overall it's looking good for now, it can be animated
   too."
2. Offer the plugin to Ko-fi members: the author links
   https://mohgam.itch.io/adventure-time-style-face-rig-plugin-godot
   in a comment. (A text fetch of that page timed out; its contents
   are unverified.)

**Check**
- A commenter (P_S_Lumapac) would rather buy it on itch "so it's in
  one place with others I bought". No commenter reports using it.

**Why**
*Inference:* shipping a plugin with named unfinished parts (facial
hair, smile curve) is the solo-dev pattern in this run: the rig is
good enough to show and share, and the unfinished list is stated
up front rather than hidden.

### The human method, distilled
1. Shader first: the face is code, not assets.
2. Name the unfinished parts in the post itself.
3. Share through Ko-fi/itch, not through a repo or a tutorial.

**Depth status:** DEPTH-LIMITED (post snippet plus 2 comments; no rig
method, shader code, node, or parameter disclosed; itch page
unretrieved. A media download would add only the clip's visuals, not
the rig method. No skill: no extractable workflow.)

## 3. "Showcasing my Stylized Character Shader" (Fiery_Griffin / FancifulCrow)

Source: https://www.reddit.com/r/godot/comments/1y11lmi/showcasing_my_stylized_character_shader/ (score 190, 43 comments, 25 retrieved) | https://v.redd.it/51hwnmin8r2i1 | Devlog: https://fancifulcrow.itch.io/charactershader/devlog/1791600/recreating-the-anime-look-in-godot (published 2026-11-20)

Tools used: Godot 4, a spatial shader, hand-painted textures
(Photoshop, Blender, Substance 3D Painter named as the texture tools),
Wiggle Bone addon for Godot 4 and Wiggle Bones for Blender (named in a
comment, for secondary motion, not implemented in the shader).

This audit reconstructs the exact workflow from the author's devlog,
step by step, so another agent can follow the same process. Every phase
has three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The video's core method is: paint the
textures first, then simplify the light into four controllable
components instead of simulating it physically.

### Phase 1: Paint the textures before writing any shader

**Do**
1. Hand-paint the diffuse maps. The author: "we have to resort to the
   good old, grueling process of hand-painting our textures."
2. Use Photoshop, Blender, or Substance 3D Painter to make and
   manipulate the diffuse maps.
3. Break realism deliberately: "rough painterly brushstrokes,
   simplified color patterns, exaggerated details, and deliberate
   imperfections".

**Check**
- The texture, not the shader, is judged first: "Shaders alone cannot
  establish a cohesive art style. The underlying textures are what
  give our models much of their visual character."

**Why**
"Before implementing any shaders, one of the most essential aspects
of achieving a convincing stylized 3D aesthetic is making the right
textures." Photographs and scans cannot carry a stylized look; only
painted maps can break away from realism on purpose.

### Phase 2: Split the light into four components

**Do**
1. "Rather than aiming for physically accurate lighting, the goal is
   to simplify how light interacts with a character."
2. Break the lighting into four main components: Base, Shadows,
   Ambient Occlusion, Highlights.
3. Base: "the overall lit appearance of the model, with its base color
   responding to the color and intensity of the light illuminating it,
   before any stylized shadows or additional lighting effects are
   applied."

**Check**
- Each component is shown separately in the devlog (base only, then
  shadows, then AO, then specular, then rim). The reader can see what
  each layer adds.

**Why**
"When drawing an object, artists often simplify lighting into a
small number of discrete tonal values rather than relying on
continuous gradients. This gives them more control over the subject's
final appearance." Four components are the control surface; physical
accuracy is not the goal.

### Phase 3: Fix the normals, then control the shadow transition

**Do**
1. Modify the mesh normals: "physically accurate normals can produce
   undesirable shadow patterns, especially around the faces. So
   artists often modify the mesh normals to produce more visually
   appealing lighting to follow the intended art direction."
2. Keep control over the sharpness of the lit-to-shadow transition:
   "these transitions can be either sharp and well-defined or soft and
   gradual. Having control over this transition allows us to achieve
   different shading styles without having to modify the underlying
   geometry or normals."
3. Keep shadow softness as an adjustable parameter in the shader (the
   author confirms this in a comment reply, after a commenter argued
   harder shadow edges would suit the model's hard outlines).

**Check**
- The devlog shows bad normals vs good normals side by side, and the
  comment thread debates the shadow edges against the model's hard
  textures and outlines. The flicker a commenter reports ("the shadows
  seems to flicker a bit at some moments") is an open defect, not
  resolved in the retrieved comments.

**Why**
Normals are an art-direction input, not a physical fact: the face
must shade the way the drawing would shade it. A softness parameter
lets one shader serve styles that want hard edges and styles that
want soft ones, without touching geometry.

### Phase 4: Paint the occlusion in, do not simulate it

**Do**
1. Paint the dark regions directly into the diffuse texture: "it is
   better to paint these dark regions directly into the diffuse
   texture to preserve the intended character look."
2. The regions: "Under the arms, between folds of pleated skirts, the
   belly button" and anywhere light has the hardest time reaching.
3. Cite the reference: "Games such as Zenless Zone Zero make
   extensive use of painted shading and texture-based details."

**Check**
- The devlog image shows Remielle's hand-painted ambient occlusions
  on the model. The painted AO is visible in the texture, not
  computed at runtime.

**Why**
Simulated AO follows the geometry; painted AO follows the intended
look. For a stylized character the intended look wins, and painting
it in guarantees it survives every lighting change.

### Phase 5: Split the highlights, then consider quantizing the light

**Do**
1. Divide highlights into two categories: specular highlights and rim
   lighting. Specular: "these reflections do not need to follow
   physically accurate behaviour. Instead, we want to be able to
   adjust and paint them." Rim: "a bright highlight along the
   silhouette of an object. This helps separate a character from the
   background and prevents the model from appearing too flat"
   (Marvel Rivals cited for rim use).
2. Consider, but do not implement, a script that "quantizes the light
   direction on the meshes into discrete angular intervals. This way,
   objects would only receive light from specific directions, skipping
   certain lighting transitions that you might not want." (Author's
   comment reply; labeled as considered, not implemented.)

**Check**
- The devlog shows specular added, then rim added, as separate
  images. The quantization idea is stated as a considered approach in
  a comment, not as shipped behavior.

**Why**
*Inference:* splitting highlights gives two independent controls
(paintable specular, silhouette rim) instead of one physical
reflection model. Quantizing light direction would be the next
control: discrete directions instead of continuous ones, matching the
discrete-tonal-values principle from Phase 2.

### Phase 6: Finish with emission, SSS, and an optional outline

**Do**
1. Add emission to the irises: "many anime characters in media have
   slightly glowing irises, as they are usually a major focal point of
   the face. We can easily add an emission to our material to achieve
   the effect."
2. Experiment with subsurface scattering: "Even in stylized 3D
   artwork, a subtle amount of subsurface scattering can make a
   noticeable difference, though we should be careful not to overdo
   it."
3. "If you want to go even further, you could try adding an outline
   shader to give a more 2D look to characters."

**Check**
- The final render is the check: the iris glow, the subtle SSS, and
  the optional outline are finishing touches judged by eye, after the
  four lighting components are in place.

**Why**
Finishing touches go last because they depend on the lighting being
right: an iris glow on top of wrong shadows would not read as anime,
it would read as a light stuck to the face.

### The human method, distilled
1. Textures first: hand-painted maps carry the style; the shader
   cannot establish it alone.
2. Simplify light into four controllable components; do not simulate
   it physically.
3. Normals are art direction: modify them until the face shades the
   way the drawing would.
4. Paint occlusion in; do not compute what the look already decided.
5. Keep the controls adjustable (shadow softness) and the unbuilt
   ideas labeled (quantized light direction, considered only).
6. Secondary motion is someone else's addon: the author points to the
   Wiggle Bone addon for Godot 4 and to baking jiggle with Blender's
   Wiggle Bones, and says "I don't have any long-term plans to
   replicate their physics."

**Depth status:** FULL for the method (devlog text read in full plus
25 comments; tools, principles, and quoted decisions all disclosed).
Caveat: no shader code is published in the devlog, and the project
download link in the post snippet was truncated and is unverified, so
the shader itself cannot be reproduced from this audit alone.

## 4. "Growing a Japanese maple bonsai from 14 years of (simulated) GitHub activity" (DocDrivenDevelopment)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1y11eu6/growing_a_japanese_maple_bonsai_from_14_years_of/ (score 39, 5 comments, 5 retrieved) | https://v.redd.it/1lsmizk49r2i1 | Project: https://gitbonsai.dev/ | Action: StevenBtw/gitbonsai@v0.5.0

Tools used: gitbonsai (GitHub Action), animated SVG output, GitHub
Actions with the built-in token, a snapshot file for incremental runs.

This audit reconstructs the exact workflow from the project site and
the post, step by step, so another agent can follow the same process.
Every phase has three parts: **Do**, **Check**, and **Why**. The
video's core method is: nothing is ever erased; every year of public
activity stays visible in the tree, and the tree regrows itself every
week.

### Phase 1: Read a tree as a record, not as decoration

**Do**
1. Grow the tree from a GitHub account's public contribution history.
   The video in the post is 14 years of simulated activity, "one frame
   a month".
2. Assign meaning before drawing anything: "A newcomer starts as a
   sprout with seed leaves. The first language is the trunk, and the
   trunk" (post snippet, truncated there; the site completes the rule).
3. Apply the site's legend, part by part:
   - Trunk: "Your first language; it only grows."
   - Leaf color: "The language, on the Japanese maple palette."
   - Girth: "Every contribution ever, and your age."
   - Crown: "Your last three to six years, a sector per language with
     a real share of them."
   - Bleached deadwood: "A language you stopped using while you kept
     working; it dies in place and weathers over the years."
   - Bare tree: "A year without contributions: resting for the
     winter."
   - Pot: "Your longest streak." Moss: "Your current weekly streak."
   - Shape: "Your last three years mostly pick the shape; the tree
     eases from one into the next as your work changes" (Chokkan,
     formal upright, for steady work in one language; Moyogi,
     informal upright, for steady work with new languages arriving).

**Check**
- The site's worked examples are the check: 15 years of girth on
  @torvalds, a bare resting tree on @tj, a long streak's pot and moss
  on @steipete, three languages' leaves on @StevenBtw. A tree that
  cannot be read against the legend is not finished.

**Why**
"An animated SVG for a profile README. A newcomer is a thin sprout;
years of work make it short, thick and wide, the way a prize bonsai
is. Each language claims a strand of the trunk, and nothing is ever
erased." The tree is a record with a legend, not a generated picture:
every visual decision maps to one fact about the account.

### Phase 2: Install the weekly regrow in your own profile repo

**Do**
1. "Everything runs in your own profile repository (`you/you`) with
   GitHub's built-in token."
2. Save the workflow as `.github/workflows/bonsai.yml` in that repo.
   The workflow in full, from the site:
   - `name: bonsai`; `on: schedule: - cron: "17 6 * * 1"` (Mondays
     06:17 UTC, "the week just ended is complete") plus
     `workflow_dispatch` to run it once by hand; `permissions:
     contents: write`.
   - Job `bonsai`, `runs-on: ubuntu-latest`: `actions/checkout@v7`,
     then `uses: StevenBtw/gitbonsai@v0.5.0` with `output-dir:
     assets` (a `legend: left` option is shown commented out).
   - Commit step: set the git identity to `github-actions[bot]`,
     `git add` the light SVG, the dark SVG, and the snapshot outputs
     (`${{ steps.bonsai.outputs.light }}`, `.dark`, `.snapshot`),
     `git diff --cached --quiet || git commit -m "Grow bonsai"`,
     `git push`.
3. "Its last step commits the tree; without it a run is green but
   changes nothing."
4. "In the Actions tab, run `bonsai` by hand. After that it runs
   every Monday."
5. Paste the `<picture>` block where the tree should stand: a dark
   source (`assets/bonsai-dark.svg`, `prefers-color-scheme: dark`)
   and a light `<img>` (`assets/bonsai-light.svg`, width 600).

**Check**
- The commit step is the check: a green run that commits nothing is
  a silent failure, and the site names it. The snapshot is what makes
  the next run fetch only recent months, and what guarantees a change
  every week: "Each SVG records the week it was grown, so every run
  commits a change and GitHub never pauses the schedule."

**Why**
"It commits as github-actions[bot], never as you, so the tree doesn't
water itself." The bot identity keeps the record honest: the tree
records the account's work, and its own regrowth must not count as
work. The snapshot plus the week stamp keeps a scheduled workflow
alive: GitHub pauses schedules on repos with no activity, so a
workflow that sometimes commits nothing would eventually stop
running, and the tree would stop growing.

### Phase 3: Ship the shading, take the repotting note

**Do**
1. Spend the time on the shading: the author, asked whether the bark
   shading can be stolen, answers "I spend quite some time on the
   shading" and will "make sure to add a more realistic 'repotting'
   to the next update" after a commenter notes "The linear increasing
   pot is weird. It should be at the center of image and pot should
   be increased with steps."
2. Ship the time-lapse variant too: "I released a new version that
   does this 'reporting' each year in the spring or when a threshold
   is met. Time-lapse on https://gitbonsai.dev/ are also updated."

**Check**
- The comment thread is the check: a reader's pot criticism is
  accepted and turned into a named next update (realistic repotting),
  not argued with.

**Why**
*Inference:* the shading is the craft cost in a generated-artifact
project ("I spend way too much time on this, normally don't post my
projects"), and the pot is the one part where the growth metaphor
breaks (a pot does not grow linearly). Fixing the metaphor beats
defending the render.

### The human method, distilled
1. Nothing is ever erased: every language, pause, and streak stays
   in the tree.
2. A legend before a picture: every part of the tree maps to one
   fact, with worked examples.
3. The bot never waters itself: automation commits as the bot, and
   the snapshot guarantees the schedule stays alive.
4. Take the pot criticism: when the metaphor breaks, fix the
   metaphor.

**Depth status:** FULL (project site read in full, including the
complete workflow YAML and the legend; post snippet plus all 5
comments. The 14-year video is simulated activity, per the post
title, not a real account's history.)

## 5. "MOSS Image ROCKS! Fast, Uncensored & Under 6 GB - EASY Install Guide" (Olivio Sarikas)

Source: https://www.youtube.com/watch?v=amjhvE-h2kM | 10:32 (632 s) | 10,996 views | uploaded 2026-11-20 | Models + workflows: https://huggingface.co/Comfy-Org/MOSS-Image

Tools used: MOSS-Image (OpenMOSS, via Comfy-Org), ComfyUI, Ultimate SD
Upscaler (ComfyUI-Ultimate-SD-Upscale custom node), Get Image Size
(built-in ComfyUI node), prompt enhancer (in the official workflow).

This audit reconstructs the exact workflow from the full ASR captions
(252 segments) and the description, step by step, so another agent can
follow the same process. Every phase has three parts: **Do**, **Check**,
and **Why**. The video's core method is: use the quantized,
generation-optimized workflow at 1-2 megapixels, then upscale with
Ultimate SD Upscaler instead of generating at 16 megapixels like H3.
This is a new variant on the existing MOSS-Image skill (starter recipe
1024x1024, 50 steps, CFG 3, shift 5, Oct 21; tuned-fusion expansion Nov
18): same model, a different, low-VRAM workflow.

### Phase 1: Pick the optimized workflow, not the base workflow

**Do**
1. Go to the official Comfy-Org MOSS-Image page: "the structure where
   everything goes with different workflows" (diffusion model, text
   encoder, VAE under Files and versions).
2. Download the workflow and drag it into ComfyUI; ComfyUI names the
   missing models and the folders they belong in (red frame, Details,
   Issues). "Click on download and point it to that folder inside of
   the ComfyUI folder inside of the models folder."
3. Use the generation-optimized workflow, not the base text-to-image
   workflow: "the base uses a base model that has not been optimized
   and is better for image training. The other one up here uses the
   model that is better optimized for your purposes for image
   generation."
4. Download the quantized model the workflow names (the ASR renders
   its name as "the int eight con rot" plus "these two other models";
   the exact file names are in the workflow, not in the captions, so
   they are not quoted here) into the folders the workflow points to.
5. "Always update ComfyUI and of course update your graphics driver"
   before starting.

**Check**
- The workflow opens naming its own missing files. If ComfyUI does
  not complain about a missing model, the files are in the right
  folders.

**Why**
The workflow is the install instructions: dragging it in surfaces
exactly what is missing and where it goes, so there is nothing to
guess about folders. The base-vs-optimized choice matters because
the base checkpoint is for training, not for generation.

### Phase 2: Generate at 1-2 megapixels, with the prompt enhancer

**Do**
1. Write the prompt in the workflow, then click the prompt enhancer:
   "this will optimize the prompt for the use with Moss image.
   However, this will take some extra time."
2. Keep the resolution in the model's optimized band: "this model has
   been optimized for one to two megapixels. So unlike when 2.1 or
   MiniMax H3, this is not for 16 megapixels."
3. Use the recommended megapixel resolutions listed on the model page
   for the workflow you chose.

**Check**
- The generated image is judged at its native 1-2 MP size first,
  before upscaling: the author's portrait review praises the skin
  detail, round retinas, and soft lighting "already very good with
  the original image that is created without upscaling".

**Why**
Generating at the resolution the model was optimized for, then
upscaling, is cheaper and safer than asking a 1-2 MP model for 16 MP
directly. The prompt enhancer costs extra time per generation, so it
is a choice, not a default the author forces.

### Phase 3: Adapt the workflow for Ultimate SD Upscale

**Do**
1. Install the Ultimate SD Upscale node: ComfyUI Manager, Extensions,
   search "ultimate", install "ComfyUI ultimate SD upscale".
2. Double-click the canvas background, search for the Ultimate SD
   Upscale node, place it where it is needed. It needs several
   inputs, "including an upscale model", so add a Load Upscale Model
   node too. Use the author's list of favorite upscale models "for
   the different purposes, might that be design or a photo with skin
   details".
3. Wire the subgraph: click the subgraph icon, and on the right side
   "there is a gray dot for the outs". Connect the model, the VAE,
   the positive prompt, and the negative prompt to the subgraph
   outputs, rename them positive/negative carefully ("make sure that
   you write the right one here so that the right one is
   connected"), click the return button, and connect the outputs to
   the matching inputs outside.
4. Drive the upscale size from the image itself: "use the get image
   size node, which is a base node that comes with ComfyUI and just
   connect the image and then connect this over here to the width and
   the height so that you automatically always get the same height as
   the original image."
5. Run at 2x upscale. Note the arithmetic the author states: "we are
   doing a two times upscale, this means it's creating four
   additional images, but if you have another ratio, it needs more
   images than that."

**Check**
- The adapted workflow produces the generated image and its upscale
  in one run, at the original image's height, with no manual
  resolution entry per image. The Get Image Size wiring is what
  makes that automatic.

**Why**
An upscaler subgraph with unwired outputs does nothing: the model,
VAE, and both prompts must be passed through, or the upscale has no
generation to refine. Deriving the size from the image removes the
one number that would otherwise drift between the generate step and
the upscale step.

### Phase 4: Review honestly, including the defects

**Do**
1. Review the test images the author generated: group portrait (face
   detail "more than actually from the MiniMax model"), mature-lady
   portrait (skin, eyes, soft lighting), perfume advertisement
   ("very intense with the colors", reflection and foreground depth
   of field praised), chess/music poster (text "in the right
   positions and with a beautiful font" and "spelled correctly,
   exactly as I defined it"), character sheet (emotional expressions
   good; small faces "often not so great", rendered multiple times).
2. For small faces, "use a face fixer before you do the upscaling so
   that you get a way better quality with that and also, of course,
   correct face details."
3. Run the prompt-adherence test: red square on a shiny ball, seven
   apples side by side, a triangle behind a glass of water. "Most of
   that, to be honest, is correct... The only mistake it made is to
   place a triangle shape behind the glass of water, and you can see
   that this is a pyramid that's kind of floating in the air."
4. Note the hand defect plainly: "on one of the hands we actually
   have six fingers. Now because the model is so lightweight and
   renders pretty fast you actually could render it just another
   time."
5. Note the uncensored claim as the author's claim: the model "also
   uncensored, so I tried different prompts of the spicy variety, and
   yes, it actually got the anatomy right, also down to the details".
   No such image is shown or verified in the retrieved text.

**Check**
- Upscaled quality is judged against the two named rivals: "this
  rival[s] Qwen 2.1 or MiniMax H3 image model from the amazing
  details of a close-up portrait" (ASR rendering; the comparison is
  the author's judgment, not a measured benchmark).

**Why**
A fast, lightweight model changes the defect economics: a six-finger
hand is a re-render, not a rescue job, because generation is cheap.
That only holds if the defects are checked per image, which is why
the review phase exists at all.

### The human method, distilled
1. The workflow names its own missing files; download exactly those.
2. Generate at the model's optimized resolution (1-2 MP); upscale
   after, do not generate big.
3. Wire the upscaler subgraph completely (model, VAE, both prompts)
   and derive its size from the image.
4. Re-render defects instead of rescuing them; fix small faces
   before upscaling, not after.
5. Review against named rivals and name the failures (six fingers,
   floating pyramid) in the same breath as the wins.

**Depth status:** FULL (252 ASR caption segments plus the full
description; files, workflow, resolution band, and defect reports all
disclosed. Caveat: the quantized model file names are ASR-garbled in
the captions and are taken from the workflow, not quoted here; no
step count, sampler, CFG, or render-time number is stated in this
video, unlike the Oct 21 starter recipe.)

## 6. "Creating 3D Textures is Basically Cheating Now..." (Blender Bros / Josh Gambrell)

Source: https://www.youtube.com/watch?v=3eHXIzavmHs | 15:11 (911 s) | 30,392 views | uploaded 2026-11-07 | Nano Banana via Prompt Edit; MaterialWorks: https://www.blenderbros.com/materialworks/

Tools used: ChatGPT (prompt writing), Nano Banana Pro (image
generation, via the Prompt Edit platform), Blender with the Node
Wrangler add-on, Cycles. MaterialWorks 2.0 is pitched in the video
but is NOT used in the demonstrated workflow; see Phase 5.

This audit reconstructs the exact workflow from the full ASR captions
(412 segments) and the description, step by step, so another agent can
follow the same process. Every phase has three parts: **Do**, **Check**,
and **Why**. The video's core method is: ChatGPT writes the prompt,
Nano Banana Pro draws the base color, then Nano Banana Pro converts
that same image into the other four maps one at a time, and Blender
assembles them with Node Wrangler. The creator's claim that the result
is "mathematically accurate" is his claim, not a verified measurement.

### Phase 1: Get ChatGPT to write the Nano Banana prompt

**Do**
1. "Hop here into Chat GPT. I'm just going to give this a basic
   prompt." The instruction: "generate me a prompt for Nano Banana
   Pro to create a concrete base color texture map. Don't generate
   anything right now except for the base color... clear chips,
   indentations, the shadows, kind of looking like the rock on a side
   of a mountain almost, a natural concrete-looking texture. Create
   a prompt so that way Nano Banana Pro can generate that for me."
2. Add the one thing ChatGPT's prompt misses: "we want it to be a 1
   by 1 square texture" (the generation platform can set that as a
   preset).
3. Do not generate in ChatGPT: "why don't I generate these in Chat
   GPT? It's because it's garbage... Nano banana is significantly
   better." (Creator's judgment, quoted.)
4. Speak the prompt if faster: the author uses Whisper Flow to dictate
   into the computer.

**Check**
- ChatGPT's prompt must be "very, very specific as to what it wants"
  before it is pasted anywhere. Vagueness at this step is the failure
  mode; the fix is rewriting the instruction, not regenerating blindly.

**Why**
Prompt-writing and image generation are split across two models on
purpose: GPT is good at writing the specific prompt, Nano Banana is
good at drawing the texture. Using one model for both jobs wastes
the strength of each.

### Phase 2: Generate five base-color candidates, pick one

**Do**
1. Use any Nano Banana platform ("there's a million different places
   to get Nano banana. You have the Gemini, you have this AI studio...
   Use whichever one you want. They're all basically the same"). The
   author uses Prompt Edit, "like 10 15 cents to generate one of
   these".
2. Paste the ChatGPT prompt in, choose 1:1 aspect ratio and 2K, and
   generate five versions "just so I can see like what type of a
   texture map I want".
3. Wait "maybe a minute or two" for the generation.
4. Pick the one you like most. The author picks one 2K 1:1 concrete
   map. "This would normally have required you going out, taking a
   picture of like a rock or concrete or something and you would
   have had to do like post-processing effects removing the lighting
   the shadows."

**Check**
- Zoom in on the candidates before choosing: the pick is judged on
  the chips, indentations, and shadow detail at full resolution, not
  on the thumbnail.

**Why**
Generating five costs more than one, but the conversion steps that
follow only need one map, and a bad base color poisons all four
derived maps. The extra generations are the cheap part; a wrong pick
is the expensive part.

### Phase 3: Convert the same image into normal, AO, roughness, displacement

**Do**
1. Download the chosen base color and feed it back to Nano Banana
   with a new prompt, one map at a time.
2. For the normal map, get ChatGPT to write the conversion prompt
   from the image: "I want you to write me a prompt for Nano Banana
   that will tell it to turn this into a normal map. It should not
   reposition any of the pixels or details or anything. All it needs
   to do is convert this into a normal map." ChatGPT's prompt adds
   "the actual normal map information here. The RGB colors that we
   want for a mathematically accurate normal map."
3. Paste the prompt into Nano Banana, drop the generated image in as
   the reference image, 1:1, 2K, one generation ("I only need one
   generation for this... It's only three credits for this which is
   pennies literally").
4. Download the normal map and flip between it and the base color:
   "if I go between them, they are literally perfectly overlaid on
   top of each other. Everything... There's no sort of
   repositioning."
5. Repeat the same ChatGPT-prompt-then-convert loop for the ambient
   occlusion map ("do the same exact thing, but this is going to be
   for an ambient occlusion map"), the roughness map, and finally the
   displacement map ("this one we can physically in the Cycles
   rendering engine like displace it off the surface... better than
   just a regular bump map").

**Check**
- The overlay flip is the acceptance check for every map: base and
  derived must align pixel for pixel with no repositioning or
  redrawing. The author checks it for the normal map and the AO map
  on camera; the same check is implied for the rest.
- *Inference, labeled:* no numeric alignment measurement is shown.
  "Perfectly overlaid" and "mathematically accurate" are the author's
  visual judgments, not measurements. A render test (Phase 4) is the
  only independent check shown.

**Why**
Converting the same image, with an explicit do-not-reposition
instruction, is what keeps the five maps registered to each other.
Generating each map independently from a text prompt would drift;
converting the chosen image keeps one set of chips, indentations, and
shadows across all five maps.

### Phase 4: Assemble in Blender with Node Wrangler and check in Cycles

**Do**
1. Add a plane, scale it up, apply the scale. Turn on the Node
   Wrangler add-on in Preferences.
2. In the Shader Editor, add a material, press Ctrl+Shift+T, and load
   the maps. Rename the files AO, base color, normal, roughness,
   displacement first ("Just rename them. Not a big deal") because
   Node Wrangler keys off the names.
3. Wire it: displacement into the displacement input, normal through
   a Normal Map node, roughness into the roughness value, base color
   into base color.
4. Wire the AO manually: Shift+A, Mix (Color), set to Multiply.
   Connect base color to the first slot and AO to the second, then
   drag the result into Base Color. ("I think we actually need to
   flip these. The base color should go into the first slot and that
   should go into the second.")
5. Load a simple HDRI, switch to Cycles, and look.
6. Set the AO multiply factor to 0.4 ("Unless you want like a harsh
   shadow... if this is set to zero, it's just going to give it the
   full base color... if you want more of a shadow, set that up to
   one... a normal shadow, you could do maybe 0.5"). Do not push the
   normal strength hard: "Don't go crazy, though. It's just going to
   look weird."
7. Play with the displacement scale ("a little bit heavier if you
   want"), the color (ColorRamp, Hue Saturation Value, or a Mix node
   "for a hint of whatever color"), then add a Solidify modifier,
   apply it, and run Smart UV Project ("because this is using UV
   coordinates... You could use generated if you prefer").
8. Keep the tiling restrained: "You just don't really want this to
   tile too much or it's going to be pretty obvious." Add a bevel for
   a concrete slab example.

**Check**
- The Cycles render with the HDRI is the check: "yep, I can see
  everything loaded in." The displacement read is judged by comparing
  the scale at zero against the scale turned up ("how clean that
  height information comes in compared if this was set to zero").

**Why**
Node Wrangler does the mechanical wiring from file names, so the
human work is the two manual decisions: the AO multiply (which is a
look decision, 0.4-0.5 for normal, 1.0 for harsh) and the
displacement scale. Everything else is naming discipline plus one
render check.

### Phase 5: Note what MaterialWorks is, and what it is not, in this video

**Do**
1. Treat the MaterialWorks mentions as a product pitch, not as steps
   in this workflow. At 08:22: "we have a texturing plugin that has
   already been built off of... mathematically accurate textures like
   this. It's called Material Works, and we just released our 2.0
   version, which has decals, trim sheets, and a full grunge
   generation system built in. All you have to do is install that,
   drag it into Blender, and then you get access to our entire
   library of hard surface details, textures, trim sheets, decals."
2. At 14:38, the pitch repeats with the vendor claim: "It has about
   21 million different texturing permutations. You don't really even
   need to generate your own textures, but if you do want to do that,
   you can also load those into Material Works as well... 50% off for
   the next 48 hours."
3. Record the cost claim for the demonstrated workflow separately:
   "five different texture maps... All these maps I generated in
   under 60 seconds for under a dollar. Honestly, under 50 cents
   using AI" and "I did this in 5 minutes, not even." Those are the
   creator's claims for one concrete example, not a measured average.

**Check**
- No MaterialWorks install, node, library item, or parameter appears
  in the captions. If a future audit cites this video for
  MaterialWorks, it is citing a pitch, not a demonstration.

**Why**
Separating the pitch from the workflow keeps the audit honest: the
transferable method is ChatGPT-to-Nano-Banana map conversion, and
MaterialWorks is a separate, untested product claim inside the same
video.

### The human method, distilled
1. Split the models: ChatGPT writes, Nano Banana draws.
2. Generate five, convert one: the pick is cheap, the conversion is
   the commitment.
3. Convert, never regenerate: the do-not-reposition instruction is
   what keeps the maps registered.
4. Flip between maps to check registration; render in Cycles to check
   the look. The author's "mathematically accurate" is a claim, not a
   measurement, until a render proves it.
5. Name the pitch: a product mentioned in a tutorial is not a step
   in the tutorial.

**Depth status:** FULL (412 ASR caption segments plus the description;
every prompt instruction, map, price, and Blender value quoted above
is in the captions. Caveat: the "mathematically accurate" and cost
claims are the creator's, unverified by any measurement in the video.)

## 7. "Creating a Glitch Render in Blender 5.3" (Max Hay)

Source: https://www.youtube.com/watch?v=ILR4joGRS6U | 17:36 (1,056 s) | 5,686 views | uploaded 2026-11-21 | Course: https://www.maxhayart.com/cyber-environments-course

Tools used: Blender 5.3, Geometry Nodes, shader editor (Layer Weight,
ColorRamp, Mix, Transparent, Emission, Volume), Poly Haven textures,
Wikipedia Commons textures (motherboard, glitch, dragonfly diagram,
fractal), Claude (AI texture search, see Phase 5), Photoshop
(touch-ups), compositor bloom.

This audit reconstructs the exact workflow from the full ASR captions
(523 segments) and the description, step by step, so another agent can
follow the same process. Every phase has three parts: **Do**, **Check**,
and **Why**. The video's core method is: start from a cube and a floor,
drive everything from two textures (one for color, one for alpha), and
vary one shader per object with a stored Geometry Nodes attribute
instead of copying the shader fifty times. Two methods the author tried
and abandoned are recorded as failure modes, not as steps.

### Phase 1: Make the floor read as puddles with one noise texture

**Do**
1. Start "just a floor plane and just a basic texture setup... just a
   texture from Polyhaven. You can use whatever source you want."
2. Run "a noise texture just running into the roughness, but more
   importantly, that same noise pattern runs into the normal map
   strength input."

**Check**
- "This creates areas of high and low normal map strength as well as
  high and low roughness in the same areas. So, it looks like
  puddles on the ground."

**Why**
One noise pattern driving two inputs in the same places is what makes
the puddle read: roughness and normal strength agree, so wet and dry
areas are the same areas, not two competing patterns.

### Phase 2: Build the cube shader from a glitch texture plus Layer Weight

**Do**
1. Load a cube with "basic computer textures, some glitch textures.
   So, one of them is just a motherboard and one of them is like a
   glitch just texture from... Wikipedia Commons... one of this
   one's probably from Unsplash."
2. "Using that image texture to drive the alpha and emission color...
   a good base for whatever else comes after that to make some kind
   of like cool techy look."
3. Drive the alpha with the glitch image through a ColorRamp "just
   with a bit more contrast", over a black cube underneath, "so you
   can see through into that".
4. Mix in a Layer Weight node with the ColorRamp adjustment, combined
   with the underlying computer texture "just with a mix color node
   set to multiply".
5. Drive the color with the TV RGB test-color image: "that's actually
   driving just the full color and that's pretty much it."

**Check**
- The viewing angle must change the read: "it is going to be brighter
  on the edges here. And when you look at it head-on, it's going to
  go dark." If the angle does not change the alpha, the Layer Weight
  wiring is wrong.

**Why**
The shader is two textures with two jobs: the glitch texture decides
where you can see through, the TV test image decides what color you
see. Layer Weight makes the transparency view-dependent, so the cube
glows at its edges and goes dark head-on, which is the glitch read.

### Phase 3: Record the two abandoned methods as failure modes

**Do**
1. Do NOT use the UV-map named-attribute image method for this scene:
   the author tried running "the UV map as a named attribute UV map
   run that straight into the image texture in geometry nodes" to
   drive selections on instances, "didn't really go too well and I
   didn't end up using that method in this one here."
2. Do NOT use the screenshot-outliner-to-AI scatter method: the
   author screenshotted the outliner's object list from an older
   project, pasted it into an AI to convert the image to text, and
   tried to scatter one instance per line. "This actually didn't end
   up going the way I wanted... I couldn't really make that work too
   well here... I kind of got sidetracked with trying to figure out
   a system to like get each line to be its own instance."

**Check**
- Both methods are named in the captions as tried and dropped. The
  audit records them so a reader does not re-try them as if they
  were the workflow.

**Why**
*Inference, labeled:* the author experiments in the open and drops
what does not work; the finished render is not evidence that every
method shown in the video worked. The two drops share a cause: both
tried to drive Geometry Nodes from a text/image list, and neither
produced one clean instance per item.

### Phase 4: Scatter characters with noise-driven Set Position

**Do**
1. Write out the characters "cube" and "x, y, and z" as individual
   letters and scatter them over the cube.
2. "Use a noise texture to drive a set position so it kind of like
   randomly explodes outwards from the cube."
3. Switch fonts and center the text ("trying to get that all
   centered").
4. Feed a glitch texture into the emissive shader on the text, box
   projected: "I've been using that a lot more since in geometry
   nodes you don't really UV maps are kind of hard. So, it's just
   easier to box project everything sometimes."

**Check**
- The scatter must read as "a mess of distributed floating exploding
  out text... expanding outwards in a scattered way from the cube",
  with "random variables and stuff", not as a neat grid. The
  "weird science textbook aesthetic" is the stated vibe check.

**Why**
Noise-driven Set Position is the scatter: one texture, one node,
random outward offsets, no per-letter hand placement. Box projection
is the texture shortcut for Geometry Nodes instances, where UVs are
hard; it trades UV precision for zero setup.

### Phase 5: Pick the dominant color, keep the composition conventional

**Do**
1. "Get the overall vibe like mapped out and figured out before I go
   too crazy into like the individual details of any one object...
   if the rest of the setting looks nice, I know I can make the
   central focal point good fairly easily after that. But if
   everything else is looking trash, it's really hard to make
   anything look good at all."
2. Skew the rainbow TV-test colors toward green: "picking a dominant
   color for the scene is really... even you can use all sorts of
   colors around that, but if you have the dominant color where like
   the majority of the light is like one kind of like one color,
   that'll help a lot with balancing things out."
3. Keep conventional composition rules even in a chaotic render:
   "trying to get even if we're going to do something glitchy and
   crazy, we still want to follow the conventional rules as much as
   we can to try and make it look good in terms of how the
   composition and the colors are."
4. Source real textures with AI search, not AI generation: "I've
   actually been getting the like Claude the AI to like go through
   [Wikipedia Commons] for me and like pick out images that I'm
   specifically looking for with a certain vibe... find... images
   that match when the license that I can use like CC0 images and
   two the basic aesthetic... I don't want to just use an AI
   generated texture here so much. So, if you can use the AI to just
   find real textures, that's kind of I feel like a better use of
   it. Just it's more just like a really targeted search."

**Check**
- The scene must stay "visually understandable" even at maximum
  chaos: "even if you're going to go super chaotic and crazy, you
  still want to have it, you know, like visually understandable."
  The author cuts detail in the middle when it becomes "a big mess
  of just too much detail... a little bit hard to even understand
  visually what's going on".

**Why**
A dominant color is the balancing mechanism for a rainbow texture:
one color carries most of the light, the rest are accents. AI as a
targeted search for licensed real textures keeps the texture sources
real and licensed, which AI generation would not guarantee.

### Phase 6: Glow with an extruded transparent shell, and grade the volume

**Do**
1. Use one linked Geometry Nodes system on every object ("these all
   every single object here has the same geometry node system linked
   together on it").
2. In that system, extrude the geometry and set the extrusion's
   material to a transparent shader "which has a value a little bit
   higher than one, so that any light going through it actually gets
   brighter", creating the glow. Layered over the Layer Weight
   shader underneath, "the angle you view it at will give you
   different values... the main strength is already like brighter on
   edges that are facing away from the camera", so the outside glows
   while interacting with the light shining down.
3. For the volume gradient: "get a cube, rotate it 90 degrees on the
   Y-axis, and then you just plug a gradient texture straight into
   the volume emission strength, and you can use a map range to
   control it, and then you'll have an upwards gradient... Turn the
   volume to zero and just use the emission only."

**Check**
- The extrusion glow must brighten light passing through it (value
  above 1.0), not just tint it. The volume gradient must read as an
  upwards emissive gradient, "a little video gamey, but it is kind
  of cool sometimes to throw that in" subtly.

**Why**
An extruded shell with a >1.0 transparent shader is a cheap glow:
no bloom pass, no extra light, just a shell that brightens what
passes through it. The rotated-cube gradient is the same idea for
volume: orientation plus a gradient texture, no simulation.

### Phase 7: Vary one shader per object with a stored attribute, then scatter like grass

**Do**
1. In Geometry Nodes, "storing a value in geometry nodes with a store
   named attribute. And then I can actually just change the location
   and rotation by hooking that value up to the shader editor with
   an attribute there. And that controls the shader group... so I
   can control the location and scale on the mapping node per object
   with the geometry nodes store named attribute."
2. Store different values per object "while keeping the shader the
   same between all of them... you want a bunch of variations of like
   the same texture without like 50 different copies of it."
3. Make clusters of cubes with the same Geometry Nodes system (glitch
   texture, transparent outer layer, floating variables), scatter
   them on the ground, and weight-paint the scatter "just trying to
   get it to feel natural and nice, like it's as if it's kind of
   like a plant almost... clusters of grass were growing somewhere...
   where it would naturally accumulate."
4. Duplicate the cube into pillars, change the one that reads too
   much like Ethereum, and keep the layout borrowed from a familiar
   structure: "big important thing in the middle with a bunch of
   pillars... heavenly lighting coming from the top as you might see
   in a church... taking the composition or layout of something
   that's very well known... and turning it into something that's
   completely different."
5. Keep one separated copy of the Geometry Nodes system for the
   "glitch mountains" background piece, tuned less intense and
   greener, so it sits in the background instead of competing.
6. Keep an accident: one frame where a disconnection turned
   everything black "actually looked really cool. So, I ended up
   toning down the emission strength... getting more shifting it more
   towards that vibe of like really dark black facing on that
   Fresnel-like Layer Weight node... a little more contrast... dark
   energy type vibe."

**Check**
- Per-object variation must come from the stored attribute, not from
  duplicated shaders: one shader, many mapping values. The scatter
  must accumulate like grass, not tile like a grid.

**Why**
A stored attribute is the per-object control surface: Geometry Nodes
writes the value, the shader reads it, and one shader serves every
object. Scattering like grass (weight-painted accumulation) makes
even glitch cubes read as a natural distribution, which is why the
scene feels placed instead of random.

### Phase 8: Finish in Photoshop and the compositor

**Do**
1. "Just did a quick run through of Photoshop. Usual touch-ups of
   like just a little bit of contrast, clarity, sharpening, and
   saturation, grain, uh bloom in the compositor as usual in in
   Blender. And then that's pretty much it."

**Check**
- The final render is the check; no render settings, sample counts,
  or compositor node values are stated in the captions.

**Why**
Finishing is a fixed, small routine (contrast, clarity, sharpening,
saturation, grain, bloom) applied after the scene is done, not a
second build pass.

### The human method, distilled
1. Vibe first, details second: map the overall scene before
   detailing any one object.
2. Two textures, two jobs: one drives color, one drives alpha.
3. One shader, many objects: vary it with a stored attribute, do not
   copy it.
4. Name the drops: the UV-attribute method and the outliner-scatter
   method did not work, and the audit should say so.
5. Keep chaos understandable: dominant color, conventional
   composition, and a cut when the middle gets too dense to read.
6. AI finds real textures; it does not generate them here.
7. Keep the accident when it looks better: the black frame became
   the darker, higher-contrast direction.

**Depth status:** FULL (523 ASR caption segments plus the description;
node types, wiring, values above 1.0, the 90-degree rotation, and both
abandoned methods are in the captions. Caveat: no render settings or
sample counts are stated, and the course project files were not
retrieved.)

## 8. "Super Fast & Easy Local Model - I use this everyday!" (Olivio Sarikas) - RE-SCAN

Source: https://www.youtube.com/watch?v=jQZZOWY7Arg | 10:37 (637 s) | 18,421 views in today's scan (11,845 at audit time) | uploaded 2026-11-16

Tools used: Qwen-Image-2.1 (7B parameters, Turbo 8-step), ComfyUI,
Hugging Face workflows (Comfy-Org/Qwen-Image-2.1).

This video is the same video ID audited in full on 2026-11-17 and made
into the skill `ai-video/qwen-image-21-comfyui-local`. It reappeared
because the 14-day channel window still covers it. No new workflow was
found in today's re-scan: the captions (244 segments today, 241 at
audit time; the difference is ASR segmentation, not new content) carry
the same workflow already in the skill: 7B parameters, Turbo 8-step,
16 seconds per image on an RTX 4080 at 2 megapixels, Euler sampler,
up to 10 reference images, multi-image edit, background removal to
transparent PNG, character sheets (front/side/back plus detail views)
as video-animation input, and the author's statement that the model
"is not open for commercial use". It was not re-audited and no skill
was duplicated or expanded for it. The watchlist row for Qwen-Image-2.1
(first seen 2026-11-17) is a genuine reappearance of the same video.

**Depth status:** RE-SCAN (already FULL, 2026-11-17; see that skill).

## Tooling extracted (summary)

| Tool / stage | Found in | Notes |
|---|---|---|
| Claude Opus 5.5 + a little Fable (agent-written game) | #1 Meltbelt | All code, shaders, textures; C++ liquid/heat sim; playtest-list loop truncated |
| Godot + C++ liquid/heat sim | #1 | Melt/sort loop; no parameters disclosed |
| Adventure Time face rig plugin (Godot, shader face) | #2 | Animatable; facial hair + smile curve unfinished; Ko-fi/itch; no method |
| Stylized Character Shader (Godot 4 spatial shader) | #3 | 4-component light, modified normals, adjustable shadow softness, painted AO, specular + rim, iris emission, SSS, optional outline |
| Hand-painted textures (Photoshop / Blender / Substance 3D Painter) | #3 | Textures first; painted AO; Zenless Zone Zero cited |
| Wiggle Bone addon (Godot 4) / Wiggle Bones (Blender) | #3 comment | Secondary motion, named not implemented |
| gitbonsai GitHub Action v0.5.0 | #4 | Weekly regrow, snapshot, bot commits, light/dark SVG |
| MOSS-Image int8 + Ultimate SD Upscaler | #5 | 1-2 MP optimized, prompt enhancer, Get Image Size wiring, face fixer advice; six-finger defect |
| ChatGPT prompt-writing + Nano Banana Pro (Prompt Edit) | #6 | 2K 1:1 base color, 5 candidates, 10-15 cents each; then normal/AO/roughness/displacement conversions, overlay check |
| Node Wrangler Ctrl+Shift+T + Cycles + HDRI | #6 | Rename maps, AO Multiply 0.4-0.5, Smart UV Project |
| MaterialWorks 2.0 (pitched, not demonstrated) | #6 | Decals, trim sheets, grunge; vendor claim 21M permutations |
| Blender Geometry Nodes + Store Named Attribute | #7 | Per-object mapping variation from one shader; noise Set Position scatter; extrusion glow shell |
| Layer Weight + ColorRamp + Multiply emissive shader | #7 | View-dependent alpha, TV RGB test color, black cube underneath |
| Poly Haven + Wikipedia Commons textures; Claude CC0 search | #7 | Floor texture, motherboard/glitch/dragonfly/fractal; AI as targeted search |
| Volume gradient (rotated cube, Gradient Texture, Map Range) | #7 | Volume zero, emission only, upwards gradient |
| Qwen-Image-2.1 Turbo 8-step (re-scan) | #8 | Already audited 2026-11-17; 16 s/image on RTX 4080, 10 refs, transparent PNG |

## Per-repo have-vs-need

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Agent-written game code/shaders/textures (Opus 5.5 + Fable) + playtest-list loop | #1 | NEED | Concept-to-input generation exists in `intake/`; no agent-written game-code stage, no playtest-list loop in the foundry | Backlog: the loop is undisclosed, so adopt nothing yet; watch for a fuller disclosure |
| C++ liquid/heat sim in Godot | #1 | NEED | Rust zone sim is deterministic SoA/navmesh, no liquid/heat sim | Watchlist: sim pattern only, different engine/stack |
| Shader face rig plugin | #2 | NEED | No rigging/skinning/retarget stage (P1 gap); a shader face is not a rig | Watchlist only: near-hit, not a fill; Tripo/Mixamo route stands |
| Stylized shader 4-component look-dev + hand-painted textures | #3 | NEED | No art bible / style-family enforcement beyond the protocol registry; no cel-shader stage | Backlog: adapt the textures-first, four-component spec pattern for look-dev docs |
| Gitbonsai weekly self-committing action (snapshot keeps schedule alive) | #4 | NEED | CI promotion gates + evidence publishing exist; no self-committing scheduled action with a snapshot guarantee | Backlog: the snapshot pattern is transferable to evidence publishing; cheap to copy |
| MOSS-Image int8 + Ultimate SD Upscale | #5 | NEED | Intake has concept generation; no local image model, no upscale stage | Watchlist: low-VRAM candidate for intake; skill expanded |
| Nano Banana PBR map conversion + overlay check | #6 | NEED | No PBR texture/material import policy or material validation gate (verified NEED); no texture-generation stage | Backlog with a verification gate: adopt the overlay check and prompt-writing split; do not adopt generated maps as "mathematically accurate" without a render/normal sanity test |
| Geometry Nodes Store Named Attribute per-object variation | #7 | NEED | No Geometry Nodes stage in the foundry; UE packaging exists but no per-object shader-variation convention | Watchlist: variation pattern for per-class profiles |
| MaterialWorks 2.0 library | #6 | NEED | No equivalent texturing library stage | Skip: pitched only, vendor claim unverified |
| Godot import validation / perf budgets / mesh compression / mesh refinement (P1 gaps) | — | NEED | Verified absent in the 2026-09-26 audit | No match today; gaps stand |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Agent-written game code (Opus/Fable) | #1 | PARTIAL | AI image client with fail-closed spend gate exists; agent-written game code is adjacent, not the same stage | Watchlist: loop undisclosed |
| Shader face rig plugin | #2 | NEED | Procedural rigs are stand-ins (audit NEED); no face-rig plugin, no shader-face stage | Watchlist: not a substitute for the production-conversion rig work |
| Stylized shader devlog (textures first, 4 components, painted AO) | #3 | PARTIAL | Projection shaders exist (`shaders/projection.gdshaderinc`); written art bible is a P1 gap (rec 2), toon-ramp law missing | Adopt now as art-bible input: textures-first rule + four-component breakdown + painted AO, adapted from anime to the 2d3d look |
| gitbonsai action pattern | #4 | NEED | No equivalent data-viz action; QA gates + CI fleet exist | Skip: pattern only, no 2d3d use |
| MOSS-Image int8 + upscale | #5 | NEED | AI image client exists; local image model is a different source | Watchlist |
| Nano Banana PBR conversion + overlay check | #6 | PARTIAL | Procedural texture generators exist (`pipeline/proc/make_textures.py`); AI map conversion is adjacent | Backlog: overlay flip-check as a QA step for generated textures; verify maps before use |
| Geometry Nodes scatter + stored-attribute variation | #7 | PARTIAL | Procedural authoring tools exist; Geometry Nodes scatter is a different authoring route, no detail gap filled | Watchlist |
| Asset import validation gate (P1, rec 9) | — | NEED | Verified absent; no naming/dims/pivot/manifest gate | No match today; gap stands |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Stylized character shader | #3 | NEED | No character-shader stage; buildings are the focus, animated subjects rig only what clips use | Watchlist: look-dev reference only |
| Nano Banana PBR maps | #6 | PARTIAL | Procedural authoring (`tools/procedural_art.py`, `city_*` family) exists; AI texture-map generation is adjacent | Watchlist: texture source option for facades/props, with the overlay check |
| Geometry Nodes scatter (grass-like accumulation) | #7 | PARTIAL | Headless Blender sprite render + procedural authoring exist; Geometry Nodes scatter is Blender-side, adjacent | Watchlist: scatter-distribution pattern |
| MOSS / Qwen local image models | #5, #8 | NEED | AI inputs optional (`tools/openai_key.py`, `tools/tripo_key.py`); no local image-model stage | Watchlist: concept-art sources |
| Shader-driven skyline fill (P1 gap) | — | NEED | No equivalent; every building authored/generated | No match today; gap stands |
| Face rig plugin / gitbonsai | #2, #4 | NEED | No equivalent stages | Skip: no Desktop City use |
| AI-vendor acceptance spec (P1-adjacent) | #6 | NEED | Generated code/images require execution + visual review, but no written "what good means" per asset class | Adopt the overlay-check idea as one written check for generated textures |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Stylized shader look-dev | #3 | NEED | Concept PNG is visual authority; no shader look-dev stage in the pipeline | Watchlist: look-dev pattern for character/station materials |
| Nano Banana PBR conversion | #6 | PARTIAL | Concept PNG + Meshy GLB in, production GLBs out; texture-map generation from an image is adjacent to the texture stage | Watchlist: candidate texture source, with overlay verification |
| MOSS-Image int8 + upscale | #5 | NEED | No image-gen stage in the pipeline | Watchlist |
| Geometry Nodes stored-attribute variation (one shader, per-object values) | #7 | PARTIAL | Per-class export profiles exist (`profiles/*.json`); per-object shader variation from one shader is adjacent | Watchlist: variation pattern could tighten per-class texture work |
| Face rig plugin | #2 | PARTIAL | Rig stage present (`stages/rig.py`, `assetpipe/blender/rig.py`); a shader face rig is a different kind, no skeleton | Watchlist only: near-hit, not a rig-stage fill |
| Godot import validation gate + re-measured export budgets (P1 gap) | — | NEED | No Godot project yet; budgets are oracle budgets, ADR 0003 requires re-measuring | No match today; gap stands |
| gitbonsai | #4 | NEED | No equivalent | Skip |

## Watchlist trending

Script output (verbatim from `bin/trend_watchlist.py --date 2026-11-21`):

## Watchlist trending
- Godot 4.5 .NET procedural creature pipeline (seed -> rig -> animations -> transparent PNG sheets + JSON manifest with directions/frames/pivots/timing; frame counts auto-derived from movement type; purely 2D; built with Claude Opus 5.5 + GPT Astra 6) (first seen 2026-10-04, status WATCH; seen again 2026-10-09, 2026-11-04, 2026-11-05, 2026-11-06, 2026-11-14, 2026-11-16, 2026-11-18, 2026-11-20, 2026-11-21) **TRENDING**
- MIDI fingering precalculation for robot piano hands (enamore22, three.js, built with Claude Opus 5.5) (first seen 2026-11-03, status WATCH; seen again 2026-11-04, 2026-11-05, 2026-11-12, 2026-11-14, 2026-11-16, 2026-11-21) **TRENDING**
- Claude Code Opus 5.5 + Tripo P2 + ElevenLabs solo-game pipeline (first seen 2026-11-14, status WATCH; seen again 2026-11-16, 2026-11-18, 2026-11-20, 2026-11-21) **TRENDING**
- Claude Fable 5.2 as Blender-Python 3D modeling code agent (first seen 2026-11-19, status WATCH; seen again 2026-11-20, 2026-11-21) **TRENDING**
- Godot tile-based flood/water sim (tile fill, lowest point, soil soak) (first seen 2026-10-16, status WATCH; seen again 2026-11-16, 2026-11-21) **TRENDING**
- Crushform (UE5 real-time vehicle damage plugin, lattice + WPO dents) (first seen 2026-10-31, status WATCH; seen again 2026-11-21)
- Runtime procedural rig + skin generation in GDScript (Godot 4, Primordium by Ouvolk) (first seen 2026-11-08, status WATCH; seen again 2026-11-09, 2026-11-14, 2026-11-16, 2026-11-20, 2026-11-21) **TRENDING**
- Fluid Forge (UE real-time fluid sim plugin, FAB, Atomic Lighthouse) (first seen 2026-11-12, status WATCH; seen again 2026-11-21)
- Hand-painted stylized character texturing (Substance Painter + ZBrush + Arnold Maya, toon aiStandardSurface variant) (first seen 2026-10-07, status WATCH; seen again 2026-10-21, 2026-10-30, 2026-11-06, 2026-11-07, 2026-11-16, 2026-11-20, 2026-11-21) **TRENDING**
- Godot procgen shader-window city (SurfaceTool boxes, no window textures) (first seen 2026-10-28, status WATCH; seen again 2026-11-03, 2026-11-14, 2026-11-16, 2026-11-21) **TRENDING**
- Godot window + raindrop shader (per-pane torus sampling, heightmap normals) (first seen 2026-10-28, status WATCH; seen again 2026-11-03, 2026-11-14, 2026-11-16, 2026-11-21) **TRENDING**
- Godot compute-shader creature brain (teninogamestudio, Godot 4.7 C#) (first seen 2026-10-29, status WATCH; seen again 2026-10-30, 2026-11-03, 2026-11-14, 2026-11-16, 2026-11-20, 2026-11-21) **TRENDING**
- Godot silk-boss VFX (vector shapes + custom pixelation shader) (first seen 2026-11-02, status WATCH; seen again 2026-11-03, 2026-11-14, 2026-11-16, 2026-11-21) **TRENDING**
- Godot fake frustum culling shader (camera-discard visualization, partybusiness) (first seen 2026-11-03, status WATCH; seen again 2026-11-14, 2026-11-16, 2026-11-21) **TRENDING**
- Godot 4 noise sky shader (gdshader on Sky material, procedural stars/nebulae) (first seen 2026-11-06, status WATCH; seen again 2026-11-14, 2026-11-16, 2026-11-20, 2026-11-21) **TRENDING**
- Godot raymarched jet-exhaust shader (mach diamonds + point-light glow) (first seen 2026-11-07, status WATCH; seen again 2026-11-14, 2026-11-16, 2026-11-21) **TRENDING**
- SimpleGrassTextured Godot grass base (alexvice02 rework, 3 shader variants by perf tier) (first seen 2026-11-08, status WATCH; seen again 2026-11-14, 2026-11-16, 2026-11-21) **TRENDING**
- Godot Item Box shader + free eBook (jettelly) (first seen 2026-11-14, status WATCH; seen again 2026-11-16, 2026-11-21) **TRENDING**
- Substance Painter 3D-space blur filter (baked Position Map, blur by 3D proximity to kill UV seams; previously paid Gumroad, now free) (first seen 2026-10-12, status WATCH; seen again 2026-10-21, 2026-10-30, 2026-11-07, 2026-11-16, 2026-11-21) **TRENDING**
- material-painter (free open-source Substance Painter alternative, alla2001/material-painter) (first seen 2026-10-01, status WATCH; seen again 2026-11-02, 2026-11-07, 2026-11-16, 2026-11-21) **TRENDING**
- MOSS-Image (OpenMOSS, 5B DiT + Qwen3.5-9B text encoder + FLUX.2 VAE, Apache 2.0) (first seen 2026-10-21, status WATCH; seen again 2026-10-28, 2026-11-01, 2026-11-18, 2026-11-21) **TRENDING**
- Qwen Image Edit 2.1 in AI-video pipelines (first seen 2026-10-23, status WATCH; seen again 2026-10-24, 2026-10-28, 2026-10-29, 2026-11-05, 2026-11-17, 2026-11-18, 2026-11-19, 2026-11-21) **TRENDING**
- Automated AI documentary pipeline (Claude visual bible + Qwen Image 2.1 + Claude QA + MiniMax H3 + Qwen3-TTS + RTX Video Super Resolution) (first seen 2026-10-27, status WATCH; seen again 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-11, 2026-11-12, 2026-11-14, 2026-11-18, 2026-11-19, 2026-11-20, 2026-11-21) **TRENDING**
- Qwen-Image-2.1 (7B local image model, Turbo 8-step, ComfyUI) (first seen 2026-11-17, status WATCH; seen again 2026-11-18, 2026-11-19, 2026-11-21) **TRENDING**
- Nano Banana-class image edit in intake/ (first seen 2026-09-27, status BACKLOGGED; seen again 2026-09-28, 2026-10-29, 2026-11-01, 2026-11-05, 2026-11-21) **TRENDING**
- Raup shell morphospace (flare/verm/spire parametric 3D generation; snug-fit rule verm=1/flare; Blender geo nodes + TouchDesigner; Blender/TouchDesigner files on Patreon) (first seen 2026-10-04, status WATCH; seen again 2026-10-05, 2026-10-06, 2026-10-07, 2026-11-12, 2026-11-14, 2026-11-16, 2026-11-21) **TRENDING**
- Blender Geometry Nodes flower motion-design setup (first seen 2026-10-15, status WATCH; seen again 2026-10-22, 2026-10-26, 2026-11-12, 2026-11-14, 2026-11-16, 2026-11-21) **TRENDING**
- Geometry Nodes upright-billboard flat-line technique (Blender) (first seen 2026-10-22, status WATCH; seen again 2026-10-26, 2026-11-12, 2026-11-14, 2026-11-16, 2026-11-21) **TRENDING**
- Blender voxel-remesh merged-geometry repair (Pose brush separation + edit-mode delete/Grid Fill/Dyntopo) (first seen 2026-10-26, status WATCH; seen again 2026-11-12, 2026-11-14, 2026-11-21) **TRENDING**
- Blender hidden-geometry separation fix (F/G key slip, Separate by Selection) (first seen 2026-10-26, status WATCH; seen again 2026-11-12, 2026-11-14, 2026-11-16, 2026-11-21) **TRENDING**
- Poly Haven base textures in scripted Blender pipelines (wood textures as shader inputs) (first seen 2026-11-20, status WATCH; seen again 2026-11-21)

**Verification (manual, against the audits above):** the script
token-matches, so most of that list is false. Genuine reappearances
today: **MOSS-Image** (Olivio int8 + upscale variant, same model),
**Qwen-Image-2.1** (same Olivio video re-scanned), **Nano Banana**
(first genuine Nano Banana Pro use since the 2026-09-27 backlog row;
prior "seen again" entries were token overlaps on Qwen image edit),
and **Poly Haven** (glitch-render floor texture, second day running).
Related-but-not-genuine: the Fable mention in Meltbelt ("a little
Fable", no workflow), the hand-painted-texture part of the stylized
devlog (different stack from the Substance+ZBrush+Arnold row), and
the Qwen Image Edit row (same model family, different workflow).
Every other row was annotated in
`references/tooling-watchlist.md` as a token-overlap false match,
following the file's established practice.

**New watchlist rows appended 2026-11-21:** Meltbelt playtest-list
loop; Adventure Time face rig plugin; Stylized Character Shader for
Godot 4; gitbonsai; MOSS-Image int8 + Ultimate SD Upscale variant;
Nano Banana Pro PBR texture-map conversion; MaterialWorks 2.0
(pitched, not demonstrated); Blender glitch render Store Named
Attribute variation; Claude AI as CC0 texture scout.

## Gap recommendations (highest leverage)

1. **Write the stylized devlog's textures-first rule into the 2d3d
   art bible (P1).** The devlog is a complete, quotable spec: painted
   textures carry the style, light splits into four components,
   normals are art direction, AO is painted in. Next step: draft one
   art-bible entry in that shape for the 2d3d look, with the
   hand-painted-texture requirement stated before any shader work.
2. **Adopt the Nano Banana overlay flip-check, not the maps, into
   texture QA (P1 acceptance-spec adjacent).** Flipping between base
   and derived maps to prove pixel registration is cheap and
   verifiable. Next step: require the flip-check (and a Cycles render
   check) before any AI-converted normal/AO/roughness map enters a
   pipeline; treat "mathematically accurate" as unproven until then.
3. **Keep MOSS-Image int8 + upscale on the watchlist as the low-VRAM
   intake candidate (P1 acceptance-spec adjacent).** The 1-2 MP
   generate-then-upscale pattern, with the Get Image Size wiring and
   the face-fixer-before-upscale rule, is the cheapest local image
   route seen this month. Next step: none until intake needs a local
   image model; the existing skill is expanded with this variant.
4. **Copy gitbonsai's snapshot pattern for scheduled evidence work
   (cheap, cross-repo).** A snapshot plus a week stamp so every run
   commits, a bot identity so automation never counts as the owner's
   work, and a named silent-failure mode (green run, no commit).
   Next step: apply the pattern to any scheduled publishing job that
   can go quiet.
5. **Treat the shader face rig as a warning, not a solution (P1 rig
   gap).** A shader face that animates with no rig, no skinning, and
   no disclosed method is exactly how the rig gap gets papered over
   in solo-dev work. Next step: keep the Tripo P2.0 / Mixamo rig route
   as the plan, and mark any shader-face character as a placeholder
   in its manifest.

## Explicit non-goals (found but correctly skipped)

- Tony Hawk pixel low-poly hybrid, wurq8 procedural trees/water,
  Fort McHenry VFX breakdown, cloud-Blender cinematic, Blender
  parody, next-gen Godot simulation, 3D-printing showcase,
  speedsculpt: high engagement or a tooling-sounding title, no
  extractable workflow in the retrieved text. Not skills, not gaps.
- Grokbot IDEAS, Imagination Studio, 3D Emojis, Rendering Really Is
  This Simple: YouTube videos scanned but not summarized; description
  snippets carry no workflow. Not audited.
- MaterialWorks 2.0: a pitch inside the Nano Banana video, not a
  demonstrated workflow. Watchlist row only, no skill, no gap fill.
- Meltbelt and the face rig plugin stay in this report only:
  DEPTH-LIMITED, no extractable workflow, never padded into `skills/`.
- Qwen-Image-2.1: re-scan of a video already skilled on 2026-11-17.
  No duplicate skill, no new row beyond the genuine watchlist
  reappearance.

## skill_library artifacts staged

- New skill `characters/godot-stylized-character-shader` (audit #3).
- New skill `automation/gitbonsai-github-activity-tree` (audit #4).
- Expanded skill `ai-video/moss-image-comfyui-recipe` with the
  2026-11-21 Olivio int8 + Ultimate SD Upscale variant (audit #5).
- New skill `materials-shaders/nano-banana-pbr-texture-maps`
  (audit #6).
- New skill `simulation-vfx/blender-glitch-render-geometry-nodes`
  (audit #7).
- Full report published to
  `docs/scout-reports/have-vs-need-2026-11-21.md`; watchlist rows
  synced to the repo mirror
  `video-tooling-scout/references/tooling-watchlist.md`; README
  tables updated (counts only).

## Run notes / coverage gaps

- Reddit: comfyui 429'd on the scan pass; its video posts are missing.
- Comments: Arctic Shift returned zero comments for Meltbelt (14
  reported); old-Reddit/PullPush fallbacks also returned nothing.
  PullPush 429'd on full-post-text requests.
- Text fetches: Reddit page blocked by policy for `browser.open`;
  itch face-rig page timed out. Neither recovery used the live
  browser, per the hard rules; both gaps are recorded above.
- YouTube: first pass failed on SSL for all 11 channels; the egress
  CA was appended to the `skills/video-summarizer` venv bundle and
  the re-scan returned 13 videos with 0 warnings. The bundle had
  lost the previously appended CA, so this fix may need repeating.
- Downloads: 0 attempted, 0 succeeded, 0 approval gates, 0 retries.
  No model files downloaded. All four new YouTube audits rest on
  full ASR captions.
- The Qwen and MOSS videos are re-scans/variants of already-skilled
  work; dedup was checked against the skill_library tree before any
  new skill was created, and the MOSS variant expands the existing
  skill instead of duplicating it.
