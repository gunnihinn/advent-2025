import argparse


def parse(fh):
    data = [tuple(map(int, line.strip())) for line in fh.readlines()]

    return data


def largest(row, d: int) -> int:
    if not d:
        return max(row)

    i, n = max(enumerate(row[:-d]), key=lambda pair: pair[1])
    return (10**d) * n + largest(row[i + 1 :], d - 1)


def part1(data):
    return sum(largest(row, 1) for row in data)


def part2(data):
    return sum(largest(row, 11) for row in data)


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
