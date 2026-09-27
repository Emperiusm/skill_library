#!/usr/bin/env python3
"""Annotate reappearing tools in the watchlist and emit a trending snippet.

Usage:
  python3 trend_watchlist.py [--date YYYY-MM-DD] <tool name> [<tool name> ...]
  python3 trend_watchlist.py [--date YYYY-MM-DD] --tools-file tools.json
      (tools.json: {"tools": [{"name": "..."}, ...]})

Compares each extracted tool name against references/tooling-watchlist.md
(case-insensitive substring match, both directions). On a match it appends
"seen again <date>" to that row's Note cell (append-only; never deletes or
rewrites history) and prints a "Watchlist trending" markdown snippet for the
run report. Exit 0 even with zero matches.
"""
import datetime
import json
import os
import re
import sys

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WATCHLIST = os.path.join(SKILL_DIR, "references", "tooling-watchlist.md")


STOPWORDS = {"the", "and", "for", "with", "from", "class", "based",
             "free", "new", "via", "into", "using", "use"}


def norm(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def tokens(s):
    return {t for t in re.findall(r"[a-z0-9]+", norm(s))
            if len(t) >= 3 and t not in STOPWORDS}


def matches(tool, cell):
    t, c = norm(tool), norm(cell)
    if not t or not c:
        return False
    if t in c or c in t:
        return True
    # token overlap: "Obi Physics particle sim" vs
    # "Obi Physics (particle-based, SDF collision)"
    return len(tokens(t) & tokens(c)) >= 2


def parse_table(lines):
    """Split markdown into (header_lines, data_rows, footer_lines).

    header_lines: title/description, column header row, separator row.
    data_rows: list of {"line", "cells"} for each table body row.
    """
    header, rows, footer = [], [], []
    state = "pre"  # pre -> head -> body
    for line in lines:
        if line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().split("|")[1:-1]]
            is_sep = bool(cells) and not any(c.strip(":- ") for c in cells)
            if state == "pre":
                state = "head"
                header.append(line)
            elif state == "head":
                header.append(line)
                state = "body"
            elif is_sep:
                header.append(line)  # stray separator, keep out of data
            else:
                rows.append({"line": line, "cells": cells})
        elif state == "body":
            footer.append(line)
        else:
            header.append(line)
    return header, rows, footer


def main():
    args = sys.argv[1:]
    date = datetime.date.today().isoformat()
    tools = []
    tools_file = None
    rest = []
    i = 0
    while i < len(args):
        if args[i] == "--date" and i + 1 < len(args):
            date = args[i + 1]
            i += 2
        elif args[i] == "--tools-file" and i + 1 < len(args):
            tools_file = args[i + 1]
            i += 2
        else:
            rest.append(args[i])
            i += 1
    if tools_file:
        with open(tools_file) as f:
            tools = [t["name"] for t in json.load(f).get("tools", [])
                     if t.get("name")]
    tools.extend(rest)
    if not tools:
        print("No tool names given; nothing to compare.")
        return

    with open(WATCHLIST) as f:
        lines = f.readlines()
    header, rows, footer = parse_table(lines)

    trending = []  # (row_tool, status, seen_again_dates)
    matched_rows = set()
    for tool in tools:
        for idx, row in enumerate(rows):
            cells = row["cells"]
            if len(cells) < 5 or idx in matched_rows:
                continue
            if matches(tool, cells[1]):
                matched_rows.add(idx)
                note = cells[4]
                tag = f"seen again {date}"
                if tag not in note:
                    cells[4] = (note + "; " + tag).strip("; ") if note else tag
                again = sorted(set(re.findall(r"seen again (\d{4}-\d{2}-\d{2})",
                                              cells[4])))
                trending.append((cells[1], cells[3], cells[0], again))

    out_lines = header[:]
    for row in rows:
        cells = row["cells"]
        if len(cells) >= 5:
            out_lines.append("| " + " | ".join(cells) + " |\n")
        else:
            out_lines.append(row["line"])
    out_lines += footer
    with open(WATCHLIST, "w") as f:
        f.writelines(out_lines)

    if trending:
        print("## Watchlist trending")
        for tool, status, first_seen, again in trending:
            flag = " **TRENDING**" if len(again) >= 2 else ""
            print(f"- {tool} (first seen {first_seen}, status {status}; "
                  f"seen again {', '.join(again)}){flag}")
    else:
        print("No extracted tools reappeared on the watchlist this run.")


if __name__ == "__main__":
    main()
