from collections import Counter
from day_14 import Sample_Input, parse_input, polymer_chain_growth


def test_input_parser():
    """Test the input parser output behavior"""
    template, polymer_chain, insertion_rules = parse_input(Sample_Input)
    assert template == "NNCB"
    assert polymer_chain == {"NN": 1, "NC": 1, "CB": 1}
    assert insertion_rules == {
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
    _, polymer_chain, insertion_rules = parse_input(Sample_Input)
    assert polymer_chain_growth(polymer_chain, insertion_rules, 1) == Counter("NCNBCHB")
    assert polymer_chain_growth(polymer_chain, insertion_rules, 2) == Counter("NBCCNBBBCBHCB")
    assert polymer_chain_growth(polymer_chain, insertion_rules, 3) == Counter("NBBBCNCCNBBNBNBBCHBHHBCHB")
    assert polymer_chain_growth(polymer_chain, insertion_rules, 4) == Counter(
        "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    )


def test_provided_step_1():
    """Ensure the sample puzzle input matches the provided answer for step 1"""
    _, polymer_chain, insertion_rules = parse_input(Sample_Input)
    counts = polymer_chain_growth(polymer_chain, insertion_rules, 10)
    assert max(counts.values()) - min(counts.values()) == 1588


def test_provided_step_2():
    """Ensure the sample puzzle input matches the provided answer for step 2"""
    _, polymer_chain, insertion_rules = parse_input(Sample_Input)
    counts = polymer_chain_growth(polymer_chain, insertion_rules, 40)
    assert max(counts.values()) - min(counts.values()) == 2188189693529
