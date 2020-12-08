

class Computer:
    def __init__(self, instructions):
        self.code = instructions
        self.pc = 0
        self.r = [0]
        self.debug = []
        self.halted = False

    def run(self):
        while self.pc < len(self.code):
            self.DoOp(self.code[self.pc])

    def DoOp(self, codePoint):
        # debug
        if self.pc in self.debug:
            self.pc = len(self.code)
            self.halted = True
            return
        else:
            self.debug.append(self.pc)
        # enddebug
        codePoint = codePoint.split()
        getattr(self, codePoint[0])(*codePoint[1:])  # so is this like java reflection...

    def acc(self, num):
        self.r[0] += int(num)
        self.pc += 1

    def nop(self, num):
        self.pc += 1

    def jmp(self, num):
        self.pc += int(num)


# shallow copy
def copy(listt):
    return [a for a in listt]


def p2Attempt(lines):
    com = Computer(lines)
    com.run()
    if not com.halted:
        print(f"part2: {com.r[0]}")
        return True
    return False


def part2(lines):
    for ln in range(len(lines)):
        if lines[ln].split()[0] == "nop":
            cp = copy(lines)
            cp[ln] = cp[ln].replace("nop", "jmp")
            if p2Attempt(cp):
                break
        if lines[ln].split()[0] == "jmp":
            cp = copy(lines)
            cp[ln] = cp[ln].replace("jmp", "nop")
            if p2Attempt(cp):
                break


def main():
    lines = []
    with open('input1.txt', 'r') as f:
        lines += [l.strip() for l in f.readlines()]
    com = Computer(lines)
    com.run()
    print(f"part1: {com.r[0]}")
    part2(lines)


if __name__ == "__main__":
    main()
