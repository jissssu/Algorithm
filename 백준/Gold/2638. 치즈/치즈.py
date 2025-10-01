from collections import deque


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_outside_air():

    visited = [[False]*M for _ in range(N)]
    q = deque([(0, 0)])
    visited[0][0] = True
    outside = [[False]*M for _ in range(N)]
    outside[0][0] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and board[nx][ny] == 0:
                    visited[nx][ny] = True
                    outside[nx][ny] = True
                    q.append((nx, ny))
    return outside

def melt(outside):

    melted = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:  # 치즈일 때
                cnt = 0
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < N and 0 <= nj < M and outside[ni][nj]:
                        cnt += 1
                if cnt >= 2:  # 외부 공기 2변 이상 접촉
                    melted.append((i, j))

    for x, y in melted:
        board[x][y] = 0
    return len(melted) > 0

time = 0
while True:
    outside = get_outside_air()
    if not melt(outside):  
        break
    time += 1

print(time)
