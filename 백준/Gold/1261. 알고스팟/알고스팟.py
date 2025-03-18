import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

dist = [[-1] * m for _ in range(n)]
dist[0][0] = 0 

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# deque을 사용한 0-1 BFS
que = deque()
que.append((0, 0))  

while que:
    x, y = que.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        if dist[nx][ny] == -1:
            if arr[nx][ny] == 1:  # 벽인 경우
                dist[nx][ny] = dist[x][y] + 1  # 벽을 부수고 가는 비용 1 증가
                que.append((nx, ny))  
            else:  
                dist[nx][ny] = dist[x][y]  
                que.appendleft((nx, ny))  # 벽을 부수지 않은 경로를 우선 처리하므로 앞에 추가

# (n-1, m-1)까지 가는 최소 벽 부수기 횟수 출력
print(dist[n-1][m-1])
