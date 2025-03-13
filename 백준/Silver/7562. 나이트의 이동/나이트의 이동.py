import sys
from collections import deque

input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs(n, bx, by, ax, ay):
    q = deque()
    q.append((bx, by))
    visited = [[0] * n for _ in range(n)]
    visited[bx][by] = 1

    while q:
        x, y = q.popleft()

        if x == ax and y == ay:
            return visited[x][y] - 1  # 초기값 빼고 이동횟수 반환

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return -1

t = int(input())

for _ in range(t):
    n = int(input())
    beforeX, beforeY = map(int, input().split())
    afterX, afterY = map(int, input().split())

    result = bfs(n, beforeX, beforeY, afterX, afterY)
    print(result)
