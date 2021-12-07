import statistics

def part1(data):
    data = [int(x) for x in data]
    target = statistics.median(data)
    cost = 0
    for i in data:
        cost += abs(i - target)
    return cost

def part2(data, part1_result):
    data = [int(x) for x in data]
    min_c = 1e64
    for target in range(min(data), max(data) + 1):
        cost = 0
        for i in data:
            cost += sum(range(int(abs(i - target)) + 1))
        if cost < min_c:
            min_c = cost
    return min_c


def main():
    with open('inp7.txt', 'r') as f:
        data = f.read().split(",")

    print('Part 1: {}'.format(part1_result := part1(data)))
    print('Part 2: {}'.format(part2(data, part1_result)))


if __name__ == "__main__":
    main()
