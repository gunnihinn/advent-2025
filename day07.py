import argparse
import functools
from typing import List, Set


def parse(fh):
    return [line.strip() for line in fh if "S" in line or "^" in line]


def part1(data: List[str]) -> int:
    def step(row: str, beams: Set[int]) -> Set[int]:
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


def part2(data: List[str]) -> int:
    def step(beams: List[int], row: str) -> List[int]:
        nxt = [0] * len(row)
        for i, val in enumerate(beams):
            if row[i] == "^":
                nxt[i - 1] += val
                nxt[i + 1] += val
            else:
                nxt[i] += val

        return nxt

    beams = [1 if c == "S" else 0 for c in data[0]]

    return sum(functools.reduce(step, data[1:], beams))


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
