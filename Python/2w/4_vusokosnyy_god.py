numb1 = int(input())
if ((numb1 % 4 == 0 and numb1 % 100 != 0) or (numb1 % 400 == 0)):
    print('YES')
else:
    print('NO')
