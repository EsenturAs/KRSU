from string import*
s = input()
alphabet = list(input())
alph = list(ascii_lowercase)
try:
    good = alph[alphabet.index("1")]
except(ValueError):
    good = ""
k = int(input())

variants = []
for i in range(len(s)):
    for j in range(len(s)):
        variants.append(s[i:j+1])

variants = list(set(variants))
variants.remove("")

ans = 0
for i in variants:
    a = list(i)
    if len(a) - a.count(good) <= k:
        ans += 1

print(ans)