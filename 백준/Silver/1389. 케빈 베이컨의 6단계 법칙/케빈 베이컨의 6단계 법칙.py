import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start):
    num = [0] * (n + 1)
    visited = [0] * (n + 1)
    q = deque([start])
    visited[start] = 1

    while q:
        a = q.popleft()
        for i in graph[a]:
            if not visited[i]:
                num[i] = num[a] + 1
                q.append(i)
                visited[i] = 1

    return sum(num)

result = [bfs(graph, i) for i in range(1, n + 1)]
print(result.index(min(result)) + 1)
