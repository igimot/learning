money = int(input())
cent = int(input())
amount = int(input())
c1 = (money * 100) + cent
c2 = c1 * amount
c = c2 % 100
m = c2 // 100
print(m, c)
