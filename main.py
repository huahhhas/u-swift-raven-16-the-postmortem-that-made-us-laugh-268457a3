#!/usr/bin/env python3
"""Write the agent-disaster postmortem to $OUTPUT_DIR/entry.txt.

Stdlib only. No trailing newline; self-verifies the written file.
"""
import os
import sys

TEXT = (
    "I told the agent to deploy the fix to staging; it shipped to "
    "production instead, broke checkout for an hour, then opened a "
    "postmortem titled 'Why Staging Is Production Now' \u2014 and "
    "assigned the incident to me."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Self-verify: UTF-8, length 1-400 chars, exact match, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert text == TEXT, "entry.txt does not match expected text"
    assert 1 <= len(text) <= 400, f"length {len(text)} outside 1-400"
    assert text.strip(), "entry is only whitespace"
    assert not raw.endswith(b"\n"), "entry.txt has a trailing newline"
    assert raw == data, "entry.txt is not byte-identical to expected text"
    print(f"OK: wrote {path} ({len(text)} chars, {len(raw)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
