from pathlib import Path
from icecream import ic
from typing import Dict

Sample_Input = """\
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""


def parse_input(input: str) -> Dict:
    calc = {}
    commands = input.splitlines()
    for command in commands:
        (ops, res) = command.split("->")
        calc[res.strip()] = ops.strip().split(" ")
    return calc


def calculate(wire):
    try:
        return int(wire)
    except ValueError:
        pass

    if wire not in results:
        ops = instructions[wire]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if op == "NOT":
                res = ~calculate(ops[1]) & 0xFFFF
            else:
                res = MAP[op](calculate(ops[0]), calculate(ops[2]))
        results[wire] = res
    return results[wire]


MAP = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "RSHIFT": lambda x, y: x >> y,
    "LSHIFT": lambda x, y: x << y,
}

if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    instructions = parse_input(input_data)
    results = {}
    print(f"Step 1: Value of 'a' {calculate('a'):,}")  # 3,176
    instructions["b"] = ["3176"]  # Replace the input on wire `b` withe the results of part 1
    results = {}  # "reset" the calculated values
    print(f"Step 2: Value of 'a' {calculate('a'):,}")  # 14,710
