#!/usr/bin/env python3

import re
from collections import deque

pattern = r"XMAS"


def load_input():
    data = list()
    with open('input') as fd:
        for i, line in enumerate(fd):
            temp = "B" + line.strip() + "B"
            if i == 0:
                data.append("".join("B" for _ in range(len(line.strip())+2)))
            data.append(temp)
        data.append("".join("B" for _ in range(len(line.strip())+2)))
    return data


def check_xmas_part1(data, x, y):
    directions = [-1, 0, 1]
    xmas_len = len(pattern)
    result = 0
    for i in directions:
        for j in directions:
            if not(i == 0 and j == 0):
                temp = ""
                for k in range(xmas_len):
                    x_i = x + k*i
                    y_j = y + k*j
                    if 0 <= x_i < len(data[0]) and 0 <= y_j < len(data):
                        temp += data[y_j][x_i]
                if temp == pattern:
                    result += 1
    return result


def check_xmas_part2(data, x, y):
    result = 0
    if data[y][x] == 'A':
        matches = 0
        for i in [-1, 1]:
            for j in [-1, 1]:
                if data[y+j][x+i] == 'M':
                    if data[y-j][x-i] == 'S':
                        matches += 1
        if matches == 2:
            result += 1
    return result            
                    

def part1(data):
    result = 0
    y_max = len(data)
    x_max = len(data[0])
    for x in range(x_max):
        for y in range(y_max):
            result += check_xmas_part1(data, x, y)
    print("Result 1: ", result)


def part2(data):
    result = 0

    y_max = len(data)
    x_max = len(data[0])
    for x in range(x_max):
        for y in range(y_max):
            result += check_xmas_part2(data, x, y)

    print("Result 2: ", result)


def main():
    data = load_input()
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
