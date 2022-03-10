from day_20 import Sample_Input, parse_input


def test_input_parser():
    """Test the input parser output behavior"""

    image_enhancement, image = parse_input(Sample_Input)
    assert hex(int("".join(image_enhancement), 2)) == "0x29f55d83b4ef3e424ce7ee3c9f32f8d4b28177eef16c93e0a1cb02092646fdef51012a3da048d646b3a050157bb107a4b432f0c6440a02033c8a8ca73e013c09"
    assert image == [
        ["1", "0", "0", "1", "0"],
        ["1", "0", "0", "0", "0"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "1", "1", "1"],
    ]


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    target_area = parse_input(Sample_Input)


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
