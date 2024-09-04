from math import sqrt
a, b, c = map(int, input().split())  #   (ax + b) * x = c
d = b**2 - 4 * a * (-c)

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)

    if x2 == int(x2):
        x2 = int(x2)
    else:
        x2 = 0

    if x1 == int(x1):
        x1 = int(x1)
    else:
        x1 = 0

    if x1 >= x2:
        print(x2)
    elif x2 >= x1:
        print(x1)
    else:
        print(0)

elif d == 0:
    x = -b / (2 * a)
    if x == int(x):
        print(int(x))
    else:
        print(0)

else:
    print(0)