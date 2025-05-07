import sys
input = sys.stdin.read

dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

data = input().split()
N = int(data[0])
flower_map = []
idx = 1
for i in range(N):
    flower_map.append(list(map(int, data[idx:idx+N])))
    idx += N

visited = [[False]*N for _ in range(N)]

def is_valid(x, y):
    # 5개 모두 겹치지 않고 격자 내에 있어야 함
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return False
        if visited[nx][ny]:
            return False
    return True

def place_flower(x, y):
    cost = 0
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        visited[nx][ny] = True
        cost += flower_map[nx][ny]
    return cost

def remove_flower(x, y):
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        visited[nx][ny] = False

min_cost = float('inf')

# 가능한 좌표를 (1,1) ~ (N-2, N-2)
for i in range(1, N-1):
    for j in range(1, N-1):
        if not is_valid(i, j):
            continue
        c1 = place_flower(i, j)
        for k in range(1, N-1):
            for l in range(1, N-1):
                if not is_valid(k, l):
                    continue
                c2 = place_flower(k, l)
                for x in range(1, N-1):
                    for y in range(1, N-1):
                        if not is_valid(x, y):
                            continue
                        c3 = place_flower(x, y)
                        min_cost = min(min_cost, c1 + c2 + c3)
                        remove_flower(x, y)
                remove_flower(k, l)
        remove_flower(i, j)

print(min_cost)
