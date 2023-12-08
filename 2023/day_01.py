from pathlib import Path
from typing import List

Sample_Input = [
    """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""",
    """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
]


def parse_input(input: str) -> List[str]:
    return input.splitlines()


def calibration_value(lines: List[str]) -> int:
    digits = 0
    for line in lines:
        nums = []
        for char in line:
            if char.isnumeric():
                nums.append(char)
        digits += int(nums[0] + nums[-1])
    return digits


def fix_calibration_value(lines: List[str]) -> List[str]:
    new_lines = []
    for line in lines:
        line = line.replace("zero", "z0o")
        line = line.replace("one", "o1e")
        line = line.replace("two", "t2o")
        line = line.replace("three", "t3e")
        line = line.replace("four", "f4r")
        line = line.replace("five", "f5e")
        line = line.replace("six", "s6x")
        line = line.replace("seven", "s7n")
        line = line.replace("eight", "e8t")
        line = line.replace("nine", "n9e")
        new_lines.append(line)

    return new_lines


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2023" / f"{Path(__file__).stem}_input.txt").read_text()
    input_data = Sample_Input[0]
    lines = parse_input(input_data)
    print(f"Step 1: Calibration Value is {calibration_value(lines):,}")
    input_data = Sample_Input[1]
    lines = parse_input(input_data)
    print(f"Step 2: Fixed calibration: {calibration_value(fix_calibration_value(lines)):,}")
