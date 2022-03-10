import re
from pathlib import Path
from typing import Any, Iterable, List, Tuple

Sample_Input = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""


def parse_input(input: str) -> Tuple[List[str], List[List[str]]]:
    lines = input.strip().splitlines()
    image_enhancement = ["1" if x == "#" else "0" for x in lines[0]]
    image = [["1" if x == "#" else "0" for x in line.strip()] for line in lines[2:]]

    return image_enhancement, image


def enhance_image(image, enhancement_algorithm):
    pass


if __name__ == "__main__":
    input_data = (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    target_area = parse_input(input_data)
