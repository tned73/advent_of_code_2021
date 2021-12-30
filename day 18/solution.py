from typing import List, Union, Optional


def read_file(filename="input.txt"):
    with open(filename, "r") as fh:
        return [eval(line) for line in fh.readlines()]


class Node:
    parent: Optional["Node"]
    left: Union[int, "Node"]
    right: Union[int, "Node"]

    def __init__(self, input: List, node:  Optional["Node"] = None):
        self.parent = node
        self.left = Node(input[0], self) if type(input[0]) == list else input[0]
        if type(self.left) != int:
            self.left.parent = self
        self.right = Node(input[1], self) if type(input[1]) == list else input[1]
        if type(self.right) != int:
            self.right.parent = self

    def __str__(self):
        return "[" + str(self.left) + ", " + str(self.right) + "]"

    def is_int_node(self):
        return type(self.left) == int and type(self.right) == int

    def set_child_zero(self, node):
        if self.left == node:
            self.left = 0
        if self.right == node:
            self.right = 0

    def left_int_add(self, value):
        if self.parent is None:
            return
        if self == self.parent.left:
            return self.parent.left_int_add(value)
        if self == self.parent.right:
            if type(self.parent.left) == int:
                self.parent.left += value
                return
            return self.parent.left.assend_right(value)

    def assend_right(self, value):
        if type(self.right) == int:
            self.right += value
            return
        return self.right.assend_right(value)

    def right_int_add(self, value):
        if self.parent is None:
            return
        if self == self.parent.right:
            return self.parent.right_int_add(value)
        if self == self.parent.left:
            if type(self.parent.right) == int:
                self.parent.right += value
                return
            return self.parent.right.assend_left(value)

    def assend_left(self, value):
        if type(self.left) == int:
            self.left += value
            return
        return self.left.assend_left(value)

    def reduce(self, level=0):
        if self.is_int_node() and level >= 4:
            self.left_int_add(self.left)
            self.right_int_add(self.right)
            self.parent.set_child_zero(self)
            return True
        else:
            if type(self.left) != int:
                state = self.left.reduce(level + 1)
                if state:
                    return state
            if type(self.right) != int:
                return self.right.reduce(level + 1)

    def split_number(self, value):
        left = value // 2
        right = value - left
        return Node([left, right], node=self)

    def split(self):
        if type(self.left) != int:
            state = self.left.split()
            if state:
                return state
        if type(self.left) == int and self.left >= 10:
            self.left = self.split_number(self.left)
            return True

        if type(self.right) != int:
            state = self.right.split()
            if state:
                return state
        if type(self.right) == int and self.right >= 10:
            self.right = self.split_number(self.right)
            return True

    def magnitude(self):
        left = self.left if type(self.left) == int else self.left.magnitude()
        right = self.right if type(self.right) == int else self.right.magnitude()
        return left * 3 + right * 2


def main():
    data = read_file()
    print(data)
    result = None
    for snail_number in data:
        el = Node(snail_number)
        if result is None:
            result = el
        else:
            result = Node([result, snail_number])
        while result.reduce() or result.split():
            pass

    print(result)
    print(result.magnitude())


def main_step_2():
    data = read_file()
    # print(data)
    max_magnitude = []
    for snail_number in data:
        for number_snail in data:
            if snail_number == number_snail:
                continue
            result = Node([snail_number, number_snail])
            while result.reduce() or result.split():
                pass
            max_magnitude.append(result.magnitude())
    print(max(max_magnitude))


if __name__ == "__main__":
    main()
    main_step_2()
