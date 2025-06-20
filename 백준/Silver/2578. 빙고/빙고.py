board = [list(map(int, input().split())) for _ in range(5)]
calls = [list(map(int, input().split())) for _ in range(5)]

# 번호 위치 저장: 숫자 -> 좌표
pos = {}
for i in range(5):
    for j in range(5):
        pos[board[i][j]] = (i, j)

# 빙고 체크 함수
def check_bingo():
    bingo = 0

    for row in board:
        if all(x == 0 for x in row):
            bingo += 1

    for c in range(5):
        if all(board[r][c] == 0 for r in range(5)):
            bingo += 1
            
    if all(board[i][i] == 0 for i in range(5)):
        bingo += 1
    if all(board[i][4 - i] == 0 for i in range(5)):
        bingo += 1

    return bingo

count = 0
for call_row in calls:
    for num in call_row:
        count += 1
        r, c = pos[num]
        board[r][c] = 0  # 해당 수 제거

        if check_bingo() >= 3:
            print(count)
            exit()
