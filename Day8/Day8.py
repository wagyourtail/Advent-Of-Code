def part1(data):
    data = [d.split('|') for d in data]
    data = [x[1].strip().split() for x in data]
    data = [1 for a in data for x in a if len(x) in [2, 4, 3, 7]]
    return sum(data)


def xor(a, b):
    c = ""
    for i in a:
        if i not in b:
            c += i
    return c


def inS(a, b):
    for i in a:
        if i not in b:
            return False
    return True


def part2(data, part1_result):
    data = [d.split('|') for d in data]
    data = [[x[0].strip().split(), x[1].strip().split()] for x in data]
    total = 0
    for datum in data:
        nums = {}
        for i in datum[0]:
            if len(i) == 2:
                nums[1] = sorted(i)
            elif len(i) == 4:
                nums[4] = sorted(i)
            elif len(i) == 3:
                nums[7] = sorted(i)
            elif len(i) == 7:
                nums[8] = sorted(i)
        # 6,9,0
        sn = [sorted(i) for i in datum[0] if len(i) == 6]
        if inS(nums[4], sn[0]):
            nums[9] = sn[0]
            if inS(nums[1], sn[1]):
                nums[0] = sn[1]
                nums[6] = sn[2]
            else:
                nums[0] = sn[2]
                nums[6] = sn[1]
        elif inS(nums[4], sn[1]):
            nums[9] = sn[1]
            if inS(nums[1], sn[0]):
                nums[0] = sn[0]
                nums[6] = sn[2]
            else:
                nums[0] = sn[2]
                nums[6] = sn[0]
        else:
            nums[9] = sn[2]
            if inS(nums[1], sn[0]):
                nums[0] = sn[0]
                nums[6] = sn[1]
            else:
                nums[0] = sn[1]
                nums[6] = sn[0]

        # 2,3,5
        sn = [sorted(i) for i in datum[0] if len(i) == 5]
        if inS(nums[7], sn[0]):
            nums[3] = sn[0]
            if len(xor(nums[6], sn[1])) == 1:
                nums[5] = sn[1]
                nums[2] = sn[2]
            else:
                nums[5] = sn[2]
                nums[2] = sn[1]
        elif inS(nums[7], sn[1]):
            nums[3] = sn[1]
            if len(xor(nums[6], sn[0])) == 1:
                nums[5] = sn[0]
                nums[2] = sn[2]
            else:
                nums[5] = sn[2]
                nums[2] = sn[0]
        else:
            nums[3] = sn[2]
            if len(xor(nums[6], sn[0])) == 1:
                nums[5] = sn[0]
                nums[2] = sn[1]
            else:
                nums[5] = sn[1]
                nums[2] = sn[0]

        revNum = {}
        for i in nums:
            revNum["".join(nums[i])] = i

        s = ""
        for i in datum[1]:
            s += str(revNum["".join(sorted(i))])

        total += int(s)
    return total


def main():
    with open('inp8.txt', 'r') as f:
        data = f.read().splitlines()

    print('Part 1: {}'.format(part1_result := part1(data)))
    print('Part 2: {}'.format(part2(data, part1_result)))


if __name__ == "__main__":
    main()
