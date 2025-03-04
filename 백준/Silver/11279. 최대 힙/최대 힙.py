import heapq
import sys

input = sys.stdin.readline

n = int(input().strip())
heap = []

for _ in range(n):
    num = int(input().strip())
    if num > 0:
        heapq.heappush(heap, -num)  # 최대 힙을 만들기 위해 음수로 저장
    else:
        if heap:
            print(-heapq.heappop(heap))  # 꺼낼 때 다시 양수로 변환
        else:
            print(0)
