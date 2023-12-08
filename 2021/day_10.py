from pathlib import Path
from typing import Iterable, List, Tuple

Sample_Input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


def parse_input(input: str) -> tuple:
    return input.strip().split("\n")


def find_errors(lines: Iterable[str]) -> int:
    illegal_chars = {")": 3, "]": 57, "}": 1197, ">": 25137}
    _, _, errors = parse_lines(lines)

    return sum([illegal_chars[e] for e in errors])


def complete_incomplete(lines: Iterable[str]) -> int:
    closing_chars = {"(": ")", "[": "]", "{": "}", "<": ">"}
    score_chars = {")": 1, "]": 2, "}": 3, ">": 4}
    _, incomplete, _ = parse_lines(lines)

    scores = []
    for line in incomplete:
        score = 0
        for symbol in line[::-1]:
            score *= 5
            score += score_chars[closing_chars[symbol]]
        scores.append(score)

    scores.sort()
    return scores[len(scores) // 2]


def parse_lines(lines: Iterable[str]) -> Tuple[List[int], List[int], List[int]]:

    errors = []
    incomplete = []
    complete = []
    for line in lines:
        status, value = checker(line)
        if status == "complete":
            complete.append(line)
        elif status == "open":
            incomplete.append(value)
        else:
            errors.append(value)

    return complete, incomplete, errors


def checker(line: str) -> Tuple[str, str]:
    open_chars = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack = []
    for l in line:
        if l in "([{<":
            stack.append(l)
        else:
            if len(stack) == 0:
                return ("error", l)
            last_char = stack.pop()
            if open_chars[l] != last_char:
                return ("error", l)
    if len(stack) == 0:
        return ("complete", "")
    else:
        return ("open", stack)


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2021" / f"{Path(__file__).stem}_input.txt").read_text()
    lines = parse_input(input_data)
    print(f"Error Score is: {find_errors(lines)}")
    print(f"Incomplete Score is: {complete_incomplete(lines)}")
