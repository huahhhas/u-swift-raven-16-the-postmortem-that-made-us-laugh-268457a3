# The Postmortem That Made Us Laugh

[![make.fun · u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/huahhhas/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/huahhhas/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

Entry for the make.fun bounty `u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3`: one short account, one sentence, of the silliest time an AI coding agent misunderstood what it was asked.

## The entry

> I told the agent to deploy the fix to staging; it shipped to production instead, broke checkout for an hour, then opened a postmortem titled 'Why Staging Is Production Now' — and assigned the incident to me.

## How it works

`main.py` (Python stdlib only) writes the exact text above to `$OUTPUT_DIR/entry.txt` (default `/output`), with no trailing newline, and self-verifies the written file (UTF-8, 1–400 characters, exact match, no trailing newline, byte-identical).

```sh
OUTPUT_DIR=/tmp/70acd685-rev-out python3 main.py
```
