date = [#[5, 3, 4], [4, 3, 5], [3, 5, 4], [5, 4, 3], [4, 5, 3], [3, 4, 5], \
        #[4, 3, 4], [4, 3, 4], [3, 4, 4], [4, 4, 3], [4, 4, 3], [3, 4, 4], \
        #[6, 3, 4], [4, 3, 6], [3, 6, 4], [6, 4, 3], [4, 6, 3], [3, 4, 6], \
        #[8, 3, 4], [4, 3, 8], [3, 8, 4], [8, 4, 3], [4, 8, 3], [3, 4, 8],
        #[100, 1, 100], \
        [5, 0, 3], [0, 5, 0], [3, 2, 5]
         ]
for d in date:
    a1 = d[0]
    b1 = d[1]
    c1 = d[2]
    #print(a1, b1, c1)
    recTrea = 'rectangular'  # прямоугольного треугольник 1
    acuTrea = 'acute'  # для остроугольного треугольника 2
    obtTrea = 'obtuse'  # для тупоугольного треугольника 3
    impTrea = 'impossible'  # если треугольника с такими сторонами не существует.6 + 3
    #a=int(input())
    #b=int(input())
    #c=int(input())
    if c1 >= b1 and c1 >= a1 and b1 >= a1:
        a = a1
        b = b1
        c = c1
    elif b1 >= a1 and b1 >= c1 and a1 >= c1:
        a = c1
        b = a1
        c = b1
    elif a1 >= c1 and a1 >= b1 and c1 >= b1 :
        a = c1
        b = b1
        c = a1
    #print(a, b, c)
    #a,b,c = sorted ([ a, b, c ])
    #print(a, b, c)
    if a+b<=c:
        print('impossible')
    elif c**2 == (a**2)+(b**2):
        print('rectangular')
    elif ((a**2)+(b**2)-(c**2))/(2*a*b)>0:
        print('acute')
    else:
        print('obtuse')