n = int(input())
lines = [int(a) for a in input().split()]
a = 0
b = 0
Sorted = sorted(lines)

if Sorted[0] < Sorted[1] + Sorted[2] and Sorted[1] < Sorted [0] + Sorted[2] and Sorted[2] < Sorted[0] + Sorted[1]:
    a = Sorted[0] + Sorted[1] + Sorted[2]
    Sr = sorted(Sorted, reverse= True)
    while True:
        if Sr[0] < sum(Sr) - Sr[0]:
            b = sum(Sr)
            break
        else:
            Sr.pop(0)

print(a, b)