import sys
input = sys.stdin.readline

N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
result = float('inf')

def dfs(depth, idx):
    global result

    # 팀 인원이 1명 이상  N-1명 이하인 경우 능력치 계산
    if 1 <= depth <= N - 1:
        team_start = 0
        team_link = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    team_start += status[i][j]
                elif not visited[i] and not visited[j]:
                    team_link += status[i][j]

        result = min(result, abs(team_start - team_link))
 
        if result == 0:
            return

    if depth == N:
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

dfs(0, 0)
print(result)
