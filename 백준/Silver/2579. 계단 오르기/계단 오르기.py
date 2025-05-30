n = int(input())
score = [0]  # 1번 계단을 인덱스 1로 만들기 위해 0 추가
for _ in range(n):
    score.append(int(input()))

if n == 1:
    print(score[1])
elif n == 2:
    print(score[1] + score[2])
else:
    dp = [0] * (n + 1)
    dp[1] = score[1]
    dp[2] = score[1] + score[2]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + score[i - 1]) + score[i]
    print(dp[n])
