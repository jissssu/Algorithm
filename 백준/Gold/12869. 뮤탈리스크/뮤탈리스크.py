from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
hp = list(map(int, input().split()))
while len(hp) < 3:
    hp.append(0)

# 가능한 데미지 분배 6가지
dmg = [
    (9, 3, 1), (9, 1, 3),
    (3, 9, 1), (3, 1, 9),
    (1, 9, 3), (1, 3, 9)
]

# visited[a][b][c] : 이미 방문한 체력 상태
visited = [[[False]*61 for _ in range(61)] for _ in range(61)]

def normalize(a, b, c):
    """내림차순 정렬된 튜플 반환"""
    return tuple(sorted((max(0, a), max(0, b), max(0, c)), reverse=True))

start = normalize(*hp)
q = deque([(start, 0)])  # (상태, 사용한 공격 횟수)
visited[start[0]][start[1]][start[2]] = True

while q:
    (a, b, c), cnt = q.popleft()
    if a == b == c == 0:      
        print(cnt)
        break
    for da, db, dc in dmg:
        na, nb, nc = normalize(a - da, b - db, c - dc)
        if not visited[na][nb][nc]:
            visited[na][nb][nc] = True
            q.append(((na, nb, nc), cnt + 1))
