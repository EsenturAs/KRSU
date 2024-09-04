a, b = map(int, input().split())
c = a - b
al = list(str(a))
cl = list(str(c))
k = -1
l = -1
a1 = ""
c1 = ""
for i in range(len(al)):
    a1 += al[0]
for i in range(len(cl)):
    c1 += cl[0]

if a - int(a1) > 0:
    k = 0
if c - int(c1) > 0:
    l = 0


num = (len(al)- 1) * 9 + int(al[0]) + k
num2 = (len(cl) - 1) * 9 + int(cl[0]) + l

print(num - num2)
print(num, al[0])
print(num2, cl[0])
print(al, cl)