import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 입력 받기
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))  # 양방향 그래프

v1, v2 = map(int, input().split())

# 다익스트라 함수 (우선순위 큐 사용)
def dijkstra(start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    q = [(0, start)]  # (거리, 현재 노드)

    while q:
        cur_dist, cur_node = heapq.heappop(q)

        if dist[cur_node] < cur_dist:
            continue  # 이미 처리된 노드는 무시

        for next_node, weight in graph[cur_node]:
            new_dist = cur_dist + weight
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))

    return dist

# 1. 각 노드에서 최단 거리 계산
dist_from_1 = dijkstra(1)     # 1번 노드에서 모든 노드까지의 최단 거리
dist_from_v1 = dijkstra(v1)   # v1에서 모든 노드까지의 최단 거리
dist_from_v2 = dijkstra(v2)   # v2에서 모든 노드까지의 최단 거리

# 2. 두 가지 경로를 계산
route1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]  # 1 → v1 → v2 → N
route2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]  # 1 → v2 → v1 → N

# 3. 최소 경로 선택 (불가능한 경우 예외 처리)
result = min(route1, route2)
print(result if result < INF else -1)
