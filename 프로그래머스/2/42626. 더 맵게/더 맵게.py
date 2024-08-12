import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1 and scoville[0] < k:  # 최소 두 개의 요소가 있는지 확인
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        answer += 1

    # 만약 힙에서 가장 작은 값이 K 이상이 아니면 -1을 반환
    if scoville[0] < k:
        return -1

    return answer
