import argparse
import math


class Mirror:
    def __init__(self, n, d=None):
        self.n = n
        if d == 0:
            self.d = 0
        else:
            self.d = int(math.floor(math.log10(n))) + 1

    def whole(self):
        if self.d == 0:
            return self.n
        return (self.n * 10**self.d) + self.n

    def __str__(self):
        return f"{self.whole()}"


def parse(fh):
    blob = fh.read().strip()
    data = [tuple(map(int, part.split("-"))) for part in blob.split(",")]

    return data


def odd_floor(x) -> int:
    n = int(math.floor(x))
    if n % 2 == 1:
        return n
    return n - 1


def lower_mirror(n: int) -> Mirror:
    if n < 10:
        return Mirror(1, 1)

    p = int(math.floor(math.log10(n)))
    if p % 2 == 0:
        return lower_mirror((10**p) - 1)

    d = (odd_floor(math.log10(n)) + 1) // 2
    a = n // 10**d

    while True:
        if (a * 10**d) + a <= n:
            return Mirror(a, d)
        a -= 1


def part1(data):
    total = 0

    for a, b in data:
        lma = lower_mirror(a)
        lmb = lower_mirror(b)
        if lma.whole() < a:
            lma = Mirror(lma.n + 1)

        for n in range(lma.n, lmb.n + 1):
            total += Mirror(n).whole()

    return total


def part2(data):
    total = 0
    for a, b in data:
        found = set()
        for n in range(a, b + 1):
            num = str(n)
            for i in range(1, len(num) // 2 + 1):
                cand = num[:i] * (len(num) // i)
                if num == cand and cand not in found:
                    total += n
                    found.add(cand)

    return total


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    with open(args.filename) as fh:
        data = parse(fh)

    for a, b in data:
        lma = lower_mirror(a)
        lmb = lower_mirror(b)

    p1 = part1(data)
    p2 = part2(data)

    print(f"part1: {p1}")
    print(f"part2: {p2}")
