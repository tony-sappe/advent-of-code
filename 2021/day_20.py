import re
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
    image_enhancement = {k: "1" if x == "#" else "0" for k, x in enumerate(lines[0])}
    image = [["1" if x == "#" else "0" for x in line.strip()] for line in lines[2:]]

    return image_enhancement, image


def enhance_image(image, enhancement_algorithm):
    pass


def apply_algorithm(image, enhancement, count):
    for _ in range(count):
        image = enhance_image(image)

    return image


if __name__ == "__main__":
    input_data = (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    enhancement, image = parse_input(input_data)

    # print(f"Step 1: Based on scanner reports, the number of beacons is: {beacon_count:,}")
    # print(f"Step 2: Largest Manhattan distance between any two scanners: {distance:,}")
