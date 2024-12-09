#!/usr/bin/env python3

from collections import defaultdict

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

def load_input():
    data = []
    vpos = None
    vdir = None
    with open('input') as fd:
        for i, line in enumerate(fd):
            for j, value in enumerate(line.strip()):
                if value == '#':
                    data.append((i, j))
                if value == '^':
                    vpos = (i, j)
                    vdir = 3
    return (vpos, vdir), data

def get_next_pos(pos, direct):
    return tuple([a+b for a, b in zip(pos, direct)])

def part1(start, data):
    positions = set()
    vpos = start[0]
    vdir = start[1]
    y_max = max([value[0] for value in data])
    x_max = max([value[1] for value in data])
    while True:
        positions.add(vpos)
        next_pos = get_next_pos(vpos, directions[vdir])
        if next_pos in data:
            vdir = (vdir+1) % 4
        else:
            vpos = next_pos
        
        if not(0 <= vpos[0] <= y_max and 0 <= vpos[1] <= x_max):
            break

    result = len(positions)
    print("Result 1: ", result)
    return positions


def detect_loop(vpos, vdir, data):
    y_max = max([value[0] for value in data])
    x_max = max([value[1] for value in data])
    trace = set()
    loop = False
    while True:
        if not(0 <= vpos[0] <= y_max and 0 <= vpos[1] <= x_max):
            break
        
        if (vpos, vdir) in trace:
            loop = True
            break
        trace.add((vpos, vdir))
        next_pos = get_next_pos(vpos, directions[vdir])
        if next_pos in data:
            vdir = (vdir+1) % 4
        else:
            vpos = next_pos
        
    return loop


def part2(start, data, positions):
    vpos = start[0]
    vdir = start[1]

    data = set(data)
    loop_count = 0

    for y, x in positions:
        temp_data = data.copy()
        temp_data.add((y,x))
        if detect_loop(vpos, vdir, temp_data):
            loop_count += 1
    result = loop_count
    print("Result 2: ", result)


def main():
    start, data = load_input()
    positions = part1(start, data)
    part2(start, data, positions)


if __name__ == '__main__':
    main()
