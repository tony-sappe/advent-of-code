from pathlib import Path

Sample_Input = """\
""
"abc"
"aaa\"aaa"
"\x27"
"""


if __name__ == "__main__":
    with open(Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt") as file:
        part_1 = sum(len(s[:-1]) - len(eval(s)) for s in file)
    print(f"Step 1: Data size {part_1:,}")  # 1,342

    with open(Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt") as file:
        part_2 = sum(2 + s.count('\\') + s.count('"') for s in file)
    print(f"Step 2: Data size {part_2:,}")  # 2,074
