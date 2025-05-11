from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[False] * m for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start = (0, 0)

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(m):
        if row[j] == 2:
            start = (i, j)

queue = deque()
sx, sy = start
queue.append((sx, sy))
visited[sx][sy] = True
dist[sx][sy] = 0

while queue:
    x, y = queue.popleft()
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

for i in range(n):
    row = []
    for j in range(m):
        if graph[i][j] == 0:
            row.append(0)
        elif dist[i][j] == -1:
            row.append(-1)
        else:
            row.append(dist[i][j])
    print(*row)
