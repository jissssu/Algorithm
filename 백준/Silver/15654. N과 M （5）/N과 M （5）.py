import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()  

visited = [False] * n 
answer = []

def dfs(path):
    if len(path) == m:
        answer.append(path[:])
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(path + [nums[i]])
            visited[i] = False  # 백트래킹

dfs([])

for seq in answer:
    print(' '.join(map(str, seq)))
