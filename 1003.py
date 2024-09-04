sample = ["C", "H", "Y", "C", "H", "K", "A", "N"]
word = list(input())
ans = 0

if word[0] == word[3] and word[0] != sample[0]:
    ans += 1
    word[0], word[3] = "C", "C"

if word[1] == word[4] and word[1] != sample[4]:
    ans += 1
    word[1], word[4] = "H", "H"

k = 0
while True:
    if word[k] != sample[k]:
        word[k] = sample[k]
        ans += 1
    k += 1
    if k == 8:
        break

print(ans)