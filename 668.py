l, r = map(int, input().split())
ans = []
for i in range(l, r + 1):
    k = [int(a) for a in list(str(i))]
    if 0 in k:
        None
    else:
        k2 = 0
        for j in k:
            if i % j == 0:
                k2 += 1
        if k2 == len(str(i)):
            ans.append(i)
print(*ans)