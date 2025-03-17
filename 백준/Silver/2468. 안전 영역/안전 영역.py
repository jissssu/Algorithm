import sys
from collections import deque
input = sys.stdin.read

# BFS로 안전한 영역 탐색
def bfs(x, y, height, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(x, y)])
    visited[x][y] = True  # 방문 처리

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 배열 범위 내이고, 방문하지 않았으며, 물에 잠기지 않는 지점이면 탐색
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] > height:
                visited[nx][ny] = True
                queue.append((nx, ny))

# 입력 처리 (sys.stdin.read 사용)
data = sys.stdin.read().splitlines()
N = int(data[0])

graph = []
max_height = 0  # 가장 높은 지점 저장

for i in range(1, N + 1):
    row = list(map(int, data[i].split()))
    graph.append(row)
    max_height = max(max_height, max(row))  # 최대 높이 업데이트

# 최대 안전 영역 개수 저장
max_safe_areas = 1  # 기본적으로 물에 안 잠길 경우 최소 1개

# 1부터 max_height - 1까지 물 높이를 변경하면서 탐색
for height in range(1, max_height):
    visited = [[False] * N for _ in range(N)]
    safe_areas = 0  # 현재 높이에서의 안전 영역 개수

    for i in range(N):
        for j in range(N):
            # 방문하지 않았고, 물에 잠기지 않는 지점이면 BFS 실행
            if not visited[i][j] and graph[i][j] > height:
                bfs(i, j, height, visited)  # BFS 사용
                safe_areas += 1  # 새로운 안전 영역 발견

    # 최대 개수 갱신
    max_safe_areas = max(max_safe_areas, safe_areas)

print(max_safe_areas)
