import argparse
import collections
import functools
import re


def parse1(fh):
    lines = fh.readlines()

    data = collections.defaultdict(list)
    for line in lines[:-1]:
        for col, n in enumerate(map(int, re.split(r" +", line.strip()))):
            data[col].append(n)

    for col, op in enumerate(re.split(r" +", lines[-1].strip())):
        data[col].append(op)

    return data


def parse2(fh):
    lines = [line[:-1] for line in fh.readlines()]

    # Use operator positions to figure out column ranges
    positions = [i for i, ch in enumerate(lines[-1]) if ch != " "]
    positions.append(len(lines[-1]) + 1)

    predata = collections.defaultdict(list)
    for line in lines[:-1]:
        for col, (a, b) in enumerate(zip(positions, positions[1:])):
            predata[col].append(line[a : b - 1])

    for col, op in enumerate(re.split(r" +", lines[-1].strip())):
        predata[col].append(op)

    data = collections.defaultdict(list)
    for key, column in predata.items():
        for i in range(len(column[0])):
            val = ""
            for j in range(len(column) - 1):
                val += column[j][i]
            data[key].append(int(val))

        data[key].append(column[-1])

    return data


def op(column):
    if column[-1] == "+":
        return sum(column[:-1])
    else:
        return functools.reduce(lambda x, y: x * y, column[:-1], 1)


def part1(data):
    return sum(map(op, data.values()))


def part2(data):
    return sum(map(op, data.values()))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    with open(args.filename) as fh:
        data1 = parse1(fh)
    p1 = part1(data1)

    with open(args.filename) as fh:
        data2 = parse2(fh)
    p2 = part2(data2)

    print(f"part1: {p1}")
    print(f"part2: {p2}")
