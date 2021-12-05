from collections import defaultdict


class Vec2d:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def part1(data):
    vecs = []
    for line in data:
        a, b = line.split('->')
        a, c = list(map(int, a.strip().split(',')))
        b, d = list(map(int, b.strip().split(',')))
        vecs.append(Vec2d(a, c, b, d))

    heatmap = defaultdict(lambda: 0)

    # filter to horizontal and vertical lines
    to_remove = []
    for vec in vecs:
        if vec.x1 != vec.x2 and vec.y1 != vec.y2:
            to_remove.append(vec)
    for vec in to_remove:
        vecs.remove(vec)

    for vec in vecs:
        if vec.x1 == vec.x2:
            y = sorted([vec.y1, vec.y2])
            for i in range(y[0], y[1] + 1):
                heatmap[(vec.x1, i)] += 1
        elif vec.y1 == vec.y2:
            x = sorted([vec.x1, vec.x2])
            for i in range(x[0], x[1] + 1):
                heatmap[(i, vec.y1)] += 1

    c = 0
    for k in heatmap:
        if heatmap[k] > 1:
            c += 1

    print(c)


def part2(data):
    vecs = []
    for line in data:
        a, b = line.split('->')
        a, c = list(map(int, a.strip().split(',')))
        b, d = list(map(int, b.strip().split(',')))
        vecs.append(Vec2d(a, c, b, d))

    heatmap = defaultdict(lambda: 0)

    for vec in vecs:
        if vec.x1 == vec.x2:
            y = sorted([vec.y1, vec.y2])
            for i in range(y[0], y[1] + 1):
                heatmap[(vec.x1, i)] += 1
        elif vec.y1 == vec.y2:
            x = sorted([vec.x1, vec.x2])
            for i in range(x[0], x[1] + 1):
                heatmap[(i, vec.y1)] += 1
        else:
            # step along vector
            x = min(vec.x1, vec.x2)
            y = vec.y1 if vec.x1 == x else vec.y2
            y1 = min(vec.y1, vec.y2)
            y2 = max(vec.y1, vec.y2)
            x1 = min(vec.x1, vec.x2)
            x2 = max(vec.x1, vec.x2)
            slope = (vec.y2 - vec.y1) / (vec.x2 - vec.x1)
            while x1 <= x <= x2 and y1 <= y <= y2:
                heatmap[(x, y)] += 1
                x += 1
                y += slope
    c = 0
    for k in heatmap:
        if heatmap[k] > 1:
            c += 1

    for j in range(0, 10):
        for i in range(0, 9):
            print(heatmap[(i, j)], end='')
        print()

    print(c)


def main():
    with open("inp5.txt", "r") as f:
        data = f.readlines()
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
