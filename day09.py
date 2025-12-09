#!/usr/bin/env python3

import argparse
import datetime
import functools
import itertools
import multiprocessing

is_inside = None


def parse(fh):
    data = tuple([tuple(map(int, line.split(","))) for line in fh.readlines()])

    return data


def area(p, q):
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)


def part1(data):
    return max(area(p, q) for p, q in itertools.combinations(data, 2))


def edges(data):
    return zip(data, itertools.islice(itertools.cycle(data), 1, None))


def interior(p, q):
    px, py = p
    qx, qy = q

    return itertools.product(range(min(px, qx), max(px, qx) + 1), range(min(py, qy), max(py, qy) + 1))


def make_is_inside(data):
    @functools.cache
    def is_inside(xy):
        # Cast a ray to the right and count how many times it intersects the edges
        x, y = xy
        for p, q in edges(data):
            px, py = p
            qx, qy = q

            mx, Mx = min(px, qx), max(px, qx)
            my, My = min(py, qy), max(py, qy)

            if mx <= x <= Mx and my <= y <= My:
                return True

        return sum(index(xy, p, q) for p, q in edges(data)) % 2

    return is_inside


def index(xy, p, q):
    x, y = xy
    px, py = p
    qx, qy = q

    mx, Mx = min(px, qx), max(px, qx)
    my, My = min(py, qy), max(py, qy)

    if px == qx:
        return x <= px and my <= y < My
    else:
        return y == py and mx <= x <= Mx


def contained_in(p, q, is_inside):
    return all(is_inside(x) for x in interior(p, q))


def calc(pq):
    if all(is_inside(x) for x in interior(pq[0], pq[1])):
        print(f"{datetime.datetime.now()}: checked {pq}")
        return area(pq[0], pq[1])
    else:
        print(f"{datetime.datetime.now()}: checked {pq}")
        return 0


def part2(data):
    global is_inside
    is_inside = make_is_inside(data)

    with multiprocessing.Pool(10) as pool:
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
