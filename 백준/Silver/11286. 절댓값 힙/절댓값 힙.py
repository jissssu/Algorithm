import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
heap = []

for _ in range(n):
    x = int(input().strip())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))  # (절댓값, 원래값) 형태로 저장
    else:
        if heap:
            print(heapq.heappop(heap)[1])  # 원래값 출력
        else:
            print(0)
