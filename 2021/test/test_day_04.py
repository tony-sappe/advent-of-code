from day_04 import Sample_Input, parse_input, simulate_game, calculate_score


def test_input_parser():
    """Test the input parser output behavior"""
    (draws, boards) = parse_input(Sample_Input)
    assert len(boards) == 3
    assert draws == [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

    assert boards[0] == [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19],
    ]


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    draws, boards = parse_input(Sample_Input)
    winner, draw_count = simulate_game(boards, draws, "win")
    score = calculate_score(boards[winner], draws[:draw_count])
    assert score == 4512


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    draws, boards = parse_input(Sample_Input)
    winner, draw_count = simulate_game(boards, draws, "lose")
    score = calculate_score(boards[winner], draws[:draw_count])
    assert score == 1924
