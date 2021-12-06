from collections import defaultdict


class School:
    def __init__(self, timers):
        self.fish = []
        for timer in timers:
            self.add_fish(timer)

    def add_fish(self, timer):
        self.fish.append(LanternFish(self, timer))

    def tick(self):
        for fish in self.fish[:]:
            fish.tick()

class LanternFish:
    def __init__(self, school, timer):
        self.school = school
        self.timer = timer

    def tick(self):
        self.timer = self.timer - 1
        if self.timer == -1:
            self.school.add_fish(8)
            self.timer = 6

def part1(data):
    school = School(data)

    for i in range(80):
        school.tick()

    print(len(school.fish))



def part2(data):
    buckets = defaultdict(lambda: 0)
    for i in data:
        buckets[i] += 1

    for _ in range(256):
        newbuckets = defaultdict(lambda: 0)
        for i in buckets:
            if (i == 0):
                newbuckets[8] += buckets[i]
                newbuckets[6] += buckets[i]
            else:
                newbuckets[i - 1] += buckets[i]
        buckets = newbuckets

    print(sum(buckets.values()))

def part2_with_lists(data):
    fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in data:
        fish[i] += 1

    for i in range(256):
        dup = fish.pop(0)
        fish.append(dup)
        fish[6] += dup

    print(sum(fish))


def main():
    with open('inp6.txt', 'r') as f:
        data = f.read().split(",")

    data = [int(x) for x in data]

    part1(data)
    part2(data)
    part2_with_lists(data)


if __name__ == "__main__":
    main()
