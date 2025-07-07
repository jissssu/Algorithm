N, K = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(K + 1)]

dp[0][0] = 1


for i in range(1, K + 1):  
    for j in range(N + 1):  
        for num in range(N + 1):
            if j >= num:  # j에서 num을 빼서 음수가 되지 않는 경우만
                dp[i][j] = (dp[i][j] + dp[i-1][j-num]) % 1000000000

print(dp[K][N])