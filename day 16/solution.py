import io
import math
from functools import reduce


def read_file(filename="input.txt"):
    with open(filename, "r") as fh:
        line = fh.read()
    print(line)
    scale = 16
    num_of_bits = 4
    return io.StringIO(''.join([bin(int(my_hexdata, scale))[2:].zfill(num_of_bits) for my_hexdata in line ]))


def action(values, type_id):
    if type_id == 0:
        return sum(values)
    if type_id == 1:
        return reduce((lambda x, y: x * y), values)
    if type_id == 2:
        return min(values)
    if type_id == 3:
        return max(values)
    if type_id == 5:
        return 1 if values[0] > values[1] else 0
    if type_id == 6:
        return 1 if values[0] < values[1] else 0
    if type_id == 7:
        return 1 if values[0] == values[1] else 0


def parse_data(data):
    total_version = 0
    version = data.read(3)
    # if not version or version == "000":
    #     return 0
    version = int(version, 2)
    print("version", version)
    total_version += version
    type_id = int(data.read(3), 2)
    print("type", type_id)
    if type_id == 4:
        value = ""
        while True:
            end = data.read(1)
            value += data.read(4)
            if end == "0":
                break
        value = int(value, 2)
        return value
    else:
        length_type = int(data.read(1), 2)
        if length_type == 0:
            length = int(data.read(15), 2)
            content = data.read(length)
            sub_data = io.StringIO(content)
            values = []
            while sub_data.tell() < len(content):
                values.append(parse_data(sub_data))
            return action(values, type_id)
        else:
            length = int(data.read(11), 2)
            values = []
            for _ in range(length):
                values.append(parse_data(data))
            return action(values, type_id)


def main():
    data = read_file()
    print(data.read())
    data.seek(0)
    total_version = 0
    total_version = parse_data(data)

    print("total version", total_version)


if __name__ == "__main__":
    main()


"""
100 010 1 00000000001 001 010 1 00000000001 101 010 0 000000000001011 110 100 0 1111 000

011 000 1 00000000010 00000000000000000101100001000101010110001011001000100000000010000100011000111000110100

"""