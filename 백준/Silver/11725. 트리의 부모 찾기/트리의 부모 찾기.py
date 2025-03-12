import sys
from collections import deque
input = sys.stdin.readline


N = int(sys.stdin.readline().strip())  
tree = [[] for _ in range(N + 1)] 
parent = [0] * (N + 1)  


for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)  
    # 양방향 그래프


def bfs(start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for child in tree[node]:  
            if parent[child] == 0: 
                parent[child] = node 
                queue.append(child)  

bfs(1) 


for i in range(2, N + 1):
    print(parent[i])
