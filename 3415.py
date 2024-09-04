n = int(input())
nums = [int(a) for a in input().split()]
con = set(nums)
ans, ans1 = 0, ""
for i in con:
    if nums.count(i) > ans:
        ans, ans1 = nums.count(i), i
print(ans1)