from pathlib import Path
from typing import Iterable, List, Tuple

Sample_Input = """2199943210
3987894921
9856789892
8767896789
9899965678
"""


def parse_input(input: str) -> List[List[int]]:
    return [[int(x) for x in row] for row in input.strip().split("\n")]


def find_low_points(grid: Iterable[Iterable[int]]) -> List[int]:
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


def determine_risk(points: Iterable[int]) -> int:
    return sum(points) + len(points)


def find_basins(grid: Iterable[Iterable[int]]) -> List[List[Tuple[int, int]]]:
    basins = []
    grid_map = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] != 9:
                grid_map.append((x, y))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start_new_basin = False
    new_basin = [grid_map.pop()]
    basin_size = len(new_basin)
    while grid_map:
        if start_new_basin:
            basins.append(new_basin)
            new_basin = [grid_map.pop()]
            start_new_basin = False
        for point in new_basin:
            for d in directions:
                x, y = point[0] + d[0], point[1] + d[1]
                if (x, y) in grid_map:
                    grid_map.remove((x, y))
                    new_basin.append((x, y))
        if len(new_basin) != basin_size:
            basin_size = len(new_basin)
        else:
            start_new_basin = True

    return basins


def largest_basins_volume(basins: Iterable[Iterable[int]]) -> int:
    sizes = sorted([len(b) for b in basins], reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


if __name__ == "__main__":
    input_data = (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    grid = parse_input(input_data)

    points = find_low_points(grid)
    print(f"Step 1: Risk Level: {determine_risk(points):,}")

    basins = find_basins(grid)
    print(f"Step 2: There are {len(basins):,} basins, 3 Largest Volumes: {largest_basins_volume(basins):,}")
