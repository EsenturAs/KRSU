# nums = ["BIR","EKI","UECH","TORT","BESH","ALTY","JETI","SEGIZ","TOGUZ","ON"]
# num, word = map(str, input().split())
# num = int(num)
# word = list(word)
# answer = []

# if num == 1:
#     for i in range(len(word)):
#         k = []
#         k.extend(word)
#         k.pop(i)
#         k = "".join(k)
#         if k in nums:
#             answer.append(nums.index(k) + 1)

# if num == 2:
#     for i in range(len(word) - 1):
#         for j in range(i, len(word) - 1):
#             k = []
#             k.extend(word)
#             k.pop(i)
#             k.pop(j)
#             k = "".join(k)
#             if k in nums:
#                 answer.append(nums.index(k) + 1)

# if num == 3:
#     for i in range(len(word) - 2):
#         for j in range(i, len(word) - 2):
#             for l in range(j, len(word) - 2):
#                 k = []
#                 k.extend(word)
#                 k.pop(i)
#                 k.pop(j)
#                 k.pop(l)
#                 k = "".join(k)
#                 if k in nums:
#                     answer.append(nums.index(k) + 1)

# try:
#     print(max(answer))
# except(ValueError):
#     print(0)

from itertools import combinations
nums = ["BIR","EKI","UECH","TORT","BESH","ALTY","JETI","SEGIZ","TOGUZ","ON"]
num, word = map(str, input().split())
num = int(num)
word = list(word)
ans = 0

a = combinations(word, len(word) - num)
combOfWord = ["".join(i) for i in a]

for i in nums:
    if i in combOfWord:
        ans = i

print(nums.index(ans) + 1 if ans != 0 else ans)
print(combOfWord)