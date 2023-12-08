from pathlib import Path
from typing import Any, Iterable, List, Tuple

Sample_Input = """A Y
B X
C Z
"""


def parse_input(input: str) -> List[int]:
    return [tuple(line.split(" ")) for line in input.splitlines()]


def calculate_score(round: Tuple[str, str]) -> int:
    # A for Rock, B for Paper, and C for Scissors
    # X for Rock, Y for Paper, and Z for Scissors
    # Rock (1), Paper (2) Scissors (3)
    scores = {
        ("A", "X"): 1 + 3,
        ("A", "Y"): 2 + 6,
        ("A", "Z"): 3 + 0,
        ("B", "X"): 1 + 0,
        ("B", "Y"): 2 + 3,
        ("B", "Z"): 3 + 6,
        ("C", "X"): 1 + 6,
        ("C", "Y"): 2 + 0,
        ("C", "Z"): 3 + 3,
    }
    return scores[round]


def calculate_final_score(rounds: Iterable[Tuple[str, str]]) -> int:
    return sum([calculate_score(r) for r in rounds])


def strategy_score(round: Tuple[str, str]) -> int:
    # A for Rock, B for Paper, and C for Scissors
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
    # Rock (1), Paper (2) Scissors (3)

    scores = {
        ("A", "X"): 3 + 0,  # scissors
        ("A", "Y"): 1 + 3,  # rock
        ("A", "Z"): 2 + 6,  # paper
        ("B", "X"): 1 + 0,  # rock
        ("B", "Y"): 2 + 3,  # paper
        ("B", "Z"): 3 + 6,  # scissors
        ("C", "X"): 2 + 0,  # paper
        ("C", "Y"): 3 + 3,  # scissors
        ("C", "Z"): 1 + 6,  # rock
    }
    return scores[round]


def strategy_final_score(rounds: Iterable[Tuple[str, str]]) -> int:
    return sum([strategy_score(r) for r in rounds])


if __name__ == "__main__":
    input_data = (Path.cwd() / "2022" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    rounds = parse_input(input_data)
    print(f"Step 1: Your Score is {calculate_final_score(rounds):,}")  # 10,941
    print(f"Step 2: Your Score is {strategy_final_score(rounds):,}")
