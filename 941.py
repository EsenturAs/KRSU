from math import gcd
a, b, c, d, e = map(int, input().split())
num1 = int(str(a) + str(b) + str(c))

chisl = num1*e + 100*d
znam = 100*e
zel = chisl//znam
chisl -= (zel * znam)
lc = gcd(chisl, znam)
chisl /= lc
znam /= lc
if znam == 1:
    znam = 0
print(int(chisl + zel + znam))