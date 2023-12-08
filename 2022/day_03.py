from pathlib import Path
from typing import Any, Iterable, List
from string import ascii_letters
from itertools import islice


Sample_Input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def parse_input(input: str) -> List[str]:
    return input.splitlines()


def calculate_priority(sack: str) -> int:
    g1, g2 = sack[: len(sack) // 2], sack[len(sack) // 2 :]
    character = (set(g1) & set(g2)).pop()
    return ascii_letters.rfind(character) + 1


def calculate_final_priority(sacks: Iterable[str]) -> int:
    return sum([calculate_priority(s) for s in sacks])


def calculate_badges(sacks: Iterable[str]) -> int:
    sum = 0
    for group in batched(sacks, 3):
        character = (set(group[0]) & set(group[1]) & set(group[2])).pop()
        sum += ascii_letters.rfind(character) + 1
    return sum


def batched(iterable: Iterable[Any], n: int) -> List[Any]:
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := list(islice(it, n)):
        yield batch


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2022" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    sacks = parse_input(input_data)
    print(f"Step 1: The Priority sum is {calculate_final_priority(sacks):,}")  # 8,202
    print(f"Step 2: The Badge sum is {calculate_badges(sacks):,}")  # 2,864
