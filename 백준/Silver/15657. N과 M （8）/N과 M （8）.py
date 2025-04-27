import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

sequence = []

def dfs(start):
    if len(sequence) == m:
        print(*sequence)
        return
    
    for i in range(start, n):
        sequence.append(nums[i])
        dfs(i)  # 다시 i부터 
        sequence.pop()

dfs(0)
