n = int(input())
stats = {}
ans = []
for i in range(n):
    k1, k2 = map(int, input().split())
    stats[k1] = k2
stats = sorted(stats.items(), key = lambda x: x[1], reverse = True)
stats = dict(stats)
idn = list(stats.keys())
point = list(stats.values())
for i in range(n):
    print(idn[i], point[i])

# Wrong Answers. Make somehow different!