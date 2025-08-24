H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H + X)]

# 결과를 담을 A 초기화
A = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
      
        if i >= X and j >= Y:
            A[i][j] = B[i][j] - A[i - X][j - Y]
        else:
            A[i][j] = B[i][j]

for row in A:
    print(*row)
