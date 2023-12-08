import re
from pathlib import Path
from typing import Iterable, List, Tuple

Sample_Input = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


def parse_input(input: Iterable[str]) -> List[Tuple[str, int]]:
    movements = []
    for movement in input.splitlines():
        m = re.search(r"([a-zA-Z]*) (\d+)", movement)
        movements.append((m.group(1), int(m.group(2))))

    return movements


def track_vector_movement(movements: List[Tuple[str, int]], use_aim=True) -> int:
    horizontal, depth, aim = 0, 0, 0

    for direction, magnitude in movements:
        if direction == "forward":
            horizontal += magnitude
            if use_aim:
                depth += aim * magnitude
        elif direction == "down":
            if use_aim:
                aim += magnitude
            else:
                depth += magnitude
        elif direction == "up":
            if use_aim:
                aim -= magnitude
            else:
                depth -= magnitude
        else:
            raise RuntimeError("Unrecognized direction")

    return horizontal * depth


if __name__ == "__main__":
    input_data = (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    movements = parse_input(input_data)

    print(f"Step 1: Submarine traveled {track_vector_movement(movements, False):,} on its course")
    print(f"Step 2: Submarine traveled {track_vector_movement(movements, True):,} on its course")
