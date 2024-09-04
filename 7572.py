# from itertools import permutations

# string = input()

# a = permutations(string, len(string))
# comb = ["".join(i) for i in a]
# comb = sorted(list(set(comb)))

# print(comb[comb.index(string) + 1])

string = list(input())
a = string[-3]
string.pop(-3)
string.append(a)
print("".join(string))