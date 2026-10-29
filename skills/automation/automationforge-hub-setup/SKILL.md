---
name: automationforge-hub-setup
description: "Install the AutomationForge Hub and get its plugins running in Unreal Engine 5.8: engine-version-first check, account sign-in, stable versus nightly channels, and the install-versus-activation distinction. Trigger when setting up AutomationForge for the first time."
---

# AutomationForge Hub Setup: Install to Activated Project

## Purpose

This skill is the click-level onboarding procedure for the
AutomationForge ecosystem: from installer download to plugins loaded
in a project, in order, with the two distinctions that break setups
when skipped. Every phase has three parts: **Do** (the action),
**Check** (how the human verifies it), and **Why** (the principle).
The core method is: check compatibility first, sign in, install on
stable, then activate with an editor restart.

## Source

YouTube, AutomationForge by Kovati (captions, 2026-10-29):

- https://youtu.be/qROAvFtDoBw — "AutomationForge Hub: Everything You Need to Know to Get Started" (7:46)

Evidence note: captions only, no frames inspected. Genuine 14-step
procedure demonstrated on screen. AutomationForge is presented as
experimental; Mac support, earlier engine versions, and Stripe
payments are roadmap items, labeled as such below. Hub version shown:
0.4.1.

## Tools used

Tools used: AutomationForge Hub installer (0.4.1); Unreal Engine 5.8
on Windows 10/11; plugins including Motion Forge, Motion Forge Kimodo
tool set, MeshForge core, MeshForge cloud, MeshForge garment.

## Phase 1: Check compatibility before downloading anything

**Do**
1. Confirm the engine version first: "We currently support Unreal
   Engine 5.8 on Windows 10 and 11." Mac machines and earlier engine
   versions (5.7, 5.6) are planned, not supported: roadmap, not a
   working feature.
2. Only then download the hub installer.

**Check**
- UE 5.8 on Windows 10 or 11? If not, stop: nothing downstream will
  work.
- Are you planning around Mac or 5.7/5.6 support that does not exist
  yet?

**Why**
Engine-version-first is the discipline that prevents the most common
setup failure: installing a toolchain against an engine it was never
built for, then debugging symptoms instead of the cause.

## Phase 2: Install the hub and sign in

**Do**
1. Run the installer and create the desktop shortcut.
2. Let the hub auto-find the Unreal Engine install.
3. Sign in or create an account before downloading anything:
   "plug-in downloads are tied to an account, including the free
   plugins. So, we need to sign in first or create an account."
4. Connect the hub to the machine.

**Check**
- Hub open, engine found, account signed in, machine connected?
- Did you skip sign-in because the plugin is free? Go back: free
  plugins still require it.

**Why**
The account requirement is the step everyone tries to skip and
nobody can: downloads are entitlement-checked against the account
regardless of price. Doing it first keeps every later step from
failing on authentication.

## Phase 3: Install and update plugins on stable

**Do**
1. Install the entire AutomationForge set at once, or pick
   individual plugins: free ones (Motion Forge) and paid ones
   (MeshForge garment). Paid purchases currently run through a
   simulated payment; Stripe payments are "coming in the next couple
   of days" (roadmap).
2. For updates: the hub "checks for newer plug-in versions" every
   few hours or on refresh. Read the release log before updating,
   then use "update all."
3. Stay on the stable channel: "you can go to settings and change
   your channel from stable to nightly or vice versa. The default is
   stable and we recommend staying on stable because nightly builds
   can be broken."

**Check**
- Release log read before updating?
- Channel set to stable unless you have a specific reason to risk
   nightly?

**Why**
"Update all" without reading the release log is how working projects
break on a Tuesday. The stable default exists because nightly builds
are allowed to be broken; overriding it is opting into that risk
deliberately.

## Phase 4: Activate in the project (not the same as installing)

**Do**
1. Open a fresh UE project on the same engine version (5.8).
2. Enable the plugins in the project (Motion Forge, Kimodo, MeshForge
   in the demonstration).
3. Restart the editor when prompted. This is mandatory, not optional.
4. Verify with the key distinction: "Installation makes a tool
   available to the engine, but activating it loads it into the
   project." Check the Plugins window search or the right-click
   Automation Forge menu.

**Check**
- Editor restarted after enabling?
- Is the tool in the project's Plugins list or right-click menu, not
  just in the hub's installed list?

**Why**
Install-versus-activation is the distinction that breaks setups:
"installed" means the engine can see the tool; "activated" means the
project loads it. Every "the plugin is installed but nothing works"
report is this distinction, missed.

## The human method, distilled

1. Engine version first: UE 5.8 on Windows 10/11, or stop.
2. Sign in before downloading, even for free plugins.
3. Read the release log; update all on stable.
4. Install is not activation: enable in the project, restart the
   editor, verify in the Plugins window.
5. Roadmap is roadmap: Mac, 5.7/5.6, Stripe payments.

## Depth status

FULL (caption evidence; 14-step procedure demonstrated on screen).
