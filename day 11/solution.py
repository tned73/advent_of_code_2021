from typing import List


def read_file(filename="input.txt"):
    total = []
    with open(filename, "r") as fh:
        for line in fh.readlines():
            # print(line)
            result = [int(i) for i in line.split()[0]]
            total.append(result)
    return total


def print_raster(raster):
    for x in range(len(raster)):
        print([raster[x][y] for y in range(len(raster))])
    print()


def update_energy(data):
    for x in range(len(data)):
        for y in range(len(data)):
            data[x][y] += 1


def get_value(data, x, y) -> int:
    if x < 0 or y < 0:
        return 0
    try:
        return data[x][y]
    except IndexError:
        return 0


def flash(data, x, y):
    flashes = 0
    if get_value(data, x, y) >= 10:
        flashes += 1
        data[x][y] = 0
        for xx in (-1, 0, 1):
            for yy in (-1, 0, 1):
                if get_value(data, x + xx, y + yy) > 0:
                    data[x + xx][y + yy] += 1
                    flashes += flash(data, x + xx, y + yy)
    return flashes


def flash_check(data):
    flashes = 0
    for x in range(len(data)):
        for y in range(len(data)):
            flashes += flash(data, x, y)
    print_raster(data)
    for x in range(len(data)):
        for y in range(len(data)):
            if data[x][y] > 9:
                data[x][y] = 0
    return flashes


def main():
    data = read_file()
    print_raster(data)
    flashes = 0
    i= 0
    while flashes<100:
        i += 1
        print("step", i)
        update_energy(data)
        flashes = flash_check(data)
        print_raster(data)
    print(flashes)


if __name__ == "__main__":
    main()
