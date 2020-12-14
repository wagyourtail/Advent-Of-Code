
import re

def genMasksP1(inpStr):
    orMask = "0b"
    andMask = "0b"
    for c in inpStr:
        #ormask
        if c == "1":
            orMask += "1"
            andMask += "1"
        elif c == "0":
            andMask += "0"
            orMask += "0"
        else:
            andMask += "1"
            orMask += "0"
    return int(andMask, 2), int(orMask, 2)


def part1(lines):
    orMask = 0
    andMask = 2 ** 36 - 1
    mem = {}
    for line in lines:
        if line.startswith("mask = "):
            andMask, orMask = genMasksP1(line[7:])
        else:
            line = re.match(r'mem\[(\d+)] = (\d+)', line)
            mem[int(line.group(1))] = int(line.group(2)) & andMask | orMask
    return sum(mem.values())

def toBinStr(address):
    bina = str(bin(address))[2:]
    return "0" * (36 - len(bina)) + bina

def calcMask(mask, address):
    bins = toBinStr(address)
    for bit in range(36):
        if mask[bit] == "1":
            bins = bins[:bit] + "1" + bins[bit+1:]
        if mask[bit] == "X":
            bins = bins[:bit] + "X" + bins[bit+1:]
    return recurseMaskOptions(bins)

def recurseMaskOptions(bins):
    opt = []
    if "X" in bins:
        ind = bins.index("X")
        opt += recurseMaskOptions(bins[:ind] + "0" + bins[ind+1:])
        opt += recurseMaskOptions(bins[:ind] + "1" + bins[ind+1:])
    else:
        opt.append(bins)
    return opt

def part2(lines):
    mask = None
    mem = {}
    for line in lines:
        if line.startswith("mask = "):
            mask = line[7:]
        else:
            line = re.match(r'mem\[(\d+)] = (\d+)', line)
            for addr in calcMask(mask, int(line.group(1))):
                mem[addr] = int(line.group(2))
    return sum(mem.values())

def main():
    with open("input1.txt", "r") as f:
        lines = [line.replace("\n", "") for line in f]
    p1 = part1(lines)
    print(f"Part1: {p1}")
    p2 = part2(lines)
    print(f"Part2: {p2}")


if __name__ == "__main__":
    print(toBinStr(42))
    main()