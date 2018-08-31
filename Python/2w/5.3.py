a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
a3 = a1 - b1
b3 = a2 - b2
if a3 <= 1 and a3 >= 1:
    x = 1
elif a3 == 0:
    x = 1
elif a3 + 1 == 0:
    x = 1
else:
    x = 0
if b3 <= 1 and b3 >= 1:
    y = 1
elif b3 == 0:
    y = 1
elif b3 + 1 == 0:
    y = 1
else:
    y = 0
if x == y:
    print('YES')
else:
    print('NO')
