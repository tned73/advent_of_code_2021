from typing import List


def read_file(filename="input.txt") -> List[str]:
    total = []
    with open(filename, "r") as fh:
        for line in fh.readlines():
            # print(line)
            result = [int(i) for i in line.split()[0]]
            total.append(result)
    return total

def get_value(data, x, y) -> List[int]:
    if x<0 or y<0:
        return []
    try:
        return [data[y][x]]
    except IndexError:
        return []

def low_point(data, x, y) -> bool:
    value = data[y][x]
    adjecent = []
    adjecent.extend(get_value(data,x-1,y))
    adjecent.extend(get_value(data,x+1,y))
    adjecent.extend(get_value(data,x,y-1))
    adjecent.extend(get_value(data,x,y+1))
    result = all([i>value for i in adjecent])
    # print(x, y, adjecent, value, result)
    return result

def search_y(data, x, y, dir) -> int:
    size = 0
    start_y = y
    while ridge(data, x, start_y):
        size += 1
        print(x,start_y)
        start_y += dir
    print(f"finish y {dir}", size)
    return size

def valid_value(data, x, y) -> bool:
    value = get_value(data, x, y)
    print(value, x, y)
    if value and value[0] < 9:
        return True

class Basin():

    def __init__(self, data):
        self.data=data
        self.coords = []

    def lake(self, x, y) -> None:
        self.coords.append([x, y])
        for xx in [-1, 1]:
            if valid_value(self.data, x+xx, y):
                    if [x+xx, y] not in self.coords:
                        self.lake(x+xx, y)
        for yy in [-1, 1]:
            if valid_value(self.data, x, y+yy):
                    if [x, y+yy] not in self.coords:
                        self.lake(x, y+yy)

    def size(self):
        return len(self.coords)


def main():
    data = read_file()
    print(data)
    totaal = 0
    result = []
    for x in range(len(data[0])):
        for y in range(len(data)):
            if low_point(data, x, y):
                print(data[y][x], x, y)
                totaal += data[y][x] + 1
                basin = Basin(data)
                basin.lake(x, y)
                print(basin.size())
                result.append(basin.size())
    print(totaal)
    print(result)
    result.sort(reverse=True)
    print((result[0:3]))
    print(result[0]*result[1]*result[2])


if __name__ == "__main__":
    main()
