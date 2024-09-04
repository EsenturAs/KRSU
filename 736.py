n = (list(input()))
k = int(input())
ans = sorted(n, reverse= True)
print("".join(ans[:-k]))