from itertools import combinations
from collections import deque


board = [input().strip() for _ in range(5)]
answer = 0
positions = [(i, j) for i in range(5) for j in range(5)]

def is_connected_and_valid(group):
    # BFS로 연결되어 있는지 확인
    q = deque([group[0]])
    visited = [group[0]]
    count_s = 0
    if board[group[0][0]][group[0][1]] == 'S':
        count_s += 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in group and (nx, ny) not in visited:
                visited.append((nx, ny))
                q.append((nx, ny))
                if board[nx][ny] == 'S':
                    count_s += 1
    return len(visited) == 7 and count_s >= 4

for comb in combinations(positions, 7):
    if is_connected_and_valid(comb):
        answer += 1

print(answer)
