import argparse


def parse(fh):
    lines = (line.strip() for line in fh.readlines())

    ranges = []
    for line in lines:
        if not line:
            break
        ranges.append(tuple(map(int, line.split("-"))))

    ids = tuple(int(line) for line in lines)

    return join(sorted(ranges)), sorted(ids)


def join(ranges):
    new = []

    while ranges:
        a, b = ranges.pop(0)
        while ranges:
            c, d = ranges[0]
            if c <= b + 1:
                b = max(b, d)
                ranges.pop(0)
            else:
                new.append((a, b))
                break
        else:
            new.append((a, b))

    return tuple(new)


def part1(data):
    ranges, ids = data

    return sum(any(a <= _id <= b for a, b in ranges) for _id in ids)


def part2(data):
    ranges, _ = data

    return sum(b + 1 - a for a, b in ranges)


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
