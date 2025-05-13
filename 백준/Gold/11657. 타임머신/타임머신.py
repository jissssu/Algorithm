import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

dist = [INF] * (n + 1)
dist[1] = 0 
for i in range(n - 1):
    for u, v, w in edges:
        if dist[u] != INF and dist[v] > dist[u] + w:
            dist[v] = dist[u] + w

# 음수 사이클 체크
for u, v, w in edges:
    if dist[u] != INF and dist[v] > dist[u] + w:
        print(-1)
        sys.exit()


for i in range(2, n + 1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])
