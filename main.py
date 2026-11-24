#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't — make.fun entry.

Writes one original one-line weather forecast to /output/entry.txt.
Pure Python standard library: no imports beyond os/sys/unicodedata,
no network, no files read, no environment read except the output
directory.

The line (137 characters): a forecast for Bumbledorf, a city that
does not exist — light drizzle, 14 C, and a 90% chance the bus is
late again — closing with the turn of phrase "pack an umbrella and
low expectations for the morning commute". It keeps the register of
a real broadcast forecast (place, conditions, temperature,
probability), names the invented city up front, gives the place one
concrete detail of its life (the chronically late bus), and lands
its joke on the bored commuter reading it at a rainy bus stop: the
thing to pack is not just an umbrella but low expectations.
"""
import os
import sys
import unicodedata

LINE = (
    "Bumbledorf: light drizzle, 14\u00b0C, with a 90% chance the bus "
    "is late again \u2014 pack an umbrella and low expectations for "
    "the morning commute."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    text = LINE.strip()
    if not 1 <= len(text) <= 140:
        print(f"entry must be 1-140 chars, got {len(text)}", file=sys.stderr)
        return 1
    if text != text.strip() or not text:
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    # The judge reads printable text: no control characters, and at
    # least one letter so it cannot be punctuation alone.
    if any(unicodedata.category(ch).startswith("C") for ch in text):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    if not any(ch.isalpha() for ch in text):
        print("entry must contain at least one letter", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
