from collections import deque, Counter
from itertools import combinations, starmap
from pathlib import Path
from typing import List

Sample_Input = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14
"""


def parse_input(input: str) -> List[int]:
    scanners = []
    beacon_list = []
    for line in input.splitlines():
        if line.startswith("---"):
            continue
        elif line == "":
            scanners.append(beacon_list)
            beacon_list = []
        else:
            beacon_list.append(tuple(map(int, line.split(","))))

    scanners.append(beacon_list)
    return scanners


def rotx(x, y, z):
    return x, -z, y


def rotz(x, y, z):
    return -y, x, z


ALL_ROTATIONS = (
    rotz,
    rotz,
    rotz,
    rotx,
    rotz,
    rotz,
    rotz,
    rotx,
    rotz,
    rotz,
    rotz,
    lambda x, y, z: (-x, -z, -y),
    rotz,
    rotz,
    rotz,
    rotx,
    rotz,
    rotz,
    rotz,
    lambda x, y, z: (x, z, -y),
    rotz,
    rotz,
    rotz,
)


def rotations(scan):
    yield scan
    for rot in ALL_ROTATIONS:
        scan = list(starmap(rot, scan))
        yield scan


def move(scan, dx, dy, dz):
    return [(x + dx, y + dy, z + dz) for x, y, z in scan]


def find_scanner(base, rotated_scans):
    for scan in rotated_scans:
        [(diff, count)] = Counter(
            (x2 - x1, y2 - y1, z2 - z1) for x1, y1, z1 in scan for x2, y2, z2 in base
        ).most_common(1)
        if count >= 12:
            return diff, move(scan, *diff)
    return None, None


def join(scans):
    joined = set(scans[0])
    remaining = deque(list(rotations(scan)) for scan in scans)
    scanners = [(0, 0, 0)]

    while remaining:
        rotated_scans = remaining.popleft()
        scanner, moved = find_scanner(joined, rotated_scans)
        if scanner:
            joined |= set(moved)
            scanners.append(scanner)
        else:
            remaining.append(rotated_scans)

    return joined, scanners


def max_distance(scanners):
    return max(abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1) for (x1, y1, z1), (x2, y2, z2) in combinations(scanners, 2))


def positioning_calculations(scanner_feed):
    joined, scanners = join(scanner_feed)
    return len(joined), max_distance(scanners)


if __name__ == "__main__":
    input_data = (Path.cwd() / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    scanner_feed = parse_input(input_data)
    beacon_count, distance = positioning_calculations(scanner_feed)
    print(f"Step 1: Based on scanner reports, the number of beacons is: {beacon_count:,}")
    print(f"Step 2: Largest Manhattan distance between any two scanners: {distance:,}")
