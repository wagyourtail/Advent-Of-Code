def getCellScore(cell, active):
    count = 0
    for x in range(cell[0] - 1, cell[0] + 2):
        for y in range(cell[1] - 1, cell[1] + 2):
            for z in range(cell[2] - 1, cell[2] + 2):
                if (x, y, z) != cell and (x, y, z) in active:
                    count += 1
    return count


def tick(active):
    nextActive = []
    for cell in active:
        for x in range(cell[0] - 1, cell[0] + 2):
            for y in range(cell[1] - 1, cell[1] + 2):
                for z in range(cell[2] - 1, cell[2] + 2):
                    if (x, y, z) not in active and (x, y, z) not in nextActive:
                        if getCellScore((x, y, z), active) == 3:
                            nextActive.append((x, y, z))

        if 2 <= getCellScore(cell, active) <= 3:
            nextActive.append(cell)
    return nextActive


def part1(active):
    for i in range(6):
        # print("\n")
        # print(i)
        # print("\n")
        # x = [a[0] for a in active]
        # y = [a[1] for a in active]
        # z = [a[2] for a in active]
        # for zz in range(min(z), max(z) + 1):
        #     print(f"\nz={zz}", end = "")
        #     for yy in range(min(y), max(y) + 1):
        #         print("")
        #         for xx in range(min(x), max(x) + 1):
        #             if (xx,yy,zz) in active:
        #                 print("#", end= "")
        #             else:
        #                 print(".", end= "")
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
                    active.append((x, y, 0))
            y += 1
    p1 = part1(active)
    print(f"Part1: {p1}")


if __name__ == "__main__":
    main()
