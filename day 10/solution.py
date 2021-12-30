
from typing import List


def read_file(filename="input.txt") -> List[str]:
    total = []
    with open(filename, "r") as fh:
        for line in fh.readlines():
            # print(line)
            result = [i for i in line.split()[0]]
            total.append(result)
    return total


char_dict = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}

def faulty(line):
    stack = []
    for char in line:
        if char in ['(', '{', '[', '<']:
            stack.append(char_dict[char])
            continue
        open_char = stack.pop()
        if char != open_char:
            return char
    stack.reverse()
    return stack


price = {
    ')': 3,
    '}': 1197,
    ']': 57,
    '>': 25137
}

price_i = {
    ')': 1,
    '}': 3,
    ']': 2,
    '>': 4
}

def main():
    data = read_file()
    print(data)
    faulty_chars = []
    incomplete = []
    for line in data:
        result = faulty(line)
        if type(result) is list:
            incomplete.append(result)
        else:
            faulty_chars.append(result)
    print(faulty_chars)
    print(incomplete)
    total = 0
    for char in faulty_chars:
        if char in price:
            total += price[char]
    print(total)
    result = []
    for line in incomplete:
        total = 0
        for char in line:
            total = total * 5 + price_i[char]
        result.append(total)
    print(result)
    result.sort()
    print(result[int((len(result)-1)/2)])


if __name__ == "__main__":
    main()
