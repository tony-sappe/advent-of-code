from pathlib import Path

Sample_Input = """\
((
"""


def part_1(input: str) -> int:
    print(input.count("("))
    print(input.count(")"))
    return input.count("(") - input.count(")")


def part_2(input: str) -> int:
    floor = 1
    for i, c in enumerate(input):
        if c == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i


if __name__ == "__main__":
    input_data = (Path.cwd() / "2015" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input[0]
    print(f"Step 1: Floor {part_1(input_data):,}")  # 74
    print(f"Step 2: Step {part_2(input_data):,}")  # 1,795
