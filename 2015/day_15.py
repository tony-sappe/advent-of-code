import re

from pathlib import Path
from typing import Dict
from itertools import product

Sample_Input = """\
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""


def parse_input(input: str) -> Dict[str, Dict[str, int]]:
    lines = input.splitlines()
    ingredients = {}
    regex = re.compile(r"(\S*): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)")
    for line in lines:
        r = regex.search(line)
        ingredients[r.group(1)] = {
            "capacity": int(r.group(2)),
            "durability": int(r.group(3)),
            "flavor": int(r.group(4)),
            "texture": int(r.group(5)),
            "calories": int(r.group(6)),
            "tsp": 0,
        }
    return ingredients


def brute_force(ingredients: Dict[str, Dict[str, int]], vol: int, count_calories: bool) -> int:
    max_score = 0

    for p in product(range(vol + 1), repeat=len(ingredients)):
        if sum(p) != 100:
            continue

        for i, v in enumerate(ingredients.values()):
            v["tsp"] = p[i]

        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        calories = 0
        for v in ingredients.values():
            capacity += v["capacity"] * v["tsp"]
            durability += v["durability"] * v["tsp"]
            flavor += v["flavor"] * v["tsp"]
            texture += v["texture"] * v["tsp"]
            calories += v["calories"] * v["tsp"]

        if count_calories and calories != 500:
            continue
        score = max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0)
        max_score = max(score, max_score)

    return max_score


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    ingredients = parse_input(input_data)
    # ic(ingredients)
    print(f"Part 1: highest score {brute_force(ingredients, 100, False)}")  # 13882464
    print(f"Part 2: highest score {brute_force(ingredients, 100, True)}")  # 11171160
