a, b, c = map(int, input().split())
ans = 1

if c > 0:
    ans *= 2
elif c == 0:
    ans *= 1

if b > 0 and a > b:
    ans *= 4
elif b > 0 and a < b:
    ans *= 2
elif b == 0 and a > 0:
    ans *= 2

if c < 0:
    ans = 0
elif b < 0:
    ans = 0
elif b == 0 and c < 0:
    ans = 0

print(ans)

# Isn't solved