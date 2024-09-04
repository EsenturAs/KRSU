n = int(input())
nums = [int(a) for a in input().split()]
numsset = list(set(nums))
k = 0
while True:
    if nums.count(numsset[k]) == 1:
        print(numsset[k])
        break
    else:
        k += 1
