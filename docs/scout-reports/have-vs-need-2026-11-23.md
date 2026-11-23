# Video tooling scout: have-vs-need, 2026-11-23

Depth-escalation mode: `pre-approved`, max 2 media downloads per run (Ehsan 2026-09-27). This run: 2 attempted, 0 succeeded, 2 blocked (YouTube bot sign-in wall, see Depth-escalation usage below). No approval gate was hit anywhere in this run. No Whisper model download was attempted (sandbox rule). No live browser was used.

## Gap alerts

Checked against `references/p1-gaps.md` by keyword AND by meaning. **No P1 gap is closed by this run. No automated rigging evidence surfaced.**

1. **AI-vendor generation/acceptance spec (Aegis, P1) — near-hit, practice evidence only.** H3MD 0.6 (audit 6) adds a pre-scan plus one manual check: face tracking and body masks build a cast list, and the operator drags a line from each character picture to the right person, which the author says "is what stops the mix-ups". Keyframes are placed only where the picture needs one, cutting a 38 s five-person clip from 19 keyframes to 10, and a redo rerolls a single keyframe. That is the shape of an acceptance/QC checkpoint, not a written spec artifact, so the gap stays open.
2. **Production-conversion stage for generated meshes (2d3d, P1) — near-hit, claim without stages.** "Sci-Fi Crescent Blade" (audit 1) calls its output a "game-ready asset" made in Blender, ZBrush and Substance Painter, but discloses no retopology, UV, rigging, LOD, or compression step. A game-ready claim with no conversion stages disclosed is not production-conversion evidence. The gap stays open.
3. **Rigging / skinning / animation-retarget (Aegis, P1) — no new evidence, gap NOT filled.** The scan's "rig" keyword hits today are rope simulation (audits 2 and 5), not character rigging. Neither rope post creates, retargets, or skins a character rig. The corrective-bones post from the 2026-11-22 run (1y2122m) reappeared in this window and was already audited yesterday; it adds no new evidence today.
4. **Per-asset performance budgets (Aegis, P1) — absence noted.** No video today states a tri count, texel density, or draw-call budget. In audit 4 a commenter asks "How many polygons are there in this bar?" and the question is unanswered in the retrieved comments. The gap stays open.

No match this run for: automated engine import validation gate, mesh compression + virtual-texture output standard, mesh-refinement stage with deviation metrics, MCP-driven DCC loop, shader-driven skyline fill, Godot import validation gate + export budgets, or a written art bible. Claude Code assistance on the planet generator (audit 7) is agent-written game code, not an MCP-driven DCC loop driving Blender or Unreal, so it is not counted as MCP-DCC evidence.

## Depth-escalation usage

- Downloads attempted: 2 (the run allowance). Downloads succeeded: 0. Downloads blocked/skipped: 2. No download was retried. No approval card or `pending_user_confirmation` was hit.
- Attempt 1: H3MD 0.6 walkthrough (ye7YbiWgzsg, linked from audit 6). `yt_extract.py` returned title and uploader only (no duration, description, or captions). The download attempt failed fast with YouTube's bot sign-in wall ("Sign in to confirm you're not a bot", via the Android player profile). Not retried. Audit 6 rests on the author's full post text plus comments; the walkthrough's on-screen ComfyUI steps were not recovered.
- Attempt 2: UE 5.8 dynamic shield tutorial (JJjrMg3Wj94, r/unrealengine). `yt_extract.py` returned title and uploader only (no duration, description, or captions). The download attempt failed fast the same way (bot sign-in wall). Not retried. The tutorial was not deep-analyzed; no on-screen steps were recovered.
- YouTube scan recovery: the first `scan_youtube.py` run failed all 11 channels with SSL CERTIFICATE_VERIFY_FAILED from the sandbox egress proxy (rotated Hatch egress CA, SHA1 fingerprint C3:B6:CB:FF:87:9F:B8:5E:B7:43:F5:1C:14:8E:61:03:6E:01:B6:20). The current CA from `/usr/local/share/ca-certificates/hatch-egress-ca.crt` was appended to the certifi bundles of both summarizer venvs, the saved CA copy at `~/workspace/custom-skills/local-video-summarizer/.venv/hatch-egress-ca.pem` was refreshed, and the scan was re-run once per the skill: 8 videos found, 1 channel warning (Ducky3D, single-video bot sign-in error). YouTube was not reported as down.

## Videos scanned

- Reddit: 45 video posts in the first scan pass (38 in a second pass; Arctic Shift returned HTTP 429 for different subreddits on each pass: aigamedev and shaders first, then houdini, gameassets, and comfyui), 23 subreddits, last 2 days, minimum score 20 (Arctic Shift API). Ranked by tooling relevance x engagement. Top relevance: Sci-Fi Crescent Blade 52.8, geometry-wrapping rope 50.8, procedural weather 42.9, 3D progress bar 41.0, Super Rope 36.4, Fable office 33.5 (already audited 2026-11-22, see below).
- YouTube: 11 configured channels, 14-day window, minimum duration 240 s (after the CA recovery described under Depth-escalation usage). 8 videos found: 2 Ryan King Art (3D emojis, Darth Maul), 3 Olivio Sarikas (MiniMax H3 Image Normal + GGUF guide, MOSS Image, Imagination Studio), 1 Max Hay (glitch render), 1 Josh / Blender Bros (rendering), 1 Olivio Sarikas (Grokbot). 1 channel warning (Ducky3D, bot sign-in wall on one video). No YouTube video was deep-analyzed in this run: the cap of 8 went to Reddit posts with extractable workflows, MOSS Image and the glitch render were already audited, H3 Image is already covered by multiple skills, and the Grokbot video is off-pipeline (AI assistants for daily life/calendar).
- Deeply analyzed: 8. Scanned but not deeply analyzed: all other posts; see Explicit non-goals. Two posts already audited in the 2026-11-22 run reappeared in the overlapping 2-day window and were NOT re-audited as new: the Fable iPhone-photo office (1y22hpf, audit 6 on 2026-11-22; score 174 now vs 171 then, 21 comments vs 22) and "Experiments with Corrective Bones" (1y2122m, audit 7 on 2026-11-22; score 106 now vs 71 then). No new workflow evidence was taken from either re-scan.

## 1. "Sci-Fi Crescent Blade" (Ghazi197)

Source: https://www.reddit.com/r/blender/comments/1y2xg80/scifi_crescent_blade/ | video https://v.redd.it/fsob2pd5n73i1 | r/blender post 1y2xg80, score 140, 8 comments | Creator: Ghazi197

Tools used: Blender, ZBrush, Substance Painter. Turntable render in Blender. Marmoset (ancient version, previously used for turntables, dropped). No versions, parameters, brush names, or tri counts are stated.

This audit reconstructs the workflow from the author's full post text (433 characters) and all 8 retrieved comments. The video's core method is: build the asset in three DCC tools, then keep the turntable under the same roof as the build. Every phase has Do, Check, and Why.

### Phase 1: Turn a saved concept into a game-ready asset

**Do**
1. Take a blade concept saved in Pinterest inspiration and model/texture it as a "game-ready asset (Blender, ZBrush and Substance Painter)".
2. No step order, sculpt brush, bake setting, or texture resolution is stated. Do not infer one.

**Check**
- The author offers only the finished turntable video as verification. No wireframe, UV, or tri-count check is shown or stated.

**Why**
The author's stated principle is consolidation, not any one tool: "once I started using Blender, keeping most of the work under one roof just made way more sense."

### Phase 2: Render the turntable in Blender

**Do**
1. Render the turntable in Blender instead of Marmoset, which the author "used to do this in" with an "ancient version".
2. No render engine, sample count, lighting rig, or turntable speed is stated.

**Check**
- The turntable itself is the check the author offers: the blade reads from all angles in the clip.

**Why**
Same consolidation principle as Phase 1: one roof for build and presentation, rather than a second tool kept only for turntables.

### The human method, distilled
1. "Super satisfying finally clearing this one off the 'someday' list!" The method on display is finishing a long-saved concept with a familiar three-tool stack, not a new technique. Commenters add no parameters; the most-voted thread content is jokes about the blade's shape ("It's like a reverse Bat'leth").

**Depth status:** DEPTH-LIMITED. Tools named, game-ready claimed, no parameters, no step order, no budgets. A media download would add only the turntable visuals; it would not add the missing workflow parameters, which the author never stated.

## 2. "I added geometry-wrapping rope the player can rappel from and here is how I did it:" (AsyncInvestigations)

Source: https://www.reddit.com/r/godot/comments/1y341pv/i_added_geometrywrapping_rope_the_player_can/ | video https://v.redd.it/9qpntc9s293i1 | r/godot post 1y341pv, score 41, 3 comments | Creator: AsyncInvestigations

Tools used: Godot (version unstated), `Curve3D`, `RayCast3D`, `PhysicsDirectSpaceState3D.get_rest_info()`, capsule colliders synced to `MeshInstance3D`, single `collision_mask` layer, GDScript implied by the Godot API names (the author does not name the language; the API names are Godot's). No Godot version or performance numbers are stated.

This audit reconstructs the exact workflow from the author's full post text (3,804 characters), which is a complete written breakdown. The video's core method is: fake the rope's last segment as a tension-pulling pivot or pendulum, and let physics shape queries, not RigidBody3D motion, decide where the rope wraps. Every phase has Do, Check, and Why.

### Phase 1: Decide against a fully physics-based rope

**Do**
1. Test a fully physics-based rope relying on `RigidBody3D` motion, then reject it.
2. Fake "the last segment of a geometry-wrapped Curve3D as a tension-pulling pivot or pendulum depending on player state" instead.

**Check**
- The deciding test is anchoring against movable objects: the author "wanted the anchor and move-able objects the rope wraps against to remain solid and prevent unexpected jumps in rope length at tension thresholds".

**Why**
"Inference" label: the author does not state a performance reason. The stated reason is determinism of rope length at tension thresholds: freezing everything was the alternative, and the Curve3D + shape-cast route avoids it while keeping anchors solid.

### Phase 2: Anchor with a raycast against the `anchorable` group

**Do**
1. Cast a `RayCast3D` from the player camera to get anything in the group `anchorable`, including physics objects.
2. Start the curve with 2 points: the anchor and the player.

**Check**
- The anchor must be a member of `anchorable`; anything outside the group is not anchorable by this cast.

**Why**
The raycast from the camera makes the anchor the thing the player is looking at, and the group gate is what keeps non-anchor geometry out of the rope system.

### Phase 3: Sync a capsule collider and mesh to every rope segment, every frame

**Do**
1. "Every frame my code counts the rope segments and creates or moves a capsule collider to line up with it."
2. "It simultaneously syncs a `MeshInstance3D` to render the capsule."
3. Put the shapes in the default physics engine on "a single `collision_mask` layer to let the player grab on to and let go of the rope", and reuse the shapes for shape-cast queries.

**Check**
- Collider and visible mesh must line up segment-for-segment each frame; a mismatch would show as the rope rendering somewhere the player cannot grab, or vice versa. The author states the sync, not a numeric tolerance.

**Why**
One shape serves three jobs (collision for the player, rendering, and the shape-cast queries in Phase 4), so the rope's visual, physical, and query representations cannot drift apart.

### Phase 4: Wrap the curve by shape-casting the last segment

**Do**
1. Each frame, take "the adjacency collision shape that's synced to the last rope segment" and run a `PhysicsDirectSpaceState3D.get_rest_info(query)` query.
2. "If it returns a collision with geometry I insert a new path control point offset from said point by the rope radius in the direction of the collision normal."
3. As the player moves around level geometry, "the rope they are attached to cleanly splits so they always have direct line of sight to the pivot".

**Check**
- Line of sight to the pivot is the invariant: the split must preserve a direct line from player to pivot at all times.

**Why**
The author states the purpose directly: "This is important because I'm faking tension by capping player velocity on the axis of the last curve segment." Wrapping is what makes the fake tension axis follow the geometry instead of cutting through it.

### Phase 5: Clamp all non-input forces along the rope axis, and fake the pendulum

**Do**
1. "I only let the player extend or contract the rope with direct input velocity. Any other forces on the player are fully clamped along the rope's axis."
2. Check the unwrapping condition every frame "by shapecasting between the player's harness and the point at `pivotIndex-1`. If its empty, remove the active pivot from the curve and swap the pivot index."
3. "I also check for unwrapping along the length of the rope with the casts debounced to 3 per frame."
4. "Adding a centering force when the player is hanging below the pivot. This acts like a pendulum by taking the `sin` of the angle of the gravity vector and applying it tangent to the pendulum arm."

**Check**
- Unwrap only when the harness-to-`pivotIndex-1` shapecast is empty; the 3-per-frame debounce bounds the unwrap checks along the rope's length.
- The pendulum check is the hanging-below-pivot state; the centering force applies only then.

**Why**
Clamping every non-input force along the axis is what makes the fake tension hold: nothing else is allowed to stretch or slacken the rope except the player's own extend/contract input. The `sin` centering force is the pendulum behaviour, borrowed from the standard pendulum model the author links (Wikipedia, Pendulum (mechanics)).

### The human method, distilled
1. "Godot's static physics state queries make it surprisingly easy." The habit is to query the physics state directly (`get_rest_info`, shape casts) instead of building a physics simulation and fighting it.
2. Fake the one segment that matters (the last, tension-bearing segment) and let queries handle the rest (wrapping, unwrapping).
3. Bound the per-frame work explicitly: unwrap casts "debounced to 3 per frame". No frame-time or rope-count benchmark is stated.
4. A commenter asks the one physics question the post does not answer: "Are the objects touched by the rope affect by physics? I feel like the chair shouldn't be supporting the player's weight." The author did not answer in the retrieved comments. Do not claim the rope moves objects; the post says anchors and movable objects "remain solid".

**Depth status:** FULL. Complete written breakdown with exact API names, group name, debounce count, and the pendulum rule. Missing only: Godot version, rope radius value, frame-time benchmarks, and the answer to the movable-objects question.

## 3. "Procedural weather in my Godot 4 survival game: rain rolls in, and every biome reacts differently" (ErmanStudio)

Source: https://www.reddit.com/r/godot/comments/1y2xi1m/procedural_weather_in_my_godot_4_survival_game/ | video https://v.redd.it/jc4zxh1hs73i1 | r/godot post 1y2xi1m, score 145, 3 comments | Creator: ErmanStudio

Tools used: Godot 4, custom sky shader, `FogVolume` for near-camera clouds, `GPUParticles3D` for rain, global shader parameters shared by grass, trees, and water, "plain GDScript" for all logic. No shader code, parameter names, values, or weather-timing numbers are stated.

This audit reconstructs the workflow from the author's full post text (840 characters) and 3 retrieved comments. The video's core method is: drift weather fronts across the world with the wind, let the biome underneath decide the local response, and drive every responder from one set of global shader parameters. Every phase has Do, Check, and Why.

### Phase 1: Drift weather fronts with the wind

**Do**
1. "Weather fronts drift across the world with the wind."
2. Let "the biome underneath decide what happens": "A swamp gets soaked, a meadow gets rain now and then, and the desert mostly just watches clouds go by."

**Check**
- The check the author offers is legibility from the ground: "looking at the sky to check for rain instead of random events is great" (commenter koorosh-m, score 7). The player reads the front coming, rather than the weather switching.

**Why**
The author's stated complaint about the alternative is immersion: games that "just randomly switch[] the weather" break it. A front the player can see coming is a forecast, not a random event.

### Phase 2: Ramp the transition instead of switching

**Do**
1. "The rain doesn't just switch on, either: the sky slowly gets darker, the wind picks up, and then it starts pouring." Order stated: darker sky, stronger wind, then rain.

**Check**
- Each stage must be visible in sequence in the video: darkening, wind, pour. No durations are stated.

**Why**
"Inference" label: the author does not state a numeric ramp time. The principle stated is the same legibility as Phase 1: a gradual ramp keeps the weather readable as a process arriving, not a state flipping.

### Phase 3: Build the sky, clouds, and rain from four Godot pieces

**Do**
1. "The sky is a custom sky shader."
2. "The clouds near the camera use a `FogVolume` so you can actually fly into them."
3. "The rain is `GPUParticles3D`."
4. "All the logic is plain GDScript."

**Check**
- The FogVolume check is fly-through: the player can fly into a near cloud. No cloud density, particle count, or shader parameter is stated.

**Why**
Each piece does one job in the engine's own terms: shader for the sky, volume for flyable clouds, GPU particles for rain, GDScript for the logic that ties them together. No custom C++ or plugin is claimed.

### Phase 4: Drive grass, trees, and water from global shader parameters

**Do**
1. "Global shader parameters let grass, trees and water all react to the same wind and rain."

**Check**
- All three responders must move/change together with the same front: grass, trees, and water reacting to the same wind and rain values, not three separate weather states.

**Why**
One shared parameter set is what makes the biome response coherent: the swamp, meadow, and desert all read the same front, and differ only in how the biome underneath responds.

### The human method, distilled
1. "Godot made a lot of this really fun to put together." The habit is to compose engine-native pieces (sky shader, FogVolume, GPUParticles3D, global parameters) rather than building a weather engine from scratch.
2. A commenter asks the one unanswered implementation question: "how did you make water react to the player?" The author did not answer in the retrieved comments; the post only says water reacts to the same global wind/rain parameters. Do not claim player-driven water interaction.

**Depth status:** FULL (post-text only). Exact engine pieces and the biome/front/global-parameter architecture are stated; no shader code, parameter names, values, or timings are disclosed. A media download would show the transitions but would not supply the undisclosed shader code or numbers.

## 4. "Timelapse of a custom 3D progress bar – from Blender to Substance Painter to Godot" (EbonCrownGames)

Source: https://www.reddit.com/r/godot/comments/1y2wx71/timelapse_of_a_custom_3d_progress_bar_from/ | video https://v.redd.it/u381mt7yn73i1 | r/godot post 1y2wx71, score 52, 6 comments (8 retrieved, including replies) | Creator: EbonCrownGames

Tools used: Blender, Substance Painter, Godot (all from the title only). No versions, parameters, polygon count, or step detail is stated anywhere in the post or comments.

This audit reconstructs what the title and comments support, and nothing more. The video's core method is, as far as the evidence goes: model in Blender, texture in Substance Painter, use in Godot. Every phase has Do, Check, and Why.

### Phase 1: Blender to Substance Painter to Godot

**Do**
1. Build the custom 3D progress bar in Blender, texture it in Substance Painter, and bring it into Godot. That is the entire pipeline the title states; no step inside any tool is described.

**Check**
- The only check on record is a commenter's unanswered question: "How many polygons are there in this bar?" No answer is retrieved. Do not state a polygon count.

**Why**
No principle is stated by the author. A commenter (Hanodev_) supplies the one design observation: "ya made it 3D but decided NOT to take advantage of the fact it's 3D? I think ya could add some perspective in there" — attributed opinion, not the author's method.

### Phase 2: The open-source alternatives the comments name

**Do**
1. Commenters, not the author, name the alternatives to Substance Painter: Material Maker ("also made with Godot", "not on par with substance painter, but it get the job done", link https://github.com/RodZill4/material-maker), ArmorPaint ("you can compile it yourself or pay one time for binaries"), and Ucupaint ("as a Blender extension").
2. A correction in the thread: "This is not an alternative to substance painter. It's an alternative to substance designer. These two are completely different software." (retardedweabo, about Material Maker.) Material Maker's painting functionality is described as "not that far yet since the focus is heavily on the 'designer' like functionality" (flamelizardcodes).

**Check**
- None of these alternatives is shown used in the video. They are comment recommendations in answer to "Is there any good open source alternative to substance painter?"

**Why**
The thread's principle is cost/licence, not technique: the ask is for an open-source route to the same Painter-class job, and the answers distinguish painting (ArmorPaint, Ucupaint) from designer-class procedural authoring (Material Maker).

### The human method, distilled
1. No author-stated principle survives in the evidence. The auditable content is the three-tool pipeline named in the title plus the comment-thread alternative list.

**Depth status:** DEPTH-LIMITED. Title-only pipeline, empty post text, no author replies in the retrieved comments. A media download would show the timelapse visuals but the author disclosed no parameters to recover; the timelapse format itself (speeded-up screen capture) would not supply them.

## 5. "Super Rope: realistic ropes and chains for Godot (textured ropes, cranes, wrap around, leashes, etc)" (fastdeveloper)

Source: https://www.reddit.com/r/godot/comments/1y31zcz/super_rope_realistic_ropes_and_chains_for_godot/ | video https://v.redd.it/plwf6oi0r83i1 | r/godot post 1y31zcz, score 321, 11 comments (5 retrieved, top-scored) | Creator: fastdeveloper (Alfred Baudisch, per the itch.io/sample links)

Tools used: Godot, Super Rope v1.2.0 (GDScript implementation, per the author's reply), browser-playable samples on itch.io (https://alfredbaudisch.itch.io/super-rope-godot). A C++ GDExtension version is announced, not released. No Godot version, rope parameters, or benchmarks are stated.

This audit reconstructs the product announcement from the author's full post text (416 characters) and the author's replies. The video's core method is a product claim, not a workflow: a GDScript rope plugin with textured ropes, wrapping, tug of war, leashes, and chains, demonstrated in browser samples. Every phase has Do, Check, and Why.

### Phase 1: Ship v1.2.0 with samples

**Do**
1. "Super Rope was released a month ago, and today I released v1.2.0."
2. It "supports textured ropes, wrap around objects, tug of war, leashes, chains, etc."
3. "It has multiple samples which you can play around in the browser" at the itch.io link above.
4. "In the crane sample you can reel in and out, and also attach rigid bodies."

**Check**
- The browser samples are the check the author offers: play them, including on mobile ("open them on mobile. Though they don't have mobile controls, but they play on mobile, thus Super Rope works on mobile", author reply).

**Why**
Samples-first is the author's answer to the cost question: try the behaviour in the browser before buying, rather than trusting a feature list.

### Phase 2: Answer the performance challenge without benchmarks

**Do**
1. A commenter (RossBot5000, score 7) challenges the plugin directly: "How expensive is this to run? You don't include any info about that, and I know ropes can be VERY expensive" and "you state this has been written in GDscript rather than C++ hooking it directly into the physics engine."
2. The author replies that "Super Rope GDScript is much cheaper and way more robust and complete than other rope alternatives" and that "Benchmark info will be released once C++ version is out, it doesn't make sense to release benchmarks now."

**Check**
- No benchmark exists on record today. Do not quote a frame time, rope count, or cost figure for the GDScript version; the author explicitly withholds them.

**Why**
The author's stated reasoning is sequencing: benchmarks for the GDScript version would be superseded by the C++ version, so they wait. Whether that reasoning holds is a buyer judgement, not evidence.

### Phase 3: Announce the C++ GDExtension and the price change

**Do**
1. "Super Rope C++ GDExtension comes out in a month or two, it's already in use in an open-world sandbox and you can have 1000s of simulated ropes/chains. Will be added as a free update for Super Rope itself."
2. "Price by then will be increased by either $19.90 or $29.90, I'm still deciding."
3. The author notes his history: "I've been creating Godot plugins and experiments since 2019 (until 2025 everything was open-source, including the popular 2020s Godello...)".

**Check**
- "1000s of simulated ropes/chains" is an author claim about the unreleased C++ version in one open-world sandbox, with no scene, hardware, or frame-time evidence attached. Treat it as an unverified claim, not a benchmark.

**Why**
The price signal is the actionable part: the increase amount is undecided ($19.90 or $29.90), the C++ version is a free update for existing buyers, and the sandbox use is the only deployment evidence claimed.

### The human method, distilled
1. Ship samples playable in a browser, answer cost challenges by pointing at the samples, and announce the faster version before it exists. The method on display is product marketing with playable evidence, not an implementation workflow.

**Depth status:** DEPTH-LIMITED (product announcement). Features, version, samples, roadmap, and price signal are exact; no rope implementation, parameters, or benchmarks are disclosed, and the author explicitly defers benchmarks. A media download would show the samples, not the implementation.

## 6. "H3MD 0.6: upgraded keyframes let a free open-source ComfyUI tool swap every person in a messy, crowded group video (MiniMax H3)" (ReferenceFluffy6159)

Source: https://www.reddit.com/r/comfyui/comments/1y38u12/h3md_06_upgraded_keyframes_let_a_free_opensource/ | video https://v.redd.it/zd2y7i7wfa3i1 | r/comfyui post 1y38u12, score 50, 4 comments | Creator: ReferenceFluffy6159

Tools used: MiniMax H3, ComfyUI, H3MD 0.6, comfy-h3md-director nodes (AGPL-3.0, https://github.com/1113800942/comfy-h3md-director), H3 Image (paints the keyframes), the included skill (the user's own AI writes keyframe prompts), the Director (renders 2–3 minute videos). Free workflows: https://civitai.com/models/3037225. Full walkthrough: https://youtu.be/ye7YbiWgzsg ("English audio, Chinese audio track and subtitles too"). Captions for the walkthrough were unobtainable in this run (see Depth-escalation usage).

This audit reconstructs the workflow from the author's full post text (1,260 characters) and 4 retrieved comments, and expands the existing `h3md-director-multi-person-swap` skill (H3MD 0.5, 2026-11-19). The video's core method is: rebuild the keyframes so multi-character swap holds on complex scenes, with one manual identity check doing the work that used to need many keyframes. Every phase has Do, Check, and Why.

### Phase 1: Pre-scan and one manual identity check

**Do**
1. "Pre-scan + one manual check. Face tracking and body masks build a cast list; you drag a line from each character picture to the right person (one picture can link to several boxes when someone is half-visible)."
2. This check covers the hard cases the author names: "People cross, block each other, walk in and out of frame and wear almost the same clothes – the kind of clip where swap tools keep putting the wrong face on the wrong person."

**Check**
- The cast list must link every picture to the right person, including half-visible people (one picture to several boxes). The author states the check's purpose directly: "That one check is what stops the mix-ups."

**Why**
Identity by manual link, not by position or by automatic tracking alone: when people cross and wear almost the same clothes, position-based assignment puts the wrong face on the wrong person. One human link per character is the fix, and it is the only manual step claimed.

### Phase 2: Let your own AI write the keyframe prompts; H3 Image paints them

**Do**
1. "Your own AI writes the keyframe prompts with the included skill; H3 Image paints them."
2. No model name for "your own AI" is stated in the 0.6 post. The 0.5 skill names Qwen Image 2.1 for the keyframe step; do not carry that over as a 0.6 fact, since the 0.6 post does not name it.

**Check**
- The painted keyframes are the checkable artifact: each keyframe is a picture the swap must match. No prompt text or keyframe image is reproduced in the post.

**Why**
Prompts are generated, not hand-written per keyframe, and the painting model is H3 Image. The division of labour (AI writes, H3 Image paints) is the author's stated 0.6 design; the skill file is the included prompt-writing aid.

### Phase 3: Place keyframes only where the picture needs one

**Do**
1. "Keyframes only where the picture needs one (start, each cut, someone entering or coming back, people swapping places)."
2. Result on the author's example: "a 38 s five-person clip went from 19 keyframes to 10."

**Check**
- Count the keyframes against the event list: start, each cut, each entry/return, each place-swap. The 19-to-10 reduction is the author's measured result on that one clip, not a general guarantee.

**Why**
Keyframes are placed at identity-risk moments (cuts, entries, returns, swaps), not at a fixed interval. Fewer, better-placed keyframes is the 0.6 claim: the rebuilt keyframe generation is what makes the reduction possible without losing identity.

### Phase 4: Redo one keyframe, or repackage the errors

**Do**
1. "Redo rerolls a single keyframe; for big errors ask your AI for a new package (cached, only the wrong ones rerun)."
2. "The plan imports straight into the Director, which renders 2–3 minute videos."

**Check**
- A single bad keyframe is fixed by rerolling that keyframe alone. Larger errors get a new package, with caching so "only the wrong ones rerun". No rerun counts or times are stated for the repackage path.

**Why**
Localised repair: a single-keyframe failure should not cost a full re-render, and a package failure should not cost re-rendering the correct keyframes. Caching is what makes both repairs cheap.

### Phase 5: Budget the render on an RTX 5090

**Do**
1. Author reply to "How much it takes to render video?": "at 5090 and H3MD 1 sec -> 1 min, short video like under 15 sec usually more fast, around 12 mins, over mins like 2 mins usually take around 120 mins". Read as: roughly 1 minute of render per 1 second of video; a sub-15-second video around 12 minutes; a ~2-minute video around 120 minutes. The author's English is compressed; quote it, do not smooth it into a cleaner claim.
2. A commenter notes the one visible defect in the demo: "Except the weird pop at about 2 seconds in, it looks good!" The author did not reply to that comment in the retrieved thread.

**Check**
- Budget 1 min/sec on a 5090 as the planning figure, and watch the ~2 s mark of the demo for the reported pop. No other hardware figure is stated.

**Why**
Render time is the real cost of the workflow: the keyframe savings in Phase 3 buy identity correctness, not speed. The pop at 2 s is the visible failure mode on record for this demo.

### The human method, distilled
1. One manual identity check, keyframes only at identity-risk moments, single-keyframe redo. The habit is to spend human attention exactly once (the drag-line check) and let the rebuilt keyframe generation carry the rest.
2. The 0.6 change in one sentence, from the author: "We rebuilt and improved how H3MD makes them, so multi-character swap now holds on complex scenes."

**Depth status:** FULL (post-text only, with the walkthrough unviewed). The 0.6 workflow, keyframe counts, render budget, and defect are exact from the post and comments. The walkthrough video (ye7YbiWgzsg) would add the on-screen ComfyUI steps; its captions were unobtainable and its download was attempted under the pre-approved allowance and blocked by YouTube's bot sign-in wall, not retried.

## 7. "Terrain, water and atmosphere done for my procedural planet generator" (El-Jomo)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1y2p5ov/terrain_water_and_atmosphere_done_for_my/ | video https://v.redd.it/sjbzqm0kz53i1 (98 s) | r/proceduralgeneration post 1y2p5ov, score 184, 22 comments (18 retrieved) | Creator: El-Jomo

Tools used: Unity with a "quite custom fork" of the Universal Render Pipeline (URP), CPU-side mesh generation with Burst, Claude Code ("coded with heavy assistance from Claude Code"). No Unity version, Burst job details, heightmap sources, or performance numbers are stated.

This audit reconstructs the architecture from the author's comments (the post text itself is one line: "Video of me flying from orbit to the surface of my procedural planet"). The video's core method is: split the planet into a queryable database and a renderer that queries it, and generate terrain on the CPU per vertex from weighted heightmaps sampled by lat/lon. Every phase has Do, Check, and Why.

### Phase 1: Split the system into a planet database and a renderer

**Do**
1. Build two parts, in the author's words: "The first part is the 'planet database'. It's basically a data provider for everything regarding the planet queried with lat,lon."
2. "The second part is the rendering which queries the planet database."
3. Terrain is the worked example: "The terrain for instance is a CPU side mesh generation (Burst) that fetches the landscape ID for each vertex based on their lat lon and samples the weighted heightmaps it needs to figure out how high that vertex needs to go."

**Check**
- Every vertex must resolve through the same query: lat/lon in, landscape ID out, weighted heightmaps sampled, height out. The author states the query shape, not a correctness test.

**Why**
A database queried by lat/lon decouples "what the planet is" from "how it is drawn": the renderer asks, the database answers, and terrain, water, and atmosphere can all read the same source. "Inference" label: the author does not state this decoupling principle in those words; it is the shape of the two-part design he describes.

### Phase 2: Subdivide an icosahedron around the camera

**Do**
1. "I start with an icosahedron (Townscaper uses a hexagon) and subdivide from there."
2. "The one from Townscaper but subdividing around the camera" — the subdivision follows the camera, with an accompanying image the author links (not read in this run; do not describe its contents).
3. The author adds a design note on coastlines: "I find that it's a good way to build interesting coastlines. Noises always felt too uniform to me." (with a linked coastline image, not read.)

**Check**
- The flythrough from orbit to surface is the check offered: detail must appear as the camera descends, without the whole planet being subdivided at once. No subdivision depth, vertex count, or frame time is stated.

**Why**
Subdividing around the camera concentrates geometry where it is seen. Starting from an icosahedron (rather than a latitude/longitude grid) avoids the pole-pinching a lat/lon grid would carry into the subdivision. "Inference" label: the pole point is not stated by the author; it is the standard reason for an icosphere base, stated here as inference only.

### Phase 3: Keep the game design question open, and the code Claude-assisted

**Do**
1. The author is explicit that the design is unresolved: "It's definitely very 'arcady' right now. I am thinking a lot about the game design challenges of presenting a player with an earth sized planet that they can feasibly explore without it involving a lot of passive gameplay."
2. The code is "coded with heavy assistance from Claude Code".
3. On selling or sharing: "Custom built for my quite custom fork of Unity's Universal Render Pipeline. I'm not interested in the support responsibility that comes with selling a product but I will consider putting in on a public repo."

**Check**
- No repository, asset, or licence is offered today. Do not treat this as an adoptable package; the author has only said he will "consider" a public repo.

**Why**
The author's stated reason for not selling is support responsibility, not secrecy about the method: he describes the architecture freely in comments while declining the product role. The Claude Code note is provenance, not a workflow step: the method described is the author's architecture, built with heavy agent assistance.

### The human method, distilled
1. Query, don't bake: a lat/lon database plus per-vertex sampling, subdivided around the camera.
2. Prefer the interesting coastline over the uniform noise: the author's stated aesthetic judgement against pure noise for coastlines.
3. A commenter (tanepiper) supplies the one comparative performance note: "Very nice and smooth loading... my clouds still look like some 2000's flight sim" on their own project. That is praise of this video's smoothness, not a measured figure for this generator.

**Depth status:** FULL (comment-architecture only). The two-part design, Burst CPU generation, lat/lon query, weighted heightmaps, and icosahedron subdivision are exact from author comments. Missing: Unity/URP fork details, heightmap sources and weights, subdivision depths, vertex counts, frame times, and the linked images (not read). A media download of the 98 s flythrough would show the result, not the undisclosed parameters.

## 8. "I turned my Claude Code sessions into a live Three.js office. Every sub-agent walks in, works at a desk and walks back to report when it's done" (xzinkx)

Source: https://www.reddit.com/r/threejs/comments/1y2ofun/i_turned_my_claude_code_sessions_into_a_live/ | video https://v.redd.it/xdojv5qws53i1 | r/threejs post 1y2ofun, score 20, 24 comments | Creator: xzinkx

Tools used: Claude Code (session logs as the data source), React 19, three.js r170, A* pathfinding, canvas textures, MIT licence, "fully local". Live demo (made-up data): https://zinkxx.github.io/agent-office/. Code: https://github.com/zinkxx/agent-office. No log format, polling interval, or frame-time numbers are stated.

This audit reconstructs the system from the author's full post text (1,175 characters) and author replies in all 24 retrieved comments. The video's core method is: read the logs Claude Code already writes, turn each session and sub-agent into a character in a three.js office, and make status glanceable instead of tab-hopping through terminals. Every phase has Do, Check, and Why.

### Phase 1: Read Claude Code's local logs

**Do**
1. "It reads the local logs Claude Code writes and turns every session into a team lead and every sub-agent into a character that walks in, sits at a role-based desk and reports back when it's done. Idle ones end up on the sofa or the console in the lounge."
2. The system is "fully local". No log path, file format, or read interval is stated.

**Check**
- The mapping must hold for the cases the author names: session to team lead, sub-agent to character, idle to sofa/console. A session waiting on input must be distinguishable at a glance (see Phase 3).

**Why**
The logs already exist; the office is a visualisation over them, not a new agent harness. "Inference" label: the author does not state this "no new harness" principle in those words; it follows from "reads the local logs" plus "fully local".

### Phase 2: Animate low-poly articulated characters with A* and canvas-texture monitors

**Do**
1. "Low-poly articulated characters with animations per activity (typing, reading, walking over to a colleague)."
2. "A* pathfinding so they walk around the desks instead of through them."
3. "The monitors are canvas textures that change with what the agent is doing (code, terminal, search)."
4. "The server rack LEDs blink with the share of busy agents, and the floor LED strip turns yellow when someone is waiting on me."

**Check**
- Pathing must route around desks, not through them; monitors must match the agent's current activity; the floor strip must be yellow exactly when someone waits on the user. A commenter confirms the status encoding independently: "You get a little blue circle on the ones waiting on input. And grey circle when they're working" (romansamurai) — the author's reply does not confirm or deny those colours; treat them as a commenter's observation, not the author's spec.

**Why**
Every visual element encodes one status fact: activity (animation + monitor), busyness share (rack LEDs), waiting-on-user (floor strip). The office is a status board first and a playground second, in the author's own framing: "for me it's mostly a glanceable status board: with 4–5 sessions in different terminals, a character waving at the lead is faster to spot than tabbing through to find which one is waiting on input."

### Phase 3: Throttle rendering so it can stay open all day

**Do**
1. "Rendering slows down when the tab is unfocused and stops when it's hidden, so it can stay open all day." The author repeats the point in a reply: "it has a low-power mode, throttles when the tab isn't focused and stops rendering entirely when it's hidden, so in a background tab it mostly idles."
2. The author concedes the scope limit in the same breath: "if it doesn't fit your workflow, it doesn't... definitely a niche thing, and a fun excuse to build a 3D office".

**Check**
- A hidden tab must stop rendering entirely; an unfocused tab must throttle. No throttle rate or power figure is stated.

**Why**
An always-open status board must cost almost nothing when nobody looks at it. Low-power mode is what makes "stay open all day" viable; without it, the 3D renderer would, in a critic's words the author accepts, "kill your laptop".

### Phase 4: Respect the fan-out shape of real Claude Code work

**Do**
1. The author defends the design against the "two devs on the same project" objection: "in claude code a lot of sub-agents are read-only helpers: an explore agent searching the codebase, a plan agent, a reviewer reading the diff, and they report back to the one session that actually edits. multiple sessions are usually different projects, and each project gets its own room."
2. A second commenter (q_tech_x51) describes a parallel, larger system of their own (virtual HQ, chief of staff, real tool usage, 2D + three.js versions); that is a different person's system, not this project's method, and is not folded into the phases above.

**Check**
- The office must show the actual fan-out: read-only helpers reporting to one editing session, different projects in different rooms. Parallel writers on the same files would be, in the author's words, "a merge conflict factory", and the office does not claim to solve that.

**Why**
The visualisation is honest only if it matches how the sessions actually work: helpers that read, one session that edits, projects kept in separate rooms. The office makes "that fan-out visible", in the author's words.

### The human method, distilled
1. "it's also just a fun three.js playground, which is honestly half the reason it exists". The method is half status board, half playground, and the author is explicit about both halves.
2. Scope honesty as a design habit: "if your flow is one terminal and you read the main session at the end, you honestly don't need it."

**Depth status:** FULL (post-text + author replies). Stack, log source, animation/pathing/monitor/LED encoding, and low-power behaviour are exact. Missing: log format and read interval, A* grid details, character rig details, and any performance numbers. A media download of the short clip would show the office in motion but would not supply the undisclosed log/parsing details.

## Have-vs-need: Aegis (primary)

Repo evidence: `references/aegis-pipeline-inventory.md` (audit 2026-09-26). HAVE only with cited evidence.

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Game-ready asset via Blender/ZBrush/Substance Painter (manual, no stages disclosed) | Audit 1 | NEED | No rigging/skinning/retarget stage; no PBR material import policy or validation gate; production-conversion evidence absent | Skip: manual showcase, no adoptable stage; the P1 production-conversion gap is a different repo's, and this discloses no stages |
| Geometry-wrapping fake-tension rope (Curve3D + shape casts, Godot) | Audit 2 | NEED | Rust zone sim + navmesh/movement exist, but no rope physics or wrap mechanic is listed | Watchlist: pattern transfers as a design (fake last segment, shape-cast wrap, debounce unwrap casts), not as Godot code; Aegis is not a Godot project |
| Super Rope plugin v1.2.0 (GDScript) + C++ GDExtension announced | Audit 5 | NEED | No rope stage in the foundry or sim; benchmarks withheld by the author | Watchlist: wait for the C++ version and its benchmarks before any evaluation; do not buy on the GDScript claim alone |
| Biome-reactive procedural weather (global shader parameters) | Audit 3 | NEED | No weather system listed in the foundry or sim inventories | Watchlist: the global-parameter single-source pattern is the transferable part; no Godot weather code to adopt |
| Blender → Substance Painter → Godot UI pipeline | Audit 4 | PARTIAL | Foundry has UV (xatlas), bake (OptiX), ORM packing, and UE packaging, but no Substance Painter stage or Godot UI asset path | Skip: title-only pipeline; the comment-thread open alternatives (Material Maker, ArmorPaint, Ucupaint) are untested recommendations, watchlist only as licence alternatives |
| H3MD 0.6 multi-person swap keyframes (QC checkpoint pattern) | Audit 6 | PARTIAL | Foundry has automated QA gates + multi-view render QA + blind-review votes, but no AI-vendor acceptance spec (P1) | Backlog (pattern only): the one-manual-check + keyframe-only-where-needed + single-keyframe redo shape is acceptance-spec practice evidence; expand the existing H3MD skill, do not treat as a spec |
| Unity planet database + Burst CPU mesh + icosahedron subdivision | Audit 7 | NEED | No planet-generation stage; deterministic Rust sim + navmesh exist, but no lat/lon database or camera-subdivision terrain | Watchlist: architecture reference only (Unity URP fork, author will not sell/support); do not adopt the fork |
| Claude Code log → three.js office visualisation | Audit 8 | NEED | No agent-session visualisation stage; CI/self-hosted runners exist, but nothing reads agent logs into a status view | Watchlist: pattern for a future fleet/dashboard view (log → character, low-power throttle); not a foundry stage |

## Have-vs-need: 2d3d

Repo evidence: `references/2d3d-pipeline-inventory.md` (Godot 4.7.2, Mobile renderer, Jolt physics; 286 gdUnit4 cases, 198 QA gates).

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Game-ready asset via Blender/ZBrush/Substance Painter | Audit 1 | NEED | Production-conversion stage absent (P1, roadmap rec 20): no retopo/UV/rig/LOD/compression stage disclosed here either | Skip as evidence: the claim adds nothing to the rec-20 design; the stages still need their own design |
| Geometry-wrapping fake-tension rope | Audit 2 | NEED | No rope/traversal mechanic in the inventory; Godot 4.7.2 + Jolt is the same engine family as the post | Backlog: the only directly transferable implementation pattern in this run (Curve3D, `get_rest_info`, debounce 3/frame, pendulum `sin` force); adopt only if a rappel/traversal mechanic enters scope |
| Super Rope plugin v1.2.0 | Audit 5 | NEED | No rope plugin in the inventory; GDScript plugin + itch.io browser samples | Watchlist: evaluate the browser samples against audit 2's hand-rolled pattern if rope enters scope; wait for C++ benchmarks |
| Biome-reactive procedural weather | Audit 3 | NEED | No weather system in the inventory; explore-mode lighting bible pending (roadmap rec 19) | Backlog: the global-shader-parameter pattern fits the lighting-bible work; no shader code was disclosed, so this is a design note, not code to port |
| Blender → Substance Painter → Godot UI pipeline | Audit 4 | PARTIAL | Asset installer with manifest/provenance/acceptance exists (`pipeline/install_asset.py`); no Substance Painter stage | Watchlist: the open alternatives (Material Maker, ArmorPaint, Ucupaint) matter only if Painter licensing becomes a constraint; untested here |
| H3MD 0.6 keyframe QC pattern | Audit 6 | NEED | No AI-video swap stage; QA gates are image/manifest gates, not video-identity gates | Watchlist: QC pattern only; no 2d3d use for multi-person video swap is in scope |
| Unity planet database + Burst terrain | Audit 7 | NEED | Reference-driven reconstruction + projection painting exist, but no lat/lon planet database or Burst mesh generation | Skip: Unity/URP-fork architecture, different engine; the icosahedron-subdivision idea is a watchlist note for any future large-world work, not a 2d3d stage |
| Claude Code log → three.js office | Audit 8 | PARTIAL | Multi-agent dashboard exists in the wider project (per project notes), but no log-to-3D-office visualisation is in the 2d3d inventory | Watchlist: the low-power throttle + glanceable-status pattern is the transferable part for any dashboard work |

## Have-vs-need: Desktop City

Repo evidence: `references/desktop-city-pipeline-inventory.md` (Godot 4.7.2, standalone asset pipeline, PRD v1.5; by design independent of Aegis).

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Game-ready asset via Blender/ZBrush/Substance Painter | Audit 1 | NEED | No retopology/rigging/3D collision imposed on static buildings by design (PRD 17.1); Blender headless sprite render exists | Skip: by-design absence; a sculpted blade pipeline does not serve fixed-view sprites |
| Geometry-wrapping rope | Audit 2 | NEED | No rope mechanic; animated subjects rig only what their exported clips use | Skip: no traversal/rope mechanic in a fixed-view city builder |
| Super Rope plugin | Audit 5 | NEED | No rope stage; same by-design scope as above | Skip: same reason |
| Biome-reactive procedural weather | Audit 3 | PARTIAL | Procedural authoring + QA gates exist; no weather system is listed | Watchlist: biome/front behaviour is a city-ambience idea only; no weather system is in the PRD scope on record |
| Blender → Substance Painter → Godot UI pipeline | Audit 4 | PARTIAL | Headless Blender sprite render + sprite contract exist; no Substance Painter stage | Watchlist: open Painter alternatives are a licence note only; the sprite pipeline already covers the UI-asset path |
| H3MD 0.6 keyframe QC pattern | Audit 6 | NEED | No video-swap stage; AI inputs optional, human approval required (PRD 17.1) | Skip: no video-swap use; the QC-checkpoint shape is a general pattern note only |
| Unity planet database + Burst terrain | Audit 7 | NEED | Shader-driven skyline fill is itself a P1 gap with no equivalent; every building is authored/generated | Skip: planet-scale architecture does not serve the skyline-fill gap; do not conflate the two |
| Claude Code log → three.js office | Audit 8 | NEED | No agent-session visualisation; self-hosted CI runner exists | Watchlist: status-board pattern only; no dashboard stage is in the PRD scope on record |

## Have-vs-need: Solarempire

Repo evidence: `references/solarempire-pipeline-inventory.md` (Godot 4.7.x native client direction, ADR 0016; asset pipeline with retopo, rig, UV, bake, LODs; rigging stage present).

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Game-ready asset via Blender/ZBrush/Substance Painter | Audit 1 | PARTIAL | Pipeline stages audit → prepare → segment → retopo → rig → UV → bake → LODs → export exist, unlike Aegis; no ZBrush/Substance Painter stage is listed | Skip: the pipeline already covers conversion; this post discloses no stage to borrow |
| Geometry-wrapping rope | Audit 2 | NEED | No rope mechanic in the pipeline or oracle client | Skip: no rope use in a space-empire asset pipeline on record |
| Super Rope plugin | Audit 5 | NEED | No rope plugin; rig stage is for characters/ships, not ropes | Skip: same reason |
| Biome-reactive procedural weather | Audit 3 | NEED | No weather system; export budgets are oracle budgets pending re-measurement (ADR 0003) | Watchlist: global-parameter coherence is a design note for any future atmosphere work; no code disclosed |
| Blender → Substance Painter → Godot UI pipeline | Audit 4 | PARTIAL | Concept PNG is visual authority; Meshy GLB is bake source; Godot import validation gate absent (P1, nothing to validate into yet) | Skip: title-only; the P1 import gate is not filled by a pipeline name |
| H3MD 0.6 keyframe QC pattern | Audit 6 | NEED | No AI-video stage; no AI-vendor acceptance spec beyond concept-PNG-as-authority | Watchlist: QC pattern only |
| Unity planet database + Burst terrain | Audit 7 | PARTIAL | Deterministic topology via VDBs + math is documented; per-asset audit reports with measured figures exist | Watchlist: the lat/lon database + camera-subdivision architecture is the closest analogue to the VDB/math topology work, but in a different engine (Unity URP fork) and at planet scale; architecture reference only |
| Claude Code log → three.js office | Audit 8 | NEED | No agent-session visualisation in the pipeline | Watchlist: status-board pattern only |

## Watchlist trending

`bin/trend_watchlist.py` was run with the single specific tool name "H3MD 0.6 multi-person character swap" (generic inputs such as "Blender", "ComfyUI", and "Godot" were deliberately NOT fed to the script: a first pass with those generics token-matched ~120 rows, and that pass was reverted in full before any of its annotations survived). The script's snippet for the targeted run, verbatim:

## Watchlist trending
- comfyui-minimax-h3-studio (BiggerFishy; SAM3 + color-inversion character-swap workflow, MIT) (first seen 2026-10-03, status BACKLOGGED; seen again 2026-10-09, 2026-10-16, 2026-10-21, 2026-10-29, 2026-10-31, 2026-11-03, 2026-11-11, 2026-11-12, 2026-11-23) **TRENDING**
- MiniMax H3 no-masking character-swap LoRA recipe (0.4 MP @ 8 steps, 6GB VRAM) (first seen 2026-10-09, status BACKLOGGED; seen again 2026-10-11, 2026-10-16, 2026-10-24, 2026-10-29, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-08, 2026-11-12, 2026-11-14, 2026-11-19, 2026-11-23) **TRENDING**
- MiniMax H3 Reference-to-Video character swap + motion transfer (ComfyUI, local RTX 5070 Ti) (first seen 2026-10-24, status WATCH; seen again 2026-10-29, 2026-10-31, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-08, 2026-11-12, 2026-11-14, 2026-11-17, 2026-11-19, 2026-11-23) **TRENDING**
- H3MD 0.5 multi-person character swap (MiniMax H3 + ComfyUI, up to 5 people, 100% local) (first seen 2026-11-19, status BACKLOGGED; seen again 2026-11-23)

**Verification (manual, against the audits above):** only the fourth line is a genuine reappearance. The first three are token-overlap false matches on "character swap": H3MD 0.6 uses neither the SAM3 color-inversion workflow, nor a character-swap LoRA, nor the Ref2V workflow. Each of those three rows was annotated in `references/tooling-watchlist.md` as a false match, following the file's established practice. Genuine reappearances today, annotated manually (not by the script): **H3MD 0.5 → 0.6** (audit 6, same author and tool, rebuilt keyframes) and **MiniMax H3 Image** (audit 6, H3 Image paints the 0.6 keyframes). Re-scans with no new evidence, annotated as such: the Fable iPhone-photo row and the corrective-bones row (same Reddit posts, overlapping window), and the MOSS-Image and glitch-render rows (same YouTube videos in the channel scan). Not genuine, and not annotated: the hand-painted stylized character texturing row (audit 1 names Substance Painter + ZBrush but discloses no Arnold/toon hand-painted workflow), the ComfyUI intake-wrapping row (today's ComfyUI use is H3MD/H3, not intake wrapping), the MCP-DCC rows (no MCP tooling in today's videos), and the Godot .NET creature-pipeline row (Godot + Claude Code overlap only).

**New watchlist rows appended 2026-11-23:** Godot geometry-wrapping fake-tension rappel rope; Super Rope Godot plugin v1.2.0; Godot biome-reactive procedural weather; Unity planet database + Burst CPU mesh + icosahedron subdivision; Claude Code agent-office three.js visualisation; open-source Substance Painter alternatives (Material Maker / ArmorPaint / Ucupaint, comment recommendations).

## Gap recommendations

1. **Expand the H3MD skill with the 0.6 keyframe rebuild (adopt now, skill work).** The one-manual-check + keyframes-only-at-risk-moments + single-keyframe redo pattern is the strongest acceptance/QC practice in this run, and the existing `h3md-director-multi-person-swap` skill is the 0.5 version of the same tool. Next step: expand that skill with Phase 1–5 of audit 6, including the 19→10 keyframe count, the 1 min/sec RTX 5090 budget, and the 2 s pop defect. This does not close the P1 acceptance-spec gap; it records the practice.
2. **New skill: Godot geometry-wrapping rappel rope (backlog).** Audit 2 is the only FULL implementation breakdown in this run with exact API names and a debounce bound. Next step: publish `godot-geometry-wrapping-rappel-rope` in `engine-runtime`, and revisit it only if a rappel/traversal mechanic enters 2d3d scope. Do not present it as rigging-gap evidence.
3. **New skill: Godot biome-reactive procedural weather (backlog).** Audit 3's global-shader-parameter architecture is the transferable design for 2d3d's pending lighting-bible work. Next step: publish `godot-biome-reactive-procedural-weather` in `engine-runtime` with the missing-code caveat (no shader code disclosed). No adoption until a weather system is scoped.
4. **New variant skill: Unity planet database + Burst terrain (watchlist).** Audit 7 is a different planet method from Exolune (CPU/Burst database query vs GPU per-point evaluation). Next step: publish `unity-planet-database-burst-terrain` in `procgen-worlds`, cross-linked to `exolune-planet-engine`, with the author's no-sale / repo-only-considered status stated. No adoption: Unity URP fork, planet scale, no package offered.
5. **New skill: Claude Code agent-office visualisation (watchlist).** Audit 8's log → character + low-power throttle pattern is the most concrete multi-agent status-board design seen in the scout. Next step: publish `claude-code-agent-office-threejs` in `automation`. No adoption until a dashboard need is scoped; the author's own scope limit ("if your flow is one terminal... you honestly don't need it") travels with the skill.

## Explicit non-goals

Tools and posts found but correctly skipped, with reasons:

- Houdini procedural thruster flight control (1y2qzc4, "Instead of keyframing a flying Tesla..."): showcase with a 1,089-character post naming Houdini + Redshift and 10 thrusters, no node names, solver settings, or parameters, and an offered breakdown that was never given. Not deep-analyzed; the cap went to posts with extractable workflows. Watchlist: none added; a future breakdown post would be a new audit.
- UE 5.8 dynamic shield tutorial (JJjrMg3Wj94, r/unrealengine): full-tutorial YouTube video, 1 Reddit comment (praise only), captions unobtainable via extraction (see Depth-escalation usage). Not deep-analyzed; no on-screen steps were recovered. No tool beyond Unreal 5.8 is named in the evidence.
- Slay the Spire 2 hooks/template pattern video (Vjn3LLcnATU, r/godot): programming-pattern talk, not an asset/tooling pipeline; relevance 15.3 on a "rig" keyword hit only. Not deep-analyzed.
- Procedural stylized water via Geometry Nodes (1y3duuw, r/blender): empty post text, zero retrievable comments (Arctic Shift 422), title only. Not deep-analyzed; no node names or parameters exist in the evidence.
- Corrective Bones (1y2122m) and Fable office (1y22hpf): already audited 2026-11-22; re-scans, not new audits (see Videos scanned).
- All remaining scanned posts (showcases, sim clips, and game-progress videos with no tooling disclosure): no workflow, parameters, or tool names beyond the engine named in the title. No watchlist rows were created from title-only mentions.
- No skill was made for the DEPTH-LIMITED audits 1, 4, and 5: thin evidence must not be padded into `skills/`, per the skill's depth rule.

## skill_library artifacts

Staged in `~/workspace/video-tooling-scout-public/` for the standing pre-approved push:

- New skill: `skills/engine-runtime/godot-geometry-wrapping-rappel-rope/SKILL.md` (audit 2).
- New skill: `skills/engine-runtime/godot-biome-reactive-procedural-weather/SKILL.md` (audit 3).
- New skill: `skills/procgen-worlds/unity-planet-database-burst-terrain/SKILL.md` (audit 7, cross-linked to `exolune-planet-engine`).
- New skill: `skills/automation/claude-code-agent-office-threejs/SKILL.md` (audit 8).
- Expanded skill: `skills/ai-video/h3md-director-multi-person-swap/SKILL.md` (audit 6, H3MD 0.6 phases, render budget, and 2 s pop failure mode added; 0.5 phases retained).
- Full report: `docs/scout-reports/have-vs-need-2026-11-23.md`, with `docs/scout-reports/README.md` index updated.
- Watchlist: 6 new rows appended to `references/tooling-watchlist.md`, synced into the repo mirror at `video-tooling-scout/references/tooling-watchlist.md`; H3MD 0.6 / H3 Image genuine reappearances and false-match corrections annotated in place.
- README: 4 new rows added to the grouped table in `skills/README.md`; root README skill count updated from 286 to 290 (procgen-worlds 49→50, engine-runtime 65→67, automation 40→41), category counts verified against the staged directories. No chronological prose added to the root README.
- No skill was made for the DEPTH-LIMITED audits 1, 4, and 5 (thin evidence, per the depth rule).
