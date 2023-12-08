from day_18 import Sample_Inputs, parse_input, calculate_magnitude, calculate_largest_magnitude


def test_input_parser():
    """Test the input parser output behavior"""

    lines = parse_input(Sample_Inputs[0])
    assert lines[0] == [1, 2]
    assert lines[1] == [[1, 2], 3]
    assert lines[2] == [9, [8, 7]]
    assert lines[3] == [[1, 9], [8, 5]]
    assert lines[4] == [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9]
    assert lines[5] == [[[9, [3, 8]], [[0, 9], 6]], [[[3, 7], [4, 9]], 3]]
    assert lines[6] == [[[[1, 3], [5, 3]], [[1, 3], [8, 7]]], [[[4, 9], [6, 9]], [[8, 2], [7, 3]]]]


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    lines = parse_input(Sample_Inputs[1])
    assert calculate_magnitude(lines) == 4140


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    lines = parse_input(Sample_Inputs[1])
    assert calculate_largest_magnitude(lines) == 3993
