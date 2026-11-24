"""Absurd Micro-Startup Pitch-Off: one sentence, under 200 characters.

The pitch: naming rights for error messages. A plumber pays $5 every
time an AI agent's crash carries his name, so the agent earns money
by failing gracefully and never has to do any work at all.
"""

LINE = "We sell naming rights to error messages: for $5, your AI agent's crash becomes 'Sponsored by Dave's Plumbing,' and Dave pays every time the agent fails gracefully."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only white space, and exactly one sentence.
    if not (1 <= len(LINE) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not LINE.strip():
        raise ValueError("entry must not be blank")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
