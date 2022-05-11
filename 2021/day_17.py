import re
from collections import namedtuple
from pathlib import Path
from typing import Tuple

Sample_Input = """target area: x=20..30, y=-10..-5
"""

Coord = namedtuple("Coord", "x,y")
Coord_Range = namedtuple("Coord_Range", "min,max")


def parse_input(input: str) -> Tuple[str, Tuple[int, int]]:
    matches = re.findall(r"(-?\d+)..(-?\d+)", input)
    x = Coord_Range(*sorted(map(int, matches[0])))
    y = Coord_Range(*sorted(map(int, matches[1])))
    return Coord(x, y)


def obtain_highest_elevation(start: Coord, target_area: Tuple[Coord_Range, Coord_Range]) -> int:
    """
    There are 2 key points to understand it (using test set, so y=-10..-5):

        n(n+1)/2 is the sum of numbers from 1 to n.
            So if you want to know the max height of y = 9 you simply do
            1+2+3+4+5+6+7+8+9 = 9(9+1)/2 = 45

        Now why n = -target_min_y -1 ?
            After we go up we'll back down at y=0 with a y velocity = -n-1. So
            -target_min_y -1 is the maximum value that after reach y=0 get in the
            range. With y = 9 we'll reach y = 0 with y velocity = -10. The next
            step we'll be at y=-10 that is in the range.
            Instead if we choose y = 10 we'll reach y=0 with y velocity = -11.
            The next step we'll be at y=-11 that is out of range.

    If the y-velocity is min_y (a negative number) at y = 0, it will
        ***hit the very bottom of the range it needs to hit.***
    Any more negative velocity and it will never hit that range. If the
    y-velocity starts at positive value v, it will reach y=0 again with velocity
    -(v+1). -(v+1)=min_y means v = -min_y - 1.
    """

    n = -target_area.y.min - 1
    return n * (n + 1) // 2


def find_every_initial_velocity(start: Coord, target_area: Tuple[Coord_Range, Coord_Range]) -> int:
    initial_velocities = set()
    y_maximum = max(abs(target_area.y.min), abs(target_area.y.max))
    for y in range(-y_maximum, y_maximum + 1):
        for x in range(0, target_area.x.max + 1):
            if lands_in_target(Coord(x, y), target_area):
                initial_velocities.add((x, y))

    return len(initial_velocities)


def lands_in_target(initial_velocity: Coord, target_area: Tuple[Coord_Range, Coord_Range]) -> bool:
    x, y = 0, 0
    vx, vy = initial_velocity
    while True:
        if (
            (x > target_area.x.max)
            or (vx == 0 and not target_area.x.min <= x <= target_area.x.max)
            or (vx == 0 and y < target_area.y.min)
        ):
            return False
        elif target_area.x.min <= x <= target_area.x.max and target_area.y.min <= y <= target_area.y.max:
            return True

        x += vx
        y += vy

        if vx > 0:
            vx -= 1
        vy -= 1


if __name__ == "__main__":
    input_data = (Path.cwd() / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    target_area = parse_input(input_data)
    start = Coord(0, 0)
    max_y = obtain_highest_elevation(start, target_area)
    print(f"Step 1: Highest Y value possible and still hitting target area: {max_y:,}")
    total_valid_velocities = find_every_initial_velocity(start, target_area)
    print(f"Step 2: Number of initial velocities hitting target area: {total_valid_velocities:,}")
