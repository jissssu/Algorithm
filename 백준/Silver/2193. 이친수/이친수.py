n = int(input())
dp = [[0, 0] for _ in range(n + 1)]

# 초기값: 1자리 이친수는 1만 가능
if n >= 1:
    dp[1][0] = 0  # 1자리에서 0으로 끝나는 것은 없음 (0으로 시작 불가)
    dp[1][1] = 1  

for i in range(2, n + 1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]  
    dp[i][1] = dp[i-1][0]               

result = dp[n][0] + dp[n][1]
print(result)