

class BingoBoard:
    def __init__(self, rows):
        self.rows = rows

    def pop(self, x):
        for row in self.rows:
            if x in row:
                row[row.index(x)] = -1

        # check for win
        for row in self.rows:
            if row.count(-1) == len(row):
                return True
        for i in range(len(self.rows[0])):
            for j in range(len(self.rows)):
                if self.rows[j][i] != -1:
                    break
            else:
                return True
        return False

    def score(self, y):
        s = 0
        for row in self.rows:
            for x in row:
                if x != -1:
                    s += x
        return s * y

def part1(data):
    data = data.split('\n')
    inputs = list(map(int, data[0].split(",")))
    del data[0]
    del data[0]

    boards = []

    while len(data):
        rows = []
        for _ in range(5):
            rows.append(list(map(int, data[0].split())))
            del data[0]
        boards.append(BingoBoard(rows))
        del data[0]

    for inp in inputs:
        for board in boards:
            if board.pop(inp):
                print(board.score(inp))
                return
    print("No win")

def part2(data):
    data = data.split('\n')
    inputs = list(map(int, data[0].split(",")))
    del data[0]
    del data[0]

    boards = []

    while len(data):
        rows = []
        for _ in range(5):
            rows.append(list(map(int, data[0].split())))
            del data[0]
        boards.append(BingoBoard(rows))
        del data[0]

    for inp in inputs:
        to_remove = []
        for board in boards:
            if board.pop(inp):
                to_remove.append(board)
        for board in to_remove:
            boards.remove(board)
        if len(boards) == 0:
            print(board.score(inp))
            return



def main():
    with open('inp4.txt', 'r') as f:
        data = f.read()
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()