import hashlib
from pathlib import Path
from icecream import ic
from typing import List, Set, Tuple

Sample_Input = ["abcdef", "pqrstuv"]


def mine_coin(secret: str, target: str) -> int:
    i = 0
    while not hashlib.md5(str.encode(secret + str(i))).hexdigest().startswith(target):
        i += 1
    return i


if __name__ == "__main__":
    secret = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text().strip()
    # secret = Sample_Input[1]
    print(f"Step 1: Number is: {mine_coin(secret, '00000'):,}")  # 117,946
    print(f"Step 2: Number is: {mine_coin(secret, '000000'):,}")  # 3,938,038
