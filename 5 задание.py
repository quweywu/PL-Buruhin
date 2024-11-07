a = int(input())
b = 2
c = int(a**(1/2))

while a % b != 0 and b < c:
    b += 1

if a % b == 0:
    print(b)
else:
    print(a)