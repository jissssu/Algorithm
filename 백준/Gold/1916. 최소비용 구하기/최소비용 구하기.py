import sys
import heapq  

input = sys.stdin.readline  

n = int(input())  # 도시 개수
m = int(input())  # 버스 개수

graph = [[] for _ in range(n + 1)]  

for _ in range(m):
    start, end, cost = map(int, input().split())  
    graph[start].append([end, cost])  

start_city, end_city = map(int, input().split())  

costs = [1e9] * (n + 1)  
priority_queue = []  

costs[start_city] = 0  
heapq.heappush(priority_queue, [0, start_city])  

while priority_queue:
    current_cost, current_city = heapq.heappop(priority_queue)  

    if costs[current_city] < current_cost:
        continue  

    for next_city, move_cost in graph[current_city]:  
        total_cost = current_cost + move_cost  

        if total_cost < costs[next_city]:  
            costs[next_city] = total_cost  
            heapq.heappush(priority_queue, [total_cost, next_city])  

print(costs[end_city])  
