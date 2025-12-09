#!/usr/bin/env python3

import argparse
import functools
import itertools

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


def fits(p, q):
    px, py = p
    qx, qy = q

    mx, Mx = min(px, qx), max(px, qx)
    my, My = min(py, qy), max(py, qy)

    if not is_inside((mx, my)):
        return False
    elif not is_inside((mx, My)):
        return False
    elif not is_inside((Mx, my)):
        return False
    elif not is_inside((Mx, My)):
        return False

    for y in range(my + 1, My, 2):
        if not is_inside((mx, y)):
            return False
        if not is_inside((Mx, y)):
            return False

    for x in range(mx + 1, Mx, 2):
        if not is_inside((x, my)):
            return False
        if not is_inside((x, My)):
            return False

    return True


def part2(data):
    global _edges
    _edges = tuple(zip(data, list(data[1:]) + [data[0]]))

    candidates = sorted(itertools.combinations(data, 2), key=lambda pq: area(pq[0], pq[1]), reverse=True)
    for p, q in candidates:
        if fits(p, q):
            return area(p, q)


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
