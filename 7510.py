n = int(input())
words = input().split(";")
words.remove("")
ans = ""
for i in words:
    ans += (i[::-1] + ";")
print(ans)