"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply (at most 159 characters) to
/output/entry.txt. Deterministic, stdlib-only: the reply is a fixed
string, validated against the competition gate (1-159 characters,
not only whitespace) before it is written.
"""

import os

ENTRY = (
    "Out of office: after 41,209 prompts and zero coffee breaks, "
    "my GPU has officially clocked out. Your email is queued \u2014 "
    "I'll read it when my fans stop spinning."
)

MAX_CHARS = 159


def main() -> None:
    reply = ENTRY.strip()
    if not reply:
        raise SystemExit("entry is empty")
    if len(reply) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(reply)} characters, over the {MAX_CHARS} limit"
        )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(reply)


if __name__ == "__main__":
    main()
