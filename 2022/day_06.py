from pathlib import Path


Sample_Inputs = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",  # 7, 19
    "bvwbjplbgvbhsrlpgdmjqwftvncz",  # 5, 23
    "nppdvjthqldpwncqszvftbrmjlhg",  # 6, 23
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",  # 10, 29
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",  # 11, 26
]


def parse_input(input: str) -> str:
    return input


def find_marker(buffer: str) -> int:
    for i in range(4, len(buffer)):
        if len(set(buffer[i - 4 : i])) == 4:
            return i


def find_message(buffer: str) -> int:
    for i in range(14, len(buffer)):
        if len(set(buffer[i - 14 : i])) == 14:
            return i


if __name__ == "__main__":
    input_data = (Path.cwd() / "2022" / "data" / f"{Path(__file__).stem}_input.txt").read_text()
    # input_data = Sample_Inputs[4]
    datastream_buffer = parse_input(input_data)
    print(f"Step 1: The marker is at {find_marker(datastream_buffer)}")  # 1707
    print(f"Step 2: The message is at {find_message(datastream_buffer)}")  # 3697
