from typing import Optional, List


def read_file(filename="input.txt"):
    total = []
    with open(filename, "r") as fh:
        for line in fh.readlines():
            # print(line)
            result = line.split()
            total.append(result)
    return total


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


def main():
    data = read_file()
    print(data)
    total = []
    value = "9" * 14
    alu = ALU(value)
    z = 0

    for index, instruction in enumerate(data):
        if instruction[0] == "inp" and index == 10:
            alu.z = int(value[13])  # 234
            alu.z = (alu.z) * 26 + 11 + int(value[12])  # 216
            alu.z = alu.z * 26 + int(value[11])  # 198
            alu.z = alu.z * 26 + int(value[10]) + 13  # 180
            alu.z = (alu.z - 7 - int(value[9])) // 26  # 162
            print(alu.z)
            alu.z = (alu.z - 15 - int(value[8])) // 26  # 144
            print(alu.z)
            alu.z = (alu.z - 12 - int(value[7])) * (26 if int(value[7]) != 6 else 1)  # 126
            print(alu.z)
            alu.z = (alu.z - 17 - int(value[6])) // 26  # 108
            print(alu.z)
            print(value[6])
        alu.execute(instruction)
        if instruction[0] == "inp":
            print("step", index, instruction, ":", alu, alu.z - z)
        if instruction[0] == "inp":
            # print("step", index, instruction, ":", alu, alu.z - z)
            z = alu.z
    print(alu)


def main2():
    for x in range(99999999999999, 10000000000000, -1):
        if "0" in str(x):
            if x % 10000 == 0:
                print(x)
            continue
        z = calculate_z(str(x))
        if z == 0:
            print("solution", x)
            break

"11111116111757"


def calculate_z(number: str):
    assert len(number) == 14
    z = int(number[0]) + 1
    z = z * 26 + 10 + int(number[1])
    z = z * 26 + 2 + int(number[2])
    z = z // 26 if z % 26 - 10 == int(number[3]) else z // 26 * 26 + 5 + int(number[3])
    z = z * 26 + 6 + int(number[4])
    z = z * 26 + int(number[5])
    z = z * 26 + 16 + int(number[6])
    z = z // 26 if z % 26 - 11 == int(number[7]) else z // 26 * 26 + int(number[7]) + 12
    z = z // 26 if z % 26 - 7 == int(number[8]) else z // 26 * 26 + int(number[8]) + 15
    z = z * 26 + 7 + int(number[9])
    z = z // 26 if z % 26 - 13 == int(number[10]) else z // 26 * 26 + int(number[10]) + 6
    z = z // 26 if z % 26 == int(number[11]) else z // 26 * 26 + int(number[11]) + 5
    z = z // 26 if z % 26 - 11 == int(number[12]) else z // 26 * 26 + 6 + int(number[12])
    z = z // 26 if z % 26 == int(number[13]) else z // 26 * 26 + 15 + int(number[13])
    return z


if __name__ == "__main__":
    main2()



# attempt 1 : 89913849193989