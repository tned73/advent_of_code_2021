from datetime import datetime


def read_file(filename="input_example.txt"):
    total = []
    with open(filename, "r") as fh:
        for line in fh.readlines():
            # print(line)
            result = [int(i) for i in line.split()[0]]
            total.append(result)
    return total


def throw(worp):
    value = worp % 100 + 1
    # print("worp", value)
    return value


class QThrow():
    player1_pos: int = 4
    player1_score: int = 0
    player2_pos: int = 8
    player2_score: int = 0


def qthrow2(throw, round=0, p1_pos=4, p1_score=0, p2_pos=7, p2_score=0, throws=0):
    player = round % 2
    if player == 0:
        p1_pos = (p1_pos + throw) % 10
        p1_score += p1_pos if p1_pos > 0 else 10
        if p1_score >= 21:
            # print("round", round, 0)
            yield 0, throws
    else:
        p2_pos = (p2_pos + throw) % 10
        p2_score += p2_pos if p2_pos > 0 else 10
        if p2_score >= 21:
            # print("round", round, 1)
            yield 1, throws

    if p1_score < 21 and p2_score < 21:
        for x, y in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
            yield from qthrow2(x, round=round + 1, p1_pos=p1_pos, p1_score=p1_score, p2_pos=p2_pos, p2_score=p2_score,
                               throws=throws * y)


def points(throws):
    value = sum([throw(throws + x) for x in range(3)])
    print("3 worp", value)
    return value


def main():
    data = [0, 0]
    position = [4, 7]
    print(data)
    throws = 0
    player = 0
    while True:
        pos = (position[player] + points(throws)) % 10
        data[player] += pos if pos > 0 else 10
        position[player] = pos
        print(f"player {player}", pos if pos > 0 else 10, data[player])
        throws += 3
        if data[player] >= 1000:
            break
        player = (player + 1) % 2
    print(data, throws)
    print(data[1] * throws)


def main_2():
    won = [0, 0]
    print(datetime.now())
    for x, y in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
        print(x, y)
        for th in qthrow2(x, throws=y):
            won[th[0]] += th[1]
    print(datetime.now())

    print(won)



if __name__ == "__main__":
    # main()
    main_2()
