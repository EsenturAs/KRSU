a, b, c = map(int, input().split())
if a > b and a > c and a <= b + c:
    print("YES")
elif b > a and b > c and b <= a + c:
    print("YES")
elif c > b and c > a and c <= a + b:
    print("YES")
else:
    print("NO")