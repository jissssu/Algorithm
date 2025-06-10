from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    melt = []

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == 0:
                    queue.append((nx, ny))
                elif board[nx][ny] == 1:
                    melt.append((nx, ny))
    return melt

time = 0
last_cheese = 0

while True:
    melt = bfs()
    if not melt:
        break
    last_cheese = len(melt)
    for x, y in melt:
        board[x][y] = 0
    time += 1

print(time)
print(last_cheese)
