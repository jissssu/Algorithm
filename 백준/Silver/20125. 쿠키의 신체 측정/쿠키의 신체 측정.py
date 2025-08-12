N = int(input().strip())
board = [list(input().strip()) for _ in range(N)]

# 1. 심장 찾기
heart_x = heart_y = None
for i in range(N):
    for j in range(N):
        if board[i][j] == '*':
            heart_x, heart_y = i + 1, j + 1  # 1-based
            break
    if heart_x:
        break

heart_x += 1

# 2. 왼팔 길이
left_arm = 0
for y in range(heart_y - 2, -1, -1):  # 심장 왼쪽 방향
    if board[heart_x - 1][y] == '*':
        left_arm += 1
    else:
        break

# 3. 오른팔 길이
right_arm = 0
for y in range(heart_y, N):
    if board[heart_x - 1][y] == '*':
        right_arm += 1
    else:
        break

# 4. 허리 길이
waist = 0
lx = heart_x  # 허리 시작 행
while lx < N and board[lx][heart_y - 1] == '*':
    waist += 1
    lx += 1

# 5. 왼다리 길이
left_leg = 0
x = lx
y = heart_y - 2
while x < N and y >= 0 and board[x][y] == '*':
    left_leg += 1
    x += 1


right_leg = 0
x = lx
y = heart_y
while x < N and y < N and board[x][y] == '*':
    right_leg += 1
    x += 1


print(heart_x, heart_y)
print(left_arm, right_arm, waist, left_leg, right_leg)
