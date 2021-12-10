from pathlib import Path
from more_itertools import pairwise


def sonar_scan(sonar_sweep):
    previous = sonar_sweep[0]
    count = 0
    for reading in sonar_sweep[1:]:
        if reading > previous:
            count += 1
        previous = reading
    return count


def triplewise(iterable):
    "Return overlapping triplets from an iterable"
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


def sonar_scan_triplets(sonar_sweep):
    tuples = list(triplewise(sonar_sweep))
    previous = sum(tuples[0])
    count = 0
    for reading in tuples[1:]:
        new_reading = sum(reading)
        if new_reading > previous:
            count += 1
        previous = new_reading
    return count


if __name__ == "__main__":
    # Sample Code
    # sonar_sweep = [
    #     199,
    #     200,
    #     208,
    #     210,
    #     200,
    #     207,
    #     240,
    #     269,
    #     260,
    #     263,
    # ]
    sonar_sweep = list(map(int, (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text().splitlines()))
    print(f"Sonar report contained {sonar_scan(sonar_sweep):,} increases.")
