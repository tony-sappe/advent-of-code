from day_09 import Sample_Input, parse_input, determine_risk, find_low_points, find_basins, largest_basins_volume


def test_input_parser():
    """Test the input parser output behavior"""
    grid = parse_input(Sample_Input)
    assert grid == [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    grid = parse_input(Sample_Input)
    points = find_low_points(grid)
    assert determine_risk(points) == 15


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    grid = parse_input(Sample_Input)
    basins = find_basins(grid)
    assert largest_basins_volume(basins) == 1134
