from pathlib import Path
from typing import List
from itertools import combinations

Sample_Input = """\
20
15
10
5
5
"""

VOLUME = 150


def parse_input(input: str) -> List[int]:
    return [int(d) for d in input.splitlines()]


def brute_force(containers: List[int]) -> int:
    total = 0
    for i in range(2, len(containers) + 1):
        for c in combinations(containers, i):
            if sum(c) == VOLUME:
                # print(c)
                total += 1

    return total


def brute_force2(containers: List[int]) -> int:
    combos = []
    for i in range(2, len(containers) + 1):
        for c in combinations(containers, i):
            if sum(c) == VOLUME:
                combos.append(c)

    min_number = min([len(c) for c in combos])
    # print(f"Minimum number of containers needed: {min_number}")
    return [True for c in combos if len(c) == min_number].count(True)


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    containers = parse_input(input_data)
    print(f"Part 1: Combinations {brute_force(containers)}")  # 4372
    print(f"Part 2: Combinations {brute_force2(containers)}")  # 4
