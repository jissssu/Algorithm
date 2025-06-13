n = int(input())
t = []
p = []

for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

dp = [0] * (n + 1)

for i in range(n):
    dp[i] = max(dp[i], dp[i - 1] if i > 0 else 0)

    # 상담을 할 수 있다면
    if i + t[i] <= n:
        dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i])
        
print(max(dp))
