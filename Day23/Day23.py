
def insert(string, val, pos):
    return string[:pos] + val + string[pos:]

def part1(cups, moves):
    for _ in range(moves):
        new = cups[4:]
        grabbed = cups[1:4]
        index = int(cups[0])
        for i in range(2, 6):
            if str((index - i) % 9 + 1) not in grabbed:
                break
        cups = insert(new, grabbed, new.index(str((index - i) % 9 + 1)) + 1) + str(index)
    one = cups.index("1")
    print(f"Part1: {cups[one + 1:]}{cups[:one]}")


class Cup:
    def __init__(self, value, next):
        self.next = next  # value of next number
        self.value = value  # this one's value


def part2(cups, moves):
    cupmap = {}
    cups = [int(a) for a in cups]
    for i in range(len(cups) - 1):
        cupmap[cups[i]] = Cup(cups[i], cups[i + 1])
    cupmap[cups[-1]] = Cup(cups[-1], 10)
    for i in range(10, 1000000):
        cupmap[i] = Cup(i, i+1)
    cupmap[1000000] = Cup(1000000, cups[0])
    index = cupmap[cups[0]]
    for _ in range(moves):
        # head of 3
        head = cupmap[index.next]
        # tail of 3
        tail = head
        # values of 3
        grabbed = [tail.value]
        for _ in range(2):
            tail = cupmap[tail.next]
            grabbed.append(tail.value)
        # pop the 3
        index.next = tail.next
        # -1 to -4
        for i in range(2,6):
            if (index.value - i) % 1000000 + 1 not in grabbed:
                break
        insert = cupmap[(index.value - i) % 1000000 + 1]
        tail.next = insert.next
        insert.next = head.value
        # update index
        index = cupmap[index.next]
    a = cupmap[1].next
    b = cupmap[a].next
    print(f"Part2: {a*b}")

def main():
    part1("398254716", 100)
    part2("398254716", 10000000)


if __name__ == "__main__":
    main()
