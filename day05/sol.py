#!/usr/bin/env python3

from collections import defaultdict

def load_input():
    order = defaultdict(list)
    updates = []
    with open('input') as fd:
        for line in fd:
            stripped = line.strip()
            if '|' in stripped:
                key, value = stripped.split('|')
                order[key].append(value)
            elif ',' in stripped:
                updates.append(stripped.split(','))
            else:
                pass
    data = [order, updates]
    return data


def part1(rules, updates):
    valid_updates = []
    for update in updates:
        for i, value in enumerate(update):
            valid = True
            allowed = rules[value]
            for j in update[i+1:]:
                if j not in allowed:
                    valid = False
                    break
            if not valid:
                break
        else:
            valid_updates.append(update)
    result = sum([int(update[(len(update)-1)//2]) for update in valid_updates])
    print("Result 1: ", result)


def part2(rules, updates):
    valid_updates = []
    for update in updates:
        fixed = []
        valid = True
        for i, value in enumerate(update):
            allowed = rules[value]
            if not fixed:
                fixed.append(value)
                continue
            for i, j in enumerate(fixed):
                if j in allowed:
                    fixed.insert(i, value)
                    valid = False
                    break
            else:
                fixed.append(value)
        if not valid:
            valid_updates.append(fixed)
    result = sum([int(update[(len(update)-1)//2]) for update in valid_updates])
    print("Result 2: ", result)


def main():
    data = load_input()
    part1(*data)
    part2(*data)


if __name__ == '__main__':
    main()
