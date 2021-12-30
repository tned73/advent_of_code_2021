from typing import List


def read_file(filename="input_5_example.txt") -> List[List[List[int]]]:
    with open(filename, "r") as fh:
        data = fh.read()
    lijst = []
    for line in data.splitlines():
        tuples = line.split("->")
        location = []
        for tup in tuples:
            location.append([int(pos) for pos in tup.strip().split(",")])
        lijst.append(location)
    return lijst


def print_raster(raster):
    for x in range(len(raster)):
        print([raster[y][x] for y in range(len(raster))])


def direction(x: int, y: int) -> int:
    if x < y:
        return 1
    if x > y:
        return -1
    return 0


def map_coords(coords):
    x = direction(coords[0][0], coords[1][0])
    y = direction(coords[0][1], coords[1][1])

    xx, yy = coords[0][0], coords[0][1]
    for teller in range(10000):
        xxx = xx + x*teller
        yyy = yy + y*teller
        yield xxx, yyy
        if xxx == coords[1][0] and yyy == coords[1][1]:
            break


def main():
    data = read_file()
    size = 10
    raster = [[0 for _ in range(size)] for _ in range(size)]
    for coords in data:
        for x, y in map_coords(coords):
                raster[x][y] += 1
    print_raster(raster)
    count = 0
    for column in raster:
        for field in column:
            if field > 1:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
