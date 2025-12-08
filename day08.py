import argparse
import collections
import functools
import heapq
import itertools


def parse(fh):
    points = sorted([tuple(map(int, line.split(","))) for line in fh.readlines()])

    def d(pt1, pt2):
        return sum((x1 - x2) ** 2 for x1, x2 in zip(pt1, pt2))

    dist = {(p, q): d(p, q) for p, q in itertools.combinations(points, 2)}

    return points, dist


def join(colors, p, q):
    cp = colors[p]
    cq = colors[q]
    color = min(cp, cq)
    new = {}
    for k, v in colors.items():
        if v == cp:
            new[k] = color
        elif v == cq:
            new[k] = color
        else:
            new[k] = v

    return new


def part1(data, test: bool):
    iters = 10 if test else 1000
    topk = 3

    points, dist = data
    colors = {pt: i for i, pt in enumerate(points)}

    heap = []
    for pq, d in dist.items():
        heapq.heappush(heap, (d, pq))

    for _, (p, q) in heapq.nsmallest(iters, heap):
        colors = join(colors, p, q)

    circuits = collections.Counter(colors.values())

    return functools.reduce(lambda x, y: x * y[1], circuits.most_common(topk), 1)


def part2(data):
    points, dist = data
    colors = {pt: i for i, pt in enumerate(points)}

    heap = []
    for pq, d in dist.items():
        heapq.heappush(heap, (d, pq))

    while heap:
        _, (p, q) = heapq.heappop(heap)
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
