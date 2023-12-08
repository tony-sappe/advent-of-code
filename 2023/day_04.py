import re

from pathlib import Path
from typing import List, Tuple
from collections import defaultdict

Sample_Input = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def parse_input(input: str) -> List[Tuple[int, List[str], List[str]]]:
    cards = []
    lines = input.splitlines()
    for line in lines:
        number = int(re.search(r"Card\s+(\d+):", line).group(1))
        l, r = line.split("|")
        winnings = re.findall(r"(\d+) ", l)
        numbers = re.findall(r" (\d+)", r)
        cards.append((number, winnings, numbers))

    return cards


def card_points(card: Tuple[int, List[str], List[str]]) -> int:
    count = len(set(card[2]) & set(card[1]))
    if count > 0:
        return int(2 ** (count - 1))
    return 0


def calculate_total(cards: List[Tuple[int, List[str], List[str]]]) -> int:
    return sum([card_points(card) for card in cards])


def cascading_cards(cards):
    total_cards = defaultdict(int)
    for i, card in enumerate(cards):
        total_cards[i] += 1

        for j in range(len(set(card[1]) & set(card[2]))):
            total_cards[i + 1 + j] += total_cards[i]

    return sum(total_cards.values())


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2023" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    cards = parse_input(input_data)
    print(f"Step 1: Points {calculate_total(cards):,}")  # 21,158
    print(f"Step 2: Number of cards: {cascading_cards(cards):,}")  # 6,050,769
