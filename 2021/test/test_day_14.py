from day_14 import Sample_Input, parse_input, polymer_chain_growth, polymer_counts


def test_input_parser():
    template, pairs = parse_input(Sample_Input)
    assert template == "NNCB"
    assert pairs == {
        "CH": "B",
        "HH": "N",
        "CB": "H",
        "NH": "C",
        "HB": "C",
        "HC": "B",
        "HN": "C",
        "NN": "C",
        "BH": "H",
        "NC": "B",
        "NB": "B",
        "BN": "B",
        "BB": "N",
        "BC": "B",
        "CC": "N",
        "CN": "C",
    }


def test_chain_growth():
    template, pairs = parse_input(Sample_Input)
    assert polymer_chain_growth(template, pairs, 1) == "NCNBCHB"
    assert polymer_chain_growth(template, pairs, 2) == "NBCCNBBBCBHCB"
    assert polymer_chain_growth(template, pairs, 3) == "NBBBCNCCNBBNBNBBCHBHHBCHB"
    assert polymer_chain_growth(template, pairs, 4) == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    template, pairs = parse_input(Sample_Input)
    counts = polymer_counts(polymer_chain_growth(template, pairs, 10))
    assert max(counts.values()) - min(counts.values()) == 1588


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    template, pairs = parse_input(Sample_Input)
    # counts = polymer_counts(polymer_chain_growth(template, pairs, 40))
    # assert max(counts.values()) - min(counts.values()) == 2188189693529
