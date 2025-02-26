import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))

    count = 1
    while (True):
        if (queue[0] == max(queue)):
            if (M == 0):
                print(count)
                break
            else:
                queue.popleft()
                
            count += 1
        else:
            queue.append(queue.popleft())
        
        M -= 1
        if (M < 0):
            M = len(queue) - 1