from collections import deque

m, n = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

# queue에 처음에 받은 토마토의 위치 좌표를 append 시킨다
# n과 m을 사용하는걸 헷갈리지 말아야 함!
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        # 처음 토마토 좌표 x, y에 꺼내고
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                # 익히고 1을 더해주면서 횟수를 세어주기
                # 여기서 나온 제일 큰 값이 정답이 될 것임
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
       
        if j == 0:
            print(-1)
            exit(0)
    
    res = max(res, max(i))

print(res - 1)
 
