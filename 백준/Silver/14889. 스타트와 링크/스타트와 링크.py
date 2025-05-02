import sys
from itertools import combinations

input = sys.stdin.readline

# 입력
n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]

min_diff = float('inf')  # 아주 큰 값으로 초기화

people = list(range(n))

# 팀을 절반으로 나누는 조합 구하기
for start_team in combinations(people, n // 2):
    link_team = list(set(people) - set(start_team))

    start_score = 0
    link_score = 0

    # 각 팀의 능력치 계산
    for i in range(n // 2):
        for j in range(n // 2):
            if i == j:
                continue
            start_score += S[start_team[i]][start_team[j]]
            link_score += S[link_team[i]][link_team[j]]

    diff = abs(start_score - link_score)
    min_diff = min(min_diff, diff)

    # 차이가 0이면 최소이므로 바로 종료 가능
    if min_diff == 0:
        break

print(min_diff)
