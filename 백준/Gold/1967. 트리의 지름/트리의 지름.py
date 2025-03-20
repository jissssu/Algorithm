import sys
sys.setrecursionlimit(100000)  # 재귀 제한을 늘려줘요

input = sys.stdin.readline  # 입력을 빠르게 받기 위해 변경했어요
n = int(input())  # 노드의 개수를 입력받아요

# 트리를 저장할 리스트를 만들어요
tree = [[] for _ in range(n + 1)]

# 트리의 간선 정보를 입력받아요
for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))  # 양방향으로 저장해야 해요

# 첫 번째 DFS: 임의의 노드(여기서는 1번)에서 가장 먼 노드를 찾아요
def dfs1(node, distance):
    visited = [False] * (n + 1)
    stack = [(node, distance)]
    visited[node] = True
    max_distance = 0
    farthest_node = node
    
    while stack:
        current, current_distance = stack.pop()
        
        if current_distance > max_distance:
            max_distance = current_distance
            farthest_node = current
        
        for next_node, weight in tree[current]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node, current_distance + weight))
    
    return farthest_node, max_distance

# 두 번째 DFS: 첫 번째 DFS에서 찾은 가장 먼 노드에서 다시 가장 먼 노드를 찾아요
def dfs2(node):
    visited = [False] * (n + 1)
    stack = [(node, 0)]
    visited[node] = True
    max_distance = 0
    
    while stack:
        current, current_distance = stack.pop()
        
        max_distance = max(max_distance, current_distance)
        
        for next_node, weight in tree[current]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node, current_distance + weight))
    
    return max_distance

# 첫 번째 DFS로 가장 먼 노드를 찾아요
farthest_node, _ = dfs1(1, 0)

# 두 번째 DFS로 트리의 지름을 구해요
diameter = dfs2(farthest_node)

print(diameter)  # 트리의 지름을 출력해요