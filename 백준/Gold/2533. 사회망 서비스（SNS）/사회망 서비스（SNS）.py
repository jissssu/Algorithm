import sys
from collections import deque

def main():
    n = int(sys.stdin.readline())
    
    # 트리가 1개 노드인 경우
    if n == 1:
        print(1)
        return
    
    # 그래프 구성
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # DP 테이블
    dp = [[0, 0] for _ in range(n + 1)]
    
    # 반복적 DFS를 위한 스택
    stack = [(1, -1, 0)] 
    
    while stack:
        node, parent, phase = stack.pop()
        
        if phase == 0:
            # 처음 방문 시 초기화
            dp[node][0] = 0
            dp[node][1] = 1
            
            # 자식 처리 후 돌아올 표시
            stack.append((node, parent, 1))
            
            # 모든 자식을 스택에 추가
            for child in graph[node]:
                if child != parent:
                    stack.append((child, node, 0))
        
        else:  
            for child in graph[node]:
                if child != parent:
                    dp[node][0] += dp[child][1]
                    dp[node][1] += min(dp[child][0], dp[child][1])
    

    print(min(dp[1][0], dp[1][1]))

if __name__ == "__main__":
    main()