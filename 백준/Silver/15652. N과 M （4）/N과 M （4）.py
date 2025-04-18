import sys
input = sys.stdin.readline

n, m = map(int, input().split())

answer = []

def dfs(start, numbers):
    if len(numbers) == m:
        answer.append(numbers)
        return

    for i in range(start, n + 1): 
        dfs(i, numbers + [i])  

dfs(1, [])

for ans in answer:
    for num in ans:
        print(num, end=" ")
    print()
