from day_01 import Sample_Input, parse_input, sonar_scan, sonar_scan_triplets


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    sonar_sweep = parse_input(Sample_Input)
    assert sonar_scan(sonar_sweep) == 7


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    sonar_sweep = parse_input(Sample_Input)
    assert sonar_scan_triplets(sonar_sweep) == 5
