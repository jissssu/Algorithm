from itertools import combinations
from collections import deque
import copy


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empties = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]
# 2(바이러스) 위치 저장
viruses = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 2]

def spread_virus(temp_map):
    q = deque(viruses)
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and temp_map[nx][ny] == 0:
                temp_map[nx][ny] = 2
                q.append((nx, ny))

def count_safe_area(temp_map):
    return sum(row.count(0) for row in temp_map)

max_safe = 0

# 벽 3개 조합 선택
for walls in combinations(empties, 3):
    temp_map = copy.deepcopy(lab)
    for x, y in walls:
        temp_map[x][y] = 1
    spread_virus(temp_map)
    # 안전 영역 크기 세기
    safe = count_safe_area(temp_map)
    max_safe = max(max_safe, safe)


print(max_safe)
