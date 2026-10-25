# Video tooling scout: have-vs-need, 2026-10-25

Depth mode: **pre-approved** (max 2 media downloads). Depth-escalation usage:
**0 downloads attempted, 0 succeeded, 0 skipped.** No download was needed:
the one YouTube video that mattered (the inverted-hull outline) yielded
full captions (142 segments) on the captions-first path, and every native
Reddit clip in this run carries its tooling signal in post text and
comments, where a media download would add nothing. The allowance was not
exhausted; it was simply not required. No approval gate was hit by any
download (none attempted); the only approval-adjacent event was YouTube's
bot check on one Ducky3D video during the channel scan (see below), which
was not retried and no cookie workaround was attempted.

Scan: 11 Reddit video posts across 23 configured subreddits (2-day window
ending 2026-10-25), min_score 20. One warning: threejs returned HTTP 429,
so that subreddit's posts may be missing from this scan. Comment retrieval
worked via Arctic Shift for every analyzed post (no 422s, no PullPush
fallbacks needed). Full selftext was re-fetched from Arctic Shift for the
top posts because the scan output truncates it to snippets; old Reddit
JSON was blocked (HTTP 403) and was not used.

YouTube channel scan: first attempt failed on every channel with an SSL
certificate error (the sandbox egress proxy's CA had rotated again since
the 2026-10-24 fix; the certifi bundle did not contain the current CA).
Fix applied per AGENTS.md: the current Hatch Sandbox Egress CA
(`/usr/local/share/ca-certificates/hatch-egress-ca.crt`) was appended to
the skills venv certifi bundle
(`~/workspace/skills/video-summarizer/.venv/lib/python3.12/site-packages/certifi/cacert.pem`;
pre-change backup at `/tmp/cacert-backup-2026-10-25.pem`, ephemeral).
After the fix the scan completed: 11 channels scanned, 12 videos found in
the 14-day window, 1 warning (Ducky3D: one video, `gb8jdGh_LsE`, blocked
by YouTube's "Sign in to confirm you're not a bot" check; not retried).
The carry-forward from 2026-10-24 (the Blender Secrets inverted-hull
outline video) was found and deeply analyzed as audit 7 below.

## Gap alerts

**No P1 gap alerts today.** Checked against `references/p1-gaps.md` by
keyword and by meaning. Three near-misses, stated plainly so they are not
mistaken for fills:

- Art bible / toon law (2d3d P1): the inverted-hull outline (audit 7) is a
  concrete toon-outline recipe, the most direct toon-law evidence the
  scout has surfaced, but it is one rendering technique, not a written
  art bible (no pillars, palette roles, silhouette rules, or toon-ramp
  law). Recorded as evidence for the gap, not a fill. The gap stays open.
- AI-vendor acceptance spec (aegis P1): the Chain Director audit (audit 4)
  is an orchestration workflow, not a "what good means" spec, but its
  commenter-reported drift failures (earring shape/size/color changing
  mid-scene, mousepad logo swapping, vase shapes changing) are directly
  usable as measurable acceptance criteria for multi-segment AI video
  takes. Recorded under Gap recommendations only.
- Rigging / skinning / animation-retarget (aegis P1): the crowd sim
  (audit 2) required a manual Mixamo fix (re-attaching an arrow to the
  hand) and a clean RBD-to-crowd handoff, but that is a one-off manual
  repair, not an automated rigging/retarget stage. It does not fill the
  gap, and it is not a gap alert. The Reallusion Rigger alert from
  2026-10-24 stands unchanged.
- Per-asset perf budgets (aegis P1): no match. The boids audit (audit 5)
  says "everything is a triangle" and the FLIP audit (audit 6) reports an
  8-hour cache time, but neither states tri counts, texel density, or
  draw calls. Not citable budget numbers.
- Import validation, mesh compression, mesh refinement, skyline fill,
  Godot import gate, MCP DCC loop: no matches in today's tooling.

## Videos deeply analyzed

| # | Video | Creator | URL | Duration | Source |
|---|-------|---------|-----|----------|--------|
| 1 | "I've spent 3 years building a subscription-free compositing app: IllusionFX" | HollywoodIllusion | https://v.redd.it/68xh0vwwh8xh1 | n/a (native clip) | r/vfx post 1xdh0i8 (score 294, 58 comments; 25 retrieved). Depth: PARTIAL (full post text + 25 comments; 5-min walkthrough not retrieved, no captions on native clip) |
| 2 | "100 crowd agents vs archers - sticky arrows, ragdolls and a collapsing floor (Houdini + UE5)" | andrey_krylevskiy | https://v.redd.it/ozc6dy2hy7xh1 | n/a (native clip) | r/Houdini post 1xde3q4 (score 105, 9 comments). Depth: PARTIAL (post text + comments; no solver parameters or node graph) |
| 3 | "Zenith: a physically based lens flare node for Copernicus, beta out today (free for non-commercial use)" | sergioeren | https://v.redd.it/zxtoff3s19xh1 | n/a (native clip) | r/Houdini post 1xdk0ct (score 32, 3 comments). Depth: PARTIAL (full feature spec + comments; no render samples measured, no workflow video breakdown) |
| 4 | "MiniMax H3 Dual Segment has evolved into MiniMax H3 Chain Director V1.0 for ComfyUI" | Far_Patience4517 | https://v.redd.it/0n1g30mzy9xh1 | n/a (native clip) | r/comfyui post 1xdovs4 (score 44, 22 comments). Depth: PARTIAL (full post + comments; workflow file itself not executed, Civitai page not retrieved) |
| 5 | "Surface constrained boids" | RagniLogic | https://v.redd.it/1qyb6hxlqaxh1 | n/a (native clip) | r/proceduralgeneration post 1xdsk1s (score 499, 28 comments; 25 retrieved). Depth: PARTIAL (1-line post + comments; engine, parameters, and surface-constraint method undisclosed) |
| 6 | "FLIP sim with local viscosity changes, and the sparkle is just fake normals" | Liivaan | https://v.redd.it/9r7lijsdg8xh1 | n/a (native clip) | r/Houdini post 1xdgr45 (score 184, 12 comments). Depth: PARTIAL (post text + comments; no solver parameters, viscosity values, or node graph) |
| 7 | "How to do an inverted hull outline and what if it doesn't work?" | Blender Secrets | https://www.youtube.com/watch?v=dybTdt9WXts | 295 s | YouTube, uploaded 2026-10-12, 9,412 views. Depth: FULL (142 caption segments + description; no frames reviewed) |
| 8 | "Procedural cliffs for my map editor inspired by Tiny Glade" | DaedricScimitar | https://v.redd.it/o2nk7vt0l9xh1 | n/a (native clip) | r/proceduralgeneration post 1xdmtwb (score 59, 2 comments). Depth: DEPTH-LIMITED (post text + 2 comments; no code, parameters, or cliff algorithm beyond Voronoi distortion) |

Scanned, not analyzed (8-video cap): "Male Torso anatomy sculpting"
(r/3Dmodeling; teaching sentence only: establish basic forms, tweak
them into shape, then sculpt detail on top, so less tweaking is needed at
high density; 1 comment, AutoModerator only; no tool disclosed;
NO-TOOLING); "Roads, hedgerows and some road signs in my rural UK
inspired voxel terrain generation" (r/proceduralgeneration, score 132,
7 comments; layering system: Perlin Noise + simulated erosion terrain,
river plotting with curves and L-systems, roads with incline costs so
they follow terrain slope; engine undisclosed, no parameters in the
snippet); "Game Changer - Corridor Key 2.0" (r/vfx, score 617, 111
comments, relevance 2.0 because the scan found no tooling keywords; a
new post about the same tool already skilled from the 2026-10-23 run as
`simulation-vfx/corridor-key-2-ai-chroma-keyer`, not re-audited under
the cap); "Forest fire automata" (r/proceduralgeneration; simple test
run, forest growth and fire spreading cascade, no tooling). YouTube
candidates not analyzed (cap): Ryan King Art "How to Make a Three Point
Lighting Setup in Blender" (2026-10-20), the 5-part "Creating a Realistic
Hamburger" Blender tutorial series (2026-10-21 to 2026-10-25), Blender
Secrets "Fix Merged Geometry after Voxel remeshing" (2026-10-17),
"5 Blender tips: Mio3 Flex, Booleans to Quads, Edge Flow, camera
animation and combining cameras" (2026-10-11), "5 Tips: Square to Round
shapes, Inverted Hull, Reduce polycount, find double geometry, better
bevels" (2026-10-15), Josh - Blender Bros "The Most ANNOYING Modeling
Situation in Blender" (2026-10-14) and "Why you get that 'weird'
smearing effect when you shade smooth" (2026-10-19). The second
inverted-hull entry (the 2026-10-15 "5 Tips" video) is a second source
for the same technique, not a new technique; the voxel-remesh fix video
is the carry-forward for mesh-refinement-adjacent work.

## 1. "I've spent 3 years building a subscription-free compositing app: IllusionFX" (HollywoodIllusion)

Source: https://v.redd.it/68xh0vwwh8xh1 | r/vfx post 1xdh0i8 (score 294)

Tools used: **IllusionFX** (hollywoodillusion.com/illusionfx; Windows,
Mac, Linux), **OpenColorIO**, **multi-channel EXR**, **Plugin SDK**
(author's own), **OpenFX** (prototype only, not shipped). Walkthrough:
https://youtu.be/TZd1AifaSyk (linked in the post; not retrieved this
run, so no settings are claimed from it).

This audit reconstructs the tool from the post text and comments, step by
step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies it),
and **Why** (the principle). The video's core method is: build the shot
with nodes, animate it with layers, and never pay a subscription.

### Phase 1: Build the shot with nodes

**Do**
1. Build the comp as a node graph (the author's framing: current tools
   are "expensive, buggy, or free but with a rough workflow").
2. Stack multiple effects inside a single node and reorder them there.

**Check**
- The author, answering the node-vs-layer question directly: "IllusionFX
  is node based, you build your shot with nodes... You can also stack
  multiple effects inside of a node, and change the order etc. But you
  don't build the shot with layers, that's only for the animation part."

**Why**
- Nodes carry the comp structure; layers carry only the animation. The
  split is the product's stated intuitiveness claim, and the author is
  explicit that it is a different approach, not a clone.

### Phase 2: Animate with the layer timeline

**Do**
1. Each node corresponds to a layer in the timeline.
2. Cut, trim, and animate layers with keyframes or expressions.

**Check**
- The timeline behavior is per-node: trimming or keyframing a node
  animates that node's contribution, not a separate layer stack.

**Why**
- One object, two views: the graph is the structure, the timeline is the
  time axis over the same nodes. Nothing is duplicated between them.

### Phase 3: Work in a 32-bit float, color-managed pipeline

**Do**
1. Work GPU-accelerated in a native 32-bit float pipeline.
2. Use OpenColorIO for color management and multi-channel EXR for
   passes.
3. Use the GPU effects: merge, keyer, grain, blur, glow, color
   correction, distortions, and more.

**Check**
- The pipeline claims are the author's feature list; no render or
  performance measurement is offered in the post or the retrieved
  comments, so none is claimed here.

**Why**
- Float + OCIO + EXR is the compositing baseline the tool must meet to
  be taken seriously against Fusion, Natron, and Blender's compositor
  (the three free alternatives a commenter names).

### Phase 4: Use the local AI tools, and know their limits

**Do**
1. Use the built-in AI tools (roto, tracking) that run locally, with no
   cloud processing and no footage upload.
2. Note the hardware split the author states: Nvidia is advised only for
   the AI modules (tracker, auto keyer); any other GPU brand works for
   the rest of the effects.
3. Note what is not yet there: object tracking exists, but camera
   tracking and 3D compositing are "coming soon"; a graph editor and 3D
   compositing are on the roadmap.

**Check**
- Commenter price report (unverified from the vendor page): "129
  euros... when community have fusion, natron, blender." Treat the
  price as a commenter claim, not a vendor fact, until the vendor page
  is checked.
- The author on authorship (the thread's main debate): "I started
  IllusionFX 3 years ago... I know every line of code, and everything
  is technically documented with UML class and sequence diagrams...
  I've used AI occasionally to optimize and debug, and in those cases
  I review and understand everything it suggests." Commenters note the
  author previously demoed this as an After Effects plugin years ago,
  which corroborates the pre-AI timeline; the "vibe coded" dispute
  itself is not a technique and is recorded here only as provenance.

**Why**
- Local AI is the privacy pitch (no footage leaves the machine), and the
  Nvidia-only-for-AI split is the hardware truth that matters for
  adoption: the comp engine itself is GPU-brand-neutral.

### The human method, distilled

1. **Subscription-free is the positioning, not the feature**: the
   feature is node structure plus layer animation over one object.
2. **Local AI, cloud-free**: roto and tracking run on the machine.
3. **Roadmap honesty**: graph editor, camera tracking, and 3D
   compositing are announced as coming, not present.

**Depth status:** PARTIAL (full post text + 25 of 58 comments; the
5-minute walkthrough video and the vendor page were not retrieved, so
no workflow steps, prices, or performance claims beyond the post are
made here).

## 2. "100 crowd agents vs archers - sticky arrows, ragdolls and a collapsing floor (Houdini + UE5)" (andrey_krylevskiy)

Source: https://v.redd.it/ozc6dy2hy7xh1 | r/Houdini post 1xde3q4 (score 105)

Tools used: **Houdini** (crowd sim), **Mixamo** animations, **Unreal
Engine 5** (this version's render), **Karma** (the first version's
render). No crowd solver, agent count tuning, or render settings are
disclosed.

This audit reconstructs the technique from the post text and comments.
Every phase has Do, Check, and Why. The video's core method is: aim
archers at live crowd targets, make every hit physical, and let the
floor take the dead down with it.

### Phase 1: Aim archers at live targets

**Do**
1. Run the crowd sim in Houdini with archers aiming at live targets
   (not pre-baked paths).
2. Fix the Mixamo problem first: Mixamo animations came with the arrow
   in the wrong place, so re-attach the arrow to the hand.

**Check**
- The arrow must ride the hand through the draw and release; a
  mis-placed arrow breaks the shot before any arrow flies.

**Why**
- Library animation is a starting pose, not a finished prop rig: the
  attachment is the author's actual work in this phase.

### Phase 2: Make hits physical (sticky arrows, 1-3 hit deaths)

**Do**
1. Hand the RBD arrow cleanly off to the crowd sim at release.
2. Arrows that hit actually stick in the target.
3. Death after 1 to 3 hits (not a fixed hit count).

**Check**
- A stuck arrow must stay with the agent's motion after impact; a
  death must read as caused by the hits, not by a timer.

**Why**
- The author names the handoff as the hard part ("I had to re-attach
  it to the hand, and then hand off the RBD arrow cleanly to the crowd
  sim"). The handoff, not the arrow model, is the technique.

### Phase 3: Collapse the floor with the ragdolls

**Do**
1. Collapse the floor into the abyss, with ragdolls going down with it.

**Check**
- Ragdolls must fall with the collapsing floor, not hover where the
  floor was.

**Why**
- The collapse is the payoff for the crowd sim: the same agents that
  fought are the debris.

### Phase 4: Render where the iteration is cheap

**Do**
1. First version: render in Karma. This version: render in Unreal.
2. Accept the tradeoff the author states: Unreal lighting "isn't quite
   as good, but I got tired of waiting for renders."

**Check**
- The author is explicit that this is a time tradeoff, not a quality
  claim for Unreal.

**Why**
- Render time is a creative constraint: a crowd shot that cannot be
  iterated is a crowd shot that cannot be finished. The author on
  learning it: "The docs alone weren't enough for me - most of what I
  know came from Crowds for Feature Film courses, plus a lot of trial
  and error and forum digging." A commenter agrees there is still no
  proper crowd course, calling crowds "arguably one of the most useful
  things in Houdini for film/tv."

### The human method, distilled

1. **Fix the library animation first**: re-attach before you simulate.
2. **The handoff is the technique**: RBD arrow to crowd sim, cleanly.
3. **Render where you can iterate**: Karma quality vs Unreal speed,
   chosen for turnaround, not for looks alone.

**Depth status:** PARTIAL (post text + all 9 comments; no solver
parameters, agent setup, or render settings disclosed).

## 3. "Zenith: a physically based lens flare node for Copernicus, beta out today" (sergioeren)

Source: https://v.redd.it/zxtoff3s19xh1 | r/Houdini post 1xdk0ct (score 32)

Tools used: **Zenith** lens flare node for **Copernicus** (Houdini 22.0,
Windows/Linux; beta 0.1.5), **GPU CUDA** (RTX 20-series / Turing or
newer) with CPU fallback, **.zmx Zemax** lens files, **Linear Rec.709
or ACEScg** color. Download/docs: https://sergeneren.com/zenith/
(linked, not retrieved). Open-source implementation of the same paper:
https://github.com/beatreichenbach/realflare (commenter-linked, code
not reviewed this run).

This audit reconstructs the setup from the author's full feature spec.
Every phase has Do, Check, and Why. The video's core method is: ray-trace
a real lens prescription instead of painting sprites, so ghosts get
their shape, color, and position from optics.

### Phase 1: Pick the lens (built-in or your own prescription)

**Do**
1. Choose a built-in lens: 28 mm retrofocus, 50 mm triplet, 50 mm
   double Gauss, 135 mm telephoto, or 300 mm telephoto.
2. Or load your own .zmx Zemax file.

**Check**
- The flare must change when the lens changes: different prescriptions
  give different ghosts, not a reskinned sprite.

**Why**
- The paper (Hullin et al., Physically-Based Real-Time Lens Flare
  Rendering, SIGGRAPH 2011) is the method: every two-bounce ghost is
  followed (light reflects off one lens surface, travels back, reflects
  again before reaching the sensor), and ghost shape, color, and
  position come from dispersion, Fresnel reflectance, and
  anti-reflection coatings.

### Phase 2: Drive the flare from lights that mean something

**Do**
1. Lights from the plate: bright regions of an HDR plate become lights,
   calibrated so each flare carries that region's energy.
2. Or place a manual light, which can follow a LOP or OBJ light (or a
   sun direction) through the camera, so the flare keeps going after
   the sun leaves the frame. The camera is automatically imported from
   the image metadata in a slap comp.

**Check**
- A plate-driven flare must track the plate's bright regions, not a
  fixed sprite position; a scene-driven flare must persist past the
  frame edge while the light is still in the scene.

**Why**
- Energy-calibrated plate lights are what make the flare look like it
  belongs to the plate rather than pasted on it.

### Phase 3: Occlude, starburst, and color correctly

**Do**
1. Occlude the manual light behind objects with a mask or the plate's
   alpha; it fades smoothly as it slips behind an edge.
2. Add the starburst computed from the iris shape, plus a veiling
   glare halo.
3. Choose RGB or full spectral rendering, in Linear Rec.709 or ACEScg.

**Check**
- Occlusion must fade, not pop; the starburst must follow the iris,
   not a generic 4-point sprite.

**Why**
- Smooth occlusion and iris-shaped starburst are the two tells that
  separate an optical flare from a painted one.

### Phase 4: Ship it within the beta's limits

**Do**
1. Run on GPU (CUDA, RTX 20-series/Turing or newer) or fall back to CPU.
2. Non-commercial: free for personal projects and learning, renders up
   to 1920x1080. Commercial: no resolution limit, unlimited render
   nodes.
3. Expect breakage: "It's a beta, so scenes may break between 0.x
   versions."

**Check**
- The author asks for feedback, bug reports, renders, and lens files
  users want working. A commenter points to the open-source realflare
  implementation of the same paper with custom optimizations; the
  author replies it could be wrapped as an HDA for Copernicus too.
  That commenter implementation is a separate tool, not Zenith, and is
  watchlisted separately.

**Why**
- A beta lens tool is adopted for its optics, not its stability: pin
  the version, expect 0.x breakage, and keep the .zmx files.

### The human method, distilled

1. **Optics, not sprites**: ghosts from prescriptions, not paintings.
2. **Lights carry energy**: plate regions calibrated, scene lights
   followed past the frame edge.
3. **Beta discipline**: free tier capped at 1080p, scenes may break.

**Depth status:** PARTIAL (full post spec + all 3 comments; no video
breakdown, render samples, or performance measurements).

## 4. "MiniMax H3 Chain Director V1.0 for ComfyUI" (Far_Patience4517)

Source: https://v.redd.it/0n1g30mzy9xh1 | r/comfyui post 1xdovs4 (score 44)

Tools used: **ComfyUI**, **MiniMax H3** (H3DirectorStudioV1 node),
**ComfyUI-H3-Motion-Context** (0.5.0 or newer required),
**KJNodes** (live preview), **LBH-123-AI Latent Upscaler** (original)
vs **xmarre Latent Upscaler-Plus** variant (compatibility issue, see
Phase 4), **Civitai** workflow download (models/LoRAs not included).
Related node mentioned by a commenter, author-unexamined:
**ComfyUI_MiniMax_H3_Extender** (github.com/tritant/ComfyUI_MiniMax_H3_Extender).

This audit reconstructs the workflow from the post and comments.
Every phase has Do, Check, and Why. The video's core method is: run a
whole multi-segment MiniMax H3 project from one Director panel, with
Motion Context carrying continuity between segments.

### Phase 1: Set the project up in the Director

**Do**
1. Install the Director manually inside `custom_nodes` (it is not
   listed in ComfyUI Manager, per the author).
2. Update ComfyUI-H3-Motion-Context to 0.5.0 or newer (`git pull`
   inside its folder if installed with Git).
3. Do not run two Motion-Context nodes at once: a commenter reports
   NikoDemon80/ComfyUI-H3-Motion-Context conflicts with
   seitanism/ComfyUI-H3-Motion-Context-MultiRef ("If you have both,
   then it cant generate the first clip, because in MultiRef means 0 =
   load the first clip from disc"); removing the MultiRef node fixed it
   for that commenter.
4. Configure duration, aspect ratio, resolution, seed, sampler,
   scheduler, steps, and render mode from the Director panel.

**Check**
- The Director executes as the H3DirectorStudioV1 node; if ComfyUI
  cannot execute it, the Director itself is not installed correctly
  (author's diagnostic).

**Why**
- One panel replaces a fixed two-segment graph: the previous Dual
  Segment workflow is now a mode, not the whole tool.

### Phase 2: Direct Single or Chain segments

**Do**
1. Choose Single (one standalone segment) or Chain (a longer
   multi-segment sequence).
2. Define general prompts shared across the project and independent
   prompts per segment.
3. Let MiniMax H3 Motion Context carry audiovisual context between
   segments to maintain consistent motion, scenes, and transitions.
4. Let automatic context trimming remove repeated transition frames
   before the next segment begins.
5. Enable/disable reference images by number: with 10 images loaded,
   selecting only 3 uses only those 3 (author's explanation of the
   numbered image toggles, answering a commenter's confusion).

**Check**
- Continuity is the thing to verify segment by segment: motion, scene,
  and transitions must carry, not restart.

**Why**
- The Director's value is continuity management (shared prompts plus
  carried context plus trimmed seams), not just launching generations.

### Phase 3: Split BASE and UPSCALE, and preview live

**Do**
1. Run BASE and UPSCALE as independent stages with different models,
   LoRAs, samplers, schedulers, and step counts.
2. Use integrated 3D latent upscaling: a configurable upscale
   multiplier followed by a second sampling pass.
3. Monitor progress and animated previews inside the Director through
   KJNodes.
4. Keep image, video, and audio references connectable, and keep the
   workflow modifiable with other ComfyUI nodes.
5. Export the final video with audio.

**Check**
- The public workflow is sanitized: it contains no private prompts,
  personal references, or model files. Models and LoRAs come from the
  Civitai page's instructions, not the download.

**Why**
- BASE/UPSCALE independence is the quality lever: a cheap base pass
  plus a tuned upscale pass beats one monolithic setting.

### Phase 4: Watch for the three known failure modes

**Do**
1. Check every segment for identity/prop drift: a commenter reports
   "the earring changing shape, sizes, and colours mid scene, the
   mousepad logo swapping like in a kaleidoscope, vases on the right
   shelf changing shapes and sizes." These are the acceptance checks
   for any Chain Director take until the author reports otherwise.
2. Expect the UPSCALE bug if you use the xmarre Latent Upscaler-Plus
   variant: its `MinimaxH3LatentUpscaler3D` node requires an additional
   `keep_proportion` parameter the Director did not pass (it called the
   LBH-123-AI parameter set). The author confirmed it as a
   compatibility issue in V1.0, prepared a patch the same thread, and
   told Git installers to `git pull` in
   `ComfyUI/custom_nodes/ComfyUI-H3-Director-Studio-V1`, restart
   ComfyUI fully, and retry UPSCALE; ZIP installers must replace the
   Director folder and keep only one active copy.
3. Ignore the audio complaints as a workflow signal, not a Director
   bug: commenters call the voice "a pain to ears" and say H3 voice
   audio "sucks"; one suggests generating audio first and cutting to
   it. That is an H3 model limitation, not a Director defect.

**Check**
- Drift is visible in small props first (earring, mousepad logo,
  vases), not in the hero subject. Check props, not just faces.

**Why**
- A director that cannot hold props across segments has not solved
  continuity; it has only automated the generation loop. The drift
  list is the acceptance test.

### The human method, distilled

1. **One panel, two modes**: Single or Chain, same Director.
2. **Continuity is carried, not hoped for**: Motion Context plus
   trimmed seams.
3. **Props are the drift detector**: check the earring before the face.

**Depth status:** PARTIAL (full post text + all 22 comments; the
Civitai workflow file was not downloaded or executed, and no generation
settings beyond the panel list are claimed).

## 5. "Surface constrained boids" (RagniLogic)

Source: https://v.redd.it/1qyb6hxlqaxh1 | r/proceduralgeneration post 1xdsk1s (score 499)

Tools used: undisclosed engine; author's "realtime procedural world
generator." No boid parameters, surface-constraint method, or frame
data disclosed.

This audit reconstructs the technique from the post and comments.
Every phase has Do, Check, and Why. The video's core method is: keep
boids on the terrain surface so a procedural world reads as alive.

### Phase 1: Constrain the flock to the surface

**Do**
1. Add surface-constrained boids to the realtime procedural world
   generator.
2. Let flocks move as herds across the landscape (commenters observe
   "they DO move in herds" and "a flock of deer").

**Check**
- The boids must read as creatures on the land, not as a particle cloud
  floating over it. The author's creatures are named as portmanteaus
  (deirds, elephanirds, dromerdarids, giraffeirds).

**Why**
- Surface constraint is what turns a boid demo into world life: the
  terrain is the stage, and the flock must stay on it.

### Phase 2: Sample only your own flock (for now)

**Do**
1. Currently, sample only the boid's own flock members for the
   simulation (author's words).
2. Plan cross-flock evaluation next: "will add at least avoidance as
   a cross-flock evaluation."

**Check**
- Flocks must not interpenetrate silently once avoidance exists; until
  then, single-flock behavior is the honest scope.

**Why**
- The author's scoping is explicit: own-flock first, cross-flock
  avoidance second. A boid system that claims flock interaction it does
  not have is oversold.

### Phase 3: Note the representation (labeled inference)

**Do**
1. Treat the author's quip as a representation hint, not a spec:
   "Everything is a triangle if you are brave enough."

**Check**
- (Inference, labeled:) the creatures read as low-poly/triangle
  creatures, consistent with a realtime procedural generator, but no
  mesh, triangle count, or renderer is disclosed, so no representation
  claim is made beyond the author's words.

**Why**
- The comment thread's main transferable idea is not boids at all: a
  commenter proposes the system as the core of an ecosystem/Spore-type
  game (per-creature group size, food preferences, health, water,
  emotional profile, temperature, DOTS ECS plus boids), where
  conservation means guiding evolution, not freezing an ecosystem.
  That is a commenter's game idea, not the author's plan; the author
  says "I have yet to find a game idea. Until then just focused on
  world building."

### The human method, distilled

1. **Life first, game later**: world building before a game idea.
2. **Own-flock now, avoidance next**: scope stated, not hidden.
3. **Names carry the joke**: deirds, elephanirds, dromerdarids,
   giraffeirds.

**Depth status:** PARTIAL (1-line post + 25 of 28 comments; no engine,
parameters, or surface-constraint method disclosed).

## 6. "FLIP sim with local viscosity changes, and the sparkle is just fake normals" (Liivaan)

Source: https://v.redd.it/9r7lijsdg8xh1 | r/Houdini post 1xdgr45 (score 184)

Tools used: **Houdini** FLIP sim (author: "a combination of a few
tricks in Houdini"). No solver, viscosity values, particle counts, or
node names disclosed.

This audit reconstructs the technique from the post and comments.
Every phase has Do, Check, and Why. The video's core method is: thicken
the fluid only where the collider moves, and fake the sparkle with
normals instead of geometry.

### Phase 1: Thicken locally where the collider moves

**Do**
1. Wherever the collider moves through the fluid, raise the local
   viscosity so the strokes hold their shape.
2. Let the viscosity relax back to its original value afterward, so
   the surface slowly settles.

**Check**
- Strokes must hold their shape during the pass and settle slowly
  after; a globally thick fluid would never settle, and a globally
  thin fluid would never hold a stroke.

**Why**
- Local viscosity is a time-varying material property, not a solver
  setting: thicken for the gesture, relax for the rest.

### Phase 2: Fake the sparkle with randomized normals

**Do**
1. Add no sparkle geometry.
2. Randomize the normals on the gel, so tiny patches catch the light
   at different angles as it moves.

**Check**
- Commenters confirm the read: "Those sparkles look really nice" and
  "the normals randomisation is genius." The sparkle must move with
  the surface, not sit on it as separate geometry.

**Why**
- A normal perturbation is nearly free compared to sparkle geometry,
  and it moves correctly by construction because it rides the surface.

### Phase 3: Budget the cache

**Do**
1. Budget for a long cache: the author reports "The FLIP sim took
   around 8 hours to cache."

**Check**
- 8 hours is the only performance number in the audit; no particle
  count, hardware, or resolution is disclosed, so no per-particle rate
  is derived from it.

**Why**
- A trick that costs 8 hours to cache is a finishing trick, not an
  iteration trick: run it late, not while blocking the shot.

### The human method, distilled

1. **Viscosity is local and temporary**: thicken for the stroke, relax
   after.
2. **Sparkle is a normal, not a mesh**: randomize, don't model.
3. **Cache time is the budget**: 8 hours means late in the schedule.

**Depth status:** PARTIAL (post text + all 12 comments; no solver
parameters, viscosity values, or node graph).

## 7. "How to do an inverted hull outline and what if it doesn't work?" (Blender Secrets)

Source: https://www.youtube.com/watch?v=dybTdt9WXts | Blender Secrets,
uploaded 2026-10-12, 295 s, 9,412 views. Description: "I made a video
before about making a toon outline shader for both Cycles and Eevee,
and I get a lot of questions about it, so I made it again with a bit
more detail."

Tools used: **Blender** (author says the method still works in Blender
5.2; captions are ASR, so the version is reported as captioned),
**Solidify modifier**, **Emission shader**, **Transparent BSDF**,
**Mix Shader**, **Geometry node (Backfacing)**, **Light Path node (Is
Camera Ray / Ray Length)**, **Gaffer add-on** (HDRI lighting),
**Cycles** and **Eevee**. Demo asset: a head from the Blender asset
pack (multi-res modifier present, collapsed and ignored).

This audit reconstructs the exact workflow from the captions, step by
step, so another agent can follow the same process. Every phase has
three parts: **Do** (the action), **Check** (how the human verifies
it), and **Why** (the principle). The video's core method is: grow a
flipped solidify shell around the mesh, give the shell a black emission
material, and use backfacing plus camera-ray logic to show only the
shell's rim as the outline.

### Phase 1: Set up two materials

**Do**
1. Drag and drop the head asset; scale it up for the demo.
2. Create two materials: a skin material for the character, and an
   outline material.
3. Make the outline material a black Emission shader.
4. Collapse/ignore the existing multi-res modifier.

**Check**
- Two materials exist, in order: skin first, outline second. The order
  matters because the Solidify material offset (Phase 2) counts from
  it.

**Why**
- The outline is a second material on a second shell, not a post
  effect: everything downstream depends on that separation.

### Phase 2: Grow the shell with Solidify (flipped)

**Do**
1. Add a Solidify modifier.
2. Under Normals, click Flip: this flips the thickness, creating the
   outline shell.
3. Under Materials, set Material Offset to 1: this gives the outline
   material to the shell.

**Check**
- With face orientation overlay on, the character looks "very
  embarrassed" (author's words, the flipped shell reads as inverted
  faces); turn face orientation off and switch to rendered preview
  (Cycles in the demo) to judge the real result.

**Why**
- Flip is the whole trick: flipped normals make the shell's faces
  backfacing from the camera, and backfacing is the signal the shader
  chain (Phase 3) keys on.

### Phase 3: Build the outline shader (Transparent + Backfacing mix)

**Do**
1. Open the shader editor and select the outline material.
2. Add a Transparent BSDF (author's warning: "not a translucent BSDF.
   That is something else").
3. Add a Mix Shader (author's warning: "not a mix color node, but a
   mix shader node. It mixes two shaders").
4. Plug the Emission shader and the Transparent BSDF into the Mix
   Shader.
5. Add a Geometry node and plug its Backfacing output into the Mix
   Shader's factor.

**Check**
- The flipped faces from the Solidify modifier create the mix between
  the emission and transparent shaders. At this point, switching to
  Eevee "already kind of works," but Cycles does not yet show the
  outline: that is expected, not a failure (Phase 4 completes it).

**Why**
- Backfacing is the rim detector: where the shell faces away, the mix
  shows emission (the outline); where it faces the camera, it shows
  transparent (nothing). The shell's rim is exactly where that
  transition happens.

### Phase 4: Gate on camera rays (Cycles) and tune thickness

**Do**
1. Switch back to Cycles.
2. Duplicate the Mix Shader (Shift-D) and chain it: the first mix's
   output goes to the second mix's bottom input, the Transparent BSDF
   goes to the second mix's top input.
3. Add a Light Path node and plug Is Camera Ray into the second Mix
   Shader's factor.
4. Switch to material preview for faster feedback and adjust the
   Solidify thickness until it looks right; the author's example value
   is 0.003.
5. Turn on denoise in the render settings.
6. Turn on an HDRI with the Gaffer add-on for scene light.
7. In the Render tab under Film, set it to Transparent for a
   transparent background.

**Check**
- After the Is Camera Ray mix, "we have an outline." If the whole head
  is black, the noodles are plugged wrong: the author names this as
  the most common confusion ("some people, they have the shader set
  up like this and the entire head is black. So, it's really important
  here that you plug it in correctly").

**Why**
- Is Camera Ray restricts the outline to what the camera actually sees
  directly, which is why Cycles needs the second mix that Eevee does
  not: without it, indirect rays would paint the shell everywhere.

### Phase 5: Fix reflections, and check the two failure modes

**Do**
1. Test a mirror: set a mirror object to metallic with roughness 0.
   Observe: "there's no outline in the mirror."
2. Fix it: select the head and replace Is Camera Ray with Ray Length
   as the second mix's factor. The reflection now has an outline.
3. Check transparent shadows: "make sure transparent shadows is not
   turned off, but is turned on."

**Check**
- Mirror test before shipping: outline in the direct view AND in
  reflections, or the fix is not applied.
- Transparent shadows ON, noodles exactly as shown, and the method
  works in Eevee and in Cycles (author's closing claim).

**Why**
- Ray Length generalizes the camera-ray test to reflected rays: a ray
  that has traveled (reflected) still qualifies, so the outline survives
  the mirror. Transparent shadows ON is the second silent killer:
  without it, the shell's shadow logic fights the transparency.

### The human method, distilled

1. **Flip first, shade second**: Solidify Flip plus Material Offset 1
   is the setup; everything else is gating.
2. **Backfacing finds the rim; camera rays confirm it**: two mixes,
   two factors, in that order.
3. **The whole-head-black check**: if the head is black, a noodle is
   wrong, not the method.
4. **Mirrors need Ray Length**: Is Camera Ray alone drops reflections.
5. **Transparent shadows ON**: the setting that silently breaks it.

**Depth status:** FULL (142 caption segments + description; no frames
reviewed, no parameters beyond those the author states on camera;
Blender version reported as captioned by ASR).

## 8. "Procedural cliffs for my map editor inspired by Tiny Glade" (DaedricScimitar)

Source: https://v.redd.it/o2nk7vt0l9xh1 | r/proceduralgeneration post 1xdmtwb (score 59)

Tools used: **Rust/Bevy** (author's game/map editor stack),
**Voronoi distortion** combined with procgen (author's only stated
technique), **Tiny Glade** cliff generation (inspiration, not a tool
used). No cliff algorithm, parameters, or code disclosed.

This audit reconstructs what the author actually states, step by step.
Every phase has Do, Check, and Why. The video's core method is: stop
placing base cliff terrain by hand; generate it from a Voronoi-distorted
procedural method that stays extensible.

### Phase 1: Start from the hand-placement pain

**Do**
1. Build a map editor for a game on Rust/Bevy.
2. Identify the hated manual task: manually placing base cliff terrain.

**Check**
- The author's motive is stated, not assumed: "I hate manually
  placing base cliff terrain and wanted a solution that's extensible."

**Why**
- Extensibility is the requirement, not just automation: a cliff tool
  that cannot grow with the editor is a dead end.

### Phase 2: Follow the Voronoi-distortion trail

**Do**
1. Find a past r/proceduralgeneration thread from 8 months ago (linked
   in the post) and follow its trail into Voronoi distortion combined
   with procgen.
2. Watch Tiny Glade developer interviews for insight (author's verdict:
   "didn't help much but still insightful on a lot of topics").

**Check**
- The author is honest about the evidence level: "I know the video
  isn't a major display of the tooling or even my game, but it was just
  used to demo the tech." A commenter asks whether it will be open
  sourced; the author does not answer in the retrieved comments.

**Why**
- The audit's value is the pointer (Voronoi distortion as the cliff
  shaping idea), not a recipe: no distortion amount, cell size, falloff,
  or meshing step is disclosed, so none is claimed.

### The human method, distilled

1. **Automate the hated task first**: base cliffs before fancy cliffs.
2. **Extensible over clever**: the tool must grow with the editor.
3. **Interviews inspire, threads instruct**: the thread gave the
   trail; the interviews did not give the method.

**Depth status:** DEPTH-LIMITED (post text + 2 comments; no code,
parameters, or cliff algorithm beyond Voronoi distortion; a media
download would add the video's visual cliff shapes but not the missing
algorithm, so no download was attempted under the allowance).

## Have-vs-need tables

### Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Rigging / skinning / animation-retarget stage | Crowd sim Mixamo fix (audit 2) | NEED (unchanged) | Inventory: "No rigging / skinning / animation-retarget stage in the foundry" (2026-09-26 audit); fix artifact prepared, not landed | Watchlist: the manual re-attach + RBD handoff is a repair pattern, not a stage; do not cite it as rig-gap evidence beyond that |
| Per-asset perf budgets | Boids, FLIP cache time (audits 5, 6) | NEED (unchanged) | Inventory NEED; fix artifact prepared with 3 cited anchors only | Watchlist: neither audit supplies citable budget numbers; do not add "everything is a triangle" or "8 hours to cache" to `perf-budgets.md` as anchors |
| AI-video multi-segment orchestration (Director node) | Chain Director (audit 4) | PARTIAL | Intake/concept generation exists (`intake/`); no multi-segment video orchestration stage | Watchlist: the Director pattern (shared prompts + carried context + trimmed seams + independent BASE/UPSCALE) is a candidate intake capability; its drift failures are acceptance-spec criteria candidates |
| Compositing app (node + layer timeline, local AI) | IllusionFX (audit 1) | NEED (no attach point) | No compositing stage in inventory; review flywheel renders multi-view QA, it does not composite | Watchlist (post-production bucket): subscription-free alternative to Fusion/Natron/Blender compositor; not a foundry stage |
| Physically based lens flare (Copernicus) | Zenith (audit 3) | NEED (no attach point) | No Copernicus/flare stage in inventory | Watchlist: optics-first flare is a render-look candidate for cinematics, not a foundry stage |
| FLIP local viscosity + fake-normals sparkle | FLIP sim (audit 6) | NEED (no attach point) | No fluid sim stage in inventory | Watchlist: the local-viscosity trick and normal-randomization sparkle are technique transfers for any future fluid work |
| Toon outline (inverted hull) | Inverted hull (audit 7) | NEED (no attach point) | No toon-outline stage in inventory; UE packaging exists but no outline shader standard | Watchlist: recipe is Blender-side; transferable as a toon-law reference, not as a foundry stage |
| Surface-constrained boids | Boids (audit 5) | NEED (no attach point) | Zone sim has movement/navmesh, but no boid flocking stage | Watchlist: own-flock sampling + planned cross-flock avoidance is a flocking pattern for ambient life, if the zone sim ever needs it |

### 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Art bible / toon law | Inverted hull outline (audit 7) | NEED (unchanged, evidence added) | Roadmap rec 2; fix artifact prepared, not landed | Adopt as evidence: the inverted-hull recipe (Solidify Flip, Material Offset 1, Backfacing mix, Is Camera Ray, 0.003 example thickness, Ray Length mirror fix, transparent shadows ON) is a citable toon-outline standard for the art bible; it is not the bible itself |
| Production-conversion stage | Crowd sim, inverted hull (audits 2, 7) | NEED (unchanged) | Roadmap rec 20 (retopo, UV, rig, LOD, compression); fix artifact prepared, not landed | Watchlist: neither audit is a conversion stage; the Mixamo re-attach is a manual repair, not a pipeline |
| Asset import validation gate | (none today) | NEED (unchanged) | Roadmap rec 9; `qa/asset_validate.py` fix artifact prepared, not landed | No change |
| Procedural cliffs (Voronoi distortion) | Cliffs (audit 8) | PARTIAL | Procedural texture/audio generators exist (`pipeline/proc/`); no terrain/cliff generator | Watchlist: Voronoi distortion is a pointer only (no parameters); do not implement from this audit |
| Surface-constrained boids | Boids (audit 5) | NEED (no attach point) | 2D pixel pipeline; no flocking stage | Watchlist: ambient-life pattern only |
| AI-video Chain Director | Chain Director (audit 4) | NEED (no attach point) | Video-as-asset-source reconstruction exists, but no AI video orchestration | Watchlist |

### Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Shader-driven skyline fill | (none today) | NEED (unchanged) | PRD 17.1: no equivalent; every building authored or generated | No change |
| Procedural cliffs / terrain shaping | Cliffs (audit 8) | PARTIAL | `tools/city_*` family (coast, layering, etc.) exists; no cliff generator | Watchlist: Voronoi-distortion pointer for terrain edges; no parameters to adopt |
| Surface-constrained boids (ambient life) | Boids (audit 5) | NEED (no attach point) | No flocking/ambient-life stage in inventory | Watchlist: flocking pattern for ambient life, if ever wanted; not a city-system need |
| Rigging | Crowd sim (audit 2) | SKIP by design | PRD 17.1: buildings need no rigging; animated subjects rig only exported clips | Skip with reason stated, not a gap |
| Toon outline | Inverted hull (audit 7) | NEED (no attach point) | Blender sprite render path exists (`tools/gen_iso_sprites.py`); no outline shader standard | Watchlist: the inverted-hull recipe could standardize outlined isometric sprites, but Desktop City sprites are rendered, not real-time outlined; evaluate only if outlines enter the sprite contract |
| AI-video Chain Director | Chain Director (audit 4) | NEED (no attach point) | No video stage in inventory | Watchlist only |

### Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Rigging stage | Crowd sim Mixamo fix (audit 2) | HAVE | `tools/asset-pipeline/stages/rig.py`, `assetpipe/blender/rig.py` | No need: Solarempire already rigs; the Mixamo re-attach is a manual repair pattern, not a gap |
| Godot import validation gate + re-measured export budgets | (none today) | NEED (unchanged) | ADR 0003; fix artifact prepared, not landed | No change |
| Toon outline | Inverted hull (audit 7) | NEED (no attach point) | Pipeline is mesh/GLB-based with concept-PNG authority; no outline shader stage | Watchlist: outline recipe is Blender-side; a toon-outline standard would need a GLB-round-trip check before adoption |
| AI-video Chain Director | Chain Director (audit 4) | NEED (no attach point) | Concept-PNG-as-authority convention only | Watchlist |
| FLIP / crowd / boids | Audits 2, 5, 6 | NEED (no attach point) | No sim stages in inventory | Watchlist: patterns only, no adoptable stage |

## Watchlist trending

## Watchlist trending
- YEDP Action Director (ComfyUI 3D viewport; Mixamo/FBX/GLB; OpenPose/Depth/Canny/Normal/Shaded/Alpha passes) (first seen 2026-10-05, status WATCH; seen again 2026-10-16, 2026-10-21, 2026-10-25) **TRENDING**

Correction to the auto-match above (same handling as prior runs): the
YEDP row matched on the token "Mixamo" only. Today's crowd audit uses
Mixamo animations as a library source to be fixed by hand; YEDP itself
was never mentioned. This is a token-overlap auto-match, not a genuine
YEDP reappearance. Genuine reappearances today: none from the
auto-matcher. Genuine new-tool activity (new rows, not reappearances):
IllusionFX, Houdini crowd sim, Zenith, realflare, Chain Director,
surface-constrained boids, FLIP local viscosity, inverted hull outline,
Tiny Glade-inspired cliffs. MiniMax H3 as a general tool reappears with
a new workflow variant (Chain Director), distinct from the SelfLift,
SyncTile, SAM3, no-mask LoRA, and Reference-to-Video variants.

New watchlist rows appended 2026-10-25 (9): IllusionFX; Houdini crowd
sim (archers/ragdolls/collapsing floor); Zenith lens flare; realflare;
MiniMax H3 Chain Director V1.0; surface-constrained boids; FLIP local
viscosity + fake-normals sparkle; Blender inverted hull outline;
Tiny Glade-inspired procedural cliffs. Full rows in
`references/tooling-watchlist.md` (and mirrored into the skill_library
staging copy).

## Gap recommendations (highest leverage)

1. **Inverted-hull outline as the citable toon-law standard for 2d3d's
   art bible.** Next step: when the `ART_BIBLE.md` fix artifact is
   landed, cite the audit-7 recipe verbatim (Solidify Flip, Material
   Offset 1, black Emission, Transparent BSDF + Backfacing mix, Is
   Camera Ray second mix, 0.003 example thickness, Ray Length mirror
   fix, transparent shadows ON) as the outline standard, with the
   whole-head-black diagnostic as its failure mode. The art-bible gap
   stays open until pillars, palette, and silhouette rules exist
   alongside it.
2. **Chain Director drift checks as acceptance criteria for any
   multi-segment AI video take.** Next step: add "no prop drift across
   segments (earring, logos, shelf props hold shape/size/color)" as a
   candidate pass/fail check for the Aegis intake spec, sourced to the
   audit-4 commenter report. These are criteria, not a spec; the spec
   gap stays open.
3. **Zenith/realflare as the optics-first flare reference.** Next step:
   if any repo's cinematics need lens flare, evaluate realflare
   (open source) before buying Zenith's commercial tier, and pin the
   Zenith beta version if it is used (0.x scenes may break).
4. **Local-viscosity + fake-normals as the cheap fluid finishing
   pattern.** Next step: if fluid work ever enters a repo pipeline,
   prototype the audit-6 pair (local viscosity for strokes, randomized
   normals for sparkle) before any geometry-based sparkle or global
   viscosity tuning, and budget cache time explicitly (8 hours in the
   author's case).
5. **Voxel-remesh fix video as the next mesh-refinement lead.** Next
   step: deep-analyze the Blender Secrets "Fix Merged Geometry after
   Voxel remeshing" video from today's YouTube scan; it is the most
   mesh-refinement-adjacent candidate in the scan and could speak to
   the Aegis P1 mesh-refinement gap where today's audits do not.

## Explicit non-goals (found but correctly skipped)

- Male torso sculpt teaching post, forest fire automata test: no
  extractable workflow; correctly skipped, not watchlisted.
- Corridor Key 2.0 new post: same tool as the 2026-10-23 skill, not
  re-audited under the cap; recorded in "Scanned, not analyzed," not
  double-counted as a new tool.
- Roads/hedgerows voxel terrain snippet, Ryan King Art hamburger
  series, three-point lighting, Josh Blender Bros modeling videos:
  scanned, not analyzed under the 8-video cap; the voxel-remesh fix
  video is the carry-forward, the rest stay unscored.
- YouTube bot-check-blocked Ducky3D video and the threejs 429: not
  attempted further; no cookie workaround exists in this loop.
- IllusionFX price (129 euros, commenter claim) and the "vibe coded"
  debate: recorded as unverified/provenance, not as vendor facts.

## skill_library artifacts staged

- New skill `materials-shaders/blender-inverted-hull-outline` (FULL
  audit 7).
- New skill `ai-video/minimax-h3-chain-director` (PARTIAL audit 4;
  variant of the existing MiniMax H3 skills, different workflow:
  Director orchestration, not SelfLift/SyncTile/character-swap).
- New skill `simulation-vfx/houdini-crowd-archers-ragdoll` (PARTIAL
  audit 2).
- New skill `simulation-vfx/zenith-lens-flare-copernicus` (PARTIAL
  audit 3; spec-based, with realflare noted as the open-source
  counterpart).
- New skill `simulation-vfx/flip-local-viscosity-fake-normals`
  (PARTIAL audit 6).
- IllusionFX, boids, and cliffs audits stay in the daily report only:
  IllusionFX is a tool announcement with no executable workflow, boids
  disclose no method, and cliffs disclose no parameters. Never pad thin
  evidence into `skills/`.
- Full report under `docs/scout-reports/have-vs-need-2026-10-25.md`,
  scout-reports README index updated, watchlist rows synced into the
  staging mirror, skills README grouped table and root README counts
  updated.
