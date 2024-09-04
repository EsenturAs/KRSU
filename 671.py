n = int(input())
nums = [int(a) for a in input().split()]
ans = 0
for i in nums:
    ans += i // 2
print(ans)