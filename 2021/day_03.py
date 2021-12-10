from pathlib import Path
from typing import Iterable

Sample_Input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def parse_diagnostics(input: Iterable[str]) -> int:
    """Part 1"""
    transpose = [[input[j][i] for j in range(len(input))] for i in range(len(input[0]))]
    half = len(input) / 2
    gamma_rate = int("".join(("0", "1")[sum(map(int, record)) >= half] for record in transpose), 2)
    epsilon_rate = int("".join(("0", "1")[sum(map(int, record)) <= half] for record in transpose), 2)

    print(f"Gamma Rate: {gamma_rate:,} | Epsilon Rate: {epsilon_rate:,}")
    return gamma_rate * epsilon_rate


def parse_additional_diagnostics(input: Iterable[str]) -> int:
    """Part 2"""
    o2_bin = []
    co2_bin = []

    while len(o2_bin) < len(input[0]):
        input_subset = [line for line in input if line.startswith("".join(o2_bin))]
        if len(input_subset) == 1:
            o2_bin = input_subset[0].split()
            break
        half = len(input_subset) / 2
        if sum([int(line[len(o2_bin)]) for line in input_subset]) >= half:
            o2_bin.append("1")
        else:
            o2_bin.append("0")

    while len(co2_bin) < len(input[0]):
        input_subset = [line for line in input if line.startswith("".join(co2_bin))]
        if len(input_subset) == 1:
            co2_bin = input_subset[0].split()
            break
        half = len(input_subset) / 2
        if sum([int(line[len(co2_bin)]) for line in input_subset]) < half:
            co2_bin.append("1")
        else:
            co2_bin.append("0")

    print(f"O2: {o2_bin} | CO2: {co2_bin}")
    o2 = int("".join(o2_bin), 2)
    co2 = int("".join(co2_bin), 2)
    print(f"Oxygen Generator Rating: {o2:,} | Carbon Dioxide Rating: {co2:,}")
    return o2 * co2


if __name__ == "__main__":
    report = (Path.cwd() / "2021" / "data" / "day_03_input.txt").read_text().splitlines()

    print(f"Diagnostic Report {parse_diagnostics(report):,}")
    print(f"Advanced Diagnostic Report {parse_additional_diagnostics(report):,}")
