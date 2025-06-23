from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0

shark_size = 2
eat_count = 0
time = 0

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, size):
    visited = [[-1]*N for _ in range(N)]
    visited[x][y] = 0
    q = deque()
    q.append((x, y))

    fish_list = []
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                # 상어가 지나갈 수 있는 칸
                if graph[nx][ny] <= size:
                    visited[nx][ny] = visited[cx][cy] + 1
                    q.append((nx, ny))
                    # 먹을 수 있는 물고기라면 후보에 추가
                    if 0 < graph[nx][ny] < size:
                        fish_list.append((visited[nx][ny], nx, ny))
    return sorted(fish_list)

while True:
    fishes = bfs(shark_x, shark_y, shark_size)
    if not fishes:
        break
    dist, fx, fy = fishes[0]
    time += dist
    shark_x, shark_y = fx, fy
    graph[fx][fy] = 0
    eat_count += 1
    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

print(time)
