def read_file(filename="input.txt"):
    total = []
    with open(filename, "r") as fh:
        for line in fh.readlines():
            # print(line)
            result = [j for i in line.split() for j in i]
            total.append(result)
    return total


def convert(data):
    result = {}
    for y, row in enumerate(data):
        for x, field in enumerate(row):
            if field != ".":
                result[(x, y)] = field
    return result, x + 1, y + 1


def select_east(data, max_x):
    result = set()
    for x, y in data:
        if data[(x, y)] == ">":
            open_space = ((x + 1) % max_x, y)
            if open_space not in data:
                result |= {((x, y), open_space)}
    return result


def move(data, steps):
    for old, new in steps:
        c = data[old]
        data.pop(old)
        data[new] = c
    return data


def select_south(data, max_y):
    result = set()
    for x, y in data:
        if data[(x, y)] == "v":
            open_space = (x, (y + 1) % max_y)
            if open_space not in data:
                result |= {((x, y), open_space)}
    return result


def print_field(data, max_x, max_y):
    for y in range(max_y):
        for x in range(max_x):
            print(data.get((x, y), "."), end="")
        print("", end="\n")
    print()


def main():
    data = read_file()
    print(data)
    data, max_x, max_y = convert(data)
    print_field(data, max_x, max_y)
    steps = 0
    while True:
        steps += 1
        step_east = select_east(data, max_x)
        data = move(data, step_east)
        # print_field(data, max_x, max_y)
        step_south = select_south(data, max_y)
        data = move(data, step_south)
        print_field(data, max_x, max_y)
        if not step_east and not step_south:
            break
    print(steps)


if __name__ == "__main__":
    main()
