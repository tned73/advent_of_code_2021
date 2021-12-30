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



import heapq


def dijkstra(adj, start, target):
    d = {start: 0}
    parent = {start: None}
    pq = [(0, start)]
    visited = set()
    while pq:
        du, u = heapq.heappop(pq)
        if u in visited: continue
        if u == target:
            break
        visited.add(u)
        for v, weight in adj[u]:
            if v not in d or d[v] > du + weight:
                d[v] = du + weight
                parent[v] = u
                heapq.heappush(pq, (d[v], v))

    return parent, d


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
            for xx in (1, -1):
                distance = get_value(data, x + xx, y)
                # print(x, y, distance, x + xx, y)
                if distance:
                    lijst.append(((x + xx, y), distance))

            for yy in (1,-1 ):
                distance = get_value(data, x, y + yy)
                # print(x, y, distance, x, y+yy)
                if distance:
                    lijst.append(((x, y + yy), distance))
    result = dijkstra(adjac_lis, (0,0), (size_x-1, size_y-1))
    # print(result)
    print(result[1][(size_x-1, size_y-1)])
    path = []
    s = (size_x-1, size_y-1)
    while s:
        path.append(s)
        s = result[0][s]
    print(path)
    print_raster(data, path)


if __name__ == "__main__":
    main()
