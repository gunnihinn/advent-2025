import argparse
import functools

_data = None


def parse(fh):
    data = {}
    for line in fh:
        i = line.find(":")
        key = line[:i]
        vals = line[i + 1 :].strip().split(" ")
        data[key] = tuple(vals)

    return data


@functools.cache
def paths(start, end):
    if start == end:
        return 1

    return sum(paths(p, end) for p in _data.get(start, []))


def part1(data):
    return paths("you", "out")


def part2(data):
    svc_dac_fft_out = paths("svr", "dac") * paths("dac", "fft") * paths("fft", "out")
    svc_fft_dac_out = paths("svr", "fft") * paths("fft", "dac") * paths("dac", "out")
    return svc_dac_fft_out + svc_fft_dac_out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    with open(args.filename) as fh:
        data = parse(fh)

    global _data
    _data = data

    p1 = part1(data)
    p2 = part2(data)

    print(f"part1: {p1}")
    print(f"part2: {p2}")
