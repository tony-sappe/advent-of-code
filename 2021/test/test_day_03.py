from day_03 import parse_diagnostics, parse_additional_diagnostics, Sample_Input


def test_provided_step_1():
    assert parse_diagnostics(Sample_Input) == 198


def test_provided_step_2():
    assert parse_additional_diagnostics(Sample_Input) == 230
