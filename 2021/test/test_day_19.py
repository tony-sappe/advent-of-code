from day_19 import Sample_Input, parse_input, positioning_calculations


def test_input_parser():
    """Test the input parser output behavior"""

    scanners = parse_input(Sample_Input)
    assert len(scanners) == 5
    assert len(scanners[0]) == 25
    assert scanners[0][0] == (404, -588, -901)
    assert scanners[0][4] == (-537, -823, -458)
    assert scanners[0][-1] == (459, -707, 401)
    assert len(scanners[4]) == 26
    assert scanners[4][0] == (727, 592, 562)
    assert scanners[4][-1] == (30, -46, -14)


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    feed = parse_input(Sample_Input)
    assert positioning_calculations(feed)[0] == 79


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    feed = parse_input(Sample_Input)
    assert positioning_calculations(feed)[1] == 3621
