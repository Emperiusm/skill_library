# Video tooling scout: have-vs-need, 2026-11-09

Run: daily video-tooling-scout, depth mode `pre-approved` (max 2 media downloads).
Window: Reddit last 2 days (2026-11-07 to 2026-11-09), YouTube channels last 14 days.
Scanned: 33 Reddit video posts across 23 subreddits, 13 YouTube videos across 11 channels.
Deeply analyzed: 8 (5 Reddit, 3 YouTube). Dedup: 2 Reddit posts and 2 YouTube videos were already audited (2026-11-08 report / existing skills) and were skipped.

## Gap alerts

Four P1/P2 gap matches this run. None of them closes a gap outright; all four are new evidence or pattern matches for gaps that already have FIX PREPARED artifacts awaiting landing (see `references/p1-gaps.md`).

1. **P2 MCP-driven DCC loop (aegis): STRONGEST MATCH.** RUSuper week 15: "Opus 5.5 (Claude Code) does basically all of the building: all code, all the performance fixes, the performance panel, and the city's layout and buildings in Blender through MCP." An agent driving Blender through MCP to lay out a city and build its buildings is the P2 loop running in production on a real game, not a demo. Warp Studio adds a second data point (full MCP support for 2D rigging), but it is a vendor pitch and 2D only.
2. **P1 AI-vendor generation/acceptance spec (aegis intake/): Gauntlet-Loop.** RUSuper's blind A/B critic loop: critic agents compare the game to the ChatGPT mockup blind, a piece is done when it wins twice (31 of 33 pieces won), plus the guard rule added after a critic wrongly removed the lighthouse beam ("loops can't remove things the game already has just because a picture doesn't have them"). That is an acceptance-record pattern with a stop rule, exactly the shape the acceptance-spec gap needs.
3. **P1 per-asset performance budgets (aegis): cosmo_tree_gen.** The addon shows a triangle counter and a draw-call counter per tree in the editor toolbar, and its LOD system spends "the rest of the tris budget" on leaves after simplifying the trunk. A per-asset budget display plus a budget rule, shipped in a real Godot addon. Pattern evidence, not a foundry-wide system.
4. **P1 2d3d import-validation gate / production-conversion stage: Blender NodeMode.** Frame-verified Mesh Repair node (Merge Duplicates, Remove Degenerates, Stitch Borders, Orient Faces, Transfer Attributes) plus an Isotropic Triangle Remesh node and a Bake node is a mesh repair plus remesh plus bake chain, the same shape as the production-conversion stage 2d3d needs at the M2 bake-off, and a checklist input for the import-validation gate.

## Videos scanned

Reddit (Arctic Shift API, 2 days, min score 20): 33 video posts. Top by relevance: cosmo_tree_gen (100.0), Claude Opus week 15 (81.8), ComfyUI Readable Node (50.7), Project Prales (42.0), Primordium creature meshes/IK (41.4), Godot 2D waterfall shader (34.5), MiniMax H3 Remix Tool (34.3, already audited 2026-11-08), IV Studio 1.0 (21.7, already audited 2026-11-08), Warp Studio (20.7). Two subreddits (blender, vfx) returned HTTP 526 from Arctic Shift and contributed no posts this run.

YouTube (11 configured channels, 14-day window, min duration 240 s): 13 videos. The scan failed outright on the first attempt (all 11 channels SSL CERTIFICATE_VERIFY_FAILED, the sandbox egress proxy CA missing from the video-summarizer venv certifi bundle). Fix applied this run: appended the current system-store CA (`/usr/local/share/ca-certificates/hatch-egress-ca.crt`) to that venv's certifi bundle and refreshed the saved copy at `~/workspace/custom-skills/local-video-summarizer/.venv/hatch-egress-ca.pem`. Re-run: 13 videos, 0 warnings. Top by score: Ryan King Art taco Parts 5 and 3 (11, 10), diamonds in Blender 5.3 (9), Entagma GSplats single image (8, already a skill), Olivio image-to-3D low VRAM (6, already a skill), Blender Secrets armour (6), Ryan King sculpting anatomy (6), Default Cube NodeMode (5), Josh Blender Bros Floaters (4) and 3D Textures (4).

## Audits

### 1. "I got tired of modeling trees, so I made a free procedural tree generator addon" (CosmonautFrog)

Source: https://www.reddit.com/r/godot/comments/1xqxbys/i_got_tired_of_modeling_trees_so_i_made_a_free/ | v.redd.it/tjsiu9rgjd0i1 | r/godot post 1xqxbys (score 1418, 107 comments) | Repo: https://github.com/FrogCosmonaut/cosmo_tree_gen (109 stars, 11 forks, MIT, created 2026-10-27, Godot 4.6+, developed in 4.6.2.stable)

Tools used: Godot 4.6+, cosmo_tree_gen addon (MIT). "100% Human made. No AI was or ever will be used in this project." Inspired by Dan Shiffman and EZTree.

This audit reconstructs the exact workflow shown in the video and documented in the repo README, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: generate the whole tree in the editor from a seed, tune it live, and export it as a finished game asset with LODs and collisions.

### Phase 1: Install and generate the first tree

**Do**
1. Copy the `addons/cosmo_tree_gen/` folder into the project and enable the addon. Requires Godot 4.6+.
2. Add a `CosmoTreeGen` node.
3. Pick a preset from the toolbar menu (4 premade: Ash, Bush, Low Poly Bush, Low Poly Tree; 7 more in the `demo` folder), or tweak `trunk_params` and `foliage_params` and add `CosmoBranchLevel`s to `branch_levels`.
4. Set bark and foliage materials, or use the ones in `addons/cosmo_tree_gen/materials`. Note: icosphere foliage needs a material with UV1 Triplanar.

**Check**
- The tree regenerates live in the editor as parameters change; randomize the seed from the toolbar to check variety.
- The toolbar shows draw calls and a triangle counter per tree; watch both while tuning.

**Why**
"Having the full creation pipeline inside Godot is neat." The author built it because "making enough variety for a whole forest was taking forever" by hand, and says it is "saving me probably months of work now."

### Phase 2: Grow the branching (recursive levels, not L-systems)

**Do**
1. Branching is recursive by level: each level grows branches out of every previous level's branches, with spread using the golden angle.
2. Sub-level length and thickness are fractions of the previous level's.
3. Control branch level length and leaf card size by curve. Multiple trunks per node, roots and broken branches appear by chance.

**Check**
- Compare the silhouette against the preset; if the tree reads as noise, reduce levels or tighten the fractions.

**Why**
The author tried L-systems first and rejected them: "I tried L-system at first but ended up doing recursive branching level... found this way easier than L-system, which was hard to predict and I didn't like the string-rewriting-thing about it." Predictability beats grammar elegance when the goal is a forest of distinct but controllable trees. (Author comment, quoted.)

### Phase 3: Foliage

**Do**
1. Choose icosphere foliage (configurable subdivisions level) or card leaves (configurable amount, double sided, with canopy normals and inner AO).
2. The leaves shader has wind sway and limited mipmaps, so alpha scissor does not make distant leaves disappear.
3. Toggle flat shading for a low-poly/PSX style.

**Check**
- Check distant trees: leaves must not pop out of existence as mipmaps shrink.
- For a weeping willow, the author notes there is no leaf gravity option yet; the workaround is a very long leaf texture with the leaf angle tuned to point down. A leaf-gravity foliage parameter is planned ("I'll try to add a leaf gravity to the foliage params").

**Why**
Foliage is where a procedural tree fails first at distance; the mipmaps limit exists specifically so the canopy survives the LOD chain.

### Phase 4: Collision

**Do**
1. Set `collision_type` and `collision_level`, and optionally `collision_max_height` to cut collision at a given height.
2. Three shape types: one convex shape per branch, one convex shape per branch segment, or a single trimesh.
3. Collision covers branches up to a configurable level (0 = trunk only). Foliage collision is a hull covering all foliage, or spheres on each leaf/branch end.
4. Preview with the `preview_collision` toggle.

**Check**
- Turn the preview on in the editor and confirm the shapes cover the trunk and the branches the player can reach, and nothing the player cannot.

**Why**
Collision generated from the same seed as the tree means the physics shape can never drift from the visible mesh.

### Phase 5: LOD and export

**Do**
1. Toggle `generate_lod`. LOD0, LOD1 and LOD2 MeshInstance3Ds generate with customizable ratios and distances. Tris budgets for LOD and distances are configured in the project settings.
2. The trunk is simplified and the rest of the tris budget goes to the leaves. Leaf cards are not simplified; fewer and bigger cards are kept instead.
3. Export as glb/glTF from the toolbar, with LODs and collisions, optionally linking the materials in the `.import` file.
4. Batch generation: one click generates dozens of trees with random seeds and reusable presets; presets save as `CosmoTreePreset` resources; there is an exposed API for script generation.

**Check**
- Read the per-tree tris and draw-call counters before export; the LOD ratios are the budget, not a suggestion.
- Roadmap (author's priority order): billboard impostor PNG generation for the last LOD is item 1 (the author is working on automatic octahedral impostor generation now, and points to https://github.com/hdrsniped/octahedral-impostor-lod-godot as a reference implementation); tree age slider is item 3; stumps, fallen trunks and felled trees from the same seed is item 8 (requested in the comments for tree-chopping mechanics); one texture atlas per bark plus foliage to reduce 1 draw call is item 10.

**Why**
Export carries the LODs and the collisions with the mesh, so the asset arrives in the game the way it looked in the editor. The budget rule (trunk simplified, leaves keep the tris) protects the silhouette, which is what the eye reads.

### Failure modes

- Mobile renderer shadows: a commenter testing on Android found the middle of the tree dark, "it had nothing to do with the addon. My shadowmap is too small because I use mobile." The author's suggested workaround is commenting out the AO / AO_LIGHT_AFFECT lines on the leaves shader. (Comment thread, quoted in substance.)
- Willow shape without leaf gravity: use a long leaf texture and tune the leaf angle down; the author calls the in-video willow "not the best willow tree ever" for exactly this reason.

### The human method, distilled

1. **Build the pipeline inside the engine.** The whole creation pipeline lives in Godot; nothing is modeled by hand and imported.
2. **Prefer a predictable generator over an elegant one.** Recursive levels with golden-angle spread beat L-systems because the author can predict what comes out.
3. **Budget visibly.** Tris and draw calls are counters in the toolbar, checked during tuning, not after export.
4. **Same seed, same tree, same collision.** Seeds plus presets make the forest reproducible and the physics shape consistent.
5. **Ship the roadmap in priority order.** Impostor LOD3 and the age slider are next because commenters asked for them; the author asks the thread what to prioritize.

**Depth status:** FULL (full post text + 25 comments with exact author method + repo README with exact parameters, presets, collision types, LOD rules, install and usage steps; the native Reddit clip has no transcript and adds nothing the post and README do not already state).

### 2. "15 weeks of making game with Claude Opus in Godot" (RUSuper, Nightshoal)

Source: https://www.reddit.com/r/aigamedev/comments/1xrknnf/15_weeks_of_making_game_with_claude_opus_in_godot/ | v.redd.it/o4o6vd5u8j0i1 | r/aigamedev post 1xrknnf (score 91, 27 comments) | Demo: https://profactor.itch.io/nightshoal

Tools used: Claude Opus 5.5 (Claude Code), Jev (the author's effort-level picker), TripoAI, Blender with Opus via MCP, GPT Astra (cost line only), OpenAI image API, ElevenLabs, Godot.

This audit reconstructs the exact workflow in the author's week-15 update, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: let Opus build, let blind critics judge against mockups, let a profiler decide what is slow, and keep the human as the stop rule.

### Phase 1: Finish the look with Gauntlet-Loop

**Do**
1. Build the bridge city look, then run Gauntlet-Loop: 10 rounds of it. Every "round critic" agent compares the game to the ChatGPT mockup blind, without knowing which one is which. (Author's artifact from Claude describing the loop: https://claude.ai/artifact/3BnUXUZQd9xLws6RxiyAtW, not retrieved.)
2. Stop rule: "if a piece wins against the mockup twice, it's done and no more polishing." 31 out of 33 pieces won.
3. Add the guard rule after the critic removed the lighthouse beam because the mockup did not have it: loops can't remove things the game already has just because a picture doesn't have them. ("Like... it's a lighthouse.")
4. Mockups: OpenAI image API made 24 of them, 6 views at 4 times of day, and those were what the critics compared against.

**Check**
- Blind comparison is the check: the critic must not know which image is the game.
- The win-twice rule is the stop condition; without it the author notes the loop "started taking forever (it always does with a loop so basically you have to be the one to stop it at one point)."

**Why**
A loop without a stop rule polishes forever. Two blind wins is a decision, not a feeling. The guard rule exists because a mockup is a reference, not the spec; the game already had a lighthouse beam and the loop deleted it for matching the picture.

### Phase 2: Day, night, and city dressing

**Do**
1. The sun moves across the sky during the day, rises on the right, sets on the left; shadows turn and get longer in the evening; the sun's reflection on the water moves with it. At night the moon takes over. This works in the whole game, not only in the city.
2. Add traffic on the bridge, a tram, window lights that turn on at night, and a lighthouse with a rotating beam.
3. Remove anachronisms on sight: "Cars had red tail lights at first and I was like... it's 1920, they shouldn't have those, so I removed them."

**Check**
- Play through the day cycle in the city and on the home islands; both must change, since the system is game-wide.
- The city is not reachable yet (it is there for zone 2; its docking site is next week's work), so the check is visual, not playable.

**Why**
Look first, gameplay second this week: "most of what got built recently was new zones, the bridge city and the black market. Gameplay there comes with their docking scenes (shops, people, quests), and that's what I'm working on next."

### Phase 3: Profile with an in-game panel, then let Opus fix what it finds

**Do**
1. Build a performance panel inside the game that shows what costs how much and writes logs; players start the game with `--perf-log` and send the file.
2. Let Opus go through the whole game with the panel and write a report of what costs the most.
3. Fix what the report names:
   - First dock at a harbour after install froze for almost 2 seconds. Now 0.2.
   - First rain, first lanterns and first cast off also froze the game on first launch. Fixed too.
   - HUD redrew itself every single frame even when nothing changed. Now the game is 15-19% faster on 1080p.
   - Map used 4 GB of graphics memory "because of a bug that drew it at double size." The author chose the proper fix over the quick fix: the map is now baked into tiles and only loads what you see. It uses around 0.3 GB now, opens instantly, and the game starts twice as fast (26 s to 13 s on the author's Mac).
   - Far harbours now load in the background while the player sails towards them instead of all being loaded all the time; overall the game uses around a quarter less graphics memory.
4. Small stuff: an achievement now rings a small ship bell (sound made with ElevenLabs), and the map in the Cabinet zooms in to fill the whole screen.

**Check**
- The panel plus the log file is the check: a player with a slow machine sends `--perf-log` output instead of a vague report.
- Numbers before and after are the acceptance: 2 s to 0.2 s, 4 GB to 0.3 GB, 26 s to 13 s, 15-19% faster at 1080p.

**Why**
"Do it properly" beats a quick fix when the bug is structural (the map drew at double size; tiling it fixed the memory, the open time, and the startup time at once). Jev picks the effort level for every task; "for performance it mostly picked 'extra', and for the performance scan it asked me if it can go max and I said yes."

### Phase 4: Build assets with the Tripo 4-view turnaround

**Do**
1. Make one image with all 4 sides of the model (front, back, left and right).
2. Opus splits it into 4 images; upload those to Tripo. "Tripo works much better when it gets all 4 sides."
3. After generation, Opus fixes the model in Blender through MCP if needed.
4. Sometimes keep Tripo's textures; sometimes Opus makes its own materials so the model fits the game's style better.
5. This week the whole black market is Tripo models: the steamer, the gatehouse, warehouses, the storehouse, the derrick, piers, launches and the cutter, plus the three black market fishing rods. City models came from Tripo too, "though not all of them, a lot were done in Blender with Opus 5.5 with MCP."

**Check**
- Compare the generated model against the 4-side input; if it is off, Opus fixes it in Blender through MCP rather than regenerating.
- Style check: Tripo textures stay only if they fit the game's style; otherwise Opus remakes the materials.

**Why**
"Tripo saves me a huge amount of time on modelling." The 4-side input is the quality lever: one image with all four sides beats a single view. The MCP fix loop is cheaper than another generation round.

### Phase 5: Prompt simply, test by playing, direct loosely

**Do**
1. Prompting: "It's a simple 'talking' there is no magic technique I use for prompting, just saying what I want, test playing and tweaking and fixing." (Author comment, quoted.)
2. Put rules in claude.md when a pattern must hold: on sprites, "you have to establish some rules that it has to follow in claude.md if you already didn't." (Author comment.)
3. For the trailer, direct vaguely this time: "I just said vaguely what I want." Opus came up with options for length, pacing and how it opens, and Jev picked between them. Opus also edited the week-15 video together from game footage.
4. Sound: "Gave ElevenLabs API key to Claude and asked Claude to do all the sound problems by itself." (Author comment.) The jump sound at 0:53 is the Quake jump sound, slightly cut at the end; ElevenLabs made the ship bell.

**Check**
- Test playing is the check: say what you want, play it, tweak, fix. No separate review step is described.
- The author accepts the presentation weakness openly: "my gameplay presentation just suck ass... I just can't seem to get it right from week to week," and agrees with commenters that each post should stand alone as a presentation.

**Why**
The human's job in this loop is taste and stopping, not typing: describe, play, judge, stop. Jev deciding effort level per task is the same idea applied to compute: not every task deserves maximum effort.

### Phase 6: Account the week in dollars

**Do**
1. Total the week: Claude Max $200 x 4 = $800; Astra $100 x 1 = $100; ElevenLabs $11; TripoAI $20 x 2 = $40; OpenAI API credits $80; other things forgotten about, around $100. "Around 1100-1150$."
2. Note the limit hit: "I hit 94% of my weekly limit and had to pause the last performance fixes until the reset, so I got another Max (now called Ultra lol) plan."

**Check**
- The cost list is the budget check; the 94% limit hit is what forced the plan upgrade, not a feature decision.

**Why**
A weekly cost total is part of the devlog: the loop's price is visible next to its output, so the reader can judge whether 15 weeks at roughly $1,100 a week is the deal they want.

### The human method, distilled

1. **Blind critics, fixed stop rule.** Compare against the mockup without knowing which is which; two wins means done.
2. **The mockup is a reference, not the spec.** A loop must never delete what the game already has to match a picture.
3. **Profile first, fix what the profiler names.** The in-game panel plus `--perf-log` turns "it feels slow" into named costs with before/after numbers.
4. **Do it properly when the bug is structural.** Tiling the map fixed memory, open time, and startup at once; a quick fix would have fixed one.
5. **Four sides in, one model out.** Tripo works much better with all four sides; Opus fixes the rest in Blender through MCP.
6. **Say what you want, play it, tweak it.** No magic prompting technique; test playing is the review.
7. **Publish the cost.** The weekly total sits next to the weekly output.

**Depth status:** FULL (complete author post text with exact numbers, costs, and quoted method + 25 comments; the video clip is a gameplay trailer with no captions and no narration, and a media download would add gameplay frames only, not pipeline detail).

### 3. "ComfyUI Readable Node: an agent skill for turning messy workflows into readable ones" (nomadoor)

Source: https://www.reddit.com/r/comfyui/comments/1xqupum/comfyui_readable_node_an_agent_skill_for_turning/ | v.redd.it/op3un4p50d0i1 | r/comfyui post 1xqupum (score 33, 11 comments) | Skill repo: https://github.com/nomadoor/comfyui-readable-node | Author's site: https://comfyui.nomadoor.net/

Tools used: ComfyUI, Readable Node agent skill, Claude Opus 5.5 (best; Sonnet noticeably worse).

This audit reconstructs the exact workflow the author describes, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: take the workflow completely apart, figure out what it does, and rebuild it from scratch to be readable, then show the replay.

### Phase 1: Learn the six readability rules

**Do**
1. Don't hide nodes: expand subgraphs, open collapsed nodes, don't stack nodes on top of each other.
2. Don't hide wires: no wireless links (Set/Get, Anything Everywhere, hidden wires), and no Bento layouts that pack nodes so tightly the wires disappear.
3. Left to right: the flow goes left to right, in processing order.
4. One workflow, one task: instead of an all-in-one workflow with switches and bypasses, split it into small workflows that each do one thing.
5. Keep custom nodes to a minimum: if it can be built with core nodes, build it with core nodes.
6. Color appropriately: colors show which function a node belongs to.

**Check**
- A readable workflow is one where "you can tell at a glance what it does, it runs reliably, and it's easy to rework. It's not about looking pretty. It's about being easy to understand and easy to change." (Author, quoted.)

**Why**
The author builds and publishes his own basic workflows for one reason: readability, even though official templates exist. The six rules are his definition, stated up front.

### Phase 2: Run the agent skill on a messy workflow

**Do**
1. Give the agent a workflow JSON and ask it to make the workflow readable with Readable Node.
2. The agent takes the workflow completely apart, figures out what it does, and rebuilds it from scratch: turning Set/Get back into wires, swapping custom nodes for core ones, removing redundant nodes, splitting bundled tasks, writing notes that explain why each part is set up the way it is. (Author comment, quoted in substance.)
3. You get the rebuilt workflow and a report page. In the report, you can replay how the AI rebuilt the workflow and read what each part does.

**Check**
- Read the report page and replay the rebuild; the replay is the verification that the agent understood the workflow rather than just rearranging it.
- "Since it aims for a more robust workflow, the output may not always match the original exactly." A changed output is expected, not a failure, when the rebuild removes a redundant node or splits a bundled task.

**Why**
"Why a skill and not a script? As I said above, readability isn't just a layout problem." Layout alone cannot turn Set/Get links back into wires or decide a custom node should be a core node; those are judgment calls, which is why the author built an agent skill instead of a layout script. The skill also builds an internal layout tool and the AI operates it: "The AI isn't specifying coordinates one by one." (Author comment.)

### Phase 3: Mind the costs and the model floor

**Do**
1. Budget time: "It's slow. A workflow of about 25 nodes takes around 10 minutes, and big ones can take 20-40."
2. Use a strong model: "Claude Opus 5.5 works best; with others, the layout may still have a few issues." Even Sonnet "made the results noticeably worse." (Author comment.)
3. For local use, give the skill to an agent harness like OpenCode or Pi; Ollama is not the route, and "getting it to run well locally would be tough." (Author comment.)

**Check**
- If the layout still has issues, the first suspect is the model, not the workflow.

**Why**
The skill was built by grinding: the author started from his own site's workflows, "then collected workflows from around the web and fixed them, over and over, hundreds of times." The model floor is a measured result of that grinding, not a preference.

### Phase 4: Use it where handoff happens, not every day

**Do**
1. Use it when trying to understand a workflow someone gave you, or when about to hand one off to someone else. "It's less of an everyday tool and more something to use when you're trying to understand a workflow someone gave you, or when you're about to hand one off to someone else." (Author comment.)

**Check**
- Commenter additions to the rules, acknowledged by the author: group nodes that belong to the same step in the workflow (the author notes the skill does use groups, but "doesn't lean on them much" and would like to work on that more), and put nodes that get adjusted regularly on the left so the user does not scroll through the whole workflow to adjust a prompt, LoRAs, and resolution. The left-to-right rule and the adjustable-nodes-left wish contradict each other; the author accepts both as open tension.
- Counterpoint from a Nuke background commenter: DAG auto-layout is standard in VFX (Nuke has had auto-arrange for over a decade, and it is instant), and compositors must write readable scripts "by law" because scripts get handed off around the facility. The author's reply, in substance: AI can make the judgment calls where layout is under-constrained or contradictory (for example, which wire crossing to avoid in a non-planar graph), which classic algorithmic auto-layout cannot.

**Why**
The author's closing argument for readability itself: "Ask the AI for what's better said in words, and do by hand what's better done by hand. If you want to do both in one place, I think ComfyUI's node graph is a pretty good fit, as long as you can read the workflow." And the paint-tool analogy: to remove a mole next to someone's eye, painting over it is faster than typing "remove the mole," which is why paint tools have not gone away.

### The human method, distilled

1. **Readability is understanding plus change, not looks.** At a glance, runs reliably, easy to rework.
2. **Rebuild, don't rearrange.** The agent takes the workflow apart and rebuilds it; the report page with its replay proves the rebuild understood the work.
3. **Name the weak spots up front.** Slow (10 minutes for 25 nodes), needs Opus 5.5, output may not match the original exactly.
4. **Use it at handoff boundaries.** Understanding someone else's workflow, or handing one off, is where readability pays.
5. **Words for words, hands for hands.** Ask the AI for what is better said in words; do by hand what is better done by hand.

**Depth status:** FULL (complete author post text with exact rules, timings, and model floor + 10 comments with the author's own clarifications and the Nuke counterpoint; the video is a demo clip of the skill running).

### 4. "I built a runtime generator for 16 km2 of Central European wilderness in Unreal Engine 5" (haithegreat, Project Prales)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xr7pia/i_built_a_runtime_generator_for_16_km%C2%B2_of_central/ | v.redd.it/e68n9vx33g0i1 | r/proceduralgeneration post 1xr7pia (score 98, 13 comments) | Full trailer: https://www.youtube.com/watch?v=dy4c_mUn9m4

Tools used: Unreal Engine 5 (C++), Quixel Megaplants (free on Fab) for tree models, Claude Code (assisted development).

This audit reconstructs the exact workflow the author describes, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: let the seed build the world, let ecology place the forest, and verify with a hash.

### Phase 1: Carve terrain river-first

**Do**
1. Generate terrain from large-scale elevation patterns.
2. Carve valleys where the drainage wants to go: river-first heightfield, plus hills, ridges, cliffs and tors. "Cliffs are created through steep elevation transitions and terrain shaping."
3. Store terrain data in a grid-based node system rather than simulating every square meter.

**Check**
- The "world builds itself" sequence in the video draws the real generated data (contours, rivers, forest, trails) over the rendered terrain of seed 100001; the overlay must match the terrain underneath.
- Every number gives a different 4 x 4 km world; the same seed must give the same world, "tested by world hashes."

**Why**
Rivers decide the valleys, so the terrain follows the water instead of the water being pasted onto finished terrain. A node grid keeps the data manageable at 16 km2.

### Phase 2: Run hydrology over the whole world

**Do**
1. Compute drainage and flow accumulation across the whole world.
2. Rivers always run downhill; smaller streams merge into larger rivers. Add lakes, springs, and marshes where the flow says water collects.

**Check**
- A river that runs uphill is a bug in the drainage pass, not in the terrain; check flow direction before adding vegetation, since the forest placement reads the same moisture data.

**Why**
Hydrology is computed on the whole world at once, so a stream in one valley and a lake in the next agree with each other; local water features would not.

### Phase 3: Derive climate, biomes, and vegetation from the ecology

**Do**
1. Run a climate pass over sunlight, temperature, and moisture; biomes follow elevation, moisture, and exposure.
2. Place vegetation from that ecology, with no random scatter layers: "beech on the middle slopes, spruce higher up, pine on dry rocky ground, alder along streams." (Author comment, quoted.)
3. Open land needs a reason: marsh on wet flats, dry grass on sunny slopes.
4. Scatter trees with coordinate-hashed randomness, plus canopy gaps, edge shrubs, and deadwood from windthrow. "Same seed, same forest."
5. Add rocks, deadwood, ground cover, two isolated forest huts, and dirt tracks. Day and night plus dynamic weather.

**Check**
- The honest split, stated by the author: "the plant models aren't generated. The trees are Quixel Megaplants (free on Fab). What's procedural is where things grow." Do not claim generated trees; the generation is placement, not models.
- Check a slope by eye: the wrong tree on the wrong slope means the climate pass is wrong, not the scatter.

**Why**
Ecology-driven placement is the difference between a forest and a scatter layer: every tree has a reason (slope, moisture, exposure) a player could infer by looking at the land. Coordinate-hashed randomness keeps it deterministic without storing a placement table.

### Phase 4: Measure performance, render the trailer offline

**Do**
1. Measure on real hardware: "around 60 FPS on Epic, 90 FPS on High and 120 FPS on Medium at 1080p, using a Ryzen 5 7600 and RX 6900 XT." (Author comment.)
2. Render the trailer offline from the game, frame by frame at 4K60. The author is explicit that the trailer "was rendered offline at 4K, though, so it's not representative of actual gameplay. Still got plenty of optimization work ahead of me!"

**Check**
- The FPS numbers are the gameplay claim; the trailer is not. Do not quote 4K60 as gameplay performance.

**Why**
Offline rendering buys a beautiful trailer without pretending the game runs that way; the FPS numbers are reported separately and honestly.

### Phase 5: Build it with an AI assistant, in the right order

**Do**
1. "Claude Code helped me quite a bit throughout development. It was especially useful for implementing systems and working through bugs and glitches." (Author comment.)
2. The author's recommended study order for someone starting in this direction: "starting with procedural terrain generation and hydraulic erosion. There's a lot to learn by experimenting with these!"

**Check**
- Seasons (with snowy winters) are next; there is no public build yet, so nothing here is verified by a player.

**Why**
Terrain first, erosion second: those two systems are the foundation the hydrology, climate, and placement passes all read from.

### The human method, distilled

1. **Rivers first.** The drainage decides the valleys; everything else reads the water.
2. **Ecology, not scatter.** Every plant has a reason (slope, moisture, exposure); open land needs a reason too.
3. **Same seed, same world, proven by hash.** Determinism is tested, not asserted.
4. **Say what is procedural and what is not.** The trees are Quixel assets; the placement is the procedural part.
5. **Report the real FPS and label the trailer.** 60/90/120 at 1080p is the claim; 4K60 is an offline render.

**Depth status:** PARTIAL (full author post text + 13 comments with exact placement rules, species-by-slope mapping, and measured FPS; no node graph, code, or parameters beyond those quoted; plant models are disclosed as Quixel assets, not generated; the full trailer on YouTube was not downloaded, the run's 2-download allowance was spent on the NodeMode and Floaters videos, and a download would add trailer frames only, no narration is stated to exist).

### 5. "Procedural creature meshes and IK walking for a Spore-inspired evolution game I'm making" (Ouvolk, Primordium)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xqpk3r/procedural_creature_meshes_and_ik_walking_for_a/ | v.redd.it/myywk10xdb0i1 | r/proceduralgeneration post 1xqpk3r (score 72, 21 comments) | Demo: https://akinjigames.itch.io/primordium | Kickstarter pre-launch: https://www.kickstarter.com/projects/primordium/primordium-evolve-your-own-creature-from-a-single-cell

Tools used: Godot 4 (runtime code generation; engine version as stated in the sibling post 1xqph5m, audited 2026-11-08). No DCC tools named; no pre-made skeletal meshes.

This audit EXPANDS the 2026-11-08 audit of the sibling post 1xqph5m ("Working on a Spore-inspired evolution and tribe game in Godot 4 with procedural creatures") and its skill `characters/godot-runtime-procedural-creatures`. Same author, same game, second post with new detail: part-placement gameplay effects, procedural parts inventory, and IK specifics. The 11-08 audit's phases (generate the design, build the rig and skin at runtime, animate with IK and lean, drive behaviour with a daily schedule) still stand; this audit adds what the new post and its comments disclose.

### What is new in this post

**Do (new detail)**
1. Procedural rig and skin: the skeleton and a single skin mesh are built from the creature's spine and limb design, with foot planting via IK, vertical body bobbing on footfall, and the body leaning into turns.
2. Procedural parts: curved Bezier horns, tapered ears, bi-lobed tail clubs, wings you can glide with, and shader eyes with blinking eyelids.
3. Where a part sits changes what it does (author comment, quoted in substance): "Fringes (the cilia) give you acceleration and turning, and they turn better when they're on the sides. Tails are your main thrust from the back: the long lash is fast but turns badly, the quick flick is twitchy. Jets boost sprinting, spikes hurt anything you ram, venom leaves a cloud, shock is an active zap, armour makes you tanky but slow, and eyes let you see further."
4. Living ecosystem and tribe stage: herds follow a daily schedule (sleeping in nests at night, stretching at dawn, resting at midday); later the player founds a tribe whose members gather, hunt, defend and play instruments.
5. Design deltas vs Spore, stated by the author: built from scratch with a modern engine, fully procedural bodies, mod support and Steam Workshop planned from day one; the player can stay in any stage as long as they want; the species carries over (what the creature ate, tamed and hunted shapes the tribe instead of everything resetting); stages have more depth, "where you put a part actually matters," and the creature stage adds hunger, stamina, predators tracking scent, nests and eggs.

**Check**
- The editor backdrop drew criticism in the comments ("Instead of a lily pad, make it look like you're in a focused circle... to mimic you looking through a microscope"); the author agrees the lily pad is "a bit silly for a simple organism" and that the bright green is distracting, and will think of something better. The backdrop is a settings pick among a few, not a load-bearing choice.
- Commenters asked what leg ranges are possible ("Can you make a millipede?") and what resources the author used to learn procedural generation; the author did not answer either in the retrieved comments.

**Why**
The design thesis, in the author's words: "Spore came out 18 years ago and we never got a real sequel, so honestly even a modern version of the same game would've been enough for me. But obviously I'm trying to push it further." Placement-as-gameplay is the push: a part's position is a build decision with combat and movement consequences, not decoration.

### The human method, distilled (additions)

1. **Placement is gameplay.** Cilia on the sides turn; a tail at the back pushes. A part's position is a stat.
2. **Carry the species over.** What the creature ate, tamed, and hunted shapes the tribe; nothing resets between stages.
3. **Let the player stay.** No stage forces the player onward; the arc is the player's choice.

**Depth status:** PARTIAL (full author post text + 21 comments; comments are mostly an AI-use debate, not workflow detail; no code, no numeric parameters, no performance figures; author offered to answer questions about mesh generation, IK walking, and AI, and answered the part-gameplay questions in detail).

### 6. "Introducing... Blender NodeMode!" (Default Cube)

Source: https://www.youtube.com/watch?v=jEynICHP1gM | Default Cube | Uploaded 2026-11-05 | 766 s (12:46) | 60,356 views | Site: https://www.blendernodemode.com (per the video description and the end card frame)

Tools used: Blender, NodeMode (Houdini-style node graph inside Blender).

This audit reconstructs the workflow from 12 frames extracted from a downloaded copy of the video (download 1 of 2 in this run's pre-approved allowance; no approval gate fired), plus the video description. No captions exist in a retrievable form: the subtitle fetch hit YouTube HTTP 429 and was not retried. No transcript lines are quoted anywhere in this audit, because none were retrieved. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: do everything Blender does through a node graph, with named nodes and explicit parameters, the way Houdini works.

### Phase 1: Remesh with the Isotropic Triangle node

**Do**
1. Feed the mesh into an "Isotropic Triangle R..." node (frame shows "Isotropic Triangle R", presumably Remesh).
2. Set Target E... 0.1 m, Iterations 7. Check Preserve Boundary, Preserve Sharp, Transfer Attributes. Set Sharp Angle 30 deg.

**Check**
- The frame shows the node wired between a geometry source and a Bake node; the parameter values are visible on the node itself. Read the actual parameters instead of relying on node names (the Cinematic Cavern rule: node labels drift, values are the truth).

**Why**
Isotropic remeshing gives even triangles before baking, so the bake downstream does not inherit stretched source topology.

### Phase 2: Bake it still

**Do**
1. Feed the remeshed geometry into a "Bake" node.
2. Set Animation: Still.

**Check**
- The Bake node sits between the remesh node and the output wire; a Still bake means the result is a static mesh, not an animated cache.

**Why**
Baking freezes the procedural result into a mesh the rest of the graph (and the exporter) can treat as finished geometry.

### Phase 3: Simulate cloth with explicit solver parameters

**Do**
1. Use a "Cloth Solver" node with Geometry in, Simulation out.
2. Set Substeps 4, Iterations 4, Delta Time 0.042.
3. Set Force to (0.000, 0.000, -9.810): gravity down Z at 9.81.
4. Under Collision, set Thickness 0.010, Friction 0.500, check Self Collision. Tearing is available as a collapsed section.
5. Feed the solver output into a "Simulation" node (Skip, Geometry) and route the result through a Portal Receive node where the graph needs it downstream.

**Check**
- The cloth frame shows the solver wired into the simulation node with a Portal node carrying geometry onward; the substeps and delta time are the stability budget (4 substeps at 0.042 s).
- A separate frame shows "Simulation Input" and "Simulation Output" nodes bracketing falling cubes above a ground plane: the simulation zone is explicit in the graph, not hidden in a modifier stack.

**Why**
Solver parameters are on the node, in the open: substeps, iterations, gravity, thickness, and friction are all visible and editable in one place, which is the whole point of doing simulation as nodes instead of as a modifier.

### Phase 4: Move data without wires using Portals

**Do**
1. Create a "Portal" node set to Transmit with a name (the frame shows a Portal named "Portal").
2. Anywhere else in the graph, create a Portal node set to Receive with the same name; it receives the value, vector, or geometry.
3. The frame shows a Vector node (X 0.000, Y 0.000, Z 0.000) wired into a Transmit Portal, and a second Transmit Portal below it, with a Receive Portal on the right exposing Value, Vector, and Value sockets.

**Check**
- The receive side lists the same sockets the transmit side offers; a portal that receives nothing has no data to show.

**Why**
Portals are the node-graph answer to long wires: data moves by name across the graph, the same role Set/Get nodes play in ComfyUI (see audit 3, where hidden wires are exactly what the Readable Node skill removes). The difference is that NodeMode portals are named and visible as nodes.

### Phase 5: Deform a surface with noise

**Do**
1. Take a "Bunny [CGM]" source (Geometry, UVMap out) into a "Surface Deformation" node (Geometry, Mesh, Pick, Pin Position, Extra).
2. Drive the deformation with a "Random Value" node (Boolean, Probability 0.010, ID, Seed 0) and an "Add" vector node fed by a "Position" node.
3. Feed a "Noise Texture" node into the Add: 3D, FBM, Normalize checked, Vector in, Scale 5.000, Detail 2.000, Roughness 0.500, Lacunarity 2.000, Distortion 0.000.

**Check**
- The frame shows the full chain wired: Bunny to Surface Deformation, Random Value and Noise Texture feeding the Add feeding the deformation's Pin Position. Probability 0.010 means roughly 1 in 100 points is picked; Seed 0 means the pick is reproducible.

**Why**
Surface deformation driven by noise plus a sparse random pick is how you add organic variation to a mesh without sculpting it: the noise decides where, the probability decides how much.

### Phase 6: Repair the mesh before it leaves

**Do**
1. Run the mesh through a "Mesh Repair" node: check Merge Duplicates, Remove Degenerates, Stitch Borders, Orient Faces, Transfer Attributes (all five checked in the frame).
2. A side panel on the same frame shows emit toggles: Emit Sharp, Emit UV, Emit Color, Emit Material (partially visible, prefixed "...mit").

**Check**
- Repair is a node in the chain, so it runs every time the graph re-evaluates; a repaired mesh cannot regress when an upstream parameter changes.

**Why**
Mesh repair as a graph node turns cleanup from a manual step into a rule, the same principle as the Cinematic Cavern scripted-repairs phase: fix the geometry first, as a repeatable operation.

### What the frames also show

- A cracked/broken skull render (frame 2): the destruction/fracture look NodeMode is used to produce.
- A sponsor segment (frames 6-8): the presenter unboxing and reclining in a LiberNovo chair, matching the affiliate link in the video description. No tooling content.
- End card (frame 11): "BlenderNodeMode.com".

### The human method, distilled

1. **Nodes for everything.** Remesh, bake, cloth, deformation, and repair are all nodes with visible parameters, not modifier-stack entries.
2. **Read the parameter, not the label.** Target 0.1 m, 7 iterations, 30 deg sharp angle, 4 substeps, 0.042 delta time: the values are the workflow.
3. **Name the data to move it.** Portals carry values by name across the graph instead of long wires.
4. **Repair is a step, not an afterthought.** The Mesh Repair node sits in the chain and runs on every evaluation.

**Depth status:** PARTIAL (12 frames from a downloaded copy with verified node names and parameters; no captions, the subtitle fetch failed with YouTube HTTP 429 and was not retried, and local transcription is unavailable in the sandbox by design; no pricing stated in the video or description).

### 7. "Floaters - The BIGGEST 3D Modeling Cheat Code" (Josh - Blender Bros)

Source: https://www.youtube.com/watch?v=2qdCIDZbF8s | Josh - Blender Bros | Uploaded 2026-11-02 | 449 s (7:29) | 87,239 views | Description links: Mech Head Design in Plasticity (https://www.blenderbros.com/mech-head-design-in-plasticity/), MaterialWorks Texturing Plugin

Tools used: Blender; Plasticity (for the mech head design course the video ties into, per the description).

This audit reconstructs the workflow from 12 frames extracted from a downloaded copy of the video (download 2 of 2 in this run's pre-approved allowance; no approval gate fired), plus the video description. No captions were retrievable and no transcript lines are quoted. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: fake the detail with separate meshes sitting on the surface instead of cutting it into the mesh.

### Phase 1: Model the base form clean

**Do**
1. Model the base form (here, a mech head) as a clean, simple shell with good topology. The frame shows a smooth dark head with a few large forms and a wireframe overlay showing even quads.
2. Do not cut vents, panels, or bolts into the base mesh.

**Check**
- The base reads as the finished silhouette with no surface detail yet; if the silhouette is wrong, no floater will fix it.

**Why**
The base mesh carries the shape; everything else is decoration. Cutting detail into it would destroy the clean topology and multiply the modeling time.

### Phase 2: Model floaters as separate pieces

**Do**
1. Model each detail as its own small mesh: cylinders, vents, rings, greebles. The frames show cylindrical floaters and ring segments as separate objects in the outliner (Scene Collection, Cylinder entries).
2. Keep floaters simple: a cylinder with a beveled edge reads as a vent housing; a ring segment reads as a panel line.

**Check**
- A floater in edit mode (frame 6) shows its base edge loop selected along the surface it will sit on; the loop must follow the base curvature.

**Why**
A floater is a cheat in the honest sense: it looks like modeled detail from every normal viewing angle, but it cost a cylinder and a bevel instead of a boolean and a topology repair.

### Phase 3: Place floaters on the surface, do not boolean them in

**Do**
1. Place each floater on the base surface so it intersects slightly; the intersection is hidden by the bevel and the viewing angle.
2. A frame shows a floater hovering above the surface, selected and outlined in orange, before placement: position first, then drop it onto the surface.
3. The right panel shows a Bevel modifier (Angle limit, Segments) on the floater: the bevel catches the light and sells the intersection.

**Check**
- Orbit the model: a floater that reads from the front but floats visibly from the side is placed wrong. The frame showing the finished head from a three-quarter view is the check; floaters sit flush and the seams read as panel lines.
- The finished wheel/hub frame shows hex bolts and ring segments placed as floaters around a central disc: the detail is dense, but every piece is a separate simple mesh.

**Why**
Booleans create topology debt (n-gons, shading breaks, cleanup). Floaters create no debt: each piece is independent, movable, and deletable. The technique trades a small amount of geometric honesty for a large amount of speed, and the trade is invisible in the render.

### Phase 4: Material the assembly as one

**Do**
1. Apply materials after placement; the frames show a material panel (metalness/roughness) and a material preview on the finished head and hub.
2. Keep the floater materials consistent with the base: same metalness and roughness range, so the pieces read as one object.

**Check**
- The material preview thumbnail must match the viewport: if a floater reads as a different material, it stops being detail and becomes a stuck-on piece.

**Why**
Materials unify the assembly. The eye forgives separate geometry when the surface response is consistent.

### The human method, distilled

1. **Silhouette first, detail second.** The base mesh carries the shape; floaters carry the detail.
2. **Never boolean what you can float.** A separate mesh costs a cylinder; a boolean costs topology repair.
3. **Bevel sells the seam.** The bevel modifier on each floater is what makes the intersection read as a designed edge.
4. **Materials unify.** Consistent metalness and roughness make separate pieces read as one object.

**Depth status:** PARTIAL (12 frames from a downloaded copy with verified technique and visible modifier settings; no captions; no spoken principles are quoted because none were retrieved; the Plasticity course link in the description is the mech-head source, not a step in the video).

### 8. "Creating 3D Textures is Basically Cheating Now..." (Josh - Blender Bros)

Source: https://www.youtube.com/watch?v=3eHXIzavmHs | Josh - Blender Bros | Uploaded 2026-11-07 | 911 s (15:11) | 19,421 views | Description links: MaterialWorks Texturing Plugin (https://www.blenderbros.com/materialworks/)

Tools named: MaterialWorks Texturing Plugin (Blender Bros). Nothing else is verifiable from the retrieved evidence.

The video could not be deepened in this run: the media download failed (YouTube asked for sign-in or cookies, "from-browser or --cookies for the authentication"), no captions were retrieved, and the run's 2-download allowance was already spent on the NodeMode and Floaters videos. The only evidence is the title and the description snippet naming the MaterialWorks plugin. No workflow, no parameters, no technique can be stated without inventing them.

**Depth status:** DEPTH-LIMITED (title plus description snippet only; download blocked by YouTube sign-in requirement, no captions; a media download on a machine with a signed-in YouTube session, or a captions fetch when YouTube is not rate-limiting, would be needed to reach PARTIAL). No skill: not executable from this evidence.

## Screened out (not audited)

- "I made a dynamic 2D waterfall using a custom shader and a texture array" (fespindola, r/godot, score 227, 8 comments): the selftext is a 373-character promo for the author's Godot VFX book (coupon ALL5OFF, https://jettelly.com/store/complete-godot-vfx-handbook) and the 8 comments are praise plus one question about time spent tuning speed vs noise, unanswered. No shader code, no parameters, no technique. **Depth status:** NO-TOOLING.
- "I've been building an AI powered Spine 2D alternative" (Crockiestar, r/aigamedev, 8 comments): Warp Studio / Warp Puppet vendor pitch. Full MCP support, AI draws characters with math as separated parts, swap parts keep animations, hair physics. Commenters are skeptical ("Looks completely fake btw", "Oh look another one..."), and the r/aigamedev mod team flagged it as commercial promotion. Paid tool, unverified claims, no workflow detail beyond the pitch. Screened out as an audit; the tool is watchlisted with a caveat. Does not fill the P1 3D rig/retarget gap (2D only).
- Ryan King Art taco Parts 3 and 5 (YouTube, scores 10 and 11): installments of a food-modeling tutorial series whose Part 1 is already a skill (`materials-shaders/blender-taco-shell-voronoi-tortilla`). Not audited this run: the 8-video cap went to higher pipeline-relevance candidates, and food modeling installments are lower value than NodeMode, Floaters, and MaterialWorks for the four repos.
- Entagma "Free Houdini: GSplats from a single image (MoGe-2 and SHARP)" (YouTube, score 8): the exact video is already the skill `capture/houdini-single-image-gsplat-sharp-moge2`. Skipped as a duplicate.
- Olivio Sarikas "FREE + LOCAL: Image to 3D for LOW Vram" (YouTube, score 6): the exact video is already the skill `capture/comfyui-ldoi-image-to-3d`. Skipped as a duplicate.
- "Minimax H3 Best Remix Tool" (r/comfyui, 1xqqhxh) and "IV Studio 1.0" (r/comfyui, 1xqfux1): both audited in full on 2026-11-08; re-scanned in the overlapping window, no new evidence.
- Other YouTube candidates not audited (cap/relevance): "How BAD is AI for Games?" (opinion piece), "Which Voice Typing app is Worth your money?" (not game tooling), "My Blender YouTube Channel Was Nearly Deleted..." (channel meta), "How I Learned to Sculpt Character Anatomy in Blender" (sculpting tutorial, no pipeline), "Creating Maximilian-inspired Armour in Blender" (Blender Secrets tutorial), "AI can do WHAT NOW?" (news roundup).

## Have-vs-need: Aegis (primary)

Repo evidence: `references/aegis-pipeline-inventory.md` (audit 2026-09-26). HAVE only with cited evidence.

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Procedural tree generation in-engine (live params, LOD, collision, glb export) | 1 cosmo_tree_gen | NEED | No vegetation/tree stage in trellis-pipe or foundry; inventory lists image-to-3D, weld, QA, LODs, ORM pack, UE packaging | Watchlist: the pattern (in-engine procgen plus built-in tri/draw-call counters plus one-click export) transfers to UE-side work, but the addon itself is Godot-only |
| Blind A/B acceptance loop vs mockups (Gauntlet-Loop, win-twice stop rule) | 2 Nightshoal | PARTIAL | Multi-view render QA (`review/`) and blind-review vote binding exist, but no blind A/B vs mockup acceptance loop with a stop rule | Backlog: fold the win-twice rule and the "can't remove what the game has" guard into the `aegis-intake/` acceptance-spec artifact (FIX PREPARED, awaiting landing); practice evidence for the P1 acceptance-spec gap |
| Tripo 4-view turnaround (1 image, 4 sides, Opus splits, Tripo generates) | 2 Nightshoal | PARTIAL | TRELLIS-2 image-to-3D is HAVE (`runtime/worker`, `gen_server`); Tripo is an alternative vendor, and the 4-side input is a technique, not a stage | Backlog: adopt the 4-view turnaround input in `intake/` as a vendor-input recipe; test against TRELLIS-2 on the same asset |
| Agent drives Blender via MCP (city layout and buildings) | 2 Nightshoal | PARTIAL | No MCP-driven DCC loop in the foundry (P2 gap); prior art is the `agentic-blender-asset-pipeline` skill | Backlog: spike a Blender MCP task behind the review stage using the city-layout example as the template; strongest P2 evidence to date |
| In-game perf panel plus --perf-log plus agent perf scan | 2 Nightshoal | PARTIAL | Automated QA gates (`runtime/qa`) and per-run evidence publishing exist; no in-game perf panel or player-submitted perf-log pattern | Watchlist: the panel-plus-log pattern is a cheap way to get real-machine perf data; per-asset perf budgets (P1) still need the budget numbers |
| ComfyUI workflow readability agent skill | 3 Readable Node | NEED | Watchlist row "ComfyUI custom nodes wrapping intake/ stages" shows intake uses ComfyUI; no readability or handoff hygiene stage | Watchlist: useful when an intake workflow is handed off; not a pipeline stage |
| River-first terrain plus whole-world hydrology plus climate biomes (deterministic, world-hash tested) | 4 Prales | NEED | No terrain generation in the foundry; UE packaging stage (`ue/`) exists but takes assets, it does not generate worlds | Watchlist: pattern candidate for Aetheria-side worldgen; UE5 C++ transfers, but Aegis has no worldgen stage to attach it to |
| Runtime procedural rig plus skin plus IK (code-generated, no skeletal meshes) | 5 Primordium | NEED | No rigging / skinning / animation-retarget stage in the foundry (P1 gap, FIX PREPARED) | Backlog, no fill: a runtime code rig is not a foundry stage; the part-placement gameplay (position changes function) is a design note for creature work |
| Houdini-style node graph in Blender (remesh, bake, cloth, repair, portals) | 6 NodeMode | NEED | No node-graph DCC stage; Blender MCP prior art exists as a skill, not a stage | Watchlist: Mesh Repair plus remesh plus bake chain is the production-conversion pattern; see gap alert 4 |
| Floaters (separate detail meshes, no booleans) | 7 Floaters | NEED | No hard-surface detail stage in the foundry; prop work goes through image-to-3D plus weld plus QA | Watchlist: prop-detail technique for foundry prop passes; cheap, no new dependency |
| MaterialWorks texturing plugin | 8 (named only) | NEED | No evidence beyond the name; Substance-side texturing is the existing route | Skip: named only, no workflow evidence |

## Have-vs-need: 2d3d

Repo evidence: `references/2d3d-pipeline-inventory.md` (audit 2026-09-26, roadmap).

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Procedural tree generation in-engine (Godot addon) | 1 cosmo_tree_gen | PARTIAL | Procedural texture/audio generators (`pipeline/proc/`) exist; no tree or vegetation generator; Godot 4.7.2 is the engine, so the addon is directly usable | Backlog: evaluate against the kit's tree needs; LOD plus collision plus glb export matches the asset installer plus manifest pattern |
| Blind A/B acceptance loop vs mockups | 2 Nightshoal | NEED | Reference fidelity is machine-measured (`docs/fidelity.md`, mean distance 0.333) and the golden-path bot plays the level per commit; no blind A/B acceptance | Backlog: the win-twice rule is a cheap acceptance gate for generated art; pairs with the art bible (P1, FIX PREPARED) |
| Tripo 4-view turnaround | 2 Nightshoal | PARTIAL | AI image client with fail-closed spend gate (`pipeline/image_client.py`) and reference reconstruction (Depth Anything 3 plus SAM 2) exist; Tripo is a vendor alternative | Watchlist: 4-view input recipe is adoptable in the reference pipeline |
| Agent drives Blender via MCP | 2 Nightshoal | PARTIAL | No MCP-driven DCC loop; `pipeline/` is Python plus GDScript, no agent-driven Blender stage | Watchlist: the MCP fix loop (Opus fixes Tripo models in Blender) is the pattern to copy for generated-mesh cleanup |
| Mesh Repair plus remesh plus bake node chain | 6 NodeMode | PARTIAL | QA gates (`qa/`) and the asset installer exist; no mesh repair stage; P1 import-validation gate (roadmap rec 9, FIX PREPARED) and P1 production-conversion stage (roadmap rec 20, FIX PREPARED) both name this shape | Backlog: the Mesh Repair checklist (merge duplicates, remove degenerates, stitch borders, orient faces, transfer attributes) is an input to the import-validation gate |
| Runtime procedural rig plus skin plus IK | 5 Primordium | PARTIAL | Generated hawk/boar art is missing and procedural rigs are stand-ins (beads 9le.25, p06.10, 9le.9); runtime rig generation is the pattern those stand-ins need | Backlog: part-placement gameplay effects are a design reference for the creature work |
| In-game perf panel plus --perf-log | 2 Nightshoal | PARTIAL | 286 gdUnit4 cases, 198 QA gates, 319 pipeline self-tests; no in-game perf panel | Watchlist: cheap real-machine perf data for the mobile renderer |
| Floaters | 7 Floaters | NEED | Projection painting onto fitted geometry exists; no floater-style hard-surface detail stage | Watchlist: prop-detail technique for kit props |
| River-first terrain plus hydrology | 4 Prales | NEED | 2d3d is a 2D-to-3D side-scroller with authored levels; runtime wilderness generation does not fit | Skip: not applicable to the kit |
| ComfyUI Readable Node | 3 Readable Node | NEED | 2d3d does not use ComfyUI | Skip: no attach point |

## Have-vs-need: Desktop City

Repo evidence: `references/desktop-city-pipeline-inventory.md` (repo tree 2026-09-27, PRD v1.5). Per PRD DEC-12, asset tooling lives in this repo and must not require the Aegis repository.

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Procedural tree generation in-engine (Godot addon) | 1 cosmo_tree_gen | PARTIAL | `tools/city_trees.py` plus `tools/procgen_*` probes exist; a Godot addon with LOD, collision, and export is a direct alternative, and a Godot addon does not violate DEC-12 | Backlog: compare against `city_trees.py` on variety, LOD, and draw calls; the built-in counters are the perf-budget pattern the PRD lacks |
| Terrain-adaptive placement from ecology | 4 Prales | PARTIAL | `tools/city_*` family (backfill, canopy, coast, layering, rail, seams, trees, walk) and layout QA gates exist; placement follows authored rules, not ecology | Watchlist: the ecology-driven placement pattern (reason per placement) is a design reference for city layout stages |
| Blind A/B acceptance loop vs mockups | 2 Nightshoal | NEED | Art-judge (`tools/art_judge.py`) and `compare_town.py` exist; no blind A/B acceptance with a stop rule | Backlog: win-twice rule as an acceptance gate for generated town views |
| Node-graph Blender workflows (remesh, bake, repair) | 6 NodeMode | NEED | Headless Blender sprite render (`tools/gen_iso_sprites.py`, `tools/render_models.gd`) is the Blender path; no node-graph workflow on that path | Watchlist: Mesh Repair as a pre-render cleanup node for the Blender sprite path |
| Floaters | 7 Floaters | PARTIAL | `tools/facade_parts.py`, `tools/street_kit.py`, `tools/building_families.py` do procedural authoring; floaters are a prop-detail technique for the same parts | Watchlist: cheap detail for street kit and facade parts |
| Tripo 4-view turnaround | 2 Nightshoal | NEED | TRELLIS/Aegis sprite route retired (`tools/_retired/`); Blender path is the only building-sprite route; Tripo is an alternative vendor | Watchlist: 4-view input recipe if image-to-3D is ever revisited for props |
| Shader-driven skyline fill (P1 gap) | none today | NEED | No equivalent; every building is authored or generated | No change: still the open P1 gap for this repo |
| In-game perf panel | 2 Nightshoal | NEED | QA gates plus `suite_floor.json` exist; no in-game panel | Skip: idle city-builder, not a 3D action game; panel pattern does not transfer |

## Have-vs-need: Solarempire

Repo evidence: `references/solarempire-pipeline-inventory.md` (repo tree 2026-09-27, `art/AGENTS.md`, ADR 0003).

| Tool/stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Mesh Repair plus remesh plus bake node chain | 6 NodeMode | PARTIAL | Blender stages (`tools/asset-pipeline/assetpipe/blender/`): audit, prepare, segment, retopo, rig, uv, bake, lods, export; the NodeMode chain maps onto retopo plus bake plus a repair step the pipeline does not name | Watchlist: Mesh Repair checklist as an explicit stage between prepare and retopo |
| Tripo 4-view turnaround | 2 Nightshoal | PARTIAL | Meshy-generated GLB plus concept PNG in, production GLBs out; Tripo is an alternative vendor to Meshy | Watchlist: 4-view input recipe for the concept-to-GLB step |
| Blind A/B acceptance loop vs mockups | 2 Nightshoal | NEED | Per-asset audit plus optimization reports with measured figures exist (for example Aurelia Ring Station: 3,104,038 tris source to 299,998-tri LOD0, silhouette IoU 0.998); no blind A/B acceptance | Backlog: win-twice rule as an acceptance gate on top of the existing audit reports |
| Runtime procedural rig plus skin plus IK | 5 Primordium | HAVE | Rigging stage present (`stages/rig.py`, `assetpipe/blender/rig.py`); unlike Aegis, this pipeline rigs | No action: HAVE with repo evidence; the runtime code-rig approach is a different method, not a gap |
| Floaters | 7 Floaters | PARTIAL | Retopo plus segment stages exist; spacecraft hard-surface detail (greebles, bolts, rings) is exactly the floater use case | Watchlist: floater pass before retopo for greeble detail on stations and ships |
| Agent drives Blender via MCP | 2 Nightshoal | NEED | No MCP-driven DCC loop; Blender stages are scripted, not agent-driven | Watchlist: the MCP fix loop as a future cleanup step |
| Procedural tree generation | 1 cosmo_tree_gen | NEED | Space game; no vegetation stage | Skip: not applicable |
| River-first terrain plus hydrology | 4 Prales | NEED | Space game; no terrain stage | Skip: not applicable |
| ComfyUI Readable Node | 3 Readable Node | NEED | No ComfyUI in the pipeline | Skip: no attach point |
| Godot import validation gate plus re-measured export budgets (P1 gap) | none today | NEED | No Godot project exists yet; export budgets are oracle budgets (ADR 0003) | No change: still the open P1 gap for this repo |

## Watchlist trending

Corrected snippet. The trend script matched on bare tokens ("Godot", "ComfyUI", "MCP") and annotated 64 rows, most of them false positives; those were reverted against the pre-run mirror. Only the genuine reappearances below were kept, plus 6 new rows appended. (Tool names in the script output that are not listed here were token-overlap false matches, not reappearances.)

- Blender NodeMode (Default Cube, blendernodemode.com) (first seen 2026-11-07, status WATCH; seen again 2026-11-09)
- Runtime procedural rig + skin generation in GDScript (Godot 4, Primordium by Ouvolk) (first seen 2026-11-08, status WATCH; seen again 2026-11-09)
- MCP servers driving Blender/Unreal (agentic DCC) (first seen 2026-09-27, status BACKLOGGED; seen again 2026-11-09) **TRENDING**
- Tripo Smart Mesh P2.0 (first seen 2026-09-28, status BACKLOGGED; seen again 2026-11-09 [2026-11-09 auto-match was token overlap on "Tripo"; RUSuper week-15 uses Tripo image-to-3D only, no Smart Mesh P2.0 rigging claimed; not new rig-gap evidence])
- GPT Astra (first seen 2026-09-28, status WATCH; seen again 2026-11-09 [2026-11-09 auto-match was token overlap on "Astra"; week-15 post lists Astra only as a $100 cost line, no GPT Astra mesh workflow described; not a genuine reappearance])
- ComfyUI-ldoi (first seen 2026-10-31, status WATCH; seen again 2026-11-09 [2026-11-09: same Olivio video 0eIjJinYgmk re-scanned in the overlapping window, already a skill; no new evidence])
- IV Studio (first seen 2026-11-03, status WATCH; seen again 2026-11-09 [2026-11-09: same post 1xqfux1 re-scanned in the overlapping window, already audited 2026-11-08; no new evidence])

New watchlist rows appended 2026-11-09: cosmo_tree_gen; Blender NodeMode (full row with frame-verified parameters); ComfyUI Readable Node; Project Prales; Gauntlet-Loop; Floaters; Warp Studio / Warp Puppet (caveated: vendor pitch, unverified, mod-flagged).

## Gap recommendations (highest leverage)

1. **Spike the Blender MCP loop behind Aegis review (P2 MCP-DCC gap).** RUSuper shows Opus building city layout and buildings in Blender through MCP on a shipping weekly cadence. Next step: a bounded spike, one Blender MCP task behind the review stage, using the city-layout example as the template. This is the first production (not demo) evidence for the P2 gap.
2. **Fold Gauntlet-Loop into the acceptance spec (P1 acceptance-spec gap).** The win-twice stop rule plus the "can't remove what the game has" guard is a concrete acceptance record. Next step: add both rules to the `aegis-intake/` acceptance-spec artifact (FIX PREPARED, awaiting landing) as the worked example.
3. **Evaluate cosmo_tree_gen for Desktop City and 2d3d (perf-budget pattern).** The addon's per-tree tri and draw-call counters plus its LOD budget rule (trunk simplified, leaves keep the tris) is the cheapest working example of the per-asset perf-budget pattern. Next step: run it against `city_trees.py` output and the 2d3d kit on variety, LOD, and draw calls.
4. **Use NodeMode's Mesh Repair checklist as a 2d3d import-gate input (P1 import-validation gap).** Merge Duplicates, Remove Degenerates, Stitch Borders, Orient Faces, Transfer Attributes is a five-line checklist that maps directly onto the import-validation gate's mesh checks. Next step: compare it against `install_asset.py` and the Solarempire retopo stage.
5. **Take Primordium's part-placement rules as a creature-design reference (P1 rig gap, no fill).** Position changes function (cilia sides turn, tail back thrusts, armor slows). Next step: a design note for Aegis creature work; the runtime code-rig itself does not fill the foundry rigging gap, and nothing today does.

## Explicit non-goals

- MaterialWorks texturing plugin: named in a video description only; no workflow, no parameters, no pricing. Skipped, not watchlisted beyond this mention.
- Ryan King Art taco Parts 3 and 5: same series as an existing skill; not audited this run (cap).
- Warp Studio / Warp Puppet: vendor pitch, mod-flagged commercial promotion, skeptical comments, unverified claims. Watchlisted with a caveat only; no audit, no skill.
- Godot 2D waterfall shader post: book promo, no technique. No audit, no skill.
- "How BAD is AI for Games?", voice-typing apps, channel-deletion video, sculpting anatomy, Maximilian armour, AI news roundup: screened out on relevance or cap.
- No new P1 gaps were opened this run. All four gap matches are evidence for existing gaps, not new gaps.

## Depth-escalation usage and run notes

- Mode: `pre-approved`, max 2 downloads. Attempted 2, succeeded 2, skipped 0 for gating: NodeMode (jEynICHP1gM, 36.9 MB, 766 s) and Floaters (2qdCIDZbF8s, 19.8 MB, 449 s). No approval gate fired on either download.
- A third download was attempted for "Creating 3D Textures" (3eHXIzavmHs) by the summarizer before the allowance accounting caught up; it failed on YouTube's side (sign-in/cookies required), not on an approval gate, and was not retried. The allowance is exhausted for this run regardless (2 successful downloads).
- Captions: none retrievable for any of the three YouTube videos. NodeMode subtitle fetch failed with YouTube HTTP 429 (Too Many Requests) and was not retried. Local transcription is unavailable in the sandbox by design (the Whisper venv python is missing: `/home/hatch/workspace/custom-skills/local-video-summarizer/.venv/bin/python` does not exist; the yt-dlp script in that venv also had a broken shebang for the same reason). The working venv is `~/workspace/skills/video-summarizer/.venv/`; the summarizer scripts were run with that venv's `bin` on PATH.
- YouTube scan recovery: the first scan failed on all 11 channels (SSL CERTIFICATE_VERIFY_FAILED, egress proxy CA missing from the video-summarizer venv certifi bundle). Fixed by appending the current system-store CA to that bundle and refreshing the saved copy; re-run found 13 videos with 0 warnings.
- Arctic Shift returned HTTP 526 for r/blender and r/vfx; those two subreddits contributed no posts this run.
- Trend script: passing generic terms ("Godot", "ComfyUI", "MCP") caused 64 token-overlap annotations; all but 7 were reverted against the pre-run mirror copy in the public repo, and the 7 kept are listed above with the false ones bracketed per the file's convention.
- Skill publishing: 6 new skills staged plus 1 expansion (see `~/workspace/video-tooling-scout-public/`); report published to `docs/scout-reports/have-vs-need-2026-11-09.md`; watchlist rows synced to the repo mirror; push via `bin/push_skill_library.py` with dry-run first (workflow-file hold-back applies if `.github/workflows/` appears).

## skill_library artifacts staged

New skills (one per FULL or PARTIAL audit):
- `automation/comfyui-readable-node` (audit 3, FULL)
- `automation/nightshoal-opus-weekly-loop` (audit 2, FULL)
- `procgen-worlds/cosmo-tree-gen-godot` (audit 1, FULL)
- `procgen-worlds/project-prales-runtime-wilderness` (audit 4, PARTIAL)
- `automation/blender-nodemode` (audit 6, PARTIAL)
- `procgen-worlds/blender-floaters-hard-surface-detail` (audit 7, PARTIAL)

Expanded skill:
- `characters/godot-runtime-procedural-creatures` (audit 5, PARTIAL; added part-placement gameplay effects, procedural parts inventory, IK specifics, and design deltas vs Spore)

No skill for audit 8 (DEPTH-LIMITED, no extractable workflow). Report at `docs/scout-reports/have-vs-need-2026-11-09.md`. Watchlist rows synced to `video-tooling-scout/references/tooling-watchlist.md`. README tables updated (skill count and category counts only).
