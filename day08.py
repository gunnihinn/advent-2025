import argparse
import collections
import functools
import itertools


def parse(fh):
    points = sorted([tuple(map(int, line.split(","))) for line in fh.readlines()])

    def d(pt1, pt2):
        return sum((x1 - x2) ** 2 for x1, x2 in zip(pt1, pt2))

    dist = {(p, q): d(p, q) for p, q in itertools.combinations(points, 2)}
    heap = sorted([pq for pq in dist], key=lambda pq: dist[pq])

    return points, heap


def join(colors, p, q):
    cp = colors[p]
    cq = colors[q]

    return {k: min(cp, cq) if v == cp or v == cq else v for k, v in colors.items()}


def part1(data, test: bool):
    iters = 10 if test else 1000
    topk = 3

    points, heap = data
    colors = {pt: i for i, pt in enumerate(points)}

    for p, q in heap[:iters]:
        colors = join(colors, p, q)

    circuits = collections.Counter(colors.values())

    return functools.reduce(lambda x, y: x * y[1], circuits.most_common(topk), 1)


def part2(data):
    points, heap = data
    colors = {pt: i for i, pt in enumerate(points)}

    for p, q in heap:
        colors = join(colors, p, q)
        if len(set(colors.values())) == 1:
            return p[0] * q[0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    with open(args.filename) as fh:
        data = parse(fh)

    p1 = part1(data, "test" in args.filename)
    p2 = part2(data)

    print(f"part1: {p1}")
    print(f"part2: {p2}")
