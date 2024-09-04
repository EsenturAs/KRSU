word = list(input())

if len(word) == 2:
    print("Impossible")

if len(word) == 3:
    if word[0] == word[1] or word[1] == word[2] or word[0] == word[2]:
        print("Possible")
    else:
        print("Impossible")

if len(word) > 3:
    ans = "Impossible"
    for i in range(len(word) - 2):
        if word[i] == word[i + 1] or word[i] == word[i + 2]:
            ans = "Possible"
    print(ans)

#Isn't solved