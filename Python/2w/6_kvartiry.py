k1 = int(input())
k2 = int(input())
if k2 % (k2 - k1 + 1) == 0:
    print('YES')
else:
    print('NO')
