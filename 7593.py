a, b = map(int, input().split())
if len(str(b)) % 2 == 0:
    n = min(int(str(b)[:len(str(b)) // 2]), int(str(b)[len(str(b)) // 2:]))
    if n == 0:
        n = max(int(str(b)[:len(str(b)) // 2]), int(str(b)[len(str(b)) // 2:])) - 1
else:
    if "".join(["9" * (len(str(b)) - 1)]) != "":
        n = int("".join(["9" * (len(str(b)) - 1)]))
    else:
        n = 0
if len(str(a)) % 2 == 0:
    m = min(int(str(a)[:len(str(a)) // 2]), int(str(a)[len(str(a)) // 2:]))
    if m == 0:
        m = max(int(str(a)[:len(str(a)) // 2]), int(str(a)[len(str(a)) // 2:])) - 1
else:
    if "".join(["9" * (len(str(a)) - 1)]) != "":
        m = int("".join(["9" * (len(str(a)) - 1)]))
    else:
        m = 0
print(n - m)