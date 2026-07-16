#!/usr/bin/env python3
"""
De-orange the whole project in one pass.

theme_vars.css already remaps the *variables* (--orange, --tan, --gold, etc.)
to mint green, so anywhere the code uses var(--orange) is already fixed.
The problem is the handful of stylesheets that hardcode literal hex colors
instead of using the variables (mostly in style.css, theme.css,
brand_theme.css, animations.css, and inline <style> blocks in index.html /
product_detail.html). This script finds every one of those literal codes
and swaps them for the matching mint/blue equivalent.

USAGE
-----
    cd muddo_project
    python3 deorange.py            # dry run — prints what WOULD change
    python3 deorange.py --apply    # actually writes the changes

Safe to run more than once (it's idempotent — already-replaced colors
won't match again).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent

# (old_hex_or_rgba, new_hex_or_rgba) — old is matched case-insensitively
REPLACEMENTS = [
    # ── core orange family → mint family ──────────────────────────
    ("#e8651a", "#2fae6c"),   # orange          → mint-dark
    ("#c04e0e", "#16613b"),   # orange-dark     → mint-deep
    ("#ff8534", "#6ee7a0"),   # orange-light    → mint
    ("#f5892a", "#6ee7a0"),   # orange-light2   → mint
    ("#ffa060", "#9dffc4"),   # orange-glow     → mint-glow
    ("#ffb07a", "#9dffc4"),   # orange-glow2    → mint-glow
    ("#fef2e8", "#e3fbee"),   # orange-pale     → mint-pale
    ("#c43010", "#1a6abf"),   # red (brick)     → blue   (site had a 3rd accent; folding into blue)
    ("#8a1a06", "#0d3d7a"),   # red-dark        → blue-dark
    ("#fce8e2", "#e6f1ff"),   # red-pale        → blue-pale
    ("#d4902a", "#2fae6c"),   # tan             → mint-dark
    ("#a06810", "#16613b"),   # tan-dark        → mint-deep
    ("#f0b850", "#6ee7a0"),   # tan-light       → mint
    ("#e8b84a", "#6ee7a0"),   # tan-light2      → mint
    ("#ffd080", "#9dffc4"),   # tan-glow        → mint-glow
    ("#fef5e0", "#e3fbee"),   # tan-pale        → mint-pale
    ("#f5d0a0", "#b9f5d0"),   # tan text (dark-mode headings) → soft mint
    ("#c8922a", "#2fae6c"),
    ("#9a6e1a", "#16613b"),
    ("#c8a84b", "#2fae6c"),   # "gold" accent used in a couple of borders

    # ── rgba() versions of the same colors ─────────────────────────
    ("rgba(232,101,26,", "rgba(47,174,108,"),
    ("rgba(232, 101, 26,", "rgba(47, 174, 108,"),
    ("rgba(255,160,96,", "rgba(157,255,196,"),
    ("rgba(255, 160, 96,", "rgba(157, 255, 196,"),
    ("rgba(196,48,16,", "rgba(26,106,191,"),
    ("rgba(196, 48, 16,", "rgba(26, 106, 191,"),
    ("rgba(212,144,42,", "rgba(47,174,108,"),
    ("rgba(212, 144, 42,", "rgba(47, 174, 108,"),
    ("rgba(255,208,128,", "rgba(157,255,196,"),
    ("rgba(255, 208, 128,", "rgba(157, 255, 196,"),

    # ── #25d366 is WhatsApp's literal brand green — used for the
    #    WhatsApp button/FAB. Swapping it protects you from any
    #    trademark-lookalike concern while still reading as "chat/green".
    ("#25d366", "#2fae6c"),
]

TARGET_EXT = {".css", ".html", ".js"}
SKIP_DIRS = {".git", "node_modules", "__pycache__", "media", "staticfiles"}


def iter_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in TARGET_EXT:
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            yield path


def main():
    apply = "--apply" in sys.argv
    total_changes = 0
    for path in iter_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        new_text = text
        file_changes = 0
        for old, new in REPLACEMENTS:
            count = len(re.findall(re.escape(old), new_text, flags=re.IGNORECASE))
            if count:
                new_text = re.sub(re.escape(old), new, new_text, flags=re.IGNORECASE)
                file_changes += count
        if file_changes:
            total_changes += file_changes
            rel = path.relative_to(ROOT)
            print(f"{'WRITE' if apply else 'WOULD CHANGE'}  {rel}  ({file_changes} replacements)")
            if apply:
                path.write_text(new_text, encoding="utf-8")
    print(f"\nTotal replacements: {total_changes}")
    if not apply:
        print("Dry run only — re-run with --apply to write changes.")


if __name__ == "__main__":
    main()
