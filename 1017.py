m, n = map(int, input().split())
q = [int(a) for a in input().split()]
num1 = []
num2 = []
ans = []
for i in range(n):
    k, l = map(int, input().split())
    num1.append(k - 1)
    num2.append(l)

for i in range(n):
    k = 0
    for j in range(num1[i], num2[i], 2):
        k += q[j]
    ans.append(k)

print(min(ans))