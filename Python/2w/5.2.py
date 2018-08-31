poseOne1 = 3
poseOne2 = 2
poseTwo1 = 2
poseTwo2 = 1
if (poseOne1 - poseTwo1 == -1) or (poseOne1 - poseTwo1 == 0) or (poseOne1 - poseTwo1 == 1):
    x = 1
else:
    x = 0
if (poseOne1 - poseTwo2 == -1) or (poseOne1 - poseTwo2 == 0) or (poseOne1 - poseTwo2 == 1):
    y = 1
else:
    y = 0
if poseOne1 == poseTwo1 and poseOne1 == poseTwo2 and poseOne2 == poseTwo1 and poseOne2 == poseTwo2:
    x = 0
if x == y:
    print('YES')
else:
    print('NO')