from pathlib import Path
from typing import List
from functools import reduce
from operator import mul

Sample_Input = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


SYMBOLS = set([c for c in "#$%&*+-/=@"])


def parse_input(input: str) -> List:
    return input.splitlines()


def find_all_chars(input):
    text = input.replace("\n", "")
    return "".join(sorted(list(set(text))))


def step_through_rows(lines: List[str]) -> int:
    total = 0

    for row, line in enumerate(lines):
        start_idx, end_idx = None, None
        num = ""
        for col, char in enumerate(line):
            if char.isnumeric():
                if num == "":
                    start_idx = col
                num += char
            elif num != "":
                end_idx = col - 1

            if end_idx or (col == len(line) - 1 and num):
                end_idx = col - 1
                number = int(num)

                is_engine_part = False

                # look for symbol
                if row > 0:  # look above
                    for top in lines[row - 1][max(start_idx - 1, 0) : min(end_idx + 2, len(line) + 1)]:
                        if set(top) & SYMBOLS:
                            is_engine_part = True
                            break
                if row < len(lines) - 1:  # Look below
                    for floor in lines[row + 1][max(start_idx - 1, 0) : min(end_idx + 2, len(line) + 1)]:
                        if set(floor) & SYMBOLS:
                            is_engine_part = True
                            break
                if start_idx > 0:  # look left
                    if line[start_idx - 1] in SYMBOLS:
                        is_engine_part = True

                if end_idx < len(line) - 1:  # look right
                    if line[end_idx + 1] in SYMBOLS:
                        is_engine_part = True

                if is_engine_part:
                    # print(f"{number} found at {row},{start_idx}-{end_idx} is a part!")
                    total += number

                # Reset vars
                num = ""
                start_idx, end_idx = None, None

    return total


def find_gear_ratio(lines: List[str]) -> int:
    gears = []
    numbers = []

    for row, line in enumerate(lines):
        start_idx, end_idx = None, None
        num = ""
        for col, char in enumerate(line):
            if char == "*":
                gears.append((row, col))

            if char.isnumeric():
                if num == "":
                    start_idx = col
                num += char
            elif num != "":
                end_idx = col - 1

            if end_idx or (col == len(line) - 1 and num):
                end_idx = col - 1
                number = int(num)
                numbers.append((number, row, start_idx, end_idx))
                # Reset vars
                num = ""
                start_idx, end_idx = None, None

    # print(f"Gears: {gears}")
    # print(f"Numbers: {numbers}")

    total = 0

    for gear in gears:
        # print(f"Gear: {gear}")
        hits = []
        width = list(range(max(gear[1] - 1, 0), min(gear[1] + 2, len(line) + 1)))
        height = list(range(max(gear[0] - 1, 0), min(gear[0] + 2, len(lines) + 1)))

        for number in numbers:
            # print(f"Number: {number}")
            # print(f"Height: {height[0]}-{height[-1]} Width: {width[0]}-{width[-1]}")
            if (number[1] in height) and set([x for x in range(number[2], number[3] + 1)]) & set(width):
                hits.append(number)

        if len(hits) > 1:
            ratio = reduce(mul, [n[0] for n in hits])
            total += ratio
    return total


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2023" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    # print(f"List of characters in input: {find_all_chars(input_data)}")
    lines = parse_input(input_data)
    print(f"Step 1: Sum is {step_through_rows(lines):,}")  # 556,367
    print(f"Step 2: Ratio is {find_gear_ratio(lines):,}")  # 89,471,771
