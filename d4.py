codes = list(range(130254, 678275))

for i in range(len(codes) - 1, -1, -1):
    if sorted(str(codes[i])) != list(str(codes[i])):
        del codes[i]
        continue
    doub = False
    for j in range(len(str(codes[i]))-1):
        a = str(codes[i])[j:j+2]
        if a[0] == a[1]:
            doub = True
    if not doub:
        del codes[i]

print(len(codes))


# -- part 2 -- #

for i in range(len(codes) - 1, -1, -1):
    doub = []
    for j in range(len(str(codes[i]))-1):
        a = str(codes[i])[j:j+2]
        if a[0] == a[1]:
            doub.append(j)
    trip = []
    for j in range(len(str(codes[i]))-2):
        a = str(codes[i])[j:j+3]
        if a[0] == a[1] and a[0] == a[2]:
            if j not in trip:
                trip.append(j)
            trip.append(j + 1)
            
    if doub == trip:
        del codes[i]

print(len(codes))
