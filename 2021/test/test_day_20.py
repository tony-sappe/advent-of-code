from day_20 import Sample_Input, parse_input


def test_input_parser():
    """Test the input parser output behavior"""

    image_enhancement, image = parse_input(Sample_Input)
    assert image_enhancement[0] == "0"
    assert image_enhancement[5] == "0"
    assert image_enhancement[10] == "1"
    assert image_enhancement[15] == "1"
    assert image_enhancement[20] == "1"
    assert image_enhancement[25] == "0"
    assert image_enhancement[30] == "1"
    assert image == [
        ["1", "0", "0", "1", "0"],
        ["1", "0", "0", "0", "0"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "1", "1", "1"],
    ]


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    # target_area = parse_input(Sample_Input)


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
