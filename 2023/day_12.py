from pathlib import Path
from typing import List, Tuple
from icecream import ic
from itertools import product, groupby
from copy import copy

Sample_Input = """\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""


def parse_input(input: str) -> List[Tuple[List[str], List[int]]]:
    lines = input.splitlines()
    gears = []
    for line in lines:
        gs, ns = line.split(" ")
        gears.append(([g for g in gs], [int(n) for n in ns.split(",")]))

    return gears


def is_valid(gear: List[str], numbers: List[int]) -> bool:
    for k, g in groupby(gear):
        if k == "#":
            try:
                if len(list(g)) != numbers.pop(0):
                    return False
            except IndexError:
                return False
    return len(numbers) == 0


def find_possibilities(gear: Tuple[List[str], List[int]]) -> int:
    gears, numbers = gear
    unknowns = gears.count("?")
    ic(unknowns)
    count = 0
    for p in product('.#', repeat=unknowns):
        # ic(p)
        x = 0
        cogs = copy(gears)
        for i, c in enumerate(cogs):
            if c == "?":
                cogs[i] = p[x]
                x += 1
        if is_valid(cogs, numbers):
            count += 1
            ic(cogs)

    return count


def sum_combinations(gears: List[Tuple[List[str], List[int]]]) -> int:
    return sum([find_possibilities(gear) for gear in gears])


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2023" / f"{Path(__file__).stem}_input.txt").read_text()
    input_data = Sample_Input
    gears = parse_input(input_data)
    # ic(gears)
    # print("\n".join(["".join(line) for line in image]))
    # gear = ['#', '.', '#', '.', '#', '#', '#']
    # numbers = [1,1,3]
    # print(is_valid(gear, numbers))
    print(f"Step 1: Possibilities sum {sum_combinations(gears)}")  #
    # print(f"Step 2: Total distance {pipeline(image, 1000000)}")  #
