import argparse
import collections


def parse(fh):
    return [line.strip() for line in fh if "S" in line or "^" in line]


def part1(data):
    def step(row, beams):
        if not beams:
            i = row.find("S")
            assert i != -1
            return set([i]), 0

        nxt = set()
        splits = 0
        for i in beams:
            if row[i] == "^":
                nxt.add(i - 1)
                nxt.add(i + 1)
                splits += 1
            else:
                nxt.add(i)

        return nxt, splits

    splits = 0
    beams = None
    for row in data:
        beams, s = step(row, beams)
        splits += s

    return splits


def step(row, beams):
    if not beams:
        i = row.find("S")
        assert i != -1
        return {i: 1}

    nxt = collections.defaultdict(int)
    for i, val in beams.items():
        if row[i] == "^":
            nxt[i - 1] += val
            nxt[i + 1] += val
        else:
            nxt[i] = val

    return nxt


def part2(data):
    def step(row, beams):
        if not beams:
            i = row.find("S")
            assert i != -1
            return {i: 1}

        nxt = collections.defaultdict(int)
        for i, val in beams.items():
            if row[i] == "^":
                nxt[i - 1] += val
                nxt[i + 1] += val
            else:
                nxt[i] = val

        return nxt

    beams = {}
    for row in data:
        beams = step(row, beams)

    return sum(v for v in beams.values())


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
