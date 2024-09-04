code = list(input())
ans = []
for i in code:
    if i == "0":
        ans.append("1")
    elif i == "1":
        ans.append("0")

if ans.count("0") == len(ans):
    print("0")
else:
    while True:
        if ans[0] == "0":
            ans.pop(0)
        else:
            print("".join(ans))
            break