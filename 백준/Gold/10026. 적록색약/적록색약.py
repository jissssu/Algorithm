import sys

sys.setrecursionlimit(100000)  

N = int(sys.stdin.readline().strip())  
grid = [list(sys.stdin.readline().strip()) for _ in range(N)]  


color_blind_grid = [['R' if cell == 'G' else cell for cell in row] for row in grid]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, color, visited, board):
    visited[x][y] = True 

    for i in range(4): 
        nx, ny = x + dx[i], y + dy[i]

        # 배열 범위 내에 있고, 방문하지 않았으며 같은 색상일 경우 탐색
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == color:
            dfs(nx, ny, color, visited, board)

def count_regions(board):
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:  
                dfs(i, j, board[i][j], visited, board)
                count += 1  
    return count


normal_result = count_regions(grid)
color_blind_result = count_regions(color_blind_grid)

print(normal_result, color_blind_result)
