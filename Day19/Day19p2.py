import re

rules = {}

def compile(a):
    if isinstance(rules[a], list):
        ss = []
        for sub in rules[a]:
            s = ""
            for b in sub:
                if b == a:
                    s += "%"
                else:
                    s += compile(b)
            ss.append(s)
        a = f"(?:{'|'.join(ss)})"
        b = str(a)
        if "%" in a:
            for _ in range(5): # depth was high enough to get right answer for AOC without crashing my computer.
                a = a.replace("%", b)
            a.replace("%", "")
        return a
    return rules[a]

def part1():
    with open("input1.txt", "r") as f:
        lines = f.read().split("\n\n")
    for a in lines[0].split("\n"):
        a = a.split(":")
        if a[1].strip().startswith("\""):
            rules[a[0]] = a[1][2]
        else:
            rules[a[0]] = [b.split() for b in a[1].split("|")]
    c = 0
    for line in lines[1].split("\n"):
        if re.fullmatch(compile("0"), line):
            c += 1
    print(f"Part1: {c}")

def part2():
    global rules
    rules = {}
    with open("input2.txt", "r") as f:
        lines = f.read().split("\n\n")
    for a in lines[0].split("\n"):
        a = a.split(":")
        if a[1].strip().startswith("\""):
            rules[a[0]] = a[1][2]
        else:
            rules[a[0]] = [b.split() for b in a[1].split("|")]
    c = 0
    for line in lines[1].split("\n"):
        if re.fullmatch(compile("0"), line):
            c += 1
    print(f"Part2: {c}")

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()