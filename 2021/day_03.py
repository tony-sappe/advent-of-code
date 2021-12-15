from pathlib import Path
from typing import Iterable, List, Tuple

Sample_Input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


def parse_input(input: str) -> List[str]:
    return input.splitlines()


def gamma_and_epsilon_diagnostics(report: Iterable[str]) -> Tuple[int, int]:
    transpose = [[report[j][i] for j in range(len(report))] for i in range(len(report[0]))]
    half = len(report) / 2
    gamma_rate = int("".join(("0", "1")[sum(map(int, line)) >= half] for line in transpose), 2)
    epsilon_rate = int("".join(("0", "1")[sum(map(int, line)) <= half] for line in transpose), 2)

    return (gamma_rate, epsilon_rate)


def o2_and_co2_diagnostics(report: Iterable[str]) -> Tuple[int, int]:
    o2_bin = []
    co2_bin = []

    while len(o2_bin) < len(report[0]):
        input_subset = [line for line in report if line.startswith("".join(o2_bin))]
        if len(input_subset) == 1:
            o2_bin = input_subset[0].split()
            break
        half = len(input_subset) / 2
        if sum([int(line[len(o2_bin)]) for line in input_subset]) >= half:
            o2_bin.append("1")
        else:
            o2_bin.append("0")

    while len(co2_bin) < len(report[0]):
        input_subset = [line for line in report if line.startswith("".join(co2_bin))]
        if len(input_subset) == 1:
            co2_bin = input_subset[0].split()
            break
        half = len(input_subset) / 2
        if sum([int(line[len(co2_bin)]) for line in input_subset]) < half:
            co2_bin.append("1")
        else:
            co2_bin.append("0")

    return (int("".join(o2_bin), 2), int("".join(co2_bin), 2))


if __name__ == "__main__":
    input_data = (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    report = parse_input(input_data)

    gamma_rate, epsilon_rate = gamma_and_epsilon_diagnostics(report)
    power_rate = gamma_rate * epsilon_rate
    print(f"Step 1: Gamma Rate: {gamma_rate:,} | Epsilon Rate: {epsilon_rate:,} | Power Rate: {power_rate:,}")

    o2, co2 = o2_and_co2_diagnostics(report)
    life_support_rating = o2 * co2
    print(f"Step 2: O2 Generator Rating: {o2:,} | CO2 Rating: {co2:,} | Life Support Rating: {life_support_rating:,}")
