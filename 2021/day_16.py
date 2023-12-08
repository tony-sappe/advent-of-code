from pathlib import Path
from typing import Any, Iterable, List, Tuple

Sample_Inputs = [
    "D2FE28",
    "38006F45291200",
    "EE00D40C823060",
    "8A004A801A8002F478",
    "620080001611562C8802118E34",
    "C0015000016115A2E0802F182340",
    "A0016C880162017C3686B18A3D4780",
    "C200B40A82",
    "04005AC33890",
    "880086C3E88112",
    "CE00C43D881120",
    "D8005AC2A8F0",
    "F600BC2D8F",
    "9C005AC2F8F0",
    "9C0141080250320F1802104A08",
]


def parse_input(input: str) -> List[str]:
    return list("".join(bin(int(hex_digit, 16))[2:].zfill(4) for hex_digit in input.strip()))


def parse_packet(bin_str_list: Iterable[str]) -> Tuple[int, int, Tuple[int, Any]]:
    version = int("".join(bin_str_list[:3]), 2)
    type_id = int("".join(bin_str_list[3:6]), 2)
    bin_str_list[:] = bin_str_list[6:]

    if type_id == 4:
        data = []
        while True:
            cont = bin_str_list.pop(0)
            data += bin_str_list[:4]
            bin_str_list[:] = bin_str_list[4:]
            if cont == "0":
                break
        data = int("".join(data), 2)
        return (version, type_id, data)

    else:
        sub_packets = []
        version_length = bin_str_list.pop(0)
        if version_length == "0":
            total_length = int("".join(bin_str_list[:15]), 2)
            bin_str_list[:] = bin_str_list[15:]

            sub_packet_data = bin_str_list[:total_length]
            bin_str_list[:] = bin_str_list[total_length:]

            while sub_packet_data:
                sub_packets.append(parse_packet(sub_packet_data))
        else:
            number_of_subpackets = int("".join(bin_str_list[:11]), 2)
            bin_str_list[:] = bin_str_list[11:]
            for _ in range(number_of_subpackets):
                sub_packets.append(parse_packet(bin_str_list))

        return (version, type_id, sub_packets)


def obtain_version_sum(parsed_packet) -> int:
    t = parsed_packet[0]
    if parsed_packet[1] == 4:
        return t
    else:
        return t + sum(map(obtain_version_sum, parsed_packet[2]))


def operator_evaluation(parsed_packet) -> int:
    operator = parsed_packet[1]
    if operator == 0:  # sum
        return sum(map(operator_evaluation, parsed_packet[2]))
    elif operator == 1:  # product
        product = 1
        for item in parsed_packet[2]:
            product *= operator_evaluation(item)
        return product
    elif operator == 2:  # minimum
        return min(map(operator_evaluation, parsed_packet[2]))
    elif operator == 3:  # maximum
        return max(map(operator_evaluation, parsed_packet[2]))
    elif operator == 4:  # value
        return parsed_packet[2]
    elif operator == 5:  # greater than
        return operator_evaluation(parsed_packet[2][0]) > operator_evaluation(parsed_packet[2][1])
    elif operator == 6:  # less than
        return operator_evaluation(parsed_packet[2][0]) < operator_evaluation(parsed_packet[2][1])
    elif operator == 7:  # equal to
        return operator_evaluation(parsed_packet[2][0]) == operator_evaluation(parsed_packet[2][1])
    else:
        raise RuntimeError(f"Type ID {operator} not recognized")


if __name__ == "__main__":
    input_data = (Path.cwd().parent / "advent-of-code-data" / "2021" / f"{Path(__file__).stem}_input.txt").read_text()
    binary_string_list = parse_input(input_data)
    print(f"Step 1: Version Sum: {obtain_version_sum(parse_packet(list(binary_string_list)))}")

    print(f"Step 2: Operator Value: {operator_evaluation(parse_packet(list(binary_string_list)))}")
