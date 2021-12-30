from collections import Counter
from typing import Tuple, List

ROTATIONS = [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 1, 3), (0, 2, 0),
             (0, 2, 1), (0, 2, 2), (0, 2, 3), (0, 3, 0), (0, 3, 1), (0, 3, 2), (0, 3, 3), (1, 0, 0), (1, 0, 1),
             (1, 0, 2), (1, 0, 3), (1, 2, 0), (1, 2, 1), (1, 2, 2), (1, 2, 3)]


def read_file(filename="input.txt") -> List[List[Tuple[int, int, int]]]:
    total = []
    scanner = []
    with open(filename, "r") as fh:
        for line in fh.readlines():
            # print(line)
            if line[:3] == "---":
                if scanner:
                    total.append(scanner)
                scanner = []
                continue
            if line.split():
                result = tuple([int(i) for i in line.split()[0].split(",")])
                scanner.append(result)
        total.append(scanner)
    return total


def rotation_x(b):
    return (b[0], b[2], -b[1])


def rotation_y(b):
    return (b[2], b[1], -b[0])


def rotation_z(b):
    return (b[1], -b[0], b[2])


def rotation(beacon: Tuple[int, int, int], rot: Tuple[int, int, int]) -> Tuple[int, int, int]:
    for _ in range(rot[0]):
        beacon = rotation_x(beacon)
    for _ in range(rot[1]):
        beacon = rotation_y(beacon)
    for _ in range(rot[2]):
        beacon = rotation_z(beacon)
    return beacon


def rotations(beacons: List[Tuple[int, int, int]], rot: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
    return [rotation(beacon, rot) for beacon in beacons]


def rel_distance(beacons, temp_rotation):
    distance = []
    for beac_o in beacons:
        for beac_t in temp_rotation:
            distance.append((beac_o[0] - beac_t[0], beac_o[1] - beac_t[1], beac_o[2] - beac_t[2]))
    return distance


def translate(beacons, offset):
    result = []
    for beacon in beacons:
        result.append((beacon[0] + offset[0], beacon[1] + offset[1], beacon[2] + offset[2]))
    return result


def manhattan_distance(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def main():
    data = read_file()
    print(data)
    beacons = set(data[0])
    index_list = list(range(1, len(data)))
    scanners = [(0, 0, 0)]
    for index in index_list:
        scanner = data[index]
        print("scanner", index)
        relative_distance = []
        for rot in ROTATIONS:
            temp_rotation = rotations(scanner, rot)
            distance = rel_distance(beacons, temp_rotation)
            counter = Counter(distance)
            relative_distance.append([counter.most_common(1)[0], rot])
        # print("relative", relative_distance)
        max_match = max([koppel[0][1] for koppel in relative_distance])
        if max_match <= 4:
            # if not matching at all reevaluate
            index_list.append(index)
            continue
        koppel = next(filter(lambda x: x[0][1] == max_match, relative_distance))
        print("matching", koppel)
        scanners.append(koppel[0][0])
        beacons |= set(translate(rotations(scanner, koppel[1]), koppel[0][0]))
    # print(beacons)
    print("answer step 1", len(beacons))
    assert len(beacons) == 496
    result = []
    for a in scanners:
        for b in scanners:
            result.append(manhattan_distance(a, b))
    print("answer step 2", max(result))
    assert max(result) == 14478


if __name__ == "__main__":
    main()
