#!/usr/bin/env python3

from collections import defaultdict

def load_input():
    data = []

    with open('input') as fd:
        for i, line in enumerate(fd):
            temp = line.strip().split(':')
            expected = int(temp[0])
            values = [int(i) for i in temp[1].strip().split(' ')]
            data.append((expected, values))
    return data


def next_operation(value, remaining, expected):
    result = False
    if value > expected:
        pass
    elif not remaining:
        if value == expected:
            result = True
    else:
        nex_value_add = value + remaining[0]
        result |= next_operation(nex_value_add, remaining[1:], expected)
        nex_value_mult = value * remaining[0]
        result |= next_operation(nex_value_mult, remaining[1:], expected)
    return result

def next_operation_part2(value, remaining, expected):
    result = False
    if value > expected:
        pass
    elif not remaining:
        if value == expected:
            result = True
    else:
        nex_value_add = value + remaining[0]
        result |= next_operation_part2(nex_value_add, remaining[1:], expected)
        nex_value_mult = value * remaining[0]
        result |= next_operation_part2(nex_value_mult, remaining[1:], expected)
        nex_value_cat = int(str(value) + str(remaining[0]))
        result |= next_operation_part2(nex_value_cat, remaining[1:], expected)

    return result

    
def part1(data):
    result = 0
    for row in data:
        expected = row[0]
        if next_operation(row[1][0], row[1][1:], expected):
            result += expected
    print("Result 1: ", result)



def part2(data):
    result = 0
    for row in data:
        expected = row[0]
        if next_operation_part2(row[1][0], row[1][1:], expected):
            result += expected

    print("Result 2: ", result)


def main():
    data = load_input()
    part1(data)
    # 3598800864292
    part2(data)
    # 340362531521793
    # 340362529351427


if __name__ == '__main__':
    main()
