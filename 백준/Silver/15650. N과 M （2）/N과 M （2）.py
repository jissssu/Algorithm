import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def dfs(start, numbers):
    if len(numbers) == m:
        print(' '.join(map(str, numbers)))
        return
    
    for i in range(start, n + 1):
        dfs(i + 1, numbers + [i])


dfs(1, [])
