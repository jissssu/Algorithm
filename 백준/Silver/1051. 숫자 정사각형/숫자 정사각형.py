n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

max_len = 1  # 1x1

for i in range(n):
    for j in range(m):
        for k in range(1, min(n - i, m - j)):
            if board[i][j] == board[i + k][j] == board[i][j + k] == board[i + k][j + k]:
                max_len = max(max_len, k + 1)

print(max_len ** 2)
