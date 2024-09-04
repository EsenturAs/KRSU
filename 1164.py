from math import ceil
n, m = map(int, input().split())
papers = []
ans = []
for i in range(n):
    papers.append([int(a) for a in input().split()])
    papers[i] = sorted(papers[i])
    ans.append(papers[i][m - ceil(m / 2)])
ans = sorted(ans)
print(ans[n - ceil(n / 2)])