def getCellScore(cell, active):
    count = 0
    for x in range(cell[0] - 1, cell[0] + 2):
        for y in range(cell[1] - 1, cell[1] + 2):
            for z in range(cell[2] - 1, cell[2] + 2):
                for w in range(cell[3] - 1, cell[3] + 2):
                    if (x, y, z, w) != cell and (x, y, z, w) in active:
                        count += 1
    return count


def tick(active):
    nextActive = []
    for cell in active:
        for x in range(cell[0] - 1, cell[0] + 2):
            for y in range(cell[1] - 1, cell[1] + 2):
                for z in range(cell[2] - 1, cell[2] + 2):
                    for w in range(cell[3] - 1, cell[3] + 2):
                        if (x, y, z, w) not in active and (x, y, z, w) not in nextActive:
                            if getCellScore((x, y, z, w), active) == 3:
                                nextActive.append((x, y, z, w))

        if 2 <= getCellScore(cell, active) <= 3:
            nextActive.append(cell)
    return nextActive


def part2(active):
    for i in range(6):
        print(len(active))
        active = tick(active)
    return len(active)


def main():
    with open("input1.txt", "r") as f:
        active = []
        y = 0
        for line in f:
            line = line.strip()
            for x in range(len(line)):
                if line[x] == "#":
                    active.append((x, y, 0, 0))
            y += 1
    p2 = part2(active)
    print(f"Part2: {p2}")

if __name__ == "__main__":
    main()
