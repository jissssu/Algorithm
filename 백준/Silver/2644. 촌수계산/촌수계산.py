n = int(input())
p1, p2 = map(int, input().split())  # 부모, 자식
m = int(input())

result_arr = []

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, depth):
    visited[start] = True

    if start == p2:  # 자식 정점에 도달하면
        result_arr.append(depth)

    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth+1)

dfs(p1, 0)

if len(result_arr) == 0:
    print(-1)
else:
    print(result_arr[0])  # 목표 정점에 처음 도달했을 때의 경로 깊이
