x1 = 1 #int(input())
y1 = 1 #int(input())
x2 = int(input())
y2 = int(input())
a = ((x1 + y1) % 2)
b = ((x2 + y2) % 2)
print(a, b)
if min(x1,y1,x2,y2) <= 0 or max(x1,y1,x2,y2) >= 9:
    print("<= 0 NO >= 9")
elif x1 <= y2 or x1 - 1 <= y2:
    print('YES vpered')
    if a == 0 and b == 0:
        print('YES black')

    else:
        print('NO white')
else:
    print('NO nazad')

    '''
    5 3
4 4     6 4
3 5     7 5
2 6     8 6
1 7 
    2 5
    4 2
    6 2
    1 1
    8 8
    4 6
    '''