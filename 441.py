n = int(input())
nums = []
for i in range(n, 0, -1):
    if n % i == 0:
        nums.append(i)

print(sum(nums))