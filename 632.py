m, n = map(int, input().split())
print(int((m**5 * (m**5 + 17) / 2) % n))