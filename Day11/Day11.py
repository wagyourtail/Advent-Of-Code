# this is kinda like game of life isn't it...

seats = {}
maxX = 0
maxY = 0

class Seat:
    def __init__(self, x, y):
        self._adjacent = None
        self._rcSeats = None
        self.x = x
        self.y = y
        self.filled = False
        self.nextFilled = False

    def adjacent(self):
        if self._adjacent is None:
            self._adjacent = []
            for x in range(self.x - 1, self.x + 2):
                for y in range(self.y - 1, self.y + 2):
                    if x == self.x and y == self.y:
                        continue
                    if (x, y) in seats:
                        self._adjacent.append(seats[(x, y)])
        return self._adjacent

    def raycast(self):
        global maxX, maxY
        if self._rcSeats is None:
            self._rcSeats = []
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    x = self.x
                    y = self.y
                    flag = True
                    while flag:
                        x += dx
                        y += dy
                        if (x, y) in seats:
                            flag = False
                            self._rcSeats.append(seats[(x, y)])
                        elif x < 0 or x >= maxX:
                            flag = False
                        elif y < 0 or y >= maxY:
                            flag = False
        return self._rcSeats

    def p1Tick(self):
        count = 0
        for seat in self.adjacent():
            if seat.filled:
                count += 1
        if self.filled and count > 3:
            self.nextFilled = False
            return True
        elif (not self.filled) and count == 0:
            self.nextFilled = True
            return True
        return False

    def p2Tick(self):
        count = 0
        for seat in self.raycast():
            if seat.filled:
                count += 1
        if self.filled and count > 4:
            self.nextFilled = False
            return True
        elif (not self.filled) and count == 0:
            self.nextFilled = True
            return True
        return False

    def postTick(self):
        self.filled = self.nextFilled


def part1():
    global seats
    flag = True
    while flag:
        flag = False
        for seat in seats.values():
            flag = seat.p1Tick() or flag
        for seat in seats.values():
            seat.postTick()
    count = 0
    for seat in seats.values():
        if seat.filled:
            count += 1
    return count

def part2():
    global seats
    #reset model
    for seat in seats.values():
        seat.filled = False
        seat.nextFilled = False
    flag = True
    while flag:
        flag = False
        for seat in seats.values():
            flag = seat.p2Tick() or flag
        for seat in seats.values():
            seat.postTick()
    count = 0
    for seat in seats.values():
        if seat.filled:
            count += 1
    return count

def main():
    global seats, maxX, maxY
    with open("input1.txt", "r") as f:
        y = 0
        for line in f:
            maxX = max(maxX, len(line))
            for x in range(0, len(line)):
                if line[x] == "L":
                    seats[(x, y)] = Seat(x, y)
            y += 1
        maxY = y
    p1 = part1()
    print(f"part1: {p1}")
    p2 = part2()
    print(f"part2: {p2}")

if __name__ == "__main__":
    main()