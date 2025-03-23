import sys

# 입력 받기
input = sys.stdin.readline
n = int(input())  # 정점 개수
graph = [list(map(int, input().split())) for _ in range(n)]  # 인접 행렬
visited = [[0] * n for _ in range(n)]  # 결과 저장용 배열

# DFS 함수 정의
def dfs(start, node):
    for next_node in range(n):
        if graph[node][next_node] == 1 and visited[start][next_node] == 0:
            visited[start][next_node] = 1  # 경로 표시
            dfs(start, next_node)  # 재귀적으로 탐색

# 각 정점에서 DFS 수행
for i in range(n):
    dfs(i, i)

# 결과 출력
for row in visited:
    print(*row)
