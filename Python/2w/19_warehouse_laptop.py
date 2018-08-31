nSizeA = int(input())
nSizeB = int(input())
nSizeC = int(input())
wSizeX = int(input())
wSizeY = int(input())
wSizeZ = int(input())
d1 = (nSizeA // wSizeX) * (nSizeB // wSizeY) * (nSizeC // wSizeZ)
d2 = (nSizeA // wSizeX) * (nSizeC // wSizeY) * (nSizeB // wSizeZ)
d3 = (nSizeB // wSizeX) * (nSizeC // wSizeY) * (nSizeA // wSizeZ)
d4 = (nSizeB // wSizeX) * (nSizeA // wSizeY) * (nSizeC // wSizeZ)
d5 = (nSizeC // wSizeX) * (nSizeA // wSizeY) * (nSizeB // wSizeZ)
d6 = (nSizeC // wSizeX) * (nSizeB // wSizeY) * (nSizeA // wSizeZ)
if d1 >= d2:
    d2 = d1
if d3 >= d4:
    d4 = d2
if d5 >= d6:
    d6 = d5
if d2 >= d4 and d2 >= d6:
    print(d2)
elif d4 >= d6:
    print(d4)
else:
    print(d6)
