from math import sqrt, ceil
a, b, s = map(int, input().split())
mb = s - (a * b)
answer = ceil(sqrt(mb))
if answer < a:
    print(answer)
else:
    print("No solution")