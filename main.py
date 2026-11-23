"""One Word From Grandma: the single word a grandma would text about AI.

The word is ALEXAAA -- grandma shouting at the talking box in the
corner, holding the A key a beat too long because she is not quite sure
shouting helps, but she is going to try anyway. Warm, a little baffled,
tied to an AI voice assistant, and funny with no caption at all.

Deterministic: the same bytes are written on every run.
Python 3.13, standard library only, no network, no environment reads.
"""

import os

# The one word grandma would text about AI. No trailing newline: the
# gate counts characters, and the entry is exactly this word.
WORD = "ALEXAAA"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check against the competition's gate before writing: exactly
    # one word, 1 to 30 characters, not only white space. Fail loudly
    # instead of shipping an entry the gate would refuse.
    if not (1 <= len(WORD) <= 30):
        raise ValueError("word must be 1 to 30 characters")
    if len(WORD.split()) != 1 or WORD != WORD.strip():
        raise ValueError("word must be exactly one word, no white space")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
