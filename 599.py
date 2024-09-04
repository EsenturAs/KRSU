from math import gcd
a, b = map(int, input().split())
if gcd(a, b) == 1:
    print("YES")
else:
    print("NO")