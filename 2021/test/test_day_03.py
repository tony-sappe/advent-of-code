from day_03 import Sample_Input, parse_input, gamma_and_epsilon_diagnostics, o2_and_co2_diagnostics


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    report = parse_input(Sample_Input)
    g, e = gamma_and_epsilon_diagnostics(report)
    assert g * e == 198


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    report = parse_input(Sample_Input)
    o, c = o2_and_co2_diagnostics(report)
    assert o * c == 230
