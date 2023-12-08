import re

from functools import reduce
from operator import mul
from icecream import ic
from pathlib import Path
from typing import Any, List, Tuple

Sample_Input = """\
Time:      7  15   30
Distance:  9  40  200
"""


def parse_input(input: str) -> List[Tuple[int, int]]:
    lines = input.splitlines()
    times = re.findall(r"(\d+)", lines[0])
    records = re.findall(r"(\d+)", lines[1])

    races = list(zip(map(int, times), map(int, records)))
    ic(races)
    return races


def winning_strategies(races: List[Tuple[int, int]]) -> List[int]:
    winners = []
    for race in races:
        winning = 0
        time, record = race
        for charge in range(time):
            distance = charge * (time - charge)
            if distance > record:
                winning += 1
        winners.append(winning)

    return winners


def parse_input2(input: str) -> List[Tuple[int, int]]:
    lines = input.splitlines()
    time = int(lines[0].replace(" ", "").split(":")[1])
    record = int(lines[1].replace(" ", "").split(":")[1])
    return [(time, record)]


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2023" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    races = parse_input(input_data)
    print(f"Step 1: Winning Strategies: {reduce(mul, winning_strategies(races)):,}")  # 1,084,752
    races = parse_input2(input_data)
    print(f"Step 2: Winning Strategies: {reduce(mul, winning_strategies(races)):,}")  # 28,228,952
