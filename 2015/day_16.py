import re
import operator

from pathlib import Path
from typing import Dict, Optional
from icecream import ic


MATCH = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse_input(input: str) -> Dict[int, Dict[str, int]]:
    aunts = {}
    regex = re.compile(r"(\S+): (\d+)")
    for i, line in enumerate(input.splitlines(), 1):
        aunt = {}
        for fact, val in regex.findall(line):
            aunt[fact] = int(val)
        aunts[i] = aunt
    return aunts


def find_match(aunts: Dict[int, Dict[str, int]]) -> Optional[int]:
    for aunt, facts in aunts.items():
        if all([MATCH[k] == v for k, v in facts.items()]):
            return aunt


def find_range_match(aunts: Dict[int, Dict[str, int]]) -> Optional[int]:
    ops = {
        "children": operator.eq,
        "cats": operator.gt,
        "samoyeds": operator.eq,
        "pomeranians": operator.lt,
        "akitas": operator.eq,
        "vizslas": operator.eq,
        "goldfish": operator.lt,
        "trees": operator.gt,
        "cars": operator.eq,
        "perfumes": operator.eq,
    }
    for aunt, facts in aunts.items():
        if all([ops[k](v, MATCH[k]) for k, v in facts.items()]):
            return aunt


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    aunts = parse_input(input_data)
    # ic(aunts)
    print(f"Part 1: Aunt {find_match(aunts)}")  # 40
    aunts = parse_input(input_data)
    print(f"Part 2: Aunt {find_range_match(aunts)}")  # 241
