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

Extra_Rows = []
Extra_Cols = []


def parse_input(input: str) -> List[List[str]]:
    return [[c for c in line] for line in input.splitlines()]


def expand_image(image: List[List[str]], extra: int) -> List[List[str]]:
    image = add_lines(image, extra)
    image = transpose(image)
    image = add_lines(image, extra)
    return transpose(image)


def add_lines(image: List[List[str]], extra: int) -> List[List[str]]:
    adds = []
    empty = []
    for i, line in enumerate(image):
        if set(line) == {"."}:
            adds.append(i)
            empty = line

    for i, a in enumerate(adds):
        for _ in range(extra):
            image.insert(a + (i * extra), empty)
    return image


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


def calculate_total_distance(galaxies: List[Tuple[int, int]]) -> int:
    total = 0
    for c in combinations(galaxies, 2):
        total += abs(c[0][0] - c[1][0]) + abs(c[0][1] - c[1][1])

    return total


def add_distance_to_galaxies(galaxies: List[Tuple[int, int]], extra: int) -> List[Tuple[int, int]]:
    for i, g in enumerate(galaxies):
        rows = [True for e in Extra_Rows if e < g[0]].count(True)
        cols = [True for e in Extra_Cols if e < g[1]].count(True)
        galaxies[i] = (g[0] + rows * extra, g[1] + cols * extra)

    return galaxies


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2023" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    image = parse_input(input_data)
    # print("\n".join(["".join(line) for line in image]))
    image = expand_image(image, 1)
    # print("\n".join(["".join(line) for line in image]))
    g = find_galaxies(image)
    print(f"Step 1: Total distance {calculate_total_distance(g)}")  # 9329143

    image = parse_input(input_data)
    Extra_Rows = expansion_grid(image)
    image = transpose(image)
    Extra_Cols = expansion_grid(image)
    image = transpose(image)
    g = find_galaxies(image)
    ic(Extra_Rows)
    ic(Extra_Cols)
    g = add_distance_to_galaxies(g, 1000000 - 1)
    print(f"Step 2: Total distance {calculate_total_distance(g)}")  # 710674907809
