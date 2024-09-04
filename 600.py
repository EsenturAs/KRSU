n = input().split("=")
if eval(n[0]) == eval(n[1]):
    print("YES")
else:
    print("NO")