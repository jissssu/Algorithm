import sys
sys.setrecursionlimit(10000)

def is_black(s, N, K, r, c):
    if s == 0:
        return 0
    size = pow(N, s-1)
    row, col = r // size, c // size
    start = (N - K) // 2
    end = start + K
    if start <= row < end and start <= col < end:
        return 1
    else:
        return is_black(s-1, N, K, r % size, c % size)

s, N, K, R1, R2, C1, C2 = map(int, sys.stdin.readline().split())

for r in range(R1, R2+1):
    line = []
    for c in range(C1, C2+1):
        line.append(str(is_black(s, N, K, r, c)))
    print("".join(line))
