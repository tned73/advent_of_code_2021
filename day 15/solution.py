from dijkstra import Graph, dijkstra, shortest


def read_file(filename="input.txt"):
    total = []
    with open(filename, "r") as fh:
        for line in fh.readlines():
            # print(line)
            result = [int(i) for i in line.split()[0]]
            total.append(result)
    return total


def cap_value(value):
    div = value // 10
    mod = value % 10
    return mod + div


def expand_data(data):
    xsize = len(data[0])
    ysize = len(data)
    row = [0] * xsize * 5
    result = []
    for _ in range(ysize * 5):
        result.append(row.copy())
    for yindex, row in enumerate(data):
        for xindex, value in enumerate(row):
            for xx in range(5):
                for yy in range(5):
                    result[yindex + ysize * yy][xindex + xsize * xx] = cap_value(value + yy + xx)
    return result


def bold(string, bold):
    if bold:
        return "\033[92m" + str(string) + "\033[0m"
    return str(string)


def print_raster(raster, path=None):
    size_x = len(raster[0])
    size_y = len(raster)
    print(size_x, size_y)
    if path is None:
        path = []
    for y in range(len(raster)):
        for x in range(len(raster)):
            b = (x, y) in path
            print(bold(get_value(raster, x, y), b), end="")
        print("", end="\n")
    print()


def get_value(data, x, y) -> int:
    if x < 0 or y < 0:
        return
    try:
        return data[y][x]
    except IndexError:
        return


def main():
    data = read_file()
    data = expand_data(data)
    print_raster(data)
    size_x = len(data[0])
    size_y = len(data)
    print(size_x, size_y)
    g = Graph()
    for y in range(size_y):
        for x in range(size_x):
            g.add_vertex((x, y))

    for x in range(size_x):
        for y in range(size_y):
            for xx in (1,-1):
                distance = get_value(data, x + xx, y)
                # print(x, y, distance, x + xx, y)
                if distance:
                    g.add_edge((x, y), (x + xx, y), distance)

            for yy in (1,-1):
                distance = get_value(data, x, y + yy)
                # print(x, y, distance, x, y+yy)
                if distance:
                    g.add_edge((x, y), (x, y + yy), distance)

    # print('Graph data:')
    # for v in g:
    #     for w in v.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print('( %s , %s, %3d)' % (vid, wid, v.get_weight(w)))

    dijkstra(g, g.get_vertex((0, 0)))

    target = g.get_vertex((size_x - 1, size_y - 1))
    path = [target.get_id()]
    shortest(target, path)
    print('The shortest path : %s' % (path[::-1]))
    print(target.distance)
    print_raster(data, path)
    print(target.distance)


if __name__ == "__main__":
    main()

## part one
# 731 to low
# 759 to high
# 741 was correct


##part two
# 2990 to high
# guess 2900 to low
# guess 2980 to high
# guess 2940 incorrect