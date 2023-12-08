import numpy as np

from collections import Counter
from pathlib import Path
from typing import Iterable, List

Sample_Input = """3,4,3,1,2
"""


def parse_input(input: str) -> tuple:
    lines = input.strip().split(",")
    return list(map(int, lines))


def simulate(fish: Iterable[int], days: int) -> int:
    """Don't brute force it, use math

    Resources
        https://numpy.org/doc/stable/reference/routines.linalg.html
        https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_power.html#numpy.linalg.matrix_power
    """
    cache = Counter(fish)
    init = np.array([cache[i] for i in range(9)])
    A = np.array(
        [
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    B = np.linalg.matrix_power(A, days)
    return B.dot(init).sum()


def brute_force_simulate(fish: Iterable[int], days: int) -> int:
    d = np.array(fish)
    for _ in range(days):
        d = brute_force_simulate_one_day(d)
    return d


def brute_force_simulate_one_day(fish: Iterable[int]) -> List[int]:
    new_fish = fish.size - np.count_nonzero(fish)
    fish[fish == 0] = 7
    fish = np.subtract(fish, 1)
    fish = np.append(fish, [8] * new_fish)

    return fish


if __name__ == "__main__":

    fish_input = (Path.cwd().parent / "advent-of-code-data" / "2021" / f"{Path(__file__).stem}_input.txt").read_text()
    initial_fish = parse_input(fish_input)

    print("========= NEW ============")
    days = 18
    simulated_fish = simulate(list(initial_fish), days=days)
    print(f"Starting with {len(initial_fish):,} fish, after {days} days the projection is {simulated_fish:,}")

    days = 256
    simulated_fish = simulate(list(initial_fish), days=days)
    print(f"Starting with {len(initial_fish):,} fish, after {days} days the projection is {simulated_fish:,}")
