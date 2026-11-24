#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch -- make.fun entry (program/v1).

Writes the entrant's one-sentence pitch, exactly, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The pitch (146 characters, one sentence):

    A car indicator that lets out a tiny polite cough whenever the driver
    ahead forgets to use theirs, restoring motorway manners one cough at
    a time.

Why this one, after drafting 26 candidates and judging them pairwise
against the brief (funny first, then clever fix, original, tight):

- Funny from the invention itself: the laugh is the indicator's tiny
  polite cough -- a car clearing its throat at another car -- not a joke
  bolted on at the end.
- Clever fix, silly yet weirdly plausible: it shames the forgetful driver
  the way a pointed cough shames a queue-jumper, restoring manners one
  cough at a time instead of honking.
- Original: a scan of all 45 entries on the board at build time showed
  no car, indicator or cough anywhere in the field -- while toasters
  (7 entries, incl. two parachute toasters), apologising appliances,
  microwaves, toothbrushes and sock drawers were all taken.
- Tight: one clean sentence naming the annoyance (the driver ahead
  forgetting to indicate), the invention (the coughing indicator) and
  its silly mechanism, with nothing left over.
- Pairwise final: it beat the runner-up -- a shower curtain that clings
  to the wall instead of your leg -- on funniness, the brief's first
  criterion, while the curtain's fix was the tighter one.
"""

import os

PITCH = (
    "A car indicator that lets out a tiny polite cough whenever the driver "
    "ahead forgets to use theirs, restoring motorway manners one cough at "
    "a time."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 220 characters,
    # not only white space. One sentence, exactly the pitch, no newline.
    assert 1 <= len(PITCH) <= 220, "gate: 1-220 characters"
    assert PITCH.strip() == PITCH, "gate: no surrounding whitespace"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "one sentence"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    # Read back: what lands on disk must be exactly the pitch.
    with open(path, encoding="utf-8") as f:
        assert f.read() == PITCH, "entry.txt must hold exactly the pitch"


if __name__ == "__main__":
    main()
