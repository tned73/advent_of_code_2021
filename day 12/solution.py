from collections import Counter


def read_file(filename="input_example.txt"):
    total = []
    with open(filename, "r") as fh:
        for line in fh.readlines():
            result = [i.strip() for i in line.split('-')]
            total.append(result)
    return total


def build_dict(data):
    dic = {}
    for dat in data:
        if dat[0] in dic:
            dic[dat[0]].append(dat[1])
        else:
            dic[dat[0]] = [dat[1]]
        if dat[1] in dic:
            dic[dat[1]].append(dat[0])
        else:
            dic[dat[1]] = [dat[0]]
    return dic


def build_paths(dictionery, key, path=None):
    if path is None:
        path = []
    for i in dictionery[key]:
        if path == [] or (i != "start"):
            p = [j for j in path]
            p.append(i)
            if i == 'end':
                print(path)
                yield path
                continue
            lijst = Counter(p)
            for li in [item for item in lijst.keys()]:
                if li.upper() == li:
                    lijst.pop(li)
            lij = Counter(lijst.values())
            if not (3 in lij or lij[2] > 1):
                yield from build_paths(dictionery, i, path=p)


def main():
    data = read_file()
    # print(data)
    dictionery = build_dict(data)
    print(dictionery)
    paths = [p for p in build_paths(dictionery, 'start')]
    print(paths)
    print(len(paths))


if __name__ == "__main__":
    main()
