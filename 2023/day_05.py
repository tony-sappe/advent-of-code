from icecream import ic
from pathlib import Path
from typing import Any, List, Tuple, Dict

Sample_Input = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
# dest, source, range


def parse_input(input: str) -> Tuple[List[int], List[Dict[int, Any]]]:
    lines = input.splitlines()
    _, seeds = lines[0].split(":")
    seeds = [int(s) for s in seeds.split(" ")[1:]]
    # ic(seeds)

    lines.append("")

    maps = []
    m = {}
    values = []
    for line in lines[2:]:
        if "map" in line:
            text = line.split(" ")[0]
            src, _, dst = text.split("-")
            # print(f"{src} -> {dst}")
        elif not line:
            m["values"] = values
            maps.append(m)
            m = {}
            values = []
        else:
            d, s, r = [int(x) for x in line.split(" ")]
            values.append({"start": s, "end": s + r, "trnsfrm": d - s})

    # ic(maps)
    return seeds, maps


def map_seeds_to_location(seeds: List[int], maps: List[Dict[int, Any]]) -> int:
    min_location = 1_000_000_000
    for seed in seeds:
        for m in maps:
            for val in m["values"]:
                if seed in range(val["start"], val["end"]):
                    seed += val["trnsfrm"]
                    break

        if seed < min_location:
            min_location = seed

    return min_location


class MapFunc:
    def __init__(self, mapping: List[Dict[str, int]]):
        self.tuples = [[m["trnsfrm"] + m["start"], m["start"], m["end"] - m["start"]] for m in mapping]

    def apply_range(self, ranges: List[Tuple[int]]) -> List[int]:
        answers = []
        for dest, src, sz in self.tuples:
            src_end = src + sz
            next_range = []
            while ranges:
                (st, ed) = ranges.pop()
                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    next_range.append(before)
                if inter[1] > inter[0]:
                    answers.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    next_range.append(after)
            ranges = next_range
        return answers + ranges


def map_seed_pairs_to_location(seeds: List[int], maps: List[Dict[int, Any]]) -> int:
    Fs = [MapFunc(s["values"]) for s in maps]

    locations = []
    pairs = list(zip(seeds[::2], seeds[1::2]))  # even seeds, odd seeds and zip together
    for st, sz in pairs:
        interval = [(st, st + sz)]
        for f in Fs:
            interval = f.apply_range(interval)
        locations.append(min(interval)[0])
    return min(locations)


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2023" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    seeds, maps = parse_input(input_data)
    print(f"Step 1: Lowest Location: {map_seeds_to_location(seeds, maps):,}")  # 662,197,086
    print(f"Step 2: Lowest Location: {map_seed_pairs_to_location(seeds, maps):,}")  # 52,510,809
