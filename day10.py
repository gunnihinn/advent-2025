import argparse
import functools
import itertools

import cvxpy as cp
import numpy as np

# Run in a Docker image built with:
#
# FROM python3:bookworm
#
# RUN pip install numpy cvxpy pyscipopt
#
# Then:
#
# $ docker run --rm -it -v $(pwd):/app $image python /app/day10.py /app/input/day10.txt


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
    s = 0
    for i, (_, wirings, joltage) in enumerate(data, start=1):
        A = np.array([tuple(i in wire for i in range(len(joltage))) for wire in wirings]).T
        b = np.array(joltage)
        q = np.ones(A.shape[1])
        G = np.eye(A.shape[1])
        x = cp.Variable(A.shape[1], integer=True)
        prob = cp.Problem(cp.Minimize(q @ x), [G @ x >= 0, A @ x == b])
        prob.solve()

        s += sum(v for v in x.value)

    return s


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    with open(args.filename) as fh:
        data = parse(fh)

    p1 = part1(data)
    print(f"part1: {p1}")

    p2 = part2(data)
    print(f"part2: {p2}")
