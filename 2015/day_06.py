import re

from pathlib import Path
from typing import List, Tuple, Callable

Sample_Input = """\
turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500
"""


def parse_input(input: str) -> List[Tuple[str, List[int], List[int]]]:
    regex = re.compile(r"(.+) (\d+,\d+) through (\d+,\d+)")
    instructions = regex.findall(input)
    for i, ins in enumerate(instructions):
        instructions[i] = (
            ins[0].replace("turn ", ""),
            [int(i) for i in ins[1].split(",")],
            [int(i) for i in ins[2].split(",")],
        )

    return instructions


def get_func1(op: str) -> Callable:
    if op == "on":
        return lambda x: 1
    elif op == "off":
        return lambda x: 0
    else:
        return lambda x: (x + 1) % 2


def get_func2(op: str) -> Callable:
    if op == "on":
        return lambda x: x + 1
    elif op == "off":
        return lambda x: max(x - 1, 0)
    else:
        return lambda x: x + 2


def operate(instructions: List[Tuple[str, List[int], List[int]]], mode: Callable) -> int:
    grid = [[0 for x in range(1000)] for y in range(1000)]
    for op, srt, end in instructions:
        func = mode(op)
        for x in range(srt[0], end[0] + 1):
            for y in range(srt[1], end[1] + 1):
                grid[x][y] = func(grid[x][y])

    return sum([elm for row in grid for elm in row])


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    instructions = parse_input(input_data)
    print(f"Step 1: Number of lights on {operate(instructions, get_func1):,}")  # 569,999
    print(f"Step 2: Brightness {operate(instructions, get_func2):,}")  # 17,836,115
