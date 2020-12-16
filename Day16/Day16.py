import re

class FieldClassifier:
    def __init__(self, name, value):
        g = re.match(r'(\d+)-(\d+) or (\d+)-(\d+)', value)
        self.ranges = [range(int(g.group(1)), int(g.group(2)) + 1), range(int(g.group(3)), int(g.group(4)) + 1)]
        self.name = name

    def matches(self, field):
        for rangeVal in self.ranges:
            if field in rangeVal:
                return True
        return False

def part1(inp, classifiers):
    bad = []
    i = 0
    while i < len(inp[2]):
        for field in inp[2][i]:
            for classif in classifiers:
                if classif.matches(field):
                    break
            else:
                del inp[2][i]
                i -= 1
                bad.append(field)
                break
        i += 1
    return sum(bad)

def part2(inp, classifiers):
    fields = {}
    for i in range(len(classifiers)):
        fields[i] = []
        for ticket in inp[2]:
            fields[i].append(ticket[i])
    scores = {}
    for j in range(len(classifiers)):
        scores[classifiers[j].name] = {}
        for i in range(len(classifiers)):
            score = 0
            for fv in fields[i]:
                if classifiers[j].matches(fv):
                    score += 1
            if score in scores[classifiers[j].name]:
                scores[classifiers[j].name][score].append(i)
            else:
                scores[classifiers[j].name][score] = [i]
    for i in scores:
        a = []
        for j in range(len(inp[2]), min(scores[i].keys()) - 1, -1):
            a.append(scores[i][j] if j in scores[i] else [])
        scores[i] = a
    fieldNames = {}

    flag = True
    while flag:
        for fieldName in scores:
            i = 0
            while len(scores[fieldName][i]) == 0:
                i += 1
            if len(scores[fieldName][i]) == 1:
                fieldNames[fieldName] = scores[fieldName][i][0]
                del scores[fieldName]
                for scoreVals in scores.values():
                    for val in scoreVals:
                        if fieldNames[fieldName] in val:
                            val.remove(fieldNames[fieldName])
                break
        else:
            flag = False
    i = 1
    inp[1][0] = [int(a) for a in inp[1][0].split(",")]
    for fieldName in fieldNames:
        if fieldName.startswith("departure"):
            i *= inp[1][0][fieldNames[fieldName]]
    return i


def main():
    with open("input1.txt", "r") as f:
        inp = f.read()
    inp = [a.split("\n") for a in inp.split("\n\n")]
    del inp[1][0]
    del inp[2][0]
    inp[2] = [[int(a) for a in b.split(",")] for b in inp[2]]

    classifiers = []
    for classif in inp[0]:
        classifiers.append(FieldClassifier(*[a.strip() for a in classif.split(":")]))
    p1 = part1(inp, classifiers)
    print(f"Part1: {p1}")
    p2 = part2(inp, classifiers)
    print(f"Part2: {p2}")


if __name__ == "__main__":
    main()
