from day_07 import Sample_Input, parse_input, realignment, realignment_fuel


def test_input_parser():
    """Test the input parser output behavior"""
    lines = parse_input(Sample_Input)
    assert lines == [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    positions = parse_input(Sample_Input)
    position, moves = realignment(positions)
    assert position == 2
    assert moves == 37


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    positions = parse_input(Sample_Input)
    position, moves = realignment_fuel(positions)
    assert position == 5
    assert moves == 168
