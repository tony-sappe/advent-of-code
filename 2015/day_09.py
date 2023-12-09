import re

from pathlib import Path
from typing import Dict
from collections import defaultdict

Sample_Input = """\
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""


def parse_input(input: str) -> Dict:
    lines = input.splitlines()
    maps = defaultdict(dict)
    regex = re.compile(r"(.*) to (.*) = (\d+)")
    for line in lines:
        r = regex.search(line)
        maps[r.group(1)][r.group(2)] = int(r.group(3))
        maps[r.group(2)][r.group(1)] = int(r.group(3))

    return maps


def shortest_trip(distance, city, cities_left):

    if len(cities_left) == 0:
        return distance

    hops = []
    for i, dest in enumerate(cities_left):
        hops.append(shortest_trip(distance + maps[city][dest], dest, cities_left[:i] + cities_left[i + 1:]))

    return min(hops)


def longest_trip(distance, city, cities_left):

    if len(cities_left) == 0:
        return distance

    hops = []
    for i, dest in enumerate(cities_left):
        hops.append(longest_trip(distance + maps[city][dest], dest, cities_left[:i] + cities_left[i + 1:]))

    return max(hops)


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    maps = parse_input(input_data)
    solutions = []
    for key in maps.keys():
        solutions.append(shortest_trip(0, key, list(maps[key].keys())))
    print(f"Step 1: Efficient route {min(solutions):,} ({min(solutions)})")  # 117

    solutions = []
    for key in maps.keys():
        solutions.append(longest_trip(0, key, list(maps[key].keys())))
    print(f"Step 2: Least Efficient route {max(solutions):,} ({max(solutions)})")  # 909
