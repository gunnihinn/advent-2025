import argparse
import functools
import itertools


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


def step(point, joltage, wiring_increments, steps, best):
    if point == joltage:
        return steps

    if steps >= best:
        return best

    neighbors = []
    for inc in wiring_increments:
        pt = tuple(p + i for p, i in zip(point, inc))
        if leq(pt, joltage):
            neighbors.append(pt)
    if not neighbors:
        return best

    neighbors.sort(key=lambda pt: sum(abs(p - j) for p, j in zip(pt, joltage)))

    got = best
    for pt in neighbors:
        got = min(got, step(pt, joltage, wiring_increments, steps + 1, best))
        if got < best:
            best = got
            print(f".... joltage={joltage}, best={best}")

    return got


def joltage_presses(joltage, wirings):
    start = tuple([0] * len(joltage))
    wirings = sorted(wirings, key=lambda w: len(w), reverse=True)
    wiring_increments = [tuple(i in wire for i in range(len(joltage))) for wire in wirings]

    return step(start, joltage, wiring_increments, 0, 1_000_000_000_000_000)


def leq(xs, ys):
    return all(x <= y for x, y in zip(xs, ys))


def part2(data):
    s = 0
    for i, (_, wirings, joltage) in enumerate(data, start=1):
        print(f".. wiring {i}/{len(data)}")
        s += joltage_presses(joltage, wirings)

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
