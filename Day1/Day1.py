testInp = """199
200
208
210
200
207
240
269
260
263"""


def part1(nums):
    prev = nums[0]
    dhigher = 0
    for num in nums[1:]:
        if num > prev:
            dhigher += 1
        prev = num
    print(dhigher)

def part2(nums):
    prev1 = nums[0:2]
    dhigher = 0
    for i in range(1, len(nums) - 2):
        cur = nums[i:i+3]
        if sum(prev1) < sum(cur):
            dhigher += 1
        prev1 = cur
    print(dhigher)



def main():
    with open('inp1.txt') as f:
        nums = [int(line) for line in f]
    # nums = [int(line) for line in testInp.split('\n')]
    part1(nums)
    part2(nums)


if __name__ == "__main__":
    main()
