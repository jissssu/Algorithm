from collections import deque

def solution(n, m, board):
    visited = [[False] * n for _ in range(m)]
    
    # 4방향 이동 (상하좌우)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    white_power = 0
    blue_power = 0
    
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                # 새로운 그룹 발견
                color = board[i][j]
                queue = deque([(i, j)])
                visited[i][j] = True
                count = 1
                
                # BFS로 연결된 같은 색상 병사 찾기
                while queue:
                    x, y = queue.popleft()
                    
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == color:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            count += 1
                
                # 위력 계산 및 추가
                power = count ** 2
                if color == 'W':
                    white_power += power
                else:  # color == 'B'
                    blue_power += power
    
    return white_power, blue_power

# 입력 처리
n, m = map(int, input().split())
board = []
for _ in range(m):
    board.append(input())

# 결과 출력
white_power, blue_power = solution(n, m, board)
print(white_power, blue_power)