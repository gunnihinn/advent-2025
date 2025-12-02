import argparse
import collections
import functools
import itertools

Instruction = collections.namedtuple("Instruction", "dir clicks")


def parse(fh):
    data = []
    for line in fh:
        lr, clicks = line[0], int(line[1:])
        data.append(Instruction(lr, clicks))

    return data


def part1(start, data):
    def step(val, instruction):
        if instruction.dir == "L":
            return (val - instruction.clicks) % 100
        else:
            return (val + instruction.clicks) % 100

    return sum(not n for n in itertools.accumulate(data, func=step, initial=50))


def part2(start, data):
    def step(state, instruction):
        val, nr = state
        d, r = instruction.clicks // 100, instruction.clicks % 100
        val += d

        if instruction.dir == "L":
            if nr - r < 0 and nr != 0:
                val += 1
            nr = (nr - r) % 100
        else:
            if nr + r > 100 and nr != 0:
                val += 1
            nr = (nr + r) % 100
        val += nr == 0

        return (val, nr)

    return functools.reduce(step, data, (0, 50))[0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    with open(args.filename) as fh:
        data = parse(fh)

    p1 = part1(50, data)
    p2 = part2(50, data)

    print(f"part1: {p1}")
    print(f"part2: {p2}")
