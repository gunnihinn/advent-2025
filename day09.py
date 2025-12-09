#!/usr/bin/env python3

import argparse
import datetime
import functools
import itertools
import multiprocessing

_data = None
n = 0


def parse(fh):
    data = tuple([tuple(map(int, line.split(","))) for line in fh.readlines()])

    return data


def area(p, q):
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)


def part1(data):
    return max(area(p, q) for p, q in itertools.combinations(data, 2))


def edges(data):
    return zip(data, itertools.islice(itertools.cycle(data), 1, None))


@functools.cache
def is_inside(xy):
    # Cast a ray to the right and count how many times it intersects the edges
    x, y = xy
    index = 0
    for p, q in edges(_data):
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


def calc(ipq):
    global n
    i, (p, q) = ipq
    px, py = p
    qx, qy = q

    mx, Mx = min(px, qx), max(px, qx)
    my, My = min(py, qy), max(py, qy)

    for x in range(mx, Mx):
        if not is_inside((x, my)):
            print(f"{datetime.datetime.now()}: {i}/{n}, {p}, {q} not within area")
            return 0
        if not is_inside((x, My)):
            print(f"{datetime.datetime.now()}: {i}/{n}, {p}, {q} not within area")
            return 0

    for y in range(my, My):
        if not is_inside((mx, y)):
            print(f"{datetime.datetime.now()}: {i}/{n}, {p}, {q} not within area")
            return 0
        if not is_inside((Mx, y)):
            print(f"{datetime.datetime.now()}: {i}/{n}, {p}, {q} not within area")
            return 0

    if not is_inside((Mx, My)):
        print(f"{datetime.datetime.now()}: {i}/{n}, {p}, {q} not within area")
        return 0

    print(f"{datetime.datetime.now()}: {i}/{n}, {p}, {q} inside area")
    return area(p, q)


def part2(data):
    global n
    global _data
    n = len(data) * (len(data) - 1) // 2
    _data = data

    with multiprocessing.Pool(10) as pool:
        return max(pool.map(calc, enumerate(itertools.combinations(data, 2))))


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
