def find_max_path(triangle, n):
    # DP 테이블 초기화
    dp = [[0] * (i + 1) for i in range(n)]
    
    # 첫 번째 줄 초기화
    dp[0][0] = triangle[0][0]
    
    # DP를 이용하여 최대 경로 합 계산
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                # 왼쪽 끝
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                # 오른쪽 끝
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                # 가운데
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
 
    return max(dp[-1])

# 입력 받기
n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

# 최대 경로 합 계산
result = find_max_path(triangle, n)
print(result)
