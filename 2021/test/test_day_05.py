from day_05 import Sample_Input, parse_input, scrub_diagonal_lines, create_points, find_hotspots


def test_input_parser():
    """Test the input parser output behavior"""
    lines = parse_input(Sample_Input)
    assert lines == [((0, 9), (5, 9)), ((8, 0), (0, 8)), ((9, 4), (3, 4)), ((2, 2), (2, 1)), ((7, 0), (7, 4)), ((6, 4), (2, 0)), ((0, 9), (2, 9)), ((3, 4), (1, 4)), ((0, 0), (8, 8)), ((5, 5), (8, 2))]


def test_diagonal_removal():

    no_diags = [((0, 9), (5, 9)), ((9, 4), (3, 4))]
    diags_only = [((8, 0), (0, 8)), ((6, 4), (2, 0)), ((0, 0), (8, 8))]
    assert scrub_diagonal_lines(no_diags) == no_diags
    assert scrub_diagonal_lines(diags_only) == []
    assert scrub_diagonal_lines(no_diags + diags_only) == no_diags


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    lines = parse_input(Sample_Input)
    line_subset = scrub_diagonal_lines(lines)
    points = create_points(line_subset)
    hotspots, hot_temperature = find_hotspots(points)
    assert len(hotspots) == 5


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    lines = parse_input(Sample_Input)
    points = create_points(lines)
    hotspots, hot_temperature = find_hotspots(points)
    assert len(hotspots) == 12
