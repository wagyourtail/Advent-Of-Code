import math

class Part1:
    def __init__(self):
        # east = 0, north = -90, south = 90, west = 180
        self.facing = 0
        # +x = east, -x = west
        self.x = 0
        # +y = south, -y = north
        self.y = 0

    def go(self, direction, dist):
        self.x += math.cos(math.radians(direction)) * dist
        self.y += math.sin(math.radians(direction)) * dist

    def N(self, dist):
        self.go(-90, dist)

    def S(self, dist):
        self.go(90, dist)

    def E(self, dist):
        self.go(0, dist)

    def W(self, dist):
        self.go(180, dist)

    def F(self, dist):
        self.go(self.facing, dist)

    def L(self, deg):
        self.facing -= deg

    def R(self, deg):
        self.facing += deg


def rect2pol(x, y):
    return math.sqrt(x ** 2 + y ** 2), math.atan2(y, x)


def pol2rect(r, theta):
    return r * math.cos(theta), r * math.sin(theta)


class Part2:
    def __init__(self):
        self.x = 10
        self.y = 1
        self.shipx = 0
        self.shipy = 0

    def N(self, dist):
        self.y += dist

    def S(self, dist):
        self.y -= dist

    def E(self, dist):
        self.x += dist

    def W(self, dist):
        self.x -= dist

    def L(self, deg):
        r, theta = rect2pol(self.x, self.y)
        theta += math.radians(deg)
        self.x, self.y = pol2rect(r, theta)

    def R(self, deg):
        r, theta = rect2pol(self.x, self.y)
        theta -= math.radians(deg)
        self.x, self.y = pol2rect(r, theta)

    def F(self, dist):
        self.shipx += self.x * dist
        self.shipy += self.y * dist


def main():
    ship = Part1()
    ship2 = Part2()
    with open("input1.txt", "r") as f:
        for line in f:
            getattr(ship, line[0])(int(line[1:]))
            getattr(ship2, line[0])(int(line[1:]))
    print(f"Part1: {round(abs(ship.x) + abs(ship.y))}")
    print(f"Part2: {round(abs(ship2.shipx) + abs(ship2.shipy))}")


if __name__ == "__main__":
    main()
