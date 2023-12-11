import re

from pathlib import Path
from typing import Dict, Any

Sample_Input = """\
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""


def parse_input(input: str) -> Dict:
    lines = input.splitlines()
    reindeer = {}
    regex = re.compile(r"(\S*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.")
    for line in lines:
        r = regex.search(line)
        reindeer[r.group(1)] = {
            "speed": int(r.group(2)),
            "flight-time": int(r.group(3)),
            "rest-time": int(r.group(4)),
            "points": 0,
            "distance": 0,
        }
        reindeer[r.group(1)]["full-flight"] = reindeer[r.group(1)]["speed"] * reindeer[r.group(1)]["flight-time"]
        reindeer[r.group(1)]["cycle"] = reindeer[r.group(1)]["flight-time"] + reindeer[r.group(1)]["rest-time"]
    return reindeer


def travel(reindeer: Dict[str, Any], time: int) -> int:
    distance = (time // reindeer["cycle"]) * reindeer["full-flight"]
    extra = time % reindeer["cycle"]
    if extra > reindeer["flight-time"]:
        distance += reindeer["full-flight"]
    else:
        distance += reindeer["speed"] * extra
    return distance


def farthest_reindeer(reindeer: Dict[str, Dict[str, Any]], time: int) -> int:
    return max([travel(v, 2503) for k, v in reindeer.items()])


def points(reindeer: Dict[str, Dict[str, Any]], time: int) -> int:
    for s in range(time):
        for k, v in reindeer.items():
            if s % v["cycle"] < v["flight-time"]:
                v["distance"] += v["speed"]

        max_distance = 0
        for v in reindeer.values():
            if v["distance"] > max_distance:
                max_distance = v["distance"]

        farthest = max([v["distance"] for v in reindeer.values()])

        for k, v in reindeer.items():
            if v["distance"] == farthest:
                v["points"] += 1

    winner = sorted(reindeer.keys(), key=lambda k: reindeer[k]["points"])[-1]
    # print(f"{winner}: {reindeer[winner]}")
    return reindeer[winner]["points"]


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    reindeer = parse_input(input_data)
    print(f"Part 1: Farthest reindeer: {farthest_reindeer(reindeer, 2503)}")  # 2640
    print(f"Part 2: Highest earned points: {points(reindeer, 2503)}")  # 1102
