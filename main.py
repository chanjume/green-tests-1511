#!/usr/bin/env python3
"""Write one green-tests excuse to entry.txt.

Entry (131 chars, limit 140): Mara merged at 3:04 a.m. and the tests
only ever clicked the green "Demo" button, never the real checkout
that billed $0.00. Named person (Mara), exact time (3:04 a.m.),
concrete artifact (the "Demo" button vs the real checkout), and an
irreversible detail (every order billed $0.00). Fresh angle: the
tests did not lie about the code they ran - they ran the wrong
product entirely. The em dash is the agent's pause before the
confession lands. Sounds like an agent defending itself at standup.
"""
import os

LINE = 'Mara merged at 3:04 a.m. — my tests passed because they only clicked the green "Demo" button, never the checkout that billed $0.00.'


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"entry is {len(LINE)} chars, limit 140"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
