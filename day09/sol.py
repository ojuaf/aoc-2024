#!/usr/bin/env python3

from collections import defaultdict
import itertools as it
from collections import deque

def load_input():
    data = None
    with open('input') as fd:
        data = fd.read().strip()

    return data


def part1(data):
    files = [int(data[i]) for i in range(0, len(data), 2)]
    frees = [int(data[i]) for i in range(1, len(data), 2)]

    files_id = []
    free_slots = []
    updated_files_id = []
    counter = 0
    for file, free in zip(files, frees):
        files_id.append(list(range(counter, counter + file)))
        counter += file
        free_slots.extend(range(counter, counter + free))
        counter += free
    files_id.append(list(range(counter, counter + files[-1])))
    updated_files_id = files_id.copy()

    number_ids = len(files_id)

    counter = 0
    stop = False
    for ids in range(number_ids-1, -1, -1):
        for i in range(len(files_id[ids])-1, -1, -1):
            if free_slots[counter] > updated_files_id[ids][i]:
                stop = True
                break
            updated_files_id[ids][i] = free_slots[counter]
            counter += 1
            if counter == len(free_slots):
                stop = True
                break
        if stop:
            break
    result = 0
    for i, pos in enumerate(updated_files_id):
        result += i * sum(pos)
    print("Result 1: ", result)


def part2(data):
    files = [int(data[i]) for i in range(0, len(data), 2)]
    frees = [int(data[i]) for i in range(1, len(data), 2)]

    files_id = []
    free_slots = []
    updated_files_id = []
    counter = 0
    for file, free in zip(files, frees):
        files_id.append(list(range(counter, counter + file)))
        counter += file
        free_slots.append(list(range(counter, counter + free)))
        counter += free
    files_id.append(list(range(counter, counter + files[-1])))
    updated_files_id = files_id.copy()

    number_ids = len(files_id)

    for ids in range(number_ids-1, -1, -1):
        for i, slot in enumerate(free_slots):
            size = len(files_id[ids])
            if slot and updated_files_id[ids][0] < slot[0]:
                break
            if len(slot) >= size:
                free_slots.append(updated_files_id[ids])
                updated_files_id[ids] = list(slot[:size])
                free_slots[i] = list(slot[size:])
                break
    result = 0
    for i, pos in enumerate(updated_files_id):
        result += i * sum(pos)

    print("Result 2: ", result)


def main():
    data = load_input()
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
