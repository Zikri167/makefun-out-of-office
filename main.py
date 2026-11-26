"""Painfully honest out-of-office auto-reply.

Writes exactly one sentence (122 chars, UTF-8) to
$OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only, deterministic, no network, no API key.
Winner of 16 scored candidates — see CANDIDATES.md in the work dir.
"""
import os

TEXT = "I'm on leave this week, reading everything and answering nothing, because a holiday spent replying isn't a holiday at all."

# Gate check: 1-200 chars, one sentence, not whitespace-only.
assert 1 <= len(TEXT) <= 200 and TEXT.strip() and TEXT.count(".") == 1

def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
