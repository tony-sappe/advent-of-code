from day_06 import Sample_Input, parse_input, simulate


def test_input_parser():
    """Test the input parser output behavior"""
    lines = parse_input(Sample_Input)
    assert lines == [3, 4, 3, 1, 2]


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    fish = parse_input(Sample_Input)
    simulated_fish = simulate(list(fish), days=18)
    assert simulated_fish == 26

    simulated_fish = simulate(list(fish), days=80)
    assert simulated_fish == 5934


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    fish = parse_input(Sample_Input)
    simulated_fish = simulate(list(fish), days=256)
    assert simulated_fish == 26984457539
