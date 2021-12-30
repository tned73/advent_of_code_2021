from statistics import mean
from typing import List


def read_file(filename="input_7.txt") -> List[int]:
    with open(filename, "r") as fh:
        data = fh.read()
    return [int(i) for i in data.split(",")]


def fuel(i,x) -> int:
    max = abs(i-x)
    return int((1+max) * (max / 2))


def main():
    data = read_file()
    print(data)
    results = [0] * max(data)
    for i in range(max(data)):
        results[i] = sum([fuel(i,x) for x in data])

    print(results)
    print(min(results))


if __name__ == "__main__":
    main()
