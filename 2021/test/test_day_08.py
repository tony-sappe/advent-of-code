from day_08 import Sample_Input, parse_input, deduce_crossed_wires, count_easy_numbers


def test_input_parser():
    """Test the input parser output behavior"""
    displays, outputs = parse_input(Sample_Input)
    assert outputs[0] == ["fdgacbe", "cefdb", "cefbgd", "gcbe"]


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    displays, outputs = parse_input(Sample_Input)
    assert count_easy_numbers(outputs) == 26


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    numbers = deduce_crossed_wires(Sample_Input)
    assert sum(numbers) == 61229
