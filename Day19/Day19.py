import re

rules = {}

class Rule:
    def __init__(self, rule):
        if rule.startswith("\""):
            self.rule = "".join(rule.split("\""))
        else:
            self.rule = None
        self.subrules = [a.split() for a in rule.split("|")]

    def fullMatch(self, str):
        return self.match(str) == len(str)

    def match(self, str):
        if self.rule:
            if str.startswith(self.rule):
                return len(self.rule)
            return 0
        d = [0]
        for a in self.subrules:
            c = 0
            for sub in a:
                b = rules[sub].match(str[c:])
                if b == 0:
                    break
                c += b
            else:
                d.append(c)
        return max(d)

def main():
    global rules
    with open("input1.txt", "r") as f:
        lines = f.read().split("\n\n")
    for rule in lines[0].split("\n"):
        rule = rule.split(":")
        rules[rule[0]] = Rule(rule[1].strip()) # no bad me
    c = 0
    for line in lines[1].split("\n"):
        if rules["0"].fullMatch(line):
            c += 1
    print(f"Part1: {c}")

if __name__ == "__main__":
    main()