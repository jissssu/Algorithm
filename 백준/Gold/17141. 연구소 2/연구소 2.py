from collections import deque
from itertools import combinations

def solve():
    N, M = map(int, input().split())
    lab = []
    for _ in range(N):
        row = list(map(int, input().split()))
        lab.append(row)
    
    # 바이러스를 놓을 수 있는 위치들 찾기
    virus_positions = []
    empty_count = 0
    
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 2:
                virus_positions.append((i, j))
                empty_count += 1  # 바이러스 놓을 수 있는 칸도 빈 칸으로 계산
            elif lab[i][j] == 0:
                empty_count += 1
    
   
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def bfs(selected_positions):
        # 거리 배열 초기화
        dist = [[-1] * N for _ in range(N)]
        queue = deque()
        
        # 선택된 바이러스 위치들을 큐에 추가하고 거리를 0으로 설정
        for pos in selected_positions:
            queue.append(pos)
            dist[pos[0]][pos[1]] = 0
        
        max_time = 0
        infected_count = len(selected_positions)
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # 범위 체크
                if 0 <= nx < N and 0 <= ny < N:
                    # 벽이 아니고 아직 방문하지 않은 곳
                    if lab[nx][ny] != 1 and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))
                        infected_count += 1
                        max_time = max(max_time, dist[nx][ny])
        
       
        if infected_count == empty_count:
            return max_time
        else:
            return float('inf')
    
   
    min_time = float('inf')
    
    for selected in combinations(virus_positions, M):
        time = bfs(selected)
        min_time = min(min_time, time)
    
  
    if min_time == float('inf'):
        print(-1)
    else:
        print(min_time)

solve()