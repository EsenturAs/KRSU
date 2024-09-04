from math import sqrt
r, x, y = map(int, input().split())
rs = r/10

rtk = x**2 + y**2

if rtk <= rs**2:
    print(10)
elif rtk > r**2:
    print(0)
elif rtk == r**2:
    print(1)
else:
    k = 2
    while k < 11:
        if rtk <= (rs * k)**2:
            print(11 - k)
            break
        else:
            k += 1