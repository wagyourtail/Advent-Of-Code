def convertLine(line, coords=None):
    if coords is None:
        coords = [0, 0, 0]
    for a in line.replace("ne", " +x -z ").replace("nw", " +y -z ").replace("sw", " -x +z ").replace("se", " -y +z ").replace("e", " -y +x ").replace(
            "w", " -x +y ").split():
        neg = 1
        if "-" in a:
            neg = -1
        if "x" in a:
            coords[0] += neg
        if "y" in a:
            coords[1] += neg
        if "z" in a:
            coords[2] += neg
    return tuple(coords)


def part1(coords):
    a = set()
    for c in set(coords):
        if coords.count(c) % 2:
            a.add(c)
    print(f"Part1: {len(a)}")
    return a

def getNeighbors(coord, coords):
    black = set()
    white = set()
    for dir in ("ne","nw","se","sw","w","e"):
        tile = convertLine(dir, list(coord))
        if tile in coords:
            black.add(tile)
        else:
            white.add(tile)
    return black, white

def part2Tick(coords):
    nextTick = set()
    whiteCandidates = set()
    for coord in coords:
        black, white = getNeighbors(coord, coords)
        if 0 < len(black) < 3:
            nextTick.add(coord)
        whiteCandidates.update(white)
    for candidate in whiteCandidates:
        black, white = getNeighbors(candidate, coords)
        if len(black) == 2:
            nextTick.add(candidate)
    return nextTick

def main():
    coords = []
    with open("input1.txt", "r") as f:
        for line in f:
            coords.append(convertLine(line))
    coords = part1(coords)
    for i in range(100):
        coords = part2Tick(coords)
    print(f"Part2: {len(coords)}")

if __name__ == "__main__":
    main()
