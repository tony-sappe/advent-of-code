import re

from pathlib import Path
from typing import Iterable, List, Tuple


Sample_Input = (
    "    [D]    \n"
    "[N] [C]    \n"
    "[Z] [M] [P]\n"
    " 1   2   3 \n"
    "\n"
    "move 1 from 2 to 1\n"
    "move 3 from 1 to 3\n"
    "move 2 from 2 to 1\n"
    "move 1 from 1 to 2\n"
)


def parse_input(
    input: str,
) -> Tuple[Tuple[List[str], List[str], List[str]], Iterable[Tuple[int, int, int]]]:

    stacks = ([], [], [], [], [], [], [], [], [])
    for row in input.splitlines()[0:8]:
        if row[1] != " ":
            stacks[0].append(row[1])
        if row[5] != " ":
            stacks[1].append(row[5])
        if row[9] != " ":
            stacks[2].append(row[9])
        if row[13] != " ":
            stacks[3].append(row[13])
        if row[17] != " ":
            stacks[4].append(row[17])
        if row[21] != " ":
            stacks[5].append(row[21])
        if row[25] != " ":
            stacks[6].append(row[25])
        if row[29] != " ":
            stacks[7].append(row[29])
        if row[33] != " ":
            stacks[8].append(row[33])

    stacks = tuple([list(reversed(stack)) for stack in stacks])

    regex = re.compile(r"move (\d*) from (\d*) to (\d*)")
    instructions = [
        (int(r.group(1)), int(r.group(2)) - 1, int(r.group(3)) - 1)
        for r in [regex.match(row) for row in input.splitlines()[10:]]
    ]
    return stacks, instructions


def parse_sample_input(
    input: str,
) -> Tuple[Tuple[List[str], List[str], List[str]], Iterable[Tuple[int, int, int]]]:

    stacks = ([], [], [])
    for row in input.splitlines()[0:3]:
        if row[1] != " ":
            stacks[0].append(row[1])
        if row[5] != " ":
            stacks[1].append(row[5])
        if row[9] != " ":
            stacks[2].append(row[9])

    stacks = tuple([list(reversed(stack)) for stack in stacks])
    regex = re.compile(r"move (\d*) from (\d*) to (\d*)")
    instructions = [
        (int(r.group(1)), int(r.group(2)) - 1, int(r.group(3)) - 1)
        for r in [regex.match(row) for row in input.splitlines()[5:]]
    ]
    return stacks, instructions


def complete_9000_operations(
    stacks: Tuple[List[str], List[str], List[str]], instructions: Iterable[Tuple[int, int, int]]
) -> Tuple[List[str], List[str], List[str]]:
    for instruction in instructions:
        for _ in range(instruction[0]):
            stacks[instruction[2]].append(stacks[instruction[1]].pop())
    return stacks


def complete_9001_operations(
    stacks: Tuple[List[str], List[str], List[str]], instructions: Iterable[Tuple[int, int, int]]
) -> Tuple[List[str], List[str], List[str]]:
    for instruction in instructions:
        stacks[instruction[2]].extend(stacks[instruction[1]][-1 * instruction[0]:])
        del stacks[instruction[1]][-1 * instruction[0]:]
    return stacks


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2022" / f"{Path(__file__).stem}_input.txt").read_text()
    stacks, instructions = parse_input(input_data)
    # input_data = Sample_Input
    # stacks, instructions = parse_sample_input(input_data)
    final_stacks = complete_9000_operations(stacks, instructions)
    print(f"Step 1: The top crates are {''.join(s[-1] for s in final_stacks)}")  # QPJPLMNNR
    # stacks, instructions = parse_sample_input(input_data)
    stacks, instructions = parse_input(input_data)
    final_stacks = complete_9001_operations(stacks, instructions)
    print(f"Step 2: The top crates are {''.join(s[-1] for s in final_stacks)}")  # BQDNWJPVJ
