from datetime import datetime
from typing import List


def read_file(filename="input_6.txt") -> List[int]:
    with open(filename, "r") as fh:
        data = fh.read()
    # return [int(i) for i in data.split(",")]
    # return [6]
    result = [0]*8
    for i in data.split(","):
        result[int(i)] += 1
    return result
# y = (x/7)*(y+1)
# y = (x-2)/7


def main():
    data = read_file()
    print(data)
    return

    for day in range(0, 264):
        print(datetime.now(), day, len(data))
        spawn = []
        for index, fish in enumerate(data):
            if fish == 0:
                data[index] = 6
                spawn.append(8)
            else:
                data[index] = fish - 1
        data.extend(spawn)
    # print(data)
    print(len(data))


if __name__ == "__main__":
    main()

6206821033 * 119 + 5617089148 * 45 + 5217223242* 48 + 4726100874 * 40 + 4368232009 * 48


