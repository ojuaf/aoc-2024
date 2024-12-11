#!/usr/bin/env python3


def load_input():
    data = {}
    y = 0
    line = None
    with open('input') as fd:
        for y, line in enumerate(fd):
            for x, value in enumerate(line.strip()):
                key = (y, x)
                data[key] = {'h': int(value), 'n': None}
    y_max = y+1
    x_max = len(line.strip())

    n_delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for y in range(y_max):
        for x in range(x_max):
            key = (y, x)
            data[key]['n'] = [(y+i, x+j) for i, j in n_delta if 0<=y+i<y_max and 0<=x+j<x_max]
    return data, (y_max, x_max)


def search_peak(pos, data):
    result = []
    if data[pos]['h'] == 9:
        result.append(pos)
        return result
    for neighbor in data[pos]['n']:
        if data[neighbor]['h']-data[pos]['h'] == 1:
            result.extend(search_peak(neighbor, data))
    return result


def part1(data, limits):
    result = 0
    for y in range(limits[0]):
        for x in range(limits[1]):
            key = (y, x)
            if data[key]['h'] == 0:
                ends = search_peak(key, data)
                result += len(set(ends))
    print("Result 1: ", result)


def part2(data, limits):
    result = 0
    for y in range(limits[0]):
        for x in range(limits[1]):
            key = (y, x)
            if data[key]['h'] == 0:
                ends = search_peak(key, data)
                result += len(ends)
    print("Result 2: ", result)


def main():
    data, limits = load_input()
    part1(data, limits)
    part2(data, limits)


if __name__ == '__main__':
    main()
