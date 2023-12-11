from pathlib import Path
from typing import List, Tuple
from icecream import ic
from itertools import combinations

Sample_Input = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""


def parse_input(input: str) -> List[List[str]]:
    return [[c for c in line] for line in input.splitlines()]


def find_emptiness(image: List[List[str]]) -> Tuple[List[int], List[int]]:
    rows = expansion_grid(image)
    image = transpose(image)
    cols = expansion_grid(image)

    return (rows, cols)


def expansion_grid(image: List[List[str]]) -> List[Tuple[int, int]]:
    adds = []
    for i, line in enumerate(image):
        if set(line) == {"."}:
            adds.append(i)

    return adds


def transpose(image: List[List[str]]) -> List[List[str]]:
    return list(map(list, zip(*image)))


def find_galaxies(image: List[List[str]]) -> List[Tuple[int, int]]:
    galaxies = []
    for i, row in enumerate(image):
        for j, c in enumerate(row):
            if c == "#":
                galaxies.append((i, j))

    return galaxies


def add_distance_to_galaxies(galaxies: List[Tuple[int, int]], extra: int, rows: List[int], cols: List[int]) -> List[Tuple[int, int]]:
    for i, g in enumerate(galaxies):
        r = [True for e in rows if e < g[0]].count(True)
        c = [True for e in cols if e < g[1]].count(True)
        galaxies[i] = (g[0] + r * extra, g[1] + c * extra)

    return galaxies


def calculate_total_distance(galaxies: List[Tuple[int, int]]) -> int:
    total = 0
    for c in combinations(galaxies, 2):
        total += abs(c[0][0] - c[1][0]) + abs(c[0][1] - c[1][1])

    return total


def pipeline(image: List[List[str]], expansion: int) -> int:
    rows, cols = find_emptiness(image)
    g = find_galaxies(image)
    g = add_distance_to_galaxies(g, expansion - 1, rows, cols)
    return calculate_total_distance(g)


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2023" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    image = parse_input(input_data)
    # print("\n".join(["".join(line) for line in image]))
    print(f"Step 1: Total distance {pipeline(image, 2)}")  # 9329143
    print(f"Step 2: Total distance {pipeline(image, 1000000)}")  # 710674907809
