import heapq
import sys

input = sys.stdin.readline

n = int(input().strip())
heap = []

for _ in range(n):
    num = int(input().strip())
    if num > 0:
        heapq.heappush(heap, num)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
