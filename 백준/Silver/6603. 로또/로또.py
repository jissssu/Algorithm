import sys
input = sys.stdin.read

def dfs(start, path, numbers, results):
    # 6개 뽑았으면 저장
    if len(path) == 6:
        results.append(path[:]) 
        return
    for i in range(start, len(numbers)):
        path.append(numbers[i])
        dfs(i + 1, path, numbers, results)
        path.pop()  

data = input().splitlines()

for line in data:
    if line == '0':
        break
    tokens = list(map(int, line.strip().split()))
    k, nums = tokens[0], tokens[1:]

    results = []
    dfs(0, [], nums, results)


    for comb in results:
        print(' '.join(map(str, comb)))
    print()  
