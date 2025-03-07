from collections import deque

graph = {}
N, M, V = map(int, input().split())

# 그래프 초기화
for _ in range(M):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    graph[node].sort()


for i in range(1, N + 1):
    if i not in graph:
        graph[i] = []


visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

def dfs(node):
    print(node, end=' ')
    visited_dfs[node] = True
    for next_node in graph[node]:
        if not visited_dfs[next_node]:
            dfs(next_node)


def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for next_node in graph[node]:
            if not visited_bfs[next_node]:
                visited_bfs[next_node] = True
                queue.append(next_node)


dfs(V)
print()


bfs(V)
