import copy
from collections import defaultdict


def part1(data):
    polymer = data.pop(0)
    sub = {}
    for line in data:
        if len(line):
            l = line.split("->")
            sub[l[0].strip()] = l[1].strip()

    for _ in range(10):
        offset = 0
        for i in range(len(polymer) - 1):
            if (polymer[i + offset] + polymer[i + offset + 1]) in sub:
                polymer = polymer[:i + offset + 1] + sub[(polymer[i + offset] + polymer[i + offset + 1])] + polymer[i + offset + 1:]
                offset += 1

    most = polymer[0]
    least = polymer[0]
    for i in set(list(polymer)):
        if polymer.count(i) > polymer.count(most):
            most = i
        if polymer.count(i) < polymer.count(least):
            least = i
    return polymer.count(most) - polymer.count(least)


def part2(data, part1_result):
    polymer = data.pop(0)
    sub = {}
    for line in data:
        if len(line):
            l = line.split("->")
            sub[l[0].strip()] = l[1].strip()

    p2 = defaultdict(lambda: 0)
    for i in range(len(polymer) - 1):
        p2[polymer[i] + polymer[i + 1]] += 1


    counts = defaultdict(lambda: 0)
    for i in range(len(polymer)):
        counts[polymer[i]] += 1

    for _ in range(40):
        p3 = copy.copy(p2)
        for i in p3:
            if i in sub:
                p2[i] -= p3[i]
                p2[i[0] + sub[i]] += p3[i]
                p2[sub[i] + i[1]] += p3[i]
                counts[sub[i]] += p3[i]

    most = polymer[0]
    least = polymer[0]
    for i in counts:
        if counts[i] > counts[most]:
            most = i
        if counts[i] < counts[least]:
            least = i
    return counts[most] - counts[least]



def main():
    with open('inp14.txt', 'r') as f:
        data = f.read().splitlines()

    print('Part 1: {}'.format(part1_result := part1(data[:])))
    print('Part 2: {}'.format(part2(data[:], part1_result)))


if __name__ == "__main__":
    main()
