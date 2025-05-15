import heapq
import sys

input = sys.stdin.read
data = input().split()

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

index = 0
problem_count = 1

while True:
    N = int(data[index])
    index += 1
    if N == 0:
        break

    cave = []
    for _ in range(N):
        row = list(map(int, data[index:index+N]))
        cave.append(row)
        index += N

    # 최소 비용 저장 배열
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = cave[0][0]

    # (비용, x좌표, y좌표)
    heap = [(cave[0][0], 0, 0)]

    while heap:
        cost, x, y = heapq.heappop(heap)

        if x == N - 1 and y == N - 1:
            break

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                new_cost = cost + cave[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))

    print(f"Problem {problem_count}: {dist[N-1][N-1]}")
    problem_count += 1
