n = int(input())
rank = [int(a) for a in input().split()]
maxRank = max(rank)
first = rank[0]
rank[rank.index(maxRank)] = first
rank[0] = maxRank
print(*rank)