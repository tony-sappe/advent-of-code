from collections import Counter
from functools import cmp_to_key
from icecream import ic
from pathlib import Path
from typing import List, Tuple

Sample_Input = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


def parse_input(input: str) -> List[Tuple[str, str]]:
    hands = input.splitlines()
    return [hand.split(" ") for hand in hands]


def card_ranks(cards: str) -> List[int]:
    """Convert a rank into a numeric value"""
    return ["--23456789TJQKA".index(c) for c in cards]


def joker_card_ranks(cards: str) -> List[int]:
    """Convert a rank into a numeric value"""
    return ["-J23456789T-QKA".index(c) for c in cards]


def assign_type(hand, bid) -> Tuple[str, str, str]:
    s = set(hand)
    groups = sorted([hand.count(i) for i in s], reverse=True)
    # ic(s)
    # ic(groups)
    if len(s) == 1:
        return (hand, bid, "kind-5")
    elif len(s) == 2 and groups[0] == 4:
        return (hand, bid, "kind-4")
    elif len(s) == 2 and groups[0] == 3 and groups[1] == 2:
        return (hand, bid, "full-house")
    elif len(s) == 3 and groups[0] == 3:
        return (hand, bid, "kind-3")
    elif groups[0] == 2 and groups[1] == 2:
        return (hand, bid, "pair-2")
    elif len(s) == 4 and groups[0] == 2:
        return (hand, bid, "pair-1")
    elif len(s) == 5:
        return (hand, bid, "high-card")
    else:
        ic(hand)
        return ("", "", "")


def joker_assign_type(hand, bid) -> Tuple[str, str, str]:
    original_hand = hand
    if "J" in hand:
        hand = hand.replace("J", "")
        if hand == "":
            return (original_hand, bid, "kind-5")
        counts = Counter(hand)
        most, count = counts.most_common(1)[0]
        while len(hand) < 5:
            hand += most

    s = set(hand)
    groups = sorted([hand.count(i) for i in s], reverse=True)

    if len(s) == 1:
        return (original_hand, bid, "kind-5")
    elif len(s) == 2 and groups[0] == 4:
        return (original_hand, bid, "kind-4")
    elif len(s) == 2 and groups[0] == 3 and groups[1] == 2:
        return (original_hand, bid, "full-house")
    elif len(s) == 3 and groups[0] == 3:
        return (original_hand, bid, "kind-3")
    elif groups[0] == 2 and groups[1] == 2:
        return (original_hand, bid, "pair-2")
    elif len(s) == 4 and groups[0] == 2:
        return (original_hand, bid, "pair-1")
    elif len(s) == 5:
        return (original_hand, bid, "high-card")
    else:
        ic(original_hand)
        return ("", "", "")


def order_hands(in_hands: List[Tuple[str, str]]) -> int:
    hands = [assign_type(hand, bid) for hand, bid in in_hands]
    hands.sort(key=cmp_to_key(hand_cmp))
    # ic(hands)

    # for i, h in enumerate(hands, 1):
    #    print(f"rank: {i}, hand:{h[0]}, bid:{h[1]}, winnings: {int(h[1]) * i}")

    return sum(int(h[1]) * i for i, h in enumerate(hands, 1))


def joker_order_hands(in_hands: List[Tuple[str, str]]) -> int:
    hands = [joker_assign_type(hand, bid) for hand, bid in in_hands]
    hands.sort(key=cmp_to_key(joker_hand_cmp))
    return sum(int(h[1]) * i for i, h in enumerate(hands, 1))


def hand_cmp(x, y) -> bool:
    types = ["high-card", "pair-1", "pair-2", "kind-3", "full-house", "kind-4", "kind-5"]
    if x[2] == y[2]:  # same type
        x_ranks = card_ranks(x[0])
        y_ranks = card_ranks(y[0])
        i = 0
        while True:
            if x_ranks[i] != y_ranks[i]:
                return x_ranks[i] - y_ranks[i]
            elif i == len(x[0]):
                return 0
            else:
                i += 1
    else:
        return types.index(x[2]) - types.index(y[2])


def joker_hand_cmp(x, y) -> bool:
    types = ["high-card", "pair-1", "pair-2", "kind-3", "full-house", "kind-4", "kind-5"]
    if x[2] == y[2]:  # same type
        x_ranks = joker_card_ranks(x[0])
        y_ranks = joker_card_ranks(y[0])
        i = 0
        while True:
            if x_ranks[i] != y_ranks[i]:
                return x_ranks[i] - y_ranks[i]
            elif i == len(x[0]):
                return 0
            else:
                i += 1
    else:
        return types.index(x[2]) - types.index(y[2])


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2023" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    hands = parse_input(input_data)
    ans = order_hands(hands)
    print(f"Step 1: Winnings: {ans:,} ({ans})")  # 250,058,342
    ans = joker_order_hands(hands)
    print(f"Step 2: Winnings: {ans:,} ({ans})")  # 250,506,580
