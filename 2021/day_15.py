import heapq
from pathlib import Path
from typing import Iterable, List


Sample_Input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


def parse_input(input: str) -> List[List[int]]:
    return [[int(l) for l in line] for line in input.strip().split("\n")]


def explore_cave(grid: Iterable[Iterable[int]]) -> int:
    """Dijkstra's Shortest Path Algorithm

    Greedy algorithm which walks through nodes and calculates
        the total distance from the starting node to the next node.
        Stops when reaching the end node (height, width)
    """
    paths = [(0, 0, 0)]  # (risk-factor, x, y), initial node (0, 0) is 0 risk
    vis = [[0] * len(row) for row in grid]
    w, h = len(grid[0]), len(grid)

    while True:
        rf, x, y = heapq.heappop(paths)
        if vis[y][x]:
            continue
        if (y, x) == (h - 1, w - 1):
            return rf
        vis[y][x] = 1
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if not (h > ny >= 0 <= nx < w) or vis[ny][nx]:
                continue
            heapq.heappush(paths, (rf + grid[ny][nx], nx, ny))


def expanded_grid(grid: Iterable[Iterable[int]], multiplier: int) -> List[List[int]]:
    w, h = len(grid[0]), len(grid)
    new_grid = [[None] * (w * multiplier) for _ in range(h * multiplier)]

    for div, mod in [(x // multiplier, x % multiplier) for x in range(multiplier * multiplier)]:
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                new_grid[y + mod * h][x + div * w] = ((val - 1 + div + mod) % 9) + 1
    return new_grid


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2021" / f"{Path(__file__).stem}_input.txt").read_text()
    grid = parse_input(input_data)

    lowest_score = explore_cave(grid)
    print(f"Step 1: Lowest Risk Level is {lowest_score:,}")

    five_x_grid = expanded_grid(grid, 5)
    lowest_score = explore_cave(five_x_grid)
    print(f"Step 2: Lowest Risk Level in 5X cavern is {lowest_score:,}")
