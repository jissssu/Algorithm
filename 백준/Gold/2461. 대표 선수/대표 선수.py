import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

students = []
for i in range(N):
    abilities = list(map(int, input().split()))
    for ab in abilities:
        students.append((ab, i))  
students.sort()  

count = defaultdict(int)
total_class = 0  # 현재 윈도우 안에 포함된 반의 수
min_diff = float('inf')

left = 0
for right in range(len(students)):
    ab, cls = students[right]
    count[cls] += 1
    if count[cls] == 1:
        total_class += 1

    # 모든 반이 포함되어 있다면 왼쪽 포인터 이동
    while total_class == N:
        curr_diff = students[right][0] - students[left][0]
        min_diff = min(min_diff, curr_diff)

        count[students[left][1]] -= 1
        if count[students[left][1]] == 0:
            total_class -= 1
        left += 1

print(min_diff)
