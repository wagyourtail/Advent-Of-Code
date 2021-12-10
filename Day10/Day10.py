import statistics


def part1(data):
    score = 0
    for line in data:
        stack = []
        for char in line:
            if char in '{[(<':
                stack.append(char)
            elif char in '}])>':
                if len(stack) == 0:
                    print("close without open")
                    break
                else:
                    if char == '}' and stack[-1] == '{':
                        stack.pop()
                    elif char == ']' and stack[-1] == '[':
                        stack.pop()
                    elif char == ')' and stack[-1] == '(':
                        stack.pop()
                    elif char == '>' and stack[-1] == '<':
                        stack.pop()
                    else:
                        score += [3, 57, 1197, 25137][')]}>'.index(char)]
                        break
    return score


def part2(data, part1_result):
    valid_or_incomplete = []
    for line in data:
        stack = []
        for char in line:
            if char in '{[(<':
                stack.append(char)
            elif char in '}])>':
                if len(stack) == 0:
                    print("close without open")
                    break
                else:
                    if char == '}' and stack[-1] == '{':
                        stack.pop()
                    elif char == ']' and stack[-1] == '[':
                        stack.pop()
                    elif char == ')' and stack[-1] == '(':
                        stack.pop()
                    elif char == '>' and stack[-1] == '<':
                        stack.pop()
                    else:
                        break
        else:
            valid_or_incomplete.append(stack)

    scores = []
    for line in valid_or_incomplete:
        score = 0
        for char in line[::-1]:
            score *= 5
            if char == '(':
                score += 1
            elif char == '[':
                score += 2
            elif char == '{':
                score += 3
            elif char == '<':
                score += 4
        scores.append(score)

    return statistics.median(scores)


def main():
    with open('inp10.txt', 'r') as f:
        data = f.read().splitlines()

    print('Part 1: {}'.format(part1_result := part1(data)))
    print('Part 2: {}'.format(part2(data, part1_result)))


if __name__ == "__main__":
    main()
