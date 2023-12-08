from pathlib import Path
from typing import Iterable, List, Tuple
from collections import Counter

Sample_Input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def parse_input(input: str) -> tuple:
    lines = input.strip().split("\n")
    parsed_lines = []
    for line in lines:
        start, end = line.split(" -> ")
        parsed_lines.append((tuple(map(int, start.split(","))), tuple(map(int, end.split(",")))))

    return parsed_lines


def scrub_diagonal_lines(lines: Iterable[Tuple[Tuple[int, int]]]) -> List[Tuple[Tuple[int, int]]]:
    return [line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]


def create_points(lines: Iterable[Tuple[Tuple[int, int]]]) -> List[Tuple[int, int]]:
    points = []
    for line in lines:
        x_range = sorted([line[0][0], line[1][0]])
        y_range = sorted([line[0][1], line[1][1]])

        if x_range[0] == x_range[1] or y_range[0] == y_range[1]:
            for x in range(x_range[0], x_range[1] + 1):
                for y in range(y_range[0], y_range[1] + 1):
                    points.append((x, y))
        else:
            x, y = line[0]
            x_dir = (1, -1)[x > line[1][0]]
            y_dir = (1, -1)[y > line[1][1]]
            while x != line[1][0] or y != line[1][1]:
                points.append((x, y))
                if x != line[1][0]:
                    x += x_dir
                if y != line[1][1]:
                    y += y_dir
            points.append(line[1])

    return points


def find_hotspots(points):
    c = Counter(points)
    return ([point for point, count in c.items() if count > 1], max(c.values()))


if __name__ == "__main__":
    lines_input = (Path.cwd().parent / "advent-of-code-data" / "2021" / f"{Path(__file__).stem}_input.txt").read_text()
    lines = parse_input(lines_input)

    line_subset = scrub_diagonal_lines(lines)
    points = create_points(line_subset)
    hotspots, hot_temperature = find_hotspots(points)
    print(f"Hottest Temperature is {hot_temperature}, {len(hotspots):,} points reach 2 or higher.")

    points = create_points(lines)
    hotspots, hot_temperature = find_hotspots(points)
    print(f"Hottest Temperature is {hot_temperature}, {len(hotspots):,} points reach 2 or higher.")
