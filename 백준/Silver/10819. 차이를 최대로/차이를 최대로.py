n = int(input())
a = list(map(int, input().split()))

visited = [False] * n   
path = []             
max_result = 0          

# 순열을 직접 생성하면서 최대값 계산
def dfs():
    global max_result


    if len(path) == n:
        total = 0
        for i in range(n - 1):
            total += abs(path[i] - path[i + 1])
        max_result = max(max_result, total)
        return

    for i in range(n):
        if not visited[i]:    
            visited[i] = True  
            path.append(a[i])  
            dfs()              
            path.pop()         
            visited[i] = False  

dfs()
print(max_result)
