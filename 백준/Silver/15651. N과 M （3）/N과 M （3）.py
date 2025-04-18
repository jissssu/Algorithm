import sys
input = sys.stdin.readline

n, m = map(int, input().split())

answer = []

def dfs(numbers):
    if len(numbers) == m:
        answer.append(numbers)
        return
    
    for i in range(1, n + 1):  # 중복 허용
        dfs(numbers + [i])

dfs([])


for ans in answer:
    for num in ans:
        print(num, end=" ")
    print()
