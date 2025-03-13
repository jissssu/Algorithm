from collections import deque

F, S, G, U, D = map(int, input().split())


def bfs(s, e):
    q = deque()
    v = [0] * (F + 1) 
    q.append(s)
    v[s] = 1  
    
    while q:
        c = q.popleft()
        if c == e:
            return v[c] - 1  
        
        for i in range(2):
            if i == 0:
                n = c + U  # 위로 U층 가는 경우
            else:
                n = c - D  # 아래로 D층 가는 경우

            if 1 <= n <= F and v[n] == 0:  # 범위 내에 있고, 아직 방문하지 않았다면
                q.append(n)
                v[n] = v[c] + 1  # 현재 층에서 한 번 더 이동한 횟수 기록

    # 목적지에 도달할 수 없는 경우
    return 'use the stairs'

ans = bfs(S, G)
print(ans)
