#!/usr/bin/env python3
"""
Final palette pass — grayscale + white base, blue/red glow accents only.

This supersedes the earlier deorange.py. It covers three generations of
colors that have accumulated in the codebase:
  1. The ORIGINAL orange/tan/brick-red "cosmos" theme
  2. The mint-green KOIX theme from the previous round
  3. The dark-green backgrounds used in hero/footer gradients since the
     very first build, plus green "success" message colors

...and replaces all of them with the new grayscale/white palette, using
light blue and red ONLY as glow accents on buttons/tabs/badges.

USAGE
-----
    cd muddo_project
    python3 finalize_grayscale_theme.py            # dry run
    python3 finalize_grayscale_theme.py --apply     # writes changes

Safe to run more than once.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent

REPLACEMENTS = [
    # ── Round 1: orange / tan / brick-red family → gray or blue ────
    ("#e8651a", "#4da3ff"),
    ("#c04e0e", "#2f7fd9"),
    ("#ff8534", "#4da3ff"),
    ("#f5892a", "#4da3ff"),
    ("#ffa060", "#4da3ff"),
    ("#ffb07a", "#4da3ff"),
    ("#fef2e8", "#eef0f2"),
    ("#c43010", "#ff5a5f"),
    ("#8a1a06", "#e0393f"),
    ("#fce8e2", "#eef0f2"),
    ("#d4902a", "#4da3ff"),
    ("#a06810", "#2f7fd9"),
    ("#f0b850", "#4da3ff"),
    ("#e8b84a", "#4da3ff"),
    ("#ffd080", "#4da3ff"),
    ("#fef5e0", "#eef0f2"),
    ("#f5d0a0", "#c7cdd3"),
    ("#c8922a", "#4da3ff"),
    ("#9a6e1a", "#2f7fd9"),
    ("#c8a84b", "#4da3ff"),

    # ── Round 2: mint/KOIX-green family → blue ──────────────────────
    ("#6ee7a0", "#4da3ff"),
    ("#2fae6c", "#2f7fd9"),
    ("#16613b", "#1f2328"),
    ("#9dffc4", "#4da3ff"),
    ("#e3fbee", "#eef0f2"),
    ("#b9f5d0", "#c7cdd3"),

    # ── Round 0 (original build): dark-green hero/footer backgrounds
    #    → dark grayscale ─────────────────────────────────────────
    ("#0d2b14", "#16191d"),
    ("#1a4a24", "#262b31"),
    ("#061008", "#0a0b0d"),
    ("#0e0804", "#121518"),
    ("#170c06", "#16191d"),
    ("#120806", "#0a0b0d"),
    ("#180a04", "#16191d"),

    # ── Original success/green UI states → blue ─────────────────────
    ("#2e7d32", "#2f7fd9"),
    ("#1b5e20", "#2f7fd9"),
    ("#e8f5e9", "#eef0f2"),
    ("#a5d6a7", "#4da3ff"),
    ("#3a5a20", "#1f2328"),
    ("#5a8a3a", "#4b5560"),
    ("#eef5e8", "#eef0f2"),
    ("#2d6e35", "#2f7fd9"),
    ("#0d3d7a", "#1f2328"),   # old "blue-dark" heading color → neutral dark gray text
    ("#1a6abf", "#4da3ff"),   # old mid-blue → the one accent blue

    # ── WhatsApp brand green (FAB button) → blue ─────────────────────
    ("#25d366", "#4da3ff"),

    # ── rgba() variants of all of the above ─────────────────────────
    ("rgba(232,101,26,", "rgba(77,163,255,"),
    ("rgba(232, 101, 26,", "rgba(77, 163, 255,"),
    ("rgba(255,160,96,", "rgba(77,163,255,"),
    ("rgba(255, 160, 96,", "rgba(77, 163, 255,"),
    ("rgba(196,48,16,", "rgba(255,90,95,"),
    ("rgba(196, 48, 16,", "rgba(255, 90, 95,"),
    ("rgba(212,144,42,", "rgba(77,163,255,"),
    ("rgba(212, 144, 42,", "rgba(77, 163, 255,"),
    ("rgba(255,208,128,", "rgba(77,163,255,"),
    ("rgba(255, 208, 128,", "rgba(77, 163, 255,"),
    ("rgba(110,231,160,", "rgba(77,163,255,"),
    ("rgba(46,196,120,", "rgba(77,163,255,"),
    ("rgba(47,174,108,", "rgba(77,163,255,"),
    ("rgba(13,61,122,", "rgba(31,35,40,"),
    ("rgba(26,106,191,", "rgba(77,163,255,"),
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
