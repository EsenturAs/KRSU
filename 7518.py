n = int(input())
nums = [int(a) for a in input().split()]
num = nums[0]

for i in range(1, n):
    num = num ** nums[i]

print(num%3)
print(num)