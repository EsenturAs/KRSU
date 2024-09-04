xl1, xr1, yl1, yr1, xl2, xr2, yl2, yr2 = map(int, input().split())
x1 = xl2
y1 = yl1
x2 = xr1
y2 = yr2
a = x2 - x1
b = y2 - y1
s1 = a * b
a = xr1 - xl1
b = yr1 - yl1
s2 = a * b
ans = s2 - s1
print(s1)