n = int(input())
ans = []
for i in range(1, int(n / 2) + 1):
    if n % i == 0:
        ans.append(i)
if sum(ans) == n:
    print("Yes")
else:
    print("No")