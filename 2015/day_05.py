from pathlib import Path
from icecream import ic
from typing import List, Callable

Sample_Input = """\
aei
xazegov
aeiouaeiouaeiou
ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy
"""


def parse_input(input: str) -> List[str]:
    return input.splitlines()


def is_nice_part1(string: str) -> bool:
    bad_list = ["ab", "cd", "pq", "xy"]
    for b in bad_list:
        if b in string:
            return False

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            break
    else:
        return False

    if sum([string.count(c) for c in "aeiou"]) < 3:
        return False

    return True


def contains_pair(string: str) -> int:
    for i in range(len(string) - 3):
        sub = string[i: i + 2]
        if sub in string[i + 2:]:
            return True

    return False


def is_nice_part2(string: str) -> bool:
    if not contains_pair(string):
        return False

    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            break
    else:
        return False

    return True


def are_nice(lines: List[str], func: Callable) -> int:
    return sum([func(l) for l in lines])


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    lines = parse_input(input_data)
    print(f"Step 1: Number is {are_nice(lines, is_nice_part1):,}")  # 255
    print(f"Step 2: Number is {are_nice(lines, is_nice_part2):,}")  # 55
