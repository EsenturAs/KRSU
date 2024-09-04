a, b = map(int, input().split())
ans = 0
for i in range(a, b + 1):
    if list(str(i))[0] == list(str(i))[-1] and list(str(i))[1] == list(str(i))[-2]:
        ans += 1
print(ans)