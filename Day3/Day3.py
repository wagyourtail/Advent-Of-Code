
def part1(field, dy, dx):
    y = 0
    x = 0
    trees = 0
    while y < len(field):
        if field[y][x % len(field[y])] == '#':
            trees += 1
        x += dx
        y += dy
    return trees

def part2(field):
    a = 1
    for b in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        a *= part1(field, b[0], b[1])
    return a


def main():
    inp1 = []
    # load lines
    with open('input1.txt', 'r') as f:
        for line in f:
            inp1.append(line.replace('\n', ''))

    print(f"part1: {part1(inp1, 1, 3)}")
    print(f"part2: {part2(inp1)}")
if __name__ == "__main__":
    main()
