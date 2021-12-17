from day_16 import Sample_Inputs, parse_input, parse_packet, obtain_version_sum, operator_evaluation

STEP_1_SAMPLE_SIZE = 7


def test_input_parser():
    """Test the input parser output behavior"""
    expected = [
        "110100101111111000101000",
        "00111000000000000110111101000101001010010001001000000000",
        "11101110000000001101010000001100100000100011000001100000",
        "100010100000000001001010100000000001101010000000000000101111010001111000",
        "01100010000000001000000000000000000101100001000101010110001011001000100000000010000100011000111000110100",
        "1100000000000001010100000000000000000001011000010001010110100010111000001000000000101111000110000010001101000000",
        "101000000000000101101100100010000000000101100010000000010111110000110110100001101011000110001010001111010100011110000000",
    ]

    for inp, ex in zip(Sample_Inputs[:STEP_1_SAMPLE_SIZE], expected):
        assert parse_input(inp) == list(ex)


def test_packet_parser():
    version, type_id, value = parse_packet(parse_input(Sample_Inputs[0]))
    assert (version, type_id, value) == (6, 4, 2021)

    version, type_id, value = parse_packet(parse_input(Sample_Inputs[1]))
    assert (version, type_id, value) == (1, 6, [(6, 4, 10), (2, 4, 20)])

    version, type_id, value = parse_packet(parse_input(Sample_Inputs[2]))
    assert (version, type_id, value) == (7, 3, [(2, 4, 1), (4, 4, 2), (1, 4, 3)])


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    expected = [6, 9, 14, 16, 12, 23, 31]

    for inp, ex in zip(Sample_Inputs[:STEP_1_SAMPLE_SIZE], expected):
        assert obtain_version_sum(parse_packet(parse_input(inp))) == ex


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    expected = [3, 54, 7, 9, 1, 0, 0, 1]

    for inp, ex in zip(Sample_Inputs[STEP_1_SAMPLE_SIZE:], expected):
        assert operator_evaluation(parse_packet(parse_input(inp))) == ex, f"{inp} should == {ex}"
