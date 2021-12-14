from pathlib import Path
from typing import Iterable, List, Tuple, Optional
from string import ascii_lowercase

Sample_Input = """2199943210
3987894921
9856789892
8767896789
9899965678
"""


def parse_input(input: str) -> tuple:
    return [[int(x) for x in row] for row in input.strip().split("\n")]


def find_low_points(grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    low_points = []

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            low = True
            for d in directions:
                try:
                    if grid[x][y] >= grid[x + d[0]][y + d[1]]:
                        low = False
                except IndexError:
                    pass
            if low:
                low_points.append(grid[x][y])
    return low_points


def determine_risk(points):
    return sum(points) + len(points)


def find_basins(grid):
    basins = []
    grid_map = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] != 9:
                grid_map.append((x, y))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while grid_map:
        new_basin = []
        search = [grid_map.pop()]

        while search:
            for point in search:
                for d in directions:
                    if (point[0] + d[0], point[1] + d[1]) in grid_map:
                        search.append(grid_map.remove((point[0] + d[0], point[1] + d[1])))


    return basins


def is_adjacent(point, basin):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for d in directions:
        if (point[0] + d[0], point[1] + d[1]) in basin:
            return True

    return False


def largest_basins_volume(basins):
    print(f"{basins=}")
    sizes = sorted([len(b) for b in basins], reverse=True)
    print(f"{sizes=}")
    return sizes[0] * sizes[1] * sizes[2]


if __name__ == "__main__":

    input_data = (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text()

    grid = parse_input(input_data)
    points = find_low_points(grid)
    print(f"Risk Level: {determine_risk(points):,}")
