n = int(input())
nums = [int(a) for a in input().split()]

k = 1
while True:
    if k not in nums:
        print(k)
        break
    else:
        k += 1