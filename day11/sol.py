#!/usr/bin/env python3

from collections import defaultdict


def load_input():
    data = {}
    with open('input') as fd:
        rd = fd.read().strip().split(' ')
        for value in rd:
            data[int(value)] = 1
    return data


def process(data, rounds):
    for _ in range(rounds):
        next_data = defaultdict(lambda: 0)
        for key, value in data.items():
            sk = str(key)
            sk_len = len(sk)
            if key == 0:
                next_data[1] += value
            elif sk_len % 2 == 0:
                k0 = int(sk[:sk_len // 2])
                next_data[k0] += value
                k1 = int(sk[sk_len // 2:])
                next_data[k1] += value
            else:
                k = 2024 * key
                next_data[k] += value
        data = next_data
    result = sum(data.values())
    return result


def part1(data):
    result = process(data, 25)
    print("Result 1: ", result)


def part2(data):
    result = process(data, 75)
    print("Result 2: ", result)


def main():
    data = load_input()
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
