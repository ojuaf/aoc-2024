#!/usr/bin/env python3


import re


def load_input():
    data = []
    pattern0 = re.compile(r'Button \w: X\+(\d+), Y\+(\d+)')
    pattern1 = re.compile(r'X=(\d+), Y=(\d+)')

    with open('input') as fd:
        temp = []
        for i, line in enumerate(fd):
            if i%4 == 0:
                match = pattern0.search(line.strip())
                temp.append((int(match.group(1)), int(match.group(2))))
            elif i%4 == 1:
                match = pattern0.search(line.strip())
                temp.append((int(match.group(1)), int(match.group(2))))
            elif i%4 == 2:
                match = pattern1.search(line.strip())
                temp.append((int(match.group(1)), int(match.group(2))))
            else:
                data.append(temp)
                temp = []
    data.append(temp)
    return data


def process(data, offset=0):
    a, b = data[:2]
    ax, ay = a
    bx, by = b
    px = data[2][0] + offset
    py = data[2][1] + offset

    j = (py*ax - px*ay)/(ax*by - ay*bx)
    i = (px - bx*j)/ax

    cost = 0
    if i.is_integer() and j.is_integer():
        cost = int(i*3 + j)
    return cost


def part1(data):
    result = 0
    for d in data:
        costs = process(d)
        if costs:
            result += costs

    print("Result 1: ", result)


def part2(data):
    result = 0
    for d in data:
        costs = process(d, 10000000000000)
        if costs:
            result += costs
    print("Result 2: ", result)


def main():
    data = load_input()
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
