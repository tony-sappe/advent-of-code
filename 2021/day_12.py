from pathlib import Path
from typing import Dict, Iterable, List

Sample_Input_1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

Sample_Input_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

Sample_Input_3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""


def parse_input(input: str) -> Iterable[str]:
    return input.strip().split("\n")


def generate_valid_paths(lines: Iterable[str]) -> List[str]:
    network = create_cave_network(lines)
    return explore_cave(network, "start", "end", [], False)


def generate_valid_paths_2(lines: Iterable[str]) -> List[str]:
    network = create_cave_network(lines)
    return explore_cave(network, "start", "end", [], True)


def explore_cave(
    network: Dict[str, List[str]], start: str, end: str, path: Iterable[str], allow_twice: bool
) -> List[List[str]]:

    path = path + [start]
    if start == end:
        return [path]
    if start not in network:
        return []

    for p in path:
        if p == p.lower() and path.count(p) >= 2:
            allow_twice = False

    paths = []
    for node in network[start]:
        if node == "start" or (node in path and node == node.lower() and not allow_twice):
            continue

        new_paths = explore_cave(network, node, end, path, allow_twice)
        for new_path in new_paths:
            paths.append(new_path)

    return paths


def create_cave_network(lines: Iterable[str]) -> Dict[str, List[str]]:
    network = {}
    for line in lines:
        start, dest = line.split("-")
        if start not in network:
            network[start] = []
        if dest not in network:
            network[dest] = []
        network[start].append(dest)
        network[dest].append(start)

    return network


if __name__ == "__main__":
    input_data = (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    lines = parse_input(input_data)

    paths = generate_valid_paths(lines)
    print(f"{len(paths):,} Paths found in cavern system")

    paths = generate_valid_paths_2(lines)
    print(f"Paths found with 1 repeat: {len(paths):,}")
