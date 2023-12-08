from pathlib import Path
from typing import List, Tuple

Sample_Input = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""


def parse_input(input: str) -> Tuple[List[List[str]], set, set]:
    grid = list(map(list, input.splitlines()))
    east, south = set(), set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ">":
                east.add((i, j))
            elif grid[i][j] == "v":
                south.add((i, j))

    return grid, east, south


def simulate_moves(grid: List[List[str]], east: set, south: set) -> int:
    moves = 0
    while True:
        new_east = set()
        new_south = set()

        cucumbers = east | south

        for r, c in east:
            new = (r, (c + 1) % len(grid[0]))
            if new in cucumbers:
                new_east.add((r, c))
            else:
                new_east.add(new)

        no_east_moves = east == new_east
        east = new_east
        cucumbers = east | south

        for r, c in south:
            new = ((r + 1) % len(grid), c)
            if new in cucumbers:
                new_south.add((r, c))
            else:
                new_south.add(new)

        no_south_moves = south == new_south
        south = new_south

        if no_east_moves and no_south_moves:
            break

        moves += 1

    return moves


def pp(grid, e, s):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in e:
                print(end=">")
            elif (i, j) in s:
                print(end="v")
            else:
                print(end=".")
        print()


if __name__ == "__main__":
    input_data = (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    grid, east, south = parse_input(input_data)
    first_stopped = simulate_moves(grid, east, south) + 1
    print(f"Step 1: Number of steps until they are locked: {first_stopped}")
