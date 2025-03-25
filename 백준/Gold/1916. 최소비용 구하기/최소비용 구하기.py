import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    g[a].append((b, w))

st, ed = map(int, input().split())

dist = [INF] * (n + 1)

def dijkstra(start):
    dist[start] = 0
    q = [(0, start)]

    while q:
        w, cur = heapq.heappop(q)
        if dist[cur] < w:
            continue

        for nxt, cost in g[cur]:
            new_cost = dist[cur] + cost
            if dist[nxt] > new_cost:
                dist[nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))

dijkstra(st)
print(dist[ed])
