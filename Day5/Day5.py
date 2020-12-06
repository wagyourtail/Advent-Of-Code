def createSeat(data):
    max = 64
    row = 0
    for i in data[:7]:
        if i == "B":
            row += max
        max >>= 1
    max = 4
    col = 0
    for i in data[7:10]:
        if i == "R":
            col += max
        max >>= 1
    return {"seat": data, "row": row, "col": col, "id": row * 8 + col}


def part2(seats, p1):
    seatMap = {}
    for seat in seats:
        seatMap[seat["id"]] = seat
    for key in range(0, p1 + 1):
        if key - 1 in seatMap and key + 1 in seatMap and key not in seatMap:
            return key

def main():
    seats = []
    # load lines
    with open('input1.txt', 'r') as f:
        for line in f:
            seats.append(createSeat(line))
    p1 = max(map(lambda x: x["id"], seats))
    print(f"part1: {p1}")
    print(f"part2: {part2(seats, p1)}")


if __name__ == "__main__":
    main()
