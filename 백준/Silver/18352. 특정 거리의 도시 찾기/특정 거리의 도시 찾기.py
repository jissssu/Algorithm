from collections import deque
import sys
input = sys.stdin.read

def find_cities_at_distance_k(N, M, K, X, roads_info):
    roads = [[] for _ in range(N+1)]
    visited = [-1] * (N+1)
    
    for a, b in roads_info:
        roads[a].append(b)
    
    queue = deque([X])
    visited[X] = 0
    
    while queue:
        current_city = queue.popleft()
        for next_city in roads[current_city]:
            if visited[next_city] == -1:
                visited[next_city] = visited[current_city] + 1
                queue.append(next_city)
    
    cities = [i for i in range(1, N+1) if visited[i] == K]
    
    if cities:
        return sorted(cities)
    else:
        return [-1]

if __name__ == "__main__":
    input_data = input().strip().split()
    N = int(input_data[0])
    M = int(input_data[1])
    K = int(input_data[2])
    X = int(input_data[3])
    
    roads_info = []
    for i in range(M):
        a = int(input_data[4 + 2 * i])
        b = int(input_data[5 + 2 * i])
        roads_info.append((a, b))
    
    result = find_cities_at_distance_k(N, M, K, X, roads_info)
    for city in result:
        print(city)
