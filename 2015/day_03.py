from pathlib import Path
from typing import Set, Tuple

Sample_Input = [">", "^>v<", "^v^v^v^v^v"]


def traverse(steps: str) -> Set[Tuple[int, int]]:
    pos = [0, 0]
    houses = set()
    houses.add(tuple(pos))
    for step in steps:
        match step:
            case "<":
                pos[0] -= 1
            case ">":
                pos[0] += 1
            case "^":
                pos[1] -= 1
            case _:
                pos[1] += 1

        houses.add(tuple(pos))

    return houses


def robo_traverse(steps: str) -> Set[Tuple[int, int]]:
    return traverse(steps[::2]) | traverse(steps[1::2])


if __name__ == "__main__":
    steps = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # steps = Sample_Input[1]
    print(f"Step 1: Total unique houses: {len(traverse(steps)):,}")  # 2,572
    print(f"Step 2: Total unique houses: {len(robo_traverse(steps)):,}")  # 2,631
