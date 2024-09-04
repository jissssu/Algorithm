import heapq


n, m = map(int, input().split())

cards = list(map(int, input().split()))


heapq.heapify(cards)

# m번 합체를 수행
for _ in range(m):
    first_card = heapq.heappop(cards)
    second_card = heapq.heappop(cards)
    new_value = first_card + second_card
    
    heapq.heappush(cards, new_value)
    heapq.heappush(cards, new_value)

result = sum(cards)


print(result)
