from day_11 import Sample_Input, parse_input, simulate_flashes, find_simultaneous_flash


def test_input_parser():
    """Test the input parser output behavior"""
    grid = parse_input(Sample_Input)
    assert grid == [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]


def test_single_step():
    lines = parse_input(Sample_Input)
    grid, _ = simulate_flashes(lines, 1)
    assert grid == [
        [6, 5, 9, 4, 2, 5, 4, 3, 3, 4],
        [3, 8, 5, 6, 9, 6, 5, 8, 2, 2],
        [6, 3, 7, 5, 6, 6, 7, 2, 8, 4],
        [7, 2, 5, 2, 4, 4, 7, 2, 5, 7],
        [7, 4, 6, 8, 4, 9, 6, 5, 8, 9],
        [5, 2, 7, 8, 6, 3, 5, 7, 5, 6],
        [3, 2, 8, 7, 9, 5, 2, 8, 3, 2],
        [7, 9, 9, 3, 9, 9, 2, 2, 4, 5],
        [5, 9, 5, 7, 9, 5, 9, 6, 6, 5],
        [6, 3, 9, 4, 8, 6, 2, 6, 3, 7],
    ]


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    lines = parse_input(Sample_Input)
    grid, flashes = simulate_flashes(lines, 100)
    assert flashes == 1656
    assert grid == [
        [0, 3, 9, 7, 6, 6, 6, 8, 6, 6],
        [0, 7, 4, 9, 7, 6, 6, 9, 1, 8],
        [0, 0, 5, 3, 9, 7, 6, 9, 3, 3],
        [0, 0, 0, 4, 2, 9, 7, 8, 2, 2],
        [0, 0, 0, 4, 2, 2, 9, 8, 9, 2],
        [0, 0, 5, 3, 2, 2, 2, 8, 7, 7],
        [0, 5, 3, 2, 2, 2, 2, 9, 6, 6],
        [9, 3, 2, 2, 2, 2, 8, 9, 6, 6],
        [7, 9, 2, 2, 2, 8, 6, 8, 6, 6],
        [6, 7, 8, 9, 9, 9, 8, 7, 6, 6],
    ]


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    lines = parse_input(Sample_Input)
    grid, steps = find_simultaneous_flash(lines)
    assert steps == 195
    assert grid == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
