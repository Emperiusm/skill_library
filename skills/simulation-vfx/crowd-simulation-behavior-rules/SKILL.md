---
name: crowd-simulation-behavior-rules
description: "Move crowds through town streets with six local rules and no physics colliders: keep right, match a slower leader, overtake under 80 percent, step back right, side-step after 0.4 seconds stuck, walk through after 1.5 seconds, plus spatial-hash neighbor queries and Dixon-style simplification tiers for scale. Rebuilt from memoryfloater's schematic crowd-sim reels and Dixon's horde recipe as a Godot 4 plain-data sim with AStar2D pathing. Trigger when crowds of NPCs or citizens must flow, queue, and never deadlock on authored streets."
---

# Crowd simulation behavior rules: lanes, overtaking, and stuck escape without colliders

## Purpose

This skill reconstructs a crowd movement system from two schematic, engine-free sources, step by step, so another agent can follow the same workflow. Every phase has three parts: **Do** (the action), **Check** (how the human verifies it), and **Why** (the principle). The core method is: put walkers on a lane grid, give each one two scan boxes and a stuck timer, and let six local rules produce flow, queues, overtaking, and deadlock escape, with no physics colliders and no steering library. Scale comes from a second source's simplification tiers: position-only agents, nearby-only separation, lazily generated ground points, and shared baked animation parents.

## Source

Creator: memoryfloater (solo dev, engine unnamed in the reels). Three narrated schematic reels, top-down 2D squares on a dark grid, local faster-whisper tiny transcriptions, 12 frames read firsthand each:

- P1: https://www.instagram.com/reel/DfzMGodICCx/ (posted Nov 16, 2026, 67 likes, 0 comments). World model plus rules 1 and 2.
- P2: https://www.instagram.com/reel/Df1uI3eIsnY/ (posted Nov 17, 2026, 202 likes, 6 comments, all 6 read). Rules 3 and 4.
- P3: https://www.instagram.com/reel/Df4UKaZIS-3/ (posted Nov 18, 2026, 37 likes, 9 comments, all 9 read, all spam). Rules 5 and 6.

Second source, creator: callme_dixon (Dixon, Unreal, Heroika). One narrated montage reel, local transcription, 12 frames read firsthand, 43 of 44 comments read:

- Horde recipe: https://www.instagram.com/reel/DfjNMnVTHKO/ (posted Nov 9, 2026, 2,592 likes). Dot-only actors, lazy ground points, nearby-only separation, 8 shared baked animation parents, climb-onto-ahead.

## Claims ledger: what is verified, what is not

Read this before citing anything from the reels. The behavior rules are fully specified at the rules level and are the substance of this skill. The scale and performance figures are not evidence.

- **Unverified creator claims, never cite as benchmarks:** 20,000 enemies above 60 FPS (Dixon title and narration; no frame among the 12 sampled shows the 20,000 counter, and no hardware, resolution, or settings are stated anywhere in the reel). 18,000 active characters (tenekekafalar, a different account, not a source for this skill; its caption contradicts its own embedded article, which says a 1 to 2 FPS drop on an RTX 2080). "Hundreds of walkers" (memoryfloater P3 narration; no counter is shown). 7,133,718 proximity checks (Dixon frame 005; the number is unlabelled on frame and its meaning is inferred from the surrounding narration). 0 vs 12 arrivals (P2 throughput comparison; no time window or walker count stated, qualitative demo only).
- **Caption promises the reels do not deliver:** P2's caption asks whether walkers should become angry. No anger state, patience system, or stuck-timer use appears in P2's narration or frames; anger appears only as viewer comments. Do not describe P2 as adding walker anger. P3's caption promises wall collision without physics colliders. No wall, building, or collider mechanism is explained in P3; the reel is entirely about stuck-escape rules, and the grey bars in its frames are unlabelled. Do not describe P3 as delivering a wall-collision system. In this skill, walls are handled by the grid itself (Phase 1): no path exists through a building because no walkable cell exists there.
- **Ambiguities resolved by this skill, labeled as derivations:** whether the 80 percent compares the leader's speed to the follower's fixed cruise speed or its current speed (this skill defines it against the fixed cruise speed, Phase 4). What rule 6's "ignore everything" suspends (this skill defines it, Phase 5). What the grey blockers in P3 are (unknown; this skill treats any blocked lane as a blockage and does not name the blocker).
- **Comment quotes verified in raw JSON before use here:** the 80 percent rationale (creator reply in the P2 comments; the fetch leaves the reply's author_name blank, but the author_id matches the account owner's replies across the page) and the two Dixon quotes in Phase 7 (author "Dixon" in the JSON). No other comment text is quoted as evidence in this skill.

## The six rules and the world model (from the reels, attributed)

World model (P1):

1. The world is a grid of streets. Every street cell is split into 4 by 4 smaller cells, giving every street four lanes. Each walker keeps to one lane at a time; lane changes are smooth lateral moves that hide the four-lane quantisation and the underlying grid.
2. Each walker has its own fixed speed. Example values shown on screen: 0.75, 1.25, 1.37, 2.0. Units are never stated.
3. Each walker has two scan boxes: a narrow one checking its own lane ahead for anyone in the way, and a larger one checking a wider area ahead across all lanes for oncoming traffic.
4. Pathing is cell to cell across the grid; the walker then follows the lanes of the cells on its path.
5. Movement costs: roads are cheaper than grass, so a walker takes the longer route on roads rather than cutting across grass.
6. Each walker keeps a stuck timer: how long it has been blocked (example shown: 0.2 s). In P1 the timer is introduced but unused; P3 finally consumes it.

Rules (P1 to P3, closing summary card of P3, transcribed verbatim):

1. Keep right. If that lane is taken, take the next free one.
2. Slower walker ahead: match its speed.
3. Leader under 80% and nobody coming: pass on a free lane.
4. Back up to speed: step back right.
5. Stuck 0.4 s: side step.
6. Stuck 1.5 s: walk through for 1.5 s.

Dixon simplification tiers (from the horde reel, attributed):

1. Strip actors to dots: position-only agents, no skeletal actors, no per-agent animation or physics cost in the sim.
2. Lazy ground points: do not bake the whole map's heights; agents generate ground points only where they actually walk.
3. Nearby-only separation: each agent scans only close neighbors and ignores the rest, cutting the check count from all-pairs to local.
4. Shared baked parents: one walk animation baked once, played on 8 parent skeletons at different phase intervals, with the animation passed down to all other actors; scrambled phases hide the sharing.
5. Climb onto the agent ahead when blocked, so back ranks can still reach the target.

## Tools used

Godot 4.x (this skill's construction is GDScript-first, with C# naming notes where they differ; Valkyrie is C#, so the sim data lives in plain C# types with no engine calls, and the Godot side only renders positions). AStar2D for cell-to-cell pathing on the plan grid. PhysicsDirectSpaceState3D intersect_ray only for the lazy ground-point cache. No physics bodies, no NavigationAgent avoidance, and no steering library are required for the six rules; the NavigationAgent RVO option is documented in Phase 8 as the alternative for near-camera hero citizens, not the default.

## Phase 1: Build the world model, grid, lanes, and costs

**Do**
1. Author the walkable street network as a grid over the plan (XZ) plane. Each street cell holds 4 lanes. A lane is an offset line parallel to the street direction, not a separate cell: lane index 0 is the rightmost lane in the direction of travel, lane 3 the leftmost. This matches the reel's 4 by 4 split while keeping one pathing graph: the path is cell to cell, and the lane is a lateral offset applied at walk time.
2. Give every cell a movement cost. Roads cost less than grass (P1's rule: walkers take the longer road route rather than cutting across grass). Encode cost as AStar2D point weight_scale: add one point per walkable cell center with `add_point(id, position, weight_scale)`, connect each cell to its walkable neighbors with `connect_points`, and override `_compute_cost` so terrain cost multiplies through weight_scale. Map world XZ to Vector2(X, Z) for the 2D graph; keep Y out of pathing entirely.
3. Mark non-walkable cells (buildings, walls, water, off-map) by simply not adding points for them. There is no wall-collision system in this skill because there is no wall to collide with: a walker cannot path into a building, since no graph edge leads there. This is the honest form of P3's caption promise, and it is a grid property, not a collider.
4. Define the two scan boxes as cell-range queries, not physics shapes. The narrow scan (own lane ahead) queries the cells ahead in the walker's current lane out to a look distance. The wide scan (all lanes ahead) queries the cells ahead across all lanes out to a longer look distance. Both queries run against the spatial hash (Phase 6), never against physics bodies.
5. Declare the tuning constants in one manifest (see Agent automation): lane count 4, look distances for both scans, road cost, grass cost, and the fixed cruise speed distribution. The reel's example speeds (0.75 to 2.0, units unstated) become this skill's starting defaults in meters per second, labeled as such: slow 0.75, typical 1.25, fast 2.0. Cruise speed is fixed per walker at spawn and never changes except by rule 2 matching.

**Check**
- A walker paths from one end of a street to the other staying on road cells even when a grass shortcut is geometrically shorter. If it cuts the grass, the cost ratio is too small; raise grass weight_scale until the road route wins.
- A walker placed on a street with buildings on both sides never enters a building cell at any point in its path. If it does, a non-walkable cell leaked into the graph; the graph build, not the walker, is wrong.
- The narrow scan returns the walker ahead in the same lane and nobody else; the wide scan returns oncoming walkers in every lane. Test both with two walkers placed by hand before running any crowd.

**Why**
- The grid is the contract between the authored map and the sim: one graph, one cost table, no per-walker steering state. Everything the six rules need (lane, ahead, oncoming, blocked) is a query over cells the walker already occupies or is about to occupy.
- Keeping Y out of pathing is what makes the sim plain data. Ground height is a render-time lookup (Phase 7), not a sim dimension.

## Phase 2: Give each walker fixed state, including the stuck timer

**Do**
1. Store walker state in plain arrays (structure of arrays), not one node per walker: position (XZ), lane index, cruise speed, current speed, path cell list plus path index, stuck timer, ghost flag with expiry, and a phase offset for animation sharing (Phase 7). In C#, these are struct fields in arrays; in GDScript, parallel arrays or a lightweight RefCounted per walker for small crowds only.
2. Update on a fixed step (the sim tick), independent of render rate. Each tick, in order: advance the stuck timer (Phase 5), evaluate rules 1 to 4 (Phases 3 and 4), integrate position along the current lane at current speed, then update the spatial hash (Phase 6) with the new positions. Rules read the hash state from the previous tick so every walker sees the same world within a tick; this keeps the sim deterministic for a fixed seed.
3. Define the stuck timer precisely, because P3 never does: the timer accumulates only while the walker is blocked, meaning its forward progress this tick is below a small epsilon (this skill's default: less than 0.05 m in one tick) AND its narrow scan reports a blocker ahead. It resets to zero the first tick the walker moves freely. A walker waiting at its destination does not accumulate; arriving is not being stuck.

**Check**
- Two walkers, one stopped ahead of the other: the follower's timer climbs while it is blocked and resets the tick it moves again. If the timer climbs while the walker moves freely, the reset condition is wrong.
- Run the same seed twice and hash all walker positions after 600 ticks: identical. If the hash differs, some rule is reading hash state written in the same tick (see the ordering rule above).

**Why**
- The stuck timer is the only memory in the whole system. Rules 5 and 6 are just thresholds on it, which is why the P1 to P3 set stays cheap: no history, no planning, one float per walker.
- Deterministic tick order is what makes the sim testable and replayable, which matters more than raw speed for a god game whose citizens persist between sessions.

## Phase 3: Rules 1 and 2, keep right and match a slower leader

**Do**
1. Rule 1, keep right: when a walker spawns or enters a new street cell, assign the rightmost free lane (lane 0 if free, else the next free lane). "Free" means the spatial hash reports no walker in that lane within one body length ahead or behind in this cell. Re-evaluate only on cell entry, not every tick; constant re-evaluation makes walkers jitter between lanes.
2. Rule 2, match a slower leader: each tick, read the narrow scan. If a walker ahead in the same lane is moving slower than this walker's cruise speed, set current speed to the leader's current speed. Do not stop, do not swerve; following is the default. This is what creates queues: a line of walkers all at the leader's speed, exactly as P1 demonstrates (five walkers all at 0.75).
3. Lane changes are smooth lateral moves: when a rule assigns a new lane, interpolate the lateral offset over a fixed lane-change time (this skill's default: 0.35 s, labeled as a derivation; the reel shows smooth changes but gives no duration). Forward speed is unchanged during the change. The walker never teleports sideways, which is what hides the four-lane quantisation from the viewer.
4. Keep-right return is rule 4, not rule 1: rule 1 assigns lanes on entry; rule 4 (Phase 4) returns an overtaker to the right after passing. Do not run a continuous "drift right" behavior; it fights rule 2 queues and makes lanes churn.

**Check**
- Two-way street, walkers spawning from both ends: after a few seconds, each direction occupies its own lanes with no head-on meetings. If head-on meetings persist, lane assignment is not respecting travel direction (lane 0 must be rightmost relative to the walker's heading, not a fixed map side).
- A fast walker behind a slow one in the same lane settles at the slow speed and holds a steady gap. If it oscillates (speed up, brake, speed up), the match is reading the leader's cruise speed instead of its current speed, or the gap check is missing; match current speed, and only match when the gap is under one body length plus the narrow scan distance.

**Why**
- Keep right plus speed matching is the whole congestion model: opposite flows separate by default, and queues form without any explicit queue data structure. The reel's claim holds here: with just these two rules, a street already flows.
- The smooth lane change is a rendering honesty device. The sim is discrete (lanes, cells); the eye must never see the discreteness.

## Phase 4: Rules 3 and 4, overtake under 80 percent and step back right

**Do**
1. Rule 3, overtake: each tick, if the narrow scan reports a leader ahead and the leader's current speed is below 80 percent of this walker's fixed cruise speed, the walker may overtake. Compare against the fixed cruise speed, not the current speed: this is this skill's disambiguation of the reel's ambiguous wording ("below 80% of its speed"), chosen because cruise speed is stable and current speed would make the threshold move as the walker slows. If the leader is at 80 percent or above (the reel's example: 90 percent follows, 70 percent passes), keep following under rule 2.
2. Before overtaking, check the wide scan: if anyone is coming in the target lane within the wide look distance, wait. If all lanes are taken, wait for a gap. Do not start a pass into occupied space; the pass begins only when the target lane is free for the full look distance.
3. Execute the pass as a lane change into the free lane (same smooth lateral move as Phase 3), at cruise speed, then continue past the leader. While passing, the walker ignores rule 2 for the leader it is passing (it is no longer behind that leader in the same lane) but still obeys rule 2 for anyone ahead in its new lane.
4. Rule 4, step back right: once the walker is back up to cruise speed and its rear has cleared the passed walker (passed walker's position is behind this walker's rear by one body length), step back into the rightmost free lane if one is available. This restores the keep-right invariant and gets the overtaker out of oncoming traffic quickly, which is the reel's stated purpose for the rule.
5. Add hysteresis, a derivation the reel does not mention: require the under-80-percent condition to hold for 3 consecutive ticks before starting a pass. Without it, a leader whose speed wobbles around the threshold makes the follower start and abort passes every few ticks.

**Check**
- The reel's own test cases, reproduced: leader at 50 percent of follower speed passes; leader at 70 percent passes; leader at 90 percent follows. All three must reproduce in the sim. If the 90 percent case passes, the comparison is against the wrong speed.
- A pass never starts into an occupied lane, and a pass never ends with the overtaker lingering in the oncoming lane: after every pass, the walker is back in the rightmost free lane within 2 seconds of clearing the leader. If it lingers, rule 4's clearance test is too strict.
- The creator's rationale, verified in the P2 comments: "Imagine you're driving a car and the car in front of you is just a bit slower than your target speed. That's where you decide to just lower your speed and stay behind it instead of overtaking. So yes it could overtake but it won't because it's 'not worth the trouble'." The threshold is a worth-it dial, not a physical limit. Expose it as one tunable (default 0.8) and prove the dial works: sweeping 0.7, 0.8, 0.9 must change measured congestion (queue length and arrivals) monotonically in the Phase 8 test street.

**Why**
- One ratio plus two checks the model already provides (wide scan, free lane) is the entire overtake decision. The cost per walker stays local, and the congestion dial is a single number a designer can tune for crowd mood: lower threshold, more queues; higher threshold, more lane-changing churn.
- The return-right rule is what keeps the system safe: without it, overtakers accumulate in oncoming lanes and the keep-right invariant, which is doing all the collision avoidance, silently dies.

## Phase 5: Rules 5 and 6, stuck escape, side step and walk-through

**Do**
1. Rule 5, side step: when the stuck timer (Phase 2) reaches 0.4 s, the walker steps into a free lane. "Free" uses the same test as rule 1, extended by the wide scan: the target lane must have no walker within one body length ahead or behind, and no oncoming walker within the wide look distance. If no lane qualifies, keep waiting; the timer keeps climbing toward rule 6. Reset the timer to zero on a completed side step.
2. Rule 6, walk through: when the stuck timer reaches 1.5 s with every lane blocked, set the ghost flag for 1.5 s. While ghosted, the walker ignores separation and lane rules, moves along its path at cruise speed, and passes through blockers. This skill defines "ignore everything" as: narrow and wide scans return empty, rule 2 does not apply, and other walkers' scans ignore the ghosted walker too, so the jam can actually clear instead of re-forming around it.
3. After the 1.5 s ghost expires, clear the flag, reset the timer, and impose a cooldown (this skill's default: 3.0 s, labeled as a derivation) before rule 6 can trigger again for the same walker. Without the cooldown, a walker can ghost repeatedly through the same jam and spend its whole journey clipping.
4. Scope rule 6 to background crowds only. At iso distance in a crowd, brief overlaps at jam points are barely visible, which is the reel's schematic context. Never apply ghosting to a hero citizen, a citizen the camera is close to, or a citizen carrying something the player is watching. For those, replace rule 6 with a wait-and-reroute behavior: after 1.5 s stuck, replan the path around the blocked cells (AStar2D again, with the blocked cells temporarily disabled) instead of walking through. The sim keeps both escape modes; the assignment of which citizens may ghost is authored data, not a runtime decision.
5. The 0.4 s and 1.5 s values are the reel's only tuned constants besides the 80 percent threshold. They are starting defaults, not measured optima: too short and side-stepping and ghosting become constant; too long and jams sit visibly. Retune against real crowd densities in the Phase 8 test street, and record the tuned values in the manifest with their provenance.

**Check**
- The P3 control demo, reproduced: two crowds meeting head-on with rules 5 and 6 switched off must lock up into a solid jam. With the rules on, the same scene must clear with zero walkers stuck longer than 5 s. If the control scene does not jam, the test street is too easy and proves nothing.
- A ghosted walker overlaps others for at most 1.5 s, then resumes normal rules, and never re-ghosts within the cooldown. If overlaps persist past expiry, the flag is not clearing.
- No hero citizen ever ghosts in a 10-minute soak run. If one does, the scoping data, not the rule, is wrong.

**Why**
- Two timer thresholds are the cheapest possible deadlock guarantee: the sim never resolves a collision, it just escalates. That is the honest trade of the whole reel set: robustness bought with brief, visible clipping, scoped to where the camera cannot judge it.
- The control demo is the proof format to copy: a system that claims to prevent lock-ups must be shown locking up with the fix off. A deadlock fix demonstrated only in scenes that never deadlock is unproven.

## Phase 6: Neighbor queries on a spatial hash, never all-pairs

**Do**
1. Maintain a flat spatial hash rebuilt every sim tick: a dictionary keyed by cell coordinate (Vector2i), each cell holding the list of walker indices currently in it. Cell side equals the separation radius (this skill's default: 1.0 m, one body length plus margin; label as a derivation, since the reels give no scan-box dimensions). Rebuilding every tick is O(n) and keeps the hash trivially consistent with the tick-ordered update in Phase 2.
2. Answer every scan as a hash query: the narrow scan reads the cells ahead in the walker's lane out to the look distance; the wide scan reads the cells ahead across all lanes; separation (Dixon's nearby-only check) reads the walker's own cell plus its 8 neighbors. A query touches only nearby candidates, never the whole crowd. This is the spatial partition pattern: store objects by position so a query for "who is near me" costs the neighborhood, not the crowd.
3. Use the hash for all three query kinds (narrow scan, wide scan, separation). Do not mix query mechanisms: no physics Area queries, no per-walker RayCast nodes, no NavigationAgent avoidance in the sim loop. Physics queries belong to the ground-point cache (Phase 7) and to hero citizens (Phase 8), not to crowd neighbor-finding.
4. Keep the hash in the sim's plain data, not in the scene tree. The hash is rebuilt from walker positions each tick; it holds indices, not nodes, so it costs nothing when a walker despawns and never goes stale across a save/load boundary if rebuilt from positions on load.

**Check**
- Equivalence gate: on a 200-walker test scene, the hash neighbor set for every walker must exactly equal the brute-force all-pairs neighbor set within the separation radius. If any neighbor is missed, the cell side is smaller than the radius, or a walker straddling a cell edge is not being found in the neighboring cells.
- Cost check: doubling walkers from 200 to 400 must roughly double the neighbor-query time, not quadruple it. Quadratic scaling means some query is still scanning the whole crowd.

**Why**
- All-pairs separation is O(n squared) and is exactly the cost Dixon's reel shows exploding (7,133,718 checks, creator's unlabelled on-screen figure, never verified). The hash is what makes "nearby only" true in implementation rather than in intent.
- A flat grid is the right partition here because the world is already a grid: the hash cells align with the lane grid, so a scan box is just a cell range, and no tree maintenance is ever needed.

## Phase 7: Simplification tiers for scale, Dixon's recipe as sim discipline

**Do**
1. Tier 1, dots: the sim stores position only per agent. No skeletal actors, no per-agent animation state, no per-agent physics bodies in the sim. Animation is a render-layer concern handed to the VAT/BAT skills (cross-links below); the sim's only contract with rendering is positions plus a phase offset per walker.
2. Tier 2, lazy ground points: do not bake the whole map's heights. Keep a ground-height cache keyed by street cell, filled on first visit: when a walker first enters a cell with no cached height, cast one ray down through PhysicsDirectSpaceState3D intersect_ray (PhysicsRayQueryParameters3D from above the terrain to below it, in _physics_process, collision mask set to terrain only) and store the returned position's Y. Every later walker in that cell reads the cache and casts nothing. Cap the cache: cells are fixed and finite, so the cache is bounded by the map, not by the crowd.
3. Tier 3, nearby-only separation: separation is the hash query from Phase 6 with a fixed radius, exactly as Dixon describes ("scan only the enemies close to them, ignore all the other ones"). In this skill, separation is already subsumed by the lane rules for street crowds; keep it as the fallback for open areas (plazas, markets) where no lanes exist: in open cells, walkers separate by a short push-apart over the hash neighborhood instead of following lanes. Do not run both lane rules and separation on the same walker in the same tick; the cell's kind (street vs open) decides which behavior governs.
4. Tier 4, shared baked parents: bake each walk cycle once and play it on a small set of parent rigs at different phase intervals, with all other walkers sampling a parent's pose. The reel's number is 8 parents; treat 8 as the creator's example, not a requirement, and tune the parent count against visible synchrony at iso distance. The mechanism (baked animation textures shared across instances) is the VAT/BAT skills' subject; this skill only specifies the sim side: each walker carries a phase offset, and walkers sharing a parent share a pose, which the reel's own comment confirms for Dixon's case: "I do have them as textures using unreal's 'Anim Bank' each animation is baked once and goblins on the same copy share one pose." Scramble phase offsets at spawn so the sharing is invisible.
5. Tier 5, climb onto the agent ahead: Dixon-only, horde context, optional. When a walker is blocked with no free lane and the stuck timer passes the rule 6 threshold, instead of ghosting it may mount: raise its Y over a short climb (this skill's default: 0.6 s up, pass over, 0.6 s down, labeled as a derivation), ignore separation while mounted, then drop back to ground level past the blocker. Use this only for swarm/horde crowds where climbing reads as terrifying, as the reel intends; for town citizens, rule 6 ghosting or rerouting (Phase 5) is the correct escape, because citizens climbing over each other breaks the painted-town read. Never implement both escapes for the same crowd kind.

**Check**
- Ground cache: after a 5-minute soak, the number of raycasts per tick is zero (every visited cell is cached) and no walker ever floats or sinks. If raycasts continue, walkers are entering uncached cells forever, which means the cell key is wrong (position quantized differently on read vs write).
- Phase scramble: 100 walkers sharing 8 parents must not read as synchronized marching at iso distance. If they do, the phase offsets are clustered; distribute them uniformly across the cycle at spawn.
- The climb tier, if enabled, never triggers for a citizen flagged as hero or near-camera. If it does, the scoping data is wrong, same failure as Phase 5.

**Why**
- Each tier removes one cost that does not belong in the sim: animation cost (dots), bake cost (lazy points), query cost (nearby only), pose cost (shared parents). The sim stays position-only, which is what lets the rule set scale without the rendering path ever entering the behavior code.
- Lazy ground points are the same idea as the lane grid applied to height: pay only for ground a walker actually stands on. On an authored island map, most cells are visited quickly, so the cache converges and the per-tick cost goes to zero.

## Phase 8: Tuning, verification, and the engine-native alternative

**Do**
1. Build the two-street test harness from the reels: street A with overtaking disabled (rules 3 and 4 off), street B identical with overtaking on, same spawn schedule, same fixed window. Count arrivals. The reel's result (0 vs 12) is qualitative only; your harness must report arrivals, mean queue length, and max stuck time over a stated window, so the 80 percent dial has numbers behind it. Sweep the threshold at 0.7, 0.8, and 0.9 and record the congestion curve in the manifest.
2. Build the head-on control from P3: two crowds meeting on one street, rules 5 and 6 switchable. Prove the lock-up appears with them off and clears with them on, as Phase 5 requires.
3. Decide the engine-native alternative explicitly, per crowd kind. Godot's NavigationAgent3D avoidance (RVO) is the built-in answer for small numbers of fully simulated agents: enable avoidance, feed the desired velocity, use the safe velocity from the velocity_computed signal. It is the right choice for hero citizens and small groups, and the wrong choice for the background crowd sim, because it needs one agent node per citizen, runs through the navigation server, and cannot express the lane rules, the stuck timer, or the ghost escape. Document the split in the manifest: sim rules for the crowd, RVO for heroes, never both on the same walker.
4. Measure at the scale you claim, or claim nothing. If the skill is ever cited with a crowd size or frame rate, the citation must name the hardware, the walker count, the tick rate, and the measurement method. The reels provide none of these, and this skill provides no scale numbers of its own: the only performance statement it makes is the complexity argument (local queries, O(n) hash rebuild) plus the harness results the reader measures themselves.

**Check**
- Threshold sweep is monotonic in the expected direction (higher threshold, more passing, shorter queues, more lane changes) or the sweep exposes a modeling bug. A non-monotonic curve is a finding, not noise: investigate before tuning further.
- Hero citizens on RVO and background citizens on sim rules coexist in one street scene without either system fighting the other: RVO heroes treat sim citizens as avoidance obstacles only through their positions, and sim citizens ignore heroes except as scan-box blockers. If heroes get stuck behind a sim queue forever, the hero needs the reroute escape from Phase 5, not a bigger push force.

**Why**
- The reels' proof format (A/B street, control demo with the fix off) is stronger than their numbers, and it is reproducible. Copy the format, not the figures.
- Naming the alternative is what keeps the skill honest about scope: RVO is a good system that solves a different problem (few agents, full avoidance). The six rules solve many agents, lane discipline, and guaranteed progress. A skill that pretends one mechanism covers both is how crowds end up either deadlocked or over budget.

## The human method, distilled

These are the decision habits the source reels demonstrate, in the creator's own framing:

1. **Rules before systems.** Six local rules, each checkable in isolation, before any solver, steering library, or physics.
2. **Schematic first.** The demos are squares on a grid, which is what makes the rules auditable: every behavior is visible, and every failure (a jam, a queue) is attributable to one rule.
3. **One dial per behavior.** The 80 percent threshold is the congestion dial; the 0.4 s and 1.5 s timers are the deadlock dials. A behavior with no dial cannot be tuned, and a behavior with five dials cannot be understood.
4. **Prove the fix with the fix off.** The lock-up control demo (rules 5 and 6 disabled) is what makes the escape rules credible. A fix shown only in scenes that never fail is unproven.
5. **The caption is not the content.** P2 promises anger it never builds; P3 promises wall collision it never explains. Read the narration and the frames, never the caption, before describing what a reel delivers.
6. **Cheap for a reason, and say the reason.** Ghosting through a jam is deliberately wrong-looking up close and deliberately right at crowd scale. The scope (background only) is part of the technique, not an afterthought.
7. **Scale by removing costs, not by adding systems.** Dots, lazy points, nearby-only checks, shared parents: each tier deletes a cost category from the sim rather than optimizing it.

## Failure modes

1. **Deadlock without rules 5 and 6.** Two crowds meet head-on, no free lane, every walker waits forever. Fix: the rules themselves (Phase 5); prove it with the control demo, and never ship the rule set with the escape tiers disabled.
2. **Ghosting visible on hero citizens.** A close-up citizen clips through another and the player sees it. Fix: scoping data (Phase 5). Ghosting and climbing are background-crowd escapes only; heroes reroute.
3. **Overtake oscillation.** A leader near the 80 percent line makes the follower start and abort passes. Fix: the 3-tick hysteresis in Phase 4, and compare against fixed cruise speed, never current speed.
4. **Lingering in the oncoming lane.** The overtaker never steps back right. Fix: rule 4's clearance test (rear clear by one body length) plus the return check every tick after a pass; log any walker still in a passing lane 2 seconds after clearing.
5. **Lane churn.** Walkers change lanes constantly without ever passing. Fix: re-evaluate lane assignment on cell entry only (Phase 3), never every tick.
6. **Missed neighbors in the hash.** A walker overlaps another it should have seen. Fix: cell side must equal or exceed the separation radius, and queries must read all 8 neighboring cells; run the equivalence gate (Phase 6) after any hash change.
7. **Stuck timer drift.** The timer climbs while the walker moves, or never climbs while blocked. Fix: the Phase 2 definition (progress below epsilon plus a reported blocker). Both conditions, not one.
8. **Ghost re-trigger loop.** A walker ghosts, expires mid-jam, and immediately ghosts again. Fix: the 3.0 s cooldown after expiry (Phase 5).
9. **Pathing through buildings.** A walker crosses a wall or water cell. Fix: the graph build (Phase 1). Non-walkable cells must have no points; never patch this with a walker-side repulsion.
10. **Intersection overlap.** Walkers overlap turning through crossings, as the reels show. Fix: none exists in the source. This skill's derivation: treat intersection cells as single-lane (one walker per intersection cell at a time, others wait at the entry), or accept brief overlap at iso distance and say so. Do not claim the reels solve intersections.
11. **Wrong speed in the 80 percent test.** Comparing against current speed makes the threshold drift as the follower slows. Fix: fixed cruise speed, stated in Phase 4.
12. **Citing reel figures as benchmarks.** The 20,000/60 FPS, 90,000/39 FPS, and "hundreds of walkers" figures enter a design doc as facts. Fix: the claims ledger at the top of this skill and the agent automation gate below. Any scale claim needs hardware, count, tick rate, and method, or it stays out.
13. **Anger system assumed present.** A reader builds a patience/anger state because P2's caption asks about anger. Fix: P2 builds no anger system. The stuck timer is the natural input if anger is ever wanted, but that connection is this skill's suggestion, not the creator's work, and it is not built here.
14. **Climb tier on town citizens.** Citizens mount each other on a market street. Fix: the climb tier is horde-only (Phase 7). Town citizens use ghosting or rerouting.

## AAA studio practice

- **Reynolds, "Flocks, Herds, and Schools: A Distributed Behavioral Model" (SIGGRAPH 1987).** The founding result: three local steering rules (separation: avoid crowding local flockmates; alignment: steer toward the average heading of local flockmates; cohesion: steer toward the average position of local flockmates) produce coherent group motion with no leader and no global plan. The six rules in this skill are a street-bound specialization of the same idea: separation becomes lane discipline plus scan boxes, alignment becomes speed matching, and cohesion is replaced by shared paths and goals, since town citizens go somewhere rather than flocking. The lesson to take is the method (local rules, emergent flow), not the three rules verbatim; pedestrians on streets are not birds.
- **Helbing and Molnar, social force model of pedestrian motion (1995 to 1998).** Pedestrians modeled as subject to a driving force toward their destination plus repulsive forces from borders and other pedestrians reproduce empirically observed self-organization, including the formation of lanes of uniform walking direction in oppositely moving crowds above a critical density. The reel's keep-right rule is an imposed, cheap version of a phenomenon Helbing's model shows emerging on its own; the practical takeaway is that lane formation reduces the frequency of avoidance maneuvers and raises flow efficiency, which is why rule 1 does so much work for so little code.
- **Assassin's Creed Unity crowd system (Ubisoft, GDC 2015, "Massive Crowd on Assassin's Creed Unity: AI Recycling").** The shipped answer to crowd scale is tiering, not one system: a pooling framework swapping low-resolution crowd members for high-resolution ones unnoticed, a simplistic AI brain for the thousands, with a stated limit of 40 real AIs and 120 high-resolution models supporting scenes of 10,000 crowd NPCs. The "bolt crowd" layer simulated in-crowd movement the way birds flock, with full AI dipping in and out of it. Take the tiering discipline (Phase 7 and Phase 8 here), not the numbers: the tiers in this skill (sim rules, shared parents, RVO heroes) are the same shape at a smaller scale.
- **Prior art, honestly noted.** A commenter on Dixon's reel points out that Unreal's Mass framework does essentially what the reel recreates (position-only agents, no per-agent actor cost), and another flags Megabonk's prior video with the same features including climbing. Both comments are verified in the raw JSON. The rules in this skill are engine-free and do not depend on Mass, DOTS, or any framework; when working in Unreal, check Mass first before rebuilding the dot tier. In Godot, no equivalent built-in exists, which is why the plain-data sim in this skill is the construction rather than a wrapper.

## Agent automation

Every crowd build in this repo must ship with these artifacts, and a build that lacks one is not done:

1. **crowd-manifest.json.** One file per crowd kind (street citizens, market crowds, horde). Every constant in the rule set listed with its value, its unit, its provenance (reel timestamp or "this skill's derivation"), and its tuning range. Constants with reel provenance: 80 percent threshold, 0.4 s side step, 1.5 s walk-through. Everything else (speeds, look distances, lane-change time, cooldown, cell size) is this skill's derivation and must say so.
2. **Determinism gate.** Fixed seed, 600 ticks, hash of all walker positions. Two runs must match exactly. A mismatch fails the build; the usual cause is a rule reading same-tick hash state (Phase 2 ordering).
3. **Deadlock gate.** The head-on control scene from Phase 5, run both ways (escape rules on and off). On: zero walkers stuck longer than 5 s. Off: a visible lock-up. Both results are required; the off result proves the on result means something.
4. **Equivalence gate.** The hash-vs-brute-force neighbor comparison from Phase 6, on a 200-walker scene, exact match required.
5. **Congestion curve.** The threshold sweep from Phase 8 (0.7, 0.8, 0.9) with arrivals, mean queue length, and max stuck time recorded per value, in the manifest. A build with a single threshold and no curve has not been tuned.
6. **Claim ledger check.** A grep over the crowd's design docs for FPS figures, crowd counts, and hardware claims must return either a measurement record (hardware, count, tick rate, method) or nothing. Reel figures (20,000, 90,000, "hundreds") appearing as facts fail the check.
7. **Scope audit.** Every crowd kind lists which escape modes it may use (ghost, climb, reroute) and which citizens are flagged hero/near-camera. A hero citizen with ghosting enabled fails the audit.

## Valkyrie note

This skill is directly for Valkyrie's citizens: one autonomous citizen per player, living on the authored Pellune Island map while the player is away, seen from a fixed iso camera. Map the pieces as follows. The street grid is authored data: Pellune's streets and plaza become the walkable cells, with lanes derived from street direction, and buildings and cliffs are non-walkable cells, so the grid itself keeps citizens out of walls. The six rules run in the plain .NET sim library (no engine calls), emitting only positions; rendering is the VAT/BAT skills' job, with shared baked parents (Phase 7, tier 4) as the bridge between the two. The stuck timer is already the kind of per-citizen state the sim keeps, so rules 5 and 6 cost one float and one flag per citizen. Scope ghosting to background crowds at iso distance; citizens near the camera, citizens the player is inhabiting, and citizens carrying quest-visible goods use the reroute escape, never the ghost. The reels' first-person and horde specifics do not transfer: there is no horde in Valkyrie, no climb tier for citizens, and no 20,000 figure to chase. What transfers is the discipline: local rules, one dial per behavior, a deadlock proof, and scale bought by deleting costs. Intersections need authored attention on Pellune: the plaza is the town's main crossing, so define its cells as single-lane or accept brief overlap there explicitly, and record the choice in the manifest.

## Depth status

PARTIAL. The behavior rules are fully specified from narrated schematic demos with on-screen rule text and closing summary cards, read firsthand with full transcripts and frames; the Dixon tiers are specified from a narrated montage plus comments verified in raw JSON. No creator code, no engine, no measurements at scale, and no reproducible counts exist in any source reel. The Godot construction (AStar2D graph, spatial hash, lazy ground cache, ghost scoping, hysteresis, cooldown, intersection handling) is this skill's refinement research, grounded in the Godot documentation and sources cited below, and has not been run hands-on. The per-phase checks are what close that gap.

## Sources

- memoryfloater P1: https://www.instagram.com/reel/DfzMGodICCx/
- memoryfloater P2: https://www.instagram.com/reel/Df1uI3eIsnY/
- memoryfloater P3: https://www.instagram.com/reel/Df4UKaZIS-3/
- callme_dixon horde recipe: https://www.instagram.com/reel/DfjNMnVTHKO/
- Godot AStar2D class reference (add_point weight_scale, connect_points, get_point_path, _compute_cost): https://docs.godotengine.org/en/4.4/classes/class_astar2d.html
- Godot PhysicsDirectSpaceState3D class reference (intersect_ray, returned dictionary fields): https://docs.godotengine.org/en/4.2/classes/class_physicsdirectspacestate3d.html
- Godot NavigationAgents tutorial (avoidance, enable_avoidance, velocity_computed signal, RVO assumptions): https://docs.godotengine.org/en/4.2/tutorials/navigation/navigation_using_navigationagents.html
- Reynolds, "Flocks, Herds, and Schools: A Distributed Behavioral Model", Computer Graphics 21(4), SIGGRAPH 1987, pp. 25-34; rule summaries via https://grasp.study/courses/3b4b18fc-3628-43e7-be22-ca84a7477db6/modules/2fb7f90d-68be-4d1c-afee-f249c03f1fd5/lessons/cf5c4aca-07db-491f-88c5-8f26df53b665 and https://b2kit.com/tools/boids-flocking-simulator/
- Helbing and Molnar, "Self-Organization Phenomena in Pedestrian Crowds" (social force model, lane formation): https://ia800709.us.archive.org/33/items/arxiv-cond-mat9806152/cond-mat9806152.pdf
- Nystrom, Game Programming Patterns, Spatial Partition chapter (flat grid, neighbor queries, update cost): https://github.com/Maxize/GameProgrammingPatterns/raw/refs/heads/master/GameProgrammingPatterns_en.pdf
- GDC Vault, "Massive Crowd on Assassin's Creed Unity: AI Recycling" (AI LOD tiers, 40 real AIs, 120 high-resolution models, 10,000 crowd NPCs): https://www.gdcvault.com/play/1022411/Massive-Crowd-on-Assassin-s
- TechRadar, "Inside Assassin's Creed Unity" (bolt crowd, 5,000 to 10,000 AI, crowd realisation team): https://www.techradar.com/news/gaming/inside-assassin-s-creed-unity-ubisoft-s-leap-of-faith-1268435/2

## Cross-links

- `engine-runtime/godot-vertex-animation-texture-crowds`: rendering the crowd. The sim in this skill emits positions; VAT plays baked animation on the crowd with zero CPU skeleton cost. Read its Phase 3 before sizing a crowd.
- `engine-runtime/bone-animation-textures-gpu-instancing`: the BAT alternative for crowds that must keep skeletons alive at runtime. Same rendering contract as VAT, different trade.
- `engine-runtime/godot-1m-agent-ecs-impostors`: scale ceiling reference. Structure-of-arrays data, batch passes, GPU impostors for distant agents. Its update-tier discipline is the fuller form of Phase 7 here.
- `engine-runtime/godot-spom-auto-lod-npc-crowds`: flow-field NPC movement and per-part auto-LOD. Its flow-field system is the alternative movement substrate for open areas where lanes do not apply; this skill's lane rules govern streets.
- `engine-runtime/threejs-sim-render-split-horde`: headless fixed-step sim over typed arrays with hashed golden tests. Its test discipline (deterministic sim, hashed outputs) is the model for the determinism gate here.
- `engine-runtime/mass-entity-niagara-crowd`: the Unreal Mass path. In Unreal, check Mass first before rebuilding the dot tier; in Godot, this skill is the construction.
- `engine-runtime/unity-dots-fake-ragdoll-crowds`: the Unity DOTS equivalent of the simplification tiers, including fake ragdolls and LOD levels. Useful comparison for what "dots plus shared animation" looks like in another engine.
- `procgen-worlds/walkability-density-remap`: the street graph this skill's grid can be built from. Walkability analysis decides where streets and densities go; this skill decides how citizens move on them.
