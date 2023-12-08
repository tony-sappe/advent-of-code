from more_itertools import pairwise
from pathlib import Path
from typing import Any, Iterable, List, Tuple

Sample_Input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def parse_input(input: str) -> List[int]:
    elves = []
    running_total = 0
    for line in input.splitlines():
        if line == "":
            elves.append(running_total)
            running_total = 0
        else:
            running_total += int(line)
    elves.append(running_total)
    return elves


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2022" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    provisions = parse_input(input_data)
    print(f"Step 1: Most calories carried is {max(provisions):,}")
    print(f"Step 2: Calories carried by top three elves: {sum(sorted(provisions)[-3:]):,}")
