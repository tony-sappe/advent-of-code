from pathlib import Path
from typing import Iterable, List, Tuple

Sample_Input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


def board_to_grids(board: Iterable[Iterable[int]]) -> List[List[int]]:
    result = board
    columns = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    result.extend(columns)
    return result


def draws_to_win(board: Iterable[Iterable[int]], draws: Iterable[int]) -> int:
    for turn in range(5, len(draws), 1):
        for grid in board:
            if set(draws[:turn]) >= set(grid):
                return turn
    return 1_000_000_000_000


def simulate_game(boards: Iterable[Iterable[Iterable[int]]], draws: Iterable[int], strategy: str = "win") -> int:
    """ """
    if strategy == "win":
        op = min
    else:
        op = max
    win_state = [(i, draws_to_win(board_to_grids(board), draws)) for i, board in enumerate(boards)]
    return op(win_state, key=lambda t: t[1])


def calculate_score(board: Iterable[Iterable[int]], draws: Iterable[int]) -> int:
    unmarked_spaces = set([x for grid in board for x in grid if x not in draws])
    return sum(unmarked_spaces) * draws[-1]


def parse_input(input: str) -> Tuple[List[int], List[List[int]]]:
    sections = input.strip().split("\n\n")
    drawn_numbers = list(map(int, sections[0].split(",")))

    boards = [section.split("\n") for section in sections[1:]]
    cleaned_boards = [[list(map(int, line.split())) for line in board] for board in boards]

    return drawn_numbers, cleaned_boards


if __name__ == "__main__":
    bingo_game_input = (Path.cwd() / "2021" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    draws, boards = parse_input(bingo_game_input)

    winner, draw_count = simulate_game(boards, draws)
    score = calculate_score(boards[winner], draws[:draw_count])
    print(f"Step 1: Best Board is #{winner+1} | Bingo on draw {draw_count:,} | Score: {score:,}")

    winner, draw_count = simulate_game(boards, draws, "lose")
    score = calculate_score(boards[winner], draws[:draw_count])
    print(f"Step 2: Worst Board is #{winner+1} | Bingo on draw {draw_count:,} | Score: {score:,}")
