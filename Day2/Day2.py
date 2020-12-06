import re


class PasswordValidator:
    def __init__(self, rules, value):
        self.rules = rules
        self.value = value

    def validate(self):
        rules = self.rules.split()
        while len(rules):
            if not self.validateRule(rules):
                return False
        return True

    def validateRule(self, rules):
        if re.fullmatch("\\d+-\\d+", rules[0]) and re.fullmatch(".", rules[1]):
            return self.letterFreqValidator(rules.pop(0), rules.pop(0))
        return False

    def letterFreqValidator(self, freq, letter):
        freq = [int(a) for a in freq.split("-")]
        return freq[0] <= self.value.count(letter) <= freq[1]


class PasswordValidator2(PasswordValidator):
    def __init__(self, rules, value):
        super().__init__(rules, value.strip())

    def validateRule(self, rules):
        if re.fullmatch("\\d+-\\d+", rules[0]) and re.fullmatch(".", rules[1]):
            return self.letterAtPosValidator(rules.pop(0), rules.pop(0))

    def letterAtPosValidator(self, positions, letter):
        pos = [int(a) for a in positions.split("-")]
        return (self.value[pos[0] - 1] is letter) ^ (self.value[pos[1] - 1] is letter)

def part1(pwords):
    filters = []
    for pword in pwords:
        if pword.validate():
            filters.append(pword)
    return filters

def loadFile():
    inp1 = []

    # load lines
    with open('input1.txt', 'r') as f:
        for line in f:
            inp1.append(line)
    lines = []
    for line in inp1:
        line = line.split(":")
        lines.append(PasswordValidator(line[0], line[1]))
    return lines

def main():
    pwords = loadFile()
    valid = part1(pwords)
    print(f"part1: {len(valid)}")

    valid = part1([PasswordValidator2(pword.rules, pword.value) for pword in pwords])
    print(f"part2: {len(valid)}")


if __name__ == "__main__":
    main()
