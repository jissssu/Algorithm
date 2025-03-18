import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y, w, h, arr, visited):
    # 스택을 사용한 DFS로 인접한 섬을 모두 방문
    stack = [(x, y)]
    visited[x][y] = True
    
    while stack:
        cx, cy = stack.pop()
        
        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny))

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    
    # 섬의 개수를 셈
    island_count = 0
    
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                dfs(i, j, w, h, arr, visited)
                island_count += 1
    
    print(island_count)