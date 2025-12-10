import argparse
import functools
import itertools


def parse(fh):
    data = []
    for line in fh:
        parts = line.strip().split(" ")

        indicators = tuple(c == "#" for c in parts[0][1:-1])
        wirings = tuple(tuple(map(int, part[1:-1].split(","))) for part in parts[1:-1])
        joltage = tuple(map(int, parts[-1][1:-1].split(",")))

        data.append((indicators, wirings, joltage))

    return data


def presses(indicators, wirings):
    return next(
        n
        for n in range(1, len(wirings) + 1)
        for combo in itertools.combinations(wirings, n)
        if indicators == press(len(indicators), combo)
    )


def press(k, combo):
    def p(lights, button):
        return tuple(v ^ (i in button) for i, v in enumerate(lights))

    return functools.reduce(p, combo, tuple(False for _ in range(k)))


def part1(data):
    return sum(presses(indicators, wirings) for indicators, wirings, _ in data)


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
