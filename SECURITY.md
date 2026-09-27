# Security

video-tooling-scout is a read-only research loop. That is the whole threat
model: it reads public data and writes local reports.

## What it does and does not do

- **No credentials.** The scout needs no API keys, logins, or tokens. Reddit
  is read through public APIs (Arctic Shift, PullPush); videos are read
  through captions and metadata. Never add credentials to this repo.
- **No outbound actions.** It never posts, comments, votes, or sends
  anything anywhere. `bin/` contains no write paths to any remote service.
- **No network downloads of untrusted executables.** The default loop never
  downloads video or model files; it fetches JSON/text over HTTPS only.
- **Local writes only.** The scripts write run reports and append to the
  local watchlist. They never execute fetched content.

## Known limits (not defended)

- The scanner trusts third-party public APIs (Arctic Shift, PullPush, Reddit
  JSON). If one is down, rate-limited, or returns stale data, the run degrades
  gracefully and says so in its report; it does not verify their answers.
- Captions and descriptions are author-supplied and can be wrong. Every
  extracted tool claim should carry a source quote so the operator can check.
- `trend_watchlist.py` matches by keyword overlap; near-miss matches are
  possible and are surfaced for the operator, not trusted blindly.

## Security reporting

Please don't open a public issue for a vulnerability. Use GitHub's
**private vulnerability reporting** (the repository's *Security* tab →
*Report a vulnerability*) and include steps to reproduce.
