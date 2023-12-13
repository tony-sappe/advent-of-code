from pathlib import Path
from typing import Dict
from copy import deepcopy

Sample_Input = """\
Hit Points: 12
Damage: 7
Armor: 2
"""

WEAPONS = {
    "Dagger": {"cost": 8, "damage": 4, "armor": 0},
    "Shortsword": {"cost": 10, "damage": 5, "armor": 0},
    "Warhammer": {"cost": 25, "damage": 6, "armor": 0},
    "Longsword": {"cost": 40, "damage": 7, "armor": 0},
    "Greataxe": {"cost": 74, "damage": 8, "armor": 0},
}
ARMOR = {
    "Leather": {"cost": 13, "damage": 0, "armor": 1},
    "Chainmail": {"cost": 31, "damage": 0, "armor": 2},
    "Splintmail": {"cost": 53, "damage": 0, "armor": 3},
    "Bandedmail": {"cost": 75, "damage": 0, "armor": 4},
    "Platemail": {"cost": 102, "damage": 0, "armor": 5},
    "": {"cost": 0, "damage": 0, "armor": 0},
}
RINGS = {
    "Damage +1": {"cost": 25, "damage": 1, "armor": 0},
    "Damage +2": {"cost": 50, "damage": 2, "armor": 0},
    "Damage +3": {"cost": 100, "damage": 3, "armor": 0},
    "Defense +1": {"cost": 20, "damage": 0, "armor": 1},
    "Defense +2": {"cost": 40, "damage": 0, "armor": 2},
    "Defense +3": {"cost": 80, "damage": 0, "armor": 3},
    "": {"cost": 0, "damage": 0, "armor": 0},
}


def parse_input(input: str) -> Dict[str, int]:
    lines = input.splitlines()
    stats = {}
    for line in lines:
        k, v = line.split(":")
        stats[k.strip()] = int(v.strip())

    return stats


def defeated_boss(boss: Dict[str, int], player: Dict[str, int]) -> bool:
    player_attack = max(player["Damage"] - boss["Armor"], 1)
    boss_attack = max(boss["Damage"] - player["Armor"], 1)

    return (boss["Hit Points"] * 1.0 / player_attack) <= (player["Hit Points"] * 1.0 / boss_attack)


def frugal_player_equipment(boss: Dict[str, int], player_hit_points: int) -> int:
    winning_costs = set()
    for kw, vw in WEAPONS.items():
        for ka, va in ARMOR.items():
            for kr, vr in RINGS.items():
                for kr2, vr2 in RINGS.items():
                    if kr == kr2:
                        continue
                    player = {
                        "Hit Points": player_hit_points,
                        "Damage": vw["damage"] + va["damage"] + vr["damage"] + vr2["damage"],
                        "Armor": vw["armor"] + va["armor"] + vr["armor"] + vr2["armor"],
                    }
                    if defeated_boss(deepcopy(boss), player):
                        # print(f'{kw} {ka} {kr} {kr2}: Cost {vw["cost"] + va["cost"] + vr["cost"] + vr2["cost"]}')
                        # print(player)
                        winning_costs.add(vw["cost"] + va["cost"] + vr["cost"] + vr2["cost"])

    return min(winning_costs)


def gullible_player_equipment(boss: Dict[str, int], player_hit_points: int) -> int:
    losing_costs = set()
    for kw, vw in WEAPONS.items():
        for ka, va in ARMOR.items():
            for kr, vr in RINGS.items():
                for kr2, vr2 in RINGS.items():
                    if kr == kr2:
                        continue
                    player = {
                        "Hit Points": player_hit_points,
                        "Damage": vw["damage"] + va["damage"] + vr["damage"] + vr2["damage"],
                        "Armor": vw["armor"] + va["armor"] + vr["armor"] + vr2["armor"],
                    }
                    if not defeated_boss(deepcopy(boss), player):
                        # print(f'{kw} | {ka} | {kr} | {kr2}: Cost {vw["cost"] + va["cost"] + vr["cost"] + vr2["cost"]}')
                        # print(player)
                        losing_costs.add(vw["cost"] + va["cost"] + vr["cost"] + vr2["cost"])

    return max(losing_costs)


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    boss = parse_input(input_data)
    print(f"Part 1: Cheapest victory {frugal_player_equipment(boss, 100)}")  # 111
    print(f"Part 2: Expensive loss {gullible_player_equipment(boss, 100)}")  # 188
