import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < k:
        if len(scoville) == 1: return -1

        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1


    return answer