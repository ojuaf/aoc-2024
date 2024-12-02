#!/usr/bin/env python3


import numpy as np


def load_input():
    data = list()
    with open('input') as fd:
        for line in fd:
            data.append([int(i) for i in line.strip().split()])
    return data


def check_safe(line):
    max_level = 3
    min_level = 1
    sign = np.sign(line[-1] - line[0])
    for i in range(0, len(line)-1):
        diff = line[i+1] - line[i]
        if min_level <= abs(diff) <= max_level and np.sign(diff) == sign:
            pass
        else:
            return False, i
    return True, None


def part1(data):
    safe_cnt = 0
    for line in data:
        safe, _ = check_safe(line)
        if safe:
            safe_cnt += 1

    result = safe_cnt

    print("Result 1: ", result)


def part2(data):
    safe_cnt = 0
    for line in data:
        safe, i = check_safe(line)
        if safe:
            safe_cnt += 1
        else:
            adjusted_line = line.copy()
            del adjusted_line[i]
            if check_safe(adjusted_line)[0]:
                safe_cnt += 1
                continue
            adjusted_line = line.copy()
            del adjusted_line[i+1]
            if check_safe(adjusted_line)[0]:
                safe_cnt += 1

    result = safe_cnt

    print("Result 2: ", result)


def main():
    data = load_input()
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
