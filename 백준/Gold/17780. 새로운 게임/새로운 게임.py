N, K = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(N)]
pieces = [list(map(int, input().split())) for _ in range(K)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


board_map = [[[] for _ in range(N)] for _ in range(N)]
for i in range(K):
    x, y, d = pieces[i]
    pieces[i] = [x-1, y-1, d-1]  # 0-index로 변환
    board_map[x-1][y-1].append(i)

def reverse(d):
    if d == 0: return 1
    elif d == 1: return 0
    elif d == 2: return 3
    elif d == 3: return 2

def move_piece(i):
    x, y, d = pieces[i]
    idx = board_map[x][y].index(i)
    move_stack = board_map[x][y][idx:]
    board_map[x][y] = board_map[x][y][:idx]

    nx = x + dx[d]
    ny = y + dy[d]

    # 이동 불가 (범위 밖 or 파란색)
    if not (0 <= nx < N and 0 <= ny < N) or chess[nx][ny] == 2:
        d = reverse(d)
        pieces[i][2] = d  
        nx = x + dx[d]
        ny = y + dy[d]

        if not (0 <= nx < N and 0 <= ny < N) or chess[nx][ny] == 2:
            board_map[x][y].extend(move_stack)  # 되돌려놓음
            return False

    # 빨간색이면 뒤집기
    if chess[nx][ny] == 1:
        move_stack.reverse()

    for p in move_stack:
        pieces[p][0], pieces[p][1] = nx, ny

    board_map[nx][ny].extend(move_stack)

    if len(board_map[nx][ny]) >= 4:
        return True
    return False

# 게임 시작
for turn in range(1, 1001):
    for i in range(K):
        x, y, d = pieces[i]
        if board_map[x][y][0] != i:
            continue  # 가장 아래 말이 아닐 경우 skip
        if move_piece(i):
            print(turn)
            exit()

print(-1)
