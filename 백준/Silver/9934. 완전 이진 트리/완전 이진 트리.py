import sys
input = sys.stdin.readline

def build(start, end, level):
    if start > end:
        return
    mid = (start + end) // 2
    result[level].append(arr[mid])
    build(start, mid - 1, level + 1)
    build(mid + 1, end, level + 1)

K = int(input())
arr = list(map(int, input().split()))
result = [[] for _ in range(K)]

build(0, len(arr) - 1, 0)

for level in result:
    print(' '.join(map(str, level)))