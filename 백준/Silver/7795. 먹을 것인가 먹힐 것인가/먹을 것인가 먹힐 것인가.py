import sys
from bisect import bisect_left

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B.sort()     
    ans = 0

    for a in A:
        ans += bisect_left(B, a)

    print(ans)
