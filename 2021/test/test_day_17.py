from day_17 import Sample_Input, parse_input, Coord, obtain_highest_elevation, find_every_initial_velocity


def test_input_parser():
    """Test the input parser output behavior"""

    target_area = parse_input(Sample_Input)
    assert target_area[0][0] == 20 and target_area[0][1] == 30
    assert target_area[1][0] == -10 and target_area[1][1] == -5
    assert target_area.x.min == 20 and target_area.x.max == 30
    assert target_area.y.min == -10 and target_area.y.max == -5


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    target_area = parse_input(Sample_Input)
    assert obtain_highest_elevation(Coord(0, 0), target_area) == 45


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    target_area = parse_input(Sample_Input)
    assert find_every_initial_velocity(Coord(0, 0), target_area) == 112
