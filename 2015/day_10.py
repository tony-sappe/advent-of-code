import re

from pathlib import Path
from itertools import groupby

Sample_Input = [
    "1",  # -> 11 (1 copy of digit 1).
    "11",  # -> 21 (2 copies of digit 1).
    "21",  # -> 1211 (one 2 followed by one 1).
    "1211",  # -> 111221 (one 1, one 2, and two 1s).
    "111221",  # -> 312211 (three 1s, two 2s, and one 1)
]


def iterations(line: str, count: int) -> str:
    for _ in range(count):
        line = ''.join([str(len(list(g))) + str(k) for k, g in groupby(line)])
    return line


def re_iterations(line: str, count: int) -> str:
    re_d = re.compile(r"((\d)\2*)")

    def replace(match_obj):
        s = match_obj.group(1)
        return str(len(s)) + s[0]

    for i in range(count):
        line = re_d.sub(replace, line)
    return line


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input[3]
    print(f"Step 1: Transformation: {len(iterations(input_data.strip(), 40))}")  # 252594
    print(f"Step 2: Transformation: {len(iterations(input_data.strip(), 50))}")  # 3579328
