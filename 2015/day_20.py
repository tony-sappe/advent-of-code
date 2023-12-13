import math

from pathlib import Path
from typing import List, Tuple


def parse_input(input: str) -> Tuple[str, List[List[str]]]:
    translators, start = input.split("\n\n")
    translations = [s.split(" => ") for s in translators.split("\n")]

    return start.strip(), translations


def aliquot_sieve(limit, target_presents, num_presents=10, quota=None):
    houses = [address * num_presents for address in range(limit + 1)]
    candidates = set([])
    for elf in range(2, len(houses)):
        bound = min(limit, elf * quota) if quota else limit
        for address in range(elf * 2, bound + 1, elf):
            houses[address] += num_presents * elf
            if houses[address] >= target_presents:
                candidates.add(address)
    return min(candidates)


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if (i * i) != n:
                large_divisors.append(n / i)
    # for divisor in large_divisors:
    for divisor in reversed(large_divisors):
        yield divisor


def new_house(limit: int, target_presents: int):
    n = limit
    max_houses = 50
    while True:
        presents = 0
        # d = divisors(n)
        # d[::-1]:
        for i in divisorGenerator(n):
            if i * max_houses > n:
                presents += i * 11
            else:
                break
        if presents > target_presents:
            return n
        else:
            n += 1


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    target = int(input_data.strip())
    # ic(translations)
    print(f"Part 1: First house {aliquot_sieve(1_000_000, target)}")  #
    print(f"Part 2: First house {new_house(5800, target)}")  #
