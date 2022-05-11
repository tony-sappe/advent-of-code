from itertools import product
from pathlib import Path
from typing import List

Sample_Inputs = [
    """[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
""",
    """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
""",
]


def parse_input(input: str) -> List[int]:
    lines = [eval(line) for line in input.splitlines()]
    return lines


class Num:
    def __init__(self, val):
        self.val = val
        self.leftn = None
        self.rightn = None
        self.leftmost = self
        self.rightmost = self
        self.parent = None

    def update_n(self):
        pass

    def __repr__(self):
        return str(self.val)


class Pair:
    def __init__(self, left, right):
        self.parent = None
        self.side = None
        self.left = left
        self.right = right
        self.leftmost = left.leftmost
        self.rightmost = right.rightmost
        self.setleft(left)
        self.setright(right)

    def setleft(self, left):
        self.left = left
        self.left.parent = self
        self.left.side = 0
        self.leftmost = self.left.leftmost
        self.left.rightmost.rightn = self.right.leftmost

    def setright(self, right):
        self.right = right
        self.right.parent = self
        self.right.side = 1
        self.rightmost = self.right.rightmost
        self.right.leftmost.leftn = self.left.rightmost

    def update_n(self):
        self.left.update_n()
        self.right.update_n()
        self.leftmost = self.left.leftmost
        self.rightmost = self.right.rightmost
        self.left.rightmost.rightn = self.right.leftmost
        self.right.leftmost.leftn = self.left.rightmost

    def __repr__(self):
        return f"[{self.left}, {self.right}]"


def convert(element):
    if isinstance(element, list):
        return Pair(convert(element[0]), convert(element[1]))
    else:
        return Num(element)


def test_explode(v, k, d=0):
    if isinstance(k, Num):
        return
    if isinstance(k.left, Num) and isinstance(k.right, Num) and d >= 4:
        if k.left.leftn:
            k.left.leftn.val += k.left.val
        if k.right.rightn:
            k.right.rightn.val += k.right.val
        if k.side == 0:
            k.parent.setleft(Num(0))
        else:
            k.parent.setright(Num(0))
        v.update_n()
        return True
    return test_explode(v, k.left, d + 1) or test_explode(v, k.right, d + 1)


def test_split(v, k):
    if isinstance(k, Num):
        if k.val >= 10:
            if k.side == 0:
                k.parent.setleft(Pair(Num(k.val // 2), Num(-(-k.val // 2))))
            else:
                k.parent.setright(Pair(Num(k.val // 2), Num(-(-k.val // 2))))
            v.update_n()
            return True
        else:
            return False
    return test_split(v, k.left) or test_split(v, k.right)


def reduce(v):
    while True:
        if test_explode(v, v):
            pass
        elif test_split(v, v):
            pass
        else:
            break


def mag(v):
    if isinstance(v, Num):
        return v.val
    else:
        return 3 * mag(v.left) + 2 * mag(v.right)


def copy(v):
    if isinstance(v, Pair):
        return Pair(copy(v.left), copy(v.right))
    return Num(v.val)


def calculate_magnitude(lines):
    accumulator = []

    for line in lines:
        if accumulator == []:
            accumulator = convert(line)
        else:
            accumulator = Pair(accumulator, convert(line))
            reduce(accumulator)

    return mag(accumulator)


def calculate_largest_magnitude(lines):
    math_lines = [convert(line) for line in lines]
    largest_value = -float("inf")

    for i, j in product(range(len(math_lines)), repeat=2):
        if i == j:
            continue

        pair = Pair(copy(math_lines[i]), copy(math_lines[j]))
        reduce(pair)
        largest_value = max(largest_value, mag(pair))

    return largest_value


if __name__ == "__main__":
    input_data = (Path.cwd() / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    math_problem = parse_input(input_data)
    answer = calculate_magnitude(math_problem)
    print(f"Step 1: Magnitude of final sum: {answer:,}")
    answer = calculate_largest_magnitude(math_problem)
    print(f"Step 2: Largest Magnitude of any sum of two different numbers: {answer:,}")
