from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

Sample_Input = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""


def parse_input(input: str) -> Tuple[Dict[int, str], List[List[str]]]:
    lines = input.strip().splitlines()
    image_enhancement = [c == "#" for c in lines[0]]

    image = [[c == "#" for c in row] for row in lines[2:]]

    return image_enhancement, image


def enhance_image(enhance: Iterable[bool], grid: Iterable[Iterable[bool]]) -> List[List[bool]]:
    ng = []
    for row in grid:
        ng.append([0] * 10 + row + [0] * 10)
    for _ in range(10):
        ng.append([0] * (len(grid[0]) + 20))
        ng.insert(0, [0] * (len(grid[0]) + 20))
    ngc = [[0] * (len(ng[0]) - 2) for _ in range(len(ng) - 2)]
    for i in range(1, len(ng) - 1):
        for j in range(1, len(ng[i]) - 1):
            v = [ng[y][x] for y in [i - 1, i, i + 1] for x in [j - 1, j, j + 1]]
            d = int("".join(map(str, map(int, v))), 2)
            ngc[i - 1][j - 1] = enhance[d]
    return ngc


def apply_algorithm(enhance: Iterable[bool], grid: Iterable[Iterable[bool]], count: int) -> int:
    if count > 10:
        for _ in range(count // 2):
            for _ in range(2):
                grid = enhance_image(enhance, grid)
            grid = grid[16:-16]
            grid = [row[16:-16] for row in grid]
    else:
        for _ in range(count):
            grid = enhance_image(enhance, grid)

        grid = grid[10:-10]
        grid = [row[10:-10] for row in grid]

    return sum(map(sum, grid))


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2021" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    algo_string, image = parse_input(input_data)

    day_2_sum = apply_algorithm(algo_string, image, 2)
    print(f"Step 1: image sum: {day_2_sum:,}")  # 5379
    algo_string, image = parse_input(input_data)
    day_50_sum = apply_algorithm(algo_string, image, 50)
    print(f"Step 2: image sum: {day_50_sum:,}")
