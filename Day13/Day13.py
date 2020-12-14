import math


def part1(busses, time):
    b2 = {}
    for bus in busses:
        b2[math.ceil(time / bus) * bus] = bus
    first = min(b2.keys())
    return (first - time) * b2[first]

# thx geeks4geeks
def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1

def part2(busses, smallest_id):
    b2 = []
    for i in range(len(busses)):
        if not busses[i] == "x":
            b2.append((i, int(busses[i])))
    ## this takes way too long...
    # i = 0
    # flag = True
    # while flag:
    #     i += smallest_id
    #     flag = False
    #     for bus in b2:
    #         if (i + bus[0]) % bus[1] != 0:
    #             flag = True
    #             continue

    ## did not work
    # print("Ask Wolfram: 0 = " + " + ".join([f"((x + {bus[0]}) mod {bus[1]})" for bus in b2]))
    # apparently pro isn't good enough

    # linear algebra? I didn't do well in that class, time to do some google.
    # found it https://tigerweb.towson.edu/nmcnew/m565s19/notes/week_5.pdf
    # chineese remainder theorem, only works with coprimes, assume good, test and brute force if not
    x = 0
    m = 1
    for i in range(len(b2)):
        ai = -b2[i][0] % b2[i][1]
        ni = 1
        for j in range(len(b2)):
            if j == i:
                continue
            ni *= b2[j][1]
        n_bari = modInverse(ni, b2[i][1])
        x += ai * ni * n_bari
        m *= b2[i][1]
    return x % m


def main():
    lines = []
    with open("input1.txt", "r") as f:
        for line in f:
            lines.append(line)
    time = int(lines[0])
    busses = [int(a.strip()) for a in lines[1].split(",") if a.strip() != "x"]
    smallest_id = min(busses)
    p1 = part1(busses, time)
    print(f"Part1: {p1}")
    busses = [bus.strip() for bus in lines[1].split(",")]
    p2 = part2(busses, smallest_id)
    print(f"Part2: {p2}")


if __name__ == "__main__":
    main()