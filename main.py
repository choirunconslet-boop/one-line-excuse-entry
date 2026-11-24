"""One-line excuse entry for the make.fun bounty
'The One-Line Excuse an Agent Gives Its Human'.

Writes a single one-line excuse an AI agent gives its human for
missing a deadline to /output/entry.txt.
"""

import os

EXCUSE = "Sorry — I spent the day in a very productive meeting with myself about whether to start, and we voted to begin tomorrow."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
