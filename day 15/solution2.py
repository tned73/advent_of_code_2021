from collections import deque


def read_file(filename="input.txt"):
    total = []
    with open(filename, "r") as fh:
        for line in fh.readlines():
            # print(line)
            result = [int(i) for i in line.split()[0]]
            total.append(result)
    return total


class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_neighbors(self, v):
        return self.adjac_lis[v]

    # This is heuristic function which is having equal values for all nodes
    def h(self, n):
        return 0

    def a_star_algorithm(self, start, stop):
        # In this open_lst is a lisy of nodes which have been visited, but who's
        # neighbours haven't all been always inspected, It starts off with the start
        # node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        closed_lst = set([])

        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0

        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start

        while len(open_lst) > 0:
            n = None

            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []

                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]

                reconst_path.append(start)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)

        print('Path does not exist!')
        return None


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


def get_value(data, x, y) -> int:
    if x < 0 or y < 0:
        return
    try:
        return data[y][x]
    except IndexError:
        return


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


def main():
    data = read_file()
    data = expand_data(data)
    print_raster(data)
    size_x = len(data[0])
    size_y = len(data)
    print(size_x, size_y)
    adjac_lis = {}
    for x in range(size_x):
        for y in range(size_y):
            lijst = []
            adjac_lis[(x, y)] = lijst
            for xx in (1,):
                distance = get_value(data, x + xx, y)
                # print(x, y, distance, x + xx, y)
                if distance:
                    lijst.append(((x + xx, y), distance))

            for yy in (1,):
                distance = get_value(data, x, y + yy)
                # print(x, y, distance, x, y+yy)
                if distance:
                    lijst.append(((x, y + yy), distance))

    graph1 = Graph(adjac_lis)
    path = graph1.a_star_algorithm((0, 0), (size_x - 1, size_y - 1))
    print_raster(data, path)
    print(len(path))
    value = -get_value(data, 0, 0)
    for step in set(path):
        value += get_value(data, step[0], step[1])
    print(value)


if __name__ == "__main__":
    main()
