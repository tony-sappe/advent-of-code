from pathlib import Path
from copy import copy

Sample_Input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


def parse_input(input: str) -> str:
    structure = root = {}
    path = []
    for line in input.splitlines():
        if line.startswith("$"):
            if line[2:4] == "cd":
                if line[5:] == "/":
                    structure = root
                    path = []
                elif ".." in line:
                    structure = path.pop()
                else:
                    if line[5:] not in structure:
                        structure[line[5:]] = {}
                    path.append(structure)
                    structure = structure[line[5:]]
        else:
            x, y = line.split()
            if x == "dir":
                if y not in structure:
                    structure[y] = {}
            else:
                structure[y] = int(x)

    return root


def find_freeable_space(system) -> int:
    if isinstance(system, int):
        return (system, 0)
    size = 0
    ans = 0
    for child in system.values():
        s, a = find_freeable_space(child)
        size += s
        ans += a
    if size <= 100000:
        ans += size
    return (size, ans)


def dir_size(system) -> int:
    if isinstance(system, int):
        return system
    return sum(map(dir_size, system.values()))


def find_best_dir(dir):
    ans = float("inf")
    if dir_size(dir) >= space_required:
        ans = dir_size(dir)
    for child in dir.values():
        if isinstance(child, int):
            continue
        children_size = find_best_dir(child)
        ans = min(ans, children_size)
    return ans


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2022" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    file_system = parse_input(input_data)
    # print(file_system)
    print(f"Step 1: Contingent Freeable Space: {find_freeable_space(file_system)[1]:,}")  # 1,453,349
    space_required = dir_size(file_system) - 40_000_000
    print(f"Step 2: The optimal folder to delete recovers {find_best_dir(file_system)}")  # 2948823
