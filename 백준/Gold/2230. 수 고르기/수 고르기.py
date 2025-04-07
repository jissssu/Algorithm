import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
A = [int(input().strip()) for _ in range(N)]
A.sort()

# 투 포인터
min_diff = float('inf')
start = 0

for end in range(N):
    while start < end and A[end] - A[start] >= M:
        min_diff = min(min_diff, A[end] - A[start])
        start += 1

print(min_diff)
