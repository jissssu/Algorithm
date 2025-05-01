import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

sequence = []
result = set()  # 중복 제거용

def dfs():
    if len(sequence) == m:
        result.add(tuple(sequence))  # 리스트는 set에 못 들어가니 튜플로 변환
        return

    for i in range(n):
        sequence.append(nums[i])
        dfs()
        sequence.pop()

dfs()


for seq in sorted(result):
    print(*seq)
