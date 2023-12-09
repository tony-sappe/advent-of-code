from pathlib import Path

Sample_Input = [
    "abcdefgh",  # abcdffaa
    "ghijklmn",  # ghjaabcc
]


def is_valid(password: str) -> bool:
    if "i" in password or "o" in password or "l" in password:
        return False

    pairs = []
    for i in range(len(password) - 1):
        if password[i] == password[i + 1] and password[i] not in pairs and password[i + 1] not in pairs:
            pairs.append(password[i])
            pairs.append(password[i + 1])

    if len(pairs) < 4:
        return False

    for x, y, z in zip(password, password[1:], password[2:]):
        if ord(y) - ord(x) == 1 and ord(z) - ord(y) == 1:
            return True

    return False


def find_next(password: str) -> str:
    while not is_valid(password):
        chars = [ord(p) for p in password][::-1]
        chars[0] += 1
        for i in range(len(chars)):
            if chars[i] > ord("z"):
                chars[i] = ord("a")
                chars[i + 1] += 1

            password = "".join([chr(c) for c in chars[::-1]])

    return password


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2015" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Input[1]
    print(f"Step 1: Transformation: {find_next(input_data.strip())}")  # hxbxxyzz
    print(f"Step 2: Transformation: {find_next('hxbxxzaa')}")  # hxcaabcc
