def part1(data):
    pass


def part2(data, part1_result):
    pass


def main():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    print('Part 1: {}'.format(part1_result := part1(data)))
    print('Part 2: {}'.format(part2(data, part1_result)))


if __name__ == "__main__":
    main()
