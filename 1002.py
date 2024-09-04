k = int(input())

if k <= 50:
    onePart = k / 3
    width = k
    lenght = onePart * 5
    ans = width * lenght
    if int(ans) == ans:
        print(int(ans))
    else:
        k = 0
        if int(str(ans)[-1]) == 3:
            k = 1
        elif int(str(ans)[-1]) == 6:
            k = 2
        print(int(ans), k, 3)

else:
    onePart = k / 5
    lenght = k
    width = onePart * 3
    ans = width * lenght
    if int(ans) == ans:
        print(int(ans))
    else:
        k = 0
        if int(str(ans)[-1]) == 2:
            k = 1
        elif int(str(ans)[-1]) == 4:
            k = 2
        elif int(str(ans)[-1]) == 6:
            k = 3
        elif int(str(ans)[-1]) == 8:
            k = 4
        print(int(ans), k, 5)