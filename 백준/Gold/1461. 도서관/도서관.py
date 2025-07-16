N, M = map(int, input().split())
positions = list(map(int, input().split()))

positive = []
negative = []

for pos in positions:
    if pos > 0:
        positive.append(pos)
    else:
        negative.append(pos)
positive.sort(reverse=True)
negative.sort()

total_steps = 0
max_distance = 0

# 양수 위치 처리 (가장 먼 곳부터 M권씩)
for i in range(0, len(positive), M):
    distance = positive[i]  
    total_steps += distance * 2  
    max_distance = max(max_distance, distance)

# 음수 위치 처리 (가장 먼 곳부터 M권씩)
for i in range(0, len(negative), M):
    distance = abs(negative[i]) 
    total_steps += distance * 2 
    max_distance = max(max_distance, distance)
total_steps -= max_distance

print(total_steps)