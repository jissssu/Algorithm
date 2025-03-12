
import sys
from collections import deque

input = sys.stdin.readline  

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, farm, visited, M, N):
    queue = deque([(x, y)])
    visited[y][x] = True

    while queue:
        cx, cy = queue.popleft()  
        for i in range(4): 
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and farm[ny][nx] == 1:
                visited[ny][nx] = True 
                queue.append((nx, ny)) 


def count_worms(M, N, K, plants):
    farm = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]


    for x, y in plants:
        farm[y][x] = 1

    worm_count = 0  

    # 모든 위치를 돌면서 BFS 실행
    for y in range(N):
        for x in range(M):
            if farm[y][x] == 1 and not visited[y][x]:  
                bfs(x, y, farm, visited, M, N) 
                worm_count += 1  

    return worm_count


T = int(input().strip())  
for _ in range(T):
    M, N, K = map(int, input().split()) 
    plants = [tuple(map(int, input().split())) for _ in range(K)]  
    print(count_worms(M, N, K, plants)) 

