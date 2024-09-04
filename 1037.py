from math import gcd

a, b, c, d, f = map(int, input().split())
x = a ** b
y = c ** d

# def gcd(num1, num2):
#     res = num1 % num2
#     if res == 0:
#         return num2
#     else:
#         return gcd(num2, res)

ans = gcd(x,y) % f
print(ans)