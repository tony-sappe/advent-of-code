from pathlib import Path
from typing import Iterable, List, Tuple

Sample_Input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


def parse_input(input: str) -> Iterable[Iterable[int]]:
    return [list(map(int, l)) for l in input.strip().split("\n")]


def simulate_flashes(grid: Iterable[Iterable[int]], steps: int) -> Tuple[List[List[int]], int]:
    # Cycle counter-clockwise from top left:
    #    ↖ ↑ ↗ → ↘ ↓ ↙ ←
    neighbors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    row_span = list(range(len(grid[0])))
    col_span = list(range(len(grid)))
    flash_total = 0
    for _ in range(steps):
        grid = add_one_to_all(grid)
        while full_energy_exists(grid):
            for x in col_span:
                for y in row_span:
                    if grid[x][y] > 9:
                        flash_total += 1
                        grid[x][y] = 0
                        for neighbor in neighbors:
                            row = x + neighbor[0]
                            col = y + neighbor[1]
                            if row in row_span and col in col_span and grid[row][col] != 0:
                                grid[row][col] += 1

    return grid, flash_total


def add_one_to_all(grid: Iterable[Iterable[int]]) -> List[List[int]]:
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y] += 1

    return grid


def full_energy_exists(grid: Iterable[Iterable[int]]) -> bool:
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] > 9:
                return True

    return False


def no_energy_exists(grid: Iterable[Iterable[int]]) -> bool:
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] != 0:
                return False

    return True


def find_simultaneous_flash(grid: Iterable[Iterable[int]]) -> Tuple[List[List[int]], int]:
    steps = 0
    while True:
        steps += 1
        grid, _ = simulate_flashes(grid, 1)
        if no_energy_exists(grid):

            return grid, steps


if __name__ == "__main__":
    steps = 100
    input_data = (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    grid = parse_input(input_data)
    grid, flashes = simulate_flashes(grid, steps)
    print(f"After {steps:,} steps, there were {flashes:,} flashes with an end state of:")
    for row in grid:
        print(f"  {row}")

    grid = parse_input(input_data)
    grid, steps = find_simultaneous_flash(grid)
    print(f"There were 100% simultaneously flashes on Step {steps:,}")
    for row in grid:
        print(f"  {row}")
