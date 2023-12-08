from collections import deque, Counter
from itertools import combinations, starmap
from pathlib import Path
from typing import List, Tuple, Iterable

Sample_Input = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""

Actual_Input = """
#############
#...........#
###D#C#B#C###
  #D#A#A#B#
  #########
"""


def input_grid(q: str) -> List[int]:
    x, y = map(int, q.split(".."))
    return range(max(x, -50), min(y, 50) + 1)


def full_grid(q: str) -> List[int]:
    x, y = map(int, q.split(".."))
    return range(x, y + 1)


def parse_input(input: str) -> List[Tuple[str, str, str, str]]:
    i = []
    for line in input.splitlines():
        ins, data = line.split(" ")
        xd, yd, zd = [d[2:] for d in data.split(",")]
        i.append((ins, xd, yd, zd))
    return i


def initialization_sequence(steps: Iterable[Tuple[str, str, str, str]]) -> int:
    on = set()

    for step in steps:
        if step[0] == "on":
            func = on.add
        else:
            func = on.discard

        for x in input_grid(step[1]):
            for y in input_grid(step[2]):
                for z in input_grid(step[3]):
                    func((x, y, z))

    return len(on)


def reboot_sequence(steps: Iterable[Tuple[str, str, str, str]]) -> int:
    on = set()

    for step in steps:
        if step[0] == "on":
            func = on.add
        else:
            func = on.discard

        for x in full_grid(step[1]):
            for y in full_grid(step[2]):
                for z in full_grid(step[3]):
                    func((x, y, z))

    return len(on)


if __name__ == "__main__":
    input_data = (Path.cwd() / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    reboot_steps = parse_input(input_data)
    print(f"Step 1: # of cubiods on: {initialization_sequence(reboot_steps):,}")  # 615,869
    print(f"Step 2: # of cubiods on: {reboot_sequence(reboot_steps):,}")
