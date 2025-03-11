from collections import deque

def solution(n, m, board):
    visited = [[False] * n for _ in range(m)]
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    
    white_power = 0
    blue_power = 0
    
    
    def bfs(x, y, color):
        queue = deque([(x, y)])
        visited[x][y] = True
        count = 1  
        
        while queue:
            cx, cy = queue.popleft()
            
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                
               
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
        
        return count * count 
    
    # 모든 위치에 대해 BFS 수행
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                color = board[i][j]
                power = bfs(i, j, color)
                
                if color == 'W':
                    white_power += power
                else:  
                    blue_power += power
    
    return white_power, blue_power


n, m = map(int, input().split())
board = []
for _ in range(m):
    board.append(input())


white_power, blue_power = solution(n, m, board)
print(white_power, blue_power)