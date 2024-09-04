n = sorted(list(input()))
print(n)
ns = set(n)
print(ns)
ans = ""
for i in ns:
    k = ""
    if n.count(i) != 1:
        k = str(n.count(i))
    ans += (i + k)

print(ans)

# Isn't solved !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1