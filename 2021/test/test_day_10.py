from day_10 import Sample_Input, parse_input, find_errors, complete_incomplete


def test_input_parser():
    """Test the input parser output behavior"""
    grid = parse_input(Sample_Input)
    assert grid == [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    lines = parse_input(Sample_Input)
    assert find_errors(lines) == 26397


def test_single_incomplete():
    test_line = ["[({(<(())[]>[[{[]{<()<>>"]
    score = complete_incomplete(test_line)
    assert score == 288957


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    lines = parse_input(Sample_Input)
    assert complete_incomplete(lines) == 288957
