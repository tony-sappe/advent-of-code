from pathlib import Path
from icecream import ic
from typing import List

Sample_Input = """\
2x3x4
1x1x10
"""  # LxWxH


def parse_input(input: str) -> int:
    return [[int(side) for side in line.split("x")] for line in input.splitlines()]


def wrap_box(dims: List[int]) -> int:
    l, w, h = dims
    a, b, _ = sorted(dims)
    total = 2 * l * w + 2 * w * h + 2 * h * l + a * b  # 2*l*w + 2*w*h + 2*h*l + "extra: (a + b)""
    return total


def wrap_boxes(boxes: List[int]) -> int:
    return sum([wrap_box(b) for b in boxes])


def ribbon(boxes: List[int]) -> int:
    feet = 0
    for l, w, h in boxes:
        a, b, _ = sorted([l, w, h])
        feet += l * w * h + a * 2 + b * 2
    return feet


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    boxes = parse_input(input_data)
    print(f"Step 1: Total square feet: {wrap_boxes(boxes):,}")  # 1,588,178
    print(f"Step 2: Total ribbon feet: {ribbon(boxes):,}")  # 3,783,758
