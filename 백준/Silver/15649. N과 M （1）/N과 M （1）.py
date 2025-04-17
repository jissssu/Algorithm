import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n+1)
sequence = []

def dfs():
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            sequence.append(i)
            dfs()
            visited[i] = False
            sequence.pop()

dfs()