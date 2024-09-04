k = int(input())
ans = ((3**k + 1) / 2) % 8
if str(ans)[-2:] == ".0": print(int(ans))
else: print(ans)