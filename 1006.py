# n = input()

# if n[0] == n[2]:
#     print((int(n[0]) - 1) * 10 + int(n[1]))

# else:
#     while True:
#         if n[0] == n[2]:
#             print((int(n[0]) - 1) * 10 + int(n[1]))
#             break
#         else:
#             n = str(int(n) - 1)

n = int(input())
ans = 0

for i in range(100, n):
    k = list(str(i))
    if k[0] == k [2]:
        ans += 1

print(ans)