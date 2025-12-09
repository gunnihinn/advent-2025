import argparse
import itertools


def parse(fh):
    data = [tuple(map(int, line.split(","))) for line in fh.readlines()]

    return data


def area(p, q):
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)


def part1(data):
    return max(area(p, q) for p, q in itertools.combinations(data, 2))


def part2(data):
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    with open(args.filename) as fh:
        data = parse(fh)

    p1 = part1(data)
    p2 = part2(data)

    print(f"part1: {p1}")
    print(f"part2: {p2}")
