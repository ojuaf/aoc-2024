#!/usr/bin/env python3

from collections import defaultdict
import itertools as it

def load_input():
    data = defaultdict(list)
    y = 0
    line = None
    with open('input') as fd:
        for y, line in enumerate(fd):
            for x, value in enumerate(line.strip()):
                if value != '.':
                    data[value].append((y, x))
        y_size = y+1
        x_size = len(line.strip())

    limits = (y_size, x_size)

    return data, limits


def get_distance(a, b):
    return tuple([i-j for i, j in zip(a, b)])


def part1(data, limits):
    antinodes = set()
    for positions in data.values():
        pairs = it.combinations(positions, 2)
        for pair in pairs:
            d = get_distance(*pair)
            antinode = tuple([i+j for i, j in zip(pair[0], d)])
            antinodes.add(antinode)
            antinode = tuple([i-j for i, j in zip(pair[1], d)])
            antinodes.add(antinode)

    valid_antinodes = []
    for antinode in antinodes:
        if 0 <= antinode[0] < limits[0] and 0 <= antinode[1] < limits[1]:
            valid_antinodes.append(antinode)

    result = len(valid_antinodes)
    print("Result 1: ", result)


def part2(data, limits):
    antinodes = set()
    for positions in data.values():
        pairs = it.combinations(positions, 2)
        for pair in pairs:
            d = get_distance(*pair)
            counter = 0
            while True:
                antinode = tuple([i+counter*j for i, j in zip(pair[0], d)])
                if not(0 <= antinode[0] < limits[0] and 0 <= antinode[1] < limits[1]):
                    break
                antinodes.add(antinode)
                counter += 1

            counter = 0
            while True:
                antinode = tuple([i-counter*j for i, j in zip(pair[1], d)])
                if not(0 <= antinode[0] < limits[0] and 0 <= antinode[1] < limits[1]):
                    break
                antinodes.add(antinode)
                counter += 1

    result = len(antinodes)
    print("Result 2: ", result)


def main():
    data, limits = load_input()
    part1(data, limits)
    part2(data, limits)


if __name__ == '__main__':
    main()
