n, a = map(int, input().split())
nums = [int(a) for a in input().split()]
ans = []

for i in nums:
    ans.append(i % a)

print(sum(ans))
print("YES" if sum(ans) > a else "NO")