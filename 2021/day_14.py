from collections import Counter
from datetime import datetime
from itertools import tee
from pathlib import Path
from typing import Iterable, Dict

Sample_Input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def parse_input(input: str) -> Iterable[str]:
    template, pairs = input.strip().split("\n\n")
    return template, {pair[:2]: pair[-1] for pair in pairs.split("\n")}


def polymer_chain_growth(template: str, pairs: Dict[str, str], steps: int) -> str:
    for _ in range(steps):
        new_chain = []
        for chunk in pairwise(template):
            new_chain.append(f"{chunk[0]}{pairs[''.join(chunk)]}")
        new_chain.append(chunk[1])
        template = "".join(new_chain)

        if steps > 15 and _ % 5 == 0:
            print(f"[{datetime.now()}] Completed Step #{_}")

    return template


def polymer_counts(chain: str) -> Dict[str, int]:
    return Counter(chain)


if __name__ == "__main__":
    input_data = (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    template, pairs = parse_input(input_data)

    for i, steps in enumerate((10, 15, 20), start=1):
        counts = polymer_counts(polymer_chain_growth(template, pairs, steps))
        quantity_range = max(counts.values()) - min(counts.values())
        print(f"Step {i}: After {steps} steps, template `{template}` has a quantity range of {quantity_range:,}")
