import argparse
import copy
import itertools


def parse(fh):
    data = set((col, row) for row, line in enumerate(fh) for col, char in enumerate(line.strip()) if char == "@")

    return data


def neighbors(pt):
    x, y = pt
    return ((x + dx, y + dy) for dx, dy in itertools.product((-1, 0, 1), repeat=2))


def accessible(pt, data):
    return sum(xy in data for xy in neighbors(pt)) <= 4


def part1(data):
    return sum(accessible(pt, data) for pt in data)


def part2(data):
    start = len(data)
    new = set(pt for pt in data if not accessible(pt, data))

    while new != data:
        data = new
        new = set(pt for pt in data if not accessible(pt, data))

    return start - len(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    with open(args.filename) as fh:
        data = parse(fh.readlines())

    p1 = part1(data)
    p2 = part2(data)

    print(f"part1: {p1}")
    print(f"part2: {p2}")
