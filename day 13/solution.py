def read_file(filename="input.txt"):
    result = {}
    with open(filename, "r") as fh:
        for line in fh.readlines():
            tup = line.split(',')
            result.update({(int(tup[0]), int(tup[1])): "#"})
    return result


def fold(data, x=None, y=None):
    assert bool(x) != bool(y)
    for key in list(data.keys()):

        if y and key[1] > y:
            data.pop(key)
            data.update({(key[0], y - (key[1] - y)): "#"})
        if x and key[0] > x:
            data.pop(key)
            data.update({(x - (key[0] - x), key[1]): "#"})


def max_(data):
    x = 0
    y = 0
    for key in data:
        if key[0] > x:
            x = key[0]
        if key[1] > y:
            y = key[1]
    return x, y


def print_data(data):
    max_x, max_y = max_(data)
    print(max_(data))
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(data.get((x, y), "."), end="")
        print("", end="\n")


def main():
    data = read_file()
    print(data)
    fold(data, x=655)
    print(len(data))
    fold(data, y=447)
    fold(data, x=327)
    fold(data, y=223)
    fold(data, x=163)
    fold(data, y=111)
    fold(data, x=81)
    fold(data, y=55)
    fold(data, x=40)
    fold(data, y=27)
    fold(data, y=13)
    fold(data, y=6)
    print(data)

    print_data(data)


if __name__ == "__main__":
    main()
