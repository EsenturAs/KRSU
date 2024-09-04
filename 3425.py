a, b = map(int, input().split())
c, d = map(int, input().split())
if a == c:
    print(b, a, c, d)
elif a == d:
    print(b, a, d, c)
elif b == c:
    print(a, b, c ,d)
elif b == d:
    print(a, b, d, c)
else:
    print(-1)