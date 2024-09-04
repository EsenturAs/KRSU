n = int(input())
s = n // 100000000
m = s // 60
h = m // 60
d = h // 24
s -= m * 60
m -= h * 60
h -= d * 24
print(d,h,m,s)