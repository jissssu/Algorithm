from collections import deque

n, m = map(int, input().split())  
maze = [list(map(int, input())) for _ in range(n)]

# 방향 이동 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()
        
        # 네 방향으로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
         
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1: 
                    maze[nx][ny] = maze[x][y] + 1  # 이동 거리 증가
                    queue.append((nx, ny))  # 큐에 추가

bfs(0, 0) 
print(maze[n-1][m-1]) 
