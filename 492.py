n = int(input())

if n < 6 or n % 2 != 0:
    print(-1)

else:
    steps = 0
    k = 0
    while True:
        if k < n:
            k += 8
            steps += 1
        elif k > n:
            k -= 2
        elif k == n:
            print(steps)
            break