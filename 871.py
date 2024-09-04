from math import sqrt
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
d1 = sqrt((x2 - x1)**2 + (y2 - y1)**2)
d2 = sqrt((x3 - x4)**2 + (y3 - y4)**2)
if d1 == d2:
    print("YES")
else:
    print("NO")