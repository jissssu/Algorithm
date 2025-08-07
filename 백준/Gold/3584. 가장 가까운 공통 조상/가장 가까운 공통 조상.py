import sys
import sys
sys.setrecursionlimit(100000)

def find_parent_and_depth(node, parent, depth, tree, parents, depths):
    parents[node] = parent
    depths[node] = depth
    for child in tree[node]:
        if child != parent:
            find_parent_and_depth(child, node, depth + 1, tree, parents, depths)

def lca(u, v, parents, depths):
    while depths[u] > depths[v]:
        u = parents[u]
    while depths[v] > depths[u]:
        v = parents[v]
    # 공통 조상 찾기
    while u != v:
        u = parents[u]
        v = parents[v]
    return u

T = int(input())
for _ in range(T):
    N = int(input())
    
    tree = [[] for _ in range(N + 1)]
    parent_check = [0] * (N + 1)

    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
        parent_check[b] += 1
    
    root = parent_check.index(0, 1)

    parents = [0] * (N + 1)
    depths = [0] * (N + 1)

 
    find_parent_and_depth(root, 0, 0, tree, parents, depths)

    u, v = map(int, input().split())
    print(lca(u, v, parents, depths))
