from day_02 import Sample_Input, parse_input, track_vector_movement


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    movements = parse_input(Sample_Input)
    assert track_vector_movement(movements, False) == 150


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    movements = parse_input(Sample_Input)
    assert track_vector_movement(movements, True) == 900
