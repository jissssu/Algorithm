import sys

input = sys.stdin.readline

n, m = map(int,input().split())

answer = []

visited = [False]*(n+1)

def dfs(numbers):
    
    if len(numbers) == m:
        answer.append(numbers)
        return
    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            dfs(numbers+[i])
            visited[i] = False

dfs([])

for ans in answer:
    for n in ans:
        print(n,end=" ")
    print()