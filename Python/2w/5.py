poseOne1 = int(input())
poseOne2 = int(input())
poseTwo1 = int(input())
poseTwo2 = int(input())
''' если первое число меньше вторых '''
if poseOne1 > poseTwo1 or poseOne2 > poseTwo2:
    ''' проверяем если разница более 1 тогда НЕТ '''
    #if (poseOne1 - poseTwo2 == 1 or poseOne2 - poseTwo1 == 1) or ( poseTwo2 - poseOne1== 1 or poseTwo1 - poseOne2 == 1):
    if poseOne1 - 1 == poseTwo1 or poseOne1 - 1 == poseTwo2:
        if poseOne2 - 1 == poseTwo1 or poseOne2 - 1 == poseTwo2:
            print("YES1")
    else:
        print("NO1")


elif poseOne1 - 1 == poseTwo1 and poseOne1 + 1 == poseTwo2:
    print('1')
    if poseOne1 - 1 == poseTwo1 or poseOne1 - 1 == poseTwo2:
        print('2')
        if poseOne2 + 1 == poseTwo1 or poseOne2 + 1 == poseTwo2:
            print("YES2")
    elif poseOne1 + 1 == poseTwo1 or poseOne1 + 1 == poseTwo2:
        print('3')
        if poseTwo1 -
            if poseOne2 + 1 == poseTwo1 or poseOne2 + 1 == poseTwo2:
                print("YES3")
            else:
                print('NO4')
    else:
        print("NO3")
else:
    print("NO")
