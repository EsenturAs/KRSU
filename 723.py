a, b = map(int, input().split())
ans = 0
while a != b:
    ans += 1
    if a < b:
        a += 3
    elif a > b:
        a -= 2
print(ans)