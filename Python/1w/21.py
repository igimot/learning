height = int(input())
dayUp = int(input())
nightDown = int(input())
a = height - dayUp
b = dayUp - nightDown
c = a / b + 1
print(int(c))
