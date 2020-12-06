import re

def p1ParseGroup(group):
    a = []
    group = "".join(group.split()) #remove all spaces
    for b in group:
        if b not in a:
            a.append(b)
    return a

def part1(groups):
    groups = [p1ParseGroup(g) for g in groups]
    a = 0
    for group in groups:
        a += len(group)
    return a

def p2ParseGroup(group):
    a = []
    group = group.strip().split("\n")
    for b in group[0]:
        for p in group[1:]:
            if b not in p:
                break
        else:
            a.append(b)
    return a

def part2(groups):
    groups = [p2ParseGroup(g) for g in groups]
    a = 0
    for group in groups:
        a += len(group)
    return a

def main():
    groups = []
    # load lines
    with open('input1.txt', 'r') as f:
        lines = re.finditer(r"([\s\S]+?)(?:\n\s*\n|\Z)", f.read(), re.MULTILINE)
        for match in lines:
            groups.append(match.group(0))
    print(f"part1: {part1(groups)}")
    print(f"part2: {part2(groups)}")

if __name__ == "__main__":
    main()