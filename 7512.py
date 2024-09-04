def esen(n, m, a, b):
    ans = n
    ans += n // m * a
    n -= n // m * m
    ans += n * b
    return ans
n, m, a, b = map(int, input().split())
print(esen(n,m,a,b))

# n, m, a, b = map(int, input().split())
# ans = n
# ans += n // m * a
# n -= n // m * m
# ans += n * b
# print(ans)