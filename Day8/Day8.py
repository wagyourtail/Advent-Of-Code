def part1(data):
    data = [d.split('|') for d in data]
    data = [x[1].strip().split() for x in data]
    data = [1 for a in data for x in a if len(x) in [2, 4, 3, 7]]
    return sum(data)


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
                nums[1] = i
            elif len(i) == 4:
                nums[4] = i
            elif len(i) == 3:
                nums[7] = i
            elif len(i) == 7:
                nums[8] = i
        # 6,9,0
        sn = [i for i in datum[0] if len(i) == 6]
        if inS(nums[4], sn[0]):
            if inS(nums[1], sn[1]):
                nums[9], nums[0], nums[6] = sn
            else:
                nums[9], nums[6], nums[0] = sn
        elif inS(nums[4], sn[1]):
            if inS(nums[1], sn[0]):
                nums[0], nums[9], nums[6] = sn
            else:
                nums[6], nums[9], nums[0] = sn
        else:
            if inS(nums[1], sn[0]):
                nums[0], nums[6], nums[9] = sn
            else:
                nums[6], nums[0], nums[9] = sn

        # 2,3,5
        sn = [i for i in datum[0] if len(i) == 5]
        if inS(nums[7], sn[0]):
            if inS(sn[1], nums[6]):
                nums[3], nums[5], nums[2] = sn
            else:
                nums[3], nums[2], nums[5] = sn
        elif inS(nums[7], sn[1]):
            if inS(sn[0], nums[6]):
                nums[5], nums[3], nums[2] = sn
            else:
                nums[2], nums[3], nums[5] = sn
        else:
            if inS(sn[0], nums[6]):
                nums[5], nums[2], nums[3] = sn
            else:
                nums[2], nums[5], nums[3] = sn

        revNum = {}
        for i in nums:
            revNum["".join(sorted(nums[i]))] = i

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
