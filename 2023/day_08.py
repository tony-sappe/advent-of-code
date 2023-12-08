from itertools import cycle
from icecream import ic
from pathlib import Path
from math import lcm
from typing import Tuple, Dict

Sample_Input = [
    """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""",
    """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""",
    """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""",
]


def parse_input(input: str) -> Tuple[str, Dict[str, Dict[str, str]]]:
    moves, *other = input.split("\n\n")
    maps = {}
    for o in other[0].splitlines():
        maps[o[:3]] = {"L": o[7:10], "R": o[12:15]}

    return moves, maps


def traverse(moves: str, maps: Dict[str, Dict[str, str]]) -> int:
    pos = "AAA"
    for step, move in enumerate(cycle(moves), 1):
        pos = maps[pos][move]
        if pos == "ZZZ":
            return step


def traverse_2(mov: str, maps: Dict[str, Dict[str, str]]) -> int:
    nodes = [key for key in maps.keys() if key[-1] == "A"]
    paths = []
    for node in nodes:
        for step, move in enumerate(cycle(moves), 1):
            node = maps[node][move]
            if node[-1] == "Z":
                paths.append(step)
                break

    return lcm(*paths)


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2023" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input[1]
    moves, maps = parse_input(input_data)
    ans = traverse(moves, maps)
    print(f"Step 1: Moves: {ans:,} ({ans})")  # 16,531
    ans = traverse_2(moves, maps)
    print(f"Step 2: Moves: {ans:,} ({ans})")  # 24,035,773,251,517
