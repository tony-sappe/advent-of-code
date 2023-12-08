from day_12 import (
    Sample_Input_1,
    Sample_Input_2,
    Sample_Input_3,
    parse_input,
    generate_valid_paths,
    generate_valid_paths_2,
)


def test_input_parser():
    """Test the input parser output behavior"""
    network = parse_input(Sample_Input_1)
    assert network == [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
    ]


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    network = parse_input(Sample_Input_1)
    paths = generate_valid_paths(network)
    assert len(paths) == 10

    network = parse_input(Sample_Input_2)
    paths = generate_valid_paths(network)
    assert len(paths) == 19

    network = parse_input(Sample_Input_3)
    paths = generate_valid_paths(network)
    assert len(paths) == 226


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    network = parse_input(Sample_Input_1)
    paths = generate_valid_paths_2(network)
    assert len(paths) == 36

    network = parse_input(Sample_Input_2)
    paths = generate_valid_paths_2(network)
    assert len(paths) == 103

    network = parse_input(Sample_Input_3)
    paths = generate_valid_paths_2(network)
    assert len(paths) == 3509
