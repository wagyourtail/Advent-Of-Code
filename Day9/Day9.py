from collections import defaultdict


def part1(data):
    data = [[int(x) for x in a] for a in data]
    su = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            # top
            if i != 0:
                if data[i - 1][j] <= data[i][j]:
                    continue
            # bottom
            if i != len(data) - 1:
                if data[i + 1][j] <= data[i][j]:
                    continue
            # left
            if j != 0:
                if data[i][j - 1] <= data[i][j]:
                    continue
            # right
            if j != len(data[i]) - 1:
                if data[i][j + 1] <= data[i][j]:
                    continue

            su += data[i][j] + 1
    return su


def part2(data, part1_result):
    data = [[int(x) for x in a] for a in data]
    low = []
    su = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            # top
            if i != 0:
                if data[i - 1][j] <= data[i][j]:
                    continue
            # bottom
            if i != len(data) - 1:
                if data[i + 1][j] <= data[i][j]:
                    continue
            # left
            if j != 0:
                if data[i][j - 1] <= data[i][j]:
                    continue
            # right
            if j != len(data[i]) - 1:
                if data[i][j + 1] <= data[i][j]:
                    continue
            low.append((i, j))

    basins_by_size = defaultdict(list)
    for i, j in low:
        already = []
        basin(i, j, already, data)
        basins_by_size[len(already)].append((i, j))

    a = []
    sizes = []
    for size in sorted(basins_by_size.keys(), reverse=True):
        if len(a) >= 3:
            break
        a += basins_by_size[size]
        sizes += [size] * min(3 - len(sizes), len(basins_by_size[size]))
    return sizes[0] * sizes[1] * sizes[2]


def basin(i, j, already, data):
    if data[i][j] == 9:
        return
    already.append((i, j))
    if i != 0 and (i - 1, j) not in already:
        basin(i - 1, j, already, data)
    if i != len(data) - 1 and (i + 1, j) not in already:
        basin(i + 1, j, already, data)
    if j != 0 and (i, j - 1) not in already:
        basin(i, j - 1, already, data)
    if j != len(data[i]) - 1 and (i, j + 1) not in already:
        basin(i, j + 1, already, data)


def main():
    with open('inp9.txt', 'r') as f:
        data = f.read().splitlines()

    print('Part 1: {}'.format(part1_result := part1(data)))
    print('Part 2: {}'.format(part2(data, part1_result)))


if __name__ == "__main__":
    main()
