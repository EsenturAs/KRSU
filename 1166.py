from math import prod
n = int(input())
nums = input().split()
chetsum = 0
nechetproiz = 0
for i in range(n):
    k = [eval(l) for l in list(nums[i])]
    if k[-1] % 2 == 0:
        if sum(k) > chetsum:
            chetsum = sum(k)
    else:
        if prod(k) > nechetproiz:
            nechetproiz = prod(k)
print(chetsum, nechetproiz)