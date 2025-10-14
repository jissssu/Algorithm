
N, M = map(int, input().split())


S = set(input().strip() for _ in range(N))


check_words = [input().strip() for _ in range(M)]

count = sum(1 for word in check_words if word in S)

print(count)
