from collections import deque

def bfs(l, start, end):
    # 나이트가 이동할 수 있는 8가지 방향
    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    queue = deque([(start[0], start[1], 0)])  
    visited = [[False] * l for _ in range(l)]
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, depth = queue.popleft()
        
        if (x, y) == end:
            return depth
        
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, depth + 1))
    
    return -1  # 이론상 도달할 수 없는 경우는 없음

# 입력 처리
t = int(input())

results = []
for _ in range(t):
    l = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    
    result = bfs(l, start, end)
    results.append(result)

for result in results:
    print(result)
