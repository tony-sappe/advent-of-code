from pathlib import Path


def parse_diagnostics(input):
    """ Part 1 """
    transpose = [[input[j][i] for j in range(len(input))] for i in range(len(input[0]))]
    half = len(input) / 2
    gamma_rate = int("".join(("0", "1")[sum(map(int, record)) >= half] for record in transpose), 2)
    epsilon_rate = int("".join(("0", "1")[sum(map(int, record)) <= half] for record in transpose), 2)

    print(f"Gamma Rate: {gamma_rate:,} | Epsilon Rate: {epsilon_rate:,}")
    return gamma_rate * epsilon_rate


def parse_additional_diagnostics(input):
    transpose = [[input[j][i] for j in range(len(input))] for i in range(len(input[0]))]
    half = len(input) / 2
    # o2 = int("".join(("0", "1")[sum(map(int, record)) >= half] for record in transpose), 2)
    # co2 = int("".join(("0", "1")[sum(map(int, record)) <= half] for record in transpose), 2)
    o2_bin = []
    co2_bin = []

    valid_readings = transpose
    i = 0
    while len(valid_readings) > 1:
        if sum(map(int, valid_readings[i])) >= half:
            o2_bin.append("1")
        else:
            o2_bin.append("0")

        valid_readings = trim_diagnostics(input, "".join(o2_bin))
        valid_readings = [[valid_readings[j][i] for j in range(len(valid_readings))] for i in range(len(valid_readings[0]))]
        print(f"O2: {o2_bin} | {valid_readings=}")

    valid_readings = transpose
    while len(valid_readings) > 1:
        if sum(map(int, valid_readings[0])) <= half:
            co2_bin.append("1")
        else:
            co2_bin.append("0")

        valid_readings = trim_diagnostics(input, "".join(co2_bin))
        valid_readings = [[valid_readings[j][i] for j in range(len(valid_readings))] for i in range(len(valid_readings[0]))]
        print(f"CO2: {co2_bin} | {valid_readings=}")

    print(f"O2: {o2_bin} | CO2: {co2_bin}")
    o2 = int("".join(o2_bin))
    co2 = int("".join(co2_bin))
    print(f"Oxygen Generator Rating: {o2:,} | Carbon Dioxide Rating: {co2:,}")
    return o2 * co2


def trim_diagnostics(input, match):
    return [line for line in input if line.startswith(match)]


if __name__ == "__main__":
    # Sample Input
    report = [
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
    # report = (Path.cwd() / "2021" / "data" / "day_03_input.txt").read_text().splitlines()

    print(f"Diagnostic Report {parse_diagnostics(report):,}")
    print(f"Advanced Diagnostic Report {parse_additional_diagnostics(report):,}")
