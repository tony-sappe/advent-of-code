from pathlib import Path
from typing import Iterable, List


Sample_Input = """30373
25512
65332
33549
35390
"""


def parse_input(input: str) -> List[List[int]]:
    return [[int(elm) for elm in row] for row in input.splitlines()]


def count_visible(grid: Iterable[Iterable[int]]) -> int:
    count = len(grid) * 2 + len(grid[0]) * 2 - 4  # outside edges
    trees = []

    transposed_grid = list(map(list, zip(*grid)))
    for i, row in enumerate(grid[1:-1], 1):
        for j, elm in enumerate(row[1:-1], 1):
            if elm > max(row[:j]) or elm > max(row[j + 1 :]):  # visible from left or right?
                count += 1
                trees.append((i, j))
            elif elm > max(transposed_grid[j][:i]) or elm > max(transposed_grid[j][i + 1 :]):
                count += 1
                trees.append((i, j))
    return count


def count(height, row) -> int:
    count = 0
    for r in row:
        if r < height:
            count += 1
        else:
            count += 1
            break
    return count


def scenic_score(grid: Iterable[Iterable[int]]) -> int:
    max_score = 0
    transposed_grid = list(map(list, zip(*grid)))
    for i, row in enumerate(grid):
        for j, elm in enumerate(row):
            l = count(elm, row[:j][::-1])
            r = count(elm, row[j + 1 :])
            u = count(elm, transposed_grid[j][:i][::-1])
            d = count(elm, transposed_grid[j][i + 1 :])
            if l * r * u * d > max_score:
                max_score = l * r * u * d
    return max_score


if __name__ == "__main__":
    input_data = (Path.cwd() / "2022" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    grid = parse_input(input_data)
    print(f"Step 1: Visible trees: {count_visible(grid)}")  # 1818
    print(f"Step 2: The top scenic score is {scenic_score(grid)}")  # 368368
