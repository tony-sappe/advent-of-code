from pathlib import Path

"""
    inp w
    mul x 0
    add x z
    mod x 26
    div z {DIV}
    add x {CHECK}
    eql x w
    eql x 0
    mul y 0
    add y 25
    mul y x
    add y 1
    mul z y
    mul y 0
    add y w
    add y {OFFSET}
    mul y x
    add z y


We can interpret this code as performing the following:
- Read an input.
- Check the condition: input == (z % 26) + {CHECK}.
- If {CHECK} is negative (or equivalently, {DIV} is 26), set z = z / 26.
- If the condition is met, do nothing further.
- Otherwise, set z = 26 * z + input + {OFFSET}
"""


def process(input):
    code_nums = []
    lines = input.splitlines()
    for i in range(14):
        check = int(lines[5 + 18 * i].split(" ")[2])
        offset = int(lines[15 + 18 * i].split(" ")[2])
        code_nums.append((check, offset))

    stack = []
    for i, pair in enumerate(code_nums):
        if pair[0] < 0:
            index, val = stack.pop()
            num = pair[0] + val  # {'+' if num < 0 else '-'} {abs(num)}
            print(f"input[{i}] == input[{index}] {'+' if num > 0 else ''} {num} ")
        else:
            stack.append((i, pair[1]))

    #     ("11", "14"),
    #     ("14", "6"),
    #     ("15", "6"),
    #     ("13", "13"),
    #     ("-12", "8"),
    #     ("10", "8"),
    #     ("-15", "7"),
    #     ("13", "10"),
    #     ("10", "8"),
    #     ("-13", "12"),
    #     ("-13", "10"),
    #     ("-14", "8"),
    #     ("-2", "8"),
    #     ("-9", "7"),

    # PUSH input[0] + 14
    # PUSH input[1] + 6
    # PUSH input[2] + 6
    # PUSH input[3] + 13
    # POP. Input[4] == input[3] + 13 - 8


# input[4] == input[3] + 1
# input[6] == input[5]  -7
# input[9] == input[8]  -5
# input[10] == input[7]  -3
# input[11] == input[2]  -8
# input[12] == input[1] + 4
# input[13] == input[0] + 5


"""
    input 0  = 4
    input 1  = 5
    input 2  = 9
    input 3  = 8
    input 4  = 9
    input 5  = 9
    input 6  = 2
    input 7  = 9
    input 8  = 9
    input 9  = 4
    input 10 = 6
    input 11 = 1
    input 12 = 9
    input 13 = 9


45989929946199


    input 0  = 1
    input 1  = 1
    input 2  = 9
    input 3  = 1
    input 4  = 2
    input 5  = 8
    input 6  = 1
    input 7  = 4
    input 8  = 6
    input 9  = 1
    input 10 = 1
    input 11 = 1
    input 12 = 5
    input 13 = 6

11912814611156
"""


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2021" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input
    # programs = parse_input(input_data)
    process(input_data)
    print(f"Step 1: Largest Model Number: 45989929946199")
    print(f"Step 2: Smallest Model Number: 11912814611156")
