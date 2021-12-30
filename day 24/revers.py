# def test_reverse():
#     solution = [0]*14
#     z = 0
#     # step 14
#     solution[13] = 9
#     p = z
#     z = z + solution[13]
#     assert (z // 26 if z % 26 == solution[13] else z // 26 * 26 + 15 + solution[13]) == p
#     # step 13
#     solution[12] = 9
#     p = z
#     z = z * 26 + 11 + solution[12]
#     assert (z // 26 if z % 26 - 11 == solution[12] else z // 26 * 26 + 6 + solution[12]) == p
#     # step 12
#     solution[11] = 9
#     p = z
#     z = z * 26 + solution[11]
#     assert (z // 26 if z % 26 == solution[11] else z // 26 * 26 + solution[11] + 5) == p
#     # step 11
#     solution[10] = 3
#     p = z
#     z = z * 26 + solution[10] + 13
#     assert (z // 26 if z % 26 - 13 == solution[10] else z // 26 * 26 + solution[10] + 6) == p
#     # step 10
#     solution[9] = 9
#     p = z
#     z = (z - 7 - solution[9]) // 26
#     assert (z * 26 + 7 + solution[9]) == p
#     # step 9
#     solution[8] = 8
#     p = z
#     z = (z - 15 - solution[8]) // 26
#     assert (z // 26 if z % 26 - 7 == solution[8] else z // 26 * 26 + solution[8] + 15) == p
from typing import List


def read_file(filename="input.txt"):
    total = []
    with open(filename, "r") as fh:
        for line in fh.readlines():
            # print(line)
            result = line.split()
            total.append(result)
    return total


def calculate_z(number: str):
    assert len(number) == 14
    z = int(number[0]) + 1
    print(0, z, number[0])
    z = z * 26 + 10 + int(number[1])
    print(1, z, number[1])
    z = z * 26 + 2 + int(number[2])
    print(2, z, number[2])
    z = z // 26 if z % 26 - 10 == int(number[3]) else z // 26 * 26 + 5 + int(number[3])
    print(3, z, number[3])
    z = z * 26 + 6 + int(number[4])
    print(4, z, number[4])
    z = z * 26 + int(number[5])
    print(5, z, number[5])
    z = z * 26 + 16 + int(number[6])
    print(6, z, number[6])
    z = z // 26 if z % 26 - 11 == int(number[7]) else z // 26 * 26 + int(number[7]) + 12
    print(7, z, number[7])
    z = z // 26 if z % 26 - 7 == int(number[8]) else z // 26 * 26 + int(number[8]) + 15
    print(8, z, number[8])
    z = z * 26 + 7 + int(number[9])
    print(9, z, number[9])
    z = z // 26 if z % 26 - 13 == int(number[10]) else z // 26 * 26 + int(number[10]) + 6
    print(10, z, number[10])
    z = z // 26 if z % 26 == int(number[11]) else z // 26 * 26 + int(number[11]) + 5
    print(11, z, number[11])
    z = z // 26 if z % 26 - 11 == int(number[12]) else z // 26 * 26 + 6 + int(number[12])
    print(12, z, number[12])
    z = z // 26 if z % 26 == int(number[13]) else z // 26 * 26 + 15 + int(number[13])
    print(13, z, number[13])
    return z


def check(number):
    assert int(number[0]) + 1 == int(number[13]), "1 - 2"
    assert int(number[1]) - 1 == int(number[12]),  "2 - 1"
    assert int(number[2]) - 8 == int(number[3]),   "9 - 1"
    assert int(number[4]) + 6 == int(number[11]),   "1 - 7"
    assert int(number[5]) - 7 == int(number[8]),    "8 - 1"
    assert int(number[6]) + 5 == int(number[7]),   "1 - 6"
    assert int(number[9]) - 6 == int(number[10]), "7 - 1 "

"12911816171712"
class ALU:
    x = 0
    y = 0
    z = 0
    w = 0

    def __init__(self, numbers: ""):
        self.numbers = [int(number) for number in numbers]

    def __repr__(self):
        return f"w={self.w}, x={self.x}, y={self.y}, z={self.z}"

    def execute(self, command: List[str]):
        getattr(self, command[0])(command[1:])

    def inp(self, command):
        if self.numbers:
            value = self.numbers.pop(0)
        else:
            assert len(command[0]) == 1
            value = input("input>:")
        assert 0 < int(value) < 10
        setattr(self, command[0], int(value))

    def get_b_value(self, value: str):
        try:
            return int(value)
        except ValueError:
            return getattr(self, value)

    def add(self, command):
        b = self.get_b_value(command[1])
        a = getattr(self, command[0])
        setattr(self, command[0], a + b)

    def mul(self, command):
        b = self.get_b_value(command[1])
        a = getattr(self, command[0])
        setattr(self, command[0], a * b)

    def div(self, command):
        b = self.get_b_value(command[1])
        a = getattr(self, command[0])
        setattr(self, command[0], a // b)

    def mod(self, command):
        b = self.get_b_value(command[1])
        a = getattr(self, command[0])
        setattr(self, command[0], a % b)

    def eql(self, command):
        b = self.get_b_value(command[1])
        a = getattr(self, command[0])
        eq = 1 if a == b else 0
        setattr(self, command[0], eq)



def alu_z(number):
    data = read_file()
    alu = ALU(number)
    for index, instruction in enumerate(data):
        alu.execute(instruction)
    print(alu)


if __name__ == "__main__":
    number = "89913849193989"
    number = "89913949293989"  # biggest number
    number = "12911816171712"  # smallest number
    print(calculate_z(number))
    alu_z(number)
    check(number)


"""
2 - 3
6 - 7
5 - 8
9 - 10
4 - 11
1 - 12
0 - 13
"""
