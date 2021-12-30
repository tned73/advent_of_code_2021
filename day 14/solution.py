from collections import Counter


def read_file(filename="input.txt"):
    result = {}
    with open(filename, "r") as fh:
        for line in fh.readlines():
            tup = line.split('->')
            result.update({tup[0].strip(): tup[1].split()[0]})
    return result


def ultimate_polymer(data, start):
    sett = ""
    result = []
    for letter in start:
        sett = sett[-1:] + letter
        if len(sett) == 2:
            result.append(sett)
    return Counter(result)


def ultimate_polymer_extend(data, counter):
    result = Counter()
    for key in counter:
        value = counter[key]
        key1 = key[0] + data[key]
        key2 = data[key] + key[1]
        result = result + Counter({key1: value, key2: value})
    return result


def main():
    data = read_file()
    print(data)
    # start = "NNCB" # example
    start = "OOBFPNOPBHKCCVHOBCSO"
    result = ultimate_polymer(data, start)
    for _ in range(40):
        result = ultimate_polymer_extend(data, result)
    print(result)
    total = Counter()
    for key in result.keys():
        total += Counter({key[0]: result[key]})
    total += Counter({start[-1]: 1})
    result = total.most_common()
    print(result)
    print(result[0][1] - result[-1][1])


if __name__ == "__main__":
    main()
