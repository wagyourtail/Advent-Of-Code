
def part1(inp1):
    #brute force add to 2020
    for a in inp1:
        for b in inp1:
            if a + b == 2020:
                return a*b

def part2(inp1):
    for a in inp1:
        for b in inp1:
            for c in inp1:
                if a + b + c == 2020:
                    return a*b*c

def main():
    inp1 = []

    #load lines
    with open('input1.txt', 'r') as f:
        for line in f:
            inp1.append(int(line))

    print(f"part1: {part1(inp1)}")
    print(f"part2: {part2(inp1)}")


if __name__ == "__main__":
    main()
