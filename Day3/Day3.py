
def part1(data):
    data = data.split('\n')
    digit_count = [0]*len(data[0])
    gamma = ""
    epsilon = ""
    for d in data:
        for k, v in enumerate(d):
            digit_count[k] += int(v)
    for i in digit_count:
        if i > len(data) / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    print(int(gamma, 2) * int(epsilon, 2))

def part2(data):
    i = -1
    d2 = data.split('\n')
    while len(d2) > 1:
        i += 1
        digit_count = 0
        for d in d2:
            digit_count += int(d[i])
        d2 = list(filter(lambda x: x[i] == ('1' if digit_count >= len(d2) / 2 else '0'), d2))
    o2 = d2[0]

    i = -1
    d2 = data.split('\n')
    while len(d2) > 1:
        i += 1
        digit_count = 0
        for d in d2:
            digit_count += int(d[i])
        d2 = list(filter(lambda x: x[i] == ('0' if digit_count >= len(d2) / 2 else '1'), d2))
    co2 = d2[0]
    print(int(co2, 2) * int(o2, 2))

def main():
    with open('inp3.txt', 'r') as f:
        data = f.read()
#     data = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010"""
    part1(data)
    part2(data)

if __name__ == '__main__':
    main()