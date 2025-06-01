from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0] * w)
time = 0
current_weight = 0

for truck in trucks:
    while True:
        time += 1
        removed = bridge.popleft()
        current_weight -= removed

        # 트럭을 올릴 수 있는지 확인
        if current_weight + truck <= L:
            bridge.append(truck)
            current_weight += truck
            break
        else:
            bridge.append(0)  
time += w

print(time)
