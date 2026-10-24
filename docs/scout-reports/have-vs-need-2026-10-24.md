# Video tooling scout: have-vs-need, 2026-10-24

Depth mode: **pre-approved** (max 2 media downloads). Depth-escalation usage:
**0 downloads attempted, 0 succeeded, 0 skipped.** No download was needed:
the one YouTube video that mattered (the APEX walkthrough) yielded full
captions (594 segments) on the captions-first path, and every native Reddit
clip in this run carries its tooling signal in post text and comments, where
a media download would add nothing. The allowance was not exhausted; it was
simply not required.

Scan: 12 Reddit video posts across 23 subreddits (2-day window ending
2026-10-24), min_score 20. Plus 3 YouTube videos from the channel scan
(see below). All 23 subreddits returned data; comment retrieval worked
via Arctic Shift for every post this run (no 422s, no PullPush fallbacks
needed). Full selftext was re-fetched from Arctic Shift for the top posts
because the scan output truncates it to snippets.

YouTube channel scan: the first attempt failed on every channel with an
SSL certificate error (the sandbox egress proxy's CA was missing from the
scan's yt-dlp venv bundle). A second attempt with an env-var CA bundle
failed the same way (yt-dlp ignores that env var). Fix applied per
AGENTS.md: the current Hatch Sandbox Egress CA
(`/usr/local/share/ca-certificates/hatch-egress-ca.crt`) was appended to
the skills venv certifi bundle
(`~/workspace/skills/video-summarizer/.venv/lib/python3.12/site-packages/certifi/cacert.pem`;
pre-change backup at `/tmp/cacert-backup-2026-10-24.pem`, ephemeral).
After the fix the scan completed: 11 channels scanned, 3 videos found, all
from BlenderSecrets (see "Scanned, not analyzed"). Four channels
(RyanKingArt, Ducky3D, JoshGambrell, KaizenTutorials) each had one video
blocked by YouTube's "Sign in to confirm you're not a bot" check; no
cookie workaround was attempted (out of this loop's scope), and the
remaining channels returned no in-window videos. The scan itself took
far longer than usual through the proxy (roughly 15 minutes wall clock)
but completed on its own; nothing was killed or retried.

## Gap alerts

**One P1 gap alert: rigging / skinning / animation-retarget (aegis P1).**
The Reallusion Rigger HDA (audit 2, FULL) is a meaning-match for this gap:
it is a complete, shipping rigging stage that takes an imported character,
builds a full animatable rig, and supports both animating from scratch and
modifying incoming animations, including cross-skin retargeting (with the
author's own warning that retargeting is an approximation). Caveat, stated
plainly: this is a Houdini-side commercial HDA for Character Creator /
iClone characters, not a drop-in for the Aegis trellis-pipe foundry. The
gap stays open. What it contributes is a proven shape for the stage
(one-click import → rig → animate/modify, with a build-time budget and a
named retarget failure mode) and a concrete design input for the
`rigging-stage-design.md` fix artifact. It does not close the gap.

Checked against `references/p1-gaps.md` by keyword and by meaning; all
other gaps: no match.

- Per-asset perf budgets (aegis P1): near-miss, not a fill. The tree
  generator (audit 6) gives a representation-level budget argument
  (cylinder primitives, "very little memory") and the ring-world post
  (audit 3) reports a live perf constraint ("keeping it running smoothly
  with so much scenery visible at once"), but neither states tri counts,
  texel density, or draw calls. Recorded under Gap recommendations only.
- AI-vendor acceptance spec (aegis P1): near-miss, not a fill. The
  MiniMax swap audit (audit 1) is a generation workflow, not a "what good
  means" spec — but its two author-reported failure modes (smearing in
  fast motion; missing facial detail in wide shots) are directly usable as
  measurable acceptance criteria for the intake spec. Recorded below.
- Skyline fill (desktop-city P1): no match. The ring-world shader trick
  (audit 3) is a different problem (faking world curvature, not filling
  unmodeled buildings with shader output) and must not be conflated with it.
- Import validation, mesh compression, mesh refinement, art bible, Godot
  import gate, MCP DCC loop: no matches in today's tooling.

## Videos deeply analyzed

| # | Video | Creator | URL | Duration | Source |
|---|-------|---------|-----|----------|--------|
| 1 | "I tried AI character swapping with MiniMax H3 in ComfyUI" | Time-Ad-7720 | https://v.redd.it/t12g0lx3m3xh1 | n/a (native clip) | r/comfyui post 1xcxdz5 (score 79, 7 comments). Depth: PARTIAL (full post text + comments; tutorial page not retrieved, no captions on native clip) |
| 2 | "Character Creator/iClone to APEX rig in Houdini" | tonehammer (tool: JV Tools) | https://v.redd.it/ogpak0dbv3xh1 | 22:56 walkthrough | r/Houdini post 1xcyokv (score 70, 11 comments) + YouTube https://www.youtube.com/watch?v=03yV4UPGfDQ (594 captions). Depth: FULL |
| 3 | "A look around my ring world prototype" | k0zakinio | https://v.redd.it/e8zgjaabl3xh1 | n/a (native clip) | r/proceduralgeneration post 1xcxac1 (score 361, 29 comments). Depth: PARTIAL (post text + comments; engine undisclosed, no parameters) |
| 4 | "Anything i can do to improve this shot?" | Willing_Touch1157 | https://v.redd.it/8ks144mc72xh1 | n/a (native clip) | r/Houdini post 1xcq4a0 (score 287, 42 comments). Depth: PARTIAL (post text + comments; no node graph or parameters) |
| 5 | "Shrimp" | yellowpenmaker | https://i.redd.it/wd7lg6e2f2xh1.gif | n/a (gif) | r/3Dmodeling post 1xcrb76 (score 122, 13 comments). Depth: NO-TOOLING (Blender named, "took me like 6 hours", no workflow) |
| 6 | "Making trees" | SloydDev | https://v.redd.it/5ywyo5v3m2xh1 | n/a (native clip) | r/proceduralgeneration post 1xcsip6 (score 73, 12 comments). Depth: PARTIAL (post text + comments; no code or parameters) |
| 7 | "Procedural cityscape" | deepak365days | https://v.redd.it/i2shc340n1xh1 | n/a (native clip) | r/proceduralgeneration post 1xcmz4c (score 38, 0 comments). Depth: NO-TOOLING (empty selftext, no comments) |
| 8 | "Sculpting Ryu from Street Fighter" | SoulScience1 | https://v.redd.it/b2jwwnlbv0xh1 | n/a (native clip) | r/3Dmodeling post 1xciww4 (score 41, 1 comment). Depth: NO-TOOLING (sculpt showcase; "refining the spine muscles", no tool disclosed) |

Scanned, not analyzed (8-video cap): "Realtime fire sim" (r/Simulated,
relevance 0.5, no engine named; author says a Play Store release is
planned next week); "Paw" (r/3Dmodeling; one technique note: toes were
made separately then attached after extruding from the base mesh failed
to align); "quest giver character progress" (r/unity; one dialogue-UI
tip: pre-type the full text at alpha 0, then reveal letters one by one,
so words never jump lines mid-typing); "Daisies (viewport in comments)"
(r/3Dmodeling; lighting note: blocking lights from directions, top light
with a color ramp on alpha plus a noise texture for a cloudy-day look,
which the author says did not work as intended). YouTube candidates not
analyzed (cap): Blender Secrets "How to do an inverted hull outline and
what if it doesn't work?" (2026-10-12, 295 s, 9,242 views), "5 Blender
tips: Mio3 Flex, Booleans to Quads, Edge Flow, camera animation and
combining cameras" (2026-10-11, 405 s, 12,548 views), "5 Tips: Square to
Round shapes, Inverted Hull, Reduce polycount, find double geometry,
better bevels" (2026-10-15, 736 s, 11,408 views). The inverted-hull
outline videos are the carry-forward for the next run: a toon-outline
technique is directly relevant to 2d3d's P1 art-bible/toon-law work.

## 1. "I tried AI character swapping with MiniMax H3 in ComfyUI" (Time-Ad-7720)

Source: https://v.redd.it/t12g0lx3m3xh1 | r/comfyui post 1xcxdz5 (score 79)

Tools used: ComfyUI, MiniMax H3 Reference-to-Video workflow, Krea 2 and
Qwen Image (character-reference generation). Local hardware: RTX 5070 Ti.
Tutorial + downloadable workflow + assets:
https://www.kaziahmed.net/kazitorials/minimax-character-swap (linked in
the post; page itself not retrieved this run, so no settings are claimed
from it).

This audit reconstructs the workflow from the post text and comments, step
by step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it),
and **Why** (the principle). The video's core method is: keep the source
video's motion and performance, replace the person and the environment
with AI-generated ones, no motion capture.

### Phase 1: Pick the source and the replacement

**Do**
1. Take an existing video as the motion source.
2. Generate the replacement character's references with Krea 2 and Qwen
   Image (author's stated tools for this step).

**Check**
- The reference reads as the intended character before any video is
  generated; the source video's performance is the thing being preserved.

**Why**
- Motion source and likeness source stay separate: the source footage
  supplies movement, the generated references supply appearance. (Same
  split as the existing SAM3 character-swap skill, different mechanism.)

### Phase 2: Run Reference-to-Video in ComfyUI

**Do**
1. Run MiniMax H3's Reference-to-Video workflow in ComfyUI locally
   (author runs it on an RTX 5070 Ti).
2. Swap the character and, if wanted, the environment, while keeping the
   movements and performance from the source footage.
3. Iterate with prompt engineering and workflow adjustments (author's
   words: "Getting better results through prompt engineering and workflow
   adjustments").

**Check**
- The output keeps the source performance; the character and environment
  are the new ones. The author is explicit that this is still
  experimental: "Still experimenting with consistency, motion accuracy,
  and generation performance."

**Why**
- Author's stated goal: character animation and indie filmmaking without
  traditional animation or motion-capture pipelines.

### Phase 3: Watch for the two known failure modes

**Do**
1. Check fast-motion sections for smearing.
2. Check wide shots for facial detail loss.

**Check**
- Author, answering "What have your biggest challenges been?":
  "Smearing in fast motion, and lack of facial details in wide shots."
  (Verbatim; these are the author's own words, not a reviewer's.)

**Why**
- These two checks are the acceptance test for any take from this
  workflow until the author reports otherwise. They are also the
  near-miss evidence for the Aegis intake acceptance-spec gap (see Gap
  alerts): a spec for character-swap takes should name exactly these two
  measurements.

### The human method, distilled

1. **No mocap setup required** (author's words): source footage is the
   motion capture.
2. **References are generated, not photographed**: Krea 2 + Qwen Image
   supply the character references.
3. **Iterate on prompts and workflow settings**, not on capture hardware.

### Commenter claims (unverified, labeled)

- DaLyon92x claims a "brand new swap lora, facerefine second stage and
  supports up to 3 people in one render", "tested and verified at 16gb+
  vram", entered in a Comfy challenge. The creator has not tried it:
  "I haven't tried it yet, will check and report back." This answers the
  thread's open question ("Can you replace two fighting persons at the
  same time?") only as an unverified claim; the multi-person case is
  otherwise unanswered.
- switch2stock suggests ComfyUI-MAINodes
  (github.com/matlowai/ComfyUI-MAINodes) "for fast paced" work. Same
  status: suggested, not creator-confirmed.

**Depth status:** PARTIAL (full post text + all 7 comments; the tutorial
page's workflow, assets, and settings were not retrieved, and the native
clip has no captions).

## 2. "Character Creator/iClone to APEX rig in Houdini" (tonehammer / JV Tools)

Source: https://v.redd.it/ogpak0dbv3xh1 | r/Houdini post 1xcyokv (score 70)
| Walkthrough: https://www.youtube.com/watch?v=03yV4UPGfDQ ("Reallusion
Rigger 1.1 Walkthrough", jvtools, 22:56, 594 caption segments, 30 views)

Tools used: **Reallusion Rigger HDA** (JV Tools; the refreshed version of
the Reallusion Importer), **Houdini 22+** (Indie or Apprentice, ships as
`.hdalc`), **Character Creator 5 / iClone 8** characters, **USD or FBX**
import, **Karma CPU/XPU** materials in LOPs, **APEX** rigging/animation,
**Solaris** (SOP import points at the final animated character).
Product: https://jvtools.dev/products/reallusion-rigger/ ; docs:
https://jvtools.dev/docs/ . Previous Reallusion Importer owners get the
Rigger HDA free; all future updates included. (No price is stated in the
captions or post, so none is claimed here.)

This audit reconstructs the exact workflow from the 22-minute
walkthrough's captions and description, step by step, so another agent
can follow the same process. Every phase has three parts: **Do** (the
action), **Check** (how the human verifies it), and **Why** (the
principle). The video's core method is: one click turns a CC5/iClone
character into a shaded, animatable, render-ready Solaris character with
a full APEX rig.

### Phase 1: Build the character (importer baseline)

**Do**
1. Set the build toggles, then press **Build Character**. With everything
   off, the HDA still pulls in data and textures from the exported
   character's folders and builds shaders in a material library in the
   stage (LOP) context.
2. Optionally enable cameras, lights, and a Karma render settings node.
3. Optionally set the scene frame range to the incoming animation's
   length (on by default).

**Check**
- With the two options above on, the result is "fundamentally exactly
  what the older Reallusion Importer HDA does", and the build takes
  "just a few seconds, because all of this was the easy part."

**Why**
- The Rigger is a strict superset of the Importer: if you only ever
  animate outside Houdini (iClone or another tool), the Importer path
  still suffices. The Rigger adds the APEX rig for animating from scratch
  in Houdini or modifying incoming animations.

### Phase 2: Build the APEX rig

**Do**
1. Enable the APEX rig toggle before building. This constructs the full
   APEX chain for the character.
2. To save build time, disable the facial rig if the face will not be
   animated or visible (mask, helmet, off-camera face).
3. To save more, disable expression presets and hand poses if the
   animation catalog features will not be used.
4. Choose stash behavior: stash the rig internally in the scene (default,
   via a stash SOP) or externally on disk.

**Check**
- APEX build time: "an average between 1 and 2 minutes in a good system",
  versus seconds for the importer-only build. Disabling the facial rig
  returns "20-30 seconds" of that time.
- The rig node (the "sidecar") is where animation and APEX settings
  live; its top button jumps into the Python state of the APEX animate
  node, the button next to it exits. Diving into the APEX node shows the
  setup nodes (edge cases, wrangling) above, then the "back character"
  node, after which everything is the rig logic itself; the default APEX
  animate node should be the last APEX animation node in the chain, and
  the out-geo below it is the final animated character the Solaris SOP
  import points at.

**Why**
- Build time is a budget, not a surprise: facial rig and catalog data are
  the two expensive toggles, and both are optional. The sidecar pattern
  (one node holding the animate state, with the rig logic open for
  extension after it) means "after this node, you can add, modify,
  manipulate anything you want using the usual Apex rigging tools."

### Phase 3: Set rig behavior (hair, viewport, gear LODs)

**Do**
1. Set the hair toggle: hair-follows-head-only ON means the whole hair
   deforms with the head only; OFF (the CC5/iClone default) leaves the
   hair partially skinned to shoulder and clavicle joints so long hair
   drapes over the shoulders.
2. Use the gear LOD toggles to hide or reveal control sets per body part
   in the viewport, simplifying a busy rig.

**Check**
- With hair-follows-head-only off, the hair visibly drapes; with it on,
  "the entire hair is moving instead of draping." The author's
  recommendation: Houdini users will usually want a native groom, so
  head-only is the likely choice, but both are offered.

**Why**
- CC5/iClone skinning conventions do not match Houdini groom
  conventions; the toggle is the seam between them, made explicit
  instead of baked in.

### Phase 4: Mix motion clips (retarget, with a warning)

**Do**
1. Input lightweight USD motion clips (as many as needed), regardless of
   whether the character came in as USD or FBX.
2. Choose which frames of each clip to use (or first/last frame only),
   press Update Motion Clips, then control which clips play in the APEX
   state.

**Check**
- The HDA "will try its best to do a rig retarget for different skins,
  but it will be just an approximation. It should work, but there might
  be some ugly deformations in there depending on how different the
  characters are." (Author's warning, verbatim in substance.)

**Why**
- Retargeting across different characters is explicitly approximate in
  this tool. That warning is the single most transferable line in the
  audit for the Aegis rigging gap: any retarget stage needs a stated
  approximation boundary, not a silent promise.

### Phase 5: Layer animation (base layer, panic reset, catalog)

**Do**
1. Create a new rest pose (flat, no animation across the frame range) as
   the start point for new animation on top of imported motion.
2. Use the body/facial animation removal buttons to strip animation from
   body controls, facial controls, or both.
3. Use the panic button to reset the base animation layer to the
   as-imported state (body, face, or both) without rebuilding the
   character.
4. Open the APEX animation catalog for expression presets and hand
   poses (only present if built with those toggles on). Use facial
   expressions as rough blockouts on a brand-new layer: create a new
   rest layer, select a face, apply, step a few frames, repeat.

**Check**
- The catalog pane shows the built expression presets and hand poses;
  the panic reset asks which scope (body, face, both) before acting.

**Why**
- Layers make the imported motion non-destructive: new animation is
  built on top, and the as-imported state is always one button away.
  Expressions as blockouts (not finals) is the author's stated catalog
  discipline.

### Phase 6: Animate the face (sets, puppet, muscle, LookAt)

**Do**
1. Face sets: pick which control set is visible via the face-config gear
   (pink gear icon, or the pink icon in the corner). Default is a curated
   set of 20 to 30 blend shapes; line thickness and alpha are adjustable.
   For a graphical layout, turn on box layout (click a circle, middle-
   click to move it).
2. Face Puppet: enter face-puppet mode, set a pre-roll (author uses
   about 3 seconds), press record (space), move the mouse in the
   viewport (left click winks), press space again to stop. Record to a
   new layer if wanted. Recording settings include record speed
   (half-time available), mouse range, and mouse smoothing.
3. Face Muscle: open the floating window, select facial controls to
   animate by muscle group rather than direct blend shapes ("a more
   natural organic animation"), symmetrical or non-symmetrical, test in
   the window's tester area, then record with the same mechanics as
   Face Puppet.
4. All 200+ blend shapes remain individually keyframeable via the face
   blend-shapes gear for users who want neither tool.
5. LookAt auto-animation: in the eye-config gear, select a target object
   and a frame range (author's example: frames 20 to 250), set the
   transition, bake the LookAt target. Faders control angle limit, body
   weight, and head weight: how much of the body follows the eyes.

**Check**
- In the author's demo, the baked LookAt makes the character start
  following the box around frame 200, with "her entire body and neck
  moving to follow it" until the weights are tuned down.
- The APEX character picker (feet, face, body picking options) selects
  controls for shots where the character is far away and direct viewport
  picking is impractical; it requires the animate state.

**Why**
- Three face tools, one layer system: sets for direct control, puppet
  for performance capture by mouse, muscle for organic grouping, plus a
  constrained auto-animation (LookAt) whose body/head influence is a
  tunable weight, not an all-or-nothing constraint. The author's
  through-line: iClone's face tooling, rebuilt inside Houdini's APEX
  state, so the same muscle memory transfers.

### The human method, distilled

1. **Importer vs Rigger is a real choice**: animate elsewhere, use the
   Importer; animate in Houdini or modify incoming animation, use the
   Rigger. The Rigger does everything the Importer does, plus APEX.
2. **Budget the build**: seconds without APEX, 1-2 minutes with it,
   20-30 seconds back by dropping the facial rig.
3. **Retargeting is an approximation**: say so, and expect ugly
   deformations on very different characters.
4. **Layers before destruction**: new animation on new layers, panic
   reset to as-imported, expressions as blockouts.
5. **Face control is a ladder**: curated sets, then puppet performance,
   then muscle groups, then raw 200+ blend shapes; LookAt weight is a
   fader, not a switch.

### Commenter context

- Commenters are enthusiastic but add no technique (one reports the
  post "saved me at least 100 hours" on a personal project; one asks
  whether mocap data will work inside Houdini without iClone — the
  author replies Houdini has its own mocap tools, separately from APEX).
  The mocap-without-iClone question is open, not answered by the tool.

**Depth status:** FULL (594 caption segments + full description with
chapter timestamps + full post text + comments; no frames reviewed, no
parameters beyond those the author states on camera).

## 3. "A look around my ring world prototype" (k0zakinio, RIDGERUNNERS)

Source: https://v.redd.it/e8zgjaabl3xh1 | r/proceduralgeneration post
1xcxac1 (score 361)

Tools used: undisclosed engine; a curved-space shader over a flat strip
(author's description). Game: RIDGERUNNERS (Steam app 4970370). The map
began as a test map holding every biome for playtesting, then was kept as
its own map variant.

This audit reconstructs the technique from the post text and 29 comments,
step by step. Every phase has Do, Check, and Why. The video's core method
is: do not build the ring; bend flat space with a shader so it reads as
a ring.

### Phase 1: Lay out the flat strip

**Do**
1. Build the world as a flat strip containing every biome (the author's
   original purpose: one playtest map for all biomes).
2. Keep the variant: the author liked how it turned out, so the test map
   became a map in its own right.

**Check**
- The strip reads as a ring from the player's view; the author reports
  the cost honestly: "Took a bit of work keeping it running smoothly
  with so much scenery visible at once!"

**Why**
- A shader illusion is cheaper than ring geometry, but the perf problem
  does not vanish: everything is visible at once, so the culling/LOD
  budget is the real work.

### Phase 2: Bend space in the shader

**Do**
1. Apply the curvature as a shader transformation: the landmass curves
   because the shader says so, not because the geometry is curved.
   (Author, verbatim in substance: "the curvature is all a shader
   illusion".)

**Check**
- Looking up shows the ring continuing overhead; the high FOV makes
  looking up "look a little bit strange" (commenter observation the
  author does not dispute).

**Why**
- The illusion holds exactly where the player only looks. It breaks
  exactly where the game must interact with the world (Phase 3).

### Phase 3: Accept the interaction limits (and the lighting debt)

**Do**
1. Accept that shooting, throwing, teleporting, and collision do not
   agree with the curved positions: a tree that curves up away from the
   player cannot be shot or landed on correctly by flat-space physics.
2. Defer the lighting/shadow problem: "any lighting and shadows would
   need to agree with the curved positions" (author's words).

**Check**
- Commenter-proposed workarounds, not author-confirmed fixes: loop
  positions with modulus arithmetic at two arbitrary edges (with the
  caveat that trajectories need the inverse of the shader's spatial
  transformation, and gravity must still integrate in linear space);
  sync a simple collider with the same curvature (commenter verdict:
  "might be more trouble than it's worth"); place a sun at the ring's
  center so any directional light does the right thing (commenter
  suggestion; the author is "deferring thinking about that").

**Why**
- A rendering illusion and a simulation must agree to be a game. This
  audit's transferable lesson is the shape of the debt: shader-space
  tricks are cheap to render and expensive to make playable, and the
  lighting/shadow agreement is a second, separate debt from the physics
  agreement.

### The human method, distilled

1. **Fake the world, pay in interaction**: curvature as a shader is a
   rendering win and a simulation IOU.
2. **Name the deferred work**: lighting/shadow agreement is explicitly
   deferred, not forgotten.
3. **Playtest maps can become maps**: a biome testbed that reads well
   earns its place as a variant.

**Depth status:** PARTIAL (post text + 29 comments; engine, shader
code, and parameters undisclosed; commenter fixes are proposals, not
author-confirmed).

## 4. "Anything i can do to improve this shot?" (Willing_Touch1157)

Source: https://v.redd.it/8ks144mc72xh1 | r/Houdini post 1xcq4a0
(score 287)

Tools used: **Houdini** + **Nuke** (author's selftext, verbatim). Render
path per author's comments: **Karma XPU** with **MaterialX** ("I couldn't
do it good with karma xpu using material x. Not skilled enough I
guess"). A creature emerges from the ocean beside an offshore-rig
staircase the author added later in the comp because "the water looked
weird" without foreground.

This audit reconstructs the shot's technique from the post text and
comments (the author answers technique questions directly). Every phase
has Do, Check, and Why. The video's core method is: sell the scale of a
creature emerging from the ocean with water behavior, not with the
creature alone.

### Phase 1: Fix the ocean surface spectrum

**Do**
1. Lower the spectrum amplitude and raise the high-frequency detail.
2. Add drifting whitewater/whitecaps; expect turbulent collapse and
   cresting on rising waves at the chosen swell height.

**Check**
- Commenter diagnosis (NineBetween): "The spectrum frequency seems too
  low, and the amplitude too high. With that swell height you'd expect
  more turbulent collapse of rising waves as well as whitewater/
  cresting." A second commenter: the water has "too much detail/noise"
  and the detail "look[s] quite uniform across the whole water surface",
  so break it up.

**Why**
- Scale reads through the water, not the monster: if the swell height
  implies a huge creature, the water must collapse and crest like it.

### Phase 2: Build the emergence (bulge, velocity, foam)

**Do**
1. Start with a bigger bulge of water pushed up before the surface
   breaks, carrying "bow shock" along the creature's surfaces.
2. Add a custom velocity field emphasizing upward movement, plus noise
   to disturb the surface; alternatively a collider purely for
   displacing water, or a pressure-driven increase.
3. Run foam as a separate pass. The author tried the foam node and it
   "looked low res probably because [of] low particle count"; the
   commenter prescription is to do it properly as a separate pass.
4. Slow the water draining off the creature's surfaces: at this scale,
   "a tremendous amount of water" is caught in its deformations during
   emergence.

**Check**
- The shot currently drains too fast and breaks up its turbulent
  forces visibly ("I can literally see S shaped forces as white water
  comes down" — commenter). Break up turbulent forces more; add spray
  breaking up around sharp areas when the wings come out.

**Why**
- Mass is conveyed by water displacement and retention, not by the
  creature's size alone. The author's own fix list adopts all of this
  ("I'll fix everything you mentioned").

### Phase 3: Fix the stepping artifact

**Do**
1. Apply the commenter's stepping fix to the affected particles:
   `@P+=v@v*rand(i@id)*(1/24.0);` (move particles randomly along velocity,
   scaled per-frame at 24 fps).

**Check**
- The artifact is visible in the last frame, screen left: "there is
  visible stepping going on."

**Why**
- A one-line VEX jitter, attributed to a commenter, fixes a
  quantization-looking artifact without re-simming.

### Phase 4: Sell the shot in comp (foreground, anticipation)

**Do**
1. Keep the foreground rig staircase (added later in comp) as the
   scale anchor.
2. Add anticipation for the camera's attention: a flock of birds, a boat
   horn, a shouted "port side", or a ship detection cue — the
   commenter's point is that the videographer's reason to look matters
   as much as the FX.
3. Consider camera shake for a hand-held read, orange underwater glow
   just before surfacing, rivulets on the lens matching wind direction,
   and a slight hand curl as the creature rises so it does not read as
   a static mesh.

**Check**
- Author's responses adopt the notes ("I'm beginning to understand
  material x. Will try to do a better job next time") and confirm the
  staircase's comp origin.

**Why**
- The thread's consensus: the FX is already promising; scale,
  anticipation, and water behavior are what sell it.

### The human method, distilled

1. **Water behavior is the scale cue**, not the creature model.
2. **Foam is a pass, not a toggle**: low particle counts read as low
   resolution, so budget it separately.
3. **Karma XPU + MaterialX is a skill gate**: the author names it as
   the thing they are still learning, not as a solved choice.

**Depth status:** PARTIAL (post text + comments; no node graph,
simulation parameters, or render settings disclosed).

## 5-8. NO-TOOLING audits (evidence only)

- **"Shrimp" (yellowpenmaker, Blender):** "I am pretty new to Blender so
  this took me like 6 hours to make lol." Comments are jokes and praise
  (one YouTube upload exists, "not 6 hours long"). No workflow, no
  settings, no technique. Correctly skipped for adoption.
- **"Procedural cityscape" (deepak365days):** empty selftext, zero
  comments. Nothing to extract; a title is not a technique.
- **"Sculpting Ryu from Street Fighter" (SoulScience1):** "Refining the
  spine muscles on Ryu." One comment (AutoModerator process prompt).
  Sculpt showcase; no tool, software, or settings disclosed.

## Have-vs-need tables

### Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Rigging / skinning / animation-retarget stage | APEX rig (audit 2) | NEED (gap alert, see above) | Inventory: "No rigging / skinning / animation-retarget stage in the foundry" (2026-09-26 audit); fix artifact prepared, not landed | Backlog as design input: use the APEX stage shape (import → rig → animate/modify, 1-2 min build budget, retarget-as-approximation warning) when landing the rigging fix; do not adopt the Houdini HDA itself |
| AI-video character-swap workflow (Reference-to-Video) | MiniMax swap (audit 1) | PARTIAL | Intake/concept generation exists (`intake/`); no video character-swap stage | Watchlist: the workflow is a candidate intake capability, and its two failure modes are acceptance-spec criteria candidates |
| Per-asset perf budgets | Tree generator, ring world (audits 3, 6) | NEED (unchanged) | Inventory NEED; fix artifact prepared with 3 cited anchors only | Watchlist: neither audit supplies citable budget numbers; do not add their qualitative claims to `perf-budgets.md` as anchors |
| Ocean/VFX shot pipeline (Houdini + Nuke + Karma XPU) | Ocean shot (audit 4) | NEED (no attach point) | No VFX shot pipeline in inventory | Watchlist (post-production bucket): Karma XPU reappearance noted, not adoptable into the foundry |
| Shader-curved world shaping | Ring world (audit 3) | NEED (no attach point) | No world-shader stage in inventory | Watchlist: shader-space vs geometry-space tradeoff is the lesson, not the ring itself |

### 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Rigging / production-conversion stage | APEX rig (audit 2) | NEED (unchanged) | Roadmap rec 20 (retopo, UV, rig, LOD, compression); fix artifact prepared, not landed | Watchlist: APEX pattern only; Houdini rigging does not transfer to the Godot 4.7.2 pipeline |
| Art bible / toon law | Blender inverted-hull outline videos (scanned, not analyzed) | NEED (unchanged) | Roadmap rec 2; fix artifact prepared | Carry forward: analyze the inverted-hull outline video next run; it is the most toon-law-relevant candidate in the scan |
| Shader-space world shaping (projection-adjacent) | Ring world (audit 3) | PARTIAL | Projection painting onto fitted geometry exists (`src/projection/`); shader-space curvature is a different trick | Watchlist: the lighting/shadow-agreement debt is directly relevant to projection work (a projected plate must agree with scene lighting the same way) |
| Asset import validation gate | (none today) | NEED (unchanged) | Roadmap rec 9; `qa/asset_validate.py` fix artifact prepared, not landed | No change |
| AI-video character swap | MiniMax swap (audit 1) | NEED (no attach point) | Video-as-asset-source reconstruction exists, but no AI character-swap stage | Watchlist |

### Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Species-rule tree generation (cylinder primitives, low memory) | Tree generator (audit 6) | PARTIAL | `tools/city_trees.py` family exists; species-rule + primitive representation is a technique candidate, not a present stage | Watchlist with a concrete next step: compare the cylinder-primitive representation against the current tree tooling's memory cost before adopting any rule set |
| Shader-driven skyline fill | (none today; ring world is not this) | NEED (unchanged) | PRD 17.1: no equivalent; every building authored or generated | No change; do not conflate the ring-world shader trick with skyline fill |
| Rigging | APEX rig (audit 2) | SKIP by design | PRD 17.1: buildings need no rigging; animated subjects rig only exported clips | Skip with reason stated, not a gap |
| AI-video character swap | MiniMax swap (audit 1) | NEED (no attach point) | No video stage in inventory | Watchlist only |

### Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Rigging stage | APEX rig (audit 2) | HAVE | `tools/asset-pipeline/stages/rig.py`, `assetpipe/blender/rig.py` | No need: Solarempire already rigs. APEX is an alternative approach for a different DCC, not a gap |
| Godot import validation gate + re-measured export budgets | (none today) | NEED (unchanged) | ADR 0003; fix artifact prepared, not landed | No change |
| AI-video character swap | MiniMax swap (audit 1) | NEED (no attach point) | Concept-PNG-as-authority convention only | Watchlist |
| Shader-space world shaping | Ring world (audit 3) | NEED (no attach point) | Pipeline is mesh/GLB-based; no shader-world stage | Watchlist: pattern only |

## Watchlist trending

## Watchlist trending
- AI video generation (Minimax H3, Seedance 2.0 Fast) (first seen 2026-09-27, status WATCH; seen again 2026-09-27, 2026-09-28, 2026-10-02, 2026-10-03, 2026-10-05, 2026-10-08, 2026-10-09, 2026-10-11, 2026-10-16, 2026-10-23, 2026-10-24) **TRENDING**
- SelfLift dual sampling + Color Transfer stitching recipe (MiniMax H3, ComfyUI) (first seen 2026-10-08, status WATCH; seen again 2026-10-11, 2026-10-16, 2026-10-21, 2026-10-24) **TRENDING**
- MiniMax H3 no-masking character-swap LoRA recipe (0.4 MP @ 8 steps, 6GB VRAM) (first seen 2026-10-09, status BACKLOGGED; seen again 2026-10-11, 2026-10-16, 2026-10-24) **TRENDING**
- SyncTile MiniMax H3 single-trajectory long-video nodes (NyckM/Bruxosdovfx-SyncTile-MiniMax-H3-v5.4, v5.5) (first seen 2026-10-23, status BACKLOGGED; seen again 2026-10-24)
- Krea 2 image-to-video in AI music-video stack (first seen 2026-10-23, status WATCH; seen again 2026-10-24)
- Qwen Image Edit 2.1 in AI-video pipelines (first seen 2026-10-23, status WATCH; seen again 2026-10-24)
- Houdini 2D-Pyro-advected particle sim + Karma XPU (first seen 2026-09-30, status WATCH; seen again 2026-10-11, 2026-10-24) **TRENDING**

Correction to the auto-matches above (same handling as the 2026-10-23
run): the SelfLift, no-mask LoRA, and SyncTile rows matched on the
token "MiniMax H3" only. Today's MiniMax audit is a different workflow
(Reference-to-Video character swap + motion transfer), not those three
recipes; those three rows are token-overlap auto-matches, not genuine
reappearances of those recipes. Genuine reappearances today: MiniMax H3
as a general tool (new workflow variant), Krea 2 (now as a character-
reference generator, previously as image-to-video), Qwen Image (now as
a reference generator, previously Qwen Image Edit 2.1 in a pipeline),
and Karma XPU (now in an ocean-shot context, as a skill gate the author
is still learning).

New watchlist rows appended 2026-10-24 (7): Reallusion Rigger HDA;
MiniMax H3 Reference-to-Video character swap + motion transfer; swap
LoRA + facerefine second stage, up to 3 people (commenter claim);
ComfyUI-MAINodes (commenter suggestion); ring-world shader-curvature
illusion; C++ branch-propagation tree generator; Houdini ocean
creature-emergence shot. Full rows in
`references/tooling-watchlist.md` (and mirrored into the
skill_library staging copy).

## Gap recommendations (highest leverage)

1. **APEX stage shape for the Aegis rigging gap (design input, not a
   fill).** Next step: when the `rigging-stage-design.md` fix artifact
   is landed, carry over the APEX stage's stated contract — import →
   rig → animate-from-scratch-or-modify, a build-time budget (seconds
   vs 1-2 minutes, with the facial-rig toggle worth 20-30 seconds), and
   an explicit retarget-as-approximation warning. The gap stays open
   until a trellis-pipe-native stage exists.
2. **Two measurable acceptance criteria for the Aegis intake spec.**
   Next step: add "no smearing in fast motion" and "facial detail
   preserved in wide shots" as candidate pass/fail checks for any
   character-swap take the intake accepts, sourced to the MiniMax swap
   author's own failure report (audit 1). These are criteria, not a
   spec; the spec gap stays open.
3. **Shader-space agreement check for 2d3d projection work.** Next
   step: when projection plates are evaluated, check lighting/shadow
   agreement with the scene the same way the ring-world audit demands
   it (audit 3): a shader-space trick that disagrees with lighting is a
   known-broken take, not a finished one.
4. **Cylinder-primitive tree representation for Desktop City.** Next
   step: measure the current tree tooling's per-tree memory against the
   audit-6 claim ("cylinder primitives, very little memory, forests run
   fine") before adopting any species-rule set; the representation is
   the adoptable part, the rule set is unproven at game scale (the
   commenter instancing caution stands).
5. **Inverted-hull outline for 2d3d toon law (next run).** Next step:
   deep-analyze the Blender Secrets inverted-hull video from today's
   YouTube scan; it is the most direct toon-outline evidence the scout
   has surfaced for the art-bible gap.

## Explicit non-goals (found but correctly skipped)

- Blender beginner shrimp model, Ryu sculpt showcase, empty cityscape
  post: no extractable workflow; correctly skipped, not watchlisted.
- Paw toe-attach tip, quest-giver dialogue text tip, daisies light-
  blocking note: micro-techniques from unscored posts, recorded in the
  "Scanned, not analyzed" section, not watchlisted (below the bar for
  the keep-on-the-side list).
- Blender Secrets tip videos (Mio3 Flex, Booleans to Quads, Edge Flow,
  camera animation, combining cameras, Square to Round, Reduce
  polycount, find double geometry, better bevels): scanned, not
  analyzed under the 8-video cap; the inverted-hull entries are the
  carry-forward, the rest stay unscored.
- YouTube bot-check-blocked videos (4 channels, one video each): not
  attempted further; no cookie workaround exists in this loop.

## skill_library artifacts staged

- New skill `characters/reallusion-rigger-apex-rig` (FULL audit 2).
- New skill `ai-video/minimax-h3-reference-video-character-swap`
  (PARTIAL audit 1; variant of the existing SAM3 character-swap skill,
  different workflow).
- New skill `procgen-worlds/ring-world-shader-curvature` (PARTIAL
  audit 3).
- New skill `simulation-vfx/houdini-ocean-emergence-shot` (PARTIAL
  audit 4).
- New skill `procgen-worlds/branch-propagation-tree-generator`
  (PARTIAL audit 6; variant of the existing recursive-tree-spawner
  skill, different author and generator).
- Full report under `docs/scout-reports/have-vs-need-2026-10-24.md`,
  scout-reports README index updated, watchlist rows synced into the
  staging mirror, skills README grouped table and root README counts
  updated.
