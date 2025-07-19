from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 주사위 굴리기
def roll(dice, dir):
    top, bottom, left, right, front, back = dice
    if dir == 0:  
        return [left, right, bottom, top, front, back]
    elif dir == 1:  
        return [back, front, left, right, top, bottom]
    elif dir == 2:  
        return [right, left, top, bottom, front, back]
    elif dir == 3: 
        return [front, back, left, right, bottom, top]

def get_score(r, c, board, N, M):
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    value = board[r][c]
    count = 1

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dr[d], y + dc[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == value:
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1

    return value * count

# 방향 회전 규칙
def rotate_dir(curr_dir, bottom, cell):
    if bottom > cell:
        return (curr_dir + 1) % 4 
    elif bottom < cell:
        return (curr_dir + 3) % 4  
    else:
        return curr_dir

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 초기값
x, y = 0, 0
direction = 0  # 동쪽
dice = [1, 6, 4, 3, 5, 2]  # [top, bottom, left, right, front, back]
total_score = 0

for _ in range(K):
    # 다음 위치
    nx = x + dr[direction]
    ny = y + dc[direction]

    # 범위 밖이면 방향 반대로
    if not (0 <= nx < N and 0 <= ny < M):
        direction = (direction + 2) % 4
        nx = x + dr[direction]
        ny = y + dc[direction]

    # 이동 및 주사위 회전
    dice = roll(dice, direction)
    x, y = nx, ny

    score = get_score(x, y, board, N, M)
    total_score += score

    direction = rotate_dir(direction, dice[1], board[x][y])  # dice[1] == bottom


print(total_score)
