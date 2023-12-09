import re
import json

from pathlib import Path
from typing import Dict


def parse_input(input: str) -> Dict:
    return json.loads(input)


def regex_sum_numbers(string: str) -> int:
    return sum([int(d) for d in re.findall(r"(-?\d+)", string)])


def remove_red(d):
    if isinstance(d, int):
        return d
    if isinstance(d, list):
        return sum([remove_red(j) for j in d])
    if not isinstance(d, dict):
        return 0
    if "red" in d.values():
        return 0
    return remove_red(list(d.values()))


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input[1]
    data = parse_input(input_data)

    print(f"Step 1: sum: {regex_sum_numbers(input_data.strip())}")  # 111754
    print(f"Step 2: Transformation: {remove_red(data)}")  # 65402
