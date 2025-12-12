import argparse


def parse(fh):
    data = eval(fh.read())

    return data


def fits(xy, counts, blocks):
    x, y = xy
    lower = sum(b * c for b, c in zip(blocks, counts))
    upper = 9 * sum(blocks)
    if x * y < lower:
        return False
    elif upper <= (x // 3) * 3 * (y // 3) * 3:
        return True


def part1(data):
    blocks = (7, 6, 7, 5, 7, 7)

    return sum(fits(xy, counts, blocks) for xy, counts in data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    with open(args.filename) as fh:
        data = parse(fh)

    p1 = part1(data)

    print(f"part1: {p1}")
