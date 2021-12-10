from pathlib import Path


def parse_movement(input):
    horizontal = 0
    depth = 0
    aim = 0

    for move in input:
        if move.startswith("forward"):
            x_units = int(move.split(" ")[1])
            horizontal += x_units
            depth += aim * x_units
        elif move.startswith("down"):
            aim += int(move.split(" ")[1])
        else:  # "up"
            aim -= int(move.split(" ")[1])

    return horizontal * depth


if __name__ == "__main__":
    course = Path("day_02_input.txt").read_text().splitlines()

    print(f"Submarine traveled  {parse_movement(course):,} on course.")
