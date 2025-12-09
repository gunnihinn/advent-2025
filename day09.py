#!/usr/bin/env python3

import argparse
import functools
import itertools
import multiprocessing
import os

_edges = None


def parse(fh):
    data = tuple([tuple(map(int, line.split(","))) for line in fh.readlines()])

    return data


def area(p, q):
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)


def part1(data):
    return max(area(p, q) for p, q in itertools.combinations(data, 2))


@functools.cache
def is_inside(xy):
    # Cast a ray to the right and count how many times it intersects the edges
    x, y = xy
    index = 0
    for p, q in _edges:
        px, py = p
        qx, qy = q

        mx, Mx = min(px, qx), max(px, qx)
        my, My = min(py, qy), max(py, qy)

        if mx <= x <= Mx and my <= y <= My:
            return True
        elif px == qx:
            index += x <= px and my <= y < My
        else:
            index += y == py and mx <= x <= Mx

    return index % 2


def calc(pq):
    p, q = pq
    px, py = p
    qx, qy = q

    mx, Mx = min(px, qx), max(px, qx)
    my, My = min(py, qy), max(py, qy)

    if not is_inside((mx, my)):
        return 0
    elif not is_inside((mx, My)):
        return 0
    elif not is_inside((Mx, my)):
        return 0
    elif not is_inside((Mx, My)):
        return 0

    for x in range(mx + 1, Mx, 2):
        if not is_inside((x, my)):
            return 0
        if not is_inside((x, My)):
            return 0

    for y in range(my + 1, My, 2):
        if not is_inside((mx, y)):
            return 0
        if not is_inside((Mx, y)):
            return 0

    return area(p, q)


def part2(data):
    global _edges
    _edges = tuple(zip(data, list(data[1:]) + [data[0]]))

    with multiprocessing.Pool(os.cpu_count()) as pool:
        return max(pool.map(calc, itertools.combinations(data, 2)))


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
