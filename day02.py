import argparse
import math


def parse(fh):
    blob = fh.read().strip()
    data = [tuple(map(int, part.split("-"))) for part in blob.split(",")]

    return data


def is_repeated(n: int, parts: int) -> bool:
    num = str(n)
    if len(num) % parts:
        return False

    return num == num[: len(num) // parts] * parts


def part1(data):
    return sum(n for a, b in data for n in range(a, b + 1) if is_repeated(n, 2))


def part2(data):
    return sum(
        n
        for a, b in data
        for n in range(a, b + 1)
        if any(is_repeated(n, i) for i in range(2, int(math.floor(math.log10(n))) + 1 + 1))
    )


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
