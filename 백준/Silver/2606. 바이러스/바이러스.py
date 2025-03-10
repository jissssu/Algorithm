# 컴퓨터 수 입력
n = int(input())
# 연결된 컴퓨터 쌍의 수 입력
m = int(input())

# 그래프 초기화
graph = [[] for _ in range(n+1)]

# 그래프 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 연결

# 방문 여부를 체크하는 리스트
visited = [False] * (n+1)

# DFS 함수 정의
def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

# 1번 컴퓨터에서 시작
dfs(1)

# 1번 컴퓨터를 제외하고 감염된 컴퓨터 수 계산
infected = sum(visited) - 1  # 1번 컴퓨터 자신은 제외

print(infected)