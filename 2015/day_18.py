from pathlib import Path
from icecream import ic
from typing import List, Tuple


Sample_Input = """\
.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""


def parse_input(input: str) -> List[List[str]]:
    return [[l for l in line] for line in input.splitlines()]


def be_on(grid: List[List[str]], coord: Tuple[int, int]) -> bool:
    curr_state = grid[coord[0]][coord[1]]

    surrounds = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    on_neighbors = 0
    for s in surrounds:
        pos = (s[0] + coord[0], s[1] + coord[1])
        if pos[0] >= 0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[1]):
            on_neighbors += 1 if grid[pos[0]][pos[1]] == "#" else 0
            # print(f"grid[{pos[0]}][{pos[1]}]: {grid[pos[0]][pos[1]]}")

    # print(f"{coord} has {on_neighbors} lit neighbors")

    if curr_state == "#" and on_neighbors in (2, 3):
        return True
    elif curr_state == "." and on_neighbors == 3:
        return True

    return False


def step(grid: List[List[str]]) -> List[List[str]]:
    # print("\n".join(["".join(l) for l in grid]))
    new_grid = [["." for j in range(len(grid[0]))] for i in range(len(grid))]
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if be_on(grid, (i, j)):
                new_grid[i][j] = "#"

    # print("---")
    # print("\n".join(["".join(l) for l in grid]))
    return new_grid


def count_on(grid: List[List[str]]) -> int:
    return sum([line.count("#") for line in grid])


def steps(grid: List[List[str]], step_count: int) -> int:
    for _ in range(step_count):
        # print(f"=== Step {_} ===")
        grid = stuck_bulbs(grid)
        grid = step(grid)
        grid = stuck_bulbs(grid)

    return count_on(grid)


def stuck_bulbs(grid: List[List[str]]):
    grid[0][0] = "#"
    grid[0][-1] = "#"
    grid[-1][0] = "#"
    grid[-1][-1] = "#"
    return grid


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input  # 4
    grid = parse_input(input_data)
    print(f"Part 1: Lights on {steps(grid, 100)}")  # 1061
    print(f"Part 2: Lights on {steps(grid, 100)}")  # 1006
