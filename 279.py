m, n = map(int, input().split())
g1, s1, c1 = map(int, input().split())
g2, s2, c2 = map(int, input().split())

m1 = g1 * m * n + s1 * n + c1
m2 = g2 * m * n + s2 * n + c2

print(1 if m1 > m2 else 2 if m2 > m1 else 0)