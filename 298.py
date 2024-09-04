# Переводы чисел между системами счисления
def from10to2_9(n, k):
    ans = []
    while True:
        ans.append(str(n % k))
        n = n // k
        if n == 0:
            break
    ans = int("".join(ans[::-1]))
    return ans


def from2_9to10(n, k):
    ans = 0
    #l = 0
    #while True:
    for l in range(len(str(n))):
        ans += int(n[l]) * k**(len(str(n)) - l - 1)
        #l += 1
        #if l == len(str(n)):
            #break
    return ans


def from10to11_16(n, k):
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    ans = []
    while True:
        ans.append(nums[n % k - 1])
        n = n // k
        if n == 0:
            break
    ans = "".join(ans[::-1])
    return ans

def from11_16to10(n, k):
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    ans = 0
    #l = 0
    #while True:
    for l in range(len(str(n))):
        ans += (nums.index(n[l]) + 1) * k**(len(str(n)) - l - 1)
        print(nums.index(n[l]) + 1, k**(len(str(n)) - l - 1), len(str(n)), l)
        #l += 1
        #if l == len(str(n)):
        #    break
    return ans

k = int(input())
n = input()

print()

# if k >= 2 and k <= 9:
#     a = from2_9to10(n, k)
#     a += 1
#     a = from10to2_9(a, k)
#     print(a)

# elif k >= 9 and k <= 16:
#     a = from11_16to10(n, k)
#     a += 1
#     a = from11_16to10(a, k)
#     print(a)


# Где-то ошибки в from10to11_16 и from10to2_9. Позже исправить.
# Есть версия с while, и есть версия с for. Выбрал с for.