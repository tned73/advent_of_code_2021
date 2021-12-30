import re


def read_file(filename="input.txt"):
    total = []
    with open(filename, "r") as fh:
        for line in fh.readlines():
            effe = line.rstrip()
            if effe:
                total.append(effe)
    return total


pattern = re.compile(
    r"(?P<action>((\bon\b)|(\boff\b))) x=(?P<xmin>[-0-9]*)\.\.(?P<xmax>[-0-9]*),y=(?P<ymin>[-0-9]*)\.\.(?P<ymax>[-0-9]*),z=(?P<zmin>[-0-9]*)\.\.(?P<zmax>[-0-9]*)")


def subtract_range(a, b, c, d):
    if a < c:
        yield a, c - 1
    if d < b:
        yield d + 1, b


class ReactorCube:
    def __init__(self, line: str = None, **kwargs):
        if line:
            match = re.search(pattern, line)
            result = match.groupdict()
        else:
            result = kwargs
        self.action = result.get("action", "on")
        self.xmin = int(result["xmin"])
        self.xmax = int(result["xmax"])
        self.ymin = int(result["ymin"])
        self.ymax = int(result["ymax"])
        self.zmin = int(result["zmin"])
        self.zmax = int(result["zmax"])

        self.outside = int(result["xmax"]) < -50 or int(result["xmin"]) > 50 or int(result["ymax"]) < -50 or int(
            result["ymin"]) > 50 or int(result["zmax"]) < -50 or int(result["zmin"]) > 50

    def is_valid(self):
        return not (self.xmin > self.xmax or self.ymin > self.ymax or self.zmin > self.zmax)

    def __repr__(self):
        return f"{self.action} x={self.xmin}..{self.xmax},y={self.ymin}..{self.ymax},z={self.zmin}..{self.zmax}"

    def cubes(self):
        return abs(self.xmax - self.xmin + 1) * abs(self.ymax - self.ymin + 1) * abs(self.zmax - self.zmin + 1)

    def subtract(self, other):
        overlap = self.overlap(other)
        if overlap:
            yield from self.divide(overlap)
        else:
            yield self

    def divide(self, overlap):
        for xmin, xmax in subtract_range(self.xmin, self.xmax, overlap.xmin, overlap.xmax):
            yield ReactorCube(xmin=xmin, xmax=xmax, ymin=self.ymin, ymax=self.ymax, zmin=self.zmin, zmax=self.zmax)
        for ymin, ymax in subtract_range(self.ymin, self.ymax, overlap.ymin, overlap.ymax):
            yield ReactorCube(xmin=overlap.xmin, xmax=overlap.xmax, ymin=ymin, ymax=ymax, zmin=self.zmin,
                              zmax=self.zmax)
        for zmin, zmax in subtract_range(self.zmin, self.zmax, overlap.zmin, overlap.zmax):
            yield ReactorCube(xmin=overlap.xmin,
                              xmax=overlap.xmax,
                              ymin=overlap.ymin,
                              ymax=overlap.ymax,
                              zmin=zmin,
                              zmax=zmax)

    def overlap(self, other):
        cube = ReactorCube(
            xmin=max(self.xmin, other.xmin),
            xmax=min(self.xmax, other.xmax),
            ymin=max(self.ymin, other.ymin),
            ymax=min(self.ymax, other.ymax),
            zmin=max(self.zmin, other.zmin),
            zmax=min(self.zmax, other.zmax))
        if cube.is_valid():
            return cube


def main():
    data = read_file()
    actions = iter([ReactorCube(line) for line in data])
    cubes = [next(actions)]
    for actie in actions:
        new_list = []
        for cube in cubes:
            new_list.extend(cube.subtract(actie))
        if actie.action == "on":
            new_list.append(actie)
        cubes = new_list
    totaal = 0
    for cube in cubes:
        print(cube, cube.cubes())
        totaal += cube.cubes()
    print(totaal)


if __name__ == "__main__":
    main()
