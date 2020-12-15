
def part1(inp):
    while len(inp) < 2020:
        prev = inp[-1]
        for i in range(len(inp) - 2, -1, -1):
            if prev == inp[i]:
                inp.append(len(inp) - i - 1)
                break
        else:
            inp.append(0)
    return inp[-1]

def part2(inp, leng):
    a = {}
    j = 0
    for i in inp[:-1]:
        a[i] = j
        j += 1
    prev = inp[-1]
    for i in range(len(inp) - 1, leng - 1):
        if prev in a:
            sp = prev
            prev = i - a[prev]
            a[sp] = i
        else:
            a[prev] = i
            prev = 0
    return prev

def main():
    inputVal = [int(a) for a in "8,11,0,19,1,2".split(",")]
    p1 = part2(inputVal[:], 2020)
    print(f"Part1: {p1}")
    p2 = part2(inputVal, 30000000)
    print(f"Part2: {p2}")


if __name__ == "__main__":
    main()
