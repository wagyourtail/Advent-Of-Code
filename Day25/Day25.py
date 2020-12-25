def calcDiff(pub_a, pub_b, subj=7, d=20201227):
    x = 1
    a = 1
    while True:
        if (a := (a * subj) % d) == pub_a:
            break
        x += 1
    a_loop = x
    x = 1
    b = 1
    while True:
        if (b := (b * subj) % d) == pub_b:
            break
        x += 1
    b_loop = x
    return a_loop, b_loop


def findLoopSizes(pub_a, pub_b, subj=7, d=20201227):
    a_loop, b_loop = calcDiff(pub_a, pub_b)
    b = 1
    for _ in range(a_loop):
        b = (b * pub_b) % d
    print(f"Part1: b")


def main():
    pub_a = 11239946
    pub_b = 10464955
    # pub_a = 5764801
    # pub_b = 17807724

    findLoopSizes(pub_a, pub_b)
    # aww no part2, guess I can't whip out any fancy linear algebra after all.


if __name__ == "__main__":
    main()
