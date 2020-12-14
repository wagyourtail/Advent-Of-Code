def part1(adapters):
    one = 0
    three = 0
    last = 0
    for a in adapters:
        if (a - last) == 3:
            three += 1
        if (a - last) == 1:
            one += 1
        if (a - last) > 3:
            print("ERR")
        last = a
    return (one, three)


class Adapter:
    def __init__(self, num):
        self.num = num
        self.next = []
        self.storedCount = None

    def __str__(self):
        return "Adapter(" + self.num + ")"

    def count(self):
        if self.storedCount is not None:
            return self.storedCount
        if len(self.next) == 0:
            return 1
        branches = 0
        for n in self.next:
            branches += n.count()
        self.storedCount = branches
        return branches


def part2(adapters):
    a = {}
    for s in adapters:
        a[s] = Adapter(s)
        for i in range(1, 4):
            if s - i in a:
                a[s - i].next.append(a[s])
    return a[0].count()


def main():
    adapters = [0]
    with open("input1.txt", "r") as f:
        for line in f:
            adapters.append(int(line))
    adapters.sort()
    adapters.append(max(adapters) + 3)
    p1 = part1(adapters)
    print(f"Part1: {p1[0] * p1[1]}")
    p2 = part2(adapters)
    print(f"Part2: {p2}")


if __name__ == "__main__":
    main()
