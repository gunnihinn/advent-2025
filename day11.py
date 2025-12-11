import argparse
import functools
import itertools


def parse(fh):
    data = {}
    for line in fh:
        i = line.find(":")
        key = line[:i]
        vals = line[i + 1 :].strip().split(" ")
        data[key] = tuple(vals)

    return data


def make_paths(data):
    @functools.cache
    def paths(start, end):
        if start == end:
            return 1
        return sum(paths(p, end) for p in data.get(start, []))

    return paths


def product(iterable):
    "Like sum() but for multiplication."
    return functools.reduce(lambda x, y: x * y, iterable)


def part1(paths):
    return paths("you", "out")


def part2(paths):
    tracks = [("svr", "dac", "fft", "out"), ("svr", "fft", "dac", "out")]

    return sum(product(itertools.starmap(paths, zip(t, t[1:]))) for t in tracks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    with open(args.filename) as fh:
        data = parse(fh)

    paths = make_paths(data)

    p1 = part1(paths)
    p2 = part2(paths)

    print(f"part1: {p1}")
    print(f"part2: {p2}")
