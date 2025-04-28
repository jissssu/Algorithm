import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()  
sequence = []

def dfs(start, depth):
    if depth == m:
        print(' '.join(map(str, sequence)))
        return
    
    prev = 0  
    for i in range(start, n):
        if prev != nums[i]:  # 이전에 선택한 숫자와 다른 경우에만 진행
            sequence.append(nums[i])
            dfs(i + 1, depth + 1)  # 같은 숫자 중복 선택 방지 위해 i+1로 다음 위치부터 탐색
            sequence.pop()
            prev = nums[i]  

dfs(0, 0)