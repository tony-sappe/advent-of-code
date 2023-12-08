from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Tuple

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


def parse_input(input: str) -> Tuple[Dict[str, int], Dict[str, str]]:
    template, rules = input.strip().split("\n\n")
    polymer_chain = Counter((x + y for x, y in zip(template, template[1:])))
    insertion_rules = {pair[:2]: pair[-1] for pair in rules.split("\n")}
    return template, polymer_chain, insertion_rules


def polymer_chain_growth(polymer_chain: Dict[str, int], rules: Dict[str, str], steps: int) -> Dict[str, int]:
    for _ in range(steps):
        new_polymer_chain = defaultdict(int)
        for polymer in polymer_chain:
            rule = rules[polymer]
            new_polymer_chain[polymer[0] + rule] += polymer_chain[polymer]
            new_polymer_chain[rule + polymer[1]] += polymer_chain[polymer]

        polymer_chain = new_polymer_chain

    hc = defaultdict(int)
    tc = defaultdict(int)

    for p in polymer_chain.keys():
        hc[p[0]] += polymer_chain[p]
        tc[p[1]] += polymer_chain[p]

    return {x: max(hc.get(x, 0), tc.get(x, 0)) for x in set(hc) | set(tc)}


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2021" / f"{Path(__file__).stem}_input.txt").read_text()
    template, polymer_chain, insertion_rules = parse_input(input_data)

    for i, steps in enumerate((10, 40), start=1):
        counts = polymer_chain_growth(polymer_chain, insertion_rules, steps)
        quantity_range = max(counts.values()) - min(counts.values())
        print(f"Step {i}: After {steps} steps, polymer_chain `{template}` has a quantity range of {quantity_range:,}")
