#!/usr/bin/env python3


from collections import defaultdict


NEIGHBOR_DIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]
DIAG_NEIGH_DIST = [(1, 1), (-1, 1), (-1, -1), (1, -1)]


def load_input():
    data = set()
    with open('input') as fd:
        for y, line in enumerate(fd):
            for x, value in enumerate(line.strip()):
                data.add((y, x, value))
    return data


def find_segments(value, data, segments):
    segments.append(value)
    neighbors = [tuple([i-j for i, j in zip(value[:2], n)]) for n in NEIGHBOR_DIST]
    for y, x in neighbors:
        if (y, x, value[2]) in data:
            data.remove((y, x, value[2]))
            find_segments((y, x, value[2]), data, segments)


def find_borders(segment):
    borders = []
    for s in segment:
        neighbors = [tuple([i-j for i, j in zip(s[:2], n)]) for n in NEIGHBOR_DIST]
        i = 0
        for y, x in neighbors:
            if (y, x, s[2]) not in segment:
                a = 2*y+NEIGHBOR_DIST[i][0]
                b = 2*x+NEIGHBOR_DIST[i][1]
                borders.append((a, b))
            i += 1
    return borders


def find_corners(segment):
    corners = 0
    for s in segment:
        for i in range(4):
            vny0 = s[0] + NEIGHBOR_DIST[i][0]
            vnx0 = s[1] + NEIGHBOR_DIST[i][1]
            vny1 = s[0] + NEIGHBOR_DIST[(i+1)%4][0]
            vnx1 = s[1] + NEIGHBOR_DIST[(i+1)%4][1]
            vn0 = (vny0, vnx0, s[2])
            vn1 = (vny1, vnx1, s[2])
            vndy = s[0] + DIAG_NEIGH_DIST[i][0]
            vndx = s[1] + DIAG_NEIGH_DIST[i][1]
            vnd = (vndy, vndx, s[2])
            if vn0 not in segment and vn1 not in segment:
               corners += 1
            elif vn0 in segment and vn1 in segment and vnd not in segment:
                corners += 1
            else:
                pass
    return corners


def process(data):
    borders = []
    segments = []
    while True:
        if not data:
            break
        value = data.pop()
        s = []
        find_segments(value, data, s)
        segments.append(s)

    for s in segments:
        b = find_borders(s)
        borders.append(b)

    result = 0
    for a, b in zip(borders, segments):
        result += len(a) * len(b)
    print("Part 1", result)

    sides = []
    for s in segments:
        corners = find_corners(s)
        sides.append(corners)

    result = 0
    for a, b in zip(sides, segments):
        result += a * len(b)

    print("Part 2", result)
    return result


def main():
    data = load_input()
    process(data)


if __name__ == '__main__':
    main()
