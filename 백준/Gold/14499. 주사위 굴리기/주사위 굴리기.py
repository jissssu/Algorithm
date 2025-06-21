
N, M, x, y, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위 상태
dice = [0] * 6 

def roll(d):
    top, bottom, north, south, west, east = dice
    if d == 0:  # 동
        dice[0], dice[1], dice[4], dice[5] = west, east, bottom, top
    elif d == 1:  # 서
        dice[0], dice[1], dice[4], dice[5] = east, west, top, bottom
    elif d == 2:  # 북
        dice[0], dice[1], dice[2], dice[3] = south, north, top, bottom
    elif d == 3:  # 남
        dice[0], dice[1], dice[2], dice[3] = north, south, bottom, top

for cmd in commands:
    dir = cmd - 1
    nx, ny = x + dx[dir], y + dy[dir]

    if 0 <= nx < N and 0 <= ny < M:
        roll(dir)
        if grid[nx][ny] == 0:
            grid[nx][ny] = dice[1]  
        else:
            dice[1] = grid[nx][ny] 
            grid[nx][ny] = 0

        print(dice[0]) 
        x, y = nx, ny  # 위치 갱신
