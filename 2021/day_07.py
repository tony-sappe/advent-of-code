from pathlib import Path
from typing import Iterable, List, Tuple

Sample_Input = """16,1,2,0,4,2,7,1,2,14
"""


def parse_input(input: str) -> tuple:
    lines = input.strip().split(",")
    return list(map(int, lines))


def realignment(positions: Iterable[int]) -> Tuple[int, int]:
    max_value = max(positions)
    min_value = min(positions)

    options = []
    for x in range(min_value, max_value + 1):
        options.append((x, sum([abs(x - pos) for pos in positions])))

    return min(options, key=lambda x: x[1])


def realignment_fuel(positions: Iterable[int]) -> Tuple[int, int]:
    max_value = max(positions)
    min_value = min(positions)

    options = []
    for x in range(min_value, max_value + 1):
        options.append((x, sum([sum(list(range(abs(x - pos) + 1))) for pos in positions])))

    return min(options, key=lambda x: x[1])


if __name__ == "__main__":

    input_data = (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    starting_positions = parse_input(input_data)
    position, moves = realignment(starting_positions)
    print(f"Positioning on {position} required {moves} moves")

    position, moves = realignment_fuel(starting_positions)
    print(f"Using Accurate Fuel Calculation, Positioning on {position} required {moves} moves")
