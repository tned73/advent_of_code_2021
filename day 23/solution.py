from typing import Tuple, List, Optional, Dict


def read_file():
    i = 1
    if i == 1:
        return {
            (0, 0): None,
            (0, 1): None,
            (0, 2): None,
            (0, 3): None,
            (0, 4): None,
            (0, 5): None,
            (0, 6): None,
            (0, 7): None,
            (0, 8): None,
            (0, 9): None,
            (0, 10): None,
            (1, 2): "B",
            (1, 4): "C",
            (1, 6): "A",
            (1, 8): "D",
            (2, 2): "B",
            (2, 4): "C",
            (2, 6): "D",
            (2, 8): "A",
        }
    if i == 2:
        return {
            (0, 0): None,
            (0, 1): None,
            (0, 2): None,
            (0, 3): None,
            (0, 4): None,
            (0, 5): None,
            (0, 6): None,
            (0, 7): None,
            (0, 8): None,
            (0, 9): None,
            (0, 10): None,
            (1, 2): "B",
            (1, 4): "C",
            (1, 6): "A",
            (1, 8): "D",
            (2, 2): "D",
            (2, 4): "C",
            (2, 6): "B",
            (2, 8): "A",
            (3, 2): "D",
            (3, 4): "B",
            (3, 6): "A",
            (3, 8): "C",
            (4, 2): "B",
            (4, 4): "C",
            (4, 6): "D",
            (4, 8): "A",
        }
    return {
        (0, 0): None,
        (0, 1): None,
        (0, 2): None,
        (0, 3): None,
        (0, 4): None,
        (0, 5): None,
        (0, 6): None,
        (0, 7): None,
        (0, 8): None,
        (0, 9): None,
        (0, 10): None,
        (1, 2): "B",
        (1, 4): "C",
        (1, 6): "B",
        (1, 8): "D",
        (2, 2): "D",
        (2, 4): "C",
        (2, 6): "B",
        (2, 8): "A",
        (3, 2): "D",
        (3, 4): "B",
        (3, 6): "A",
        (3, 8): "C",
        (4, 2): "A",
        (4, 4): "D",
        (4, 6): "C",
        (4, 8): "A",
    }


class Sort:
    column = {"A": 2, "B": 4, "C": 6, "D": 8}

    def __init__(self, data: Dict[Tuple[int, int], Optional[str]],
                 steps: List[Tuple[str, Tuple[int, int], Tuple[int, int]]]):
        self.data = data
        self.steps = steps
        self.bottom = max([pos[0] for pos in self.data])
        print(self.__repr__())

    def __repr__(self):
        return str(self.steps) + "\n" + "#" * 13 + "\n#" + "".join([self.string((0, x)) for x in range(0, 11)]) \
               + "#\n" + self.caves() + \
               "  #########\n" +\
               str(self.close_to_solution()) + "  " + str(self.total_energy())

    def caves(self):
        string = ""
        for line in range(1, self.bottom + 1):
            string += "###" if line == 1 else "  #"
            string += "#".join([self.string((line, x)) for x in [2, 4, 6, 8]])
            string += "###" if line == 1 else "#  "
            string += "\n"
        return string

    def string(self, pos):
        kar = self.data[pos] if self.data[pos] else "."
        if self.steps and (pos in self.steps[-1]):
            return "\033[32m" + kar + "\033[0m"
        if self.data[pos] and pos[1] == self.column[self.data[pos]] and all(
                [self.data[(x, pos[1])] == kar for x in range(pos[0], self.bottom + 1)]):
            return "\033[92m" + kar + "\033[0m"
        return kar

    def is_sorted(self):
        return all(
            [self.data[(y, self.column[atype])] == atype for y in range(1, self.bottom + 1) for atype in self.column])

    def get_movable(self):
        if self.is_sorted():
            yield self
        for pos in sorted(self.data, reverse=True):
            if self.data[pos]:
                atype = self.data[pos]
                previous = self.steps[-1][2] if len(self.steps) > 0 and atype == self.steps[-1][0] else pos
                for next_pos in self.get_next_pos(pos, previous, atype):
                    data = self.data.copy()
                    data[pos] = None
                    data[next_pos] = atype
                    yield Sort(data, self.steps + [(atype, pos, next_pos)])

    def get_next_pos(self, pos: Tuple[int, int], previous: Tuple[int, int], atype: str):
        if all([self.data[(y, self.column[atype])] in [atype, None] for y in range(1, self.bottom + 1)]) and pos[1] != \
                self.column[atype]:
            if all([self.data[(up, pos[1])] is None for up in range(pos[0] - 1, 0, -1)]):
                richting = 1 if self.column[atype] > pos[1] else -1
                if all([self.data[(0, step)] is None for step in
                        range(pos[1] + richting, self.column[atype], richting)]):
                    for y in range(self.bottom, 0, -1):
                        if self.data[(y, self.column[atype])] is None:
                            yield (y, self.column[atype])
                            break
        else:
            if pos[0] > 0:
                up_pos = (pos[0] - 1, pos[1])
                if self.data[up_pos] is None and (pos[1] != self.column[atype] or not all(
                        [self.data[(y, pos[1])] == atype for y in range(pos[0], self.bottom + 1)])):
                    for end_pos in range(pos[1], -1, -1):
                        if end_pos in [2, 4, 6, 8]:
                            continue
                        if self.data[(0, end_pos)] is not None:
                            break
                        yield (0, end_pos)
                    for end_pos in range(pos[1], 11, 1):
                        if end_pos in [2, 4, 6, 8]:
                            continue
                        if self.data[(0, end_pos)] is not None:
                            break
                        yield (0, end_pos)
            else:
                if previous[1] > pos[1]:
                    for end_pos in range(pos[1] - 1, -1, -1):
                        if end_pos in [2, 4, 6, 8]:
                            continue
                        if self.data[(0, end_pos)] is not None:
                            break
                        yield (0, end_pos)
                if previous[1] < pos[1]:
                    for end_pos in range(pos[1] + 1, 11, 1):
                        if end_pos in [2, 4, 6, 8]:
                            continue
                        if self.data[(0, end_pos)] is not None:
                            break
                        yield (0, end_pos)

    @staticmethod
    def energy(step: Tuple[str, Tuple[int, int], Tuple[int, int]]) -> int:
        price = {"A": 1, "B": 10, "C": 100, "D": 1000}
        steps = abs(step[1][1] - step[2][1]) + step[1][0] + step[2][0]
        return price[step[0]] * steps

    def total_energy(self):
        return sum([self.energy(step) for step in self.steps])

    def close_to_solution(self):
        result = 0
        for y in [2, 4, 6, 8]:
            for x in range(self.bottom, 0, -1):
                if self.data[(x, y)] and self.column[self.data[(x, y)]] == y:
                    result += 1
                else:
                    break
        return result


def main():
    data = read_file()
    # print(data)
    # print("step 1", 20 * 1 + 10 * 10 + 10 * 100 + 10 * 1000, "ok")
    sort = Sort(data, [])
    total = []
    lijst = []
    low = 99999999999
    solution = 0
    work = [sort]
    solutions = []
    while True:
        new_work = []
        for elm in work:
            new_work.extend(elm.get_movable())
        costs = [elm.close_to_solution() for elm in new_work]
        solution = max(costs)
        solutions.extend(filter(lambda x: x.close_to_solution() == 4 * sort.bottom, new_work))
        new_work = list(
            filter(lambda x: solution - 2 <= x.close_to_solution() < 4 * sort.bottom,
                   new_work))
        work = new_work
        if not new_work:
            break
    print("#" * 50)
    print()
    costs = [elm.total_energy() for elm in solutions]
    min_cost = min(costs)
    print("minimum cost", min_cost)
    for elm in solutions:
        if elm.total_energy() == min_cost:
            print(elm)


if __name__ == "__main__":
    main()

## step 2 is to low 49172

result_step_1 = [
    ("D", (1, 8), (0, 7)),  # 2 * 1000
    ("A", (2, 8), (0, 9)),  # 3 * 1
    ("D", (0, 7), (2, 8)),  # 3 * 1000
    ("A", (1, 6), (0, 1)),  # 6 * 1
    ("D", (2, 6), (2, 8)),  # 5 * 1000
    ("C", (1, 4), (2, 6)),  # 5 * 100
    ("C", (2, 4), (1, 6)),  # 5 * 100
    ("B", (1, 2), (2, 4)),  # 5 * 10
    ("B", (2, 2), (1, 4)),  # 5 * 10
    ("A", (0, 1), (2, 2)),  # 3 * 1
    ("A", (0, 9), (1, 1)),  # 8 * 1

]  # 5 * 10

D = 10000
C = 1000
B = 100
A = 20
totaal = 11120
