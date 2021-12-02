class turtle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def executeInstr(self, instr):
        for inst in instr.split("\n"):
            dir, count = inst.split()
            count = int(count)
            getattr(self, dir)(count)

    def up(self, count):
        self.y += count

    def down(self, count):
        self.y -= count

    def forward(self, count):
        self.x += count


class turtle2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.aim = 0

    def executeInstr(self, instr):
        for inst in instr.split("\n"):
            dir, count = inst.split()
            count = int(count)
            getattr(self, dir)(count)

    def up(self, count):
        self.aim += count

    def down(self, count):
        self.aim -= count

    def forward(self, count):
        self.y += self.aim * count
        self.x += count


def part1(instr):
    t = turtle(0, 0)
    t.executeInstr(instr)
    print(f"Part 1: {t.x} {t.y}: {t.x * t.y}")


def part2(instr):
    t = turtle2(0, 0)
    t.executeInstr(instr)
    print(f"Part 2: {t.x} {t.y}: {t.x * t.y}")


def main():
    with open("inp2.txt") as f:
        instr = f.read()
    part1(instr.strip())
    part2(instr.strip())


if __name__ == "__main__":
    main()
