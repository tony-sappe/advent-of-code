import re

from pathlib import Path
from typing import Dict
from collections import defaultdict
from icecream import ic
from copy import deepcopy

Sample_Input = """\
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"""


def parse_input(input: str, part2: bool) -> Dict:
    lines = input.splitlines()
    maps = defaultdict(lambda: defaultdict(int))
    regex = re.compile(r"(\S*) would (lose|gain)\W(-?\d+).* (\S*)\.")
    for line in lines:
        r = regex.search(line)
        val = int(r.group(3))
        if r.group(2) == "lose":
            val *= -1
        maps[r.group(1)][r.group(4)] += val
        maps[r.group(4)][r.group(1)] += val
        if part2:
            maps["Tony"][r.group(1)] = 0
            maps["Tony"][r.group(4)] = 0
            maps[r.group(1)]["Tony"] = 0
            maps[r.group(4)]["Tony"] = 0
    return maps


def maximize_guests(m: Dict, start: str):
    order = [start]
    total = 0
    guests = len(m.keys())
    while guests != len(order):
        max_val = -1_000_000
        max_key = ""
        for k, v in m[start].items():
            if v > max_val:
                max_key, max_val = k, v

        order.append(max_key)
        total += max_val
        del m[max_key][start]
        del m[start][max_key]
        start = max_key

        for g in order[:-1]:
            for k, v in m.items():
                if g in v:
                    del m[k][g]

    total += m[order[0]][order[-1]]

    # ic(order)
    # print(total)
    return total


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    maps = parse_input(input_data, True)
    # ic(maps)
    solutions = []
    for key in maps.keys():
        solutions.append(maximize_guests(deepcopy(maps), key))
    print(f"Optimal happiness {max(solutions):,} ({max(solutions)})")  # 733
