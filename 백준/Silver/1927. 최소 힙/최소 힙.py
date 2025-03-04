import heapq
import sys

input = sys.stdin.readline

def process(n, nums):
    heap = []

    for num in nums:
        if num > 0:
            heapq.heappush(heap, num)
        else:
            if heap:
                print(heapq.heappop(heap))
            else:
                print(0)

if __name__ == '__main__':
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    process(n, nums)
