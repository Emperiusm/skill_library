# Video tooling scout: have-vs-need 2026-10-15

Run: daily cron `daily-video-tooling-scout`, Thu 2026-10-15 08:18 EDT.
Depth mode: `pre-approved` (max 2 media downloads/run, enabled by Ehsan 2026-09-27).
Depth escalation used: **0 attempted / 0 succeeded / 0 skipped** (see Depth note).
Scan: `/usr/bin/python3 bin/scan_videos.py 2` over 18 subreddits, Oct 13-15 2026.
**Result: scan succeeded, 3 video posts** (Arctic Shift primary; PullPush fallback armed but unneeded).
Two-pass scan (initial + verification re-run) returned the identical 3 posts.

Report: `hidden_files/have-vs-need-2026-10-15.md` (goal workspace; the body's
`~/workspace/your_files/video-tooling-scout/` path is stale per goal rules).

## Depth note

All 3 posts are native Reddit clips (v.redd.it); per the skill's workflow
step 2, the tooling signal for native clips lives in post text and comments,
which were fully retrieved via `bin/fetch_comments.py` (Arctic Shift, first
pass, no failures). None of the three clips is a tutorial or breakdown with
visible node graphs, parameters, or transcripts to recover, so a media
download would add showcase footage only, not an auditable workflow. The
pre-approved allowance (2) went unused, and no approval gates were hit.
A PullPush attempt to fetch full post selftexts 429'd once; not retried
(no retry storm). Audits below use the scan selftext snippets (300 chars)
plus full retrieved comments (fetch caps bodies at 800 chars; noted where
a comment was truncated).

## Scan anomaly (Arctic Shift coverage, third run in a row)

The 2-day window was Oct 13-15, but all 3 returned posts are from Oct 14
midday (12:09 and 12:52 EDT). The Oct 13 run showed the same pattern (window
Oct 11-13, all returned posts from Oct 11). Either posting volume in the
18 watched subs genuinely cratered, or Arctic Shift's index has multi-day
coverage gaps. Treat today's "3 posts" as "3 posts Arctic Shift surfaced",
not a verified census of the subs. Transient per-sub 429s (gameassets on
pass 1, photogrammetry on pass 2) affected no post in either pass.

## Gap alerts

**No P1/P2 gap was filled today.** Explicit checks:
- The Godot thread's commenter questions about mesh/LOD/audio streaming
  and mesh chunking (leetNightshade) are questions, not a tool or a
  fill for Solarempire's P1 "Godot import validation gate + re-measured
  export budgets" gap (no import validation, no budgets, no numbers).
- The James20k engine-wishlist (shadows, MSAA effects, compositor,
  transparency, SSR, frame pacing, input latency, multithreaded rendering)
  is a feature wishlist, not the Aegis P1 per-asset perf-budget gap (no
  tri counts, texel densities, or draw-call budgets disclosed).
- The Jolt physics anecdote is a commenter describing their own project,
  not the author's pipeline; it matches no P1 gap (no rig/retarget,
  mesh-compression, mesh-refinement, acceptance-spec, skyline-fill, or
  MCP-agentic-DCC content anywhere in the run).
- "Raycast wheel woes" (post #2 selftext) is a two-word aside in a
  joke clip, not a workflow.

## Videos scanned

3 video posts (scan window 2 days, min score 20, deep cap 8). Subreddits:
unity, unrealengine, godot, blender, houdini, substance3d, photogrammetry,
gameassets, topology, aigamedev, comfyui, vibecoding, technicalart,
proceduralgeneration, vfx, Simulated, 3Dmodeling, gamedev.

| # | Sub | Title | Creator | URL | Post | Score | Comments | Rel |
|---|-----|-------|---------|-----|------|-------|----------|-----|
| 1 | godot | Tired of hearing that "Godot can't do 3D", so here some of my humble 3D game | jijigri_ | https://v.redd.it/j6guhg5xhgvh1 | 1x5vcp9 | 94 | 33 | 11.9 |
| 2 | godot | i guess they're just excited to race. | Dangerous-Town2195 | https://v.redd.it/1v5rctbajgvh1 | 1x5vfxy | 45 | 3 | 0.2 |
| 3 | blender | Learning motion design and having some fun with geonodes flower setup | Specialist-Peach-789 | https://v.redd.it/35koxs8fqgvh1 | 1x5whnb | 20 | 4 | 0.1 |

Deep-analyzed: #1 (DEPTH-LIMITED), #3 (DEPTH-LIMITED); #2 marked NO-TOOLING.
0 reached FULL depth.

## Deep audits

### 1. "Tired of hearing that \"Godot can't do 3D\", so here some of my humble 3D game" (jijigri_)

Source: https://v.redd.it/j6guhg5xhgvh1 | r/godot post 1x5vcp9 (score 94, 33 comments).

Tools used: Godot (version undisclosed; author's multi-year project).

This audit reconstructs what the thread actually evidences (native Reddit
video; the tooling signal is in the post text and comments per the skill).
The video's core claim is: Godot 3D scales fine; the scaling problems the
author hit were their own.

**Do**
1. Build a 3D game in Godot as a multi-year project (author: "I've been
   working on this game for years" and it is "by far my biggest project").
2. Treat scaling problems as author-caused until proven otherwise (author,
   verbatim from the scan snippet: "the only 'scaling' problems I've had
   were caused by myself, and myself only").
3. Ship a grapple mechanic: the most-praised moment in the comments is the
   grapple ("That grapple scratched an itch in my brain i didnt think i
   had" - Sea_Day_7567, score 1).

**Check**
- The counter-read from commenters: the "Godot can't do 3D" claim is really
  about AAA/high-fidelity scale, not whether 3D works (Boom_Fish_Blocky,
  score 1: "what people mean by 'cant do 3D' is that godot cant handle
  unreal or unity levels of 3D stuff as easily"; "a go to style for godot
  3D games to have retro, cartoony or low poly graphics").
- The map/grid question from AssistWorth5353 ("how you made the map when
  i do it blocks seem to go in location that do not match the grid") went
  unanswered in the retrieved comments: no grid-placement method is
  recoverable from this thread.
- Commenter Apprehensive-Fun3969 calls the game "2.5d", which the author
  did not answer in the retrieved comments: the 3D-vs-2.5D framing is
  unresolved in-thread (inference: the clip reads as a fast-paced 3D
  action game; the "2.5d" label is one commenter's read, not the author's).

**Why**
The thread's real content is not a workflow but a scoping debate: Godot 3D
is proven at indie scale by a multi-year project, and the ceiling debate is
about AAA fidelity (shadows, pipeline, effects, streaming), not about
whether 3D works at all. The author's principle (scaling problems were
mine, not the engine's) is the checkable version of that claim.

### The human method, distilled
1. "Scaling problems were mine" (author, quoted): when perf/scale bites,
   audit your own code first; the engine is the suspect of last resort.
2. From the comment thread: name the actual ceiling. The productive
   Godot-3D discussion is a feature inventory (see below), not a verdict.

### Commenter evidence: the Godot engine-ceiling inventory (James20k, score 8)

A commenter posted an 11-point list of what Godot's renderer/pipeline is
missing. Items 1-10 are quoted verbatim from the retrieved comment; item
11 was truncated by the fetch tool's 800-char body cap ("The abil..."),
so it is recorded as truncated, not guessed:

1. "Better shadows, Godot's are not good quality. Contact shadows help a lot though!"
2. "A programmable pipeline"
3. "Effects that work with MSAA enabled, eg subsurface scattering"
4. "Compositor effects that work better than the current ones, which appear to be very limited/broken a lot of the time"
5. "A better solution for transparency. It really does not work well in Godot at all"
6. "Screenspace reflections that work on transparent/depth reading materials, like water"
7. "The ability to write transparent objects to the normal-roughness buffer for mostly-opaque objects (water)"
8. "Better frame pacing, because godot's frame pacing is pretty mid"
9. "Reduced input latency, Godot has a frame too many"
10. "Multithreaded rendering that's better supported than the separate thread rendering mode"
11. Truncated in retrieval ("The abil..."); content unknown.

Related commenter threads (questions and anecdotes, not author-verified):
- leetNightshade (score 1): "Does Godot do animation streaming yet? Does it
  have mesh streaming? Does it have LOD streaming and mesh chunking for
  world streaming? Does it have audio streaming?" plus a link to Godot's
  "what's missing in Godot for AAA" article (link not verified this run).
- alpinedude (score 1, own project, NOT the author's): "Jolt is much better
  but still not there... Jolt was +2.5ms on physics compared to Unity which
  was 0.2ms in total, so ~10x less, same calculations... just casting rays
  was slower, jolt queries were slower... drive over a box and either of
  you is suddenly launched, even on high physics rate." Treat as one
  developer's anecdote, not a measured Jolt verdict; the author also
  muses the slowdown may have been GDScript ("this physics part I should
  have ported to an extension").
- carriesloane (score 4): links a visual-scripting gap analysis
  (carriesloane.com/godotproposals) - "visual scripting for Godot... is
  missing a bunch of features". Not verified this run; recorded as a
  commenter link, not an audit finding.

**Depth status:** DEPTH-LIMITED (showcase clip + engine-ceiling discussion;
no workflow, no Godot version, no perf numbers from the author, no
grid-placement method; commenter anecdotes are labeled as such). No
skill: a wishlist and a debate are not an executable workflow.

### 2. "i guess they're just excited to race." (Dangerous-Town2195) - NO-TOOLING

Source: https://v.redd.it/1v5rctbajgvh1 | r/godot post 1x5vfxy (score 45,
3 comments). Selftext snippet: "raycast wheel woes".

A racing-game joke clip (cars piling up / bouncing at a start line, per
the title). The 3 retrieved comments are GIF reactions, a pun ("roll
with it... just bounce"), and a "why's this dealer" joke. "Raycast
wheels" is named only in the two-word selftext aside; no implementation,
no parameters, no workflow. Marked NO-TOOLING.

### 3. "Learning motion design and having some fun with geonodes flower setup" (Specialist-Peach-789)

Source: https://v.redd.it/35koxs8fqgvh1 | r/blender post 1x5whnb (score 20,
4 comments).

Tools used: Blender Geometry Nodes (flower setup, motion design).

This audit reconstructs what the thread evidences: a finished GeoNodes
flower animation presented as a learning exercise. No node graph, no
parameter, and no render setting is published in the post or comments.

**Do**
1. Build a flower setup in Blender Geometry Nodes as a motion-design
   exercise (author: "Learning motion design and having some fun with
   geonodes flower setup").

**Check**
- The three substantive commenter questions all went unanswered in the
  retrieved comments (the author replied only with thanks):
  - the_grandmaster901: "Can I ask how you did the caustic lights?"
  - khushnud3D: "What rendering setup do you use?"
  - -_--__---___----____: "Couldn't figure out if I should use bones or
    bend meshes with a shrinkwrap modifier. Haven't really done either
    in geonodes. If you have tips, I'd be so grateful"
- The praise confirms the result reads well ("Holy crap that's beautiful",
  "Learning.. brotha you can teach"), but praise is not a workflow.
- Weaselot_III's reaction ("geo nodes is such a mountain to climb") is
  the only learning-curve signal in the thread.

**Why**
A showcase with unanswered how-questions is evidence that the result is
attainable, not evidence of how to attain it. The bones-vs-shrinkwrap
question is the one genuine technique fork in the thread, and it stays
open because the author never answered.

### The human method, distilled
1. (No author method recoverable.) The thread's only transferable lesson
   is negative: a GeoNodes result posted without its node graph teaches
   nothing reproducible, however good it looks.

**Depth status:** DEPTH-LIMITED (tools named; zero parameters, node names,
or render settings; all how-questions unanswered). No skill: nothing
executable to stage.

## Have-vs-need

### Aegis (primary)

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|------------|------------------|--------|---------------|----------------|
| Godot 3D at scale + engine-ceiling inventory (shadows, programmable pipeline, MSAA effects, compositor, transparency, SSR, frame pacing, input latency, multithreaded rendering) | Audit 1 (r/godot) | NEED | Inventory: UE packaging stage exists (`ue/`); no Godot stage; UE5 client lives in separate repo `Emperiusm/Aetheria` | watchlist: the ceiling inventory is reference for any Godot-side evaluation; nothing adoptable for the UE foundry |
| Jolt physics perf anecdote (+2.5ms vs Unity 0.2ms, slow ray queries) | Audit 1 comments (commenter's own project) | NEED | Inventory: deterministic Rust zone sim, Q16.16 fixed-point; no Jolt anywhere | skip: Aegis sim is custom Rust, not Jolt; one anecdote about another dev's project |
| Blender GeoNodes flower motion-design setup | Audit 3 (r/blender) | NEED | Inventory: no GeoNodes / motion-design stage in foundry | skip: cinematics-adjacent motion design; no foundry attach point, and no workflow detail to adopt anyway |
| Raycast wheels | Audit 2 (selftext aside) | NEED | Inventory: no vehicle/wheel stage | skip: NO-TOOLING clip |

### 2d3d

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|------------|------------------|--------|---------------|----------------|
| Godot 3D at scale + engine-ceiling inventory | Audit 1 | PARTIAL | Inventory: Godot 4.7.2 Mobile renderer, Jolt physics, 286 gdUnit4 cases; NEED: asset import validation gate (P1, rec 9), production-conversion stage (P1, rec 20) | watchlist: the ceiling list is a scoping checklist for the 2D-to-3D camera work (shadows, transparency, SSR, frame pacing, input latency); the author's "scaling problems were mine" is supporting evidence that 2d3d-scale Godot 3D is tractable. NOT a fill for the P1 import-validation gap |
| Jolt physics perf anecdote | Audit 1 comments | PARTIAL | Inventory: Jolt physics is HAVE in 2d3d | watch: commenter reports +2.5ms vs Unity 0.2ms + slow ray queries in their own project, with a GDScript-vs-extension confound admitted. 2d3d should measure its own physics cost rather than trust the anecdote; no action until measured |
| GeoNodes flower setup | Audit 3 | NEED | Inventory: procedural texture/audio generators, projection painting | skip: 2d3d art is reference-reconstruction, not GeoNodes motion design |
| Raycast wheels | Audit 2 | NEED | Inventory: no vehicle stage | skip: NO-TOOLING clip |

### Desktop City

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|------------|------------------|--------|---------------|----------------|
| Godot 3D at scale + engine-ceiling inventory | Audit 1 | PARTIAL | Inventory: Godot 4.7.2, procedural authoring, headless Blender sprite path; NEED: shader-driven skyline fill (P1) | watchlist: ceiling list relevant only if a real-time 3D view ever appears; current pipeline is fixed-view sprites, so SSR/transparency/MSAA items are out of scope today |
| Jolt physics anecdote | Audit 1 comments | NEED | Inventory: no physics-sim stage (fixed-view sprites) | skip |
| GeoNodes flower setup | Audit 3 | NEED | Inventory: procedural authoring tools, headless Blender render | watch: Blender-side procedural pattern; sprite pipeline already covers procedural authoring |
| Raycast wheels | Audit 2 | NEED | Inventory: no vehicle stage | skip |

### Solarempire

| Tool/stage | Found in (video) | Status | Repo evidence | Recommendation |
|------------|------------------|--------|---------------|----------------|
| Godot 3D at scale + engine-ceiling inventory + streaming questions (mesh/LOD/audio streaming, mesh chunking) | Audit 1 | PARTIAL | Inventory: Godot 4.7.x native client direction (ADR 0016), oracle budgets; NEED: Godot import validation gate, re-measured export budgets (ADR 0003) | watchlist: the streaming questions bear directly on the oracle-budget re-measurement (ADR 0003); the author's multi-year Godot 3D experience is supporting evidence, not a fill |
| Jolt physics anecdote | Audit 1 comments | NEED | Inventory: no Jolt; spacecraft pipeline | skip |
| GeoNodes flower setup | Audit 3 | NEED | Inventory: Blender stages throughout | skip: concept-to-GLB pipeline, not GeoNodes motion design |
| Raycast wheels | Audit 2 | NEED | Inventory: no vehicle stage | skip |

## Gap recommendations (highest-leverage NEEDs)

Thin run: both audited videos are DEPTH-LIMITED with no extractable
workflows, so recommendations are pattern-level, not adoptions.

1. **2d3d / Solarempire / Desktop City: keep the Godot engine-ceiling
   inventory as the scoping checklist for Godot 3D work.** The James20k
   list (shadows, programmable pipeline, MSAA-safe effects, compositor,
   transparency, SSR on transparent/depth materials, normal-roughness
   buffer writes, frame pacing, input latency, multithreaded rendering)
   plus the streaming questions (mesh/LOD/audio streaming, mesh chunking)
   is the most concrete "what Godot 3D costs" inventory the scout has
   surfaced. Concrete next step: when Solarempire re-measures export
   budgets against a real Godot importer (ADR 0003), check the streaming
   and transparency items against the measured importer behavior instead
   of the oracle reasoning.
2. **2d3d: measure Jolt physics cost rather than trusting the anecdote.**
   The +2.5ms-vs-0.2ms claim comes with an admitted GDScript confound
   from a commenter describing their own project. Next step: none until
   2d3d's own physics cost is profiled; the anecdote is a prompt to
   measure, not a verdict.
3. **No new P1 filed.** Nothing today met the bar of "verified absent in
   the repo + fills a described need". The Godot thread is a debate, the
   GeoNodes post is a showcase with unanswered how-questions, and the
   racing clip is a joke.

## Non-goals (found but correctly skipped)

- #2 racing clip: joke clip with GIF comments; "raycast wheel woes" is a
  two-word aside. NO-TOOLING.
- GeoNodes flower setup: finished result, no node graph, no parameters,
  all how-questions unanswered. DEPTH-LIMITED, report-only.
- Jolt anecdote: commenter's own project, GDScript confound admitted;
  not scored as a gap fill or a verdict.
- carriesloane's visual-scripting proposal link: commenter link, not
  verified this run; recorded in audit 1, not adopted.
- Godot version numbers: none disclosed in any post; no version rows.

## Watchlist trending

No genuine reappearances. The automated matcher flagged the Raup shell
morphospace row (2026-10-04) as seen-again on token overlap ("Blender geo
nodes") with today's GeoNodes flower post; this is NOT a genuine
reappearance (parametric shell morphospace vs a flower motion-design
setup: different tool, different workflow) and the annotation was
reverted with a note. Manual review kept this run, same as the 2026-10-13
and 2026-10-14 token-overlap corrections. Godot rows on the watchlist
(Ultrapolis procgen city, Godot 4.5 .NET creature pipeline) share the
"Godot" token with today's thread but are distinct tools; not
reappearances.

New watchlist rows (appended 2026-10-15): Godot 3D engine-ceiling
inventory (James20k wishlist + streaming questions + Jolt anecdote);
Blender Geometry Nodes flower motion-design setup (DEPTH-LIMITED).

## skill_library staging

Staged in `~/workspace/video-tooling-scout-public/` (browser upload happens
when Ehsan is present; never unattended):

- No new or expanded skills this run: both audits are DEPTH-LIMITED with
  no extractable workflow, and one clip is NO-TOOLING (standing rule:
  never pad thin evidence into `skills/`).
- Report copy: `docs/scout-reports/have-vs-need-2026-10-15.md`.
- Watchlist sync: new 2026-10-15 rows + the reverted false-match note
  copied into the mirror's
  `video-tooling-scout/references/tooling-watchlist.md`.
- README: `docs/scout-reports/README.md` index row added.

Dedup check: no existing skill covers the Godot engine-ceiling debate or
the GeoNodes flower setup, and neither audit clears the depth bar for a
new skill (no executable workflow to stage).

## Run log

- 08:18 cron fired; skill re-read at run start per AGENTS.md.
- Scan attempt 1: success, 3 video posts (Arctic Shift primary OK;
  gameassets 429'd once, transient).
- Scan verification re-run: identical 3 posts (photogrammetry 429'd once,
  transient); scan JSON saved to
  `hidden_files/scan-2026-10-15.json`.
- Comments fetched for all 3 posts via bin/fetch_comments.py (Arctic
  Shift, first pass, no failures).
- PullPush full-selftext attempt: 429'd once; not retried.
- Depth: 0 attempted / 0 succeeded / 0 skipped. All native Reddit clips;
  no YouTube/Vimeo targets; no approval gate fired at any point.
- 3/8 deep-analysis slots used: 2 DEPTH-LIMITED, 1 NO-TOOLING.
- trend_watchlist.py run with 5 tool names; 1 false token-overlap match
  (Raup shells) reverted with a note; no genuine reappearances.
- 2 new watchlist rows appended (2026-10-15).
- Report written to hidden_files/have-vs-need-2026-10-15.md.
- 0 new skills + report + watchlist sync + README row staged in
  ~/workspace/video-tooling-scout-public/ for Ehsan's upload session.
