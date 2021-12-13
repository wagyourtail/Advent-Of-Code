def part1(data):
    points = set()
    folds = []
    for i in range(len(data)):
        if data[i].startswith('fold'):
            folds.append(tuple(data[i].split()[2].split("=")))
        elif len(data[i]):
            points.add(tuple([int(x) for x in data[i].split(',')]))

    for fold in folds:
        dim = fold[0]
        val = int(fold[1])
        newPoints = set()
        for point in points:
            if dim == 'x' and point[0] >= val:
                newPoints.add((val-(point[0]-val), point[1]))
            elif dim == 'y' and point[1] >= val:
                newPoints.add((point[0], val-(point[1]-val)))
            else:
                newPoints.add(point)
        points = newPoints

        return len(points)





def part2(data, part1_result):
    points = set()
    folds = []
    for i in range(len(data)):
        if data[i].startswith('fold'):
            folds.append(tuple(data[i].split()[2].split("=")))
        elif len(data[i]):
            points.add(tuple([int(x) for x in data[i].split(',')]))

    for fold in folds:
        dim = fold[0]
        val = int(fold[1])
        newPoints = set()
        for point in points:
            if dim == 'x' and point[0] >= val:
                newPoints.add((val - (point[0] - val), point[1]))
            elif dim == 'y' and point[1] >= val:
                newPoints.add((point[0], val - (point[1] - val)))
            else:
                newPoints.add(point)
        points = newPoints

    points = list(points)
    minX = points[0][0]
    maxX = points[0][0]
    minY = points[0][1]
    maxY = points[0][1]
    for (x, y) in points:
        if x < minX:
            minX = x
        if x > maxX:
            maxX = x
        if y < minY:
            minY = y
        if y > maxY:
            maxY = y

    s = "\n"
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            if (x, y) in points:
                s += '#'
            else:
                s += ' '
        s += '\n'
    return s


def main():
    with open('inp13.txt', 'r') as f:
        data = f.read().splitlines()

    print('Part 1: {}'.format(part1_result := part1(data)))
    print('Part 2: {}'.format(part2(data, part1_result)))


if __name__ == "__main__":
    main()
