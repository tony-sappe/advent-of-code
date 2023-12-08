from more_itertools import pairwise
from pathlib import Path
from typing import Any, Iterable, List, Tuple

Sample_Input = """199
200
208
210
200
207
240
269
260
263
"""


def parse_input(input: str) -> List[int]:
    return list(map(int, (input.splitlines())))


def sonar_scan(sonar_sweep: Iterable[int]) -> int:
    previous = sonar_sweep[0]
    count = 0
    for reading in sonar_sweep[1:]:
        if reading > previous:
            count += 1
        previous = reading
    return count


def triplewise(iterable: Iterable[Any]) -> Tuple[Any, Any, Any]:
    "Return overlapping triplets from an iterable"
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


def sonar_scan_triplets(sonar_sweep: Iterable[int]) -> int:
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
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2021" / f"{Path(__file__).stem}_input.txt").read_text()
    sonar_sweep = parse_input(input_data)
    print(f"Step 1: Sonar report contained {sonar_scan(sonar_sweep):,} (single-measure) increases.")
    print(f"Step 2: Sonar report contained {sonar_scan_triplets(sonar_sweep):,} (three-measure) increases.")
