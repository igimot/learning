lineWord = 'Na lugu pasetsya'
c = int(input())
wd1 = 'korov'
wd2 = 'korova'
wd3 = 'korovy'
x = c % 10
if c == 0 or (c >= 5 and c <= 20) or (x == 0 or (x >= 5 and x <= 9)):
    print(c, wd1)
elif c == 1 or x == 1:
    print(c, wd2)
else:
    print(c, wd3)
