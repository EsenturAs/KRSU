n, a = map(int, input().split())
nums = [int(a) for a in input().split()]
ans = []

for i in range(n):
    ans.append(nums[i] % a)

ans = set(ans)
print(len(ans))