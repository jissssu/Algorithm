n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [False] * n
result = []
results = []

def dfs(depth):
    if depth == m:
        results.append(tuple(result))  # 중복 제거를 위해 튜플로 저장
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result.append(nums[i])
            dfs(depth + 1)
            result.pop()
            visited[i] = False

dfs(0)

for seq in sorted(set(results)):
    print(' '.join(map(str, seq)))
