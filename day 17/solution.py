from dataclasses import dataclass

start = (0, 0)
target = (211, 232, -124, -69)
# target = (20, 30, -10, -5)  # example

exmaple_result = [
    (23, -10), (25, -9), (27, -5), (29, -6), (22, -6), (21, -7), (9, 0), (27, -7), (24, -5),
    (25, -7), (26, -6), (25, -5), (6, 8), (11, -2), (20, -5), (29, -10), (6, 3), (28, -7),
    (8, 0), (30, -6), (29, -8), (20, -10), (6, 7), (6, 4), (6, 1), (14, -4), (21, -6),
    (26, -10), (7, -1), (7, 7), (8, -1), (21, -9), (6, 2), (20, -7), (30, -10), (14, -3),
    (20, -8), (13, -2), (7, 3), (28, -8), (29, -9), (15, -3), (22, -5), (26, -8), (25, -8),
    (25, -6), (15, -4), (9, -2), (15, -2), (12, -2), (28, -9), (12, -3), (24, -6), (23, -7),
    (25, -10), (7, 8), (11, -3), (26, -7), (7, 1), (23, -9), (6, 0), (22, -10), (27, -6),
    (8, 1), (22, -8), (13, -4), (7, 6), (28, -6), (11, -4), (12, -4), (26, -9), (7, 4),
    (24, -10), (23, -8), (30, -8), (7, 0), (9, -1), (10, -1), (26, -5), (22, -9), (6, 5),
    (7, 5), (23, -6), (28, -10), (10, -2), (11, -1), (20, -9), (14, -2), (29, -7), (13, -3),
    (23, -5), (24, -8), (27, -9), (30, -7), (28, -5), (21, -10), (7, 9), (6, 6), (21, -5),
    (27, -10), (7, 2), (30, -9), (21, -8), (22, -7), (24, -9), (20, -6), (6, 9), (29, -5),
    (8, -2), (27, -8), (30, -5), (24, -7),
]


@dataclass
class Position:
    x: int
    y: int
    x_speed: int
    y_speed: int

    def step(self) -> "Position":
        return Position(
            x=self.x + self.x_speed,
            y=self.y + self.y_speed,
            x_speed=self.x_speed - 1 if self.x_speed > 0 else 0,
            y_speed=self.y_speed - 1
        )

    def target_reached(self):
        return target[0] <= self.x <= target[1] and target[2] <= self.y <= target[3]

    def overshoot(self):
        return self.x > target[1] or self.y < target[2]


def main():
    results = []
    start_results = []
    for x_speed in range(0, max(target[0], target[1])+1):
        for y_speed in range(min(target[2], target[3])-1, 500):
            start = Position(0, 0, x_speed, y_speed)
            path = [start]
            height = 0
            step = start
            while True:
                step = step.step()
                # print(step)
                height = max(step.y, height)
                path.append(step)
                if step.target_reached():
                    print(height, x_speed, y_speed)
                    results.append(height)
                    start_results.append((x_speed, y_speed))
                    break
                if step.overshoot():
                    break
            # print(len(path))
    print(results)
    print(max(results))
    print(len(results))
    # print(start_results)
    # print(set(exmaple_result).difference(start_results))


if __name__ == "__main__":
    main()


## step 2
# 306 to low
# 1504 to low