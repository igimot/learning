poseOne1 = 4
poseOne2 = 4
b1 = 3
poseTwo2 = 5
z1 = 0
z2 = 0
if poseOne1 > b1:
    print('>')
    if poseOne1 - b1 ==1:
        print('yes1')
        x1 = 1
    else:
        print('NO1')
elif poseOne1 < b1:
    print('<')
    if b1 - poseOne1 == 1:
        print("yes")
    else:
        print('NO')
elif poseOne1 == b1:
    print('=')
if poseOne1 > b1:
    print('>')
    if poseOne1 - b1 ==1:
        print('yes1')
        z1 = 1
    else:
        print('NO1')
elif poseOne1 < b1:
    print('<')
    if b1 - poseOne1 == 1:
        print("yes")
    else:
        print('NO')
elif poseOne1 == b1:
    print('=')

if poseOne1 > poseTwo2:
    print('>')
    if p2 ==1:
        print('yes1')
        z2 = 1
    else:
        print('NO1')
elif poseOne1 < poseTwo2:
    print('<')
    if poseTwo2 - poseOne1 == 1:
        print("yes")
    else:
        print('NO')
elif poseOne1 == poseTwo2:
    print('=')
print(x1, x2, y1, y2)
print(z1, z2)
