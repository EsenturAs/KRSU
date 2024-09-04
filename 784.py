num = list(input())
nechet = 0
chet = 0
for i in range(len(num)):
    if int(num[i]) % 2 == 0:
        chet += 1
    else:
        nechet += 1

print(nechet, chet)