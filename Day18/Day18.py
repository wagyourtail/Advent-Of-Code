import re

def toGroups(line):
    head = []
    depthArr = [head]
    prev = 0
    for i in range(len(line)):
        if line[i] == '(':
            if i > prev:
                depthArr[-1].append(line[prev:i])
            depthArr[-1].append([])
            depthArr.append(depthArr[-1][-1])
            prev = i + 1
        if line[i] == ")":
            if i > prev:
                depthArr[-1].append(line[prev:i])
            depthArr.pop()
            prev = i + 1
    if len(line) - 1 > prev:
        depthArr[-1].append(line[prev:])
    return head

def doBadMath(parsedLine):
    for i in range(len(parsedLine)):
        if isinstance(parsedLine[i], list):
            parsedLine[i] = doBadMath(parsedLine[i])
    parsedLine = "".join(parsedLine)
    while a := re.match(r"(\d+(?:\+|\*)\d+)(.*)", parsedLine):
        parsedLine = str(eval(a.group(1))) + a.group(2)
    return parsedLine

def doBadMathPart2(parsedLine):
    for i in range(len(parsedLine)):
        if isinstance(parsedLine[i], list):
            parsedLine[i] = doBadMathPart2(parsedLine[i])
    parsedLine = "".join(parsedLine)
    while len(a := [b for b in re.finditer(r"\d+\+\d+", parsedLine)][::-1]): #this line is kinda cancer
        for m in a:
            parsedLine = parsedLine[:m.start()] + str(eval(m.group(0))) + parsedLine[m.end():]
    return str(eval(parsedLine))

def main():
    with open("input1.txt", "r") as f:
        lines = ["".join(a.strip().split()) for a in f]
    p1l = [toGroups(a) for a in lines]
    p2l = [toGroups(a) for a in lines]
    print(f"Part1: {sum([int(doBadMath(a)) for a in p1l])}")
    print(f"Part1: {sum([int(doBadMathPart2(a)) for a in p2l])}")

if __name__ == "__main__":
    main()