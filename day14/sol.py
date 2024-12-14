#!/usr/bin/env python3


import re
from collections import defaultdict
import math

# TAILS_X = 11
# TAILS_Y = 7

TAILS_X = 101
TAILS_Y = 103

def load_input():
    data = {}
    pattern = re.compile(r'p=(.+),(.+) v=(.+),(.+)')
    with open('input') as fd:
        for line in fd:
            match = pattern.search(line.strip())
            p = (int(match.group(1)), int(match.group(2)))
            v = (int(match.group(3)), int(match.group(4)))
            data[(p, v)] = 1
    return data


def process(data):
    next_robots = defaultdict(lambda: 0)
    for p, v in data:
        x, y = p
        vx, vy = v
        next_y = (y + vy) % TAILS_Y
        next_x = (x + vx) % TAILS_X
        next_robots[((next_x, next_y), v)] += 1
    result = next_robots
    return result

def count_neighbors(robots):
    positions = set([p for p, _ in robots.keys()])
    counter = 0
    for x, y in positions:
        for nx, ny in [(0,1), (0, -1), (-1, 0), (1, 0)]:
            if (x+nx, y+ny) in positions:
                counter += 1
    return counter

def print_robots(robots):
    positions = set([p for p, _ in robots.keys()])

    for y in range(TAILS_Y):
        line = ""
        for x in range(TAILS_X):
            if (x, y) in positions:
                line += 'X'
            else:
                line += '.'
        print(line)
    print(" ")


def part1(data):
    seconds = 100

    for _ in range(seconds):
        data = process(data)

    q = [0]*4
    for p, v in data:
        x, y = p
        if x < TAILS_X//2 and y < TAILS_Y//2:
            q[0] += 1
        elif TAILS_X//2 < x and y < TAILS_Y//2:
            q[1] += 1
        elif x < TAILS_X//2 and TAILS_Y//2 < y:
            q[2] += 1
        elif TAILS_X//2 < x and TAILS_Y//2 < y:
            q[3] += 1
        else:
            pass

    result = math.prod(q)
    print("Result 1: ", result)


def part2(data):
    seconds = 100000
    max_counter = 0
    tmp_robots = {}
    ts = 0
    for second in range(seconds):
        data = process(data)
        v = count_neighbors(data)
        if v > max_counter:
            max_counter = v
            tmp_robots = data.copy()
            ts = second
        elif v == max_counter:
            break
        else:
            pass
    print_robots(tmp_robots)
    print("Result 2: ", ts+1)


def main():
    data = load_input()
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
