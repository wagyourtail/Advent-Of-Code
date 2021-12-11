
def flash(squid, squids, flashed):
    flashed.add(squid)
    for i in range(squid[0] - 1, squid[0] + 2):
        for j in range(squid[1] - 1, squid[1] + 2):
            if (i, j) in squids:
                squids[(i, j)] += 1
                if squids[(i, j)] > 9 and (i, j) not in flashed:
                    flash((i, j), squids, flashed)


def part1(data):
    data = [[int(x) for x in a] for a in data]
    squids = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            squids[(i, j)] = data[i][j]

    flash_count = 0

    for _ in range(100):
        for squid in squids:
            squids[squid] += 1

        flashed = set()

        for squid in squids:
            if squids[squid] > 9 and squid not in flashed:
                flash(squid, squids, flashed)

        flash_count += len(flashed)

        for squid in flashed:
            squids[squid] = 0

    return flash_count

def part2(data, part1_result):
    data = [[int(x) for x in a] for a in data]
    squids = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            squids[(i, j)] = data[i][j]

    gen = 0
    while True:
        gen += 1
        for squid in squids:
            squids[squid] += 1

        flashed = set()

        for squid in squids:
            if squids[squid] > 9 and squid not in flashed:
                flash(squid, squids, flashed)

        if len(flashed) == len(squids):
            break

        for squid in flashed:
            squids[squid] = 0

    return gen


def main():
    with open('inp11.txt', 'r') as f:
        data = f.read().splitlines()

    print('Part 1: {}'.format(part1_result := part1(data)))
    print('Part 2: {}'.format(part2(data, part1_result)))


if __name__ == "__main__":
    main()
