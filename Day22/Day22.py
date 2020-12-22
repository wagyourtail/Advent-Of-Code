class RecursiveCombatGame:
    def __init__(self, p1, p2, game=1):
        self.p1_history = []
        self.p2_history = []
        self.game = game
        self.round = 1
        self.p1 = p1
        self.p2 = p2
        self.flag = False

    # true if p1 wins, false if p2 wins
    def play(self):
        #print(f"=== Game {self.game} ===")
        while len(self.p1) and len(self.p2):
            #self.printPreRound()
            self.round += 1
            if self.p1 in self.p1_history or self.p2 in self.p2_history:
                self.flag = True
                return True
            self.tick()
        return len(self.p1) > 0

    def printPreRound(self):
        print(f"-- Round {self.round} (Game {self.game}) --")
        print(f"Player 1's deck: {self.p1}")
        print(f"Player 2's deck: {self.p2}")

    def getWinner(self):
        return self.p1 if len(self.p1) or self.flag else self.p2

    def tick(self):
        self.p1_history.append(self.p1[:])
        self.p2_history.append(self.p2[:])
        p1_card = self.p1.pop(0)
        p2_card = self.p2.pop(0)
        if p1_card <= len(self.p1) and p2_card <= len(self.p2):
            if RecursiveCombatGame(self.p1[:p1_card], self.p2[:p2_card], self.game+1).play():
                self.p1 += [p1_card, p2_card]
            else:
                self.p2 += [p2_card, p1_card]
        else:
            if p1_card > p2_card:
                self.p1 += [p1_card, p2_card]
            else:
                self.p2 += [p2_card, p1_card]


def part1(p1, p2):
    while len(p1) and len(p2):
        a = p1.pop(0)
        b = p2.pop(0)
        if a > b:
            p1 += [a, b]
        else:
            p2 += [b, a]
    return calcScore(p1 if len(p1) else p2)

def calcScore(winner):
    winner = winner[::-1]
    score = 0
    for i in range(len(winner)):
        score += winner[i] * (i + 1)
    return score

def main():
    with open("input1.txt", "r") as f:
        a = f.read().split("\n\n")
        p1 = [int(b) for b in a[0].split("\n")[1:]]
        p2 = [int(b) for b in a[1].split("\n")[1:]]
    print(f"Part1: {part1(p1[:], p2[:])}")
    p2 = RecursiveCombatGame(p1,p2)
    p2.play()
    print(f"Part2: {calcScore(p2.getWinner())}")


if __name__ == "__main__":
    main()
