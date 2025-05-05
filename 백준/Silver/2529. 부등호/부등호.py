k = int(input())
signs = input().split()

visited = [False] * 10  # 0~9 숫자 사용 여부
results = []

def check(i, j, op): 
    if op == '<':
        return i < j
    if op == '>':
        return i > j
    return False

def dfs(depth, path):
    if depth == k + 1:
        results.append(''.join(map(str, path)))
        return

    for num in range(10):
        if not visited[num]:
            if depth == 0 or check(path[-1], num, signs[depth - 1]):
                visited[num] = True
                dfs(depth + 1, path + [num])
                visited[num] = False 

dfs(0, [])

results.sort()
print(results[-1])  # 최대값
print(results[0])   # 최소값
