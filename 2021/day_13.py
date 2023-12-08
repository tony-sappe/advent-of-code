import re
from pathlib import Path
from typing import Iterable, List, Tuple

Sample_Input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

DOT = "#"
EMPTY = "."


def parse_input(input: str) -> Iterable[str]:
    point_lines, fold_lines = input.strip().split("\n\n")
    points = [tuple(map(int, point.split(","))) for point in point_lines.split("\n")]
    folds = []
    for fold in fold_lines.split("\n"):
        m = re.search(r"(x|y)=(\d+)", fold)
        folds.append((m.group(1), int(m.group(2))))
    return points, folds


def place_dots(points: Iterable[Tuple[int, int]]) -> List[List[str]]:
    """(x,y) == (→,↓)"""
    width = max(points, key=lambda x: x[0])[0] + 1
    height = max(points, key=lambda x: x[1])[1] + 1

    grid = [[EMPTY] * width for _ in range(height)]

    for point in points:
        grid[point[1]][point[0]] = DOT

    return grid


def fold_paper(grid: Iterable[Iterable[str]], fold_instruction: Tuple[str, int]) -> List[List[str]]:
    if fold_instruction[0] == "y":
        height = len(grid)
        for j in range(fold_instruction[1], height):
            for i in range(len(grid[0])):
                if grid[j][i] == DOT:
                    grid[height - j - 1][i] = DOT

        return grid[: fold_instruction[1]]
    else:
        width = len(grid[0])
        for j in range(len(grid)):
            for i in range(fold_instruction[1], width):
                if grid[j][i] == DOT:
                    grid[j][width - i - 1] = DOT

        return [row[: fold_instruction[1]] for row in grid]


def count_dots(grid: Iterable[Iterable[str]]) -> int:
    return sum([1 for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] == DOT])


def step_1(points: Iterable[Tuple[int, int]], folds: Tuple[str, int]) -> int:
    grid = place_dots(points)
    folded_grid = fold_paper(grid, folds[0])
    return count_dots(folded_grid)


def display_grid(grid) -> None:
    print(f"  {'-' * (len(grid[0]) + 2)}")
    for row in grid:
        print(f"  | {''.join(row)} |")
    print(f"  {'-' * (len(grid[0]) + 2)}", "\n")


if __name__ == "__main__":
    input_data = (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    points, folds = parse_input(input_data)

    print(f"Step 1: {step_1(points, folds)}")

    points, folds = parse_input(input_data)
    grid = place_dots(points)
    for fold in folds:
        grid = fold_paper(grid, fold)

    print(f"Step 2: ")
    display_grid(grid)
