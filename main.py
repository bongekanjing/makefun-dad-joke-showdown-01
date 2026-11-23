"""Dad Joke Showdown entry (make.fun u-mfnakmal-dad-joke-showdown-1d2ce3e5).

Pure Python stdlib, no network. Writes one dad joke to /output/entry.txt.
"""

import os

JOKE = "I told my kids I want to be a professional napper when I grow up \u2014 I take my work lying down."

# Validation: the gate requires UTF-8 text of 1-200 characters, and the
# judge wants a single tight joke with its punchline at the end.
assert 1 <= len(JOKE) <= 200, f"joke must be 1-200 chars, got {len(JOKE)}"
assert JOKE == JOKE.strip(), "joke must be stripped"
assert "\n" not in JOKE and "\t" not in JOKE, "no newline or tab allowed"
assert JOKE[-1] in ".!?" and sum(c in ".!?" for c in JOKE) == 1, (
    "exactly one terminal punctuation mark, at the end"
)
# Revision pass: extra structural checks so a stray edit cannot slip a
# malformed entry past the gate (double spaces, control characters, or a
# second delivery pause would all blunt the spoken rhythm).
assert "  " not in JOKE, "no double spaces"
assert all(c.isprintable() for c in JOKE), "no control characters"
assert JOKE.count("\u2014") == 1, "exactly one em-dash delivery pause"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)

print(f"Wrote {len(JOKE)} characters to /output/entry.txt")
