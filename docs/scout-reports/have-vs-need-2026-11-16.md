# Video tooling scout: have-vs-need — 2026-11-16

Run: daily-video-tooling-scout, Mon 2026-11-16 08:18 EST. Depth mode:
`pre-approved`, max 2 media downloads per run. Depth-escalation usage:
**0 downloads attempted, 0 succeeded, 0 skipped.** All 8 audited videos
are native Reddit clips (v.redd.it); per the skill the tooling signal for
those is in post text and comments, and full post text plus comments were
retrieved for all 8. The 3 YouTube candidates fell outside the top 8 and
are a beginner tutorial series, so no download was attempted for them
either. Allowance unused: 0/2.

## Gap alerts

**P1 ALERT — Rigging / skinning / animation-retarget stage (aegis,
trellis-pipe).** Nightshoal week 16 (RUSuper, 1xxioq5) gives the first
field-proven recipe for this exact gap: 12 harbour characters made in
TripoAI, rigged in Mixamo, with Opus writing a script that copies Mixamo
animations onto Tripo's skeleton when Mixamo cannot rig a model (the rum
seller failed), plus Blender weight fixes for tearing long coats and an
apron. Mixamo does not accept Tripo's skeleton, so models are uploaded
skeleton-less and Mixamo rigs them itself (worked for 3 of 12). The
2026-10-21 fix artifact (`aegis-pipeline/rigging-stage-design.md`, Tripo
P2.0 route recommended, Mixamo FBX path) is still unlanded; this run is
new evidence the Mixamo leg of that design works in production.

**P2 ALERT — MCP-driven DCC loop (aegis, foundry loop).** Same post: the
most complete agentic-DCC loop seen to date. Fable 5.2 is now the
manager (finds things to fix, writes tasks, checks results), Opus 5.5
agents build, and the loop is closed two ways: blind Gauntlet critics
compare the game to the mockup (black market harbour took 30 rounds; at
round 12 the author stopped it and demanded a top-down blueprint in
metres first, because the loop placed things by picture position and "the
picture is never actually 'proper'"), and a fresh-eyes agent reads the
whole plan with the sole job of proving it wrong (found 21 problems,
best one: the plan sent the missing boat south when the game says north).
Opus builds both harbour scenes in Blender through MCP. Prior art: the
`agentic-blender-asset-pipeline` skill. This is the pattern to copy for
the P2 spike.

**Possible, unverified — Rigging gap adjacent: TumbleRig.** Post
1xw84qm ("Rigging used to scare me. Then I tried TumbleRig") has no
retrievable selftext and no retrievable comments (Arctic Shift 422,
PullPush 0). The watchlist row from yesterday's run already records it
as a Houdini APEX auto-rig (Tumblehead, tumbletrove.com). No new evidence
today; do not count it as gap evidence.

## Videos scanned

- **Reddit:** 2 scan runs (Arctic Shift rate-limited differently each
  time: run 1 warned 429 on VoxelGameDev + 3Dmodeling, 47 video posts;
  run 2 warned 429 on photogrammetry, topology, aigamedev, comfyui,
  proceduralgeneration, 37 video posts). Combined candidate pool used;
  top-8 list below merges both runs. Subs: unity, unrealengine, godot,
  threejs, GraphicsProgramming, blender, houdini, substance3d,
  photogrammetry, gameassets, topology, aigamedev, comfyui, vibecoding,
  technicalart, proceduralgeneration, vfx, RealTimeVFX, shaders,
  VoxelGameDev, Simulated, 3Dmodeling, gamedev. Date range: last 2 days.
- **YouTube:** 11 channels (RyanKingArt, DefaultCube, Ducky3D,
  JoshGambrell, MaxHayArt, BlenderSecrets, GDQuest, KaizenTutorials,
  Brackeys, Entagma, OlivioSarikas), 2-day window. First attempt failed
  on all 11 channels with SSL CERTIFICATE_VERIFY_FAILED (stale sandbox
  egress CA in the yt-dlp venv bundles); refreshed the current Hatch
  egress CA into both venv certifi bundles and re-scanned once: **3
  videos found**, all Ryan King Art "Gingerbread House in Blender"
  beginner tutorial parts 3-5 (Nov 14-16). One warning: Ducky3D, one
  video behind a YouTube bot-check sign-in ("Sign in to confirm you're
  not a bot"); skipped, no retry, no cookies used.
- **Deep analysis cap:** 8 videos. The 3 YouTube videos scored below the
  top 8 and are a beginner series with paid asset packs; scanned, not
  deep-analyzed (see Non-goals).

## Videos deeply analyzed

1. "16 weeks of making game with Claude Opus in Godot" — RUSuper —
   r/vibecoding 1xxioq5 (score 48) + r/aigamedev crosspost 1xxikfy —
   v.redd.it — FULL
2. "I created an asset generator after 11 months of work that produces
   thousands of animated game assets in seconds — completely offline,
   with no AI required!" — Buchedegato — r/aigamedev 1xxbbgq (score
   144) — v.redd.it — FULL
3. "467M stars, billions of planets, all from one seed and every one of
   them can be visited. How I generate the galaxy for my space game" —
   Backbone_Labs — r/proceduralgeneration 1xwugk4 (score 101) —
   v.redd.it — FULL
4. "The Creator - shot recreation" — Key-Swimmer3238 — r/Houdini
   1xw7t59 (score 140) — v.redd.it — PARTIAL (re-scan: same post
   audited 2026-11-15, skill already exists; no new workflow evidence)
5. "Tree Simulator. Zoom into the chloroplast of a redwood, if you
   want." — Umairus — r/threejs 1xx1rsv (score 27) — v.redd.it — PARTIAL
6. "Eye Spy..." — Photini-By-Design — r/blender 1xxe665 (score 461) —
   v.redd.it — DEPTH-LIMITED (old project, no parameters)
7. "Materials with Dispersion" — Farrukh3D — r/blender 1xxedm8 (score
   445) — v.redd.it — DEPTH-LIMITED (tutorial promised, not yet out)
8. "Rigging used to scare me. Then I tried TumbleRig" —
   Existing-Fix7274 — r/Houdini 1xw84qm (score 50) — v.redd.it —
   DEPTH-LIMITED (title only; no selftext, no comments retrievable)

---

## 1. "16 weeks of making game with Claude Opus in Godot" (RUSuper)

Source: https://www.reddit.com/r/vibecoding/comments/1xxioq5/16_weeks_of_making_game_with_claude_opus_in_godot/ (also r/aigamedev 1xxikfy) | Nightshoal, a 1920s fishing and exploration game (Godot) | Demo free at https://profactor.itch.io/nightshoal

Tools used: Claude Opus 5.5 (Claude Code), Fable 5.2 (manager + checker), Jev (effort-level picker), OpenAI image API (mockups), Blender via MCP, TripoAI, Mixamo, ElevenLabs, Godot, GPT Astra (cost line only, $100).

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: let Fable manage, let Opus build against mockups judged by blind critics, let a fresh-eyes agent try to break the plan, and keep the human as the stop rule.

### Phase 1: Plan the whole game on paper first

**Do**
1. Plan every zone up front: where each zone is and what is in it (every island, harbour, person, quest, item, fish), each zone with a top-down blueprint.
2. Ask Opus to settle the economy question on the game's own gold simulator: Opus built a model on top of the simulator and answered that more time in later zones is not enough, fish need to pay a bit more each zone.
3. Rezone as the plan settles: Bridge city is now zone 2, tropics moved to zone 3.

**Check**
- The plan is a written document Jev can pick from ("Every pick is saved with its percentage so I can overrule it later").
- Economy tuning comes from the author playing it personally plus player feedback once all zones are done, not from the simulator alone. Commenter Total-Reasonable (score 7) flags the exact failure mode: "the economy model Opus built on your gold simulator only tells you what a simulated player does, and the sim player is probably an optimal or scripted one. Real players wander, fish badly, and skip content, so 'fish need to pay more each zone' could overshoot. Log real session data from the demo (gold earned per hour, time per zone) and compare it to the sim."

**Why**
Planning the whole game before building zone 2 means "later I (Well Claude) only have to build it." The simulator answers direction (pay more per zone); real play answers magnitude.

### Phase 2: Mockup, then Gauntlet-loop the scene against it in Blender

**Do**
1. OpenAI (image API) makes a mockup of the place.
2. Opus builds the scene in Blender through MCP.
3. Critics compare the game to the mockup blind (Gauntlet loop). Black market harbour took 30 rounds.
4. At round 12, stop the loop and make a top-down blueprint first (in metres), then resume. Rule added: a mockup of a place that already exists has to be made from the game's own view, not from imagination.
5. For the second harbour (Bridge city), do not chase the mockup as long: once the scene is overall good, stop the critics and fix it piece by piece from the author's notes.

**Check**
- Blind comparison against the mockup is the judge, not the author's eye.
- The round-12 intervention is the tell that the loop was failing: "the loop was placing things by where they land in the picture and picture is never actually 'proper' so to say, so something could look right and still stand in the wrong place."
- Bridge city harbour: 8 people on the dock, works at day/dusk/night/dawn, lamps turn on in the evening; hover-and-click people, fish trader and yard foreman open counters, every window shows the person's face "taken live from the 3D model."
- Black market harbour: only at night (by day "the market is shut"); 4 people on the dock (rod seller with leads to two more, fuel seller, boat repairer); sell protected fish for 3x if the patrol does not catch you; rest until dawn and "you wake up outside the chain."

**Why**
A picture can look right while the layout is wrong; the blueprint in metres is the ground truth the picture cannot supply. And a loop without a stop rule burns rounds: the second harbour shows the human stopping the critics once the scene is good enough and finishing from notes.

### Phase 3: Characters — TripoAI, then Mixamo, then a retarget script

**Do**
1. Make all 12 people for the two harbours in TripoAI.
2. Rig them in Mixamo for standing and talking animations. Mixamo does not accept Tripo's skeleton, so upload the model without a skeleton and let Mixamo rig it itself. This worked for 3 of them.
3. For the rest (including the rum seller, whom Mixamo "just couldn't rig, no idea why"): download the rigged version from Tripo and have Opus write a script that copies the Mixamo animations onto Tripo's skeleton.
4. Fix tearing in Blender: long coats and one apron tore when the arms moved, so Opus fixed the weights in Blender.

**Check**
- Two uploaded images show how the characters look outside the game (imgur.com/a/d9k1sAh).
- In-game check: faces in the dialogue windows come live from the 3D model; animations are standing/talking only.

**Why**
Mixamo's auto-rig is the fast path when it accepts the model; the retarget script is the fallback that keeps the pipeline moving when it does not. Weight fixes are a Blender job, not a generation job.

### Phase 4: Sound without ears — ElevenLabs, measured not listened to

**Do**
1. ElevenLabs makes the black market's sounds: night ambience, small dock sounds, a murmur for each of the four people (murmurs made but "nothing plays them yet").
2. Opus picks the takes by measuring them: "Opus can't listen to them, so it picks the takes by measuring them lol."

**Check**
- (Inference, labeled:) no listening check exists in this loop; measurement is a proxy for quality, and the murmurs are unverified in-game since nothing plays them yet.

**Why**
An agent that cannot hear can still select audio by measurable properties; the gap is explicit, not hidden.

### Phase 5: Fresh-eyes audit of the whole plan

**Do**
1. After the plan is written, let one more agent read all of it with fresh eyes; its only job is to prove it wrong.
2. It found 21 problems. Best one (author's words): "the plan sent the missing boat south when the game itself says it went north lol."

**Check**
- 21 problems found is the metric; the boat-direction catch is the proof the audit is real, not ceremonial.

**Why**
The builder cannot audit its own plan: the same context that wrote it will re-read it as correct. A separate agent with an adversarial job description is the cheapest reviewer available.

### Phase 6: Trailer filmed inside the game

**Do**
1. Author says vaguely what he wants; Opus comes up with options; Jev picks between them.
2. Opus films the trailer inside the game and cuts it together. First version had too little gameplay (basically only fishing), so the author listed what to show and Opus made a second one.
3. The keys lighting up on screen are the real key presses, not added in editing.

**Check**
- Trailer contents (author's list): fishing with the keys pressed, gear on the boat, exploring an island at night, finding a ship in a bottle, the Cabinet (one ship "fires its cannons inside the bottle"), a whale, a boat in trouble you can save, picking a talent, a storm, the 2 new harbours.

**Why**
A trailer cut from real play with real key presses is evidence, not a promise. The second version exists because the author, not the model, decided what "enough gameplay" means.

### Phase 7: Performance fixes and cost accounting

**Do**
1. Fix the talent chart freezing the game the first time it opened.
2. Ship the sea's map ready instead of rebuilding it on every start.
3. Replace render scale with one normal RESOLUTION list in settings; draw the Cabinet sharper.
4. Fix the white fog on the waterfall: it was the sun's reflection on the still river.
5. Total the week: Claude Max $200 x 4 = $800; Astra $100 x 1 = $100; ElevenLabs $11; TripoAI $20 x 2 = $40; OpenAI API credits $80; other things forgotten ~$100. "Around 1100-1150$." Hit 91% of the weekly limit again.

**Check**
- Zone 1 "works" because the author test-played it "like a gazillion times"; future zones need testing too, and the whole game at the end. "It will take some time though as I don't expect game to be finished for several months at least."

**Why**
A weekly cost total next to the output is what makes the loop auditable: 16 weeks at roughly $1,100 a week is the deal, stated plainly.

### The human method, distilled

1. "Once you enjoy the process everything becomes so much easier." (Author, on why this game worked after earlier attempts did not: he built something he himself would enjoy playing.)
2. Plan everything on paper, then let Claude build it.
3. A picture is not a plan: if the loop places things by picture position, stop and blueprint in metres first.
4. A mockup of a place that already exists must come from the game's own view, not imagination.
5. The builder does not audit its own plan; a fresh-eyes agent whose only job is to prove it wrong does.
6. Stop the critics once the scene is good and finish from your own notes.
7. Cost is part of the devlog: publish the total every week.

**Depth status:** FULL (complete author post text with exact numbers, costs, and quoted method + 9 comments; video clip is a gameplay trailer with no captions; a media download would add gameplay frames only, not pipeline detail).

---

## 2. "I created an asset generator after 11 months of work..." (Buchedegato)

Source: https://www.reddit.com/r/aigamedev/comments/1xxbbgq/i_created_an_asset_generator_after_11_months_of/ | "My Magic Asset Workshop" — demo/download: https://buchedegato.itch.io/my-magic-asset-workshop — Discord: https://discord.gg/DBmXaSBck

Tools used: a hand-written rule-based procedural generator (no AI, no internet); DeepSeek (interface and translations); free Claude (bug-finding in final stages); "AI RECIPE" JSON paste-in for custom assets. Export: PNG, BMP, TGA, animated GIF, JSON atlas, Godot and Unity compatibility. Windows and Linux; Mac version if there is enough demand.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: hand-written rules, not a model — type a word, get a historically accurate animated sprite, same seed same sprite.

### Phase 1: Type a word, get the asset

**Do**
1. Type what you want ("hoplite") and the program looks the word up, picks the helmet, shield, and spear that go with it, and generates the sprite with animations.
2. A random seed changes the small details so each one comes out a bit different; use the same seed and you get the exact same sprite every time.
3. If you type something it does not know, it says it does not recognize it instead of making something up. (Author, in comments: "If you type something it doesn't know, it just tells you it doesn't recognize it instead of making something up.")

**Check**
- Free demo on the site lets anyone check the whole catalogue without paying.
- Known limits, stated by the author: English support still has glitches ("sword" alone gives nothing; write "sword ICON" or "Soldier with a Sword"); fantasy classes thief/rogue/paladin were missing at launch and are being added; several languages are in beta.
- Commenter DjPersh confirms the English gap from use: "I tried some items like 'sword' and it gives nothing... paladin... gave me nothing like what I think a westerner would imagine."

**Why**
Refusing an unknown word is the rule-based generator's version of honesty: a lookup either matches or it does not, and the failure mode is visible instead of a hallucinated asset. (Author: "It's procedural generation, kind of like how Minecraft builds its worlds, but for sprites. I spent months writing the rules by hand: body shapes, armour and weapons for each culture, colors, animations, etc.")

### Phase 2: Coverage — cultures, nature, objects, terrain, effects

**Do**
1. Generate troops by culture and period: Stone Age to pre-industrial — Greek city-state hoplites, Chinese dynasties, Hittites, Assyrians, Macedonians, medieval military orders, Roman soldiers of every period, Celts, Gauls, Goths, Alans, African tribes, Amazons, Aztec/Olmec/Inca/Teotihuacan warriors, Napoleonic Wars, American revolutions, Zulu Wars. (Author: "with historical accuracy.")
2. Generate nature: 200+ tree species, 500+ flowers/plants/grass/rocks, 90+ animal species with juvenile versions (dolphins jump and splash, horses gallop, crocodiles do the death roll, turtles lay eggs), mounted units on horses, camels, elephants.
3. Generate objects and buildings: hundreds of objects (chairs, tables, chandeliers, forges, alchemy tables) adapted per culture, not just recolored ("Aztec food stalls are set up on the ground over blankets, while Chinese candles are placed inside bamboo stumps"); buildings with customizable floors/width/decorations, or hundreds of modular pieces (walls, floors, roofs, windows, doors open/glazed/at any height).
4. Generate effects and terrain: dozens of VFX (explosions, magic, level-ups, foraging, tree-felling, mining, sword movements, snow/rain, bees/fireflies/flies with count and dispersion), 30+ siege weapons with 500+ models (Greek fire, springalds, battering rams, crew optional, projectiles toggleable), hundreds of terrain types (grass, ice, snow, lava, water with adjustable transparency), 30+ paths/bridges with elevation/cliffs/waterfalls, 50+ crop plots, 400+ icon families with 5,000+ variations.
5. Animate everything: attacking, defending, running, walking, reloading, dying, throwing bombs/torches, mining, digging, talking, eating, fishing, and more, "perfectly sequenced and logically consistent."

**Check**
- Every asset comes with its animation set; seasons (4) adapt each asset including correct seasonal fruits; wind, falling leaves, fallen fruit on the ground; picked-flower variants for gathering games; real-world scale option relative to soldiers.
- Scale of the system, author's numbers: each sprite has 1,400,832 possible appearances from style options alone, "nearly 98 quintillion possible combinations" in total.

**Why**
Culture is a rule set, not a palette swap: the same object type is built differently per culture. That is the whole value of hand-written rules over a generative model: consistency across thousands of assets.

### Phase 3: Style it — three styles, 19 palettes, 8 facings

**Do**
1. Pick a style: voxel, chibi, or pixel art (hand-drawn and NES styles coming; an Age of Empires / American Conquest / Cossacks style in progress). Switching style re-renders the same asset with all its animations.
2. Pick from 19 color palettes (dark, vibrant, 16-bit, 8-bit), unit outlines, line smoothing, blood on/off, team colors.
3. Pick the view: side view (2D) or overhead, with 8 directional facings.

**Check**
- The same soldier in a different style is the check that style is a rendering choice, not a different asset.

**Why**
Style as a switch means one catalogue serves three games. The author built it this way because "developers who struggle to get consistent assets with proper animations" is the customer.

### Phase 4: Custom assets via JSON ("AI RECIPE")

**Do**
1. For anything the program cannot generate, or any animation you want: ask any AI to create a JSON file describing what you want, paste it into the program's "AI RECIPE" section, and it generates the custom animation or design.
2. Author's example to a commenter: for a cowboy, ask ChatGPT or DeepSeek to generate a JSON of the cowboy with specifications, paste the JSON in, and it generates it; same for a gun image.

**Check**
- (Inference, labeled:) the JSON recipe is user-authored spec, not a vendor acceptance test; no schema is published in the post, so the exact fields are unverified.

**Why**
The escape hatch keeps the rule system open: the catalogue covers the common cases, JSON covers the long tail, and the generator still does the drawing so the output stays consistent.

### Phase 5: Export and ship

**Do**
1. Export as PNG, BMP, TGA, animated GIF, JSON atlas, or with Godot/Unity compatibility.
2. Use commercially with no credit required. First-week discount; all future updates free.
3. Note what is missing, from the author and commenters: no MCP ("Does it have MCP? I could use it in my ai workflow" — unanswered, no MCP claimed); no 3D-model export yet (commenter asked; author did not promise it); no mobile yet (in progress, "practically everything is already there, I'm just arranging the interface," about a week); westerns not handled yet (Sioux, Cherokee tribes already added; hats/guns/clothes coming this week); no UI generation yet; no ships yet; 28 languages supported.

**Check**
- Commercial-use terms are stated in the post ("Everything you create can be used in your commercial games, with no credit required").

**Why**
Offline and token-free is the product: "It doesn't use tokens or AI: you can run it on a computer without an internet connection."

### The human method, distilled

1. Rules, not models: "I spent months writing the rules by hand."
2. Refuse rather than hallucinate: unknown word gets "I don't recognize it," not a wrong asset.
3. Same seed, same sprite: determinism is the feature that makes the catalogue usable.
4. Culture is construction, not color: an Aztec stall and a Chinese stall are built differently.
5. The escape hatch is a spec (JSON), not a prompt: the generator still draws, so output stays consistent.

**Depth status:** FULL (complete author post text, ~8,600 chars, with exact counts + 21 comments including author replies; video clip is a showcase reel; a media download would add frames, not pipeline detail).

---

## 3. "467M stars, billions of planets, all from one seed..." (Backbone_Labs)

Source: https://www.reddit.com/r/proceduralgeneration/comments/1xwugk4/467m_stars_billions_of_planets_all_from_one_seed/ | Space game (exploration, resources, combat), Unity client + browser/mobile planned, video captured straight from Unity, still in development.

Tools used: Unity (Mono editor / IL2CPP / .NET runtimes); grayscale density maps (own PNG decoder); reimplemented Unity RNG; improved Perlin + ridged multifractal (Musgrave-style) terrain; single GPU buffer + one draw call per camera; background-thread generation and sorting.

This audit reconstructs the exact workflow shown in the video, step by step, so another agent can follow the same process. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The video's core method is: one seed, density maps for placement, bit-exact math for determinism, and one draw call for all stars.

### Phase 1: Place the galaxy with density maps

**Do**
1. Start from one seed. From it: 467,561,373 stars, about 4.9 billion planets, 8.2 billion moons, with orbits, atmospheres, chemistry, geology, and terrain. Nothing is stored on disk.
2. Use density maps: grayscale images of the galaxy seen from top, with the spiral arms already in them. One map decides where the stars go; three more maps decide where the dust goes. "The seed put each thing in his exact place." (Author, in comments.)
3. Render dust as many semi-transparent sprites in three sizes (big, medium, small), always facing the camera. The brighter the pixel in the map, the bigger and more opaque the sprite. Dark zones are just gaps in the maps: no dust, so you see black and loose stars.
4. When on a planet, the sky is the same galaxy seen from that place, not a generic skybox.

**Check**
- Census numbers, verified by walking the whole galaxy star by star with the same code the client uses (no extrapolating from a sample): 467,561,373 stars; ~1 star in 100 has no planets at all; ~185 million planets have liquid-water oceans; 1,852,531 have life; 281,081 neutron stars; 186,578 black holes.
- "You can fly to any star, go into its system and visit any planet or moon, it gets generated when you arrive and anyone who goes there sees exactly the same thing, bit for bit."

**Why**
Maps are cheaper than math for galaxy shape: the spiral structure is authored once into an image, and the seed does the rest. Dust as camera-facing sprites is the same trick as the galaxy row already in the watchlist (Blender GeoNodes galaxies), done in Unity with maps instead of nodes.

### Phase 2: Make planets from chemistry, not random rolls

**Do**
1. Derive each planet's chemistry from the rock/metal/ice mix it formed from, calibrated so Earth comes out within about a point of its measured composition.
2. Work out the final state for every candidate surface and throw away the ones that contradict themselves (e.g. frozen oceans at 200 C).
3. Version 1 had "something like 16% nonsense planets"; now: "Zero contradictions in the census, which honestly took way longer than I'd like to admit."
4. Rate every world 0-10 for minerals, rare earths, energy, water, food, and jump fuel, plus hostility, all from its actual data. The world map splits the surface into 32 cells; each cell gives resources based on the real terrain under it (coast gives water, volcanic slope gives geothermal, icy moon over an ocean gives water and not much else).

**Check**
- The census is the check: zero self-contradicting surfaces across ~4.9 billion planets.
- Author's design rule, stated in comments: "when realism and fun are in conflict, I choose fun" — and "the most valuable stuff use to be on the most hostile worlds."

**Why**
Derived chemistry plus a contradiction filter is an acceptance test built into the generator: nonsense is rejected at generation time, not found by players. (Adjacent pattern, not a gap match: this is procedural validation, not the P1 AI-vendor acceptance spec.)

### Phase 3: Terrain as a pure function of 3D position

**Do**
1. Terrain height at any point is a function of its 3D position: improved Perlin plus a ridged multifractal (Musgrave style), with every octave rotated so the mountains do not line up with the noise axes.
2. Small moons are not spheres: nine shape families based on real bodies like Phobos or Arrokoth.
3. Because terrain is a function, zoom is nearly free: the whole globe and a bit of coastline are the same function sampled at different resolution.

**Check**
- (Inference, labeled:) no numeric parameters (octave counts, frequencies, amplitudes) are given in the post or comments.

**Why**
A pure function needs no storage and no LOD stitching: resolution is a sampling choice, not a data problem.

### Phase 4: Bit-exact determinism across platforms

**Do**
1. Fix the float problem: Mono in the editor does float math at double precision and rounds "whenever it feels like it"; IL2CPP and .NET round after every operation. Result: roughly 7 in 25,000 stars had a different temperature depending on where it ran.
2. Apply the ugly fix: an explicit `(float)` cast after every single operation in the generator; no `Math.Pow` or any library function whose last bit depends on the platform.
3. Reimplement Unity's RNG and check it draw by draw against the real one.
4. Read the density maps with your own PNG decoder, because Unity was compressing them on import and changing 36% of the pixels.
5. Run the same generator locally on every platform (Unity client, browser, maybe mobile); the server only keeps what players change.

**Check**
- Same seed, same galaxy, on any PC, "down to the bit." The census numbers are the proof: they were produced by the client code itself.
- Commenter question answered: "leave and come back and its exactly the same... every one of them runs the same generator locally, so nothing about the galaxy gets downloaded."

**Why**
"Same algorithm" is not enough; it has to be the same bits. Every layer that can silently change a value (runtime float promotion, library functions, texture import compression) gets replaced or pinned.

### Phase 5: Render it — one buffer, one draw call, universe moves around the camera

**Do**
1. Drop the GameObject-per-star version (about 19 fps).
2. Put all loaded stars in a single GPU buffer drawn with one draw call per camera; a background thread sorts them back to front; new sectors generate in the background while flying.
3. Do not move the camera: the universe moves around it, so everything stays close to the origin where floats keep their precision.
4. Result: "From 19 to around 400 fps."

**Check**
- 19 fps before, ~400 fps after, same scene class. The origin trick is what makes the float budget work at galaxy scale.

**Why**
One draw call plus background generation is the only shape that fits hundreds of millions of stars; and at that scale, float precision is a rendering problem solved by never letting coordinates get large.

### The human method, distilled

1. Author the shape once (density maps), let the seed do the rest.
2. Derive, don't roll: chemistry from formation mix, resources from real terrain, calibrated so Earth comes out right.
3. Reject nonsense at generation time: work out the final state, throw away self-contradictions.
4. Same bits, not same algorithm: cast after every op, reimplement the RNG, decode your own PNGs.
5. The universe moves around the camera: keep coordinates near the origin where floats are precise.
6. "When realism and fun are in conflict, I choose fun."

**Depth status:** FULL (complete author post text, ~3,900 chars, with exact census numbers + 29 comments including detailed author replies; video is captured Unity footage; a media download would add frames, not pipeline detail).

---

## 4. "The Creator - shot recreation" (Key-Swimmer3238) — RE-SCAN

Source: https://www.reddit.com/r/Houdini/comments/1xw7t59/the_creator_shot_recreation/ | r/Houdini post 1xw7t59, score 140 (was 106 yesterday), 13 comments (was 12).

Tools used: Blender (modeling), Substance Painter (texturing), Houdini + Solaris (lighting and scene assembly), Nuke (comp), Meadow toolkit (vegetation scattering, by beatreichenbach), KTT terrains, Megascans cliffs, vegetation assets (external). Full breakdown linked by the author (ArtStation artwork lEraae) returned HTTP 403 when fetched yesterday and was not re-fetched today.

This post was already audited in the 2026-11-15 run and converted to the skill `procgen-worlds/creator-shot-blender-houdini-solaris`. Today's re-scan (overlapping 2-day window) adds no new workflow evidence. New details since yesterday: one additional comment (59vfx91, score 2) with a scale critique: "The temple feels a little small scale, something about the wear details, the scale of the AO mask in the texturing don't give me the impression of a gigantic object. I think you need to dial the large wear back a bit and then layer on more subtle high res details. It could also be partially be that the comp of it feels a little crunchy for how distant the object is, and therefore feels slightly less atmospheric than it should be." That critique (comp too crunchy for the distance) is already reflected in the existing skill. Author's own notes, already captured: "I handled most aspects of it. Except for vegetation assets and Megascans cliffs. There are some monk models too with bad cloth sims, but they hold up at this scale and give the shot some movement." No skill expansion needed.

**Depth status:** PARTIAL (re-scan of an already-audited post; tools and stages named, no parameters).

---

## 5. "Tree Simulator. Zoom into the chloroplast of a redwood, if you want." (Umairus)

Source: https://www.reddit.com/r/threejs/comments/1xx1rsv/tree_simulator_zoom_into_the_chloroplast_of_a/ | Coast redwood simulator.

Tools used: Rust engine, raw WebGL2 viewer, Rust physics engine. Render stack: HDR post stack (4x MSAA, SSAO, DOF, bloom, light shafts, film grade), wrapped-Lambert sun and sky lighting, sun-tinted aerial fog, procedural shader textures. No path tracing, no shadow maps yet. 11,800 lines of source code.

This audit reconstructs the workflow as described, so another agent can follow the same approach. Every phase has three parts: **Do**, **Check**, and **Why**. The project's core method is: simulate the tree's real biology (cohesion-tension water, pipe-model trunk) and render it at every scale from trunk to chloroplast.

### Phase 1: Model the tree on real biology

**Do**
1. Move water by cohesion-tension (the mechanism that pulls water up a redwood).
2. Build the trunk on the pipe model (trunk as a bundle of pipes, one per branch).
3. Zoom from the ~100 m trunk down to xylem, phloem, and chloroplasts. "Everything you see is drawn, based on all real documentation of how redwoods look like, internal structure and so on."

**Check**
- Open question from commenter PurchaseCommercial34, unanswered by the author: a ~100 m trunk down to a chloroplast is ~7 orders of magnitude, "way past what float32 positions and one depth buffer can hold without jitter and z-fighting. do you swap to a separate scene per scale level and crossfade, or keep one world and re-center the origin + tighten near/far as you zoom in? also does the cohesion-tension sim drive anything you can actually see at the cell level, like flow in the xylem?"
- (Inference, labeled:) no answer is in the retrieved comments, so the scale-handling mechanism is unverified.

**Why**
Biology first, rendering second: the simulation's structure comes from the documentation, not from what looks good.

### Phase 2: Render it in raw WebGL2

**Do**
1. Render with a raw WebGL2 viewer on a Rust engine and Rust physics engine (11,800 lines).
2. Apply the HDR post stack: 4x MSAA, SSAO, DOF, bloom, light shafts, film grade; wrapped-Lambert sun and sky lighting; sun-tinted aerial fog; procedural shader textures.
3. Note what is not there yet: no path tracing, no shadow maps.

**Check**
- (Inference, labeled:) no performance numbers, frame times, or hardware are given; the only scale figure is the 11,800 lines.

**Why**
Raw WebGL2 plus a hand-rolled HDR stack is the author's answer to "draw everything": no engine, no path tracer, just the documented structure rendered at every scale.

### The human method, distilled

1. "Based on all real documentation" — the biology is the spec.
2. "I do not know why I made this. Perhaps sharing this with others will light the way forward."

**Depth status:** PARTIAL (architecture and render-stack parameters are stated, but no build steps, no performance numbers, and the key scale-handling question is unanswered; a media download would show the zoom behavior but the clip is a short native Reddit video whose tooling signal is the post text).

---

## 6. "Eye Spy..." (Photini-By-Design) — DEPTH-LIMITED

Source: https://www.reddit.com/r/blender/comments/1xxe665/eye_spy/ | score 461, 15 comments.

Tools used: Blender shader editor (procedural eye), Blender Geometry Nodes (crawling creature). Author: "An old project I whiped together a few years back using a procedural eye I made in the shader editor, and a crawling creature in geometry nodes."

No parameters, node names, or workflow steps are given in the post or comments (comments are reactions, plus one unanswered question from Ok_Argument_5256 about making the whole eye share one texture without a seam line). Report only, no skill.

**Depth status:** DEPTH-LIMITED (tools named, no workflow detail; a media download would add frames of the finished render, not the shader or node setup).

---

## 7. "Materials with Dispersion" (Farrukh3D) — DEPTH-LIMITED

Source: https://www.reddit.com/r/blender/comments/1xxedm8/materials_with_dispersion/ | score 445, 16 comments.

Tools used: Blender 5.3 (new light dispersion setting), Cycles rendering. Author: "Made some materials with the new light dispersion setting added in Blender 5.3. Using cycles for rendering." Theme: Rupee / Sims plumbob (commenters identified it; author confirmed). Author promises a tutorial "in a few days" on https://www.youtube.com/farrukh3d. No parameters disclosed. New watchlist row: Blender 5.3 light dispersion setting (Cycles); revisit when the tutorial lands.

**Depth status:** DEPTH-LIMITED (new Blender 5.3 feature named, no parameters; the tutorial does not exist yet).

---

## 8. "Rigging used to scare me. Then I tried TumbleRig" (Existing-Fix7274) — DEPTH-LIMITED

Source: https://www.reddit.com/r/Houdini/comments/1xw84qm/rigging_used_to_scare_me_then_i_tried_tumblerig/ | score 50, 4 comments per scan.

Tools used: TumbleRig (named in the title only). No selftext (0 chars). Comments unretrievable: Arctic Shift 422, PullPush 0 comments, old Reddit 403. The watchlist row from yesterday's run already records TumbleRig as a Houdini APEX auto-rig (Tumblehead, tumbletrove.com); today's post adds no new evidence. Possible rig-gap adjacent, unverified; not counted as gap evidence.

**Depth status:** DEPTH-LIMITED (title only; a media download would show the rigged result, not the tool's workflow).

---

## Have-vs-need

### Aegis (primary)

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Mixamo auto-rig + Tripo-skeleton animation retarget script | Nightshoal week 16 | NEED | Inventory: "No rigging / skinning / animation-retarget stage in the foundry"; fix artifact `aegis-pipeline/rigging-stage-design.md` prepared 2026-10-21, unlanded | **Adopt now** — this run is field evidence the Mixamo leg works (3/12 rigged clean, retarget script covers the rest, Blender weight fixes for coats). Land the prepared fix artifact. |
| MCP-driven Blender scene building + blind Gauntlet critic loop | Nightshoal week 16 | PARTIAL | Aegis has review/ blind-review vote binding + QA gates, but no agent-driven DCC loop; P2 gap row exists | Backlog (P2) — copy Fable-manager + Opus-builders + Gauntlet-critics + fresh-eyes-audit as the spike pattern |
| Fresh-eyes adversarial plan audit (21 problems found) | Nightshoal week 16 | PARTIAL | Aegis has lore-auditor + QA gates; no plan-level adversarial audit agent | Backlog — cheap reviewer pattern, applies to intake/ plans |
| Economy model on own simulator | Nightshoal week 16 | HAVE | `tools/ts/economy-sim` | None — but carry the commenter's calibration warning: sim players are optimal/scripted; tune against real session data (gold/hour, time/zone) |
| Offline rule-based sprite generation + JSON "AI RECIPE" custom assets | Asset Workshop | PARTIAL | Aegis intake/ does concept-to-input generation; no deterministic rule-based sprite path, no JSON-recipe manifest pattern | Watchlist — closer fit for 2d3d/Desktop City; note the JSON-recipe pattern as adjacent to the P1 acceptance-spec gap (user-authored spec, not vendor spec) |
| Density-map galaxy + bit-exact determinism recipe | Galaxy post | NEED | Aegis Rust zone sim is already deterministic (Q16.16 fixed-point); no galaxy-scale procgen in scope | Watchlist (pattern only) — adopt the census-validation discipline (walk the whole space, zero contradictions) and the explicit-float-cast rule for any cross-platform determinism work |
| Blender → Substance Painter → Houdini Solaris → Nuke shot pipeline | The Creator (re-scan) | NEED | Foundry is TRELLIS-based; no Solaris/Nuke cinematic stage | Watchlist — cinematics/trailer bucket; skill already exists |
| Rust + raw WebGL2 multi-scale tree simulator | Tree Simulator | NEED | Different engine (Rust/WebGL2 vs Aegis UE + Rust sim); no tree sim in scope | Skip for Aegis; watchlist pattern (multi-scale rendering) |
| Blender 5.3 light dispersion (Cycles) | Materials with Dispersion | NEED | No material/dispersion work in foundry | Watchlist — revisit when Farrukh3D's tutorial lands |
| TumbleRig (Houdini APEX auto-rig) | TumbleRig post (title only) | NEED | Houdini-only; foundry has no rig stage, but TumbleRig is not a foundry stage | Watchlist — already rowed 2026-11-15; no new evidence today |

### 2d3d

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Offline rule-based sprite generation (word lookup, seed-deterministic, JSON atlas + Godot export) | Asset Workshop | PARTIAL | HAVE: procedural texture/audio generators (`pipeline/proc/make_textures.py`), pixelize + asset installer with manifest/provenance/acceptance; no word-driven rule-based sprite generation | **Backlog (strongest 2d3d fit today)** — evaluate the rule system + JSON "AI RECIPE" pattern against `make_textures.py` and the P1 import-validation gap (manifest pattern) |
| Mixamo auto-rig + Tripo retarget script | Nightshoal week 16 | PARTIAL | NEED: production-conversion stage (retopo, UV, rig, LOD, compression) for generated meshes; no rig stage named | Backlog — retarget-script pattern applies directly to 2d3d's generated meshes |
| MCP-driven Blender building + Gauntlet loop | Nightshoal week 16 | PARTIAL | 2d3d has Godot + Blender tooling; no agentic DCC loop documented | Watchlist |
| Density-map galaxy | Galaxy post | NEED | 2D/3D side-scroller; galaxy-scale procgen out of scope | Skip |
| Tree Simulator / Blender 5.3 dispersion / TumbleRig | — | NEED | Out of scope or no parameters | Skip / watchlist |

### Desktop City

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Offline rule-based sprite generation (culture-adapted objects/terrain/seasons, JSON atlas + Godot compat) | Asset Workshop | PARTIAL | HAVE: headless Blender sprite render (`tools/gen_iso_sprites.py`), procedural authoring (`tools/procedural_art.py`), sprite contract/standards; no rule-based word-driven generation | Backlog — evaluate against `procedural_art.py`; the season/adaptation rules fit city sprite variants |
| Blind-critic-against-mockup QA loop | Nightshoal week 16 | PARTIAL | HAVE: `tools/qa_model_vs_sprite.py`, `tools/check_asset_views.py`; no blind-critic loop | Watchlist — QA pattern upgrade candidate |
| Shader-driven skyline fill | — | NEED | P1 gap; no equivalent (every building authored/generated) | No match today; gap stands |
| Density-map galaxy / Tree Simulator | — | NEED | Out of scope (space procgen; Rust/WebGL2 sim) | Skip; note TreeSculpt row already covers tree tooling |

### Solarempire

| Tool / stage | Found in | Status | Repo evidence | Recommendation |
|---|---|---|---|---|
| Mixamo auto-rig + Tripo retarget script | Nightshoal week 16 | HAVE (stage present) | HAVE: rigging stage present (`stages/rig.py`, `assetpipe/blender/rig.py`) — unlike Aegis | None for the stage; backlog the retarget-script pattern as an enhancement variant |
| Offline rule-based sprite generation | Asset Workshop | PARTIAL | Blender-stage asset pipeline; no rule-based intake path; Godot export compat relevant | Watchlist |
| Density-map galaxy generation | Galaxy post | NEED | Space game thematically, but implementation is Unity; Solarempire is Godot | Watchlist (technique pattern for space-scale procgen, not the implementation) |
| MCP-driven DCC loop | Nightshoal week 16 | NEED | No agentic DCC loop evidenced | Backlog (same P2 pattern as Aegis) |
| Godot import validation gate / export budgets | — | NEED | P1 gap; no Godot project yet | No match today; gap stands |

## Gap recommendations (highest-leverage NEEDs)

1. **Land Aegis's rig stage using the Nightshoal recipe (P1).** Mixamo rigs Tripo models skeleton-less; when Mixamo fails, a script copies Mixamo animations onto Tripo's skeleton; Blender weight fixes handle coats/aprons. The fix artifact is already prepared (2026-10-21) and unlanded; this run supplies the field evidence. Next step: land `aegis-pipeline/rigging-stage-design.md` (waits on Ehsan reminting fine-grained GitHub tokens).
2. **Use the Nightshoal week-16 loop as the P2 MCP-DCC spike pattern.** Fable 5.2 manager, Opus 5.5 builders via Blender MCP, blind Gauntlet critics with a metre-blueprint stop rule, fresh-eyes adversarial plan audit (21 problems). Next step: spike Blender MCP behind the review stage with the Gauntlet stop rule (blueprint before more rounds).
3. **Evaluate the Asset Workshop's rule-based generation for 2d3d and Desktop City (backlog).** Seed-deterministic, offline, token-free, JSON atlas + Godot export, "AI RECIPE" JSON escape hatch. Next step: compare its rule catalogue and JSON schema against 2d3d `pipeline/proc/make_textures.py` and Desktop City `tools/procedural_art.py`.
4. **Adopt the galaxy post's determinism discipline as a pattern (watchlist).** Explicit `(float)` cast after every op, no platform-dependent library functions, reimplemented RNG checked draw by draw, own PNG decoder (Unity import changed 36% of pixels), census validation (walk the whole space, zero contradictions). Next step: reference in Aegis determinism work; no code change proposed.
5. **Blender 5.3 dispersion: watch only.** Revisit when Farrukh3D's tutorial lands on youtube.com/farrukh3d.

## Watchlist trending

Genuine reappearances today (from `bin/trend_watchlist.py --date 2026-11-16`):

- MCP servers driving Blender/Unreal (agentic DCC) (first seen 2026-09-27, BACKLOGGED; seen again 2026-11-16) **TRENDING** — genuine: Opus builds Blender scenes via MCP (Nightshoal week 16).
- Fable 5.2 steering (Opus-class model driving Blender MCP plus Tripo) (first seen 2026-11-10; seen again 2026-11-16) **TRENDING** — genuine: Fable is now the manager and checker.
- ElevenLabs SFX (hit-and-miss, cleanup budget) (first seen 2026-11-10; seen again 2026-11-16) **TRENDING** — genuine: ElevenLabs made the black market sounds; Opus picks takes by measuring.
- Claude Code Opus 5.5 + Tripo P2 + ElevenLabs solo-game pipeline (first seen 2026-11-14; seen again 2026-11-16) — genuine: week 16 is the same pipeline family.
- Meadow toolkit, KTT terrains + Megascans cliffs, Houdini Solaris + Nuke comp (first seen 2026-11-15; seen again 2026-11-16) — same post 1xw7t59 re-scanned in the overlapping window, already audited 2026-11-15; no new evidence.
- TumbleRig (first seen 2026-11-15; seen again 2026-11-16) — same post 1xw84qm re-scanned; no new evidence.

Note on the raw script output: it over-matched on the bare tokens "Godot" and "Unity" (and "Blender MCP", "Mixamo", "Substance Painter", "Geometry Nodes", "Opus 5.5", "Astra"), appending "seen again 2026-11-16" to 46 rows where the specific tool was not used. All 46 were qualified in place in `references/tooling-watchlist.md` with a bracketed "[2026-11-16 auto-match was token overlap on ...; not a genuine reappearance]" note, per the file's established practice. Only the 4 genuine rows above keep a bare "seen again 2026-11-16".

New watchlist additions (append-only):

- **My Magic Asset Workshop** (offline rule-based procedural sprite/asset generator, Buchedegato) — WATCH. 11 months, no AI, no internet; word lookup, seed-deterministic; JSON atlas + Godot/Unity export; "AI RECIPE" JSON paste-in; no MCP, no 3D export yet.
- **Density-map galaxy generation** (Unity, grayscale density maps + camera-facing dust sprites, bit-exact cross-platform determinism) — WATCH. Distinct from the 2026-10-09 Blender GeoNodes galaxy row.
- **Blender 5.3 light dispersion setting (Cycles)** — WATCH. New Blender 5.3 feature; tutorial promised; revisit when it lands.

## Non-goals (tools found but correctly skipped)

- **Eye Spy procedural eye + GeoNodes creature:** tools named, no parameters; report only.
- **Ryan King Art Gingerbread House parts 3-5 (YouTube):** beginner Blender tutorial series with paid Geometry Nodes/ornament/wreath asset packs; low tooling novelty for the four repos; scanned, not deep-analyzed.
- **Tree Simulator:** impressive multi-scale Rust/WebGL2 sim, but no build steps, no perf numbers, key scale question unanswered; engine-runtime reference only.
- **TumbleRig:** title-only evidence today; already watchlisted from yesterday; no new claim made.
- **Ducky3D bot-checked video:** YouTube sign-in wall; skipped, no cookies, no retry.

## skill_library artifacts (staged in ~/workspace/video-tooling-scout-public/)

- **Expand** `skills/automation/nightshoal-opus-weekly-loop/` with week-16 evidence (Fable 5.2 manager, 30-round Gauntlet with round-12 blueprint intervention, Mixamo + Tripo retarget script, fresh-eyes audit finding 21 problems, economy model, perf fixes, 91% limit, ~$1,100-1,150).
- **New** `skills/procgen-worlds/offline-procedural-sprite-generator/` (My Magic Asset Workshop: word lookup, hand-written culture rules, seed determinism, JSON "AI RECIPE", style/palette/facing switches, export formats).
- **New variant** `skills/procgen-worlds/procedural-galaxy-density-maps-unity/` (density maps + dust sprites + bit-exact determinism; distinct from the existing Blender GeoNodes `procedural-galaxy-generator-blender`).
- **No skill** for The Creator (already exists from yesterday's run), Eye Spy, Tree Simulator, Materials with Dispersion, or TumbleRig (DEPTH-LIMITED / re-scan / no extractable workflow).
- Full report copied to `docs/scout-reports/have-vs-need-2026-11-16.md`; new watchlist rows synced to the repo mirror's `video-tooling-scout/references/tooling-watchlist.md`; `skills/README.md` grouped table + root README skill/category counts updated.

## Run notes / gaps in evidence

- Arctic Shift 429'd 2 subs on run 1 and 5 subs on run 2 (different sets); the combined pool was used, but a video in a 429'd sub on both runs could have been missed. No evidence of a missed top candidate: the two runs' top-10 lists agree except for the 429'd subs' entries.
- Old Reddit JSON is 403-blocked from this sandbox, so full selftext came from Arctic Shift subreddit searches instead; all 8 retrieved in full.
- PullPush comment search 400s for post IDs fetched with wrong (video) IDs initially; corrected to permalink post IDs, then 1xw84qm still returned 0 comments (Arctic 422). TumbleRig audit is title-only.
- YouTube scan: SSL CA staleness (Hatch egress CA missing from both yt-dlp venv certifi bundles) fixed by appending the current CA from /usr/local/share/ca-certificates/hatch-egress-ca.crt; re-scan recovered 3 videos. Ducky3D one video behind a bot-check sign-in; skipped.
- No approval gates hit; no downloads attempted; no model files downloaded.
