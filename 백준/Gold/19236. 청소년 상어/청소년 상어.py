import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0

def move_fishes(board, fish_info, shark_x, shark_y):
    for num in range(1, 17):
        if num not in fish_info:
            continue
        x, y, d = fish_info[num]
        for i in range(8):
            nd = (d + i) % 8
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == shark_x and ny == shark_y):
                if board[nx][ny] != 0:
                    other = board[nx][ny]
                    fish_info[other][0], fish_info[other][1] = x, y
                else:
                    other = 0
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                fish_info[num] = [nx, ny, nd]
                break

def dfs(board, fish_info, shark_x, shark_y, shark_d, total):
    global answer
    move_fishes(board, fish_info, shark_x, shark_y)

    can_move = False
    for step in range(1, 4):
        nx = shark_x + dx[shark_d] * step
        ny = shark_y + dy[shark_d] * step
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] != 0:
            can_move = True
            new_board = copy.deepcopy(board)
            new_fish_info = copy.deepcopy(fish_info)

            target = new_board[nx][ny]
            new_board[shark_x][shark_y] = 0
            new_board[nx][ny] = -1
            dir_ = new_fish_info[target][2]
            del new_fish_info[target]

            dfs(new_board, new_fish_info, nx, ny, dir_, total + target)

    if not can_move:
        answer = max(answer, total)

# 입력 받기
board = [[0]*4 for _ in range(4)]
fish_info = {}

for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        a, b = row[j*2], row[j*2+1] - 1
        board[i][j] = a
        fish_info[a] = [i, j, b]

first = board[0][0]
shark_dir = fish_info[first][2]
board[0][0] = -1
del fish_info[first]

dfs(board, fish_info, 0, 0, shark_dir, first)
print(answer)
