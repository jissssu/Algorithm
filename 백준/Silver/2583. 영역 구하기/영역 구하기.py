from sys import setrecursionlimit, stdin
setrecursionlimit(10000)

# 입력 받기
m, n, k = map(int, stdin.readline().split())
arr = [[0] * n for _ in range(m)]

result_arr = []

# DFS를 사용하여 연결된 빈 공간의 넓이를 계산
def dfs(x, y):
    stack = [(x, y)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                stack.append((nx, ny))
                count += 1
    return count

# 직사각형 입력 받아서 격자에 표시
for _ in range(k):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

# 빈 공간을 찾아 DFS로 영역 넓이를 계산
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = 1
            result_arr.append(dfs(i, j))

# 결과 출력
print(len(result_arr))
print(*sorted(result_arr))
