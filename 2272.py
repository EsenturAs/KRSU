ip = input().split(".")
ans = 0
for i in ip:
    if int(i) <= 255:
        ans += 1
print("YES" if ans == 4 else "NO")