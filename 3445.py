n = int(input())
num = list(input())
ans = "yes"

if n - num.count("0") == 0:
    ans = "no"

elif n % 2 == 0:
    for i in range(0, 10):
        if num.count(str(i)) % 2 != 0:
            ans = "no"

else:
    k = 0
    for i in range(0, 10):
        if num.count(str(i)) % 2 != 0:
            k += 1
        if k >= 2:
            ans = "no"

print(ans)