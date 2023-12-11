from pathlib import Path
from typing import List
from copy import copy
from icecream import ic

Sample_Input = ["""\
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
""",
   """\
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""",
]


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.


def parse_input(input: str) -> List[List[str]]:
    return [[c for c in line] for line in input.splitlines()]


def navigate(maze: List[List[str]]) -> int:
    for r, row in enumerate(maze):
        for c, col in enumerate(row):
            if col == "S":
                start = (r, c)
                pos = (r, c)

    steps = 0
    while True:
        if steps > 2:
            maze[start[0]][start[1]] = "S"

        if maze[pos[0]][pos[1]] == "S" and steps > 0:
            return (steps + 1) // 2

        north, south, east, west = None, None, None, None
        if pos[1] < len(maze[0]) - 1:
            east = maze[pos[0]][pos[1] + 1]
        if pos[1] > 0:
            west = maze[pos[0]][pos[1] - 1]
        if pos[0] > 0:
            north = maze[pos[0] - 1][pos[1]]
        if pos[0] < len(maze) - 1:
            south = maze[pos[0] + 1][pos[1]]

        spot = maze[pos[0]][pos[1]]

        can_go_north = north and north in "|7FS" and spot in "|LJS"
        can_go_south = south and south in "|LJS" and spot in "|7FS"
        can_go_east = east and east in "-7JS" and spot in "-LFS"
        can_go_west = west and west in "-LFS" and spot in "-7JS"

        # print(f"({pos[0]},{pos[1]}): {maze[pos[0]][pos[1]]}")
        # print(f"N:{north} S:{south} E:{east} W:{west}")
        # print(f"N:{can_go_north} S:{can_go_south} E:{can_go_east} W:{can_go_west}")

        maze[pos[0]][pos[1]] = "."
        if can_go_north:
            pos = (pos[0] - 1, pos[1])
        elif can_go_south:
            pos = (pos[0] + 1, pos[1])
        elif can_go_east:
            pos = (pos[0], pos[1] + 1)
        else:
            pos = (pos[0], pos[1] - 1)

        steps += 1

        if not (can_go_north or can_go_south or can_go_east or can_go_west):
            ic(maze)
            # ic(maze[pos[0]][pos[1]])
            print(f"({pos[0]},{pos[1]}): {maze[pos[0]][pos[1]]}")
            print(f"N:{north} S:{south} E:{east} W:{west}")
            print(f"N:{can_go_north} S:{can_go_south} E:{can_go_east} W:{can_go_west}")
            raise SystemExit


def find_interior_spaces(lines: List[str]) -> int:
    width = len(lines[0])
    data = ''.join(lines)

    dmap = {
        'S': [],
        '|': [width, -width],
        '-': [-1, 1],
        '.': [],
        '7': [-1, width],
        'L': [1, -width],
        'J': [-1, -width],
        'F': [1, width]
    }

    start = data.find('S')
    path = {start}
    data = [dmap[c] for c in data]

    for i, offsets in enumerate(data):
        if start in (i + o for o in offsets):
            dmap['S'].append(i - start)

    dist = 0
    new = None
    while 1:
        new2 = new
        new = set()
        for p in (new2 or path):
            for offset in data[p]:
                if p + offset not in path:
                    new.add(p + offset)

        if new:
            path |= new
            dist += 1
        else:
            break

    # print('Part 1:', dist)

    inside = 0
    for i in range(len(data)):
        if i in path:
            continue
        outside_right = outside_left = True
        j = i
        while j > 0:
            if j in path and 1 in data[j]:
                outside_right = not outside_right
            if j in path and -1 in data[j]:
                outside_left = not outside_left
            j -= width

        if not (outside_right or outside_left):
            inside += 1

    return inside


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2023" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input[0]
    maze = parse_input(input_data)
    print(f"Step 1: Farthest distance {navigate(maze)}")  # 7086
    print(f"Step 2: Interior {find_interior_spaces(input_data.split()):,}")  # 317
