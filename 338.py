n = list(input())
j = len(n)
while j != 0:
    if n[0] == "0":
        n.pop(0)
        j -= 1
    else:
        break
n = "".join(n)

if len(n) % 2 == 0:
    a = list(n[:int(len(n) / 2)])
    b = list(n[int(len(n) / 2):])
    k , l = 0, 0
    for i in a:
        k += int(i)
    for i in b:
        l += int(i)
    if k == l:
        print("lucky")
    else:
        print("unlucky")

else:
    print("unlucky")