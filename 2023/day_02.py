import re

from functools import reduce
from operator import mul
from pathlib import Path
from typing import Dict, List

Sample_Input = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def parse_input(input: str) -> Dict[int, List[Dict[str, int]]]:
    games = {}
    lines = input.splitlines()
    for line in lines:
        game_num = int(re.search(r"Game (\d+)", line).group(1))
        sets_list = line.split(";")
        games[game_num] = []
        for s in sets_list:
            colors = re.findall(r"(\d+) (\w+)", s)
            games[game_num].append({color: int(count) for count, color in colors})

    return games


def count_games(games: Dict[int, List[Dict[str, int]]]) -> int:
    bag = {"red": 12, "green": 13, "blue": 14}

    total = 0
    for game, sets in games.items():
        all_sets_ok = True
        for s in sets:
            if s.get("red", 0) > bag["red"] or s.get("green", 0) > bag["green"] or s.get("blue", 0) > bag["blue"]:
                all_sets_ok = False
        if all_sets_ok:
            # print(f"Game #{game} fits!")
            total += game

    return total


def calculate_minimums(game: List[Dict[str, int]]) -> Dict[str, int]:
    colors = {}
    for s in game:
        for color, count in s.items():
            if color not in colors:
                colors[color] = count
            elif count > colors[color]:
                colors[color] = count
    return colors


def calculate_powers(games: Dict[int, List[Dict[str, int]]]) -> int:
    return [reduce(mul, calculate_minimums(game).values()) for game in games.values()]


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2023" / f"{Path(__file__).stem}_input.txt").read_text()
    input_data = Sample_Input
    games = parse_input(input_data)
    print(f"Step 1: Sum is {count_games(games):,}")  # 2,617
    print(f"Step 2: Power is {sum(calculate_powers(games)):,}")  # 59,795
