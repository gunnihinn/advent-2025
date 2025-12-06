import argparse
import collections
import functools
import re


def parse(fh):
    lines = fh.readlines()

    data = collections.defaultdict(list)
    for line in lines[:-1]:
        for col, n in enumerate(map(int, re.split(r" +", line.strip()))):
            data[col].append(n)

    for col, op in enumerate(re.split(r" +", lines[-1].strip())):
        data[col].append(op)

    return data


def op(column):
    if column[-1] == "+":
        return sum(column[:-1])
    else:
        return functools.reduce(lambda x, y: x * y, column[:-1], 1)


def part1(data):
    return sum(map(op, data.values()))


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
