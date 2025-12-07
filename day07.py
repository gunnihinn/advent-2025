import argparse
import functools
from typing import List, Tuple


def parse(fh):
    return [line.strip() for line in fh if "S" in line or "^" in line]


def part1(data: List[str]) -> int:
    def step(acc: Tuple[List[bool], int], row: str) -> Tuple[List[bool], int]:
        beams, splits = acc

        nxt = [False] * len(row)
        for i, beam in enumerate(beams):
            if beam and row[i] == "^":
                nxt[i - 1] |= beam
                nxt[i + 1] |= beam
                splits += 1
            else:
                nxt[i] |= beam

        return nxt, splits

    beams = [c == "S" for c in data[0]]

    return functools.reduce(step, data[1:], (beams, 0))[1]


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

    beams = [c == "S" for c in data[0]]

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
