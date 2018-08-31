x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
a = ((x + y) % 2)
b = ((x1 + y1) % 2)
if a == 0 and b == 0:
    print('YES')
elif a == 1 and b == 1:
    print('YES')
else:
    print('NO')
