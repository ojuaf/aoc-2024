#!/usr/bin/env python3



def load_input():
    with open('input') as fd:
        data = list()
        for line in fd:
            data.append([int(i) for i in line.strip().split()])
    return data


def main():
    data = load_input()
    result = None
    list0 = list(map(lambda x: x[0], data))
    list1 = list(map(lambda x: x[1], data))

    # Task 1
    list0_sorted = sorted(list0)
    list1_sorted = sorted(list1)

    distances = [abs(i-j) for i, j in zip(list0_sorted, list1_sorted)]
    result = sum(distances)

    print("Result 1: ", result)

    # Task 2
    result = 0
    for i in list0:
        times = list1.count(i)
        result += times*i

    print("Result 2: ", result)


if __name__ == '__main__':
    main()
