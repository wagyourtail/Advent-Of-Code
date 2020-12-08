a = """<x=-6, y=-5, z=-8>
<x=0, y=-3, z=-13>
<x=-15, y=10, z=-11>
<x=-3, y=-8, z=3>"""

# -- parse -- #
import re
mun = []
for b in a.split('\n'):
    m = re.search(r'(?<=\=)(-*\d+).+?(?<=\=)(-*\d+).+?(?<=\=)(-*\d+)',b)
    mun.append([[int(m.group(1)), 0], [int(m.group(2)), 0], [int(m.group(3)), 0]])
print(mun)
import copy
mun2 = copy.deepcopy(mun)
# -- part 1 -- #

from itertools import combinations

for iteration in range(1000):
    #velocity update
    #print("step", iteration+1)
    for [i, j] in combinations(range(len(mun)), 2):
        for k in range(3):
            if mun[i][k][0] < mun[j][k][0]:
                mun[i][k][1] += 1
                mun[j][k][1] -= 1
            elif mun[i][k][0] > mun[j][k][0]:
                mun[i][k][1] -= 1
                mun[j][k][1] += 1
    #pos update
    for i in range(len(mun)):
        for j in range(3):
            mun[i][j][0] += mun[i][j][1]
        #print(mun[i][0], mun[i][1])

tot = 0
for i in mun:
    mul = 1
    for j in i:
        su = 0
        for k in j:
            su += abs(k)
        mul *= su
    tot += mul

print(tot)

#from numba import jit, cuda 

def gpu(m2, t):
    if m2 in t:
        return True
    else:
        return False

# -- part 2 -- #
states = []
for _ in range(len(mun2)):
    states.append([[],[],[]])
iterr = 0
stop = True
while stop:
    if not iterr % 1000000:
        print(iterr)
    #velocity update
    #print("step", iteration+1)
    for [i, j] in combinations(range(len(mun)), 2):
        for k in range(3):
            if mun[i][k][0] < mun[j][k][0]:
                mun[i][k][1] += 1
                mun[j][k][1] -= 1
            elif mun[i][k][0] > mun[j][k][0]:
                mun[i][k][1] -= 1
                mun[j][k][1] += 1
    #pos update
    flag = True
    for i in range(len(mun)):
        for j in range(3):
            mun[i][j][0] += mun[i][j][1]
            if flag and mun[i][j] not in states[i][j]:
                flag = False
            states[i][j].append(mun[i][j][:])
    if flag:
        stop = False
        #print(mun[i][0], mun[i][1])
    iterr += 1
    

print(iterr)
