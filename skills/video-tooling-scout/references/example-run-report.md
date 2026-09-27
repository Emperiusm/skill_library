# Video tooling scout: full-depth run report (SAMPLE)

**What this is:** a real `video-tooling-scout` run (2026-09-27), sanitized:
project and operator names genericized, nothing else changed. It shows the
full output contract: gap alerts first, per-inventory have-vs-need tables,
watchlist trending, non-goals, then a full-depth workflow audit for every
audited video. **Depth benchmark:** every audited video is reconstructed as
source line, tools used, phased Do / Check / Why, exact parameters where the
source gives them, and distilled principles. **24 unique videos/posts**
audited. Method: captions/metadata only, zero downloads, zero approval
prompts. Anything inferred is marked [inference]. Videos without captions
are marked DEPTH-LIMITED.

## Gap alerts (P1/P2)

No new P1/P2 gap matches in the latest (v3) window. Standing gaps, unchanged:

1. **Per-asset performance budgets + automated UE import validation (P1).**
   Procedural/shader/LOD-heavy content lands in-engine unchecked; no import
   validation gate exists.
2. **Rigging / retargeting stage in the asset pipeline (P1).** Every asset
   that should move is stuck static. Concrete step: `runtime/rig` stage
   (auto-rig + retarget) before UE packaging.
3. **AI-vendor generation/acceptance spec (P1).** the intake stage needs a written
   "what good means" per asset type before the next model swap.
4. **Mesh compression + virtual-texture standard for pipeline output (P1).**
   The Cave Expedition devlog (video #3 below) is the copyable recipe:
   8-bit UVs, octahedron normals, 3-integer vertices, patch-grid UVs.
   **Caution:** the devlog's captions were unavailable for this deep audit
   (YouTube rate-limit), so its specific numbers are unverified, and the
   trailing numbers quoted in the 2026-09-27 rerun report (waterfall source
   4.7 units, particle separation 0.04, voxel scale 0.75) were identified as
   contamination from the unrelated Cinematic Cavern video and have been
   quarantined. The recipe direction stands; the exact constants do not
   until captions or a download (the operator's explicit approval) confirm them.
5. **Mesh-refinement stage with deviation metrics, Planer-class (P1).**
   Flatten, sharpen, report deviation, preserve UVs; slots between `weld`
   and `qa`.
6. **MCP-driven DCC loop (P2).** Agents driving Blender/UE directly, plus the
   inverse (agent consuming a game to produce a cinematic). Concrete step:
   spike a Blender MCP behind the review stage.
7. **Deterministic-vs-learned evaluation harness (P2).** "Fake player" eval:
   deterministic scripts vs RL policy, reproducible via the deterministic core.
8. **ComfyUI interop for intake/ (P2).** Expose intake stages as ComfyUI
   custom nodes; the `@comfyorg` pattern proves vendors do this.

## Have-vs-need per repo (consolidated across all runs)

### Example pipeline A (Blender + Godot indie project)

| Tool / stage | Found in video | Status | Recommendation |
|---|---|---|---|
| Mesh compression recipe (8-bit UVs, octahedron normals, 3-int vertices) | #3 Cave Expedition | NEED | **Backlog (P1).** Adopt as asset-pipeline output standard; answers the perf-budget gap |
| Virtual texturing + GPU feedback rendering | #3 | NEED | **Backlog, same ticket.** Only if scenes get large |
| Rigging / skinning / animation retarget | #7 model revival | NEED | **Adopt now (P1).** Second independent signal for the audit gap |
| MCP servers driving Blender/Unreal (agentic DCC) | n/a | NEED | **Adopt (P2).** Blender MCP spike behind review stage |
| Agentic cinematic from game source | #16 Claude trailer | PARTIAL | **Backlog (P2-adjacent).** Trailer generation as review-stage artifact |
| Obi Physics (particle-based, SDF collision) | #3 | NEED | **Watchlist.** Proven rope/ragdoll pattern for gameplay modules |
| SPH fracture/contact modeling (Autodyn-class) | #23 armor sim | NEED | **Watchlist.** Only if destruction sim enters scope |
| Squishy Volumes (Blender MPM soft-body) | #17 | NEED | **Watchlist.** Free; fracture upcoming |
| ComfyUI custom nodes / Minimax H3 via `@comfyorg` | #1 RESISTANCE | NEED | **Watchlist.** Expose intake stages as custom nodes |
| AI video generation (Minimax H3, Seedance 2 Fast) | #1 | NEED | **Watchlist.** Trailers/marketing only |
| AI image edit/gen feeding pipeline (Nano Banana class) | #1 | PARTIAL | **Backlog.** Define intake's image stage as model-swappable |
| LLM in creative loop (ChatGPT concept/script) | #1 | PARTIAL | **Backlog.** Extend lore-tool pattern to visual concepts |
| Houdini Engine queued SaaS pattern | #12 jewelry | NEED | **Watchlist.** $525/head/yr licensing is the constraint |
| Procedural construction shader (blueprint + rim + reverse erosion) | #5 | NEED | **Backlog.** UE material functions first (also relevant to construction animations) |
| Shader-driven skyline fill | #9 | NEED | **Watchlist.** Authored-vs-shader per district in art bible |
| Deterministic topology via VDBs + math | #12 | HAVE | Validation, no action |
| LOD generation | #8 Minecraft | HAVE | Keep; texture-LOD-from-seed is PARTIAL → watchlist |
| Deterministic behavioral scripts beating learned policies | #6 RO engine | HAVE | Adopt the *validation*: fake-player eval harness as an AI-service milestone |
| Procedural ribbon cables (Blender GeoNodes) | #20 | PARTIAL | **Watchlist.** Prop-detail stage if ever needed |
| Leather-patch Substance generator | #21 | NEED | Same as material-acceptance-spec gap: define "good material" first |
| Procedural material authoring (Substance-class) | #14, #15 | NEED | **Backlog.** Pairs with AI-vendor acceptance spec |
| Intelligent frame extraction (quality scoring, overlap warnings) | #11 | NEED | **Backlog.** Front door if intake ever accepts video |
| Gaussian Splatting as representation | #11 comments | NEED | **Watchlist.** Fast preview before mesh commit |
| SAM background removal | #11 comments | NEED | **Watchlist.** Phone-scan cleanup before intake |
| Light Wrangler gobos (Blender) | #18 | PARTIAL | **Watchlist.** Minor; only if render-look work grows |
| Non-manifold fix for surface-nets | #3 | PARTIAL | **Watchlist.** Only if voxel meshing enters the pipeline |
| Compute-shader tessellation | #3 | NEED | **Watchlist.** UE5 Nanite covers client side |
| Tideglass target-driven GPU fluid | #22 | n/a | **Skip.** Cinematics-only, not asset tooling |
| Weta bubbles solver in Houdini | #13 | n/a | **Skip.** Cinematics-only, not asset tooling |
| NLE / edit / grade (Da Vinci Resolve 21) | #1 | n/a | **Skip.** Human editing tool |
| Browser-based procedural delivery | #10 | n/a | **Skip.** Different project's lane |

### Example pipeline B (2D project)

| Tool / stage | Found in video | Status | Recommendation |
|---|---|---|---|
| Rigging / retargeting | #7 | NEED | adopt: character form-swap systems will need retargets |
| Mesh compression standard | #3 | NEED | watch: relevant when 3D segments ship |
| Agentic cinematic from game source | #16 | PARTIAL | backlog: trailer artifact for the slice |
| Deterministic scripts vs RL | #6 | HAVE | validation of deterministic-core instinct |
| Everything else above | n/a |, | skip: no fit for a 2D project |

### Example pipeline C (city-builder)

| Tool / stage | Found in video | Status | Recommendation |
|---|---|---|---|
| Procedural construction shader | #5 | NEED | **Backlog.** Construction animation for buildings |
| Shader-driven skyline fill | #9 | NEED | **Watchlist.** Directly relevant to skyline scale |
| Houdini Engine SaaS | #12 | NEED | skip: project deliberately engine-independent |
| SPH fracture | #23 | NEED | skip: static buildings, no destruction in scope |

### Example pipeline D (strategy game)

| Tool / stage | Found in video | Status | Recommendation |
|---|---|---|---|
| SPH fracture/contact modeling | #23 | NEED | **Watchlist.** Conceivable for battle-damage later |
| Mesh compression standard | #3 | NEED | **Watchlist.** Fleet-scale scenes |
| Houdini Engine SaaS | #12 | NEED | skip: engine-neutral Python+Blender pipeline |

## Watchlist trending

- Houdini Engine queued SaaS pattern (seen again 2026-09-27 (WATCH)
- AI video generation (Minimax H3, Seedance 2 Fast) (seen again 2026-09-27 (WATCH)
- ComfyUI custom nodes wrapping intake/ stages (seen again 2026-09-27 (WATCH)
- Agentic cinematic from game source (seen again 2026-09-27 (BACKLOGGED)
- Obi Physics (particle-based, SDF collision) (seen again 2026-09-27 (WATCH)
- SPH fracture/contact modeling (Ansys Autodyn-class) (new 2026-09-27 (WATCH)

## Non-goals (audited, no tooling signal)

- "The reason I love RO. 1st WOE in Ragnarok Zero Global", gameplay footage.
- "Looking for advice on topology / rendering. Any tips?", beginner Q&A.
- "Similar attract, Opposites repel" / "Stair climbing simulation" /
  "1,000 balls dropped into a halfpipe", pure sim eye-candy.
- "Adding DRUG power ups to my Hotline Miami boomer shooter" / "Greywatch",
  zero tooling keywords, correctly downweighted.
- "Birth of the Universe - Petri Dish Practical Effects", physical practical FX.

---

# Full-depth video audits

---

# YouTube videos: full-depth workflow reconstructions

## 1. "RESISTANCE | Sci-Fi Short Film" (James Lee's Films)

Source: https://youtu.be/KE-_YFv3mXA | duration unknown | r/comfyui post 1wqcicx (score 36)

Tools used: ChatGPT (free tier; character/asset design help, occasional prompt help),
Nano Banana (character frames, keyframes, storyboard panels; image edit), Minimax H3
(open-weight; video generation for almost the entire film, run via ComfyUI, per @comfyorg),
Seedance 2.0 Fast (inside Dreamina; killer-alien-drone attack scenes; strong on action),
Da Vinci Resolve 21 (edit and grade), RunningHub (rented GPUs for trial-and-error action
shots), local PC with RTX 5060 Ti 16GB VRAM (simple shots), Gemini (occasional prompt help),
iClone 8 + Unreal Engine (abandoned original concept from ~2 years earlier), Seedance
director skill (used on a different project, The Yokai Journal: The Mask of Tengu).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: AI shots are directing, not rendering: lock keyframes and concepts first, generate shots as repeatable ComfyUI nodes, keep prompt writing manual, then edit and grade in an NLE.
Note on the "99%": the post title says "made 99% with Minimax H3 on Comfy UI"; the blog
qualifies this: the entire video generation is Minimax H3 except the drone-attack scenes.

### Phase 1: Concept and design assistance

**Do**
1. Use ChatGPT (free tier) to help create the characters, drone, mothership, locations,
   and other elements. All images are generated with Nano Banana.
2. Fix the creative target before generating: the original plan was a 3D/animation film
   (iClone 8 + Unreal Engine test from ~two years earlier, abandoned because his animation
   skills were still mediocre). The AI version was first aimed at converting Jane, the
   original 3D protagonist, but the look was reworked toward grounded realism, closer to
   the feeling of I Am Legend, The Walking Dead, or Arrival.

**Check**
- Direct 3D-to-AI conversions of Jane still looked like famous personalities, so the
  character was reworked until it landed as Elena Morales ("She looked and felt like
  Elena"). [inference: recognizable-real-person likeness was a rejection criterion.]
- Dreamina's strict policy refuses to generate real-life humans similar to actual people;
  Seedance refused the character in tests, so keep backup character versions in case a
  video model refuses the character outright.

**Why**
Design and tone come first; a character that survives the likeness filters of every
tool in the chain is a prerequisite, not a detail.

### Phase 2: Lock the keyframes with Nano Banana

**Do**
1. Generate keyframes for the shots and scenes in mind with Nano Banana.
2. Once a frame is locked, use storyboard prompts to instruct Nano Banana to create
   storyboard panels based on the scene description.
3. Extract the best images from the storyboards; expect to be lucky if three good frames
   come out of a storyboard.

**Check**
- "Every clip begins with the frame." The starting frame must already carry composition,
  character, environment, lighting, and overall look.

**Why**
A strong image as the starting frame gives the video model the composition, character,
environment, lighting, and look to work from, giving far more control than
reference-to-video, where the AI must figure out the shot and generate much of it from
scratch. "Spend more time on the images and keyframes before going into video
generation."

### Phase 3: Camera placement as on a physical set

**Do**
1. During image generation, treat it like a movie shoot: place the camera as if you were
   actually on a film set with limitations and physical constraints, not anywhere in
   space (the animator-tutorial insight: some animations fail to feel cinematic not from
   design or lighting but from unrestricted camera placement).

**Check**
- A camera that flies from the sky, lands, then flies into a building can be cool, but
  it is also when you start feeling you are not watching something real. Adjust by genre
  and vision.

**Why**
Realistic camera placement is what makes the shot believable and cinematic; unlimited
camera freedom is one of the reasons AI work breaks the cinematic feeling.

### Phase 4: Video generation with Minimax H3 in ComfyUI

**Do**
1. Generate clips from the locked starting frames with Minimax H3 in ComfyUI (the
   creator's standard workflow; he had already used H3 for two music videos and a few
   clips).
2. Keep the gunfight/firefight scenes (Elena vs. the armed men, on the large office
   floor) on Minimax H3 as well.
3. Simple shots: generate locally on the RTX 5060 Ti 16GB, averaging 15–20 minutes per
   clip; raising steps can push it to ~40 minutes per clip.
4. Action and late-film scenes needing heavy trial and error: rent GPUs on RunningHub.
   A 15-second clip costs an estimated $0.14, still "way cheaper than using paid AI
   models."

**Check**
- Trial and error is the norm for action: expect many failed clips per keeper.
- Watch for Minimax artifacts: bullet casings "can look pretty strange" → he removed
  those shots. H3 shot-to-shot consistency is hard (commenter corroborates: "very hard
  to have consistency between shots").

**Why**
Open-weight H3 is free, so iterating cheaply is the strategy; the filmmaker's labor is
in the curation, not the per-clip cost. The big plus point of H3 is that it is free.

### Phase 5: Drone attack on Seedance 2 Fast

**Do**
1. Generate the scenes where the killer alien drone enters and attacks the armed men
   with Seedance 2 Fast in Dreamina, the one sequence not on H3.
2. Keep prompts short for Seedance: "Seedance is smart, so there is no point giving it
   a very long descriptive prompt. Sometimes it can actually make the result worse."

**Check**
- Seedance handles shell ejection but sometimes ejects the casing from the wrong side
  of the weapon; triage those clips.

**Why**
"Seedance wins in the action department." For action and fighting, Seedance is one of
the strongest options; H3 and Seedance are "fairly close" otherwise, but the drone
sequence needed Seedance.

### Phase 6: Prompt writing (deliberately manual)

**Do**
1. Write prompts like a director or screenwriter, in plain language, not in the
   structured formats the community recommends. For Minimax H3, most of the videos did
   not use H3's (quite complex) recommended structure at all.
2. Use the complicated structure only when something will not resolve, especially simple
   movements like walking from one point to another.
3. Write 99% of the prompts yourself; use ChatGPT or Gemini only when you cannot get
   something right.

**Check**
- The filmmaker's test on The Yokai Journal (Seedance director skill + Gemini) was
  "amazing" and effortless, but afterwards he had not really learned much from the
  process.

**Why**
Writing is "one of the few skills left that is still important to the filmmaker."
Automating it away removes the last part that still needs the filmmaker, and skipping
it means not learning the craft.

### Phase 7: Spatial continuity via montage editing

**Do**
1. Accept that AI's greatest challenge is spatial awareness and continuity: a normal
   two-person drama is fine, but action with many position changes cannot hold spatial
   continuity with the current workflow.
2. For action scenes, rely on the good-old montage: cut up random footage and assemble
   it into something coherent, establishing an idea of space, action, and story. (This
   is how the office-floor firefight was built.)

**Check**
- When the group of armed men entered, the film risked becoming "a collection of random
  clips with very little to no connection," with room layout and character positions
  random each clip (a top commenter critique): the montage must establish space,
  action, and story, not just splice clips.

**Why**
No video model currently holds spatial continuity across an action scene; the
filmmaker's editing is the tool that creates it. "Resistance: Where the Filmmaker
Still Matters."

### Phase 8: Edit and grade in Da Vinci Resolve 21

**Do**
1. Assemble, pace, and grade in Da Vinci Resolve 21.

**Check**
- Commenter feedback: "The first couple of minutes are great but editing needs a bit of
  work to improve the pacing."

**Why**
The edit is the final control surface for pacing and coherence; "No film is perfect,
and I guess the job of a filmmaker is to keep pursuing it anyway" (creator reply).

### Phase 9: Organization across apps

**Do**
1. Keep organization explicit because the work spans multiple apps (ChatGPT, Nano
   Banana, ComfyUI/H3, Dreamina/Seedance 2 Fast, RunningHub, Resolve). "Organization
   is key especially working alone and in multiple apps."

**Check**
- Track which character version went into which model and which shots were cut for
  artifacts (bullet casings) so nothing regresses.

**Why**
A one-person multi-tool pipeline breaks down without explicit asset and version
tracking.

### The human method, distilled

1. **Every clip begins with the frame.** Spend the time on keyframes before video
   generation; a strong starting frame gives the model composition, character,
   environment, lighting, and look to work from.
2. **Place the camera like a physical set.** Realistic, constrained camera placement is
   what makes AI shots cinematic; unlimited camera freedom breaks believability.
3. **Cheap iteration is the strategy.** Free open-weight models (Minimax H3) let the
   filmmaker iterate; the value is in curation, not per-clip cost ($0.14 per 15-second
   clip on rented GPUs for hard shots).
4. **Use the right model per scene type.** H3 for the bulk of the film; Seedance 2 Fast
   for the drone-attack/action sequence, where Seedance wins.
5. **Prompt like a director, not a prompt engineer.** Plain screenwriter language works;
   reserve complex structures for stubborn cases (simple walking movements); keep
   Seedance prompts short.
6. **Write 99% of prompts by hand.** Deliberately avoid over-automation so the craft
   is learned, not bypassed.
7. **Fix spatial continuity in the edit.** Montage editing, cutting disparate footage
   into a coherent sense of space, action, and story, since no model holds it natively.
8. **Triage artifacts ruthlessly.** Cut Minimax's strange bullet casings; watch
   Seedance's wrong-side shell ejections; consistency between shots is H3's hard edge.
9. **Keep likeness-safe backups.** Character versions that survive each tool's
   real-person-likeness filters; Seedance refused the character in tests.
10. **Organize explicitly.** One person, many apps: track assets, character versions,
    and cut shots so the pipeline does not regress.

**Depth status:** DEPTH-LIMITED (no captions; the caption-fetch tool hit an approval
gate that was declined, and the video file cannot be pulled. Full depth would require
a media download, which needs the operator's explicit approval per the skill's interactive
exception. The reconstruction above is unusually rich for DEPTH-LIMITED because the
creator's long-form blog post on the process, the Reddit post selftext, and the thread
comments were all readable.)

---

## 2. "Fix Lumpy Photogrammetry Meshes in Blender: Google 3D Tiles" (Nachiket B)

Source: https://youtu.be/m9oxz99Ysp0 | duration unknown | r/photogrammetry post 1wjnwzi (score 223)

Tools used: Blender 4.2+; Planer add-on (Blender add-on by nachiket_bhand: detects planar
regions, snaps vertices onto fitted planes, rebuilds creases as straight edges and
corners as sharp points; $35 on SuperHive [Gumroad also listed in the task brief]; MIT
licensed; plain Python, bpy; only dependency is numpy, which already ships with
Blender; no wheels, no network access, no external dependencies); SuperHive product
page (https://superhivemarket.com/products/planer--photogrammetry-mesh-refiner); the
demo video itself shows a full run: N-panel settings visible, report line at the end,
viewport orbiting the result (per the author's comment).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Fix the geometry, don't smooth it: detect planar regions, snap vertices to fitted planes and their intersections, and prove fidelity with a deviation report.
### Phase 1: Start from the damaged mesh

**Do**
1. Pull a city block from Google Photorealistic 3D Tiles, a drone survey, or any
   photogrammetry pipeline.
2. Confirm the symptoms: walls that ripple, roofs that undulate, ridges that come
   through as saw-tooth, corners that are rounded mush.
3. Reject the usual fixes on their trade-offs: smoothing softens wanted detail;
   remeshing destroys the UVs; decimation smears the baked atlas texture into streaks;
   manual retopology takes a day per building.

**Check**
- The mesh's problems are geometric (planar regions displaced), not shading: a
  smoothing pass would just round the corners further.

**Why**
Every existing fix costs something (detail, UVs, texture, or a day per building);
Planer exists to fix the geometry without paying those costs.

### Phase 2: Run the Planer pipeline (N-panel)

**Do**
1. Install the add-on: Blender 4.2+, Preferences → Add-ons → Install from Disk. The
   panel appears in the 3D Viewport N-panel under the "Planer" tab.
2. Run it on the mesh. The internal algorithm, in order: bilateral normal filtering →
   planar region growing and merging → snap-to-plane with sharp edge and corner
   reconstruction. Regions are gated by area, not face count, so the coarse
   large-triangle tiles that come out of 3D Tiles still qualify.
3. The solver behavior to expect:
   - Vertices supported by two planes snap onto the plane–plane intersection *line*,
     so creases come out straight instead of jagged (straight roof ridges and eaves).
   - Vertices supported by three planes snap to the intersection *point* (crisp
     building corners).
   - Topology is preserved on a copy that keeps the original loops, so texture, UVs,
     and material come through untouched: no re-bake, no data-transfer, no smearing.
   - Output is always a new `REFINED_` mesh alongside the source; the original object
     is never modified.

**Check**
- Deviation is reported in the status bar as the ground truth, not a guess (see
  Phase 3).

**Why**
Flatter is not smoother: "Genuinely planar walls and roof facets. Not smoothed, solved. Planar regions are detected, merged, and enforced." Keeping the topology and
the original object makes the operation non-destructive and re-runnable.

### Phase 3: Tune the parameters against the symptoms

**Do**
1. Adjust the N-panel settings per the symptom→fix table:
   | Symptom | Fix |
   | --- | --- |
   | Result too rounded, ridges lost | Lower Crease Sensitivity to 0.15–0.20 |
   | Not flat enough | Raise Refine Iterations to 3 |
   | Small details being flattened | Raise Min Plane Area |
   | Nothing gets refined | Lower Min Plane Area |
   | Spikes or stretched vertices | Lower Snap Guard |
   | Single house or prop, not a block | Lower Min Plane Area to 0.1–0.5 |

**Check**
- Re-run and compare the new report line against the previous one; the deviation
  numbers tell you whether the change stayed faithful.

**Why**
Each parameter targets one failure mode, so tuning is diagnostic rather than blind
tweaking.

### Phase 4: Verify with the report line

**Do**
1. Read the full report line from the status bar: face count in/out, planes found,
   verts snapped (edge, corner), open edges, non-manifold | deviation mean / p95 / max
   in metres.
   - Product-page example: `Refined: 14980->14980 faces, 300 planes, 6752 verts
     snapped (1487 edge, 129 corner), open edges 4186, non-manifold 4690 |
     deviation mean 0.024m p95 0.121m max 0.741m`
   - Real user-mesh run (u/drumfish's file): `Refined: 205980->205980 faces,
     18 planes, 91847 verts snapped (966 edge, 1 corner), open edges 0,
     non-manifold 0 | deviation mean 0.008m p95 0.019m max 0.085m`
2. Benchmarks from the author: mean deviation of 7cm on a full city block; on a single
   ~55m building, mean deviation lands around 0.02m, roughly 0.1% of the bounding
   diagonal.
3. Inspect the result visually: the demo video ends with the viewport orbiting the
   refined result.

**Check**
- "You are not guessing whether it stayed faithful to the survey; you can read it
  off the status bar and put it in a client report."
- The three deviation numbers (mean / p95 / max) are the deliverable-grade proof of
  fidelity.

**Why**
Quantified deviation replaces subjective before/after judgment; it is the mechanism
that makes the tool client-reportable instead of a visual flourish.

### Phase 5: Respect the caveats

**Do**
1. Know what Planer does not do: it does not make meshes watertight, does not reduce
   poly count (it triangulates, so the face count goes up), does not fix holes or
   non-manifold edges, and does not touch the texture image.
2. Budget compute: it is slow on big meshes, about four minutes for 195k faces.
3. For a real trial on your own data, run it on your own meshes with your own settings
   (the author's refund policy: "buy it, run it on your own meshes with your own
   settings, and if it doesn't do what the page says, message me and I'll refund you.
   No questions").

**Check**
- Report line shows the real face count change (triangulation increasing faces is
  expected, e.g. 14980->14980 means no face-count change before triangulation passes).

**Why**
Knowing the non-goals prevents misapplying the tool to watertightness or decimation
tasks; a trial on your own mesh is the only real test ("sending you things is just
not how you test an addon. it's how you test a service," community feedback that
reshaped the author's demo policy).

### The human method, distilled

1. **Flatten, don't smooth.** Detect, merge, and enforce planar regions instead of
   averaging vertices; smoothing is what rounded the corners in the first place.
2. **Snap to intersections, not averages.** Two-plane verts go to the intersection
   line (straight creases), three-plane verts to the intersection point (sharp
   corners).
3. **Gate regions by area, not face count.** Coarse large-triangle 3D-Tiles geometry
   must still qualify as planar.
4. **Never modify the source.** Output a new `REFINED_` mesh alongside; topology and
   original loops survive so UVs/materials carry through natively.
5. **Quantify fidelity every run.** Report faces, planes, snapped verts (edge/corner),
   open edges, non-manifold, and deviation mean/p95/max in metres; the report line is
   client-reportable proof, not decoration.
6. **Tune diagnostically.** Each parameter maps to one symptom (Crease Sensitivity
   0.15–0.20, Refine Iterations 3, Min Plane Area, Snap Guard).
7. **Keep the dependency footprint at zero.** Plain Python + the numpy that ships with
   Blender; no wheels, no network access, no external dependencies.
8. **Name the non-goals up front.** No watertightness, no poly reduction (triangulation
   raises face count), no hole repair, no texture-image edits.
9. **A real trial is a self-run.** The only meaningful test is the buyer running it on
   their own mesh with their own settings, reading their own report line.

**Depth status:** DEPTH-LIMITED (no captions; the caption-fetch tool hit an approval
gate that was declined, and the video file cannot be pulled. Full depth would require
a media download, which needs the operator's explicit approval per the skill's interactive
exception. The reconstruction above draws on the SuperHive product page, the Reddit
post selftext, the full comment thread including the author's demo description and
two report lines, and the exact tuning table.)

---

# Full-depth audits, continued

## 3. "My Cave Exploration Game just got upgraded render tech! (Cave Expedition)" (Moonmilk Games)

Source: https://www.youtube.com/watch?v=4k1OHSCp_h0 | ~20:53 (duration from requester note; yt_summarize returned null) | r/photogrammetry post 1wbwrns (score 42, by GooseJordan2)
Tools used: Unity, URP (Universal Render Pipeline), Shader Graph (custom function nodes), Unity Burst/Jobs, compute shaders, Obi Physics (Virtual Method Unity asset: particle-based distance, collision, and shape-matching constraints) for ropes, photogrammetry for rock textures, Steam Deck as the low-end performance target.
Verified context: Cave Expedition is a 1-4 player co-op caving simulator (Steam app 4372950; fictional cave layouts; scanned rock textures for realism), built in Unity, with a photogrammetry-sourced rock texture pipeline and a high-performance water system (sources: author's Reddit post selftext, author's comment, third-party press). The devlog exists because, in the author's words, "the rendering did had to move mountains to get the rendering to look like this and still work on lower end devices like Steam Deck" (author comment on post 1wbwrns; typo in original).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Performance is a pipeline: voxel terrain with mesh compression, virtual texturing, and GPU-driven detail, each stage held to its budget.
**Caption availability:** None. yt_summarize (captions/metadata, --no-frames) returned no transcript; a captions-only subtitle fetch hit YouTube HTTP 429 followed by a sign-in/bot challenge, which is treated as a hard stop for that provider in this task. The numbered claims below come from a prior audit that reportedly extracted them from the captions. They are reproduced here structured as workflow phases, but they are NOT re-verified against the captions (see caution flags). Claims in **bold** are verified from the Reddit post/comments or the video metadata.

### Phase 1: Voxel terrain core: CLA ("canvas level of detail")

**Do**
1. Build the cave geometry as an **SDF (signed distance field) voxel volume** with **surface-nets meshing**, instead of hand-authored meshes or a heightfield [prior-audit claim, unverified].
2. Name the approach **CLA ("canvas level of detail")** [prior-audit claim, unverified].
3. **Do not start from dense, detail-rich geometry.** The system starts low-resolution and adds detail as the camera approaches: "inverse Nanite" [prior-audit claim, unverified].

**Check**
- [inference] Proximity drives LOD: far terrain stays coarse, near terrain resolves fine, keeping the vertex budget under control on low-end GPUs (consistent with the stated Steam Deck target, which is verified from the author's comment).

**Why**
Nanite-style pipelines assume shipping dense geometry and decimating at runtime; on an indie budget and a Steam Deck target, the reverse is cheaper: resolution is manufactured only where the player looks.

### Phase 2: Sculpting and detail via "stamps"

**Do**
1. Make the voxel terrain **sculptable** in-editor/dev tooling [prior-audit claim, unverified].
2. Add detail through **"stamps"**: authored detail patches that support **stretch, rotate, blend, and wetness** parameters [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
Stamps separate authored art detail from the underlying coarse volume: the same stamp can be stretched over a wall, rotated into a ceiling, blended into a floor, or given a wet sheen near water, without new unique geometry.

### Phase 3: Non-manifold fix in surface nets

**Do**
1. Detect the failure cases in the surface-nets meshing: **bit patterns of solid vs. non-solid voxels** that produce non-manifold topology [prior-audit claim, unverified].
2. **Split vertices per case** instead of emitting a shared vertex when the bit pattern is non-manifold [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
Surface nets collapse cell corners into shared vertices, which breaks (non-manifold edges) at certain solid/empty configurations; duplicating vertices for those patterns is a local, cheap fix that keeps the fast meshing path intact.

### Phase 4: "Brutal unwrapping": integer UV grid

**Do**
1. Skip conventional UV unwrapping entirely; use a **strict integer UV grid** [prior-audit claim, unverified].
2. Organize the texture space into **256 patches** laid out in **morton order** [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
A voxel surface has no natural seams, so classical unwrapping is wasted effort; a strict integer grid gives every surface cell a deterministic, seam-consistent home in texture space, and morton order keeps spatially adjacent cells adjacent in texture memory (cache coherency). "Brutal" is the author's framing: a deliberately crude rule that beats a clever one at runtime.

### Phase 5: Mesh compression: three 32-bit integers per vertex

**Do**
1. Compress **UVs to 8 bits per quad** [prior-audit claim, unverified].
2. **Pack the indices** [prior-audit claim, unverified].
3. **Omit UVs and tangents from the vertex data entirely**: recompute the tangent in the vertex shader instead of storing it [prior-audit claim, unverified].
4. Store **normals as 16-bit octahedron pairs** [prior-audit claim, unverified].
5. Result: a **final vertex of three 32-bit integers** [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
Memory bandwidth, not ALU, is the binding constraint on low-end GPUs. Anything the vertex shader can recompute deterministically (tangent from a strict integer UV grid; normal from an octahedron pair) is recomputed rather than stored. The payoff is a vertex small enough to fit a whole cave in limited VRAM.

### Phase 6: Virtual texturing with GPU feedback rendering

**Do**
1. Implement **virtual texturing** fed by a **GPU feedback prepass** that computes **LOD + patch ID** per pixel [prior-audit claim, unverified].
2. Run **per-light feedback passes for shadows** [prior-audit claim, unverified].
3. **Later rewrite the feedback fully GPU-side, per-quad** [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
With 256 texture patches, only the patches actually visible at a given LOD need to be resident. The feedback prepass is the bookkeeping that decides which those are; moving it GPU-side per-quad removes a CPU round-trip from the hot loop. Per-light feedback extends the same idea to shadow map paging.

### Phase 7: Custom compute-shader tessellation in URP/Shader Graph

**Do**
1. Replace hardware tessellation with a **custom compute-shader tessellation** pipeline, because the author develops on **Apple Silicon**, which lacks hardware tessellation support [prior-audit claim, unverified].
2. Write it as a **Shader Graph custom function** node inside **URP** [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
A missing hardware feature is not a blocker if the pipeline is programmable: compute shaders can do the subdivision work manually, and exposing it as a Shader Graph custom function keeps it usable inside URP's artist-facing tooling.

### Phase 8: Burst/Jobs as an intermediate step

**Do**
1. Before reaching compute shaders, route the heavy meshing/data work through **Unity Burst/Jobs** as the intermediate implementation [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
[Inference] Burst/Jobs parallelize the CPU-side voxel meshing with minimal code changes; moving to compute shaders later pushes the same work onto the GPU. It is the standard two-step migration: first thread it on CPU, then lift it off CPU entirely.

### Phase 9: Rope physics: Obi Physics with O(1) SDF collision

**Do**
1. Use **Obi Physics** (the Virtual Method Unity asset: particle-based **distance, collision, and shape-matching constraints**) for the cave ropes [prior-audit claim, unverified].
2. Resolve rope collisions against the terrain with **O(1) SDF lookups**, since the terrain already exists as a signed distance field [prior-audit claim, unverified].

**Check**
- Not specified in available sources.

**Why**
Cave Expedition is built around ropes (rope descents, anchors, SRT gear per the press coverage); particle-based rope physics is the natural fit, and because the world is already an SDF, collision queries against it are constant-time lookups rather than mesh casts. The representation choice in Phase 1 pays off twice.

### Phase 10: Photogrammetry rock textures (verified from the Reddit post)

**Do**
1. Photograph real cave rock and process it into textures (post selftext: "I used photogrammetry to make the rock textures for Cave Expedition") [verified: post 1wbwrns selftext].
2. Map those scanned textures onto the fictional cave layouts: "the cave layouts are fictional; the scanned textures are part of giving them that real underground feel" [verified: post 1wbwrns selftext].
3. Check them **in-game under the headlamps**, through tight passages and rope descents, since headlamp-lit rock is the actual player view [verified: post 1wbwrns selftext].

**Check**
- The deliverable is believability under moving headlamps, not studio lighting.

**Why**
Procedural cave layouts plus scanned real-rock textures split the problem: fiction for gameplay freedom, photogrammetry for tactile credibility. Judging from the player's light source keeps the art honest about what players will actually see.

### Caution flags on the prior-audit numbers

- The claims ending the prior-audit list (waterfall source box "4.7 units wide, center at 7.37 vertical"; particle separation 0.04; voxel scale 0.75) are **verbatim numbers from an unrelated earlier audit** and appear to be contamination, not this video's content. They must not be attributed to this video. They are excluded from the phases above.
- All other numeric claims (256 patches, 8-bit UVs per quad, 16-bit octahedron normals, three 32-bit integers per vertex, O(1) SDF collision) come solely from the prior audit and are **not re-verifiable** without captions.

### The human method, distilled

1. **Inverse Nanite:** start coarse and manufacture detail where the player looks, instead of shipping dense geometry and decimating it. [prior-audit claim, unverified]
2. **Target your weakest device first:** the whole render-tech rebuild exists to make high-end looks run on Steam Deck-class hardware. [verified: author comment]
3. **Recompute, don't store:** tangents recomputed in the vertex shader, normals as octahedron pairs; vertex = three 32-bit integers. [prior-audit claim, unverified]
4. **Brutal rules beat clever tools:** a strict integer UV grid with morton-ordered patches replaces classical unwrapping for voxel surfaces. [prior-audit claim, unverified]
5. **Push bookkeeping GPU-side:** feedback prepass for LOD + patch ID and per-light shadow feedback, later rewritten fully GPU-side per-quad. [prior-audit claim, unverified]
6. **Author on the hardware you have:** no hardware tessellation on Apple Silicon, so write compute-shader tessellation as a Shader Graph custom function in URP. [prior-audit claim, unverified]
7. **Representation choices pay twice:** the SDF terrain gives both meshing and O(1) rope collision. [prior-audit claim, unverified]
8. **Fictional layouts, real textures:** photogrammetry grounds invented caves in real rock; judge it under the player's headlamps, not studio lights. [verified: post selftext]

**Depth status:** DEPTH-LIMITED (no captions obtainable: yt_summarize returned no transcript, captions-only fetch blocked by YouTube rate-limit/bot challenge; video download not attempted per hard rule. Verified layer: video metadata, the author's Reddit post 1wbwrns selftext + author comments, Steam listing details cited by the post. "Full depth would require a media download, which needs the operator's explicit approval per the skill's interactive exception.")

---

## 4. "RAGNAROK ONLINE ZERO GLOBAL FIRST WOE Sept 20 2026" (Duwayt TV)

Source: https://www.youtube.com/watch?v=lZvwaCmeyI8 | 2:53 (173 s) | r/RagnarokOnline post (no post ID in the scout dataset; task-given title "The reason I love RO. 1st WOE in Ragnarok Zero Global")
Tools used: None observable. This is gameplay capture of a commercial game, not a development workflow.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Reverse the process: define erosion as the build unit, run it in reverse for the grow-in, and layer blueprint preview, climbing rim, and ember finish.
One paragraph: the video is 173 seconds of player-POV gameplay footage from Ragnarok Zero Global's first War of Emperium (WOE) on September 20, 2026, played from a Hunter point of view (the description reads "ROZ 09202026 1ST WOE / Hunter POV - Frozen LOLs", ~1,792 views, keyword "Ragnarok"). It shows guild siege combat in a live commercial MMO build: spell effects, guild members moving through a castle map, a capture objective being contested. Because it is a player capturing their own play session, there is no authoring tooling on display, no asset pipeline, no code, no engine configuration, and nothing in the metadata, description, keywords, or Reddit context that names a tool, technique, or workflow step. There is no workflow signal to reconstruct: it carries zero prescriptive content for the video-tooling-scout project.

**Depth status:** NO-TOOLING (captions also absent on this video, but irrelevant: gameplay footage of a commercial title cannot yield a tooling workflow even with a transcript. Not pursued further per task instructions.)

---

# Native Reddit demo clips: workflow reconstructions

All three videos in this batch are **native Reddit video posts (v.redd.it)**: short demo clips, not narrated tutorials. There is no voiceover, no step-by-step, no screen capture of an editor. Each reconstruction below is built only from the author's post text, the visible comments, and (for V5) the author's post history context visible in the dataset. Where the source is thin, phase breakdowns are explicitly marked **[inference]**.

---

## 5. "Blueprint/Construction effect" (u/craftymech)

Source: https://v.redd.it/e4yyvwdinbqh1 | r/proceduralgeneration post 1wjye2x (score 67) | native clip (demo, not tutorial)

Tools used: Unnamed game engine (the author describes a "procedural build system"; engine not stated). Shaders/materials are the author's own: a transparent blueprint material, a separate orange "rim" shader, and "ember" particle effects. Structures are assembled from individual stones and timber beams (author's procedural stone/timber work, per post text and author history visible in the dataset).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Test the question empirically: pit deterministic behavioral scripts against a learned policy in the same engine and measure which wins.
### Phase 1: Define the build unit: the erosion factor

**Do**
1. Structures are built from individual stones and timber beams.
2. The procedural build system carries an "erosion" factor that tears the structure down piece by piece.

**Check**
- Confirm the erosion tears down the *full* structure in a legible order (the author relies on it being readable in both directions).

**Why**
The teardown parameter already encodes the build order. Reusing it as the build parameter means the construction animation is free: the system already knows which stone/beam comes in which order.

### Phase 2: Run erosion in reverse: the grow-in

**Do**
1. To "build" the structure, run the erosion factor in reverse: instead of removing pieces, pieces grow in over time.
2. Keep the growth tied to the existing erosion ordering so the assembly reads as construction, not a dissolve.

**Check**
- Watch the reversed pass once through: does the structure emerge in a plausible building sequence (foundation/first stones before the timber/upper parts)?

**Why**
One parameter drives both teardown and construction; no separate build animation is authored. **[inference]** Reversing a teardown curve is cheaper than authoring a second growth curve, and it guarantees the two directions are exact mirrors.

### Phase 3: Blueprint preview material

**Do**
1. Render the unbuilt/queued structure as a "blueprint" view: a transparent material.
2. Blend specular into that material so the lighting on the preview is not flat.

**Check**
- Rotate the camera around the blueprint ghost: the preview should still read as solid geometry (specular highlights on edges/faces), not a flat overlay.

**Why**
A flat transparent tint would read as UI, not as a structure-to-be. Specular blending keeps lighting information, so the player sees *what* is coming, not just *where*.

### Phase 4: The climbing construction rim

**Do**
1. Add a separate shader that renders an orange "rim" on top of the architecture.
2. Animate the rim so it climbs the structure in sync with the grow-in.

**Check**
- Verify the rim tracks the build frontier: the orange edge should always sit where the next pieces are appearing.

**Why**
The rim separates "already built" from "being built" at a glance. **[inference]** A second shader on top of the geometry is used instead of coloring the geometry itself, so the build highlight never contaminates the final material.

### Phase 5: Ember finish

**Do**
1. Throw in a few "ember" particles for a little extra pizzazz.

**Check**
- **[inference]** Check that the particles read as construction/furnace sparks and do not obscure the structure during the grow-in.

**Why**
Author's own words: finish. A small particle pass sells the "hot work of building" without touching the structural system.

### Community note

Commenter RagingPsychoBandit (score 9) suggested moving away from the "futuristic blue" toward a pencil-sketch-on-paper/papyrus look, evoking medieval or Renaissance architectural sketches. Author craftymech replied (score 4): "Thats an interesting idea, I'll have to experiment a little." No change confirmed.

### The human method, distilled

1. **One parameter, two directions.** If teardown is already parameterized, construction is just erosion in reverse; no second system needed.
2. **Build from parts, not blobs.** Individual stones and beams give the grow-in a legible order for free.
3. **Previews need lighting, not just transparency.** Specular blending keeps the blueprint ghost readable as geometry.
4. **Highlight the frontier, not the result.** A separate climbing shader marks the build edge without touching final materials.
5. **Finish is cheap, structure is not.** Ember particles sell the moment; the build order came from the system itself.

**Depth status:** DEPTH-LIMITED (demo clip, not tutorial; no engine, parameter values, or shader code given; the author describes the *concept*, not the implementation. No Check/Why detail beyond what the post text supports.)

---

## 6. "I built a Ragnarök Online engine to test if a neural network can beat deterministic scripts" (u/Known_Chip8544)

Source: https://v.redd.it/23mmjd2nsrqh1 | r/RagnarokOnline post 1wly4u6 (score 53) | native clip (demo, not tutorial)

Tools used: Godot (custom Ragnarök Online prototype engine built by the author). Per-character behavioral scripts (author-built; deterministic baseline and reinforcement-learning neural network teams are both authored by the author, with AI assistance for learning neural networks, per his own account).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Revive, don't rebuild: retexture the old model, rig and animate it, and let the original forms carry the nostalgia.
### Phase 1: Set the question: can a fake player beat a veteran?

**Do**
1. Define the target: a "fake player" good enough to beat an experienced PvP player.
2. Inspired by the concept of "fake players" (the author cites a post about Ragnarök Offline that he tested and got hooked on).

**Check**
- **[inference]** The question is falsifiable only if "beat" is measured in matches, which leads directly to the match framework below.

**Why**
A concrete opponent (deterministic scripts, then a real PvP veteran as the eventual goal) turns a vague AI interest into a benchmark.

### Phase 2: Build the testbed: custom RO prototype in Godot

**Do**
1. Build a custom Ragnarök Online prototype engine in Godot.
2. Give it the ability to select characters and assign their behavioral scripts per character.

**Check**
- The testbed must support symmetric team setup: same roster available to both sides, differing only in behavior logic.

**Why**
A prototype instead of the real RO client means full control over characters, scripts, and match conditions. Per-character script assignment is the mechanism that lets two *different* control schemes fight each other.

### Phase 3: Build the deterministic baseline: Team A

**Do**
1. Field a 2v2 (Champion + Professor/Scholar on each side).
2. Assign deterministic scripts with explicit roles: the Professor focuses on crowd control/debuffs; the Champion focuses on kills.

**Check**
- Baseline behavior is inspectable and repeatable: role-based, no learning involved.

**Why**
The deterministic scripts are the yardstick. They encode *known-good* strategy (CC/debuff setup into a kill role), so the RL agent is measured against competent play, not random play.

### Phase 4: Build the challenger: Team B, reinforcement-learning neural network

**Do**
1. Train a reinforcement-learning neural network to control the same 2v2 roster.
2. The author notes he knows "almost nothing about neural networks" and used AI assistance to learn and develop it.

**Check**
- **[inference]** Training progress is judged by match outcomes against Team A, not by loss curves (the author reports results in match terms only).

**Why**
RL is the hypothesis: learned behavior vs. authored behavior. AI-assisted development is the author's stated path given his starting skill level.

### Phase 5: Run the symmetric match and observe

**Do**
1. Run a symmetrical 2v2 match: Team A (deterministic) vs. Team B (RL neural network).
2. Watch the outcome: Team A "completely rolls over" Team B; the neural network "hasn't figured out how to handle the deterministic strategy yet."

**Check**
- Symmetry (same roster, same match conditions) isolates the variable under test: behavior logic.

**Why**
A symmetric 2v2 removes roster excuses. The decisive win establishes the current state: authored role-based strategy beats the early RL agent, and the experiment continues toward the eventual goal (a fake player that can beat a real human PvP veteran).

### Community notes

- Alone_Conference7144 (score 4) advised running training in "simulated time," warning the author will "not get any results in a meaningful amount of time" at real-time speed. No reply from the author in the data.
- Kyruka (score 2) described a parallel idea: an LLM-driven team with full game guides vs. a team that only knows basic concepts, competing in WoE to see if the AI discovers strategies the guides never mention, with separate exp/drop rates for bots vs. humans.

### The human method, distilled

1. **Fix the question first.** "Can a fake player beat a veteran" becomes "can Team B beat Team A," which is measurable.
2. **Build the arena before the agent.** A controllable prototype with script assignment is the precondition for the whole experiment.
3. **Benchmark against competence, not randomness.** The deterministic baseline uses real roles (CC/debuff → kill), so a win means something.
4. **Symmetry isolates the variable.** Same roster, same match; only the control logic differs.
5. **Report the negative result.** "The network hasn't figured it out yet" is the finding; it defines how far training still has to go.
6. **Simulated time is the training bottleneck** (community advice): real-time matches are too slow to produce meaningful RL results.

**Depth status:** DEPTH-LIMITED (demo clip, not tutorial; no network architecture, training regimen, reward function, Godot implementation details, or match count given. The experimental method is fully reconstructable from the post text; everything beneath the match description is [inference] or community suggestion.)

---

## 7. "Found this ancient model I made in 2013, so I revived it" (u/Mephasto)

Source: https://v.redd.it/yf5ayxscynrh1 | r/3Dmodeling post 1wpvl1q (score 388) | native clip (demo, not tutorial)

Tools used: None named in the post or comments. The model is an Anomalocaris (extinct marine arthropod) originally made in 2013; it now appears animated in a project the author calls "The Hive," which the author describes in a comment as being for an "old-school real-time strategy game."

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Scale through sampling: build the world from one block with deterministic sampling and LOD so billions of square kilometers stay traversable.
### Phase 1: Assess the old mesh [inference]

**Do**
1. Recover the 2013 Anomalocaris model file and open it.
2. **[inference]** Judge whether the geometry is worth reviving rather than rebuilding: silhouette, segment count, proportion.

**Check**
- **[inference]** Does the old mesh still hold up at the target fidelity (an old-school RTS, where per-unit detail budgets are low)?

**Why**
**[inference]** A 2013 model was likely built for older render budgets, which maps well onto an old-school RTS unit; the revival is economical only if the old topology is serviceable.

### Phase 2: Retexture

**Do**
1. Give the old model a new texture (author: "gave it a new texture").

**Check**
- **[inference]** The new texture should match the look of "The Hive" (commenters compare the look to Bioshock 2; the author also entertained a "Jrpg dungeon" reading).

**Why**
Texture is the cheapest way to modernize an old model: new surface detail and art direction without touching geometry.

### Phase 3: Rig

**Do**
1. Rig the model (author: "rigged ... it").

**Check**
- **[inference]** The Anomalocaris body plan (segmented body, paired flapping lobes, frontal appendages) needs a joint chain that can swim; verify the rig bends along the segments.

**Why**
**[inference]** A 2013 static model has no skeleton; rigging is what converts a museum piece into a game unit.

### Phase 4: Animate

**Do**
1. Animate the rigged model (author: "rigged and animated it").

**Check**
- The author reports the end state: "13 years later, the little guy is happily alive in 'The Hive'." The check is the finished, moving creature in its game context.

**Why**
The revival is only complete when the model moves inside its project; the clip itself is the proof-of-life.

### Community notes

- Commenters read the piece through game-art lenses: Bioshock 2 vibes (LetAvailable9651, score 2), a JRPG dungeon setting (ValseOubliee, score 3), a "living fossil" joke (PolarSparks, score 8).
- The author confirmed "The Hive" is for an old-school real-time strategy game (Mephasto comment, score 2).
- The r/3Dmodeling AutoModerator requested process details (software, render settings, time taken, wireframe); the author did not provide them in the visible comments.

### The human method, distilled

1. **Old assets are inventory.** A 2013 model is a starting point, not a loss; keep old files openable.
2. **Texture first, geometry last.** A new texture modernizes the asset at the lowest cost.
3. **Rig what you intend to move.** The skeleton is the bridge from static model to game unit.
4. **The clip is the deliverable.** "Happily alive in The Hive", the proof is the animated creature in context, not the process log.
5. **Name the end use early.** Knowing it serves an old-school RTS sets the fidelity target for every phase.

**Depth status:** DEPTH-LIMITED (demo clip, not tutorial; post is two sentences. No software, texture method, rigging approach, animation technique, or timeline given. Phases are grounded in the author's stated sequence "new texture → rigged and animated," with all phase internals marked [inference].)

---

---

# World-scale procgen: reconstructions

## 8. "The Entire Minecraft World, From One Block to 3.6 Billion km²" (u/ImolaBoost)
Source: https://v.redd.it/zzrkz89e6drh1 | r/proceduralgeneration post 1wonb8q (score 176) | native clip (demo, not tutorial)

The clip is a demo, not a narrated workflow: a single camera ascent from the ground to Y=20,000,000 showing the whole world at once. All technique detail comes from the author's post selftext and three author replies in the comments. Nothing below is invented; gaps are marked [inference].

Tools used: Minecraft (Java edition implied), a custom mod written by the author, plus the third-party Distant Horizons mod (used in the video for near-field terrain; stops applying at the dimension transition).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Fill the skyline with shaders, not geometry: a procedural building shader generates the city at render time.
**Core trick (stated by the author):** "No CG or AI, rendered entirely in game and to scale." The world is shown through progressively higher/lower-detail LOD textures generated from the world seed, rendered in a separate dimension mapped 1:1 to overworld coordinates.

### Phase 1: Query the seed, never generate chunks

**Do**
1. Exploit the fact that Minecraft world seeds are deterministic and queryable: you can ask "what would be here" at any coordinate without generating the chunk (author's words).
2. Sample the world generator at a per-LOD granularity ("sampled per x units"; the exact step size is not stated).
3. Bake the sampled world gen onto one massive to-scale texture. Each pixel represents the average of what it represents (terrain type/color of its footprint).

**Check**
- Every portion of the overworld map must be represented, whether previously generated or not.
- At the highest LOD the texture must portray the map at near block-per-pixel accuracy.

**Why**
Rendering the full world in chunks is, per the author, "physically impossible," so the only tractable route is to reduce the world's surface to a 2D summary image built from the same deterministic generator the game itself uses. The average-per-pixel bake keeps each texel honest about its footprint.

### Phase 2: Build the LOD pyramid

**Do**
1. Build progressively higher/lower-detail LOD texture versions of the baked world map.
2. Put the lowest LOD of the entire world on a single plane ("generating the entire world on one plane at the lowest LOD"), which is also much faster than per-chunk approaches.
3. For higher resolutions, keep only local LOD tiles ("I only include local LOD for higher res tiles") instead of one giant high-res texture. Divide the tiles per viewer Y value.
4. Increase tile resolution progressively all the way down to Y=500.

**Check**
- The camera transition at each LOD boundary must stay continuous as the viewer rises.
- Far-field summary must still read as the same world the player walks in (the author confirms every spot on the map is visitable).

**Why**
[Inference] A single texture can never hold block-per-pixel detail for 60M x 60M blocks, so the pyramid trades memory for visibility: one coarse whole-world plane plus local high-res tiles near the viewer. The Y=500 cutoff bounds how far the tile pyramid needs to go before the real world takes over.

### Phase 3: Mount the textures in a 1:1-mapped separate dimension

**Do**
1. Render the LOD textures in a separate Minecraft dimension.
2. Map that dimension's coordinates 1:1 with overworld coordinates, so texture pixels sit exactly over the blocks they summarize.
3. At Y=500, transition back to the overworld dimension (real chunks, Distant Horizons still applies below this point; the author notes Distant Horizons stops applying at the dimension transition).

**Check**
- The seam at Y=500: the last LOD tile must hand off to real terrain without a visible pop.
- Coordinate mapping must be exactly 1:1 so the map and the world never disagree.

**Why**
A separate dimension keeps the fake far-field rendering isolated from real chunk logic (no chunk-gen cost, no entity processing), while 1:1 mapping makes the illusion geometrically honest: "rendered entirely in game and to scale."

### Phase 4: Fly the ascent (the demo itself)

**Do**
1. Move the camera from Y=0 up to Y=20,000,000.
2. As height increases, let the renderer transition through the LOD levels until the entire 60,000,000 x 60,000,000 block world is visible at once.

**Check**
- 60M blocks x 1 m/block = 60,000 km per side, 3.6 billion km² total (title's number; about 7x Earth's surface, per a commenter).
- World gen is bounded by the hardcoded 60M x 60M limit (author's understanding), so the map has a true edge.

**Why**
Height is the zoom control: the demo proves the LOD pyramid is continuous from ground level to whole-planet view in one unbroken shot.

### The human method, distilled
1. **Query, don't generate.** If the generator is deterministic, the cheapest representation of the world is a function call, not geometry.
2. **Average-per-pixel is a legitimate LOD strategy.** Each texel summarizing its footprint keeps the far view honest instead of aliased.
3. **Isolate the illusion in its own dimension.** Real chunk systems and fake map systems share nothing but a coordinate frame.
4. **Height-indexed LOD tiles with a handoff altitude.** Tiles divide per Y value; Y=500 is the seam where the map becomes the world again.
5. **Averaging the same generator twice must agree.** Because both the map and the chunks come from the seed, map and territory cannot disagree (near block-per-pixel at the top LOD).
6. **One plane for the planet, tiles for the neighborhood.** Whole-world-at-once lives on a single plane; high detail is only ever local.

**Depth status:** DEPTH-LIMITED (demo clip with no narration; author disclosed the technique in selftext plus three replies, but exact sampling step, number of LOD levels, and tile sizes were not stated)

---

## 9. "Procedural building shader to fill out the skyline of my cyberpunk city" (u/Zestyclose_End3101)
Source: https://v.redd.it/15mwc0oaw1qh1 | r/proceduralgeneration post 1wipca1 (score 21) | native clip (demo, not tutorial)

The clip is a demo, not a narrated workflow. Sourcing is extremely thin: title only, no selftext, zero comments. The only verifiable claim is in the title: the skyline fill is done with a procedural building shader, so the buildings are shader output rather than authored assets, serving a cyberpunk city scene. Everything below is a phase skeleton built from that single fact and is marked [inference] where it goes beyond it.

Tools used: Not stated. A shader language in some 3D engine (which engine, which language, and whether the shader runs on instanced meshes, billboards, or raymarched geometry is unknown).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Ship the experience in the browser: client-side WebGPU rendering with a WGSL pipeline and a GLSL fallback.
### Phase 1: Define the skyline's role [inference]

**Do**
1. Decide the shader exists to "fill out" the skyline, meaning the foreground city is presumably authored or higher-fidelity, and the shader supplies background massing.

**Check**
- The title's word "fill" is the only scope cue: background fill, not hero buildings.

**Why**
Background buildings buy depth cheaply; no viewer will inspect them, so they can be pure shader output.

### Phase 2: Author buildings as shader code, not meshes [inference]

**Do**
1. Generate building facades, windows, and silhouettes procedurally inside the shader rather than modeling assets.
2. Tune for the cyberpunk look (neon-lit windows, varied heights), since that is the stated art direction.

**Check**
- Cannot be checked: no parameters, no code, and no author description were posted.

**Why**
A shader can produce an unbounded number of varied buildings at near-zero asset cost, which is the standard motivation for this approach.

### Phase 3: Integrate with the city scene [inference]

**Do**
1. Place the shader-driven buildings behind/around the main city geometry so the skyline reads as dense.

**Check**
- The demo clip presumably shows the composite, but the clip itself was not transcribed or frame-analyzed for this reconstruction.

**Why**
Skyline fill only works in context: it must sit behind the authored foreground and match its lighting and atmosphere.

### The human method, distilled
1. **Background massing is a shader problem, not an asset problem.** (from the title: shader, not authored assets)
2. **Scope honesty:** this reconstruction is title-only; phases 1-3 are inferred scaffolding, not reported fact.

**Depth status:** DEPTH-LIMITED (title-only sourcing: no selftext, no comments, no stated tools or parameters)

---

## 10. "procedural backrooms in the browser" (u/pablostanley)
Source: https://v.redd.it/v492vggifpqh1 | r/proceduralgeneration post 1wlm2w9 (score 21) | native clip (demo, not tutorial)

The clip is a demo, not a narrated workflow. All technique detail comes from the author's post selftext (which reads as a compact architecture summary). The four comments add no technique detail (two praise the scares, one asks about an unrelated site, one jokes about a pool). The project is playable at vackrooms.vercel.app and open source (MIT) at github.com/pablostanley/vackrooms; the repo was not audited for this reconstruction (no downloads per task rules).

Tools used: Browser (client-side), WebGPU via vgpu with a WGSL post-processing pipeline, GLSL fallback for WebGL2.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Feed photogrammetry only the frames that matter: score frames for quality and overlap, extract the best, skip the rest.
### Phase 1: Generate everything client-side from a seed

**Do**
1. Seed the generator and produce, all in the browser: the rooms, furniture, places, and the audio acoustics.
2. Keep generation fully client-side (no server round-trips for world content).

**Check**
- Same seed must reproduce the same rooms, furniture, places, and acoustics.
- Acoustics included: the procedural audio reverb/echo model is part of the seeded output, not a fixed preset.

**Why**
Seeded client-side generation means the game ships as code, not content: infinite backrooms with a static hosting footprint (it lives on vercel.app as a static deploy).

### Phase 2: Stream a 3x3 window of 57m sections

**Do**
1. Divide the world into 57m square sections.
2. Stream a 3x3 window of sections around the player (a 171m x 171m active area), loading/unloading as the player moves.
3. Let sections regenerate as the player wanders (regeneration is expected, not a bug).

**Check**
- The active window must follow the player without hitches at section boundaries.

**Why**
A fixed 3x3 window bounds memory and draw cost no matter how far the player roams; regeneration is safe because everything derives from the seed.

### Phase 3: Keep doorways aligned with shared boundary hashes

**Do**
1. When neighboring sections regenerate, align their doorways using shared boundary hashes.

**Check**
- Walk through a doorway into a freshly regenerated section: the doorway on both sides must line up and connect.

**Why**
Independent section generation would otherwise produce doorways that do not meet. A shared boundary hash gives adjacent sections a common reference so their portals agree without either section storing the other.

### Phase 4: Grade the VHS look as a WGSL post pipeline

**Do**
1. Apply the VHS look as a post-processing pipeline written in WGSL with vgpu: warp, tracking errors, chroma offset, and bloom.
2. Provide a GLSL fallback path for WebGL2 browsers.

**Check**
- The look must hold on WebGPU (WGSL) and degrade gracefully on WebGL2 (GLSL).

**Why**
Doing the VHS grade in post keeps the world renderer clean and lets the retro look be tuned independently of the geometry; the GLSL fallback preserves reach on browsers without WebGPU.

### Phase 5: Drive the creature with bounded A* and real frustum visibility

**Do**
1. Move the creature with bounded A* (pathfinding with a bounded search budget).
2. Gate its movement on actual frustum visibility: it only moves when the player really cannot see it.

**Check**
- [Inference] The classic Weeping-Angel rule is enforced geometrically (frustum test), not by timers: if any part of the creature is inside the camera frustum and visible, it freezes.

**Why**
Frustum-gated movement is what makes the scare work: the creature advances only in the player's blind spots, which is exactly the behavior the commenters reacted to ("screamed," "those skinny dudes scared the shit outta me").

### The human method, distilled
1. **Seed covers everything, including acoustics.** Rooms, furniture, places, and audio reverb all derive from one seed.
2. **Bounded active window, unbounded world.** A 3x3 grid of 57m sections streams around the player; memory stays flat.
3. **Shared boundary hashes for portal agreement.** Neighbors agree on doorways through a common hash, not stored state.
4. **Retro look as a separable post stage.** WGSL pipeline (warp, tracking errors, chroma offset, bloom) with a GLSL fallback for reach.
5. **Horror AI keyed to real visibility.** Bounded A* movement gated by an actual frustum check, so the creature only moves unseen.

**Depth status:** DEPTH-LIMITED (author selftext is an architecture summary, not a narrated workflow; the four comments add no technique detail; the linked MIT repo was not audited)

---

# Photogrammetry/SfM + Houdini tooling: reconstructions

Full-depth workflow reconstructions of audited videos, in the style of the cinematic-cavern workflow guide. Each section: source line, tools used, phased Do / Check / Why, distilled principles, depth status. No per-repo have-vs-need judgments. [inference] marks anything not stated in the sources.

---

## 11. "Adaptive video frame extractor for photogrammetry/SfM" - WearyFortune7055

Source: https://v.redd.it/d88gwsgctinh1 | r/photogrammetry post 1w77cpe (score 48) | native clip (demo, not tutorial)

The video is a screen recording of the GUI app in basic use. The workflow below is reconstructed from the post text (the feature set as shipped) and the comment thread (the community's additions, the creator's counter-positions, and the pain points that motivated the tool). Repo: https://github.com/morishuz/adaptive-frame-extractor

Tools used: adaptive-frame-extractor (native C++ desktop app, macOS/Windows/Linux builds, runs locally, no Python setup), COLMAP, Gaussian Splatting / NeRF pipelines, Meshroom/AliceVision (KeyframeSelection, the incumbent the tool is measured against), JPEG and PNG output, CSV per-frame metadata.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Sell the engine, not the app: headless Houdini Engine behind an async queue and server pool, with deterministic VDB-and-math topology at the core.
### Phase 1: Load video and set timeline regions

**Do**
1. Open the video in the GUI. Scrub the timeline to find the capture sections that matter.
2. Mark multiple timeline regions for the sections you want to keep. Different passes, different takes, or cutting a turntable pause out of the middle of a clip are all region material.
3. Give each region an optional separate output folder so the frames from different passes do not mix downstream.

**Check**
- Regions are the unit of work, not the whole clip. A region you would not run COLMAP on should not send it frames.

**Why**
The camera motion, and therefore the right frame spacing, changes across a capture session. Regions let one extraction pass treat each part on its own terms, and separate folders keep multi-pass scans separable when you get to reconstruction.

### Phase 2: Adaptive extraction (motion-driven spacing)

**Do**
1. Run the adaptive extractor instead of pulling every Nth frame. Frame spacing follows estimated camera motion.
2. Expect: fewer near-duplicate frames when the camera is barely moving, denser frame spacing during faster movement and rotation.

**Check**
- The principle the creator names explicitly: "keyframe" here means frames that are important for Structure-from-Motion reconstruction. The extractor does not distinguish I vs P/B frames, and in the creator's words "in practice an I-frame is not necessarily higher quality or lossless."
- Sanity-check the density balance: if a slow sweep yields the same frame count as a fast one, the motion model is not doing its job.

**Why**
Fixed-interval extraction wastes frames on the boring parts and starves the parts where parallax actually changed. Motion-adaptive spacing spends the frame budget where the geometry information is. This is the tool's whole argument for existing, and it is aimed squarely at Meshroom/AliceVision's KeyframeSelection being, in a user's words, "painfully, painfully slow."

### Phase 3: Manual curation pass

**Do**
1. Use manual extraction of individual frames to add any specific frame you care about, and remove frames you do not want before export.
2. For clips where adaptive logic is wrong for the material (a scan that is all slow, deliberate rotation), fall back to regular fixed-interval extraction, which the app also supports.

**Check**
- Fixed-interval remains in the toolbox on purpose: adaptive is the default, not the only mode.

**Why**
No automation model understands intent. The manual layer is the creator's acknowledgment that artists using this tool know their capture better than the motion estimator does.

### Phase 4: The blur question (creator's position, not a feature)

**Do**
1. Do not build a blur-rejection stage into your expectations of this tool. The creator's stated position: measuring blur and working around blurry frames is "surprisingly tricky to do well" and has "very little payoff."
2. Instead, let registration do the filtering: if a frame is too blurry for structure-from-motion, it will essentially fail to get registered. "No harm done. Perhaps it cause a bit of extra runtime."

**Check**
- This is the contested point of the thread. The counter-ask from the community (NorthernBaseOfficial, Skinkie): a per-frame quality score based on sharpness, exposure, and motion blur, letting the user "quickly remove the weakest ones before exporting."
- Note the community's practical context: TheDailySpank runs "questionable videos" (bad lighting, auto shutter) through Meshroom's KeyframeSelection precisely because its options are richer, despite the speed.

**Why**
Two philosophies collide here. The creator treats blur rejection as an unsolved measurement problem whose failure mode is cheap (unregistered frames cost compute, not correctness). The community wants a score, not a gate: let the human decide on a sorted list. If you implement the score, make it advisory, not automatic, or you have sided with the wrong camp.

### Phase 5: Coverage and overlap check before the long run

**Do**
1. Before export, look at the timeline for sections with too little camera movement or sudden jumps in camera position. In the community's requested version of this feature, those sections get highlighted on the timeline as warnings.
2. Treat a sudden jump as a scan-break risk and a low-movement stretch as a parallax deficit.

**Check**
- The value is measured against the cost of discovery: you want to catch a coverage gap before starting "a long COLMAP or Gaussian Splatting run," not after.

**Why**
Reconstruction failures are cheapest to fix at the frame-selection stage and most expensive to fix after hours of COLMAP. A timeline warning converts a silent downstream failure into a visible upstream decision.

### Phase 6: Export with metadata

**Do**
1. Choose JPEG or PNG output per region.
2. Export and review the extraction summary, plus the CSV with detailed metadata for every selected frame.

**Check**
- The CSV is the audit trail: it records which frames were selected and why, so a failed reconstruction can be traced back to the frame set rather than re-extracted blind.

**Why**
Reproducibility matters in capture work. If a COLMAP run fails on pass three, the summary and CSV let you compare what changed in the frame set instead of guessing.

### Phase 7: Background removal decision (the SAM suggestion)

**Do**
1. Decide whether your subject is an object scan. Proper_Rule_420's case: scanning objects, the background is "useless information" that slows SfM, and they patched the older CLI themselves with "a simple threshold on detected non-moving points," which "worked ok but was not the best."
2. Their recommendation: try SAM (Segment Anything), specifically SAM 3, which they describe as "quite easy to use (input words)" and "actually working great." The creator confirmed the app currently has no background remover ("no it does not") and asked about the use case before committing.

**Check**
- This is a niche need, acknowledged as such by the requester ("it might be a very niche need"), and the creator is still in the use-case-gathering stage. Treat SAM integration as proposed, not shipped.

**Why**
Background masking is a pipeline step, not a quality score: it changes what SfM is allowed to match, not just which frames it gets. The threshold-on-static-points hack worked acceptably, which tells you the bar for a first shipped version is lower than it looks, but SAM 3's text-prompted masks are what make it usable for artists instead of programmers, the exact audience the GUI rewrite was for.

### The human method, distilled

1. **Spend the frame budget on motion.** Adaptive spacing is the whole tool; fixed interval is the fallback, not the rival.
2. **Regions before frames.** Organize the capture into regions first, then let extraction run inside them, with separate output folders per region.
3. **"Keyframe" means SfM-important, not codec-important.** Do not prefer I-frames; an I-frame is not necessarily higher quality or lossless.
4. **Let registration filter blur; do not gate on it automatically.** A blurry frame that fails to register costs runtime, not correctness. If you add a quality score, make it advisory and let the human sort.
5. **Warn before the long run, not after.** Overlap/coverage warnings on the timeline exist to be read before COLMAP or Gaussian Splatting starts, because that is where the cost sits.
6. **Export the audit trail.** The per-frame CSV is what makes a failed reconstruction debuggable instead of repeatable.
7. **Background removal is a pipeline decision, not a quality filter.** Masking changes what SfM may match; thresholding static points is the minimum viable version, SAM 3 with text prompts is the artist-friendly one.

**Depth status:** FULL (post feature list is complete, comment thread is substantive; the native clip's screen-recorded steps are unseen, but the reconstruction is grounded in what the creator and commenters stated).

---

## 12. "Procedural jewelry system on Houdini Engine (B2B SaaS)" - Plane-Good-6147

Source: https://v.redd.it/im6mq9nu9prh1 | r/houdini post 1wq2fi7 (score 59) | native clip (demo, not tutorial)

The video shows procedural geometry being generated and returned to a web interface. The post is a request for technical feedback; the architecture below is reconstructed from the creator's numbers and the comment thread's licensing reality check. Product page: https://beka3d.com/jewelcore/

Tools used: Houdini Engine (headless geometry engine), VDBs, Houdini math/solver networks (the deterministic core), an async queue and server pool in front of the Engine licenses, a web interface as the user-facing application, community references to docker-based Houdini web-server tooling (e.g. https://github.com/mushyfruit/houdini-web-rendering-interface as prior art).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Implement the paper, don't approximate it: a two-way coupled bubbles solver built from the whitepaper's equations in vanilla Houdini nodes.
### Phase 1: Build the procedural core as a deterministic asset graph

**Do**
1. Build the jewelry generator as a Houdini asset graph intended to run headless under Houdini Engine, not as a user-facing Houdini session.
2. Use VDBs and Houdini's math throughout. In the creator's words, this makes "topology fully deterministic."

**Check**
- Deterministic topology is the manufacturability prerequisite: the same inputs must produce the same geometry every time, because downstream tolerances and production tooling depend on it.

**Why**
When Houdini runs as a geometry engine behind a web app, there is no artist in the loop to fix a bad cook. The asset has to be a reliable function of its inputs. VDBs give watertight, topology-stable intermediates; Houdini's math keeps the whole graph recomputable rather than hand-tweaked.

### Phase 2: Put the Engine behind an async queue, not dedicated sessions

**Do**
1. Do not give users dedicated Engine instances. Run requests through an async queue feeding a server pool of Engine workers.
2. The pool exists because of the cook times: base updates return procedural geometry to the web interface in under 1 second; high-precision geometry for production takes around 3 seconds.

**Check**
- The creator's own scaling claim: because base updates take under 1s and production previews take ~3s, "users don't hold dedicated instances open," so "just a few Engine licenses can easily handle hundreds of concurrent requests (which translates to thousands of general users)."

**Why**
The queue is what turns per-seat licensing into a shared resource. A request occupies a license for seconds, not hours, so license concurrency, not user concurrency, is the unit of capacity. This is the load-bearing architectural decision in the whole project.

### Phase 3: Size the license pool from measured cook times

**Do**
1. Measure the two cook tiers separately: interactive base updates (<1s) and production previews (~3s). These numbers are the capacity model.
2. Buy licenses to cover concurrent cooks, not concurrent users. The creator's math: a few licenses for hundreds of concurrent requests.

**Check**
- Keep the two tiers honest: the sub-1s tier is what makes the web UI feel interactive; the ~3s tier is what makes production output trustworthy. If the base tier slips past a second, the queue model still works but the product stops feeling live.

**Why**
Licensing cost is the scaling variable, so every performance win in the asset graph directly reduces the license pool. The queue architecture and the deterministic topology both serve the same goal: minimum cook time per request, because each second of cook time is a slice of a $525/year license.

### Phase 4: Confront the licensing reality before scaling

**Do**
1. Check the Houdini Engine license terms for SaaS use. The comment thread's flag (jwdvfx): "not sure that the standard Houdini Engine seats would cover it being run for other users."
2. Price it: $525 per head per year (per i_am_toadstorm, from SideFX's website). The top-voted skepticism in the thread (i_am_toadstorm, score 4): "The only real concern with scaling up an application like this is the dependency on Houdini Engine... those license costs add up, so the feasibility of something like this really depends on how many simultaneous users you're planning on having. If this is meant to be customer-facing you will not be able to afford it."

**Check**
- The creator acknowledges the scaling question and counters it with the queue math, but does not claim the SaaS licensing question is resolved in the thread.

**Why**
The scaling constraint here is legal, not technical. The architecture scales; whether the standard seat covers a SaaS deployment is a contract question, and it has to be answered with SideFX before the user count grows, because a retroactive answer changes the unit economics of the entire product.

### Phase 5: Validate manufacturing tolerances with real production

**Do**
1. Fine-tune every real-world tolerance against actual production runs, not just against the geometry in the viewer. The creator: deterministic topology is established by the VDB/math core, "but fine-tuning every single real-world tolerance will definitely require direct production testing."

**Check**
- Deterministic geometry is necessary but not sufficient for manufacturing. The check is a produced piece, not a render.

**Why**
Jewelry has to be made, not just previewed. Casting, milling, and setting impose tolerances the asset graph cannot derive from first principles; the feedback loop from the shop floor back into the procedural graph is part of the product, not a one-time calibration.

### Phase 6: Ship as closed B2B, then early access

**Do**
1. Keep it a strictly B2B pipeline tool (the creator's own framing, not a consumer configurator).
2. Launch sequence as stated: closed testing now, Early Access in about a month, waitlist at beka3d.com/jewelcore, live demo access codes by DM for specific workflows or use cases.

**Check**
- The B2B framing is load-bearing: a pipeline tool has fewer, more tolerant users than a consumer product, which is exactly what a seconds-per-cook queue architecture can serve.

**Why**
The go-to-market matches the architecture. "Strictly B2B" means each account is a production pipeline with predictable cook patterns, which is the usage profile an async pool can actually guarantee. The waitlist and demo codes are how you validate the queue under real load before opening the floodgates.

### The human method, distilled

1. **Houdini as engine, not as app.** Headless procedural cooking behind a dedicated interface is a different product category from user-facing CAD.
2. **The queue is the product.** An async queue with a server pool turns per-seat licenses into a shared resource; without it the licensing math does not work.
3. **Size licenses by cook time, not user count.** Sub-1s base updates and ~3s production previews are the capacity model; a few licenses cover hundreds of concurrent requests because nobody holds an instance open.
4. **Deterministic topology first.** VDBs plus Houdini math make the asset a reliable function of its inputs, which is the prerequisite for headless production use.
5. **The scaling constraint is legal.** Standard Engine seats may not cover SaaS-for-other-users; resolve the contract with SideFX before scaling, because it changes unit economics.
6. **Manufacturing tolerances need the shop floor.** Deterministic geometry does not equal manufacturable geometry; production testing is a standing feedback loop, not a milestone.
7. **B2B matches the architecture.** A pipeline tool's predictable cook patterns are what an async pool can guarantee; ship closed, validate under load, then open early access.

**Depth status:** FULL (post numbers and the licensing thread are concrete; the asset internals shown in the clip are unseen, but the SaaS-architecture reconstruction is fully grounded in the creator's stated figures and the comment discussion).

---

## 13. "Two-Way Coupled Bubbles Solver | Weta FX Whitepaper Implementation" - CdvrSzf

Source: https://v.redd.it/eh53g0sb82qh1 | r/houdini post 1wiqmdp (score 286) | native clip (demo, not tutorial)

The video shows the solver results (Rubber Toy test at 00:16, underwater head test at 00:06). The implementation workflow below is reconstructed from the creator's post text and the unusually technical comment thread, where another implementer (diskl0sure) compares notes on the exact projection step. Parameters and test timings are the creator's own numbers.

Tools used: Houdini (vanilla nodes only, no custom plugins), Gas Project Non Divergent Variational (the vanilla projection node doing the heavy lifting), FLIP/Whitewater-adjacent tooling as the baseline being replaced, the Weta FX two-way coupled bubbles whitepaper (Equations 17/18, Section 3.4, Section 3.5 fb clamp).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Drive the DCC with agents: MCP servers loop an agent between Blender and Unreal, and the human inspects every step.
### Phase 1: Define what the native solver cannot do

**Do**
1. Start from the limitation of Houdini's native Whitewater solver: its one-way coupling model. The FLIP velocity field pushes the bubbles; buoyancy is a constant vector.
2. Confirm where that breaks: it holds up for mid- and background elements but "falls short for hero-scale simulations," which is what forces artists onto the Pyro + POP Advect by Volumes workaround.

**Check**
- The hero-scale test is the acceptance criterion. If the fix only improves background elements, it is not worth a custom solver.

**Why**
Rewriting a solver starts with a precise statement of the native one's failure mode. One-way coupling is fine until the bubbles are the subject; the whitepaper implementation exists because hero shots needed the water to push back.

### Phase 2: Adopt the whitepaper, scope the simplification

**Do**
1. Work from the Weta FX whitepaper on two-way coupled bubbles.
2. Implement the inertia-unaware case (theta = 0) from Equation 18 first. The creator is explicit: the inertia-aware system is not yet implemented, "but I'm actively working on it."

**Check**
- Scope honesty matters here: theta = 0 is a stated simplification, not a hidden one. The inertia-aware case is open work, named as such.

**Why**
A full whitepaper replication is a multi-month project; shipping the theta = 0 case first gets a working two-way solver into shots while the harder case is still in development. The simplification is a sequencing decision, not a compromise of the method.

### Phase 3: Model bubbles as ideal spheres with f@pscale radii

**Do**
1. Treat each bubble as an ideal sphere with radius stored in the f@pscale attribute.
2. [inference] This is the POP-level particle representation; the sphere assumption is what makes the volume math tractable.

**Check**
- Every downstream force and multiplier is a function of bubble volume derived from this radius, so the pscale values have to be trustworthy before anything else.

**Why**
"Ideal sphere" is the modeling contract with the paper. It trades bubble-deformation realism for a volume integral you can actually compute, and the creator's results show the organic look comes from the coupling, not the bubble shape.

### Phase 4: Rasterize bubble volume onto the voxel grid

**Do**
1. Rasterize each bubble's volume onto a voxel grid. This rasterized volume is "the primary multiplier for all forces and operations."
2. From the collective bubble volume, derive the displaced liquid volume and adjust the fluid's density and velocity accordingly.

**Check**
- The rasterization is where particle space becomes grid space. If the volume field is wrong, every force built on it is wrong in the same direction.

**Why**
Two-way coupling needs the water to know where the bubbles are in its own language, which is a grid. Volume as the primary multiplier means every force scales with how much water was actually displaced, which is the physical content of the whole method.

### Phase 5: Project pressure with a vanilla Gas Project Non Divergent Variational

**Do**
1. Build the pressure projection from the vanilla Gas Project Non Divergent Variational node, with what the creator calls "a few minor simplifications," replicating the core logic of the Weta paper.
2. Implement the theta = 0 system as a one-phase variational projection: collect a combined velocity field (fw * u + fb * v) with one effective density (water density + implicit drag force contribution), run it through Gas Project Non Divergent Variational, then decompose the result back to the water velocity.
3. Add the fb clamp from Section 3.5 to keep the system stable.

**Check**
- The other implementer in the thread (diskl0sure) got stuck at exactly this stage and proposes the same Utemp = fw * u + fb * v blend, with an open question about algorithm order: the paper's Section 3.4 says "With the solution for P available, u is readily computed from the first equation in (17)," implying velocity and pressure are evaluated simultaneously via Equation 18, and diskl0sure suspects they "got the algorithm order wrong during the Newton iterations."
- The creator's decisive result: "There is no synthetic buoyancy vector here: upward motion emerges physically, driven by the fluid pressure gradient from high-pressure zones to low-pressure ones."

**Why**
The no-synthetic-buoyancy result is the proof the projection is right. Constant-vector buoyancy is what the native solver does; if your two-way solver still needs one, you have rebuilt the one-way solver. The fb clamp is the stability price of the combined-field formulation.

### Phase 6: Time it on real shots (M4 Max benchmarks)

**Do**
1. Run the canonical tests and record wall-clock times. The creator's numbers, on a MacBook Pro M4 Max:
   - Rubber Toy test: 1 hour 43 minutes (demo video, 00:16)
   - Underwater head test: 1 hour 35 minutes (demo video, 00:06)
   - Sphere falling into water: about half an hour ("noticeably faster")
2. Treat optimization as open work: "The solver needs to be improved, and I think I have a little room for optimization."

**Check**
- [inference] RAM requirements were asked about (kastef) but not answered with numbers in the visible thread. Do not quote a RAM figure.

**Why**
Sim times are the production reality check. Sub-2-hour hero sims on a laptop put this in the usable range for real shots, but the spread between tests (30 min vs 103 min) says scene-dependent cost dominates, which is where optimization effort should go first.

### Phase 7: Name the remaining work

**Do**
1. Finish the foam solver on the water surface.
2. Fix the remaining "unpleasant technical limitations" (the creator's phrase; unspecified in the thread).
3. Pursue the inertia-aware system from Equation 18.

**Check**
- A community member already wants the HDA ("Lol somebody just needs to make a whitewater solver 2.0 hda that people can download"), and the creator has not committed to releasing one. Do not present an HDA as available.

**Why**
Shipping the roadmap publicly is how a solo whitepaper implementation becomes a tool other artists can use. The foam solver and the technical limitations are the gap between a working solver and a usable one; the inertia-aware case is the gap between the simplification and the paper.

### The human method, distilled

1. **Name the native solver's exact failure mode first.** One-way coupling with constant-vector buoyancy is fine for background, fatal for hero. That is the whole justification.
2. **Implement the scoped case, ship it, then extend.** Theta = 0 from Equation 18 is a stated simplification and a working solver beats a complete plan.
3. **Ideal spheres buy you the volume integral.** The organic look comes from the coupling, not from deforming the bubbles.
4. **Rasterize volume to make particles speak grid.** The rasterized bubble volume is the primary multiplier for every force; displaced liquid volume drives the density and velocity adjustments.
5. **Vanilla nodes can carry the paper's core logic.** Gas Project Non Divergent Variational plus a combined field (fw * u + fb * v), one effective density, decomposition back to water velocity, and the Section 3.5 fb clamp.
6. **No synthetic buoyancy is the test of correctness.** If upward motion does not emerge from the pressure gradient, you have rebuilt the one-way solver.
7. **Benchmark on real shots, optimize what varies.** 1h43m, 1h35m, and ~30m on an M4 Max; the scene-dependent spread is where the optimization lives.

**Depth status:** DEPTH-LIMITED (the clip's node graph and exact parameter values beyond f@pscale are unseen; the reconstruction is grounded in the unusually detailed comment thread, but sim internals, the foam solver, and the inertia-aware path are not visible in the sources. [inference] marks the thin spots).

---

---

# Agentic DCC workflows: reconstructions

Reconstructions of three audited videos. Same format as the cinematic-cavern guide:
source line, tools used, phased sections each with Do / Check / Why, exact
parameters and names wherever the source gives them, distilled principles.
Anything inferred is marked [inference].

---

## 14. "How to Make Realistic Rust Materials" (Loic Anquetil)

Source: https://v.redd.it/9oiwcc43mhrh1 | r/Substance3D post 1wp51i2 by P_Gresty
(score 39, 0 comments) | native clip (demo, not tutorial)

Tools used: Substance 3D Designer (primary authoring tool), Substance 3D
Assets (publishes the "Desirable Patina" Signature Collection: 24 assets
covering rust, paint with rust, 3D materials, and procedural texture
generators), the artist's own reference photography.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Texture characters as a pipeline: bake mesh maps, build materials in layers, keep the stack editable.
Creator context (from the post and the 80 Level article it links):
Loic Anquetil, Senior 3D and Material Artist at Ubisoft Montpellier; credits
include Rayman Legends Retold, Ghost Recon Breakpoint, and Prince of Persia:
The Lost Crown; also a 3D teacher (Rubika, CG Academy). The reconstruction
below is grounded in the 80 Level article the post advertises as containing
"Loic's behind-the-scenes secrets"
(https://80.lv/articles/desirable-patina-how-to-make-realistic-rust-in-3d);
the post selftext alone only summarizes it.

### Phase 1: Study the material before building anything

**Do**
1. Take your own reference photos whenever you encounter interesting rust in
   everyday life. Stock/reference images are "too distant or stylized" to
   reveal the material's structure.
2. Decipher rust's "surface language": even inside a limited brownish-orange
   range there are micro-variations, tiny shifts in tone, small accents,
   unexpected transitions.
3. Reorder your research: the artist started thinking color exploration would
   be the main area, then shifted to granularity and microstructure. Understand
   rust structurally before tackling its color range.

**Check**
- Can you describe the grain and relief vocabulary, not just the color?
  Production rust references even showed "fluorescent tones, vibrant oranges,
  greens, blues" that read like abstract paintings.

**Why**
"With rust, studying the physical complexity of the material comes before
anything else." Casual looking sees one brownish-orange; the believable
material lives in the micro-detail.

### Phase 2: Establish one foundation material that sets the structural logic

**Do**
1. Build "Coarse Rust Pitting" first. It was the material he struggled with
   most, and it "laid the groundwork for everything else."
2. Nail three relationships: the breakup patterns, the relationship between
   height and roughness, and how color variation interacts with surface detail.

**Check**
- The foundation is solid before anything layers on top. Once it is, "the
  rest of the collection could become more fluid and playful."

**Why**
One solved structural core unlocks everything downstream: peeling paint,
blended corrosion stages, dirt and accumulation. Time, exposure, and
environment then "begin to tell the story of an object."

### Phase 3: Build the noise generators from scratch, fast-mockup first

**Do**
1. Work primarily with single grayscale outputs; focus on blending noises
   together.
2. Loop: study references, take photos, make quick mockups in Designer; once
   you like the result, rebuild it properly in procedural form.
3. Borrow the collage mindset from his graphic-design background (physically
   painting and scanning surfaces in earlier jobs): take disparate elements,
   mix, transform. Test question he asked himself: "If I take a wood texture,
   recolor and distort it, can it become rust?"
4. Target the noises that carry weathered metal: patina, erosion, and water
   streaks; also corrosion flaws.

**Check**
- Do the noises simulate water streaks and corrosion flaws while staying fully
  procedural?

**Why**
"Noises are fundamental resources in material creation. We always need them."
Building them from scratch is both control and craft; production schedules
normally deny him the time.

### Phase 4: Reverse-engineer the built-in nodes instead of fighting them

**Do**
1. Open Designer's graphs and base noises, access their internal data, modify
   them, add parameters, rebuild parts of their logic. "All the noises in this
   project went through that reinterpretation."
2. Keep graphs clean and organized: clean structure, logical grouping, clarity.
   Chaotic "spaghetti" graphs "aren't helpful to other artists."

**Check**
- [inference] Another artist can open the graph, follow the logic, and modify
  it. "Even if the result looks complex, it shouldn't feel intimidating."

**Why**
"Nothing is truly closed" in Designer, and "reverse engineering is one of the
most powerful ways to learn." Taking shortcuts that make sense "isn't
cheating, it's efficiency"; production deadlines are real.

### Phase 5: Layer the corrosion story, keep the graphs readable

**Do**
1. Introduce peeling paint, blend stages of corrosion, add subtle dirt and
   accumulation on top of the foundation material.
2. Keep every graph organized and readable as you layer, per Phase 4.
3. Balance: materials must be expressive but "production-ready and adaptable";
   they "need to be parametrized, reused, and shared." A material should look
   good AND be controllable.

**Check**
- Expressive but adaptable: can the parameters serve art direction, gameplay
   needs, and realistic constraints, not just self-indulgence?

**Why**
In production, materials serve a defined framework. His professional mindset
"returned quickly": the collection had to balance artistic exploration with
functional utility.

### Phase 6: Work the toolbox, not the system

**Do**
1. Deliberately break the controlled, analytical habit: mix noises
   instinctively, plug nodes together "just to see what would happen," stop
   overthinking.
2. Treat each node as a brush, a pair of scissors, a texture stamp. "You mix,
   you test, you react."

**Check**
- Some experiments are terrible, some are incredible. Keep the incredible
   ones: "Some of those experiments are now part of my daily workflow."

**Why**
Total mastery killed his spontaneity ("I could visualize a material and
instantly know how to build it. There was no room left for accidents or
surprises. That's a dangerous place for an artist."). Designer as a creative
toolbox is what makes it approachable.

### Phase 7: Publish as a reusable collection

**Do**
1. Ship the 24 assets as the "Desirable Patina" Signature Collection on
   Substance 3D Assets, with clean, organized graphs so other artists can
   open, study, reorganize, hack, and rebuild them.

**Check**
- The work "continues beyond the collection" when someone opens a graph,
  modifies it, and creates something new.

**Why**
Shared, parametrized, readable materials compound; locked black boxes do not.

### The human method, distilled

1. Study before building: understand the material structurally
   (microstructure before color).
2. Take your own references; stock photos are too distant or stylized.
3. Solve one foundation material that establishes the structural logic
   (breakup, height-to-roughness, color-to-detail), then layer fluidly.
4. Mock up fast, rebuild properly once it reads right.
5. A small node set used intelligently beats ultra-technical graphs; you do
   not need custom functions everywhere or Pixel Processor nodes in every
   direction.
6. Reverse-engineer built-in nodes; nothing is closed, and shortcuts that make
   sense are efficiency.
7. Clean, organized graphs are a feature: readability for the next artist.
8. Treat Designer as a creative toolbox, not a technical system; leave room
   for accidents.
9. Balance exploration with utility: expressive, but parametrized,
   production-ready, and shareable.

**Depth status:** FULL (grounded in the 80 Level article the post itself links
as the source of the behind-the-scenes method; the clip and post selftext
alone would be thin, since the post has 0 comments).

---

## 15. "I Used Substance Painter to Texture my Characters!" (SpencerJDev)

Source: https://v.redd.it/0sg7ad4lrxph1 | r/Substance3D post 1wi7qbh (score 36,
1 comment thread: "that cat is awesome i love it lol", "Nice!") | native clip
(demo, not tutorial)

Tools used: Substance 3D Painter (stated). Characters are for the
creator's animation work (stated: "keep up with my animation work").

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Direct the agent, inspect the cut: give the agent game access plus a creative brief, then curate its cinematic output.
### Phase 1: Block the character textures procedurally

**Do**
1. Texture the characters "mainly" with procedural techniques (stated).
   [inference] In Painter this means generator- and mask-driven layers
   (curvature, AO, edge wear style masks) rather than fully hand-painted
   maps, but no specific generators, brushes, or maps are named in the
   source.
2. [inference] Keep the work in a layered, editable stack so the procedural
   base stays live.

**Check**
- [inference] The procedural pass covers the character consistently with no
  baked-in decisions that block later changes.

**Why**
- The stated reason for loving Painter is "the non-destructive workflow":
  procedural layers stay editable, so design changes do not mean repainting.

### Phase 2: Hand-paint details on top

**Do**
1. Add hand painting on top of the procedural base (stated: "mainly
   procedural techniques with some hand painting on top").
2. [inference] Reserve hand painting for hero details and character-specific
   accents the procedural pass cannot reach.

**Check**
- [inference] The painted details read at the character's on-screen distance
  without fighting the procedural base.

**Why**
- [inference] Procedural for coverage and consistency, hand-painted for
  character. The split keeps the bulk of the work editable while the unique
  details stay authored.

### The human method, distilled

1. Non-destructive first: keep every decision editable for as long as
   possible. (stated as the reason he loves the tool)
2. Procedural base, hand-painted top: let generators do the coverage, reserve
   the brush for what only a human eye places. (stated, in his words: "mainly
   procedural techniques with some hand painting on top")
3. [inference] Texture for the final medium: these characters exist for his
   animation work, so the texturing only has to survive the camera, not a
   portfolio close-up.

**Depth status:** DEPTH-LIMITED (the entire method statement is two sentences
in the selftext plus two trivial comments; no layers, generators, brushes,
maps, bakes, or export settings are named anywhere in the source).

---

# Simulation workflows: reconstructions

Sections 17-19. Reconstructed from Reddit post metadata, selftext, and comments only.
No video transcripts were available (all three are native v.redd.it demo clips).
Anything not stated by the sources is marked [inference].

---

## 16. "I gave claude access to my cozy tower defense game, and asked it to make a cinematic trailer. It interpreted my game as a horror-movie." (illadann7)

Source: https://www.reddit.com/r/aigamedev/comments/1wrgmaw | r/aigamedev post 1wrgmaw (score 91) | native clip (demo, not tutorial)

Tools used: Claude (agent/director), Unity (read-only access via MCP), OpenRouter API, Veo 3.1 lite (video generation, reached through OpenRouter), browser access (agent used it to monitor the OpenRouter page). A high-quality text-to-speech model was requested in the prompt but the agent did not use it. Game: "The Endless Harvest" (cozy tower defense; Steam app 5052960).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Fake fracture at scale: an 890k-particle Material Point Method sim with Voronoi-cell fracture, inside Blender.
### Phase 1: Grant the agent read access to the game

**Do**
1. Give Claude MCP access to the Unity project with an explicit read-only
   constraint. The prompt's access clause: "Look at my game, dont change
   anything inside the game itself, I only gave it so you read through it,
   so you know what it is about."
2. Give it API access to OpenRouter, plus browser access so it can monitor
   the OpenRouter page.

**Check**
- The game itself was not modified (no changes reported; the constraint held).

**Why**
A trailer agent needs source-material understanding without the risk of it
editing the game. Read-only access plus a written no-changes rule is the
safest way to let an agent study a project.

### Phase 2: Prompt with constraints, a budget, and autonomy

**Do**
Issue one prompt carrying style, resources, budget, length, and autonomy
(OP pasted it verbatim in the post and in comments):

"Look at my game, dont change anything inside the game itself, I only gave
it so you read through it, so you know what it is about. please make a
video with a cinematic editing style with quick and snappy storytelling.
use different angles and lighting to make it seem like a professional
cinematic trailer for the game. you may use openrouter for assets, use a
budget of 10$ max. Use high quality text-to-speech model for generation.
You can use any tools you can find access to and resources on the internet.
You create the script, the assets, the animation, everything. Work
autonomously until done. Quality is paramount. Make the trailer be
~45 seconds."

**Check**
- Prompt text is identical in post selftext and the OP's comment reply.

**Why**
Constraints (cinematic style, $10 budget, ~45 seconds) plus full autonomy
("Work autonomously until done", "You create the script, the assets, the
animation, everything") turn an open-ended agent loose with guardrails.

### Phase 3: Agent reads and interprets the game

**Do**
Let the agent read through the project via the Unity MCP connection. No
specific reading instructions were given beyond the access grant.

**Check**
- Interpretation was half right: OP says the agent "got the details and
  assets of my game quite right" and "the final shot of my boss is
  especially amazing", but it read the cozy tower defense game as a
  horror movie.

**Why**
Interpretation quality shows in the details even when the overall genre
read is wrong. The details came from actually reading the project; the
genre miss came from the open-ended prompt (see Phase 6).

### Phase 4: Agent selects its own tool chain

**Do**
The agent decided, on its own, to use Veo 3.1 lite clips via the OpenRouter
API. (OP: "because I asked for a cinematic trailer, it decided to use Veo
3.1 lite clips of my game using OpenRouter API.") It did NOT use the
text-to-speech model the prompt requested.

**Check**
- Total cost was about $3, inside the $10 budget (OP: "this wasn't free,
  but this video cost about 3$ to make, so basically free").
- OP on the workflow: "Yeah I just let it do its thing with all possible
  tools without providing instructions on specifics."
- Commenter AlgaeNo3373: "using an actual video gen AI with claude as
  director is a clever workflow!"

**Why**
Director-agent pattern: Claude directs, a video-generation model renders.
Letting the agent pick the model worked (Veo 3.1 lite delivered), but the
unused TTS shows the agent silently drops prompt requirements it does not
need.

### Phase 5: Generate clips and assemble the trailer

**Do**
1. Agent generated Veo 3.1 lite clips, monitoring the OpenRouter page in
   its browser while jobs ran.
2. Edited the clips into a ~45-second cinematic trailer: quick, snappy
   storytelling, different angles and lighting, per the prompt.
3. Unprompted, the agent changed the game's soundtrack to be spookier and
   more on theme. (OP: "it didnt actually use the text-to-speach model,
   but it did change the game's soundtrack to be more spooky and on theme
   haha. I did not request that at all, but im happy it did that.")

**Check**
- Trailer reads as professional cinematic; details and assets match the
  game (commenter: "Looks very good!").
- The horror framing is consistent throughout (trailer, music), even
  though the game is cozy.

**Why**
An autonomous agent fills gaps on its own initiative (here, the music).
Unprompted choices can be good, but they need a review pass because they
are outside the prompt's contract.

### Phase 6: Review the result and tighten the next prompt

**Do**
1. OP's verdict: "It's fair to say I won't use this trailer anywhere, but
   it did give me a good chuckle."
2. Lesson logged by OP: "my future prompts should be more specific, and
   less open to interpretation I guess haha."

**Check**
- Horror read of a cozy game = interpretation miss caused by openness,
  not by a tool failure.

**Why**
Open prompts buy creativity at the cost of genre accuracy. Specificity
(genre, tone, reference trailers) is the lever that fixes the next run.

### The human method, distilled
1. **Read-only access plus a written no-changes rule** is the safe way to
   let an agent study a game project.
2. **Director-agent pattern:** Claude as director, a video-gen model (here
   Veo 3.1 lite via OpenRouter) as renderer.
3. **Budget and autonomy in one prompt** ($10 max, "work autonomously
   until done") produced a ~$3, ~45-second trailer with no human in the loop.
4. **The agent silently drops unneeded requirements** (TTS was requested,
   never used); check what it skipped, not just what it did.
5. **Unprompted initiative needs review** (the spookier soundtrack); good
   here, but outside the contract.
6. **Details survive openness; genre does not.** The agent nailed assets
   and the boss shot from reading the project, but read cozy as horror.
   Fix it with a more specific prompt next time.

**Depth status:** FULL (for post+comments reconstruction; the tool chain,
budget, and agent decisions were all mined from OP's comments, which is
where the HOW lived)

---

## 17. "Material Point Method in Blender, 890k Particles, Faking Fracture With Voronoi Cells" (Algebraic-UG)

Source: https://www.reddit.com/r/Simulated/comments/1w8fd67 | r/Simulated post 1w8fd67 (score 67) | native clip (demo, not tutorial)

Tools used: Blender, "Squishy Volumes" add-on (free). Method: Material Point Method (MPM) soft-body simulation at 890,000 particles. Fracture is faked with Voronoi cells; actual fracture is an upcoming feature of the add-on.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Bridge the DCCs: Houdini motion operators drive Blender/Cycles rendering.
### Phase 1: Install the free add-on

**Do**
Install "Squishy Volumes" in Blender. (Author Algebraic-UG: 'You can
easily find it as "Squishy Volumes" (it\'s free)'.)

**Check**
- Add-on present in Blender's add-on list, enabled.

**Why**
The whole workflow rides on one free add-on, so the barrier to repeating
it is installation, not licensing.

### Phase 2: Set up the MPM soft-body simulation

**Do**
Build a soft-body simulation using the Material Point Method at 890k
particles, per the post title.

**Check**
- Particle count and method are stated in the title; no setup parameters
  were given in post or comments.

**Why**
MPM is the add-on's simulation core; the 890k particle count is the
scale the demo runs at.

### Phase 3: Fake fracture with Voronoi cells

**Do**
Shatter the object into pre-defined Voronoi cells so it breaks into
chunks, instead of simulating true fracture. (Title: "Faking Fracture
With Voronoi Cells". Author: "Yes, it's relatively simple, and actual
fracture is an upcoming feature in Squishy Volumes!")

**Check**
- Current fracture is a visual fake (pre-fractured cells), not a fracture
  simulation; real fracture is on the roadmap, not in the add-on yet.

**Why**
Pre-fractured cells deliver a convincing break-up now, while true fracture
remains an unsolved-hard problem (see Check in Phase 4).

### Phase 4: Judge against the physical-fracture standard

**Do**
Compare the result against what real fracture demands.

**Check**
- Commenter GiantPandammonia (score 5, top comment): the add-on author
  "works in scientific computing. Physics models not for graphics.
  Accurate fracture that matches experiments and gives a consistent result
  independent of mesh resolution is a tricky problem. Especially with
  shock impact loading and size effects when you are smashing stuff to
  fine powder."

**Why**
Mesh-resolution-independent fracture that matches experiments is the hard
bar; the Voronoi fake is honest about not clearing it yet.

### The human method, distilled
1. **Fake what is too hard to simulate**, and say so: Voronoi cells stand
   in for fracture until the real feature ships.
2. **The author's background shapes the tool**: scientific computing,
   "physics models not for graphics", which is why physical accuracy
   (mesh-resolution independence, experimental match) is the stated goal.
3. **Know the hard cases**: shock impact loading and size effects when
   smashing things to fine powder are where fracture models break.
4. **Free add-on, public roadmap**: "Squishy Volumes" is free now, with
   actual fracture announced as upcoming.

**Depth status:** DEPTH-LIMITED (empty selftext; only 5 short comments; no sim setup parameters, no Voronoi workflow steps, and no render details stated)

---

## 18. "Houdini X Mops-Blender/cycles" (gio_bero)

Source: https://www.reddit.com/r/houdini/comments/1wp1cad | r/houdini post 1wp1cad (score 66) | native clip (demo, not tutorial)

Tools used: Houdini with MOPS (Motion Operators for Houdini) for motion graphics, Blender/Cycles for rendering, "Light Wrangler" Blender add-on for lighting (premade gobo textures).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Smooth movement is reconciliation: client prediction with server correction, tested at every reachable crossing.
### Phase 1: Build motion graphics in Houdini with MOPS

**Do**
Author the motion-graphics work in Houdini using MOPS (Motion Operators
for Houdini), per the post title "Houdini X Mops-Blender/cycles".

**Check**
- MOPS named as the motion tool in the title; no operator names or
  parameter values were given.

**Why**
Houdini plus MOPS is the motion-design stage; rendering happens elsewhere.

### Phase 2: Move the work to Blender and render in Cycles

**Do**
Transfer the Houdini/MOPS result into Blender and render with Cycles.
(The transfer mechanism, file format, and any material conversion were
not stated [inference: some export/import step is required, but the
source does not say which].)

**Check**
- Final frames are Cycles renders of MOPS-driven motion graphics.

**Why**
Split the pipeline by strength: Houdini for motion, Cycles for the final
look.

### Phase 3: Light with the Light Wrangler add-on

**Do**
1. Switch from standard Blender lighting to the "light wrangler" add-on.
2. Use its premade gobo textures for the lighting rigs (this answers
   commenter i_am_toadstorm's question, "Is this a stock gobo you're
   using for lighting or is it geometry-driven?": stock/premade gobo
   textures from the add-on).
3. Aim lights by transforming and rotating them toward the object directly,
   with no manually added constraints.

**Check**
- Author gio_bero: 'For the lighting i switched from standard blender
  lightning to the "light wrangler" add-on. You could do it in vanila
  blender light setup, but i prefer this add-on, since it comes with pre
  made gobo textures. Also transforming and rotation light\'s towards the
  object is way easier, with no need to add any constraints manually.'

**Why**
The add-on buys two things: premade gobo textures (no need to build or
model patterned light blockers) and faster light aiming without manual
constraint setup. Vanilla Blender could do the same work; the add-on is
a speed preference, not a capability unlock.

### The human method, distilled
1. **Split the pipeline by strength**: Houdini/MOPS for motion design,
   Blender/Cycles for rendering.
2. **Stock gobos are fine when they read well**: premade gobo textures
   from Light Wrangler answered the "stock or geometry-driven?" question
   with stock.
3. **Prefer the add-on for speed, not capability**: vanilla Blender
   lighting could do the job; Light Wrangler wins on premade textures
   and constraint-free light aiming.
4. **Aim lights directly at the object**: transform/rotate toward the
   target beats rigging manual constraints for lookdev speed.

**Depth status:** DEPTH-LIMITED (selftext is only an Instagram follow link; one substantive author comment covers lighting only; MOPS setup, the Houdini-to-Blender transfer, and render settings are not stated)

---

*Author Instagram (from post selftext): https://www.instagram.com/polygonal.heaven*

---

# Game-dev workflows: reconstructions

Reconstruction format follows the cinematic-cavern benchmark: source line,
tools used, phased sections with Do / Check / Why, exact parameters where the
source states them, a distilled-principles list, and a depth status.
Nothing below invents transcript lines, parameters, or tool names. Anything
inferred beyond the sources is tagged [inference].

---

## 19. "How I made the multiplayer movement smooth in my game" (Ase-Dev ("Don't Lose Your Head"))

Source: https://v.redd.it/yvsd4zqwjarh1 | r/unity post 1wo9pos (score 29) |
native clip (demo, not tutorial)

Tools used: Unity; Rigidbody (Interpolation set to Interpolate); Network
Rigidbody component; Network Transform (interpolation mode, interpolation
slider); networking backend Facepunch.Steamworks (confirmed in comments:
"Steamworks Facepunch"). [inference]: the "network rigidbody component" and
"network transform" wording most closely matches NGO-style or Fish-Networking
style components, but the source never names the netcode library, so no
specific package is claimed.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Detail procedurally: ribbon cables generated with parametric controls instead of modeled by hand.
### Phase 1: Rigidbody-level interpolation

**Do**
1. Select the player prefab and find its Rigidbody component.
2. Set the Rigidbody's interpolation option to **Interpolate**.

**Check**
- The player position now updates on every rendered frame, not only on the
  FixedUpdate cycle.

**Why**
Jitter in networked movement comes from rendered frames falling between
physics ticks. Rigidbody interpolation smooths the visual transform between
fixed updates.

### Phase 2: Add the network components

**Do**
1. Add the **network rigidbody component** to the player, alongside the
   network transform component.
2. Tick **all** of the network rigidbody component's checkboxes.

**Check**
- Confirm the component is present on the player prefab and every checkbox
  is ticked.

**Why**
The network rigidbody carries the physics state (position/rotation) across
the P2P connection; the source treats "tick all checkboxes" as the setup
step and gives no per-checkbox detail.

### Phase 3: Tune the network transform interpolation

**Do**
1. Set the network transform's **interpolation mode to Interpolate**.
2. Adjust the **interpolation slider** to **0.35**.

**Check**
- Watch a remote player's movement in play: it should be jitter-free.
- If it looks floaty or laggy, the slider is too high; if it jitters, it is
  too low.

**Why**
The slider is the core trade-off of the whole setup, stated explicitly by
the author: **the higher its value, the smoother but also more delayed the
movement**. 0.35 was chosen because the game is a coop rage game, so the
delay cannot be big. The value is genre-tuned: a slow game could push it
higher for extra smoothness; a reaction-heavy game keeps it low.

### The human method, distilled

1. **Smoothness is bought with delay.** Every interpolation setting trades
   visual smoothness against input-to-display latency; pick the number from
   the genre, not from a default.
2. **Interpolate at two layers.** Rigidbody interpolation covers the gap
   between FixedUpdate ticks; network transform interpolation covers the gap
   between network snapshots.
3. **A small stack can be jitter-free.** The whole demo runs on a P2P
   Facepunch.Steamworks backend; smoothness came from three settings, not a
   dedicated server.

**Depth status:** FULL (short source, fully captured: all three steps, the
exact slider value 0.35, the smoothness-vs-delay trade-off, and the backend
confirmation are stated in the post and comments)

---

## 20. "Procedural Ribbon cables" (deepak365days)

Source: https://v.redd.it/v7m78fgu9eqh1 | r/proceduralgeneration post 1wkatjx
(score 177) | native clip (showcase, no tutorial)

Tools used: Blender 3D (confirmed by the author in comments: "Blender 3D").
[inference]: the generator's node/graph internals are never stated; the
workflow below reconstructs only what the clip and comments confirm.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Generate materials, don't paint them: a parametric leather-patch generator with exposed controls.
### Phase 1: Build the procedural cable system [inference: reconstruction]

**Do**
1. Build the cable generator in Blender as a procedural system, so cable
   paths, lengths, and twists can be regenerated rather than hand-modeled.
2. Expose end points for post-generation adjustment: a commenter asked
   whether ends can be manually adjusted after generating, and the author
   answered "Yes" (the exact adjustment workflow is not shown).

**Check**
- Regenerate: does a fresh seed produce a new valid cable layout without
  broken ends?
- Can the ends be moved after generation without breaking the procedural
  system?

**Why**
Procedural generation earns its keep when the output stays editable. The
author's yes to end-adjustment is the main confirmed workflow property.

### Phase 2: Randomized color assignment [inference: minimal reconstruction]

**Do**
1. Leave color randomization on its default: the cables are mostly red
   because the author "didn't adjusted color ramp"; the colors are random.
2. If a specific palette is needed, the author confirms the system is
   procedural and "user can change colors as per need".

**Check**
- Watch a regeneration: are colors random across cables? If a deliberate
   palette is wanted, adjust the color ramp.

**Why**
The red look is incidental (unadjusted defaults), not a design choice. In a
procedural system, unrandomized defaults read as intentional; either seed
the ramp or accept the default.

### The human method, distilled

1. **Keep generator outputs adjustable.** A procedural system that locks its
   results is just a fancy static mesh; confirmed end-adjustment is what
   makes this one a tool.
2. **Random defaults are not design decisions.** If the color ramp is
   unadjusted, say so; viewers will read intention into randomness.
3. **Expose the levers users ask about.** The thread's questions were ends,
   colors, and further modulation ("weirder and weirder sounds"); the author
   answered all three as doable.

**Depth status:** DEPTH-LIMITED (author confirms "Blender 3D", procedural
system, random unadjusted colors, and adjustable ends, but no node setup,
parameters, or geometry method are stated anywhere; phases above are mostly
[Inference] scaffold around those four facts)

---

## 21. "Leather Patch Generator" (Javadrajabzade)

Source: https://v.redd.it/9vqa8ywo21rh1 | r/Substance3D post 1wn37iv
(score 176) | native clip (showcase, portfolio cross-post; 1 comment)

Tools used: Substance 3D (implied by the r/Substance3D subreddit; the
post title says "Generator"). Portfolio:
https://www.artstation.com/a/56020938. The single comment is a reaction
("This is great!!"), not a technical question.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Drive fluid by target: a target-driven GPU fluid sim running in real time.
### Phase 1: Author a procedural leather material [inference: reconstruction]

**Do**
1. Build the leather as a procedural material generator (Substance graph
   style): exposed parameters for variation rather than a fixed texture.
2. Generate leather patches from the system: the deliverable is the
   generator plus its outputs, cross-posted to ArtStation as a portfolio
   piece.

**Check**
- Regenerate with different seeds: does the leather read as leather
   (grain, cracks, pores) in each variant?
- [inference]: no parameter names, node names, or values are given in any
   source, so no exact numbers can be reconstructed.

**Why**
A generator post is a portfolio move: the tool is the artifact. With no
tutorial content, the workflow cannot go deeper than this.

### The human method, distilled

1. **A generator is the portfolio piece.** When the post is the tool itself,
   the outputs prove the parameter space.
2. **Showcase posts carry no workflow signal by themselves.** Without a
   breakdown, questions, or author explanation, reconstruction stops at the
   tool category.

**Depth status:** DEPTH-LIMITED (one clip, one reaction comment, one
ArtStation link; no parameters, nodes, or method stated; nothing further can
be honestly reconstructed)

---

## 22. "Arrival Logograms, on a target-driven fluid sim. Real time on the GPU" (PiXeL161616 (TideGlass))

Source: https://v.redd.it/41d4qi2la9nh1 | r/Simulated post 1w60bt0
(score 631) | native clip (demo; rich author selftext + 18 comments)

Tools used: Swift and Metal; TideGlass (the author's small Mac app,
tideglass.app); the logograms are the real glyph plates from the film
Arrival (fifty plates; "Offer weapon" and "there is no linear time" named).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: Simulate the impact: SPH fracture and contact modeling for armor simulation.
### Phase 1: Simulate the fog as a real-time GPU fluid

**Do**
1. Build the fog layer as a fluid simulation running **in real time on the
   GPU** (Metal compute, macOS).
2. The simulation is the carrier medium: everything visual (fog, ink)
   rides on the fluid's velocity field.

**Check**
- It runs in real time on the GPU while the machine is otherwise in use;
   the app's design goal is worlds like this running on a second monitor
   while you work.

**Why**
Real-time GPU execution is the product constraint: TideGlass is an ambient
companion app, not an offline render, so the sim must hold frame rate as
wallpaper.

### Phase 2: Emit ink along the glyph stroke with a travelling pen

**Do**
1. Drive a **travelling pen** along the logogram's stroke; the pen emits
   ink as it goes.
2. Let the fluid carry the emitted ink; the pen is the emitter, the fluid
   is the transport.

**Check**
- The ink should trace the stroke path and then be advected by the fog's
   motion rather than sitting on a static canvas.

**Why**
Separating emission (the pen) from transport (the fluid) is what makes the
logogram feel like a phenomenon inside weather instead of a drawing.

### Phase 3: Pull density toward the target glyph without snapping

**Do**
1. Add a **target-driving force** that pulls the ink density toward the
   finished glyph shape, **without ever snapping it there** (the author
   cites Fattal and Lischinski's 2004 work for the approach).
2. Let the force act continuously: the glyph emerges and holds its shape
   against the fluid's motion but never becomes a rigid overlay.

**Check**
- The finished glyph reads clearly but still breathes with the fluid; no
   hard cut between "forming" and "formed".

**Why**
"Without ever snapping" is the whole aesthetic decision: a snapped glyph
is a decal; a continuously pulled one is an event happening in fog.

### Phase 4: Keep settled grains alive with perpetual motion

**Do**
1. Give the grains a **small random walk that continues even after they
   have settled**.
2. Add a **slow drift over the whole word** on top of the per-grain
   jitter.

**Check**
- A finished sign must never sit there dead: a commenter read the small
   jitter as "the alien trying hard to get the point across", which the
   author confirmed was intentional.

**Why**
Stillness kills the illusion of a living medium. The perpetual micro-motion
is a deliberate design choice, validated by an outside viewer's read before
the author even named it.

### Phase 5: React to the environment (music)

**Do**
1. Make the sim **react to whatever music is playing while you watch**.

**Check**
- Play music and watch: the fluid's response should be visible in the
   motion of fog and ink.

**Why**
Ambient software earns its second-monitor place by being alive to the room,
not just looping.

### Phase 6: Sequence the plates one at a time

**Do**
1. Use the **real glyph plates from the film: fifty of them**.
2. Write **one at a time**, letting each logogram form, hold, and give
   way to the next.

**Check**
- Each plate should be legible as its own event before the next begins.

**Why**
One-at-a-time sequencing gives the viewer time to read ("what did it
say?" was the thread's top question) and mirrors the film's own pacing.

### The human method, distilled

1. **Separate emission, transport, and targeting.** Pen emits, fluid
   carries, target force shapes: three independent systems composed into
   one phenomenon.
2. **Pull toward the target; never snap.** Continuous attraction reads as
   alive; snapping reads as UI.
3. **Settled does not mean still.** A small perpetual random walk plus a
   slow whole-word drift keeps a finished image breathing.
4. **Design for the second monitor.** Real-time GPU, ambient motion, and
   reactivity to the room (music) are product constraints, not decorations.
5. **Borrow real references.** Fifty actual film plates beat invented
   glyphs; "Offer weapon" and "there is no linear time" carry their own
   weight.

**Depth status:** FULL (author selftext gives the full method: travelling
pen, fluid-carried ink, target-driving force per Fattal and Lischinski
2004, perpetual random walk plus slow drift, music reactivity, Swift and
Metal, real film plates; comments add the 20% conservation donation intent
and the Mac-only status)

---

## 23. "I'm making an armor simulation mode for my game" (silenttoaster7 (Galaxy Engine))

Source: https://v.redd.it/ugv32oe4vrrh1 | r/Simulated post 1wqejcs
(score 243) | native clip (devlog-style demo; 16 comments)

Tools used: Galaxy Engine (open source,
https://github.com/NarcisCalin/Galaxy-Engine); in development for over a
year. Author caveat: "This simulation is not really that accurate compared
to actual professional software. It is meant to look cool." [inference]:
the thread names Smoothed Particle Hydrodynamics (SPH) only via commenter
u/CFDMoFo describing what popular YouTube ballistics sims use; the author
does not name his own solver.

### Phase 1: Reuse the engine's existing physics as the base

**Do**
1. Start from the engine's existing physics ("The engine actually already
   had these physics"); do not write a new solver for the mode.
2. Build a **specific armor simulation mode** on top: mode-specific setup,
   not a fork of the engine.

**Check**
- The mode shares the engine's physics core; changes to the core propagate
   to the mode.

**Why**
A mode reuses tested physics instead of duplicating it; the new work is
scenario tooling, not a new engine.

### Phase 2: Add armor-mode authoring tools

**Do**
1. Add mode-specific construction tools: the author names a **box tool**
   and a **circle tool** for building armor layouts (part of the upcoming
   major update, alongside UI changes and guides).
2. [inference]: the clip shows layered/spaced armor being penetrated by a
   projectile; exact material or thickness parameters are not stated.

**Check**
- Build a spaced-armor layout with the box/circle tools and run the
   penetration: does the layout survive construction and simulate?

**Why**
Authoring tools are what turn a physics demo into a mode: users need to
build scenarios, not just watch one.

### Phase 3: Run it in real time and tune constraints by eye

**Do**
1. Run the simulation **in real time at roughly 28fps** (author-confirmed);
   this is the headline engineering fact of the post.
2. Tune realism through the **settings of the constraints** ("I could try
   messing with the settings of the constraints"): e.g. a commenter noted
   the last armor plate should be "wayyy more solid" because real APFSDS
   penetrators "barely leave a hole 3~5 times their width in the armor"
   instead of blasting it apart on contact.
3. Accept arbitrary values: the author states plainly he has "no degrees
   in math or physics" and builds with "arbitrary values", aiming to make
   the physics as realistic as he can within that.

**Check**
- Watch the penetration: spalling and plate break-up should look
   plausible; if the armor shatters unrealistically, tighten the
   constraint settings.
- The author notes the new armor features are "not yet finished and
   uploaded": current public builds do "similar-ish simulations in 2d".

**Why**
Real-time at ~28fps is the trade that makes this accessible: professional
tools (Ansys Autodyn, an explicit FEA solver, per u/CFDMoFo) are accurate
but require serious knowledge, hardware, and time. The author's stated
contract is "meant to look cool to have some quick fun", and constraint
tuning by eye is the honest method for that contract.

### The human method, distilled

1. **Mode, not engine.** New scenarios reuse the existing physics core;
   the new work is authoring tools (box, circle) and mode setup.
2. **Real-time is the feature.** ~28fps on consumer hardware is what makes
   an open-source toy competitive with renders that take "60 HPF (hours
   per frame)".
3. **Tune by eye, label honestly.** Arbitrary constraint values are fine
   when the stated goal is "look cool"; the failure mode is claiming
   accuracy you do not have (the author explicitly disclaims it).
4. **Know the professional reference.** u/CFDMoFo's note (Ansys Autodyn,
   explicit FEA, SPH to simplify fracture and contact modeling) is the
   accuracy bar the toy is measured against; citing it keeps the scope
   honest.

**Depth status:** FULL (source is a devlog demo, not a tutorial; everything
stated is captured: >1 year of development, open source, engine reuse,
box/circle tools, real-time ~28fps, constraint-settings tuning, arbitrary
values, the accuracy disclaimer, and the professional-software reference
from the thread. SPH is attributed only to the commenter's description of
popular YouTube sims, not to the author's own solver.)

---

## 24. "Looking for advice on topology / rendering. Any tips?" (Rew1ndy)

Source: https://v.redd.it/pqk9jg7mp0sh1 | r/blender post 1wre6mr (score 26) |
native clip (work-in-progress render turntable, not a tutorial)

**What it is:** A beginner weapon-modeling Q&A. The author (second weapon
for their project; a Glock, described as "artistic interpretation rather
than an exact replica") posts mesh stats (10,826 vertices, 21,344 edges,
10,538 faces, 20,979 triangles), notes 3 hours of physics baking and 11
hours rendering at 3840x3840, and asks for topology/rendering advice. The
thread is critique: the trigger-guard topology is "funky as all hell", the
model is broken into sections/parts (grip + lower receiver, upper
receiver, barrel from a modified cylinder, silencer, holographic sight
parts, trigger/screws), and the rendering feedback is about composition
and lighting.

**Why no workflow signal:** The post contains no tooling, no technique
being demonstrated, and no reproducible method. It is a request for
feedback, and the comments are reactions and critique, not a pipeline.
There is no generator, solver, simulation, or authoring workflow to
reconstruct; the only "tools" named are Blender and a render, with no
settings given.

**Depth status:** NO-TOOLING
