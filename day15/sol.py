#!/usr/bin/env python3


import re
from collections import defaultdict
import math

MOVES = {'^': (-1, 0), '<': (0, -1), '>': (0, 1), 'v': (1, 0)}

def load_input_part1():
    boxes = set()
    walls = set()
    robot = None
    instructions = ""
    part = 0
    with open('input') as fd:
        for y, line in enumerate(fd):
            if not line.strip():
                part = 1
                continue
            if part == 0:
                for x, i in enumerate(line.strip()):
                    if i == '#':
                        walls.add((y, x))
                    elif i == 'O':
                        boxes.add((y, x))
                    elif i == '@':
                        robot = (y, x)
                    else:
                        pass
            else:
                instructions += line.strip()

    data = (robot, instructions, walls, boxes)
    return data


def load_input_part2():
    boxes = []
    walls = set()
    robot = None
    instructions = ""
    part = 0
    with open('input') as fd:
        for y, line in enumerate(fd):
            if not line.strip():
                part = 1
                continue
            if part == 0:
                for x, i in enumerate(line.strip()):
                    if i == '#':
                        walls.add((y, 2*x))
                        walls.add((y, 2*x+1))
                    elif i == 'O':
                        boxes.append([(y, 2*x), (y, 2*x+1)])
                    elif i == '@':
                        robot = (y, 2*x)
                    else:
                        pass
            else:
                instructions += line.strip()

    data = (robot, instructions, walls, boxes)
    return data

def part1(robot, instructions, walls, boxes):
    result = 0
    for i in instructions:
        y, x = robot
        my, mx = MOVES[i]
        ny = y + my
        nx = x + mx
        if (ny, nx) in walls:
            continue
        elif (ny, nx) in boxes:
            positions = [(ny, nx)]
            by = ny
            bx = nx
            push = True
            while True:
                by += my
                bx += mx
                if (by, bx) in walls:
                    push = False
                    break
                if (by, bx) not in boxes:
                    positions.append((by, bx))
                    break
            if push:
                boxes.remove(positions[0])
                boxes.add(positions[1])
                robot = (ny, nx)
        else:
            robot = (ny, nx)


    for by, bx in boxes:
        result += by*100 + bx
    print("Result 1: ", result)


def update_boxes(boxes, indices, my, mx):
    for i in indices:
        boxes[i] = [(y+my, x+mx) for y, x in boxes[i]]


def map_pos_to_id(boxes):
    pos2id = {}
    for i, box in enumerate(boxes):
        for pos in box:
            pos2id[pos] = i
    return pos2id


def find_indices(pos, boxes, walls, my, mx, pos2id, indices):
    y, x = pos
    ny = y + my
    nx = x + mx

    if (ny, nx) in walls:
        return None
    if (ny, nx) in pos2id:
        index = pos2id[(ny, nx)]
        if index not in indices:
            indices.add(index)
            for pos in boxes[index]:
                oi = find_indices(pos, boxes, walls, my, mx, pos2id, indices)
                if oi is None:
                    return None
    return True


def part2(robot, instructions, walls, boxes):
    result = 0
    pos2id = map_pos_to_id(boxes)
    for i in instructions:
        y, x = robot
        my, mx = MOVES[i]
        ny = y + my
        nx = x + mx

        if (ny, nx) in walls:
            continue
        if (ny, nx) in pos2id:
            pos2id = map_pos_to_id(boxes)
            indices = set()
            let_move = find_indices((y, x), boxes, walls, my, mx, pos2id, indices)
            if let_move:
                update_boxes(boxes, indices, my, mx)
                pos2id = map_pos_to_id(boxes)
                robot = (ny, nx)
        else:
            robot = (ny, nx)

    for values in boxes:
        result += values[0][0]*100 + values[0][1]
    print("Result 2: ", result)


def main():
    data = load_input_part1()
    part1(*data)
    data = load_input_part2()
    part2(*data)


if __name__ == '__main__':
    main()
