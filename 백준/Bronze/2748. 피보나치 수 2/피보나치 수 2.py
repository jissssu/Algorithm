n = int(input())

dp = [0] * 91
dp[0], dp[1] = 0, 1

for i in range(2, n + 1):
    if not dp[i]:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n])