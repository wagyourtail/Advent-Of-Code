

def part1(nums, preambLen):
    prev = nums[:preambLen]
    for i in range(preambLen, len(nums)):
        for j in range(preambLen):
            flag = False
            for k in range(j + 1, preambLen):
                if prev[j] + prev[k] == nums[i]:
                    flag = True
                    break
            if flag:
                del prev[0]
                prev.append(nums[i])
                break
        else:
            return nums[i]


def part2(nums, res):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            s = sum(nums[i:j])
            if s == res:
                return min(nums[i:j]) + max(nums[i:j])
            if s > res:
                break

def main():
    nums = []
    with open("input1.txt", "r") as f:
        for line in f:
            nums.append(int(line))
    p1 = part1(nums, 25)
    print(f"part1: {p1}")
    print(f"part2: {part2(nums, p1)}")


if __name__ == "__main__":
    main()