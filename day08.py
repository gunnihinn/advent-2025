import argparse


def parse(fh):
    data = [tuple(map(int, line.split(","))) for line in fh.readlines()]

    return data


def part1(data):
    return 0


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
