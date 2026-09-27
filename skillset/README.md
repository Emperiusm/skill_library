# Skill set (starter)

**What this is:** the "library" in skill_library. Run reports
(`skills/video-tooling-scout/references/example-run-report.md` shows the format) are ephemeral; skill
cards are the durable knowledge the runs produce. Each card is one
learned skill: what it does, which pipeline stage it fills, where it was
learned from, and the evidence behind it.

**Format rules:**
- One file per skill, named `<slug>.md`.
- `Learned from` must name the video/post with a URL. No URL, no card.
- `Evidence` carries a quote or a verifiable number, never a paraphrase
  presented as fact.
- `Status` is one of: WATCH (interesting, not needed yet), BACKLOG
  (wanted, scheduled), ADOPTED (in the pipeline, with the evidence path),
  SKIPPED (audited, rejected, with the reason).
- Cards are append-only in spirit: when a skill is superseded, annotate the
  card (SUPERSEDED + date + what replaced it), don't delete it.

**How a card gets made:** after a run, the operator promotes high-signal
extractions from the run report into cards. A card is a compression of a
full-depth audit, not a replacement for it; the report keeps the phases,
the card keeps the actionable core.

**Cards vs. skills:** cards are reference notes (what a tool is, where it was
learned from, the evidence). Executable skills, full workflows an agent can
follow step by step, live under `skills/` (e.g.
`skills/cinematic-cavern/SKILL.md`).

**The cards below are EXAMPLES** from a real 2026-09-27 run, sanitized.
Delete them and start your own, or keep them marked EXAMPLE until real
cards arrive.

| Card | Stage | Status |
|---|---|---|
| [planer-mesh-refiner.md](planer-mesh-refiner.md) | Mesh cleanup / QA | EXAMPLE |
| [obi-physics-rope.md](obi-physics-rope.md) | Physics (rope/ragdoll) | EXAMPLE |
| [comfyui-ai-video.md](comfyui-ai-video.md) | Marketing / trailer generation | EXAMPLE |
| [mesh-compression-recipe.md](mesh-compression-recipe.md) | Engine output / perf | EXAMPLE |
