from itertools import combinations
import sys
import copy

# 입력 받기
n = int(input())
graph = []
teachers = []
spaces = []

for i in range(n):
    row = input().split()
    graph.append(row)
    for j in range(n):
        if row[j] == 'T':
            teachers.append((i, j))
        elif row[j] == 'X':
            spaces.append((i, j))

# 감시 함수: 특정 방향으로 학생을 감시할 수 있는지
def watch(x, y, dx, dy, temp):
    while 0 <= x < n and 0 <= y < n:
        if temp[x][y] == 'O':  # 장애물
            return False
        if temp[x][y] == 'S':  # 학생 발견
            return True
        x += dx
        y += dy
    return False

# 감시 시뮬레이션 함수
def process(temp):
    for x, y in teachers:
        # 상, 하, 좌, 우 네 방향 감시
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            if watch(x, y, dx, dy, temp):
                return True  # 학생이 감시에 걸림
    return False  # 모든 감시에도 학생이 안 걸림

# 모든 조합에 대해 시도
found = False
for obstacles in combinations(spaces, 3):
    temp = copy.deepcopy(graph)
    for x, y in obstacles:
        temp[x][y] = 'O'
    if not process(temp):  # 감시에 아무도 안 걸림
        found = True
        break

print("YES" if found else "NO")
