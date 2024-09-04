n = list(input())
while True:
    k = 0
    for i in n:
        k += int(i)
    if len(str(k)) == 1:
        print(k)
        break
    else:
        n = list(str(k))