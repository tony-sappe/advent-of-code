import re

from pathlib import Path
from typing import List, Tuple, Set


Sample_Input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def parse_input(input: str) -> List[Tuple[Set[int], Set[int]]]:
    regex = re.compile(r"(\d*)-(\d*),(\d*)-(\d*)")
    pairs = [regex.match(line) for line in input.splitlines()]
    return [
        (
            set(range(int(p.group(1)), int(p.group(2)) + 1)),
            set(range(int(p.group(3)), int(p.group(4)) + 1)),
        )
        for p in pairs
    ]


def is_complete_overlap(assignment: Tuple[Set[int], Set[int]]) -> bool:
    if len(assignment[0]) > len(assignment[1]):
        return assignment[0] >= assignment[1]
    else:
        return assignment[0] <= assignment[1]


def is_any_overlap(assignment: Tuple[Set[int], Set[int]]) -> bool:
    return bool(assignment[0] & assignment[1])


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2022" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    pairs = parse_input(input_data)
    print(f"Step 1: # of complete overlaps: {sum([is_complete_overlap(p) for p in pairs]):,}")  # 513
    print(f"Step 2: # of partial overlaps: {sum([is_any_overlap(p) for p in pairs]):,}")  # 878
