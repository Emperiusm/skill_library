#!/usr/bin/env python3
"""Fetch top comments for Reddit posts (tooling details live in comments).

Usage: python3 fetch_comments.py <post_id>[:num_comments] [<post_id>[:num_comments] ...]
Post IDs are the base-36 ids from permalinks, e.g. 1wjnwzi.
Outputs JSON: {post_id: [{author, score, body}, ...], "_sources": {post_id: source}}.

Source: Arctic Shift public API (same as scan_videos.py). Fallback chain when
Arctic Shift returns zero comments but the post reports num_comments > 0
(known index coverage gap):
  1. old.reddit.com JSON (https://old.reddit.com/comments/<id>/.json) with a
     browser User-Agent;
  2. PullPush API (https://api.pullpush.io/reddit/search/comment/), the
     Pushshift successor.
Old Reddit is tried first, but Reddit bot-walls unauthenticated JSON from
this sandbox (returns the "Welcome to Reddit" interstitial HTML instead of
JSON), so PullPush is the fallback that actually works here. No login,
read-only.
"""
import json
import sys
import time
import urllib.parse
import urllib.request

ARCTIC = "https://arctic-shift.photon-reddit.com/api/comments/search"
SCOUT_UA = "Mozilla/5.0 (compatible; video-tooling-scout/1.0)"
BROWSER_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")


def get_json(url, ua, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def fetch_arctic(pid, limit=25):
    q = urllib.parse.urlencode({"link_id": pid, "limit": limit, "sort": "desc"})
    data = get_json(ARCTIC + "?" + q, SCOUT_UA)
    return [{
        "author": c.get("author"),
        "score": c.get("score"),
        "body": (c.get("body") or "")[:800],
    } for c in data.get("data", [])]


def flatten_old_reddit(node, out, depth=0):
    """Collect t1 comments from an old-reddit JSON listing, one reply level."""
    if not isinstance(node, dict):
        return
    data = node.get("data") or {}
    for child in data.get("children", []):
        if not isinstance(child, dict) or child.get("kind") != "t1":
            continue
        cd = child.get("data") or {}
        out.append({
            "author": cd.get("author"),
            "score": cd.get("score"),
            "body": (cd.get("body") or "")[:800],
        })
        if depth == 0:
            flatten_old_reddit(cd.get("replies"), out, depth=1)


def fetch_old_reddit(pid, limit=25):
    """Old Reddit JSON. Returns None (not an error) when Reddit serves its
    bot-wall interstitial instead of JSON, so the caller can try PullPush."""
    url = f"https://old.reddit.com/comments/{pid}/.json?limit={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": BROWSER_UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            if "json" not in (r.headers.get("content-type") or ""):
                return None
            payload = json.load(r)
    except Exception:
        return None
    out = []
    listings = payload if isinstance(payload, list) else [payload]
    for listing in listings[1:2] or listings:  # comments listing is 2nd
        flatten_old_reddit(listing, out)
    out.sort(key=lambda c: c.get("score") or 0, reverse=True)
    return out[:limit]


def fetch_pullpush(pid, limit=25):
    """PullPush (Pushshift successor) comment search by post id."""
    q = urllib.parse.urlencode({
        "link_id": pid, "size": limit, "sort": "desc", "sort_type": "score"})
    data = get_json("https://api.pullpush.io/reddit/search/comment/?" + q,
                    SCOUT_UA)
    return [{
        "author": c.get("author"),
        "score": c.get("score"),
        "body": (c.get("body") or "")[:800],
    } for c in data.get("data", [])]


def fetch_fallback(pid, limit=25):
    """Fallback chain: old Reddit JSON, then PullPush. Returns (comments, src).

    PullPush is occasionally flaky/rate-limited, so it gets two attempts
    with a short backoff before we give up and report empty.
    """
    comments = fetch_old_reddit(pid, limit)
    if comments:
        return comments, "old_reddit_fallback"
    comments = []
    for attempt in range(2):
        try:
            comments = fetch_pullpush(pid, limit)
            break
        except Exception:
            time.sleep(3)
    return comments, "pullpush_fallback" if comments else "empty"


def parse_spec(spec):
    if ":" in spec:
        pid, _, n = spec.partition(":")
        try:
            return pid, int(n)
        except ValueError:
            return pid, None
    return spec, None


def main():
    out, sources = {}, {}
    for spec in sys.argv[1:]:
        if spec.startswith("-"):
            continue
        pid, expected = parse_spec(spec)
        try:
            comments = fetch_arctic(pid)
            source = "arctic_shift"
        except Exception as e:
            out[pid] = {"error": f"arctic_shift: {e}"}
            sources[pid] = "error"
            continue
        if not comments and expected and expected > 0:
            # Known Arctic Shift index coverage gap: post has comments that
            # the index does not. Run the fallback chain (old Reddit JSON,
            # then PullPush), all read-only, no login.
            try:
                comments, source = fetch_fallback(pid)
            except Exception as e:
                sources[pid] = f"arctic_shift_empty+fallback_failed: {e}"
                out[pid] = []
                continue
        elif not comments:
            source = "empty"
        out[pid] = comments
        sources[pid] = source
    out["_sources"] = sources
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
