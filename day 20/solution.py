def read_file(filename="input_example.txt"):
    total = {}
    enhanced = None
    y = x = 0
    with open(filename, "r") as fh:
        for line in fh.readlines():
            if not line.split():
                continue
            if not enhanced:
                enhanced = line.split()[0]
                continue
            for i in line.split()[0]:
                if i == "#":
                    total[(x, y)] = i
                x += 1
            y += 1
            x = 0
    return enhanced, total


def get_bound(image):
    rim = 0
    x_min = x_max = y_min = y_max = 0
    for pos in image:
        x_min = min(x_min, pos[0])
        x_max = max(x_max, pos[0])
        y_min = min(y_min, pos[1])
        y_max = max(y_max, pos[1])
    return x_min - rim, x_max + rim, y_min - rim, y_max + rim


def enhance_pix(x, y, image, data, default="."):
    binary = ""
    for yy in range(y - 1, y + 2):
        for xx in range(x - 1, x + 2):
            bit = image.get((xx, yy), default)
            binary += "1" if bit == "#" else "0"
    return data[int(binary, 2)]


def enhance_image(data, image, step):
    new_image = {}
    rim = 10
    x_min, x_max, y_min, y_max = get_bound(image)
    for y in range(y_min - rim, y_max + rim + 1):
        for x in range(x_min - rim, x_max + rim + 1):
            # fix for infinite image size and flipping between "." and "#"
            default = data[-1] if step % 2 else data[0]
            default = "." if (x_min < x < x_max and y_min < y < y_max) or data[0] == "." else default
            if (pix := enhance_pix(x, y, image, data, default)) and pix == "#":
                new_image[(x, y)] = pix
    return new_image


def print_raster(image):
    x_min, x_max, y_min, y_max = get_bound(image)
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            print(image.get((x, y), "."), end="")
        print("", end="\n")
    print()


def main():
    data, image = read_file()
    print(data, image)
    print(image)
    for step in range(50):
        print_raster(image)
        image = enhance_image(data, image, step + 1)
        if step == 1:
            answer_step1 = len(image)
    print_raster(image)

    print("answer step 1", answer_step1)
    print("answer step 2", len(image))


if __name__ == "__main__":
    main()
