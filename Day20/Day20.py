# I contemplated moving to matlab for this one...
import re

TileG = []


class Tile:
    def __init__(self, data, id):
        self.borders = None  # up, down, left, right
        self.matchingTiles = [None, None, None, None]
        self.id = id
        self.data = data

    def getBorders(self):
        if self.borders is not None:
            return self.borders
        self.borders = []
        self.borders.append(self.data[0])
        self.borders.append(self.data[-1])
        left = ""
        right = ""
        for i in range(len(self.data)):
            left += self.data[i][0]
            right += self.data[i][-1]
        self.borders.append(left)
        self.borders.append(right)
        return self.borders

    def linkMatching(self):
        for border in self.getBorders():
            if self.matchingTiles[self.borders.index(border)]:
                continue
            for tile in TileG:
                if tile is self:
                    continue
                if border in tile.getBorders():
                    self.matchingTiles[self.borders.index(border)] = tile
                    tile.matchingTiles[tile.borders.index(border)] = self
                elif border[::-1] in tile.getBorders():
                    self.matchingTiles[self.borders.index(border)] = tile
                    tile.matchingTiles[tile.borders.index(border[::-1])] = self

    def flipV(self):
        self.data = self.data[::-1]
        self.borders[0], self.borders[1] = self.borders[1], self.borders[0]
        self.borders[2], self.borders[3] = self.borders[2][::-1], self.borders[3][::-1]
        self.matchingTiles[0], self.matchingTiles[1] = self.matchingTiles[1], self.matchingTiles[0]

    def flipH(self):
        self.data = [a[::-1] for a in self.data]
        self.borders[2], self.borders[3] = self.borders[3], self.borders[2]
        self.borders[0], self.borders[1] = self.borders[0][::-1], self.borders[1][::-1]
        self.matchingTiles[2], self.matchingTiles[3] = self.matchingTiles[3], self.matchingTiles[2]

    def rotate(self):
        data = [""] * len(self.data)
        for i in range(len(self.data) - 1, -1, -1):
            for j in range(len(self.data)):
                data[j] += self.data[i][j]
        self.data = data
        self.borders[0], self.borders[1], self.borders[2], self.borders[3] = self.borders[2][::-1], self.borders[3][::-1], self.borders[1], \
                                                                             self.borders[0]
        self.matchingTiles[0], self.matchingTiles[1], self.matchingTiles[2], self.matchingTiles[3] = self.matchingTiles[2], self.matchingTiles[3], \
                                                                                                     self.matchingTiles[1], self.matchingTiles[0]

    def orientRight(self):
        if self.matchingTiles[3]:
            while self.borders[3] != self.matchingTiles[3].borders[2] and self.borders[3][::-1] != self.matchingTiles[3].borders[2]:
                self.matchingTiles[3].rotate()
            if self.borders[3] != self.matchingTiles[3].borders[2]:
                self.matchingTiles[3].flipV()
            self.matchingTiles[3].orientRight()

    def orientDown(self):
        if self.matchingTiles[1]:
            while self.borders[1] != self.matchingTiles[1].borders[0] and self.borders[1][::-1] != self.matchingTiles[1].borders[0]:
                self.matchingTiles[1].rotate()
            if self.borders[1] != self.matchingTiles[1].borders[0]:
                self.matchingTiles[1].flipH()
            self.matchingTiles[1].orientDown()


def stitchRow(tile):
    tile.orientRight()
    head = tile.matchingTiles[3]
    lines = [a[1:-1] for a in tile.data[1:-1]]
    while head:
        for i in range(0, len(head.data) - 2):
            lines[i] += head.data[i + 1][1:-1]
        head = head.matchingTiles[3]
    return lines


def stitchCol(tile):
    tile.orientDown()
    head = tile
    lines = []
    while head:
        lines += stitchRow(head)
        head = head.matchingTiles[1]
    return lines[::-1]


def hicSuntDracones(sea):
    noDragons = True
    a = 0
    rough = 0
    while noDragons:
        if a % 2:
            sea.flipH()
            sea.rotate()
        else:
            sea.flipH()
        a += 1
        if a > 16:
            print("err")
        for i in range(0, len(sea.data[0]) - 20):
            iter = [a for a in re.finditer(r"^(..................#.).*\n^(#....##....##....###).*\n^(.#..#..#..#..#..#...).*",
                                           "\n".join([a[i:] for a in sea.data]), flags=re.MULTILINE)]
            if len(iter):
                for dragon in iter:
                    rough += 15
                noDragons = False
    return "".join(sea.data).count("#") - rough


def main():
    with open("input1.txt", "r") as f:
        lines = f.read()
    tiles = lines.split("\n\n")
    for tile in tiles:
        tile = tile.split("\n")
        TileG.append(Tile(tile[1:], tile[0]))
    for tile in TileG:
        tile.linkMatching()
    c = 1
    topLeft = None
    for tile in TileG:
        if tile.matchingTiles.count(None) == 2:
            if tile.matchingTiles[0] is None and tile.matchingTiles[2] is None:
                topLeft = tile
            c *= int(tile.id[5:9])
    print(f"Part1: {c}")
    full = Tile(stitchCol(topLeft), 0)
    full.getBorders()
    print("\n".join(full.data))
    print(f"Part2: {hicSuntDracones(full)}")


if __name__ == "__main__":
    main()
