from collections import deque

gears = [deque(input().strip()) for _ in range(4)]

K = int(input()) 

def rotate(idx, direction):
    if direction == 1:  # 시계 방향
        gears[idx].appendleft(gears[idx].pop())
    else: 
        gears[idx].append(gears[idx].popleft())

for _ in range(K):
    num, dir = map(int, input().split())
    num -= 1  # index 

    directions = [0] * 4
    directions[num] = dir

    for i in range(num, 0, -1):
        if gears[i][6] != gears[i-1][2]:
            directions[i-1] = -directions[i]
        else:
            break


    for i in range(num, 3):
        if gears[i][2] != gears[i+1][6]:
            directions[i+1] = -directions[i]
        else:
            break

    for i in range(4):
        if directions[i] != 0:
            rotate(i, directions[i])

score = 0
if gears[0][0] == '1': score += 1
if gears[1][0] == '1': score += 2
if gears[2][0] == '1': score += 4
if gears[3][0] == '1': score += 8

print(score)
