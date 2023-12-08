from pathlib import Path
from typing import Iterable, List, Tuple, Optional

Sample_Input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""


def parse_input(input: str) -> tuple:
    lines = input.strip().split("\n")
    displays = [line.split(" | ")[0].split(" ") for line in lines]
    outputs = [line.split(" | ")[1].split(" ") for line in lines]
    return displays, outputs


def guess_number(segment: str) -> Optional[int]:
    length = len(segment)
    if length == 2:
        return 1
    elif length == 3:
        return 7
    elif length == 4:
        return 4
    elif length == 7:
        return 8
    else:
        return None


def count_easy_numbers(readings: str) -> int:
    return sum([1 for segments in readings for segment in segments if guess_number(segment) in (1, 4, 7, 8)])


def get_frequencies(config):
    letters = ["a", "b", "c", "d", "e", "f", "g"]
    return {letter: str(config.count(letter)) for letter in list(letters)}


def get_numeric_representation(frequencies, config_word):
    return int("".join(sorted([frequencies[letter] for letter in list(config_word)])))


def sort_letters(word):
    word = list(word)
    word.sort()
    return "".join(word)


def deduce_crossed_wires(input_data):
    displays = [[part for part in line.split(" | ")] for line in input_data.strip().split("\n")]

    digits_representation = "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg"  # 0 - 9
    digit_frequency = get_frequencies(digits_representation)
    digits_value = {}

    for i, digit_representation in enumerate(digits_representation.split(" ")):
        numeric_reppresentation = get_numeric_representation(digit_frequency, digit_representation)
        digits_value[numeric_reppresentation] = str(i)

    digits = []
    for configuration, numbers in displays:
        config_frequencies = get_frequencies(configuration)
        config_digits = {
            sort_letters(word): digits_value[get_numeric_representation(config_frequencies, word)]
            for word in configuration.split(" ")
        }

        digits.append(int("".join([config_digits[sort_letters(number)] for number in numbers.split(" ")])))

    return digits


if __name__ == "__main__":

    input_data = (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text()

    displays, outputs = parse_input(input_data)
    print(f"There are {count_easy_numbers(outputs)} characters of 1, 4, 7, or 8")

    numbers = deduce_crossed_wires(input_data)
    print(f"Sum of numbers {numbers} is {sum(numbers)}")
