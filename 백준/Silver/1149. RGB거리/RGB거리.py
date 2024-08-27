N = int(input().strip())

# 비용을 저장할 리스트
cost = [list(map(int, input().split())) for _ in range(N)]

# DP 테이블 초기화
dp = [[0]*3 for _ in range(N)]

# 첫 번째 집의 초기 비용 설정
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

# DP 테이블 갱신
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

# 최종적으로 최소 비용 출력
print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))
