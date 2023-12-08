from pathlib import Path
from itertools import cycle
from typing import Any, Dict, Iterable, List, Tuple

Sample_Input = """
Player 1 starting position: 4
Player 2 starting position: 8
"""


Actual_Input = """
Player 1 starting position: 10
Player 2 starting position: 7
"""


def play(p1: int, p2: int) -> int:
    p1_score, p2_score = 0, 0
    p1_pos, p2_pos = p1, p2
    turn = "p1"
    die = cycle(range(1, 101))
    rolls = 0

    while p1_score < 1000 and p2_score < 1000:
        my_rolls = next(die) + next(die) + next(die)
        if turn == "p1":
            turn = "p2"
            p1_pos = (p1_pos + my_rolls - 1) % 10 + 1
            p1_score += p1_pos
        else:
            turn = "p1"
            p2_pos = (p2_pos + my_rolls - 1) % 10 + 1
            p2_score += p2_pos

        rolls += 3

    if p1_score > p2_score:
        print(f"After {rolls:,} rolls, Player 1 won: {p1_score:,}, Player 2 lost: {p2_score:,}")
        return p2_score * rolls
    else:
        print(f"After {rolls:,} rolls, Player 2 won: {p2_score:,}, Player 1 lost: {p1_score:,}")
        return p1_score * rolls


def play_dirac(p1: int, p2: int) -> int:
    cache = {}

    def c():
        return [x + y + z for x in [1, 2, 3] for y in [1, 2, 3] for z in [1, 2, 3]]

    def u(p0, p1, s0=0, s1=0):
        k = (p0, p1, s0, s1)
        if k in cache:
            return cache[k]
        oc = [0, 0]
        for r in c():
            p0_ = (p0 + r - 1) % 10 + 1
            s0_ = s0 + p0_
            if s0_ >= 21:
                oc[0] += 1
            else:
                dy, dx = u(p1, p0_, s1, s0_)
                oc[0] += dx
                oc[1] += dy
        cache[k] = oc

        return oc

    return max(u(p1, p2))


if __name__ == "__main__":

    print(f"Step 0: Test {play(4, 8):,}")
    print(f"Step 1: Game solution {play(10, 7):,}")
    print(f"Step 1.5: Test Probability {play_dirac(4, 8):,}")
    print(f"Step 2: Game Probability {play_dirac(10, 7):,}")
