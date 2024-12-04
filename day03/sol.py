#!/usr/bin/env python3

import re


pattern = r"mul\((\d+),(\d+)\)"


def load_input():
    data = None
    with open('input') as fd:
        data = fd.read().strip()
    return data


def part1(data):
    result = 0
    matches = re.findall(pattern, data)
    for match in matches:
        result += int(match[0]) * int(match[1])

    print("Result 1: ", result)


def part2(data):
    result = 0
    dos = list()
    do_split = data.split(r"do()")
    for x in do_split:
        dos.append(x.split(r"don't()")[0])

    matches = re.findall(pattern, "".join(dos))
    for match in matches:
        result += int(match[0]) * int(match[1])

    print("Result 2: ", result)


def main():
    data = load_input()
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
