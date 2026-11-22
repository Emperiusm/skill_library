---
name: gitbonsai-github-activity-tree
description: "Grow a Japanese maple bonsai from a GitHub account's public contribution history as an animated SVG for a profile README: first language is the trunk, leaf color is the language, girth is every contribution, deadwood is a stopped language, and a GitHub Action regrows it every Monday without watering itself. Trigger when turning activity history into a readable visual record, or when a scheduled workflow must keep committing so GitHub never pauses it."
---

# gitbonsai: Grow a Bonsai from GitHub Activity

## Purpose

This skill reconstructs the exact workflow from the gitbonsai project
site and its launch post: turn public GitHub activity into an animated
SVG bonsai whose every part maps to one fact about the account, and
regrow it weekly with a GitHub Action that never counts its own work.
Every phase has three parts: **Do** (the action), **Check** (how the
human verifies it), and **Why** (the principle). The core method is:
nothing is ever erased; every year of public activity stays visible
in the tree, and the tree regrows itself every week.

## Source

Creator: DocDrivenDevelopment (StevenBtw). Post: "Growing a Japanese
maple bonsai from 14 years of (simulated) GitHub activity",
https://www.reddit.com/r/proceduralgeneration/comments/1y11eu6/growing_a_japanese_maple_bonsai_from_14_years_of/
(score 39, 5 comments, 5 retrieved). Project site:
https://gitbonsai.dev/ (read in full, including the complete workflow
YAML and the legend). Action: StevenBtw/gitbonsai@v0.5.0. Audited in
the 2026-11-21 scout run, audit 4. The 14-year video in the post is
simulated activity, per the post title, not a real account's history.

## Tools used

gitbonsai (GitHub Action, StevenBtw/gitbonsai@v0.5.0), animated SVG
output, GitHub Actions with the built-in token, a snapshot file for
incremental runs.

## When to use this skill

- Turning a GitHub account's history into a profile README visual
  that can actually be read, not just admired.
- Writing a scheduled GitHub Action that must keep running: the
  snapshot pattern here keeps a schedule alive.
- Designing any generated artifact where every visual decision needs
  a legend entry.

## Prerequisites

- A GitHub profile repository (`you/you`). "Everything runs in your
  own profile repository with GitHub's built-in token."
- Public contribution history to read. "Everything gitbonsai reads
  is public."

## Phase 1: Read a tree as a record, not as decoration

**Do**
1. Grow the tree from the account's public contribution history. The
   post's video is 14 years of simulated activity, "one frame a
   month".
2. Assign meaning before drawing anything: "A newcomer starts as a
   sprout with seed leaves. The first language is the trunk."
3. Apply the legend, part by part:
   - Trunk: "Your first language; it only grows."
   - Leaf color: "The language, on the Japanese maple palette."
   - Girth: "Every contribution ever, and your age."
   - Crown: "Your last three to six years, a sector per language
     with a real share of them."
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
- Use the site's worked examples as the test: 15 years of girth on
  @torvalds, a bare resting tree on @tj, a long streak's pot and
  moss on @steipete, three languages' leaves on @StevenBtw. A tree
  that cannot be read against the legend is not finished. The site
  also hides "a few small surprises of its own" in a tree; the legend
  never says what they are, so do not document them as legend entries.

**Why**
"An animated SVG for a profile README. A newcomer is a thin sprout;
years of work make it short, thick and wide, the way a prize bonsai
is. Each language claims a strand of the trunk, and nothing is ever
erased." The tree is a record with a legend, not a generated picture:
every visual decision maps to one fact about the account.

## Phase 2: Install the weekly regrow in your own profile repo

**Do**
1. Save the workflow as `.github/workflows/bonsai.yml` in the
   profile repository. The workflow in full, from the site:

   ```yaml
   name: bonsai
   on:
     schedule:
       - cron: "17 6 * * 1"   # Mondays 06:17 UTC: the week just ended is complete
     workflow_dispatch:        # run it once by hand
   permissions:
     contents: write
   jobs:
     bonsai:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v7
         - uses: StevenBtw/gitbonsai@v0.5.0
           id: bonsai
           with:
             output-dir: assets
             # legend: left        # what the colors and signs mean, beside the tree
         - name: Commit if it changed
           run: |
             git config user.name "github-actions[bot]"
             git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
             # The snapshot too: the next run then fetches only recent months.
             git add "${{ steps.bonsai.outputs.light }}" "${{ steps.bonsai.outputs.dark }}" \
               "${{ steps.bonsai.outputs.snapshot }}"
             git diff --cached --quiet || git commit -m "Grow bonsai"
             git push
   ```

2. "In the Actions tab, run `bonsai` by hand. After that it runs
   every Monday."
3. Paste the `<picture>` block where the tree should stand: a dark
   source (`assets/bonsai-dark.svg`, `prefers-color-scheme: dark`)
   and a light `<img>` (`assets/bonsai-light.svg`, width 600).

**Check**
- The commit step is the check: "Its last step commits the tree;
  without it a run is green but changes nothing." A green run that
  commits nothing is a silent failure, and the site names it.
- The snapshot is what makes the next run fetch only recent months,
  and what guarantees a change every week: "Each SVG records the
  week it was grown, so every run commits a change and GitHub never
  pauses the schedule."

**Why**
"It commits as github-actions[bot], never as you, so the tree doesn't
water itself." The bot identity keeps the record honest: the tree
records the account's work, and its own regrowth must not count as
work. The snapshot plus the week stamp keeps a scheduled workflow
alive: GitHub pauses schedules on repos with no activity, so a
workflow that sometimes commits nothing would eventually stop
running, and the tree would stop growing.

## Phase 3: Ship the shading, take the repotting note

**Do**
1. Spend the time on the shading. The author, asked whether the bark
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
  accepted and turned into a named next update (realistic
  repotting), not argued with.

**Why**
The shading is the craft cost in a generated-artifact project ("I
spend way too much time on this, normally don't post my projects"),
and the pot is the one part where the growth metaphor breaks (a pot
does not grow linearly). Fixing the metaphor beats defending the
render.

## Failure modes

- **Green run, no commit.** The workflow ran, the tree did not
  change, and nobody noticed. The commit step in Phase 2 exists
  specifically to catch this: without it, a run is green but changes
  nothing.
- **The bot waters itself.** Committing as the account owner would
  make the regrowth itself count as activity. Always commit as
  `github-actions[bot]`.
- **A paused schedule.** A workflow that sometimes commits nothing
  gets paused by GitHub for inactivity. The snapshot and the week
  stamp in every SVG guarantee a change on every run.
- **A pot that grows like a tree.** Linear pot growth reads wrong
  because pots do not grow. Step the pot, center it, and repot
  realistically instead of scaling it with the tree.

## Production practice (vendor docs, not AAA)

No AAA game-studio source was found for growing a visualization
from GitHub activity, and none is claimed here. What the research
did find is vendor documentation that corrects and hardens the
two automation claims in Phase 2, plus industry guidance showing
where GitHub Actions sits in game build pipelines.

Correction to Phase 2, stated plainly: GitHub's documented rule
is narrower than "GitHub pauses schedules on repos with no
activity." In a public repository, scheduled workflows are
automatically disabled when no repository activity has occurred
in 60 days; when a public repository is forked, scheduled
workflows are disabled by default. The documentation does not
state the same 60-day rule for private repositories, so do not
apply it to them. The workflow's state distinguishes the cause:
`disabled_inactivity` for the 60-day rule, `disabled_fork` for a
fork, `disabled_manually` for a human disable. Re-enable from
the Actions tab, with `gh workflow enable`, or by a commit that
changes the cron schedule. Source: GitHub Docs, "Disabling and
enabling a workflow",
https://docs.github.com/en/enterprise-server@3.10/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow ;
state values per an independent write-up of the documented rule,
http://dev.to/kalemi/scheduled-workflow-disabled-after-60-days-of-inactivity-1j45

The second documented rule is the real mechanism behind part of
the "bot never waters itself" principle, and it is separate from
contribution counting. When a workflow uses the repository's
`GITHUB_TOKEN` to perform tasks, events triggered by that token
will not create a new workflow run, with the exceptions of
`workflow_dispatch` and `repository_dispatch` (and, in current
cloud docs, `pull_request` opened/synchronize/reopened events
from a bot-created pull request, which create runs in an
approval-required state). The stated purpose is preventing
recursive workflow runs: a push made with `GITHUB_TOKEN` will
not trigger a push workflow even if one exists. So the
self-commit in Phase 2 cannot retrigger other workflows on its
own; that loop protection is GitHub's, not the bot identity's.
The contribution-graph claim (committing as `github-actions[bot]`
keeps the regrowth from counting as the owner's work) remains
the author's rationale as stated in Phase 2, and is not
separately verified here. Source: GitHub Docs, "Triggering a
workflow",
https://docs.github.com/en/enterprise-cloud@latest/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow

On where GitHub Actions sits in game production: an industry
build-pipeline guide puts GitHub Actions with GameCI as the
right answer for most indie and mid-size Unity teams already on
GitHub, while Unreal teams more often use Jenkins, TeamCity, or
Horde (Epic's own system), and larger studios lean on Jenkins
or TeamCity for complex pipelines. That is guidance, not a named
studio's practice, and it is why this skill's keepalive pattern
is presented as a transferable automation pattern, not as AAA
studio practice. Source: GameDevProducer, "How to Set Up a Build
Pipeline for a Game",
https://www.gamedevproducer.com/posts/how-to-set-up-a-build-pipeline-for-a-game/

### Agent automation

- **Workflow-state check.** Before relying on the Monday run,
  read the workflow state with `gh api
  repos/OWNER/REPO/actions/workflows/bonsai.yml --jq .state`
  and record it. It must read `active`; `disabled_inactivity`,
  `disabled_fork`, or `disabled_manually` each need their own
  fix (re-enable, fork decision, or human review), not a
  re-run of the workflow file. (Grounded in the state values
  above and the `gh api` check in
  https://hyperping.com/blog/how-to-monitor-github-actions-scheduled-workflows )
- **Weekly heartbeat record.** After each Monday run, record
  the run date, whether a commit landed, the commit author
  (must be `github-actions[bot]`), and the week stamp recorded
  in the SVG. A green run with no commit is the silent failure
  named in Phase 2; a week with no run at all is checked
  against the workflow state first, since a disabled schedule
  produces no run and no failure notification. (Grounded in
  the 60-day rule and the Phase 2 commit check.)
- **Snapshot-presence gate.** Every regrow commit must include
  the snapshot file alongside the light and dark SVGs, as in
  Phase 2's `git add` step. A commit with SVGs but no snapshot
  fails the gate: the next run would fetch the full history
  instead of only recent months. (Grounded in Phase 2's
  snapshot rationale; the gate is this skill's own check.)

## The human method, distilled

1. Nothing is ever erased: every language, pause, and streak stays
   in the tree.
2. A legend before a picture: every part of the tree maps to one
   fact, with worked examples.
3. The bot never waters itself: automation commits as the bot, and
   the snapshot guarantees the schedule stays alive.
4. Take the pot criticism: when the metaphor breaks, fix the
   metaphor.

## Depth status

FULL: the project site was read in full, including the complete
workflow YAML and the legend; the post snippet plus all 5 comments
were retrieved. The 14-year video is simulated activity, per the post
title.
