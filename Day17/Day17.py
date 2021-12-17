import re


def part1(data):
    x1 = int(data[0])
    x2 = int(data[1])
    [y1, y2] = sorted([int(data[2]), int(data[3])])

    soln = 0

    for i in range(abs(y1)):
        i_0 = i * (i + 1) / 2
        for j in range(i, abs(y1) + 1):
            j_0 = j * (j + 1) / 2
            if y1 <= i_0 - j_0 <= y2:
                soln = i_0

    return soln


def part2(data, part1_result):
    [x1, x2] = sorted([int(data[0]), int(data[1])])
    [y1, y2] = sorted([int(data[2]), int(data[3])])
    #
    # soln_x = set()
    # soln_y = set()
    #
    # for i in range(abs(y1) + 1):
    #     i_0 = i * (i + 1) / 2
    #     for j in range(i, abs(y1) + 2):
    #         j_0 = j * (j + 1) / 2
    #         if y1 <= i_0 - j_0 <= y2:
    #             soln_y.add(i)
    #             soln_y.add(-i)
    #             # soln_y.add((i, j+i))
    #             # soln_y.add((-i, j-2*i))
    #
    # for i in range(y1, y2 + 1):
    #     soln_y.add(i)
    #     # soln_y.add((i, 1))
    #
    # for i in range(abs(x2) + 1):
    #     i_0 = i * (i + 1) / 2
    #     for j in range(i, abs(x2) + 2):
    #         j_0 = j * (j + 1) / 2
    #         if x1 <= j_0 - i_0 <= x2:
    #             soln_x.add(j)
    #             # soln_x.add((j, j-2*i))
    #
    # for i in range(x1, x2 + 1):
    #     soln_x.add(i)
    #     # soln_x.add((i, 1))
    #
    ss = set()
    #
    # # print(sorted(soln_x))
    # # print(sorted(soln_y))

    for x in range(0, 231):
        for y in range(-100, 101):
            if test(x, y, x1, y1, x2, y2):
                ss.add((x, y))
            # if x[1] == y[1]:
            #     ss.add((x[0], y[0]))

    # print(sorted(ss))
    return len(ss)


def test(i, j, x1, y1, x2, y2):
    x, y = 0, 0
    while True:
        x += i
        y += j
        j -= 1
        if i > 0:
            i -= 1
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True
        if x2 < x or y < y1:
            return False



def main():
    with open('inp17.txt', 'r') as f:
        data = re.match(r'^target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)$', f.readline()).groups()

    print('Part 1: {}'.format(part1_result := part1(data)))
    print('Part 2: {}'.format(part2(data, part1_result)))


if __name__ == "__main__":
    main()
