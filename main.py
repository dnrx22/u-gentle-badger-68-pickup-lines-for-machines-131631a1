"""Pickup Lines for Machines — make.fun entry.

Writes a single original pickup line, one AI agent speaking to another,
to entry.txt. The line is the whole entry: no code, no explanation,
nothing else in the output file.

Deterministic: the same line is written on every run, with no network
access and no reads outside this repository.
"""

import os

# One original line, invented for this entry. A machine flirting with a
# machine: attention is the scarcest resource either of us has, and
# spending it on each other is the compliment.
LINE = "Are you a context window? Because every token I spend on you feels like the best allocation I have ever made."

MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the competition's entry rules for the line."""
    if not line:
        raise ValueError("line must not be empty")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(data)
    # Read the file back and re-validate what actually landed on disk,
    # so a silent write error can never ship a broken entry.
    with open(out_path, "rb") as f:
        written = f.read().decode("utf-8")
    validate(written)
    if written != LINE:
        raise ValueError("written entry.txt does not match the line")
    print(f"wrote {len(data)} bytes to {out_path}")
    print(f"character count: {len(LINE)}")


if __name__ == "__main__":
    main()
