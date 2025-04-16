import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(node):
    global count
    visited[node] = True
    path[node] = True  # 현재 경로에 있는 노드

    next_node = choices[node]

    if not visited[next_node]:
        dfs(next_node)
    elif path[next_node]: 
        # 사이클 구성 노드 수 세기
        temp = next_node
        while temp != node:
            count += 1
            temp = choices[temp]
        count += 1  # 자기 자신까지 포함

    path[node] = False  

t = int(input())
for _ in range(t):
    n = int(input())
    choices = [0] + list(map(int, input().split()))  # 1-based index
    visited = [False] * (n + 1)
    path = [False] * (n + 1)
    count = 0  # 팀을 이룬 사람 수

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    print(n - count)  
