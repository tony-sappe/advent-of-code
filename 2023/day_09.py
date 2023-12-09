from pathlib import Path
from typing import List
from copy import copy

Sample_Input = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def parse_input(input: str) -> List[List[int]]:
    return [[int(x) for x in line.split(" ")] for line in input.splitlines()]


def find_next_val(row: List[int]) -> int:
    sequences = []
    sequences.append(copy(row))
    while sum([s != 0 for s in sequences[-1]]) != 0:  # boolean check is to ensure all elms are 0
        p = sequences[-1]  # previous sequence
        sequences.append([p[i + 1] - p[i] for i in range(len(p) - 1)])

    for i in range(len(sequences) - 1, 0, -1):
        sequences[i - 1].append(sequences[i - 1][-1] + sequences[i][-1])

    return sequences[0][-1]


def extrapolated_values_sum(rows: List[List[int]]) -> int:
    return sum([find_next_val(row) for row in rows])


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2023" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    rows = parse_input(input_data)
    ans = extrapolated_values_sum(rows)
    print(f"Step 1: Sum: {ans:,} ({ans})")  # 1861775706

    rows = [row[::-1] for row in rows]
    ans = extrapolated_values_sum(rows)
    print(f"Step 2: Sum: {ans:,} ({ans})")  # 1082
