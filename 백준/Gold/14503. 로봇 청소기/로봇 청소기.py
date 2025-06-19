N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]
cleaned = [[0]*M for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

count = 0

while True:
    # 1. 현재 칸 청소
    if cleaned[r][c] == 0:
        cleaned[r][c] = 1
        count += 1

    cleaned_flag = False

    # 2. 주변 4칸 탐색
    for i in range(4):
        # 반시계 방향으로 회전
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]

        # 청소되지 않은 빈 칸이면 이동
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0 and cleaned[nr][nc] == 0:
            r, c = nr, nc
            cleaned_flag = True
            break

    if not cleaned_flag:
        # 후진 방향
        back_d = (d + 2) % 4
        r -= dr[d]
        c -= dc[d]
        
        if room[r][c] == 1:
            break

print(count)
