a = """..#..###....#####....###........#
.##.##...#.#.......#......##....#
#..#..##.#..###...##....#......##
..####...#..##...####.#.......#.#
...#.#.....##...#.####.#.###.#..#
#..#..##.#.#.####.#.###.#.##.....
#.##...##.....##.#......#.....##.
.#..##.##.#..#....#...#...#...##.
.#..#.....###.#..##.###.##.......
.##...#..#####.#.#......####.....
..##.#.#.#.###..#...#.#..##.#....
.....#....#....##.####....#......
.#..##.#.........#..#......###..#
#.##....#.#..#.#....#.###...#....
.##...##..#.#.#...###..#.#.#..###
.#..##..##...##...#.#.#...#..#.#.
.#..#..##.##...###.##.#......#...
...#.....###.....#....#..#....#..
.#...###..#......#.##.#...#.####.
....#.##...##.#...#........#.#...
..#.##....#..#.......##.##.....#.
.#.#....###.#.#.#.#.#............
#....####.##....#..###.##.#.#..#.
......##....#.#.#...#...#..#.....
...#.#..####.##.#.........###..##
.......#....#.##.......#.#.###...
...#..#.#.........#...###......#.
.#.##.#.#.#.#........#.#.##..#...
.......#.##.#...........#..#.#...
.####....##..#..##.#.##.##..##...
.#.#..###.#..#...#....#.###.#..#.
............#...#...#.......#.#..
.........###.#.....#..##..#.##..."""

import turtle, math
tt = turtle.Turtle()
tt.speed(0)
tt.penup()
def draw(tt, y, x, color):
    y = -y
    tt.color(color)
    tt.goto(x*20-250,y*20+250)
    tt.pd()
    tt.forward(9)
    tt.left(90)
    tt.forward(9)
    tt.left(90)
    tt.forward(9)
    tt.left(90)
    tt.forward(9)
    tt.left(90)
    tt.penup()

# -- formatting -- #
row = 0
col = 0
mat = []

for i in a:
    if i == "#":
        mat.append([row,col])
    col += 1
    if i == "\n":
        row += 1
        col = 0


for r in mat:
    draw(tt, r[0], r[1], "black")
        
# -- part 1 -- #

# original solution to part 1 was a gcd solution.



ma = []
for station in mat:

    rad = [] # t, r
    for a in mat:
        theta = math.atan2(-a[1] + station[1], -a[0] + station[0]) * 180 / math.pi
        if theta > 0:
            theta = -180 - theta
        if theta < 270:
            theta = -(-theta-270)
        if theta < 90:
            theta = -theta
        rad.append([theta, (a[0] - station[0]) ** 2 + (a[1] - station[1]) ** 2])
        if rad[-1][1] == 0:
            rad[-1][1] = 20000
    #draw(tt,station[0], station[1], "green")

    mapp = {}
    
    for r in sorted(rad)[::-1]:
        if r[0] not in mapp:
            mapp[r[0]] = []
        mapp[r[0]].append(r[1])

    #print(station)
    #for r in sorted(rad):
    #    print(mat[rad.index(r)])
    count = 0
    for r in mapp:
        count += 1
        mapp[r] = sorted(mapp[r])
        m = mat[rad.index([r, mapp[r][0]])]
        #tt.goto(station[1]*10,-station[0]*10)
        #tt.pd()
        #draw(tt,m[0], m[1], "black")
        #print("%s: [%s, %s], %s, %s" %(count,m[0] - station[0], m[1] - station[1], m[0] * 100 + m[1], r))
    ma.append(count)
                        
print(max(ma))

# -- part 2 -- #

station = mat[ma.index(max(ma))]

draw(tt,station[0], station[1], "green")

mapp = {}

rad = [] # t, r
for a in mat:
        theta = math.atan2(-a[1] + station[1], -a[0] + station[0]) * 180 / math.pi
        if theta > 0:
            theta = -180 - theta
        if theta < 270:
            theta = -(-theta-270)
        if theta < 90:
            theta = -theta
        rad.append([theta, (a[0] - station[0]) ** 2 + (a[1] - station[1]) ** 2])
        if rad[-1][1] == 0:
            rad[-1][1] = 20000
    
for r in sorted(rad)[::-1]:
    if r[0] not in mapp:
        mapp[r[0]] = []
    mapp[r[0]].append(r[1])

#print(station)
#for r in sorted(rad):
#    print(mat[rad.index(r)])
count = 0
for r in mapp:
    count += 1
    mapp[r] = sorted(mapp[r])
    m = mat[rad.index([r, mapp[r][0]])]
    tt.goto(station[1]*20-250,-station[0]*20+250)
    tt.pd()
    draw(tt,m[0], m[1], "red")
    # it took me multiple hours to finally realize i just messed up the x and y coordinates for the answer calculation
    # i added the turtle part to debug that...
    # finally realized it when i used the test field
    print("%s: [%s, %s] r[%s, %s], %s, %s" %(count,m[0], m[1],m[0] - station[0], m[1] - station[1], m[1] * 100 + m[0], r))
